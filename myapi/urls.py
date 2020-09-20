from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('delete/<int:note_id>', views.delete, name="delete"),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]