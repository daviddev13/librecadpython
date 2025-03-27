# rotulo.py
import ezdxf

 #   """Crea un bloque y lo devuelve."
def crear_bloque_rotulo(doc, nombre, horizontal, vertical, margen, letraTitulo, letraConte, rotulox):
    """Crea un bloque genérico y lo devuelve."""

    # Crear el bloque con el nombre proporcionado
    block = doc.blocks.new(name=nombre)

    cuadroy= (vertical-margen*2)/7
    cuadrox= rotulox

    #rectángulo margen
    esq1=(margen,margen)
    esq2=(horizontal-margen,margen)
    esq3=(margen,vertical-margen)
    esq4=(horizontal-margen,vertical-margen)
    block.add_lwpolyline([esq1, esq2, esq4, esq3, esq1], close=True)


    rotx=-margen+horizontal-cuadrox
    rotx2=-margen+horizontal
    # cuadrados de rotulo
    #puntos del rotulo
    r1 = (rotx,margen)
    r2 = (rotx,margen+cuadroy*1)
    r3 = (rotx,margen+cuadroy*2)
    r4 = (rotx,margen+cuadroy*3)
    r5 = (rotx,margen+cuadroy*4)
    r6 = (rotx,margen+cuadroy*5)
    r7 = (rotx,margen+cuadroy*6)
    r8 = (rotx,margen+cuadroy*7)
    r21 = (rotx2,margen)
    r22 = (rotx2,margen+cuadroy*1)
    r23 = (rotx2,margen+cuadroy*2)
    r24 = (rotx2,margen+cuadroy*3)
    r25 = (rotx2,margen+cuadroy*4)
    r26 = (rotx2,margen+cuadroy*5)
    r27 = (rotx2,margen+cuadroy*6)
    r28 = (rotx2,margen+cuadroy*7)
    #lineas en x
    block.add_line(start=r2, end=r22)
    block.add_line(start=r3, end=r23)
    block.add_line(start=r4, end=r24)
    block.add_line(start=r5, end=r25)
    block.add_line(start=r6, end=r26)
    block.add_line(start=r7, end=r27)
    #msp.add_line(start=r8, end=r28)
    #lineas en y
    block.add_line(start=r1, end=r8)
    block.add_line(start=r21, end=r28)

    # Agregar texto al rótulo
    #titulos rotulos
    dezpText=8
    rot1 = block.add_text("PROYECTO:", dxfattribs={"height": letraTitulo})
    rot1.dxf.insert = (rotx+margen,r8[1] - (cuadroy*1/4))
    rot2 = block.add_text("CONTENIDO:", dxfattribs={"height": letraTitulo})
    rot2.dxf.insert = (rotx+margen,r7[1]- (cuadroy*1/4))
    rot3 = block.add_text("ARQUITECTO:", dxfattribs={"height": letraTitulo})
    rot3.dxf.insert = (rotx+margen,r6[1]- (cuadroy*1/4))
    rot4 = block.add_text("DIBUJO:", dxfattribs={"height": letraTitulo})
    rot4.dxf.insert =  (rotx+margen,r5[1]- (cuadroy*1/4))
    rot5 = block.add_text("FECHA:", dxfattribs={"height": letraTitulo})
    rot5.dxf.insert = (rotx+margen,r4[1]- (cuadroy*1/4))
    rot6 = block.add_text("PLANO:", dxfattribs={"height": letraTitulo})
    rot6.dxf.insert = (rotx+margen,r3[1]- (cuadroy*1/4))
    rot7 = block.add_text("ESCALA:", dxfattribs={"height": letraTitulo})
    rot7.dxf.insert = (rotx+margen,r2[1]- (cuadroy*1/4))
    #contenido rotulo
  
    rot8 = block.add_text("Casa ", dxfattribs={"height": letraConte})
    rot8.dxf.insert = (rotx+margen,r8[1]-(cuadroy*3/4))
    rot9 = block.add_text("Planta PISO 1", dxfattribs={"height": letraConte})
    rot9.dxf.insert = (rotx+margen,r7[1]-(cuadroy*3/4))
    rot9 = block.add_text("Plano de Localización", dxfattribs={"height": letraConte})
    rot9.dxf.insert =(rotx+margen,r7[1]-(cuadroy*3/4))
    rot10 = block.add_text("", dxfattribs={"height": letraConte})
    rot10.dxf.insert = (rotx+margen,r6[1]-(cuadroy*3/4))
    rot11 = block.add_text("xxxxo@gmail.com", dxfattribs={"height": letraConte})
    rot11.dxf.insert = (rotx+margen,r5[1]-(cuadroy*3/4))
    rot12 = block.add_text("2025", dxfattribs={"height": letraConte})
    rot12.dxf.insert = (rotx+margen,r4[1]-(cuadroy*3/4))
    rot13 = block.add_text("Arquitectonico 1/1", dxfattribs={"height": letraConte})
    rot13.dxf.insert =(rotx+margen,r3[1]-(cuadroy*3/4))
    rot14 = block.add_text("1:100", dxfattribs={"height": letraConte})
    rot14.dxf.insert = (rotx+margen,r2[1]-(cuadroy*3/4))

    return block

if __name__ == "__main__":
    # para probar individualmente
    doc = ezdxf.new()
    msp = doc.modelspace()
    rotulo_block = crear_bloque_rotulo(doc,"rotulo", horizontal=21, vertical=29.7, margen=1, letraTitulo=0.5, letraConte=0.3, rotulox=6)
    msp.add_blockref("rotulo", insert=(0, 0)) 
    # Guardar el DXF
    doc.saveas("rotulo.dxf")
    print("Archivo rotulo creado.")





