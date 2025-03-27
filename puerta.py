# puerta.py
import ezdxf

 #   """Crea un bloque y lo devuelve."
def crear_bloque_puerta(doc, nombre, medida):
    """Crea un bloque genérico y lo devuelve."""

    # Crear el bloque con el nombre proporcionado
    block = doc.blocks.new(name=nombre)

    esp=0.04

    p1=(0,0)
    p2=(esp,0)
    p3=(0,medida)
    p4=(esp,medida)
    block.add_lwpolyline([p1, p2, p4, p3, p1], close=True)
 
    radio = medida
    start_angle = 0     # Ángulo inicial en grados
    end_angle = 90     # Ángulo final en grados

    block.add_arc(center=p2, radius=radio, start_angle=start_angle, end_angle=end_angle)

    return block

if __name__ == "__main__":
    # para probar individualmente
    doc = ezdxf.new()
    msp = doc.modelspace()
    puerta_block = crear_bloque_puerta(doc,"puerta", medida=0.8)
    msp.add_blockref("puerta", insert=(0, 0)) 
    # Guardar el DXF
    doc.saveas("puerta.dxf")
    print("Archivo 'puerta' creado.")

