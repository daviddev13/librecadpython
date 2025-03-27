# ducha.py
import ezdxf

 #   """Crea un bloque y lo devuelve."
def crear_bloque_ducha(doc, nombre, corto, largo):
    """Crea un bloque genérico y lo devuelve."""

    # Crear el bloque con el nombre proporcionado
    block = doc.blocks.new(name=nombre)

    esp=0.08

    p1=(0,0)
    p2=(corto,0)
    p3=(0,largo)
    p4=(corto,largo)
    block.add_lwpolyline([p1, p2, p4, p3, p1], close=True)

    espesor=0.08
    t1=(p1[0]+esp,p1[1]+esp)
    t2=(p2[0]-esp,p2[1]+esp)
    t3=(p3[0]+esp,p3[1]-esp)
    t4=(p4[0]-esp,p4[1]-esp)
    block.add_lwpolyline([t1, t2, t4, t3, t1], close=True)

    c1=(corto/2,largo/2)
    radio=0.030
    block.add_circle(center=(c1), radius=radio)

    #bajante
    block.add_line(start=t1, end=t4)
    block.add_line(start=t3, end=t2)

    return block

if __name__ == "__main__":
    # para probar individualmente
    doc = ezdxf.new()
    msp = doc.modelspace()
    lavamanos_block = crear_bloque_ducha(doc,"ducha", corto=0.6, largo=1.2)
    msp.add_blockref("ducha", insert=(0, 0)) 
    # Guardar el DXF
    doc.saveas("ducha.dxf")
    print("Archivo 'ducha' creado.")

