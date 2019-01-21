from rest_framework import serializers

from .models import NoteModel

class NoteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = '__all__'