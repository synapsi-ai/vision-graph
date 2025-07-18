import uuid

from visiongraph.entities.nodes.inout import Input, Output, InputBatchImages, OutputObjectDetection, OutputClassification


class Node:

    def __init__(self, entity_id: str = ""):
        self._id: str = entity_id
        if self._id == "":
            self._id = str(uuid.uuid4())


#
# Node Start/End
#

class NodeStart(Node):

    def __init__(self):
        pass


class NodeEnd(Node):

    def __init__(self):
        pass


#
# Node Inference
#

class NodeCompute(Node):

    def __init__(self):
        pass

    def compute(self, input: Input) -> Output:
        return Output()


class NodeInference(Node):

    def __init__(self):
        pass


class NodeInferenceObjectDetection(NodeInference):

    def __init__(self):
        pass

    def compute(self, input: InputBatchImages) -> OutputObjectDetection:
        return OutputObjectDetection()


class NodeInferenceObjectClassification(NodeInference):

    def __init__(self):
        pass

    def compute(self, input: InputBatchImages) -> OutputClassification:
        return OutputClassification()

#
# Node Conditional
#


class NodeConditional(Node):
    def __init__(self):
        pass


class NodeConditionalIf(Node):
    def __init__(self):
        pass
