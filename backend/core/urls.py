from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_auth_app.api.urls')),
    path('', include('dashboard_app.api.urls'))
]