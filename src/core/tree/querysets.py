import typing as t

from django.db.models import QuerySet, Max


class TreeQuerySet(QuerySet):
    def get_parents_for_node(self, node) -> t.Union[QuerySet, list]:
        if node.is_root:
            return []

        return (
            self
            .filter(
                left__lte=node.left - 1,
                right__gte=node.right + 1,
                tree_id=node.tree_id,
            )
            .order_by('left')
        )

    def get_children_for_node(self, node) -> QuerySet:
        return self.filter(parent_id=node.id)

    def get_siblings_for_node(self, node) -> QuerySet:
        return self.filter(parent_id=node.parent.id if node.parent else None).exclude(id=node.id)
