print("Hello world")

llista_alumnes = ['Anna', 'Joan', 'Oriol', 'Silvia', 'Ricard', 'Iria', 'Francesc']
alumnes_ultima_hora = ['Josep', 'Lidia', 'Alba']
#Llistat complert de l'alumnat - ok
#Elaborar dos llistats que correspondran a dos aules A y B.
#Els alumnes parell tenen que anar a la aula A y els senars a la B.
#Per ultim mostrar ambes llistes.

alumnes_ultima_hora.extend(llista_alumnes)

print(alumnes_ultima_hora)

llist_aula_a = []


llista_aula_b = []

llist_aula_a = alumnes_ultima_hora[0:5]
llista_aula_b = alumnes_ultima_hora[5:]
print(llist_aula_a)
print(llista_aula_b)