from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.product,name='product'),
    path('subcategory/<int:subcategory_id>',views.product,name='productsubcategory'),
    path('<int:id>',views.productdetail,name='productdetail'),
]




