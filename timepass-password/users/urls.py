from django.urls import path
from . import views
app_name='users'
urlpatterns = [

    path('forgot_password/',views.ForgetFormView, name ='ForgetPassword'),
    path('security_question/<int:pk>',views.SecurityQuestion,name='SecurityQuestion'),
    path('new_password/<int:pk>',views.NewPass,name='NewPass'),
    path('signup/', views.SignUp.as_view(), name='signup'),
  ]


