"""app_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from .import views
from django.views.generic.base import TemplateView # 追加
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls
from two_factor.urls import urlpatterns as tf_urls
#from two_factor.admin import AdminSiteOTPRequired

#admin.site.__class__ = AdminSiteOTPRequired
app_name= 'customLogin222'

urlpatterns = [
    # 今回作成するアプリ「app_folder」にアクセスするURL
    #path('app_folder/', include('app_folder.urls')),
    # 何もURLを指定しない場合（app_config/views.pyで、自動的に「app_folder」にアクセスするよう設定済み）
    url(r'^login/', include('customLogin.urls')),
    path('accounts/', include('accounts.urls')),
    path('aaa/', views.index, name='index'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/passwordc/', views.password, name='password'),
    path('accounts/passwordchange/', views.passwordchange, name='passwordchange'),
    path('accounts/project/', views.project, name='project'),
    path('accounts/koutuhilist/', views.koutuhilist, name='koutuhilist'),
    path('accounts/koutuhi/', views.koutuhi, name='koutuhi'),
    path('accounts/koutuhisubmit/', views.koutuhisubmit, name='koutuhisubmit'),
    path('accounts/appearrance/', views.appearrance, name='appearrance'),
    path('accounts/output/', views.output, name='output'),
    path('accounts/output2/', views.output2, name='output2'),
    path('accounts/kintai/', views.kintaiload, name='kintai'),
    path('accounts/kintaiproject/', views.kintaiproject, name='kintaiproject'),
    path('accounts/kintaitouroku/', views.kintaitouroku, name='kintaitouroku'),
    path('accounts/twoAuth/', views.twoAuth, name='twoAuth'),
    path('accounts/kintaiabs/', views.kintaiabs, name='kintaiabs'),
    path('accounts/kintaiload/', views.kintaiload, name='kintaiload'),
    path('', include(tf_twilio_urls)),
    path('', include(tf_urls)),
]

# メディアファイル公開用のURL設定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
