from django.urls import path
from . import views
from django.conf.urls.static import static
from web_site import settings

urlpatterns = [
    path('user_point/<method>', views.user_point, name='user_point'),
    path('prod_point/<method>', views.prod_point, name='prod_point'),
    path('order_point/<method>', views.order_point, name='order_point'),
    path('datasets_point/', views.create_fake_datasets_point, name='datasets_point'),
    path('order_all/', views.OrderUser.as_view(), name='order_all'),
    path('order/<int:order_id>', views.get_order, name='order'),
    path('upload/<int:product_pk>', views.upload_image, name='upload'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)