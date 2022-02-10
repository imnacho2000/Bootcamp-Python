def listaGen(lista):
    list=[]
    for n in lista:
        n = n * 2
    list.append(n)
    print(f"Lista: {list}" )
    
listaGen([1,2,3,5,8,13])