from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include

app_name= 'customLogin'
urlpatterns = [
    path('accountsa/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    url(r'^login/', include('customLogin.urls')),
    url(r'', admin.site.urls),
]