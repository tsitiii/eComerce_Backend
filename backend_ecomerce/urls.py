"""
URL configuration for backend_ecomerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title="simple eCommerce API",
      default_version='v1',
      description='''
      🛒 Description about the eCommerce App 

This Django-based eCommerce application provides a full-featured online shopping platform with secure user management and intuitive product handling. Key features include:

    Product Listing: Displays a variety of products with detailed information including images, descriptions, and pricing.

    Shopping Cart System: Allows users to add, update, and remove products from their cart with real-time total calculation.

    User Authentication: Supports user registration and login using email and password, with token-based authentication (JWT or similar).

    Password Reset: Users can securely reset their passwords via email verification and token-based reset links.

    RESTful API: All functionalities are exposed through RESTful endpoints, making it easy to integrate with frontend applications or mobile apps.

    Swagger Documentation: Developer-friendly API documentation is provided using Swagger UI for easy testing and reference.''',
      terms_of_service="https://www.yoursite.com/terms/",
      contact=openapi.Contact(url="http://tsiyongashaw.netlify.app/"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('account.urls')),  # Use an empty string for the root path
    path('products/', include('products.urls')),  
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
    
]