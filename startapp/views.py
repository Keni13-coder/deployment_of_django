from .utils import CrudOrder, CrudProduct, CrudUser, function_handler, Product
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from typing import Any
from datetime import timedelta, datetime
from .form import UpdateProduct, ImageForm
from django.core.handlers.wsgi import WSGIRequest
from django.core.files.storage import FileSystemStorage

def user_point(request, method: str):
    user = CrudUser()
    user_dict = {'name': 'Alex', 'email': 'alex@inbox.com', 'phone_number': '+64739173647', 'address':'кукуего'}
    return function_handler(method=method, model=user, data=user_dict)
            

def prod_point(request, method: str):
    product = CrudProduct()
    product_dict = {'title':'typewriter', 'description': 'color red, 10x15', 'price':15.0, 'count': 4}
    return function_handler(method=method, model=product, data=product_dict)



def order_point(request, method: str):
    order = CrudOrder()
    order_dict= {'user_id': 1, 'total_cost':30.0}
    # не стал уже еще больше заводиться по поводу добавление Many To Many. Есть статичное добавление [1,2] в классе CrudOrder
    return function_handler(method=method, model=order, data=order_dict)


def create_fake_datasets_point(request):
    # create_fake_datasets()
    return 'OK'

# many to many добовляем продукт и после переписыем общую стоимость
# order.products.add()
# total_cost = order.products.all().aggregate(Sum('price'))
#order.save()


    
    

class OrderUser(TemplateView):
    template_name = 'startapp/order.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['orders'] = CrudOrder().get_all()
        return context


def get_order(request, order_id: int):
    order = CrudOrder()
    date = 'date_create_product'
    order = order.get(pk=order_id)
    prods7 = order.products.all().filter(date_create_product__range=[datetime.now() - timedelta(days=7), datetime.now()]).order_by(f'-{date}')
    prods30 = order.products.all().filter(date_create_product__range=[datetime.now() - timedelta(days=30), datetime.now()]).order_by(f'-{date}')
    prods365 = order.products.all().filter(date_create_product__range=[datetime.now() - timedelta(days=365), datetime.now()]).order_by(f'-{date}')
    context = {'title': f'Заказ-{order_id}',
               'order': order, 'prods7':prods7,
               'prods30':prods30, 'prods365':prods365
               }
    return render(request=request, template_name='startapp/one_order.html', context=context)
    
    

def upload_image(request: WSGIRequest, product_pk: int):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            name = fs.save(name=image.name, content=image)
            product = Product.objects.filter(pk=product_pk).first()
            if product:
                product.image = name
                product.save()

    else:
        form = ImageForm()
        product = product = Product.objects.filter(pk=1).first()
    return render(request=request, template_name='startapp/upload_image.html', context={'form': form, 'prod': product})