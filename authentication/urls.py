from django.urls import path
from . import views



urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login/', views.MyTokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('test/', views.index)
]
