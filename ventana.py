# lavamanos.py
import ezdxf

 #   """Crea un bloque y lo devuelve."
def crear_bloque_ventana(doc, nombre, tamano, gp):
    """Crea un bloque genérico y lo devuelve."""

    # Crear el bloque con el nombre proporcionado
    block = doc.blocks.new(name=nombre)

    tamanovent=tamano
    grosor=gp

    # Definir puntos
    p1i = (0, 0)
    p2i = (0, grosor/3)
    p3i = (0, 2*(grosor/3))
    p4i = (0, grosor)
    p1d = (tamanovent, 0)
    p2d = (tamanovent,grosor/3)
    p3d = (tamanovent,  2*(grosor/3))
    p4d = (tamanovent, grosor)
    i1i = (grosor/3, grosor/3)
    i2i = (grosor/3, (grosor/3)+(grosor/6))
    i3i = (grosor/3, (grosor/3)+(2*grosor/6))
    i1d = (tamanovent-grosor/3,grosor/3)
    i2d = (tamanovent-grosor/3, (grosor/3)+(grosor/6))
    i3d = (tamanovent-grosor/3, (grosor/3)+(2*grosor/6))


    #horizontales
    block.add_line(start=p1i, end=p1d)
    block.add_line(start=p2i, end=p2d)
    block.add_line(start=p3i, end=p3d)
    block.add_line(start=p4i, end=p4d)
    #horizon int
    block.add_line(start=i2i, end=i2d)
    #verticales
    block.add_line(start=p4i, end=p1i)
    block.add_line(start=p4d, end=p1d)
    #verticales interiores
    block.add_line(start=i1i, end=i3i)
    block.add_line(start=i1d, end=i3d)
    

    return block

if __name__ == "__main__":
    # para probar individualmente
    doc = ezdxf.new()
    msp = doc.modelspace()
    ventana_block = crear_bloque_ventana(doc,"ventana", tamano=1, gp=.15)
    msp.add_blockref("ventana", insert=(0, 0)) 
    # Guardar el DXF
    doc.saveas("ventana.dxf")
    print("Archivo 'ventana' creado.")

