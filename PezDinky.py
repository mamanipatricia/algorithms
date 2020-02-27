'''

Consideremos el ejemplo volumen=10, machos=4, hembras=6, se forman inicialmente
cuatro parejas. Al final del primer mes, nacen cuatro machos y cuatro hembras Dinkies. Con
lo que hay 18 peces Dikies en total y 8 parejas. Al final de segundo mes, las 8 parejas tienen
un par de Dikies y suman un total de 34, lo que no abastece el medio litro para cada pez en
un tanque de 10 litros. Asi, se ha tomado, 2 meses para llegar a un estado lleno de peces.

CANTIDAD
[litros]    | NRO PECES
------------------------
0.5         | 1 pez
1           | 2 peces
1.5         | 3 peces
2           | 4 peces
...           ...
l           | p/0.5 = l    \\ p=54 -> 108 | p=peces, l=litros
p = l * 0.5 |

'''
# INPUT
L = 431131
M = 764
H = 249

# defining variables
totalFish = M + H
nroMonth = 0
i = H - M
M = min(M, H)
print(i)

# verifying if the tank is full with n fishes
def isFull(fish):
    lit = (fish * 0.5)
    if lit <= L :
        return True
    return False

# calculating how many months lasts until the tank is going to be full.
while isFull(totalFish):
    M = M * 2
    totalFish = totalFish + M
    print("T F. ", totalFish)
    nroMonth += 1
    print("MESES: ", nroMonth)

# OUTPUT
# 11 months