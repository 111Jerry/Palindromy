def palindroms(word):
    """
       Def palindroms(word) can comparison words
       which we have and return to us information,
       that it is or not palindrom
    """
    word = "Kodilla"
    for letter in word:
        print(letter)
    return
palindroms("kajak")


"""
Pamiętaj, że wszystkie zadania, które wysyłasz Mentorowi powinny być umieszczone w Twoim zdalnym repozytorium,
jako osobne projekty. W czasie pracy zapisuj więc kolejne commity i prześlij całość na serwer w serwisie GitHub.
Twoim zadaniem będzie napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem.
Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.
Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False,
mówiącą czy podany tekst jest palindromem.

Podpowiedź
Pamiętaj, że string/tekst, to kolekcja znaków. Znasz już funkcje kolekcji,
które pozwalają odnosić się do elementów indeksowanych od początku i od końca.
Do zadania dodaj krótką dokumentację i umieść je w zdalnym repozytorium. Link prześlij Mentorowi.

def customized_hello(first_name, last_name):
    print("Hello Mr %s %s" % (first_name, last_name))

customized_hello("John", "Cleese")

def shopping(items):
    shopping_cart = "Koszyk zawiera: "
    for item in items:
        shopping_cart += item + '\n'
    return shopping_cart

basket = shopping(shopping_items)
print(basket)

numbers = []
for i in range(1, 101):
    if i % 5 == 0:
        numbers.append(i)

print("Liczby z zakresu od 1 do 100 podzielne przez 5 to:", numbers)
cube = [number ** 3 for number in numbers]
print(f"Liczby z listy wyżej podniesione do potęgi trzeciej to {cube}")

"""