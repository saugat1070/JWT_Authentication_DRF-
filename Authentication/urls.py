from django.urls import path
from Authentication import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('',views.api_root,name='api_root'),
    path('obtain_token/',obtain_auth_token,name='obtain_token'),
    path('student_record/',views.StudentView.as_view(),name='student'),
]
