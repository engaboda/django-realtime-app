from django.urls import path

from .views import NoteDetail
from .views import NoteList

urlpatterns = [
    path('', NoteList.as_view(), name='note-list'),
    path('<int:pk>/', NoteDetail.as_view(), name='note-detail'),
]
