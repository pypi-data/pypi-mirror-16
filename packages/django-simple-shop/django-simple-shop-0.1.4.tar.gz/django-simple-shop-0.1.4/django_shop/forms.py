from __future__ import unicode_literals, absolute_import

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from phonenumber_field.formfields import PhoneNumberField

from .models import Product, DeliveryType, PaymentType


class CartModifyForm(forms.Form):
    """Форма для изменения корзины в POST запросе"""
    ACTION_ADD = 'add'
    ACTION_REMOVE = 'remove'
    ACTION_SET = 'set'
    ACTIONS = (
        (ACTION_ADD, ACTION_ADD),
        (ACTION_REMOVE, ACTION_REMOVE),
        (ACTION_SET, ACTION_SET)
    )

    RESPONSE_FULL = 'full'
    RESPONSE_MINIMAL = 'minimal'
    RESPONSES = (
        (RESPONSE_FULL, RESPONSE_FULL),
        (RESPONSE_MINIMAL, RESPONSE_MINIMAL),
    )

    action = forms.ChoiceField(choices=ACTIONS)
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    amount = forms.DecimalField(min_value=0.1, required=False,
                                decimal_places=1)
    response = forms.ChoiceField(choices=RESPONSES)

    def clean_amount(self):
        if self.cleaned_data['amount'] is None:
            return
        return round(self.cleaned_data['amount'], 1)

    def clean(self):
        data = super(CartModifyForm, self).clean()
        if data.get('action') in (self.ACTION_SET, self.ACTION_ADD):
            if 'amount' not in data or not data['amount']:
                raise ValidationError(_('No amount data for action'),
                                      code='invalid')
        return data

    def perform_action(self, cart):
        """Выполнить действие формы над корзиной

        :type cart: django_shop.cart.Cart
        """
        assert self.is_valid()
        if self.cleaned_data['action'] == self.ACTION_ADD:
            cart.add(self.cleaned_data['product'],
                     self.cleaned_data['amount'])
        elif self.cleaned_data['action'] == self.ACTION_REMOVE:
            cart.remove(self.cleaned_data['product'])
        elif self.cleaned_data['action'] == self.ACTION_SET:
            cart.set(self.cleaned_data['product'],
                     self.cleaned_data['amount'])
        else:
            raise NotImplementedError('Action is not implemented')


class OrderForm(forms.Form):
    """Формирование заказа: общие данные о заказе, его тип доставки и оплаты"""
    payment_type = forms.ModelChoiceField(
        queryset=PaymentType.objects.filter(is_active=True),
        widget=forms.HiddenInput
    )
    delivery_type = forms.ModelChoiceField(
        queryset=DeliveryType.objects.filter(is_active=True),
        widget=forms.HiddenInput
    )
    delivery_options = forms.CharField(max_length=4000, required=False,
                                       widget=forms.HiddenInput)


class ReceiverForm(forms.Form):
    """Фомирование заказа: данные о покупателе"""
    name = forms.CharField(label='Имя', max_length=300)
    email = forms.EmailField(label='Email')
    phone = PhoneNumberField(
        label='Телефон',
        help_text='Введите ваш телефон в формате +7XXXXXXXXXX'
    )


class AddressForm(forms.Form):
    """Фомирование заказа: адрес покупателя"""
    address = forms.CharField(label='Адрес', max_length=500, required=False)
    city = forms.CharField(label='Город или Населенный пункт',
                           max_length=200, required=False)
    zip_code = forms.CharField(label='Индекс', max_length=20,
                               required=False)
    province = forms.CharField(label='Регион/Облась', max_length=200,
                               required=False)
    country = forms.CharField(label='Страна', max_length=200,
                              required=False)

    def clean(self):
        data = super(AddressForm, self).clean()
        # Если указан город - ожидаем, что адрес тоже передан
        if data.get('city'):
            if not data.get('address'):
                raise ValidationError('Не указан адрес')

        # Если указана страна, ожидаем, что нам передадут, город и индекс
        if data.get('country'):
            if not data.get('city'):
                raise ValidationError('Не указан город')
            elif not data.get('zip_code') and data['city'] != 'Санкт-Петербург':
                raise ValidationError('Не указан индекс')

        return data


class ProductOrderForm(forms.Form):
    """Фомирование заказа: информация о заказанном продукте"""
    product = forms.ModelChoiceField(queryset=Product.objects.all(),
                                     widget=forms.HiddenInput)
    amount = forms.DecimalField(min_value=0.1, decimal_places=1,
                                required=False, widget=forms.HiddenInput)
