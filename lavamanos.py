# lavamanos.py
import ezdxf

#def crear_lavamanos(doc):
 #   """Crea un bloque y lo devuelve."
def crear_bloque_lava(doc, nombre, ancho, profun):
    """Crea un bloque genérico y lo devuelve."""

    # Crear el bloque con el nombre proporcionado
    block = doc.blocks.new(name=nombre)

    # Definir mesa rectangular
    p1 = (0, 0)
    p2 = (ancho, 0)
    p3 = (0, profun)
    p4 = (ancho, profun)
    block.add_lwpolyline([p1, p2, p4, p3, p1], close=True)

    # llaves
    c1=(0.21,profun-0.05)
    c2=(0.21*2,profun-0.05)
    radio=0.02
    block.add_circle(center=(c1), radius=radio)
    block.add_circle(center=(c2), radius=radio)

    #grifo
    g1=((ancho/2)-0.01,0.091+0.275)
    g2=((ancho/2)+0.01,0.091+0.275)
    g3=((ancho/2)-0.01,0.091+0.275+0.16)
    g4=((ancho/2)+0.01,0.091+0.275+0.16)
    block.add_lwpolyline([g1, g2, g4, g3, g1], close=True)

    # Definir los parámetros del óvalo
    center = (0.32, 0.275)  # Centro del óvalo
    major_axis = (0.27, 0)  # Vector que define el eje mayor (longitud y dirección)
    ratio = 0.7  # Relación entre el eje menor y el eje mayor
    block.add_ellipse(center, major_axis, ratio)

    return block

if __name__ == "__main__":
    # para probar individualmente
    doc = ezdxf.new()
    msp = doc.modelspace()
    lavamanos_block = crear_bloque_lava(doc,"lavamanos", ancho=0.64, profun=0.55)
    msp.add_blockref("lavamanos", insert=(0, 0)) 
    # Guardar el DXF
    doc.saveas("lavamanos.dxf")
    print("Archivo 'lavamanos' creado.")

