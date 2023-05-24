from django.urls import path, include
from accounts import views



urlpatterns = [
	path('register/', views.Register.as_view(), name="register"),
	path('login/', views.LoginView.as_view(), name="login"),
	path('logout/', views.LogoutView.as_view(), name="logout"),
	path('user/', views.UserView.as_view(), name="me"),

	# path('accounts/', include('rest_registration.api.urls')),
	# path('accounts/', include('rest_framework.urls')),
	path('accounts/', include('djoser.urls')),
	path('accounts/', include('djoser.urls.authtoken')),
]
