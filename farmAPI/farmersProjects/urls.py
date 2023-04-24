from django.urls import path
from . views import ManageProjectView

urlpatterns = [
    path('manage/',ManageProjectView.as_view()),
]