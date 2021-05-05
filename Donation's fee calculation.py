def main():
  print("Devi fare una donazione? Calcola la percentuale di tassazione!")
  print()
  val_donazione = int(input("Qual è il valore del bene donato? "))
  val_eccedente1 = int(val_donazione) - 1000000
  da_pagare1 = (val_eccedente1 * 4 / 100)
  val_eccedente2 = int(val_donazione) - 100000
  da_pagare2 = (val_eccedente2 * 6 / 100)
  tasso1 = (val_donazione * 6 / 100)
  tasso2 = (val_donazione * 8 / 100)
  print("Sei un genitore o parente in linea retta del donatario? ")
  Gen_Par = input()
  if (Gen_Par == "Sì") or (Gen_Par == "si") or (Gen_Par == "sì") or (Gen_Par == "Si"):
    if (val_donazione <= 1000000):
        print("Tassazione pari a 0.")
    else :
      print("Tassazione pari al 4% sull'importo che eccede la franchigia. Dovrai pagare " + str(da_pagare1) + " euro")

  elif (Gen_Par == "No") or (Gen_Par == "no") :
    print("Sei un fratello o sorella del donatario? ")
    Fra_Sor = input()
    if (Fra_Sor == "Sì") or (Fra_Sor == "Si") or (Fra_Sor == "si") or (Fra_Sor == "sì") :
      if (val_donazione <= 100000):
        print("Tassazione pari a 0.")
      else :
        print("Tassazione pari al 6% sull'importo che eccede la franchigia. Dovrai pagare " + str(da_pagare2) + " euro")

    elif (Fra_Sor == "No") or (Fra_Sor == "no"):
      print("Sei un parente fino al quarto grado del donatario? ")
      Par_4 = input()
      if (Par_4 == "Sì") or (Par_4 == "Si") or (Par_4 == "si") or (Par_4 == "sì") :
        print("Tassazione pari al 6%. Dovrai pagare " + str(tasso1) + " euro")
      else:
        print("Tassazione pari all'8%. Dovrai pagare " + str(tasso2) + " euro")

  restart = input("Vuoi inserire un altro valore? ")
  if ((restart == "Si") or (restart == "Sì") or (restart == "si") or (restart == "sì")):
     main()
  else:
    print("Arrivederci!")

main()
