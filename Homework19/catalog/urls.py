from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactListView, ProductCreateView, ProductUpdateView, VersionListView
from django.urls import path



app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('create', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('version_list/', VersionListView.as_view(), name='list')
]