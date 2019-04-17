from django.contrib import admin
from django.urls import path

from login_app.views import (BasicCheckView, BasicLoginView, BasicLogoutView,
                             TokenAuthentication, TokenCheckView,
                             TokenLoginView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_check/', BasicLoginView.as_view()),
    path('login_basic/', BasicLoginView.as_view()),
    path('check/', BasicCheckView.as_view()),
    path('logout/', BasicLogoutView.as_view()),
    path('tokenlogin/', TokenLoginView.as_view()),
    path('tokencheck/', TokenCheckView.as_view()),
]
