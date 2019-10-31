#!/usr/bin/env python
# coding: utf-8

# Licencia MIT

# Copyright (c) 2019 Brayan Rayo

# Por la presente se otorga permiso, sin cargo, a cualquier persona que obtenga una copia
# de este software y los archivos de documentación asociados (el "Software"), para tratar
# en el Software sin restricción, incluidos, entre otros, los derechos
# para usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y / o vender
# copias del Software y para permitir a las personas a quienes pertenece el Software
# amueblado para hacerlo, sujeto a las siguientes condiciones:

# El aviso de copyright anterior y este aviso de permiso se incluirán en todos
# copias o partes sustanciales del software.

# EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O
# IMPLÍCITO, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
# APTITUD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO EL
# LOS AUTORES O LOS TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES POR CUALQUIER RECLAMACIÓN, DAÑO U OTRO
# RESPONSABILIDAD, EN CASO DE ACCIÓN DE CONTRATO, TORTURA O DE OTRA MANERA, DERIVADA DE,
# FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTRAS OFERTAS EN EL
# SOFTWARE.



import xml.etree.ElementTree as ET # libreria para manipular archivos xml
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
            

            

