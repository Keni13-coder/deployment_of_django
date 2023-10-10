from django.contrib import admin
from .models import User, Product, Order



@admin.action(description='Изменить статус активности (True, False)')
def reset_active(modeladmin, request, queryset):
    # queryset имеет представлении db, посмотреть какой класс
    queryset.update(is_active=False)



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','date_create_user']

    ordering = ['name', 'date_create_user']

    list_filter = ['date_create_user', 'address', 'phone_number', 'is_active']

    search_fields = ['name', 'address', 'email']

    search_help_text = 'Поиск по полю Имени, Адреса, Електронной почти пользователя (name, address, email)'

    actions = [reset_active]

    readonly_fields = ['date_create_user', 'is_active']

    fieldsets = [
        (None, {'classes': ['wide'], 'fields':['name']}),
        ('Подробности', {'classes': ['collapse'], 'description': 'Адрес и дата', 'fields': [
         'address', 'date_create_user']}),
        ('Данные Пользователя', {'description': 'Доп. данные пользователя', 'fields': ['email', 'phone_number']})
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'date_create_product']

    ordering = ['title', 'price', '-date_create_product']

    list_filter = ['price', 'date_create_product', 'count', 'is_active']

    search_fields = ['title', 'description']

    search_help_text = 'Поиск по полю Имени и Описанию продукта (title, description)'

    actions = [reset_active]

    readonly_fields = ['date_create_product', 'image_preview', 'is_active']
    
    fieldsets = [
        (None, {'classes': ['wide', "extrapretty"], 'fields':['title', 'date_create_product']}),
        ('Подробности', {'classes': ['collapse'], 'description': 'Описание и изображение', 'fields': [
         'description', 'image_preview']}),
        ('Для продажи', {'description': 'Ценна товара и его количесвто', 'fields': ['price', 'count']}),
        (None, {'classes': ['wide', "extrapretty"], 'fields': ['is_active']})
    ]
    
    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_products', 'total_cost', 'date_create_order']

    ordering = ['date_create_order', 'total_cost']

    list_filter = ['total_cost', 'date_create_order', 'is_active']

    search_fields = ['user', 'products']

    search_help_text = 'Поиск по полю Имени пользователя и по полю с Товарами (user, products)'

    actions = [reset_active]

    readonly_fields = ['date_create_order', 'is_active', 'get_products']

    fields = ['user', 'get_products', 'total_cost', 'is_active', 'date_create_order']

    @admin.display(description='products')
    def get_products(self, obj):
        return ', '.join([prod.title for prod in obj.products.all()])


'Username=admin'
'password=1313'