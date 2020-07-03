"""ifscfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from Bank.api import BankList,Branchdata
from Bank import views
from django.conf.urls import url

urlpatterns = [
    url(r'admin/', admin.site.urls),
    # path('', views.printdata),
    url(r'api/bank_list/', BankList.as_view(), name='bank_list'),
    url('api/branch_data/', Branchdata.as_view(), name='branch_data'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)