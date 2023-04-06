from django.urls import path
from Account import views
from .views import RegisterUserAPIView,LoginApi,ProjectiewSet,Projec_listviewSet,Card_listviewSet,Check_listviewSet,ALlUsers
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'projectiewSet', ProjectiewSet),

router.register(r'alluser', views.ALlUsers, basename='alluser'),

router.register(r'Projec_listviewSet', Projec_listviewSet, ),

router.register(r'card_listviewSet', Card_listviewSet),

router.register(r'check_listviewSet', Check_listviewSet),




urlpatterns = [
    path('', views.Index,name=""),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.LoginApi.as_view(), name='LoginApi'),

    path('register/',RegisterUserAPIView.as_view()),


]
urlpatterns += router.urls