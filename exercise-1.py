horasextras = float(input("Número de horas extras: "))
horasFaltantes = float(input("Número de Horas faltantes: "))
tminutos = (horasextras) - (2/3 * horasFaltantes) * 60

  if tminutos >= 2401:
    print("Minutos totais: ", tminutos, "Gratificação de R$500,00")
  elif tminutos <= 2400 and tminutos <= 1801:
    print("Gratificação de R$$400,00")
  elif tminutos <= 1801 and tminutos >= 1201:
    print("Gratificação de R$300,00")
  elif tminutos <= 1201 and tminutos >= 600:
    print("O valor do prêmio é R$200,00")
  else:
    print("O valor do prêmio é de R$100,00")

    