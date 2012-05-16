if __name__ == '__main__':
    import cnf
    cnf.user='admin'
    cnf.passwd='redtdt'

import module2
from module2 import session, Persona
from  metaphone import dm

def similaridad(a,b):
    
    if a[0] == b[0]: return 4
    if a[0] == b[1] or \
           a[1] == b[0]: return 2
    if a[1] and b[1] and \
           a[1] == b[1]: return 1
    return 0

def palabras_sim(palabras1, palabras2):
    palabras1 = module2.Sortable(palabras1).encode('latin_1').split(' ')
    palabras2 = module2.Sortable(palabras2).encode('latin_1').split(' ')
    cuenta = 0
    for j in range(min(len(palabras1),len(palabras2))):
        cuenta +=  similaridad(dm(palabras1[j]), dm(palabras2[j]))
    return cuenta
    
def persona_sim(p1, p2):
    peso_apellido = 3
    peso_nombre   = 1
    peso_edo      = 1
    peso_mpo      = 1
    cuenta = 0
    apellidos1 = p1.apellido
    apellidos2 = p2.apellido

    nombre1    = p1.nombre
    nombre2    = p2.nombre

    cuenta = palabras_sim(apellidos1, apellidos2) * peso_apellido
    if cuenta:
        cuenta += palabras_sim(nombre1, nombre2) * peso_nombre
        if p1.estado_nac_u_origen:
            cuenta += (p1.estado_nac_u_origen == p2.estado_nac_u_origen ) * peso_edo
        if p1.mpio_nac_u_origen:
            cuenta += (p1.mpio_nac_u_origen == p2.mpio_nac_u_origen) * peso_mpo
        
    return cuenta
    
codigosab = {}
buscar = session.query(Persona).filter(Persona.esindividual == 1).all()[70]


print buscar.apellido, buscar.nombre, buscar.estado_nac_u_origen, buscar.mpio_nac_u_origen
indx = 0

lista = session.query(Persona).filter(Persona.esindividual == 1).filter(Persona.id < 9999).all()

for i in lista:
        cuenta = persona_sim(i, buscar)
        if cuenta:
            print cuenta, i.apellido, i.nombre, i.estado_nac_u_origen, i.mpio_nac_u_origen
