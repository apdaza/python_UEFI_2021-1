def fibbo(n):
    if n <= 2:
        return 1
    else:
        t1 = 1
        t2 = 1
        contador = 3
        while contador <= n:
            t1, t2 = t2, t1 + t2
            contador += 1
        return t2

def fibbo_rec(n):
    if n <= 2:
        return 1
    else:
        return fibbo_rec(n-1) + fibbo_rec(n-2)

def producto_rec(n1, n2):
    if n2 == 1:
        return n1 
    return n1 + producto_rec(n1, n2 - 1)

"""
5 * 4 = 5 + 5 + 5 + 5
        5 + (5 * 3)
             5 + (5 * 2)
                 5 + (5 * 1)
                      5
"""

# 1 1 2 3 5 8 13 21 ....

for i in range(1, 11):
    print(i,fibbo(i),fibbo_rec(i))

print(producto_rec(5, 4))

