from django.urls import path
from contents.views import ContentView, ContentIdView

urlpatterns = [
    path("courses/<course_id>/contents/", ContentView.as_view()),
    path("courses/<course_id>/contents/<content_id>/", ContentIdView.as_view()),
]
