"""
URL configuration for banco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
openapi .Info(
title ="DOC API" ,
default_version ='v1',
description ="Estamos gerando documentação para a nossa API inicial de banco (Sistema Financeiro)" ,
terms_of_service ="",
contact =openapi.Contact(email ="email@email.com" ),
license =openapi.License(name ="BSD License" ),
),
public =True,
permission_classes =(permissions .AllowAny,),
)


routers = routers.DefaultRouter()

urlpatterns = [
    path( 'swagger<format>/' , schema_view .without_ui(cache_timeout =0), name='schema-json' ),
    path( 'swagger/' , schema_view .with_ui( 'swagger' , cache_timeout =0), name='schema-swagger-ui' ),
    path( 'redoc/' , schema_view .with_ui( 'redoc', cache_timeout =0), name='schema-redoc' ),
    path("admin/", admin.site.urls),
    path('api/emprestimos/', include("emprestimos.api.urls")),
    path('api/financiamentoImovel/', include("financiamentoImovel.api.urls")),
    path('api/financiamentoVeiculo/', include("financiamentoVeiculo.api.urls"))
    
]
