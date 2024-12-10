import random

#Üleasnne1 
nimi=input("Mis on sinu nimi? ")
if nimi.isalpha() and nimi.isupper():
    if nimi=="JUKU":
        print("Läheme kinno")
        try:
            vanus=int(input(f"Kui vana sa oled {nimi}?"))
            if vanus<0:
                print("Viga!")
            elif vanus<=6:
                print("Tasuta")
            elif vanus<15:
                print("Lastepilet")
            elif vanus<65:
                print("Täispilet")
            elif vanus<100:
                print("Sooduspilet")
            else:
                print("Nii palju!!!!")
        except:
           print("Täisarv oli vaja sissestada")
        else:
            print("Ootan Juku")
    else:
        print("Segatud sõne")
#Üleasnne 2
# var1
nimi1=input("1. Mis on sinu nimi? ")
nimi2=input("2. MIs on sinu nimi? ")
nimed=["Kieill","Gleb"]
if nimi1.isalpha() and nimi2.ialpha():
    if(nimi1 in nimed) and (nimi2 in nimed):
        print("nad on pinginaabrid")
    else:
        print("Nad ei ole naaabrid")
else:
    print("Viga")
# var2
if (nimi1=="KIril" and nimi2=="Gleb") or (nimi2=="Kiril" and nimi1=="Gleb"):
    print("Nad on pinginaabrid")
else:
    print("Nad ei ole naabrid")


#Üleasnne 3
try:
    a=float(input("Toa pikkus:"))
    b=float(input("Toa laius:"))
    S=a*b
    print(f"Põranda pindalda on {S} m**2")
    vastus=input("Kas tahad remonti teha?(Jah-1/Ei-0)") 
    if vastus.upper()=="JAH" or vastus=="1":
        print("Remont")
        hind=float(input("Ühe meetri hind: "))
        summa=hind*S
        print(f"Remondi kulud: {summa} eur")
    elif vastus.upper()=="EI" or vastus=="0":
            print("-")
    else:
        print("Ei saa aru")
except:
    print("Numbrid!!!!")


#Ülesanne 4
alg_hind = float(input("Mis on toote alghind? "))
if alg_hind > 700:
    soodustus = 0.30 * alg_hind
    uus_hind = alg_hind - soodustus
    print(f"30% soodustus! Uus hind on {uus_hind:.2f} eurot.")
else:
    print("Soodustus ei kehti, kuna alghind on väiksem või võrdne 700.")

#Üleasnne 5
temperatuur = float(input("Mis on hetke temperatuur? "))
if temperatuur > 18:
    print("Temperatuur on üle 18 kraadi, see on sobilik toasoojus talvel.")
else:
    print("Temperatuur on alla 18 kraadi, see on külm.")

#Üleasnne 6 
pikkus=int(input("Mis pikkus teil on ?"))
if pikkus <=150:
    print("Lühike pikkus")
elif pikkus<=180:
    print("Keskmine pikkus")
elif pikkus<=200:
    print("Pikk pikkus")

# Ülesanne 7
sugu=input("Mis sugu sa oled(mees/naine): ")
pikkus=int(input("Mis pikkus teil on ?"))
if pikkus <=150:
   kategooria="Lühike"
elif pikkus<=180:
    kategooria="Keskmine"
elif pikkus<=200:
    kategooria="Pikk"
print(f"Tere pikkus on {kategooria} {sugu}")

# Üleasnne 8

tooded = [("piim", 1.10), ("sai", 0.89), ("suhkur", 5.00), ("munad", 2.05)]
receipt = []

for product, price in tooded:
    print(f"Tahad osta {product}? Tema hind {price:.2f} EUR.")
    vastus = input("Kirjutage 'jah' või 'ei': ").strip().lower()
    if vastus == "jah":
        kogus = int(input(f"Kui palju sa tahad osta {product}: "))
        total_cost = price * kogus
        receipt.append((product, kogus, total_cost))
        print(f"Kokku tuleb {total_cost:.2f} EUR.")
    else:
        print("Järgmine toode.")

# Печать чека
print("\nTänan ostude eest! Siin on teie ostukviitung:\n")
total_sum = 0
for product, kogus, total_cost in receipt:
    print(f"{product}: x{kogus} ************ {total_cost:.2f} EUR")
    total_sum += total_cost

print(f"\nKokku: {total_sum:.2f} EUR")


# Üleasnne 9
a=float(input("Kirjutage ´A´ külje :"))
b=float(input("Kirjutage ´B´ külje :"))
c=float(input("Kirjutage ´C´ külje :"))
d=float(input("Kirjutage ´D´ külje :"))

if a==b==c==d:
    print("See on ruud")
else:
    print("See ei ole ruud")

# Ülesanne 10 

a=float(input("Esimene arv :"))
b=float(input("Teine arv :"))
tegevus=(input("Valige tehe (+,-,*,/):"))

if tegevus=="+":
    result=a+b
    print(f"Tulemus:{a}+{b}={result}")
elif tegevus=="-":
    result=a-b
    print(f"Tulemus:{a}-{b}={result}")
elif tegevus=="*":
    result=a*b
    print(f"Tulemus:{a}*{b}={result}")
elif tegevus=="/":
    result=a/b
    print(f"Tulemus:{a}/{b}={result}")

# Ülesanne 11

# Ülesanne 12
price=float(input("Цена товара :"))

if price == 10:
    discount= 0.10
elif price > 10:
    discount =0.20
else:
    discount=0

    final_price = price*(1- discount)
print(f"Окончательная цена товара: {final_price} евро")

#Ülesanne 13
sugu = input("Kirjuta sinu sugu (mees/naine): ")

if sugu == "naine":
    print("Me võtame ainult mehi.")
else:
    try:
        vanus = int(input("Kui vana sa oled? "))
        if vanus < 0:
            print("Viga! Vanus ei saa olla negatiivne.")
        elif vanus < 16 or vanus > 18:
            print("Kahjuks ei sobi.")
        else:
            print("Sobib! Tere tulemast.")
    except ValueError:
        print("Viga!")
