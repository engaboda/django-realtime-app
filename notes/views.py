from rest_framework import generics

from .models import NoteModel
from .serializers import NoteModelSerializer

class NoteList(generics.ListCreateAPIView):
    queryset = NoteModel.objects.all().order_by('-created_at', '-updated_at')
    serializer_class = NoteModelSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteModelSerializer