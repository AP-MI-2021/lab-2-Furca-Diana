from math import sqrt
from math import ceil

def get_largest_prime_below(n):
    '''
    Determina cel mai mare numar prim mai mic decat n
    :param n: numar natural
    :return: numarul cautat
    '''
    numar_curent = n-1 # imi declar numarul curent

    while numar_curent>=2:
        gasit = 0 # daca numarul este prim valoarea lui 'gasit' ramane pe 0
        for i in range(2, numar_curent//2+1): 
            if numar_curent%i==0: #verificam daca numarul_curent are divizori
                gasit =1 # daca numarul nu este prim punem gasit pe 1
        
        if gasit == 0: #daca gasit a ramas 0 returnam valoarea numarului gasit(numar_curent)
            return numar_curent
        
        numar_curent -=1
    return -1 # daca nu am gasit nici un numar prim mai mic decat numarul dat returnez -1

def test_get_largest_prime_below():
    assert get_largest_prime_below(50) == 47 # test 1 
    assert get_largest_prime_below(49) == 47 # test 2

test_get_largest_prime_below() # apelez functia test


def is_palindrome(n):
    '''
    Determina daca un numar este palindrom
    :param n: numar natural
    :return: True sau False
    '''

    og = 0 # declararea variabilei pentru a afla inversul numarului n
    m = n # imi salvez valoarea lui n intr-o variabila auxiliara
    while m != 0:
        og = og*10+m%10 # formez inversul numarului
        m//=10
    
    return og == n # returnez valoarea de adevar a expresiei (inversul == numarul => palindrom (True) altfel False)


def test_is_palindrome():
    assert is_palindrome(123321) == True # test 1
    assert is_palindrome(7823952) == False # test 2
    assert is_palindrome(244442) == True # test 3
    assert is_palindrome(26472) == False # test 4

test_is_palindrome() # apelez functia test



def get_perfect_squares(start: int,end: int):
    '''
        Determina toate patratele perfecte cuprinse intr-un interval inchis dat
        :param : start, end numere naturale
        :return:  list[int] lista cu patratele perfecte cautate
    '''
    squares = []
    square=ceil(sqrt(start))
    ok=1
    while ok:

        if square**2<=end:
            squares.append(square**2)
        else:
            ok=0
            break
        square= square+1

    return squares

def test_get_perfect_squares():  # verific get_perfect_squares
    assert get_perfect_squares(10,40) == [16, 25, 36] # Test 1
    assert get_perfect_squares(20,50) == [25, 36, 49] # Test 2
    assert get_perfect_squares(38, 99) == [49, 64, 81] # Test 3

test_get_perfect_squares()

def input_get_perfect_squares ():
    print("Functia returneaza o serie de patrate perfecte cuprinse intr-un interval dat.")
    x = int(input("Limita stanga = "))
    y = int(input("Limita dreapta = "))
    print (f"Intre {x}  si {y} exista urmatoarele patrate perfecte: {get_perfect_squares(x,y)}.")

def main():
    isrunning = True # variabila de tip boolean pentru meniu 

    while isrunning: # cat timp isrunning are valoarea True programul functioneaza, cand valoarea trece pe False programul se opreste
        problema = input("Scrie numarul problemei: ") # citesc numarul problemei sau x daca vreau sa opresc programul

        if problema == "1":
            print("Ai ales problema 1: Determina cel mai mare numar prim mai mic decat n") 
            n = int(input("Scrie numarul n: ")) # citesc valoarea lui n
            print("Numarul gasit este: " + str(get_largest_prime_below(n))) # afisez rezultatul
        
        elif problema == "2":
            print("Ai ales problema 1: Determina daca un numar este palindrom")
            n = int(input("Scrie numarul n: ")) # citesc valoarea lui n
            palindrom = is_palindrome(n) # retin valoarea booleana a functiei
            if palindrom == True: # daca functia returneaza True -> este palindrom
                print("Numarul este palindrom.") 
            else:
                print("Numarul nu este palindrom.")
        elif problema == '3':
            input_get_perfect_squares()
        elif problema == 'x':
            isrunning = False # daca am ales 'x' programul se opreste
        else:
            print("Ai ales o obtiune invalida, incearca din nou!") # daca nu exista optiunea, poti alege alta optiune
        

if __name__ == "__main__":
    main() # apelez programul principal














