#! /usr/bin/even python3
#coding = utf-8
import math
class Equation:

    @classmethod
    def calcul_fonction(cls):

        print("programe de calcul d'une equation du second degree".center(30,"-"))

        cls.nombre_1 = input("Entrer votre premier nombre : ")
        cls.nombre_1 = float(cls.nombre_1)
        cls.nombre_2 = input("Entrer votre deuxieme nombre : ")
        cls.nombre_2 = float(cls.nombre_2)
        cls.nombre_3 = input("Entrer votre troisieme nombre : ")
        cls.nombre_3 = float(cls.nombre_3)

          if cls.nombre_2 % 2 == 1:
              print("le nombre_2 est : impaire ")
              cls.discriminant = ((cls.nombre_2 * cls.nombre_2) - 4 * cls.nombre_1 * cls.nombre_3)

Equation.calcul_fonction()
