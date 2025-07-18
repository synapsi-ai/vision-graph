import dataclasses
from typing import List


#
# Input
#

class Input:

    def __init__(self):
        pass


class InputBatchImages(Input):

    def __init__(self):
        pass


#
# Output
#

class Output:

    def __init__(self):
        pass


class OutputObjectDetection(Output):

    @dataclasses.dataclass
    class Box():
        x1: float
        y1: float
        x2: float
        y2: float

    def __init__(self):
        self._boxes: List[OutputObjectDetection.Box] = []
        self._classes_names: List[str] = []
        self._classes_ids: List[str] = []
        self._confidences: List[float] = []
        self._objects_id: List[int] = []


class OutputClassification(Output):

    def __init__(self):
        self._classes: List[str] = []
