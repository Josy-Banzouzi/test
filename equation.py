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

              if cls.discriminant < 0:

                  print("l'equation n'admet aucune racine il n'y a pas de solution")
              elif cls.discriminant > 0:

                  cls.X1 = ((-cls.nombre_2) - 2 * math.sqrt(cls.discriminant))/(2 * cls.nombre_1)

                  cls.X2 = ((-cls.nombre_2) + 2 * math.sqrt(cls.discriminant))/(2 * cls.nombre_1)

                  print("l'equation admet deux racine distinct X1 == {} et X1 == {} ".format(cls.X1 , cls.X2))

              else:
                  cls.X3 = (- cls.nombre_2)/(2 * cls.nombre_1)
                  print("l'equation admet une racine double X3 ==  {}".format(cls.X3))

         elif cls.nombre_2 % 2 == 0:
              print("le nombre_2 est : paire ")

              cls.X4 = cls.nombre_2/2
              cls.discriminant = ((cls.X4 * cls.X4) -  cls.nombre_1 * cls.nombre_3)

              if cls.discriminant < 0:
                 print("l'equation n'admet aucune racine il n'y a pas de solution")
              elif cls.discriminant > 0:

                   cls.X1 = ((-cls.X4) - 2 * math.sqrt(cls.discriminant))/(cls.nombre_1)

                   cls.X2 = ((-cls.X4) + 2 * math.sqrt(cls.discriminant))/(cls.nombre_1)

                    print("l'equation admet deux racine distinct X1 == {} et X1 == {} ".format(cls.X1 , cls.X2))

              else:
                  cls.X3 = (- cls.X4)/( cls.nombre_1)
                  print("l'equation admet une racine double X3 ==  {}".format(cls.X3))

Equation.calcul_fonction()
