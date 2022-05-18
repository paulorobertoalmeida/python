llista = [1,2,3,4,5,6]

llista.remove(1)
print(llista)


del llista[2]
print(llista)


my_math = reduce(lambda x,y: x + y, llista)
print(my_math)
