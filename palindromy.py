def palindroms(word):
    """
       Def palindroms(word) can comparison words
       which we have and return to us information,
       that it is or not palindrom
    """
    word = "Kodilla"
    for letter in word(-1):
        print(letter)
palindroms("kajak")


"""
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