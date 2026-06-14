import random

from rest_framework import generics

from characters.paginations import CharactersListPagination
from characters.serializers import CharacterSerializer
from characters.models import Character


class CharacterListView(generics.ListAPIView):
    serializer_class = CharacterSerializer
    pagination_class = CharactersListPagination
    queryset = Character.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if "name" in self.request.query_params:
            name = self.request.query_params.get("name")
            queryset = queryset.filter(name__icontains=name)
        return queryset


class CharacterRandomView(generics.RetrieveAPIView):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()

    def get_object(self):
        ids = self.queryset.values_list("pk", flat=True)
        random_id = random.choice(ids)
        return self.queryset.get(pk=random_id)
