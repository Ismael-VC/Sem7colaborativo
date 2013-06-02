#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():

    linea_nro = 1
    linea_lst = []

    print "Ingrese el código (digite 'Salir' para terminar):\n"

    while True:

        linea = raw_input("[%d] " % linea_nro)
        if linea.lower() == "salir":
            break
        else:
            linea_lst.append([linea_nro, linea])
            linea_nro += 1

    print linea_lst

main()
