from django.urls import path
from .views import blind_login, mute_login, regular_login, login_selection

urlpatterns = [
    path('', login_selection, name='login_selection'),  # Main login selection page
    path('blind/', blind_login, name='blind_login'),  # Voice login
    path('mute/', mute_login, name='mute_login'),  # Secret code login
    path('regular/', regular_login, name='regular_login'),  # Standard login
]
