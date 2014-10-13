#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import smallSMILHandler
import sys
import os


class karaokeLocal():

    def __init__(self, fichero):
        parser = make_parser()
        cHandler = smallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        self.lista = cHandler.get_tags()

    def __str__(self):
        cadena = ""
        for Dic in self.lista:
            cadena += str('\n' + Dic['etiqueta'] + '\t')
            for Clave in Dic:
                if Clave != 'etiqueta' and Dic[Clave] != "":
                    cadena += str(Clave + "= " + '"' + Dic[Clave] + '"' + '\t')
        return cadena

    def do_local(self):
        cadena = ""
        for Dic in self.lista:
            cadena += str('\t' + Dic['etiqueta'] + '\t')
            for Clave in Dic:
                if Clave != 'etiqueta' and Dic[Clave] != "":
                    if Clave == 'src':
                        os.system("wget -q " + Dic[Clave])
                        Dic[Clave] = Dic[Clave].split('/')[-1]
                    cadena += str(Clave + "= " + '"' + Dic[Clave] + '"' + '\t')
        return cadena


if __name__ == "__main__":
    """
    Programa principal
    """
    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python karaoke.py file.smil.")
    Cadena = karaokeLocal(fichero)
    print Cadena
    Cadena.do_local()
    print Cadena
