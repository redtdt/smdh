#-----------------------------------------------------------------------------
# Name:        moduleRep6.py
#
#
# RCS-ID:      $Id: moduleRep6.py $
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
from module2 import status
por_imprimir={}

por_imprimir['RolPerpetradores']=[
                                  'CR.E',
                                  'PrtID',
                                  'persona/Descriptor',
                                  
                                  #'PLoginfo',
                                  
                                   'Pgradoinvolucramiento',
                                   'Ptipoperpetrador',
                                   'Pultimostatusperpetrador',
                                   'Observaciones',
                                   'PLoginfo/PrtCreacion',
                                  'PLoginfo/PrtActualizacion',
                                  'exportar'
                                   
                                   
                                   ]

por_imprimir['CasoResumen'] = [
            # caso p1
            'PrtTitulo1.C',
            
            'PrtDescriptor',
            'Pfecha_inicio',
            'Pfecha_final',
            
            'PrtLocalidades',
            'localidades',
            'no_persona_afectadas',
            # caso p2  inf narrativa
            
            
            'resumen_descripcion.B',
            
            

            # caso P6 actos, victimas, perp....
              'PrtTitulo5.C',
              'actosResumen',
              
              'PrtTitulo8.C',
              'intervencionesResumen',
              
                ]
                
por_imprimir['actosResumen']=[

                    'PTipodeacto',
                    'Pvictima/Descriptor',
                    'Pfechainicio',
                    'Pfechafin',
                    'PEstatusvictima',
                    'RolPerpetradores',
                    ]                
                                   
por_imprimir['Caso'] = [
            # caso p1
            
            'PrtTitulo1.C',
            'PrtID',
            'PrtDescriptor',
            'Pfecha_inicio',
            'Pfecha_final',
            
            #'PLoginfo',
            
            'PrtLocalidades',
            'localidades',
            'no_persona_afectadas',
            'PLoginfo/PrtCreacion',
            'PLoginfo/PrtActualizacion',
            'exportar',
            # caso p2  inf narrativa
            'PrtTitulo2.C',
            'descripcion_narrativa.B',
            'resumen_descripcion.B',
            'observaciones.B',
            # casp p3 adm 
            'PrtTitulo3.C',
            'Pfrecepcion',
            'proyecto_grupo', 
              'proyecto_conjunto', 
              'proyecto_se',
              'comentarios',
              'Pmonitoreo',
              'archivos',
            # caso p4 tipificaciones  
              'PrtTitulo4.C',
              'strDerechosAfectados',
              'strTemas',
            # caso P5 casos relacionados
              'PrtTitulo10.C',
              'PrtCasosRelacionados.B',
            # caso P6 actos, victimas, perp....
              'PrtTitulo5.C',
              'actos',
              'PrtTitulo8.C',
              'intervenciones',
              'PrtTitulo7.C',
              'fuentes',
              
              'PPublicaciones',
              
              'PrtTitulo9.C',
              'Personas_relacionadas'
                ]
if not status.SE: por_imprimir['Caso'].remove('proyecto_se')
print status.SE
print por_imprimir['Caso']
                
por_imprimir['Persona'] = [
                         'PrtTitulo1.C',
                         'PrtID',
                         'PrtDescriptor',
                         # faltaria el tipo de persona?
                         'otro_nombre',
                         'Ptipo',
                         'Psexo',
                         'Pfecha_nac_o_fund',
                         'Ppais_nac_u_origen',
                         'Pestado_nac_u_origen',
                         'Pmpio_nac_u_origen',
                         'localidad_nac_u_origen',
                         'Pciudadania_o_sede',
                         'Pescolaridad',
                         'PLoginfo/PrtCreacion',
                         'PLoginfo/PrtActualizacion',
                         
                         
                         
                         #'Lugar_de_origen',
                         
                         
                         #Detalles
                         'PrtTitulo2.C',
                         'Pocupacion',
                         'Idiomas',
                         
                         
                         
                         
                         
                         
                         'habla_lengua_local',
                         'Lenguas',
                         'OrigenEtnico',
                         'Preligion',
                         'Pestado_civil',
                         'no_dependientes',
                         'descripcion_del_grupo',
                         'Direcciones',
                         'Pmonitoreo',
                         
                         'exportar',
                         
                         #datos administrativos
                         'PrtTitulo3.C',
                         'observaciones.B',
                         #'Pconfiabilidad', ????
                         'comentarios.B',
                         'archivos.B',
                         'Pfrecepcion',
                         'proyecto_grupo',
                         'proyecto_conjunto',
                         'proyecto_se',
                         'strRoles',
                         
                         'PrtTitulo4.C',
                         'DetallesBio']
                         
if not status.SE: por_imprimir['Persona'].remove('proyecto_se')

por_imprimir['DetallesBio']=['descriptorVin.D',
                            
                            #'PLoginfo',
                            
                            'PFecha_inicial',
                            'PFecha_final',
                            'PFecha_info_vigente',
                            'observaciones','comentarios',
                            'puesto','rango',
                            'PersonaVin/strRoles',
                            'PLoginfo/PrtCreacion',
                            'PLoginfo/PrtActualizacion',
                            'exportar',
                            'CR.E'
                            ]
                
por_imprimir['Acto']=[
                    #'Descriptor',
                    'PrtID',
                    'PTipodeacto',
                    
                    #'PLoginfo',
                    
                    'Pvictima/Descriptor',
                    
                    
                    'Pfechainicio',
                    'Pfechafin',
                    'strCaracRelevantes',
                    
                    
                    'PTipodelugar',
                    'PEstatusvdh',
                    'PEstatusvictima',
                     'strEdad_victima',
                    'PLocalidad/PrtDescriptor',
                    'PLocalidad/strPais',
                    'PLocalidad/strEstado', 
                    'PLocalidad/strMpio', 
                    'PLocalidad/notas_municipio', 
                    'PLocalidad/strLocalidad',
                    'PLocalidad/notas_localidad', 
                    'observaciones',
                    'PLoginfo/PrtCreacion',
                    'PLoginfo/PrtActualizacion',
                    'exportar',
                    
                    
                    
                    
                    'RolPerpetradores',
                    'strLegisNac',
                    'strLegisInt',
                    
                    'CR.E'
                    ]
por_imprimir['fuentes']=['PrtID',
                         'PPersona_como_fuente/Descriptor',
                         'PPersona/Descriptor',
                         'PConexion_info', 
                         
                         #'PLoginfo',
                         
                         'Pfecha',
                         'PIdioma',
                         'PLengua_indigena',
                         'observaciones',
                         'PConfiabilidad',
                         'comentarios',
                         'PLoginfo/PrtCreacion',
                         'PLoginfo/PrtActualizacion',
                         'exportar',
                         'CR.E']
por_imprimir['Intervencion']=[
                            'PrtID',
                            'tipo',
                            'Pinterviniente/Descriptor',
                            'Pfecha',
                            'solicitante/Descriptor', 
                            
                            'contraparte/Descriptor',
                            
                            
                            'respuesta',
                            'impacto',
                            'observaciones',
                            'comentarios',
                            #'PLoginfo',
                            'PLoginfo/PrtCreacion',
                         'PLoginfo/PrtActualizacion',
                            
                            #'Pestatus',
                            
                            'exportar',
                            'CR.E']
por_imprimir['PPublicaciones']=[
                       'PrtID',
                       'Descriptor',
                       'titulo',
                       'datos_publicacion',
                       'Pfecha',
                       'PTipopublicacion',
                       'Nombre_del_sitio',
                       'Liga_publicacion',
                       'Pfecha_consulta',
                       'PIdioma',
                       'PLengua_indigena',
                       
                       #'PLoginfo',
                       
                       'observaciones',
                       'PPersonareferenciada/Descriptor',
                       'PConfiabilidad',
                       'comentarios',
                       'PLoginfo/PrtCreacion',
                       'PLoginfo/PrtActualizacion',
                       'exportar',
                       'CR.E'
                       ]
por_imprimir['PLoginfo']=['PrtCreacion','PrtActualizacion']
#por_imprimir['localidades'] = ['strPais', 'strEstado','prtMpio','prtMpioNotas','prtLocalidad', 'prtLocalidadNotas']
por_imprimir['localidades'] = ['strPais', 'strEstado','prtMpio','prtLocalidad']
por_imprimir['Caso_vinculo'] = ['PrtID']


                       
por_imprimir['actos']=por_imprimir['Acto']
por_imprimir['Fuente']=por_imprimir['fuentes']
por_imprimir['intervenciones']=por_imprimir['Intervencion']
por_imprimir['publicacion']=por_imprimir['PPublicaciones']
por_imprimir['Personas_relacionadas']=por_imprimir['Persona']
por_imprimir['Loginfo']=por_imprimir['PLoginfo']

campos = {}


campos['Caso_vinculo'] = {
    'PrtID':('Relacion No.','PrtFun'),
     


}
campos['localidades']={
       'strPais':(u'Pa\xeds','PrtFun'),
       'strEstado':('Estado','PrtFun'),
       'prtMpio':('Municipio','PrtFun',3,['prtMpioNotas']),
       'prtMpioNotas':('Notas','PrtFun'),
       'prtLocalidad':('Localidad','PrtFun',3,['prtLocalidadNotas']),
       'prtLocalidadNotas':('Notas','PrtFun'),
       'CR':(u'INTRODUCIR UN ESPACIO','PrtConst'),


}
campos['Caso']={
              'PrtTitulo1':('DATOS GENERALES','PrtFun',0),
              'PrtTitulo2':(u'INFORMACI\xd3N NARRATIVA','PrtFun',0),
              'PrtTitulo3':(u'INFORMACI\xd3N ADMINISTRATIVA','PrtFun',0),
              'PrtTitulo4':('TIPIFICACIONES','PrtFun',0),
              'PrtTitulo5':('ACTOS, VICTIMAS, PERPETRADORES','PrtFun',0),
              'PrtTitulo6':('NORMATIVIDAD','PrtFun',0),
              'PrtTitulo7':('FUENTES','PrtFun',0),
              'PrtTitulo8':('INTERVENCIONES','PrtFun',0),
              'PrtTitulo9':('PERSONAS RELACIONADAS CON EL CASO','PrtFun',0),
              'PrtTitulo10':('RELACIONES ENTRE CASOS','PrtFun',0),
              'PrtID':('Caso No.','PrtFun'),
              'PrtDescriptor':('Nombre del caso','PrtFun'), 
              'PrtLocalidades':(u'Localizaci\xf3n', 'PrtFun',3,['PrtLocalidadesNotas']),
              'PrtLocalidadesNotas':('Notas','PrtFun'),
              'descripcion_narrativa':(u'Descripci\xf3n narrativa','PrtStr'),
              'resumen_descripcion':(u'Resumen de la descripci\xf3n','PrtStr'),
              'observaciones':('Observaciones','PrtStr'),
              'no_persona_afectadas':('No. de personas afectadas','PrtStr'),
              'comentarios':('Comentarios','PrtStr'),
              'archivos':('Archivos','PrtStr'),
              'actos':('Informaci\xf3n de Actos','PrtObj'),
              'actosResumen':('Actos','PrtObj'),
              'strTemas':('Temas','PrtFun'),
              'strDerechosAfectados':('Derechos afectados','PrtFun'),
              'intervenciones':('Informaci\xf3n de Intervenciones','PrtObj'),
              'intervencionesResumen':('Intervenciones','PrtObj'),
              'localidades':(u'Informaci\xf3n de Localizaci\xf3n detallada','PrtObj'),
              
       
              
              #'PLoginfo':(u'Datos de creaci\xf3n y actualizaci\xf3n','PrtObj'),
              'Pmonitoreo':('Estatus del caso','PrtTes'),
              'proyecto_grupo':('Proyecto local','PrtStr'),
              'proyecto_conjunto':('Proyecto conjunto Red TDT','PrtStr'),
              'proyecto_se':('Proyecto SE','PrtStr'),
              'Pfrecepcion':(u'Fecha de recepci\xf3n','PrtDateC'),
              
              'PLoginfo/PrtCreacion':(u'Creaci\xf3n del registro','PrtFun'),
              'PLoginfo/PrtActualizacion':(u'\xdaltima actualizaci\xf3n','PrtFun'),
              'exportar':('Exportar','PrtChk'),
              
              'fuentes':('Informaci\xf3n de Fuente personal','PrtObj'),  
              'PPublicaciones':('Informaci\xf3n de Fuente documental','PrtObj'),
              'Pfecha_inicio':('Fecha inicial','PrtDateC'),
              'Pfecha_final':('Fecha final','PrtDateC'),
              'Personas_relacionadas':('Informaci\xf3n de Personas relacionadas con el caso','PrtObjFun'),
              'PrtCasosRelacionados':('Casos relacionados', 'PrtFun'),
              'CR':(u'Rengl\fx3n en blanco','PrtConst'),
              
            
               }
campos['Loginfo']={'PrtCreacion':(u'Creaci\xf3n del registro','PrtFun'),
                   'PrtActualizacion':(u'\xdaltima actualizaci\xf3n','PrtFun'),
                   'CR':(u'INTRODUCIR UN ESPACIO','PrtConst'),
                   }
               
campos['Fuente']={'PPersona/Descriptor':(u'Persona sobre qui\xe9n se aporta informaci\xf3n','PrtFun'),
                  'PPersona_como_fuente/Descriptor':(u'Nombre de la fuente personal','PrtFun'),
                  'PConexion_info':(u'Conexi\xf3n con la informaci\xf3n','PrtTes'),
                  'PIdioma':('Idioma','PrtTes'),
                  'PLengua_indigena':(u'Lengua ind\xedgena','PrtTes'),
                  'exportar':('Exportar fuente personal','PrtChk'),
                  #'PLoginfo':(u'Datos de creaci\xf3n y actualizaci\xf3n','PrtObj'),
                  'PLoginfo/PrtCreacion':(u'Creaci\xf3n del registro','PrtFun'),
              'PLoginfo/PrtActualizacion':(u'\xdaltima actualizaci\xf3n','PrtFun'),
                  'Pfecha':(u'Fecha de la informaci\xf3n','PrtDateC'),
                  'PConfiabilidad':('Confiabilidad','PrtTes'),
                  'observaciones':('Observaciones','PrtStr'),
                  'comentarios':('Comentarios','PrtStr'),
                  'PrtID':('Fuente personal No.','PrtFun'),
                  'CR':(u'INTRODUCIR UN ESPACIO','PrtConst'),
                  }
                  
campos['Intervencion']={'tipo':(u'Tipo de intervenci\xf3n','PrtTes'),
                        'tipo/DescriptorCompleto':(u'Tipo de intervenci\xf3n','PrtFun'),
                        'solicitante/Descriptor':(u'Sobre qui\xe9n se interviene','PrtFun'),
                        'contraparte/Descriptor':(u'A qui\xe9n se le dirigi\xf3 esta intervenci\xf3n','PrtFun'),
                        'Pinterviniente/Descriptor':(u'Qui\xe9n inicia o realiza esta  intervenci\xf3n','PrtFun'),
                        #'Pestatus':(u'Estatus del expediente','PrtTes'),
                        'observaciones':('Observaciones','PrtStr'),
                        'comentarios':('Comentarios','PrtStr'),
                        'respuesta':(u'Respuesta a la intervenci\xf3n','PrtStr'),
                        'impacto':(u'Impacto de la intervenci\xf3n','PrtStr'),
                        'Pfecha':(u'Fecha de la intervenci\xf3n','PrtDateC'),
                        'PrtID':(u'Intervenci\xf3n No.','PrtFun'),
                        'exportar':(u'Exportar intervenci\xf3n','PrtChk'),
                        #'PLoginfo':(u'Datos de creaci\xf3n y actualizaci\xf3n','PrtObj'),
                        'PLoginfo/PrtCreacion':(u'Creaci\xf3n del registro','PrtFun'),
              'PLoginfo/PrtActualizacion':(u'\xdaltima actualizaci\xf3n','PrtFun'),
                        'CR':(u'INTRODUCIR UN ESPACIO','PrtConst'),
                        }

campos['PPublicaciones']={'titulo':(u'T\xedtulo de la fuente','PrtStr'), 
                       'Descriptor':(u'Identificaci\xf3n','PrtFun'),
                       'datos_publicacion':(u'Datos de la fuente','PrtStr'),
                       'Pfecha':('Fecha de la fuente','PrtDateC'),
                       'Pfecha_consulta':('Fecha de consulta','PrtDateC'),
                       'Nombre_del_sitio':('Nombre del sitio','PrtStr'),
                       'Liga_publicacion':(u'Liga a la fuente','PrtStr'),
                       'Pfecha_consulta':('Fecha de consulta','PrtDateC'),
                       'PTipopublicacion':(u'Tipo de fuente','PrtTes'),
                       'PIdioma':('Idioma','PrtTes'),
                       'PLengua_indigena':(u'Lengua ind\xedgena','PrtTes'),
                       'PConfiabilidad':('Confiabilidad','PrtTes'),
                       'observaciones':('Observaciones','PrtStr'),
                       'comentarios':('Comentarios','PrtStr'),
                       'PPersonareferenciada/Descriptor':(u'Persona sobre qui\xe9n se aporta informaci\xf3n','PrtFun'),
                       'PrtID':('Fuente documental No.','PrtFun'),
                       'exportar':('Exportar fuente documental','PrtChk'),
                       #'PLoginfo':(u'Datos de creaci\xf3n y actualizaci\xf3n','PrtObj'),
                       'PLoginfo/PrtCreacion':(u'Creaci\xf3n del registro','PrtFun'),
              'PLoginfo/PrtActualizacion':(u'\xdaltima actualizaci\xf3n','PrtFun'),
                       'CR':(u'INTRODUCIR UN ESPACIO','PrtConst'),
                       }
                       
              
               
campos['Persona']={

                   'PrtTitulo1':('DATOS GENERALES','PrtFun',0),
                   'PrtTitulo2':('DETALLES','PrtFun',0),
                   'PrtTitulo3':('INFORMACION ADMINISTRATIVA','PrtFun',0),
                   'PrtTitulo4':('DATOS BIOGRAFICOS','PrtFun',0),
                   
                   'PrtDescriptor':('Nombre completo','PrtFun'),
                   'Ptipo':(u'Tipo de grupo','PrtTes'),
                   'Psexo':(u'Sexo','PrtTes'),
                   'Pfecha_nac_o_fund':((u'Fecha de nacimiento',u'Fecha de creaci\xf3n'),'PrtDateC'),
                   #'Lugar_de_origen':((u'Lugar de nacimiento',u'Lugar de origen'),'PrtFun'),
                   'Pciudadania_o_sede':((u'Ciudadan\xeda',u'Pa\xeds sede'),'PrtTes'),
                   'Pescolaridad':((u'Escolaridad', u"Nivel de escolaridad predominante"),'PrtTes'),
                   'Pocupacion':((u'Ocupaci\xf3n',u'Ocupaci\xf3n predominante'), 'PrtTes'),
                   'habla_lengua_local':(u'Habla y entiende espa\xf1ol','PrtSi'),
                   'Porigen_etnico':(u'Origen \xe9tnico','PrtTes'),
                   'Preligion':((u'Religi\xf3n',u'Religi\xf3n predominante'),'PrtTes'),
                   'Pestado_civil':(u'Estado civil','PrtTes'),
                   'no_dependientes':((u'No. de dependientes',u'No. de personas en el grupo'),'PrtInt'),
                   'descripcion_del_grupo':(u'Descripci\xf3n del grupo','PrtStr'),
                   'observaciones':(u'Observaciones','PrtStr'),
                   'Pconfiabilidad':(u'Confiabilidad','PrtTes'),
                   'Pfrecepcion':(u'Fecha de recepci\xf3n','PrtDateC'),
                   'Pmonitoreo':(u'Monitoreo','PrtTes'),
                   'comentarios':(u'Comentarios','PrtStr'),
                   'archivos':(u'Archivos','PrtStr'),
                   'Direcciones':(u'Direcciones','PrtFun'),
                   'Idiomas':((u'Idioma que habla',u'Idioma predominante'),'PrtFun'),
                   'Lenguas':((u'Lengua que habla',u'Lengua(s) predominante(s)'),'PrtFun'),
                   'OrigenEtnico':((u'Origen \xe9tnico',u'Origen \xe9tnico predominante'),'PrtFun'),
                   'CaracteristicasRelevantes':(u'Caracter\xedsticas Relevantes','PrtFun'),
                   'strRoles':(u'Roles','PrtFun'),
                   'DetallesBio':(u'Informaci\xf3n de Datos biogr\xe1ficos','PrtObj'),
                   'exportar':(u'Exportar persona','PrtChk'),
                   #'PLoginfo':(u'Datos de creaci\xf3n y actualizaci\xf3n','PrtObj'),
                   'PLoginfo/PrtCreacion':(u'Creaci\xf3n del registro','PrtFun'),
              'PLoginfo/PrtActualizacion':(u'\xdaltima actualizaci\xf3n','PrtFun'),
                   'otro_nombre':(u'Otro nombre','PrtStr'),
                   'Ppais_nac_u_origen':((u"Pa\xeds de nacimiento",u"Pa\xeds de origen"),'PrtTes'),
                   'Pestado_nac_u_origen':((u'Estado de nacimiento','Estado de origen'),'PrtTes'),
                   'Pmpio_nac_u_origen':((u'Municipio de nacimiento',u'Municipio de origen'),'PrtTes'),
                   'localidad_nac_u_origen':((u'Localidad de nacimiento','Localidad de origen'),'PrtStr'),
                   #'habla_lengua_local':(u'Habla y entiende espa\xf1ol','PrtChk'),
                   'Direcciones':(u'Direcci\xf3n(es)','PrtFun'),
                   'proyecto_grupo':('Proyecto local','PrtStr'),
                   'proyecto_conjunto':('Proyecto conjunto Red TDT','PrtStr'),
                   'proyecto_se':('Proyecto SE','PrtStr'),
                   'PrtID':('Persona No.','PrtFun'),
                   'CR':(u'INTRODUCIR UN ESPACIO','PrtConst'),
                   
                   
                   }

# la tabla campos describe, para cada entidad y para campo, como hacer el 'render' respectivo                   
campos['EventoTipificacion']={'derechosafectados': ('Derecho afectado','PrtTes','TesDerechoAfectado','derechosafectados', 'descripcion'),
                              'tipificacion/DescriptorCompleto':('Derecho afectado','PrtFun'),
                              'temas':             ('Tema relacionado','PrtTes','TesTema',           'derechosafectados', 'descripcion'),}
                              #campo                 descr             render    al.tesnode           id???                campo???
campos['TesNode']={'descripcion':('Termino de tesauro','PrtStr'),
                   'tipo/DescriptorCompleto':('Termino de tesauro','PrtFun'),
                   }
 
             
campos['Acto']={'Descriptor':(u'Descripci\xf3n del acto','PrtFun'),

                # campo           descrip        render    clase      id             campo a imprimir?

                
                'Pvictima/Descriptor':(u'Nombre de la v\xedctima','PrtFun'),
                'PrtID':('Acto No.','PrtFun'),
                'exportar':('Exportar acto','PrtChk'),
                #'PLoginfo':(u'Datos de creaci\xf3n y actualizaci\xf3n','PrtObj'),
                'PLoginfo/PrtCreacion':(u'Creaci\xf3n del registro','PrtFun'),
                'PLoginfo/PrtActualizacion':(u'\xdaltima actualizaci\xf3n','PrtFun'),
                'PTipodeacto':('Tipo de acto o VDH','PrtTes'),
                'PTipodeacto/DescriptorCompleto':('Tipo de acto o VDH','PrtFun'),
                'PTipodelugar':('Tipo de lugar','PrtTes'),
                'Pvictima/Psexo':(u'V\xedctima: sexo','PrtTes'),
                'Pvictima/Pescolaridad':(u'V\xedctima: escolaridad','PrtTes'),
                'Pvictima/Ptipo':(u'V\xedctima: tipo de grupo','PrtTes'),
                'Pvictima':(u'V\xedctima', 'PrtFun','PerVictima','Pvictima','Descriptor'),
                'edad_victima':(u'Edad de la v\xedctima cuando ocurri\xf3 el acto','PrtInt'),
                'strEdad_victima':(u'Edad de la v\xedctima cuando ocurri\xf3 el acto','PrtFun'),
                'PEstatusvdh':('Estatus VDH','PrtTes'),
                'PEstatusvictima':(u'Estatus v\xedctima','PrtTes'),
                'observaciones':('Observaciones del acto','PrtStr'),                
                'strCaracRelevantes':(u'Caracter\xedsticas relevantes','PrtFun'),  
                'strLegisNac':(u'Legislaci\xf3n nacional aplicable','PrtFun'),
                'strLegisInt':(u'Instrumentos internacionales aplicables','PrtFun'),
                'RolPerpetradores':('Informaci\xf3n de Perpetradores','PrtObj'),
                'Pfechainicio':('Fecha inicial','PrtDateC'),
                'Pfechafin':('Fecha final','PrtDateC'),
                'PLocalidad/PrtDescriptor':(u'Localizaci\xf3n','PrtFun'),
                'PLocalidad/strPais':(u'Pa\xeds','PrtFun'),
                'PLocalidad/strEstado':(u'Estado','PrtFun'),
                'PLocalidad/strMpio':(u'Municipio','PrtFun'),
                'PLocalidad/notas_municipio':('Notas sobre municipio','PrtStr'),
                'PLocalidad/strLocalidad':(u'Localidad','PrtFun'),
                'PLocalidad/notas_localidad':('Notas sobre localidad','PrtStr'),
                'legislacion_nacional':(u'Legislaci\xf3n nacional','PrtTes'),
                'legislacion_nacional_notas':(u'Legislaci\xf3n nacional: notas','PrtStr'),
                'instrumentos_internacionales':('Instrumentos internacionales','PrtTes'),
                'instrumentos_internacionales_notas':('Instrumentos internacionales: notas','PrtStr'),
                'localidades':(u'Localizaci\xf3n detallada','PrtObj'),
                'CR':(u'INTRODUCIR UN ESPACIO','PrtConst'),

                # XXX localizacion
                }
                
                
                

campos['RolPerpetradores']={
                 
                 'persona':('Perpetrador: nombre','PrtFun','PerPerpetrador','RolPerpetradores','Descriptor'),
                 'persona/Descriptor':('Nombre del perpetrador','PrtFun'),
                 'Pgradoinvolucramiento':('Grado de involucramiento','PrtTes'),
                 'Ptipoperpetrador':('Tipo de perpetrador','PrtTes'),
                 'Pultimostatusperpetrador':(u'\xdaltimo estatus del perpetrador','PrtTes'),
                 'exportar':('Exportar perpetrador','PrtChk'),
                 #'PLoginfo':(u'Datos de creaci\xf3n y actualizaci\xf3n','PrtObj'),
                 'PLoginfo/PrtCreacion':(u'Creaci\xf3n del registro','PrtFun'),
              'PLoginfo/PrtActualizacion':(u'\xdaltima actualizaci\xf3n','PrtFun'),
                 'Observaciones':('Observaciones del perpetrador','PrtFun'),
                 'PrtID':('Perpetrador No.','PrtFun'),
                 'CR':(u'INTRODUCIR UN ESPACIO','PrtConst'),
                 }

campos['DetallesBio'] = {
                 'PrtID':(u'Dato biogr\xe1fico No.','PrtFun'),
                 'descriptorVin':(u'Descripci\xf3n','PrtStr'),
                 'PersonaVin/strRoles':('Roles','PrtFun'),
                 'PFecha_inicial':('Fecha inicial','PrtDateC'),
                 'PFecha_final':('Fecha final','PrtDateC'),
                 'PFecha_info_vigente':('Fecha de vigencia','PrtDateC'),
                 'observaciones':('Observaciones','PrtStr'),
                 'comentarios':('Comentarios','PrtStr'),
                 'puesto':('Puesto o cargo','PrtStr'),
                 'rango':('Rango','PrtStr'),
                 'exportar':(u'Exportar datos biogr\xe1ficos','PrtChk'),
                 #'PLoginfo':(u'Datos de creaci\xf3n y actualizaci\xf3n','PrtObj'),
                 'PLoginfo/PrtCreacion':(u'Creaci\xf3n del registro','PrtFun'),
              'PLoginfo/PrtActualizacion':(u'\xdaltima actualizaci\xf3n','PrtFun'),
                 'CR':(u'INTRODUCIR UN ESPACIO','PrtConst'),
                }                           

campos['Localidad'] = {
                 'Descriptor':('Localidad','PrtFun'),
                 'strEstado':('Localidad (estado)','PrtFun'),
                 'strMpio':('Localidad (Mpo)','PrtFun'),
                 'CR':(u'INTRODUCIR UN ESPACIO','PrtConst'),
                      }
                      
campos['Caracrelevantes'] = {
                 'Descriptor':(u'Acto: caracterst\xedca relevante','PrtFun')
                             }
                             
                             
#    como aparece en el mapper = nombre de la entidad
campos['actos'] = campos['Acto']
campos['Involucramiento'] = campos['RolPerpetradores'] 
campos['derechosafectados']=campos['EventoTipificacion']
campos['EventoTipificacionDerechosAfectados'] =campos['EventoTipificacion']
campos['fuentes']=campos['Fuente']
campos['intervenciones']=campos['Intervencion']
campos['publicacion']=campos['PPublicaciones']
campos['Personas_relacionadas']=campos['Persona']

campos['CasoResumen'] = campos['Caso']
campos['actosResumen'] = campos['Acto']
campos['intervencionesResumen'] = campos['Intervencion']
campos['PLoginfo'] = campos['Loginfo']

TituloAlternativo = {
u'Descripci\xf3n narrativa':'Hechos:',
u'Resumen de la descripci\xf3n':'Resumen de los hechos:'
}



