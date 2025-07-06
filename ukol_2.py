# Část 1
import requests

ico = input("Zadej IČO subjektu: ")

url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"

response = requests.get(url)
data = response.json()
obchodni_jmeno = data.get("obchodniJmeno")
textova_adresa = data.get("sidlo", {}).get("textovaAdresa")

if obchodni_jmeno and textova_adresa:
    print(obchodni_jmeno)
    print(textova_adresa)
    exit()
else:
    print("Subjekt nebyl nalezen nebo chybí údaje.")


# Část 2
nazev = input("Zadej název subjektu nebo jeho část: ")

url_vyhledat = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

data = {
    "obchodniJmeno": nazev
}

response = requests.post(url_vyhledat, headers=headers, json=data)
vysledek = response.json()
pocet = vysledek.get("pocetCelkem")
seznam = vysledek.get("ekonomickeSubjekty", [])

print(f"Nalezeno subjektů: {pocet}")

for subjekt in seznam:
    jmeno = subjekt.get("obchodniJmeno")
    ico = subjekt.get("ico")
    print(f"{jmeno}, {ico}")