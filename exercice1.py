def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat
    if n % 15 == 0:
        return "buzzfizz"
    if n % 3 == 0:
        return "fizz"
    if n % 5 == 0:
        return "buzz"
    else:
        return n

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))

