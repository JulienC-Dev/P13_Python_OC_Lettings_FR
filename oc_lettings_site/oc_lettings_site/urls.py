from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('sentry-debug/', views.trigger_error),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
]
