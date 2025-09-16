from catia_app import CatiaApp
from sketch_builder import SketchBuilder
from part_builder import PartBuilder

def generate_part(longueur, largeur, hauteur):
    app = CatiaApp(visible=True)
    part_doc = app.new_part(name="AutoPart")

    sk = SketchBuilder(part_doc)
    sketch = sk.create_sketch_xy()
    sk.draw_rectangle(sketch, -largeur/2.0, -longueur/2.0, largeur, longueur)

    pb = PartBuilder(part_doc)
    pb.add_pad(sketch, hauteur)

    print(f"✅ Pièce générée : longueur={longueur}, largeur={largeur}, hauteur={hauteur}")

if __name__ == "__main__":
    generate_part(100, 50, 20)
