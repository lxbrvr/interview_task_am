from django.db.models import Manager, Max, QuerySet

from core.utils import find_latest_id_for_model


class TreeManager(Manager):
    def get_next_tree_id(self) -> int:
        max_tree_id = self.aggregate(max_tree_id=Max('tree_id')).get('max_tree_id')
        return (max_tree_id or 0) + 1

    def bulk_create_from_dtc(self, dct: dict) -> QuerySet:
        objs = self.convert_raw_tree_to_models(dct)
        return self.bulk_create(objs)

    def convert_raw_tree_to_models(self, dct: dict) -> list:
        tree_id = self.get_next_tree_id()
        nodes_stack = []
        node = dict(dct).copy()

        def _convert_raw_tree_to_models(raw_node, nodes_counter=1, depth=0, parent=None):
            _convert_raw_tree_to_models.latest_inserted_id += 1
            children = raw_node.pop('children', [])
            node_model = self.model(
                id=_convert_raw_tree_to_models.latest_inserted_id,
                tree_id=tree_id,
                depth=depth,
                left=nodes_counter,
                parent=parent,
                **raw_node,
            )
            nodes_stack.append(node_model)

            for child in children:
                nodes_counter = _convert_raw_tree_to_models(
                    raw_node=child,
                    nodes_counter=nodes_counter + 1,
                    depth=depth + 1,
                    parent=node_model,
                )

            nodes_counter += 1
            node_model.right = nodes_counter

            return nodes_counter

        latest_inserted_id = find_latest_id_for_model(self.model) or 0
        _convert_raw_tree_to_models.latest_inserted_id = latest_inserted_id
        _convert_raw_tree_to_models(raw_node=node)

        return nodes_stack

