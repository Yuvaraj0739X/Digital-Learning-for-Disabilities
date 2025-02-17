from django.urls import path
from django.urls import path
from .views import dashboard, learn_page, grade_lessons, grade1, grade2, grade3, grade4, grade5, grade1_alphabets, grade1_numbers, grade1_shapes
from django.conf import settings
from django.conf.urls.static import static
from .views import blind_login, mute_login, regular_login, login_selection

urlpatterns = [
    path('', login_selection, name='login_selection'),  # Main login selection page
    path('blind/', blind_login, name='blind_login'),  # Voice login
    path('mute/', mute_login, name='mute_login'),  # Secret code login
    path('regular/', regular_login, name='regular_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('learn/', learn_page, name='learn_page'),  # Route for Learn page
    path('learn/grade/<int:grade>/', grade_lessons, name='grade_lessons'),  # Standard login
    path('learn/grade1/', grade1, name='grade1'),
    path('learn/grade1/alphabets/', grade1_alphabets, name='grade1_alphabets'),
    path('learn/grade1/numbers/', grade1_numbers, name='grade1_numbers'),
    path('learn/grade1/shapes/', grade1_shapes, name='grade1_shapes'),
    path('learn/grade2/', grade2, name='grade2'),
    path('learn/grade3/', grade3, name='grade3'),
    path('learn/grade4/', grade4, name='grade4'),
    path('learn/grade5/', grade5, name='grade5'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)