from django.contrib import admin
from django import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('checksite.urls'))
]
