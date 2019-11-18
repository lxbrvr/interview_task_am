from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.categories.models import Category


class CategoryCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)

    class Meta:
        model = Category
        fields = ('id', 'name',)

    def get_fields(self) -> dict:
        fields = super().get_fields()
        fields['children'] = serializers.ListField(child=CategoryCreateSerializer(), required=False)
        return fields

    def create(self, validated_data) -> Category:
        return self.Meta.model.objects.bulk_create_from_dtc(validated_data)[0]

    def validate_names(self, data: dict) -> None:
        if self.parent:
            return

        stack, names = [data], []

        while stack:
            node = stack.pop()
            names.append(node.get('name'))

            for child in node.get('children', []):
                stack.append(child)

        error = ValidationError('Names must be unique.')

        if len(set(names)) != len(names):
            raise error

        if Category.objects.filter(name__in=names).exists():
            raise error

    def validate(self, data: dict) -> dict:
        self.validate_names(data)
        return data


class FlatCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class FullCategorySerializer(serializers.ModelSerializer):
    children = FlatCategorySerializer(many=True)
    parents = FlatCategorySerializer(many=True)
    siblings = FlatCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'children', 'parents', 'siblings',)
