from django.urls import path
from . views import ManageProductsView,GetProductListView,ManageOrderAPIview

urlpatterns = [
    path('manage/',ManageProductsView.as_view()),
    path('listedproducts/',GetProductListView.as_view()),
    path('manageorders/',ManageOrderAPIview.as_view()),
]