import random

# #Üleasnne1 
# nimi=input("Mis on sinu nimi? ")
# if nimi.isalpha() and nimi.isupper():
#     if nimi=="JUKU":
#         print("Läheme kinno")
#         try:
#             vanus=int(input(f"Kui vana sa oled {nimi}?"))
#             if vanus<0:
#                 print("Viga!")
#             elif vanus<=6:
#                 print("Tasuta")
#             elif vanus<15:
#                 print("Lastepilet")
#             elif vanus<65:
#                 print("Täispilet")
#             elif vanus<100:
#                 print("Sooduspilet")
#             else:
#                 print("Nii palju!!!!")
#         except:
#             print("Täisarv oli vaja sissestada")
#     else:
#         print("Ootan Juku")
# else:
#     print("Segatud sõne")
# #Üleasnne 2
# # var1
# nimi1=input("1. Mis on sinu nimi? ")
# nimi2=input("2. MIs on sinu nimi? ")
# nimed=["Kieill","Gleb"]
# if nimi1.isalpha() and nimi2.ialpha():
#     if(nimi1 in nimed) and (nimi2 in nimed):
#         print("nad on pinginaabrid")
#     else:
#         print("Nad ei ole naaabrid")
# else:
#     print("Viga")
#  # var2
# if (nimi1=="KIril" and nimi2=="Gleb") or (nimi2=="Kiril" and nimi1=="Gleb"):
#     print("Nad on pinginaabrid")
# else:
#     print("Nad ei ole naabrid")


# #Üleasnne 3
# try:
#     a=float(input("Toa pikkus:"))
#     b=float(input("Toa laius:"))
#     S=a*b
#     print(f"Põranda pindalda on {S} m**2")
#     vastus=input("Kas tahad remonti teha?(Jah-1/Ei-0)") 
#     if vastus.upper()=="JAH" or vastus=="1":
#         print("Remont")
#         hind=float(input("Ühe meetri hind: "))
#         summa=hind*S
#         print(f"Remondi kulud: {summa} eur")
#     elif vastus.upper()=="EI" or vastus=="0":
#         print("-")
#     else:
#         print("Ei saa aru")
# except:
#     print("Numbrid!!!!")


# #Ülesanne 4
# alg_hind = float(input("Mis on toote alghind? "))
# if alg_hind > 700:
#     soodustus = 0.30 * alg_hind
#     uus_hind = alg_hind - soodustus
#     print(f"30% soodustus! Uus hind on {uus_hind:.2f} eurot.")
# else:
#     print("Soodustus ei kehti, kuna alghind on väiksem või võrdne 700.")

# #Üleasnne 5
# temperatuur = float(input("Mis on hetke temperatuur? "))
# if temperatuur > 18:
#     print("Temperatuur on üle 18 kraadi, see on sobilik toasoojus talvel.")
# else:
#     print("Temperatuur on alla 18 kraadi, see on külm.")

# #Üleasnne 6 
# pikkus=int(input("Mis pikkus teil on ?"))
# if pikkus <=150:
#     print("Lühike pikkus")
# elif pikkus<=180:
#     print("Keskmine pikkus")
# elif pikkus<=200:
#     print("Pikk pikkus")

# # Ülesanne 7
# sugu=input("Mis sugu sa oled(mees/naine): ")
# pikkus=int(input("Mis pikkus teil on ?"))
# if pikkus <=150:
#     kategooria="Lühike"
# elif pikkus<=180:
#     kategooria="Keskmine"
# elif pikkus<=200:
#     kategooria="Pikk"
# print(f"Tere pikkus on {kategooria} {sugu}")

#Üleasnne 8
# def shop_simulation():
#     products = {
#         "Молоко": (50, 100),
#         "Хлеб": (30, 70),
#         "Яйца": (70, 150),
#         "Сахар": (40, 90),
#         "Масло": (90, 200)
#     }

   
#     receipt = []

#     def ask_to_buy(product, price):
#         nonlocal receipt  
#         print(f"Хотите ли вы купить {product}? Цена: {price} руб/шт")
#         answer = input("Введите 'да' или 'нет': ").strip().lower()
#         if answer == "да":
#             quantity = int(input(f"Сколько {product} вы хотите купить? "))
#             total_cost = price * quantity
#             receipt.append((product, quantity, price, total_cost))


#     for product, price_range in products.items():
#         price = random.randint(*price_range)
#         ask_to_buy(product, price)


#     if receipt:
#         print("\nВаш чек:")
#         print("=" * 30)
#         print(f"{'Товар':<10}{'Кол-во':<8}{'Цена':<8}{'Итого':<8}")
#         print("=" * 30)

#         total_sum = 0
#         for item in receipt:
#             product, quantity, price, total_cost = item
#             print(f"{product:<10}{quantity:<8}{price:<8}{total_cost:<8}")
#             total_sum += total_cost

#         print("=" * 30)
#         print(f"Итого к оплате: {total_sum} руб")
#     else:
#         print("Вы ничего не купили. Спасибо за визит!")


# if __name__ == "__main__":
#     shop_simulation()

