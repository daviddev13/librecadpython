# estufa.py
import ezdxf

def crear_estufa(doc):
    """Crea un bloque y lo devuelve."""

    # bloque estufa
    block = doc.blocks.new(name="estufa")

    ancho=0.50
    profun=0.50

    p1=(0,0)
    p2=(ancho,0)
    p3=(0,profun)
    p4=(ancho,profun)
    # Dibujar rectángulo
    block.add_lwpolyline([p1, p2, p4, p3, p1], close=True)

    # boquillas esfufa
    c1=(0.125,0.125)
    c2=(0.125,0.375)
    c3=(0.375,0.125)
    c4=(0.375,0.375)
    radio=0.050
    block.add_circle(center=(c1), radius=radio)
    block.add_circle(center=(c2), radius=radio)
    block.add_circle(center=(c3), radius=radio)
    block.add_circle(center=(c4), radius=radio)
    
    return block

if __name__ == "__main__":
    # para probar individualmente
    doc = ezdxf.new()
    msp = doc.modelspace()
    estufa_block = crear_estufa(doc)
    msp.add_blockref("estufa", insert=(0, 0))
    # Guardar el DXF
    doc.saveas("estufa_test.dxf")
    print("Archivo 'estufa_test.dxf' creado.")






