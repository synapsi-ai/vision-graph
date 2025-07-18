from typing import Optional
import uuid

from nodes.node import Node


class Arc:

    def __init__(self, entity_id: str = "", node_from: Optional[Node] = None, node_to: Optional[Node] = None):
        self._id: str = entity_id
        if self._id == "":
            self._id = str(uuid.uuid4())

        self._node_from:  Optional[Node] = node_from
        self._node_to: Optional[Node] = node_to
