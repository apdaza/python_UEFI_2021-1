x = int(input("ingrese un valor: "))

print("usted ingreso el: " + str(x))

if x % 4 == 0:
    x /= 4
else:
    if x % 3 == 0:
        x /= 3
    else:
        if x % 5 == 0:
            x *= 5
        else:
            x += 1

print("el nuevo valor es : " + str(x))
