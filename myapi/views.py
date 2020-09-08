from rest_framework import viewsets, serializers

from .models import Note

class NoteSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Note
    fields = ('id', 'title', 'subject', 'content', 'modified')
        
class NoteViewSet(viewsets.ModelViewSet):
  queryset = Note.objects.all() #.order_by('name')
  serializer_class = NoteSerializer

