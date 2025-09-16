class SketchBuilder:
    def __init__(self, part_doc):
        self.part_doc = part_doc
        self.part = part_doc.Part

    def _get_part_body(self):
        bodies = self.part.Bodies
        try:
            return bodies.Item("PartBody")
        except Exception:
            body = bodies.Add()
            try:
                body.Name = "PartBody"
            except Exception:
                pass
            return body

    def create_sketch_xy(self):
        body = self._get_part_body()
        sketches = body.Sketches
        origin = self.part.OriginElements
        plane = origin.PlaneXY
        ref = self.part.CreateReferenceFromObject(plane)
        sketch = sketches.Add(ref)
        return sketch

    def draw_rectangle(self, sketch, x, y, width, height):
        factory2d = sketch.OpenEdition()
        x1, y1 = x, y
        x2, y2 = x + width, y
        x3, y3 = x + width, y + height
        x4, y4 = x, y + height

        factory2d.CreateLine(x1, y1, x2, y2)
        factory2d.CreateLine(x2, y2, x3, y3)
        factory2d.CreateLine(x3, y3, x4, y4)
        factory2d.CreateLine(x4, y4, x1, y1)

        sketch.CloseEdition()
        self.part.Update()
