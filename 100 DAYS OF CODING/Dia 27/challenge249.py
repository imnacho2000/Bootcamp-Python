def add(*kwargs):
    sum = 0
    for n in kwargs:
        sum += n
    return(f"La Suma es: {sum} ")

print(add(4,8,6,4))


def filter(*kwargs):
    print(kwargs)

filter(1,2)