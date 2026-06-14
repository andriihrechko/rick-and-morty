from django.urls import path

from characters.views import CharacterListView, CharacterRandomView

app_name = "characters"

urlpatterns = [
    path("", CharacterListView.as_view(), name="characters"),
    path("random/", CharacterRandomView.as_view(), name="random-character"),
]
