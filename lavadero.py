# lavader
import ezdxf

def crear_lavadero(doc):
    """Crea un bloque y lo devuelve."""
    # bloque para lavadero
    block = doc.blocks.new(name="lavadero")

    ancho=.60
    profun=.50

    p1=(0,0)
    p2=(ancho,0)
    p3=(0,profun)
    p4=(ancho,profun)
    # Dibujar la base del sanitario (rectángulo)
    block.add_lwpolyline([p1, p2, p4, p3, p1], close=True)

    espesor=0.08
    tanque=.3
    t1=(tanque,espesor)
    t2=(ancho-espesor,0+espesor)
    t3=(tanque,profun-espesor)
    t4=(ancho-espesor,profun-espesor)
    block.add_lwpolyline([t1, t2, t4, t3, t1], close=True)

    # llave
    block.add_circle(center=(tanque+(tanque-espesor)/2, espesor/2), radius=0.02)

    #lavado
    longitud=0.17
    l1=(espesor,espesor)
    l2=(espesor,espesor*2)
    l3=(espesor,espesor*3)
    l4=(espesor,espesor*4)
    l9=(espesor,espesor*5)
    l5=(l1[0] + longitud, l1[1])
    l6=(l2[0] + longitud, l2[1])
    l7=(l3[0] + longitud, l3[1])
    l8=(l4[0] + longitud, l4[1])
    l10=(l9[0] + longitud, l9[1])
    block.add_line(start=l1, end=l5)
    block.add_line(start=l2, end=l6)
    block.add_line(start=l3, end=l7)
    block.add_line(start=l4, end=l8)
    block.add_line(start=l9, end=l10)

    return block

if __name__ == "__main__":
    # para probar individualmente
    doc = ezdxf.new()
    msp = doc.modelspace()
    lavader_block = crear_lavadero(doc)
    msp.add_blockref("lavadero", insert=(0, 0))  # Insertar en la posición
    # Guardar el DXF
    doc.saveas("lavadero.dxf")
    print("Archivo creado.")






