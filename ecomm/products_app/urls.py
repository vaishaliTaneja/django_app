from django.urls import path
from . import views
from ecomm.settings import DEBUG
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    # path('upload/', views.upload, name = 'upload-book'),
    path('update/<int:product_id>', views.update_product),
    path('delete/<int:product_id>', views.remove_product)
]