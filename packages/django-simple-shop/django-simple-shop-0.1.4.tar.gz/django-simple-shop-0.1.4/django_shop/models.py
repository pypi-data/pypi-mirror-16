# coding=utf8
from __future__ import unicode_literals, absolute_import

import json
import uuid
from operator import attrgetter
from decimal import Decimal

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models, transaction
from django.db.models import Sum, Q
from django.utils.functional import cached_property
from phonenumber_field.modelfields import PhoneNumberField

from .utils import delivery
from .utils.payment import create_payment, get_payment


class ProductCategory(models.Model):
    """Товарная категория, содержит в себе товары одного типа"""

    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='categories/%Y/',
                              verbose_name='Изображение')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name

    def products_ordered(self):
        """Получить упорядоченный по убыванию доступного остатка список товара
        в категории.

        В список попадают только те товары, которые есть в наличии или помечены
        как отображающиеся всегда.

        :rtype: list[Product]
        """
        qs = self.products.get_available()
        return sorted(qs, key=lambda x: x.entries__quantity__sum or 0,
                      reverse=True)

    @cached_property
    def has_products(self):
        """Свойство: есть ли продукты в категории"""
        return self.products.exists()

    @cached_property
    def has_in_stock(self):
        """Свойство: количество продуктов в наличии в категории"""
        in_stock = self.products.filter(entries__quantity__gte=0).aggregate(
            Sum('entries__quantity')).get('entries__quantity__sum') or 0
        return in_stock

    @cached_property
    def have_to_display(self):
        """Свойство: нужно ли отобразить категорию в списке"""
        return self.products.get_available().exists()


class ProductCategoryCustomField(models.Model):
    """"""
    TYPE_BOOLEAN = 1
    TYPE_INTEGER = 2
    TYPE_DECIMAL = 3
    TYPE_STRING = 4
    FIELD_TYPE_CHOICES = (
        (TYPE_BOOLEAN, 'Да/Нет'),
        (TYPE_INTEGER, 'Целое число'),
        (TYPE_DECIMAL, 'Дробное число'),
        (TYPE_STRING, 'Строка до 500 символов'),
    )

    key = models.CharField('Название', max_length=200)
    type = models.IntegerField('Тип значения', choices=FIELD_TYPE_CHOICES)
    required = models.BooleanField('Обязательное поле', default=False)
    category = models.ForeignKey(ProductCategory, verbose_name='Категория',
                                 related_name='fields')

    class Meta:
        verbose_name = 'дополнительное поле'
        verbose_name_plural = 'дополнительные поля'

    def __str__(self):
        return '{}({})'.format(self.key, self.get_type_display())


class ProductManager(models.Manager):
    def get_available(self):
        return self.annotate(Sum('entries__quantity')).filter(
            Q(is_unlimited=True) | Q(always_visible=True) |
            Q(entries__quantity__sum__gt=0))


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(ProductCategory, verbose_name='Категория',
                                 related_name='products')
    price = models.DecimalField(max_digits=9, decimal_places=2,
                                verbose_name='Цена')
    is_unlimited = models.BooleanField(
        'Количество неорганичено', default=False,
        help_text='Если количество товара неограничено - для него не нужно '
                  'заводить поставки'
    )
    is_weight = models.BooleanField(
        default=False, verbose_name='Весовой товар',
        help_text='Весовой товар - это товар, которого можно приобрести '
                  'дробное количество'
    )
    weight = models.IntegerField(
        verbose_name='Вес',
        help_text='Масса единицы товара в упаковке (брутто) в граммах, '
                  'нужна для расчета стоимости доставки')
    measure = models.CharField(
        max_length=10, verbose_name='Единица измерения', blank=True,
        help_text='Обязательно заполнить, если товар весовой'
    )
    short_description = models.TextField(
        verbose_name='Короткое описание', blank=True,
        help_text='Описание, состоящее из одного абзаца текста, помещается '
                  'рядом с картинкой товара в каталоге.'
    )
    description = models.TextField(
        verbose_name='Полное описание',
        help_text='Полное описание продукта, будет показано в его карточке.'
    )
    always_visible = models.BooleanField(
        'Виден всегда', default=False,
        help_text='Включите, если товар должен отображаться, даже если его '
                  'нет в наличии')

    objects = ProductManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    @cached_property
    def primary_image(self):
        """Основное по приоритету изображение товара"""
        try:
            return self.images.order_by('priority')[0].image
        except IndexError:
            return 'placeholder.jpg'

    @cached_property
    def in_stock(self):
        """Количество незабронированного товара на складе"""
        stock_amount = self.entries.filter(quantity__gt=0).aggregate(Sum('quantity')).get('quantity__sum') or 0
        reserved = self.orders.filter(order__state=Order.STATE_CREATED).aggregate(
            Sum('quantity')).get('quantity__sum') or 0
        if reserved > stock_amount:
            return 0
        return stock_amount - reserved
    in_stock.short_description = 'В наличии'

    def build_images(self):
        images = self.images.order_by('priority')
        images_count = len(images)
        if not images_count:
            return 0, 'placeholder.jpg', []
        primary_image = images[0].image
        return images_count, primary_image, (x.image for x in images[1:])

    def get_absolute_url(self):
        return reverse('shop:product', kwargs={'cat_slug': self.category.slug,
                                               'slug': self.slug})


class ProductCustomFieldValue(models.Model):
    product = models.ForeignKey(Product, related_name='custom_fields')
    field = models.ForeignKey(ProductCategoryCustomField,
                              related_name='values')
    value = models.CharField(max_length=550)


class ProductImage(models.Model):
    image = models.ImageField(
        upload_to='products/%Y/', verbose_name='Изображение',
        help_text='Изображение должно быть больше 600 пикселей по ширине'
    )
    priority = models.PositiveSmallIntegerField(
        verbose_name='Приоритет',
        help_text='Чем меньше это число, тем раньше будет отображено '
                  'изображение'
    )
    product = models.ForeignKey(Product, related_name='images')

    class Meta:
        verbose_name = 'изображение продукта'
        verbose_name_plural = 'изображения продукта'
        ordering = ['priority']


class ProductEntry(models.Model):
    """Поставка товара на складе"""
    product = models.ForeignKey(Product, related_name='entries')
    quantity = models.DecimalField('Количество', max_digits=9,
                                   decimal_places=2)
    price = models.DecimalField(max_digits=9, decimal_places=2,
                                verbose_name='Стоимость')
    date = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'поставка продукта'
        verbose_name_plural = 'поставки продукта'
        ordering = ['date']

    def __str__(self):
        return self.date.strftime('%c')


class PaymentType(models.Model):
    """Модель, задающая поддерживаемые магазином способы оплаты товара"""
    TYPE_OFFLINE = 1
    TYPE_ONLINE = 2
    TYPE_CHOICES = (
        (TYPE_OFFLINE, 'Оплата при получении'),
        (TYPE_ONLINE, 'Оплата онлаин')
    )

    name = models.CharField(
        max_length=200, verbose_name='Название',
        help_text='Короткое название способа оплаты'
    )
    description = models.TextField(
        verbose_name='Описание', blank=True,
        help_text='Короткое (в одно-два предложения) описание способа оплаты'
    )
    payment_type = models.IntegerField(
        verbose_name='Тип оплаты', choices=TYPE_CHOICES
    )
    payment_hook = models.CharField(
        verbose_name='Конкретный тип онлайн оплаты', max_length=50, blank=True
    )
    is_active = models.BooleanField(
        verbose_name='Используется', default=True,
        help_text='С помощью этой опции можно временно отключить способ '
                  'оплаты'
    )

    class Meta:
        verbose_name = 'способ оплаты'
        verbose_name_plural = 'способы оплаты'

    def __str__(self):
        return self.name

    def create_payment(self, order):
        """Создать объект платежа в Яндекс.Кассе если это нужно

        :type order: Order

        :rtype: yandex_money.models.Payment or None
        """
        if self.payment_type != self.TYPE_ONLINE:
            return

        return create_payment(self.payment_hook, order)

    def get_payment(self, order):
        if self.payment_type != self.TYPE_ONLINE:
            return

        return get_payment(self.payment_hook, order)


class DeliveryType(models.Model):
    """Модель, задающая поддерживаемые магазином способы доставки товара до
    покупателя"""

    SELECT_FULL = 'full'
    SELECT_LOCAL = 'local'
    SELECT_CONTACTS = 'contacts'
    SELECT_WIDGET = 'widget'
    ADDRESS_SELECT = (
        (SELECT_FULL, 'Ввод полного адреса'),
        (SELECT_LOCAL, 'Ввод локального адреса'),
        (SELECT_CONTACTS, 'Ввод контактов'),
        (SELECT_WIDGET, 'Ввод c помощью виджета'),
    )

    name = models.CharField(
        max_length=200, verbose_name='Название',
        help_text='Короткое название способа доставки'
    )
    description = models.TextField(
        verbose_name='Описание', blank=True,
        help_text='Короткое (в одно-два предложения) описание способа доставки'
    )
    pricing_method = models.CharField(
        verbose_name='Определение цены', max_length=30,
        choices=delivery.PRICING_METHODS,
        help_text='Способ вычисления цены доставки'
    )
    delivery_hook = models.CharField(
        verbose_name='Метод определения цены', max_length=30, blank=True,
        help_text='Задайте, если для получения цены и определения адреса '
                  'доставки используется отдельная логика'
    )
    address_select = models.CharField(
        verbose_name='Форма ввода адреса', max_length=30,
        choices=ADDRESS_SELECT, default=SELECT_FULL,
        help_text='Выбор вида отображаемой формы адреса'
    )
    price = models.DecimalField(
        verbose_name='Цена', max_digits=9, decimal_places=2, blank=True,
        null=True,
        help_text='Цена доставки, указывается в случае, если для вычисления '
                  'цены используются методы "Заданная цена" и "Процент от '
                  'стоимости". Во втором случае нужно указать процент от '
                  'суммы покупки, который будет стоить доставка'
    )
    is_active = models.BooleanField(
        verbose_name='Используется', default=True,
        help_text='С помощью этой опции можно временно отключить способ '
                  'доставки'
    )

    class Meta:
        verbose_name = 'способ доставки'
        verbose_name_plural = 'способы доставки'

    def __str__(self):
        return self.name

    def actual_pricing(self):
        if self.pricing_method == delivery.METHOD_FREE:
            return
        elif self.pricing_method == delivery.METHOD_CONSTANT:
            return '{} руб.'.format(self.price)
        elif self.pricing_method == delivery.METHOD_PERCENT:
            return '{}%'.format(self.price)
        elif self.pricing_method == delivery.METHOD_API:
            return 'Цена расчетная'
        else:
            raise NotImplementedError
    actual_pricing.short_description = 'Цена'

    def price_display(self):
        if self.pricing_method == delivery.METHOD_FREE:
            return 'Бесплатно'
        elif self.pricing_method == delivery.METHOD_CONSTANT:
            return '{} &#8381;'.format(self.price)
        elif self.pricing_method == delivery.METHOD_PERCENT:
            return '{}% от стоимости товара'.format(self.price)
        elif self.pricing_method == delivery.METHOD_API:
            return 'Цена расчетная'
        else:
            raise NotImplementedError
    price_display.short_description = 'Цена'

    def get_price_and_address(self, options, address_form, order_price, weight, measures):
        """Получить цену доставки и ее реальный адрес.

        Дополнительные данные о параметрах заказа нужны для засчета реальной цены в службе доставки

        :type options: str
        :param options: дополнительные параметры доставки
        :type address_form: dict[str, ANY]
        :param address_form: Данные об адресе доставки
        :type order_price: decimal.Decimal
        :param order_price: стоимость заказа
        :type weight: int
        :param weight: вес заказа в граммах
        :type measures: (int, int, int)
        :param measures: высота, ширина и глубина коробки, в которой поедет заказ

        :rtype: (decimal.Decimal, dict[str, ANY])
        :return: Цена доставки и ее реальный адрес
        """
        try:
            options = json.loads(options)
        except ValueError:
            options = {}
        options['hook'] = self.delivery_hook
        options['type_price'] = self.price
        return delivery.compute_price_and_address(
            self.pricing_method, options, address_form, order_price, weight, measures)


class DeliveryAddress(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=300)
    email = models.EmailField(verbose_name='Email')
    phone = PhoneNumberField(verbose_name='Телефон')
    address = models.CharField(verbose_name='Адрес', max_length=500, blank=True)
    city = models.CharField(verbose_name='Город/Населенный пункт', max_length=200, blank=True)
    zip_code = models.CharField(verbose_name='Индекс', max_length=20, blank=True)
    province = models.CharField(verbose_name='Регион/Облась', max_length=200, blank=True)
    country = models.CharField(verbose_name='Страна', max_length=200, blank=True)


class Order(models.Model):
    STATE_CREATED = 'Created'
    STATE_CONFIRMED = 'Confirmed'
    STATE_DECLINED = 'Declined'
    STATE_SHIPPED = 'Shipped'
    STATE_DELIVERED = 'Delivered'
    STATE_REJECTED = 'Rejected'
    STATE_NC_CREATED = 'NCCreated'
    STATE_NC_PAID = 'NCPaid'
    STATE_NC_PAY_ERROR = 'NCPayError'
    STATE_NC_CONFIRMED = 'NCConfirmed'
    STATE_NC_DECLINED = 'NCDeclined'
    STATE_NC_SHIPPED = 'NCShipped'
    STATE_NC_DELIVERED = 'NCDelivered'
    STATE_NC_REJECTED = 'NCRejected'
    STATES = (
        (STATE_CREATED, 'Создан'),
        (STATE_CONFIRMED, 'Подтвержден'),
        (STATE_DECLINED, 'Не подтвержден'),
        (STATE_SHIPPED, 'Отправлен'),
        (STATE_DELIVERED, 'Доставлен'),
        (STATE_REJECTED, 'Отказ в получении'),
        (STATE_NC_CREATED, 'Создан (безнал)'),
        (STATE_NC_PAID, 'Оплачен (безнал)'),
        (STATE_NC_PAY_ERROR, 'Ошибка оплаты (безнал)'),
        (STATE_NC_CONFIRMED, 'Подтвержден (безнал)'),
        (STATE_NC_DECLINED, 'Не подтвержден (безнал)'),
        (STATE_NC_SHIPPED, 'Отправлен (безнал)'),
        (STATE_NC_DELIVERED, 'Доставлен (безнал)'),
        (STATE_NC_REJECTED, 'Отказ в получении (безнал)'),
    )
    STATES_DICT = {k: v for k, v in STATES}
    STATES_ORDERS = {
        STATE_CREATED: (STATE_CONFIRMED, STATE_DECLINED),
        STATE_CONFIRMED: (STATE_SHIPPED,),
        STATE_SHIPPED: (STATE_DELIVERED, STATE_REJECTED),
        STATE_NC_CREATED: (STATE_NC_PAY_ERROR,),
        STATE_NC_PAID: (STATE_NC_CONFIRMED, STATE_NC_DECLINED),
        STATE_NC_CONFIRMED: (STATE_NC_SHIPPED,),
        STATE_NC_SHIPPED: (STATE_NC_DELIVERED, STATE_NC_REJECTED),
    }

    uuid = models.UUIDField(verbose_name='Уникальный ключ', default=uuid.uuid4, unique=True, editable=False)
    sid = models.CharField(verbose_name='ID клиента', editable=False, max_length=50)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    changed = models.DateTimeField('Дата изменения', auto_now=True)
    state = models.CharField('Статус', max_length=50, choices=STATES, default=STATE_CREATED)
    delivery_type = models.ForeignKey(DeliveryType, verbose_name='Способ доставки')
    delivery_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Стоимость доставки')
    delivery_address = models.ForeignKey(DeliveryAddress, verbose_name='Адрес доставки', editable=False)
    payment_method = models.ForeignKey(PaymentType, verbose_name='Способ оплаты', editable=False, null=True)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return 'Заказ №{}'.format(self.id)

    def get_absolute_url(self):
        return reverse('shop:order', kwargs={'uuid': self.uuid.hex})

    def get_state_choices(self):
        """Получить возможные варианты выбора статуса из текущего в формате choices"""
        so = [self.state] + list(self.STATES_ORDERS.get(self.state, []))
        return [(s, self.STATES_DICT[s]) for s in so]

    def reduce_stock_amount(self):
        """Списать со склада товар в заказе"""
        for product in self._products.select_for_update():
            product.reduce_stock_amount()

    def _send_customer_mail(self, template):
        subject = 'Ваш заказ получен'
        message = render_to_string(template, {'order': self})
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.delivery_address.email],
                  fail_silently=True)

    def _send_manager_mail(self, template):
        subject = 'Получен заказ на сайте'
        message = render_to_string(template, {'order': self})
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [m[1] for m in settings.MANAGERS],
                  fail_silently=True)

    def send_emails(self):
        """Отправить письма клиентам и менеджерам, если это нужно в текущем статусе"""
        if self.state == self.STATE_CREATED:
            self._send_customer_mail('django_shop/email/order_cash_customer_email.txt')
            self._send_manager_mail('django_shop/email/order_cash_manager_email.txt')
        elif self.state == self.STATE_NC_PAID:
            self._send_customer_mail('django_shop/email/order_nc_customer_email.txt')
            self._send_manager_mail('django_shop/email/order_nc_manager_email.txt')

    def get_payment_complete_url(self, success):
        base_url = self.get_absolute_url()
        if self.payment_finished:
            return base_url
        if success:
            return base_url + '?success=1'
        else:
            return base_url + '?success=0'

    @classmethod
    def get_by_order_id(cls, order_id):
        try:
            return cls.objects.get(uuid=order_id)
        except cls.DoesNotExist:
            return

    @classmethod
    @transaction.atomic
    def from_forms(cls, products_form, order_form, receiver_form, address_form, session_key):
        """Создать заказ из словарей с данными из набора форм"""
        dt = order_form['delivery_type']
        weight = sum(p['product'].weight * p['amount'] for p in products_form)
        order_price = sum(p['product'].price * Decimal(p['amount']) for p in products_form)
        measures = (30, 30, 40)
        price, addr = dt.get_price_and_address(order_form['delivery_options'], address_form,
                                               order_price, weight, measures)

        da = DeliveryAddress.objects.create(
            name=receiver_form['name'], email=receiver_form['email'],
            phone=receiver_form['phone'],
            address=addr.get('address', ''), city=addr.get('city', ''),
            zip_code=addr.get('zip_code', ''), province=addr.get('province', ''),
            country=addr.get('country', '')
        )

        pm = order_form['payment_type']
        state = cls.STATE_CREATED if pm.payment_type == pm.TYPE_OFFLINE else cls.STATE_NC_CREATED

        order = cls.objects.create(delivery_type=dt, delivery_price=price,
                                   delivery_address=da, sid=session_key,
                                   payment_method=pm, state=state)

        for pf in products_form:
            ProductOrder.objects.create(
                product=pf['product'], order=order, quantity=pf['amount'],
                price=pf['product'].price * Decimal(pf['amount'])
            )

        payment = pm.create_payment(order)
        order.payment = payment
        order.save()

        return order

    @cached_property
    def payment(self):
        """Объект платежа"""
        if self.payment_method is None:
            return None
        return self.payment_method.get_payment(self)

    @cached_property
    def payment_finished(self):
        """Платеж закончен (успешно или нет)"""
        if self.payment is None:
            return False
        return self.payment.is_completed

    @cached_property
    def payment_done(self):
        """Заказ успешно оплачен"""
        if self.payment is None:
            return False
        return self.payment.is_payed
    payment_done.boolean = True
    payment_done.short_description = 'Заказ оплачен'

    @cached_property
    def _products(self):
        ps = self.products.select_related('product')
        list(ps)
        return ps

    @cached_property
    def price(self):
        """Полная цена заказа без доставки"""
        return sum(map(attrgetter('price'), self._products))
    price.short_description = 'Стоимость товара'

    @cached_property
    def full_price(self):
        """Полная цена заказа с доставкой"""
        return self.price + self.delivery_price
    full_price.short_description = 'К оплате'

    @cached_property
    def products_string(self):
        products_data = []
        for product in self._products:
            if product.product.is_weight:
                measure = product.product.measure
            else:
                measure = 'шт'
            products_data.append(' - {} ({:.1} {});'.format(
                product.product.name, product.quantity, measure))
        return '\n'.join(products_data)
    products_string.short_description = 'Заказ'

    @cached_property
    def receiver(self):
        address_data = []
        for field in self.delivery_address._meta.fields:
            if field.name == 'id':
                continue
            data = getattr(self.delivery_address, field.name)
            if not data:
                continue
            address_data.append('{}: {}'.format(field.verbose_name, data))
        return '\n'.join(address_data)
    receiver.short_description = 'Информация о получателе'

    def process_payment(self):
        if self.state in (self.STATE_NC_CREATED, self.STATE_NC_PAY_ERROR):
            self.state = self.STATE_NC_PAID
            self.save()

            self.reduce_stock_amount()
            self.send_emails()

    def process_payment_fail(self):
        if self.state == self.STATE_NC_CREATED:
            self.state = self.STATE_NC_PAY_ERROR
            self.save()

            self.reduce_stock_amount()


class ProductOrder(models.Model):
    """Товарная позиция в заказе"""

    product = models.ForeignKey(Product, related_name='orders')
    order = models.ForeignKey(Order, related_name='products')
    quantity = models.DecimalField('Количество', max_digits=9,
                                   decimal_places=2)
    price = models.DecimalField(max_digits=9, decimal_places=2,
                                verbose_name='Стоимость')
    stock_reduced = models.BooleanField(default=False, editable=False)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return str(self.product)

    @transaction.atomic
    def reduce_stock_amount(self):
        """Списать из доступного для продажи остатка количество товара в
        позиции
        """
        if self.stock_reduced:
            raise RuntimeError('Stock amount had already been reduced')

        if not self.product.is_unlimited:
            qs = self.product.entries.filter(
                quantity__gt=0).select_for_update()
            stock_amount = qs.aggregate(
                Sum('quantity')).get('quantity__sum') or 0

            if stock_amount < self.quantity:
                raise RuntimeError(
                    'На складе меньше товара, чем нужно (%s < %s)',
                    stock_amount, self.quantity)

            current_quantity = self.quantity

            for entry in qs:
                if entry.quantity >= current_quantity:
                    entry.quantity -= current_quantity
                    current_quantity = 0
                else:
                    current_quantity -= entry.quantity
                    entry.quantity = 0

                entry.save()
                if not current_quantity:
                    break

        self.stock_reduced = True
        self.save()
