#!/usr/bin/env python
# coding: utf-8

import xml.etree.ElementTree as ET
context = ET.iterparse('file.xml', events=('end', )) # nombre del archivo  a editar file.xml
index = 0


for event, elem in context:
    if elem.tag == 'Informe':
        index += 1
        filename = format('CLIENTE' + str(index) + ".xml") # nombre del archivo a guardar CLIENTE + extension .xml o txt, etc.
        with open(filename, 'wb') as f:
            a = bytearray("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n", encoding='utf8' ) # convertir str a binary y codificacion
            b = bytearray("<Informes>\n", encoding='utf8' ) # convertir str a binary y codificacion
            c = bytearray("</Informes>", encoding='utf8' ) # convertir str a binary y codificacion
            f.write(a) # Escribe la cabecera de xml
            f.write(b) # Escribe la etiqueta de apertura
            f.write(ET.tostring(elem)) # Escribe etiquetas sub-etiquetas + cuerpo <root> cuerpo </root>.         
            f.write(c) # Escribe la etiqueta de Cierre
            

            

