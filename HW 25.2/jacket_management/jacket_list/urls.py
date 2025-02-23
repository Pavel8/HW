from django.urls import path
from .views import JacketListView, JacketCreateView, JacketDetailView, JacketUpdateView, JacketDeleteView

urlpatterns = [
    path('', JacketListView.as_view(), name='jacket-list'),
    path('add/', JacketCreateView.as_view(), name='add-jacket'),
    path('<int:pk>/', JacketDetailView.as_view(), name='jacket-detail'),
    path('<int:pk>/edit/', JacketUpdateView.as_view(), name='jacket-update'),  # URL pro úpravu bundy
    path('<int:pk>/delete/', JacketDeleteView.as_view(), name='jacket-delete'),  # URL pro vymazání bundy
]
