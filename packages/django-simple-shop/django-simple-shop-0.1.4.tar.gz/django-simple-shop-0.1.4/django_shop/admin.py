from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import transaction
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

from .models import ProductCategory, Product, ProductImage, ProductEntry, \
    DeliveryType, PaymentType, Order, ProductOrder, ProductCategoryCustomField
from .admin_forms import ProductImageAdminForm, DeliveryTypeAdminForm, \
    PaymentTypeAdminForm
from .utils.payment import get_description
from .utils.delivery import get_description as get_delivery_description


class SummernoteFlatPageAdmin(FlatPageAdmin, SummernoteModelAdmin):
    pass

# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, SummernoteFlatPageAdmin)


class ProductCategoryCustomFieldInline(admin.TabularInline):
    model = ProductCategoryCustomField
    extra = 0


@admin.register(ProductCategory)
class ProductCategoryAdmin(SummernoteModelAdmin):
    form = ProductImageAdminForm

    inlines = [
        ProductCategoryCustomFieldInline
    ]


class ProductImageInline(admin.TabularInline):
    form = ProductImageAdminForm
    model = ProductImage
    extra = 1


class ProductEntryInline(admin.TabularInline):
    fields = ('quantity', 'price')
    model = ProductEntry
    extra = 1

    def get_queryset(self, request):
        qs = super(ProductEntryInline, self).get_queryset(request)
        return qs.filter(quantity__gt=0)


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = ('name', 'price', 'in_stock', 'is_weight')
    prepopulated_fields = {
        'slug': ('name',),
    }
    inlines = [
        ProductImageInline,
        ProductEntryInline,
    ]


@admin.register(PaymentType)
class PaymentTypeAdmin(SummernoteModelAdmin):
    list_display = ('name', 'payment_type', 'payment_hook_name', 'is_active')
    form = PaymentTypeAdminForm

    def payment_hook_name(self, obj):
        return get_description(obj.payment_hook)
    payment_hook_name.short_description = 'Конкретный тип онлайн оплаты'


@admin.register(DeliveryType)
class DeliveryTypeAdmin(SummernoteModelAdmin):
    list_display = ('name', 'pricing_method', 'delivery_hook', 'actual_pricing', 'is_active')
    form = DeliveryTypeAdminForm

    def delivery_hook_name(self, obj):
        return get_delivery_description(obj.delivery_hook)
    delivery_hook_name.short_description = 'Конкретный тип API доставки'


class ProductOrderInline(admin.TabularInline):
    fields = ('__str__', 'quantity', 'price')
    readonly_fields = ('__str__', 'quantity', 'price')
    model = ProductOrder
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'products_string_html', 'state', 'created', 'changed', 'full_price')
    fields = ('state', 'created', 'changed', 'delivery_type', 'delivery_price', 'receiver', 'full_price',
              'payment_method')
    readonly_fields = ('created', 'changed', 'receiver', 'full_price', 'payment_method')
    inlines = [
        ProductOrderInline
    ]

    def get_actions(self, request):
        actions = super(OrderAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def get_form(self, request, obj=None, **kwargs):
        form = super(OrderAdmin, self).get_form(request, obj, **kwargs)
        if obj is not None:
            # Modify form.base_fields['state'].choices
            form.base_fields['state'].choices = obj.get_state_choices()
        return form

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    @transaction.atomic
    def save_model(self, request, obj, form, change):
        if change:
            current_version = Order.objects.get(pk=obj.id)
            if current_version.state == Order.STATE_CREATED and obj.state == Order.STATE_CONFIRMED:
                obj.reduce_stock_amount()

        obj.save()

    def products_string_html(self, obj):
        return mark_safe(obj.products_string.replace('\n', '<br>'))
    products_string_html.short_description = 'Заказ'
