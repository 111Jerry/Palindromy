
def palindroms(word):
    """
       Definition of palindroms(word) can comparison words
       which we have and return to us information,
       that it is palindrom or not. 
    """
    word_input = ""
    word_output = ""
    word_input = word
    word_output = word_input[::-1]
    if word_input != word_output:
        print("Podane przez Ciebie słowo nie jest palindromem!")
    else:
        print("Podane przez Ciebie słowo nie jest palindromem.")            
    # print(word_input, word_output)
if __name__ == "__main__":
    text = input("Podaj proszę wyraz, aby sprawdzić czy jest on palindromem: ")
    palindroms(text)


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
"""
