"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.helloview),
    path('datetime/', views.now_date),
    path('goodby/', views.goodby),
    path('', views.main_view),
    path('products/', views.products),
    path('categories', views.category_list_view),
    path('products/<int:id>/', views.products_detail_view),
    path('products/create/', views.product_create_view),
    path('categories/create/', views.category_create_view),
    path('users/', include('users.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
