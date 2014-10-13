#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import smallSMILHandler
import sys
import os


def Impresion_Ordenada(lista):
    for Diccionario in lista:
        print Diccionario['etiqueta'], ('\t'),
        for Clave in Diccionario:
            if Clave != 'etiqueta' and Diccionario[Clave] != "":
                if Clave == 'src':
                    os.system("wget -q " + Diccionario[Clave])
                    Diccionario[Clave] = Diccionario[Clave].split('/')[-1]
                print Clave, "= " + '"' + Diccionario[Clave] + '"' + ('\t'),
        print


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = smallSMILHandler()
    parser.setContentHandler(cHandler)
    try:
        parser.parse(open(sys.argv[1]))
    except IndexError:
        sys.exit("Usage: python karaoke.py file.smil.")
    lista = cHandler.get_tags()
    Impresion_Ordenada(lista)
