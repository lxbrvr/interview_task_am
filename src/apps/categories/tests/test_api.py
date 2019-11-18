import pytest
from rest_framework import status as http_status

from apps.categories.models import Category


RAW_CATEGORIES_TREE = {
    "name": "Category 1",
    "children": [
        {
            "name": "Category 1.1",
            "children": [
                {
                    "name": "Category 1.1.1",
                    "children": [
                        {
                           "name": "Category 1.1.1.1"
                        },
                        {
                            "name": "Category 1.1.1.2"
                        },
                        {
                            "name": "Category 1.1.1.3"
                        }
                    ]
                },
                {
                    "name": "Category 1.1.2",
                    "children": [
                        {
                            "name": "Category 1.1.2.1"
                        },
                        {
                            "name": "Category 1.1.2.2"
                        },
                        {
                            "name": "Category 1.1.2.3"
                        }
                    ]
                }
            ]
        },
        {
            "name": "Category 1.2",
            "children": [
                {
                    "name": "Category 1.2.1"
                },
                {
                    "name": "Category 1.2.2",
                    "children": [
                        {
                            "name": "Category 1.2.2.1"
                        },
                        {
                            "name": "Category 1.2.2.2"
                        }
                    ]
                }
            ]
        }
    ]
}


@pytest.mark.django_db
def test_success_creation_nested_node(api_client):
    response = api_client.post('/categories/', data=RAW_CATEGORIES_TREE, format='json')

    assert response.status_code == http_status.HTTP_201_CREATED
    assert Category.objects.count() == 15


@pytest.mark.django_db
def test_fetching_nested_node(api_client):
    api_client.post('/categories/', data=RAW_CATEGORIES_TREE, format='json')
    category = Category.objects.get(name='Category 1.1.2')
    response = api_client.get(f'/categories/{category.id}/', format='json')

    assert response.status_code == http_status.HTTP_200_OK


@pytest.mark.django_db
def test_unique_error(api_client):
    non_unique_name = 'non_unique_name'
    nested_node = {
        "name": "Category 1",
        "children": [
            {"name": non_unique_name},
            {"name": non_unique_name},
        ]
    }

    response = api_client.post('/categories/', data=nested_node, format='json')

    assert response.status_code == http_status.HTTP_400_BAD_REQUEST
    assert response.json() == {'non_field_errors': ['Names must be unique.']}
