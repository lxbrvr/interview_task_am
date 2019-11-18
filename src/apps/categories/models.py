from django.db import models as dj_models

from core.tree.models import Node


class Category(Node):
    name = dj_models.CharField(max_length=20, unique=True)
