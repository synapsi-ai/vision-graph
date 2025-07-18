import uuid


class Workflow:

    def __init__(self, entity_id: str = ""):
        self._id: str = entity_id
        if self._id == "":
            self._id = str(uuid.uuid4())
