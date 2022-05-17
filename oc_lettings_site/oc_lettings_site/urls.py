from django.urls import path, include
from django.contrib import admin
from . import views


def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
]

