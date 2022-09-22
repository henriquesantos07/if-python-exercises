angulo1 = int(input("VALOR DO PRIMEIRO ANGULO: "))
angulo2 = int(input("VALOR DO SEGUNDO ANGULO: "))
angulo3 = int(input("VALOR DO TERCEIRO ANGULO: "))

if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
  print("TRIÂNGULO RETÂNGULO")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
  print("TRIÂNGULO OBTUSÂNGULO")
elif angulo1 < 90 or angulo2 < 90 or angulo3 < 90:
  print("TRIÂNGULO ACUTÂNGULO")
else:
  print("TRIÂNGULO NÃO IDENTIFICADO")