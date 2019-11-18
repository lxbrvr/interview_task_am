from django.urls import path

from apps.categories.views import CategoryCreateAPIView, CategoryRetrieveAPIView

app_name = 'categories'

urlpatterns = [
    path('', CategoryCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', CategoryRetrieveAPIView.as_view(), name='retrieve'),
]