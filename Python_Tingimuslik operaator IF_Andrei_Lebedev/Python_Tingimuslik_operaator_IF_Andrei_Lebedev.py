# #�leasnne1 
# nimi=input("Mis on sinu nimi? ")
# if nimi.isalpha() and nimi.isupper():
# � � if nimi=="JUKU":
# � � � � print("L�heme kinno")
# � � � � try:
# � � � � � � vanus=int(input(f"Kui vana sa oled {nimi}?"))
# � � � � � � if vanus<0:
# � � � � � � � � print("Viga!")
# � � � � � � elif vanus<=6:
# � � � � � � � � print("Tasuta")
# � � � � � � elif vanus<15:
# � � � � � � � � print("Lastepilet")
# � � � � � � elif vanus<65:
# � � � � � � � � print("T�ispilet")
# � � � � � � elif vanus<100:
# � � � � � � � � print("Sooduspilet")
# � � � � � � else:
# � � � � � � � � print("Nii palju!!!!")
# � � � � except:
# � � � � � � print("T�isarv oli vaja sissestada")
# � � else:
# � � � � print("Ootan Juku")
# else:
# � � print("Segatud s�ne")


� � 
# #�leasnne 2
# # var1
# nimi1=input("1. Mis on sinu nimi? ")
# nimi2=input("2. MIs on sinu nimi? ")
# nimed=["Kieill","Gleb"]
# if nimi1.isalpha() and nimi2.ialpha():
# � � if(nimi1 in nimed) and (nimi2 in nimed):
# � � � � print("nad on pinginaabrid")
# � � else:
# � � � � print("Nad ei ole naaabrid")
# else:
# � � print("Viga")
# �# var2
# if (nimi1=="KIril" and nimi2=="Gleb") or (nimi2=="Kiril" and nimi1=="Gleb"):
# � � print("Nad on pinginaabrid")
# else:
# � � print("Nad ei ole naabrid")


# #�leasnne 3
# try:
# � � a=float(input("Toa pikkus:"))
# � � b=float(input("Toa laius:"))
# � � S=a*b
# � � print(f"P�randa pindalda on {S} m**2")
# � � vastus=input("Kas tahad remonti teha?(Jah-1/Ei-0)") 
# � � if vastus.upper()=="JAH" or vastus=="1":
# � � � � print("Remont")
# � � � � hind=float(input("�he meetri hind: "))
# � � � � summa=hind*S
# � � � � print(f"Remondi kulud: {summa} eur")
# � � elif vastus.upper()=="EI" or vastus=="0":
# � � � � print("-")
# � � else:
# � � � � print("Ei saa aru")
# except:
# � � print("Numbrid!!!!")


# #�lesanne 4
# alg_hind = float(input("Mis on toote alghind? "))
# if alg_hind > 700:
# � � soodustus = 0.30 * alg_hind
# � � uus_hind = alg_hind - soodustus
# � � print(f"30% soodustus! Uus hind on {uus_hind:.2f} eurot.")
# else:
# � � print("Soodustus ei kehti, kuna alghind on v�iksem v�i v�rdne 700.")

# #�leasnne 5
# temperatuur = float(input("Mis on hetke temperatuur? "))
# if temperatuur > 18:
# � � print("Temperatuur on �le 18 kraadi, see on sobilik toasoojus talvel.")
# else:
# � � print("Temperatuur on alla 18 kraadi, see on k�lm.")

# #�leasnne 6 
# pikkus=int(input("Mis pikkus teil on ?"))
# if pikkus <=150:
# � � print("L�hike pikkus")
# elif pikkus<=180:
# � � print("Keskmine pikkus")
# elif pikkus<=200:
# � � print("Pikk pikkus")

# # �lesanne 7
# sugu=input("Mis sugu sa oled(mees/naine): ")
# pikkus=int(input("Mis pikkus teil on ?"))
# if pikkus <=150:
# � � kategooria="L�hike"
# elif pikkus<=180:
# � � kategooria="Keskmine"
# elif pikkus<=200:
# � � kategooria="Pikk"
# print(f"Tere pikkus on {kategooria} {sugu}")