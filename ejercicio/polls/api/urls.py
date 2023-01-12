from django.urls import path, include
from polls.api.api import question_get_delete, question_create, question_update_delete, RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views

urlpatterns = [
    path('primero/<int:pk>/', question_get_delete.as_view(), name='question_retrieve_delete_view'),
    path('segundo/', question_create.as_view(), name='question_create_view'),
    path('tercero/<int:pk>/', question_update_delete.as_view(), name='question_retrieve_delete_view'),
    path("api/auth/", include('knox.urls')),
    path('api/auth/register/', RegisterAPI.as_view(), name='register_api'),
    path('api/auth/log/', LoginAPI.as_view(), name='login_api'),
    path('api/auth/user/', UserAPI.as_view(), name='user_api'),
] 