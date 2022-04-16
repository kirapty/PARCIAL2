from django.urls import path
from .views import YearsListView, YearsDetailView


urlpatterns = [
    path('years/', YearsListView.as_view(), name='years_list'),
    path('years/<int:pk>', YearsDetailView.as_view(), name='years'),
]