from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

 
app_name = 'accounts'
urlpatterns = [
    path('register/',views.UserRegister.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = routers.SimpleRouter()
router.register('user',views.UserViewSets)
urlpatterns += router.urls 

"""
{
	"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMDEyNjcwMywiaWF0IjoxNzAwMDQwMzAzLCJqdGkiOiIxYzI2NzAyODE4MTM0MTAxYmFiYjgzMDIzNjQyOWE5ZSIsInVzZXJfaWQiOjF9.Gy9e5eyePkX2kgGArZsZqDp9_RM1vPbld8B6TS9S_30",
	"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwMDQwNjAzLCJpYXQiOjE3MDAwNDAzMDMsImp0aSI6IjQ0ZDFlMGRlYTAzMTQ4MzI4ZjQ1ODFhMTg3NDg1ODZkIiwidXNlcl9pZCI6MX0.VwsAGDToAGD5AxqUScdy3ZLLMirbhY-EBSvyhyy1Aec"
}
"""