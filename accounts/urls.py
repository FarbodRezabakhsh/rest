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
    path('users/',views.UserListApi.as_view())
]

router = routers.SimpleRouter()
router.register('user',views.UserViewSets)
urlpatterns += router.urls 


"""
{
	"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMDU4ODM1NSwiaWF0IjoxNzAwNTAxOTU1LCJqdGkiOiIyYjFhNThmZTBmNjE0MTZiOTAxNDkyYzRlMDdiYjhiZSIsInVzZXJfaWQiOjF9.7kxl0JpGMUeXCZ14UDOz6CbGylcp4pyi7vIno2WjX48",
	"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwNTAyMjU1LCJpYXQiOjE3MDA1MDE5NTUsImp0aSI6ImZmNTU2ZTQwNDliMTQ2Mzg4YTlmOTMwMmY3ZGFlZjVmIiwidXNlcl9pZCI6MX0.vknVQDFB0ZRR_xhx094Uc6MFK8-o3jq6ZM7JY_iu1sU"
}
""" 