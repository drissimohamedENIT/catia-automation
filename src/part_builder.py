class PartBuilder:
    def __init__(self, part_doc):
        self.part_doc = part_doc
        self.part = part_doc.Part

    def add_pad(self, sketch, length=50.0):
        shape_factory = self.part.ShapeFactory
        pad = shape_factory.AddNewPad(sketch, length)
        self.part.Update()
        return pad
