a=int(input("Ievadi termiņa līgumu: "))
b=int(input("Ievadi kilowatu skaitu: "))

if a==1:
  e=b*0.20159
  print("Jūsu samaksa ir ",e)
elif a==2:
  r=b*0.16961
  print("Jūsu samaksa ir ",r)
elif a==3:
  g=b*0.16427
  print("Jūsu samaksa ir ",g)
elif a==4:
  o=b*0.15964
  print("Jūsu samaksa ir ",o)
else:
  print("Nav tāds līgums iespējams")