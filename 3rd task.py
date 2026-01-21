gander = str(input("Enter your gander: "))
hemoglobin = float(input("Enter your hemoglobin: "))

if gander == "male" :
   if hemoglobin < 134:
        print("Your hemoglobin level is Low. ")
   elif hemoglobin < 167:
       print("Your hemoglobin level is Normal. ")
   elif hemoglobin > 167:
        print("Your hemoglobin level is High. ")

elif gander == "female" :
    if hemoglobin < 117:
        print("Your hemoglobin level is Low. ")
    elif hemoglobin < 155:
        print("Your hemoglobin level is Normal. ")
    elif hemoglobin > 155:
        print("Your hemoglobin level is High. ")