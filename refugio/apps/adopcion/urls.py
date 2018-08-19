from django.urls import path
from apps.adopcion.views import index

'''Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
'''

urlpatterns = [
    path('', index),
]
