from django.urls import path
from Account import views
from .views import RegisterUserAPIView,RegisterApi
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', views.Index,name=""),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('userdetail/', views.CurrentUserView.as_view(), name='userdetail'),
    path('register/',RegisterUserAPIView.as_view()),
    # path("get-details/",UserDetailAPI.as_view()),

]