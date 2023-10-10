from django.db.models.base import ModelBase
from .models import User, Product, Order
from django.http import HttpResponse
# from django.db.models import Sum


__all__ = ['CrudUser', 'CrudProduct', 'CrudOrder']

class Crud():
    model: ModelBase = None
    
    def get_all(self):
        responce = self.model.objects.all()
        return responce
        
        
    def get(self, pk: int):
        responce = self.model.objects.filter(pk=pk).first()
        return responce


    def create(self, data: dict):
        responce = self.model(**data)
        responce.save()
        return f'{self.model} create'
        
        
    def delete(self, pk: int):
        responce= self.model.objects.filter(pk=pk)
        responce.delete()
        return f'{self.model} delete'
    
    


class CrudUser(Crud):
    model = User
    
class CrudProduct(Crud):
    model = Product
    
class CrudOrder(Crud):
    model: Order = Order
    

    def get_all(self):
        responces = self.model.objects.all()

            # price = responce.products.all().aggregate(Sum('price'))['price__sum'] 
            # responce.total_cost = price if price else 0.0
            # print(responce.products.all().aggregate(Sum('price'))['price__sum'])
            # responce.save()
        return responces
        
    
    
    def get(self, pk: int):
        responce = self.model.objects.filter(pk=pk).first()
        return responce
    
    
    
    def create(self, data: dict):
        responce = self.model(**data)
        responce.save()
        responce.products.add(*[1,2])
        return f'{self.model} create'





def function_handler(method: str, model: ModelBase, data: dict={}):
    method = method.lower()
    match method:
        case 'get':
            responce = model.get_all()
            return HttpResponse(responce if responce else 'NO get')
        case 'prod':
            if data:
                responce = model.create(data)
                return HttpResponse(responce)
            else:
                raise ValueError('Pass the arguments of the dict class')
        case 'delete':
            responce = model.delete()
            return HttpResponse(responce)
        case _:
            raise ValueError('There can only be: get, prod, delete')
        
    
    
# def create_fake_datasets():
#     COUNT = 10
#     for i in range(1, COUNT + 1):
#         user = i
#         for j in range(1, COUNT + 1):
#             prod = j
#             order = get_object_or_404(Order, pk=i)
#             order.products.add(prod)
#             order.save()
