import ezdxf

 #  Crea un bloque y lo devuelve."
def crear_bloque_sanitario(doc,nombre):

    # Crear un bloque para el sanitario
    block = doc.blocks.new(name=nombre)

    tapatanquex=.2
    tapatanquey=.36
    radiotaza=.17

  # tanque 
    p1=(0,0)
    p2=(tapatanquex,0)
    p3=(0,tapatanquey)
    p4=(tapatanquex,tapatanquey)
    block.add_lwpolyline([p1, p2, p4, p3, p1], close=True)
  # taza del sanitario
    center = (tapatanquex+radiotaza+.02, tapatanquey/2)  # Centro del óvalo
    major_axis = (radiotaza,0)  # Vector que define el eje mayor (longitud y dirección)
    ratio = 0.7  # Relación entre el eje menor y el eje mayor
    block.add_ellipse(center, major_axis, ratio)
    c2=(center[0]+0.05, center[1])
    radio2=0.15
    # arco (de 270° a 90°, que cubre la parte derecha)
    block.add_arc(center=c2, radius=radio2, start_angle=270, end_angle=90)
    #lineas horizontales
    p5=(.24+tapatanquex,0.03)
    p6=(tapatanquex,0.03)
    p7=(.24+tapatanquex,radio2*2+0.03)
    p8=(tapatanquex,radio2*2+0.03)
    block.add_line(start=p5, end=p6)
    block.add_line(start=p7, end=p8)
 # boton
    c1=(tapatanquex/2,tapatanquey/2)
    radio3=0.02
    block.add_circle(center=(c1), radius=radio3)

    return block

# para probar individualmente
if __name__ == "__main__":
    # Crear un nuevo documento DXF
    doc = ezdxf.new()
    msp = doc.modelspace()

    sanitario_block = crear_bloque_sanitario(doc)
    msp.add_blockref("Sanitario", insert=(0, 0)) 
    # Guardar el DXF
    doc.saveas("saniario.dxf")
    print("Archivo sanitario creado.")
 



