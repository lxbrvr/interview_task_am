from django.urls import include, path


urlpatterns = [
    path('categories/', include('apps.categories.urls', namespace='categories')),
]
