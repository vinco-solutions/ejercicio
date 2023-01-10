from django.urls import path
from polls.api.api import question_get_delete, question_create, question_update_delete

urlpatterns = [
    path('primero/<int:pk>/', question_get_delete.as_view(), name='question_retrieve_delete_view'),
    path('segundo/', question_create.as_view(), name='question_create_view'),
    path('tercero/<int:pk>/', question_update_delete.as_view(), name='question_retrieve_delete_view'),
] 