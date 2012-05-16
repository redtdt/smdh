#-----------------------------------------------------------------------------
# Name:        moduleFechas.py
#
#
# RCS-ID:      $Id: moduleFechas.py $
#
# Licence: Sistema de Monitoreo de Derechos Humanos, Compilacion de datos
#  Copyright (C) 2010, Asociacion Todos los Derechos para Todos, A.C.
#  Registro Publico de Derechos de Autor, Num. de Registro
#  03-2010-101210014200-01, Mexico.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see<http://www.gnu.org/licenses/>.
#
#-----------------------------------------------------------------------------
import calendar
import datetime



def ajustaFecha(tipo, dia, mes, anio, ini, status):
    diag = ''
    try:
        tipo = int(tipo)
    except:
        tipo = 0
    if tipo == status.idSinDia:
        dia = 1 if ini else calendar.monthrange(anio, mes)[1]
    if tipo == status.idSinMes or tipo == 116:
        
        dia = 1 if ini else 31
        mes = 1 if ini else 12
    if dia and mes and anio:        
        fecha = datetime.date(anio, mes, dia)
    
        return fecha
    else:
        return None
        
    


def FechasValidas(tipoI, diaI, mesI, anioI, tipoF, diaF, mesF, anioF, status):
    if not tipoI or not tipoF:
        return True
        # nada que comparar
    fechaI = ajustaFecha(tipoI, diaI, mesI, anioI, True, status)
    fechaF = ajustaFecha(tipoF, diaF, mesF, anioF, False, status)
    
    if fechaI and fechaF:
    
        if fechaF < fechaI: 
            
            #print 'Fechas:', tipoI, fechaI, tipoF, fechaF
            return False
        return True
    else:
        return False
def camposFechasValidas(tipoI, fechaI, tipoF, fechaF, status):
    return FechasValidas(tipoI, fechaI.day, fechaI.month, fechaI.year, tipoF, fechaF.day, fechaF.month, fechaF.year, status)

def ctrlFechasValidas(ctrlFechaI, tipoI, ctrlFechaF, tipoF, status):
    if tipoI: 
        tipoI=tipoI.id
    else:
        tipoI=0
    
    if tipoF: 
        tipoF=tipoF.id
    else:
        tipoF=0
    
    return FechasValidas(tipoI, ctrlFechaI[0].GetValue(), ctrlFechaI[1].GetValue(), ctrlFechaI[2].GetValue(),  
                         tipoF, ctrlFechaF[0].GetValue(), ctrlFechaF[1].GetValue(), ctrlFechaF[2].GetValue(), status)
                         
    
