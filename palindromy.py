
def palindroms(word):
    """
       Definition of palindroms(word) can comparison words
       which we have and return to us information,
       that it is palindrom or not. 
    """
    #result = bool #"Podane słowo"
    word_output = word[::-1]
    return word == word_output
    """
    if word == word_output:
        #print(word == word_output)
        #result = result + "  jest palindromem."
        #result = True
    else:
        #print(word == word_output)
        #result = result + " nie jest palindromem."
        result = False
    return result
    """
    
if __name__ == "__main__":
    text = input("Wpisz wyraz, aby sprawdzić czy jest on palindromem: ")
    end = palindroms(text)
    print(end)
    

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
