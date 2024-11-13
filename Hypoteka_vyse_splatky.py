import numpy as np
import pandas as pd


def vypocet_splatky_hypoteky(jistina, urokova_sazba, pocet_let):
    # Převod roční úrokové sazby na měsíční
    mesicni_urokova_sazba = urokova_sazba / 100 / 12
    
    # Celkový počet splátek (měsíce)
    celkovy_pocet_splatek = pocet_let * 12
    
    # Výpočet měsíční splátky (anuitní splátka)
    mesicni_splatka = (jistina * mesicni_urokova_sazba * (1 + mesicni_urokova_sazba) ** celkovy_pocet_splatek) / ((1 + mesicni_urokova_sazba) ** celkovy_pocet_splatek - 1)
    
    return mesicni_splatka

# Příklad použití:
jistina = float(input("Zadejte výši hypotéky (jistina): "))
urokova_sazba = float(input("Zadejte roční úrokovou sazbu (%): "))
pocet_let = int(input("Zadejte dobu splácení v letech: "))

mesicni_splatka = vypocet_splatky_hypoteky(jistina, urokova_sazba, pocet_let)
print(f"Vaše měsíční splátka bude: {mesicni_splatka:.2f} Kč")

# Inicializace seznamu pro tabulku
mesice = []
splatky_jistiny = []
splatky_uroky = []
zbytek_jistiny =[]
kontrola =[]
zaplaceno_na_urocich = []

#pomocna promenna
zbyvajici_jistina = jistina
splatka_uroky = 0
splatka_jistiny = 0
kontroly = 0
uroky = 0


#Vypocet pro kazdy mesic
for mesic in range(1, (pocet_let*12)+1):
    splatka_uroky = zbyvajici_jistina * (urokova_sazba/100/12)
    splatka_jistiny = mesicni_splatka - splatka_uroky
    zbyvajici_jistina = zbyvajici_jistina - splatka_jistiny
    kontroly = splatka_jistiny + splatka_uroky
    uroky = uroky + splatka_uroky

    #Ulozeni do seznamu
    mesice.append(mesic)
    splatky_uroky.append(splatka_uroky)
    splatky_jistiny.append(splatka_jistiny)
    zbytek_jistiny.append(zbyvajici_jistina)
    kontrola.append(kontroly)
    zaplaceno_na_urocich.append(uroky)



#Vytvoreni data framu
df = pd.DataFrame({
    "Mesic" : mesice,
    "Splátka úroku" : splatky_uroky,
    "Splátka jistiny" : splatky_jistiny,
    "Zbývající jistina" : zbytek_jistiny,
    "Kontrola" : kontrola,
    "Zaplaceno na uroci" : zaplaceno_na_urocich
})

print(df.head(360))