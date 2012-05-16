#-----------------------------------------------------------------------------
# Name:        camposexp.py
#
#
# RCS-ID:      $Id: camposexp.py $
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
camposExp={}
camposExp['Caso']=(['descripcion','descripcion_narrativa',
                  'resumen_descripcion','observaciones','no_persona_afectadas',
                  #'comentarios','archivos',
                  'proyecto_grupo','proyecto_conjunto',
                   #'proyecto_se',
                   'exportar','exportarrelaciones',
                   'fecha_inicio','fecha_final',
                   #'frecepcion'
                   ],
                   ['monitoreo', 'tipo_fecha_inicio', 'tipo_fecha_final', #'tipo_frecepcion'
                   ]
                   )

camposExp['RefCaso']=(['observaciones',
                      #'comentarios'
                      ],
                      ['tipo_id'])

camposExp["Localidad"]=(['notas_localidad', 'notas_municipio', 'localidad'],
                        ['pais_id', 'estado_id', 'municipio_id'])
                        
#camposExp[objeto]=(camposismples,campostesauro)

camposExp["Acto"]=(['observaciones','localizacion_id', 'fechainicio', 'fechafin',
                  'legislacion_nacional_notas', 'instrumentos_internacionales_notas','edad_victima',
                  'edad_victima_tipo',
                  'exportar', 'exportarnormatividad'],
                  ['tipodeacto','tipofechainicio','tipofechafinal',
                   'tipolugar','estatusvdh','estatusvictima'])
camposExp["Involucramiento"]=(['observaciones','exportar'],
                               ['tesauro_id', 'gradoinvolucramiento', 
                                'tipoperpetrador', 'ultimostatusperpetrador'])
camposExp["Intervencion"]=(['observaciones',
                  #'comentarios', 
                  'respuesta', 'impacto', 'fecha', 
                  'exportar'],
                  ['tesauro_id', 'estatus_id', 'tipofecha'])

camposExp["Publicacion"]=(['titulo_de_parte','Nombre_del_sitio', 
                  'Liga_publicacion','fecha_consulta', 'observaciones',
                  #'comentarios',
                  'fecha',
                  'exportar','datos_publicacion'],
                  ['tipofecha', 'tipofechaconsulta', 'tipopublicacion',
                   'idioma', 'lengua_indigena', 'confiabilidad']) 
camposExp["FuentePersonal"]=(['observaciones',
                              #'comentarios',
                              'fecha',
                              'exportar'],
                              ['tipofecha', 'conexion_con_informacion',
                              'idioma', 'lengua_indigena', 'confiabilidad'])                 
camposExp["Persona"]=([
                  'nombre', 'apellido', 'esindividual', 'otro_nombre','fecha_nac_o_fund',
                 'localidad_nac_u_origen', 'habla_lengua_local', 'no_dependientes', 
                 'descripcion_del_grupo', 'proyecto_grupo', 'proyecto_conjunto', 
                 #'proyecto_se',  
                 #'frecepcion',
                 'observaciones',
                  #'archivos','comentarios',
                  'exportar'],
                   ['sexo', 'tipo_fecha_nac_o_fund', 
                      'pais_nac_u_origen', 'estado_nac_u_origen', 
                      'mpio_nac_u_origen', 'ciudadania_o_sede', 
                      'escolaridad', 'ocupacion', 'religion', 
                      'estado_civil', 
                      #'monitoreo', 
                      'tipo', 
                      #'tipo_frecepcion'
                    ]
                     )
camposExp["Direccion"]=(['masinformacion', 'telefono', 'celular', 'web', 'correo_e'],['tesauro_id'])
camposExp["DetalleBiografico"]=(['Fecha_inicial', 'Fecha_final', 
                    'observaciones', 
                    #'comentarios', 
                    'fecha_info_vigente', 'descripcion', 'exportar'],
                    ['tipofecha_inicial', 'tipofecha_final','tipofecha_info_vigente'])
camposExp["VinculoBiografico"]=(['Fecha_inicial', 'Fecha_final', 
                    'observaciones', 
                    #'comentarios', 
                    'fecha_info_vigente', 'exportar', 'puesto','rango'],
                    ['tipofecha_inicial', 'tipofecha_final', 
                     'tipofecha_info_vigente', 'tipo_id'])
camposExp["EventoTipificacion"]=(['notas'],['tesauro_id'])
camposExp['Caracrelevantes']=([],['caracrelevantes_id'])
camposExp['Loginfo']=(['fechaCreacion', 'fechaActualizacion'],[])
camposExp['PersonaTipificacion']=(['masinformacion','telefono','celular','web','correo_e','tesauro_id'],[])

                   