"""
URL configuration for pycharm_django_p1 project.

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
from django.urls import path
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('info/list/',views.info_list),
    path('info/delete/',views.info_delete),
    path('submit/suscess/',views.submit_suscess),
    path('',views.origin),
    path('archive/24/02/27',views.archive_24_02_27),
    path('archive/23/12/11',views.archive_23_12_11),
    path('archive/23/11/23',views.archive_23_11_23),
    path('archive/23/11/20',views.archive_23_11_20),
    path('archive/23/11/17',views.archive_23_11_17),
    path('archive/23/11/13',views.archive_23_11_13),
    path('archive/23/11/09',views.archive_23_11_09),
    path('archive/23/11/02',views.archive_23_11_02),
    path('archive/23/10/30',views.archive_23_10_30),
    path('archive/23/10/16',views.archive_23_10_16),
    path('archive/23/10/15',views.archive_23_10_15),
    path('archive/23/02/28',views.archive_23_02_28),
    path('archive/23/02/23/A',views.archive_23_02_23_A),
    path('archive/23/02/23/D',views.archive_23_02_23_D),
    path('archive/23/02/20',views.archive_23_02_20),
    path('archive/23/02/16',views.archive_23_02_16),
    path('archive/list/',views.archive_list),
    path('archive/list/2/',views.archive_list_2),
]
