from django.urls import path
from .views.ProveedorList import ProveedorList
from .views.ProveedorDetail import ProveedorDetail
from .views.ProveedorView import ProveedorView
from .views.ArticuloView import ArticuloView
urlpatterns = [    
    path('proveedor/',ProveedorView.proveedor_list,name="proveedor_list"),    
    path('proveedor/<pk>/',ProveedorView.proveedor_detail,name="proveedor_detail"),    
    
    path('articulo/',ArticuloView.articulo_list,name="articulo_list"),
    path('articulo/<pk>/',ArticuloView.articulo_detail,name="articulo_detail")
]