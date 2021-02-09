from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accountsa/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]