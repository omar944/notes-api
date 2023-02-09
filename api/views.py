from api.models import Note
from api.permissions import IsAuthorized
from api.serializers import NoteSerializer
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet


class NotesViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    permission_classes = [IsAuthenticated, IsAuthorized]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
