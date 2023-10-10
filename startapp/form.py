from django.forms import Form, IntegerField, CharField, DateField, DecimalField, ImageField
from django.forms import Textarea, DateTimeInput, DateInput
import datetime


'''
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count =models.IntegerField()
    date_create_product
'''

'''
Задание №6
Доработаем задачу про клиентов, заказы и товары из
прошлого семинара.
Создайте форму для редактирования товаров в базе
данных
'''

class UpdateProduct(Form):
    title = CharField(min_length=4, max_length=50)
    description = CharField(min_length=4, max_length=150, widget=Textarea())
    price = DecimalField(max_digits=8)
    count = IntegerField()
    date_create_product = DateField(initial=datetime.datetime.now, widget=DateTimeInput(attrs={'type': 'date-local'}))
    
    
class ImageForm(Form):
    image = ImageField()
    time = DateField(initial=datetime.datetime.now)