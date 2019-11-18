from django.db import models as dj_models
from django.db.models import QuerySet

from core.tree.managers import TreeManager
from core.tree.querysets import TreeQuerySet


class Node(dj_models.Model):
    left = dj_models.PositiveIntegerField(editable=False)
    right = dj_models.PositiveIntegerField(editable=False)
    depth = dj_models.PositiveIntegerField(editable=False)
    tree_id = dj_models.PositiveIntegerField(editable=False)
    parent = dj_models.ForeignKey(to='self', on_delete=dj_models.CASCADE, null=True)

    objects = TreeManager.from_queryset(TreeQuerySet)()

    class Meta:
        abstract = True
        ordering = ('left',)

    @property
    def is_root(self) -> bool:
        return self.parent is None

    @property
    def children(self) -> QuerySet:
        return self.__class__.objects.get_children_for_node(self)

    @property
    def parents(self) -> QuerySet:
        return self.__class__.objects.get_parents_for_node(self)

    @property
    def siblings(self) -> QuerySet:
        return self.__class__.objects.get_siblings_for_node(self)
