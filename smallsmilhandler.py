#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class smallSMILHandler(ContentHandler):

    def __init__(self):
        """
        Constructor. Inicializamos las variables
        """
        self.Karaoke = {
            'root-layout': ['width', 'height', 'background-color'],
            'region': ['id', 'top', 'bottom', 'left', 'right'],
            'img': ['src', 'region', 'begin', 'dur'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region']
        }

        self.lista = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta

        """
        if name in self.Karaoke:
            Dic = {}
            Dic['etiqueta'] = name
            for atributo in self.Karaoke[name]:
                Dic[atributo] = attrs.get(atributo, "")
            self.lista.append(Dic)

    def get_tags(self):
        return self.lista


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = smallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print cHandler.get_tags()
