from django.urls import path

from characters.views import CharacterListView, CharacterRandomView

app_name = "characters"

urlpatterns = [
    path("characters/", CharacterListView.as_view(), name="characters"),
    path("characters/random/", CharacterRandomView.as_view(), name="random-character"),
]
