from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path("", chat_views.chatPage),

	# login-section
	path("login_user/", chat_views.login_view),
    path("login/", chat_views.login),
	path("auth/logout/", chat_views.logout, name="logout-user"),
]
