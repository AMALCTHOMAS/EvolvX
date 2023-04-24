from django.urls import path
from . views import ManageProjectView,ProjectDetailAPIView,BookigAPIView,ProjectListAPIView,BookingListAPIView

urlpatterns = [
    path('manage/',ManageProjectView.as_view()),
    path('listprojects/',ProjectListAPIView.as_view()),
    path('<int:pk>/',ProjectDetailAPIView.as_view()),
    path('book/',BookigAPIView.as_view()),
    path('bookinglist/',BookingListAPIView.as_view()),
]