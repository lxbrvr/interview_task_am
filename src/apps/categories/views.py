from rest_framework.generics import CreateAPIView, RetrieveAPIView

from apps.categories.models import Category
from apps.categories.serializers import CategoryCreateSerializer, FullCategorySerializer


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategoryCreateSerializer
    queryset = Category.objects.all()


class CategoryRetrieveAPIView(RetrieveAPIView):
    serializer_class = FullCategorySerializer
    queryset = Category.objects.all()
