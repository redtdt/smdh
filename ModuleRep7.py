#-----------------------------------------------------------------------------
# Name:        ModuleRep7.py
#
#
# RCS-ID:      $Id: ModuleRep7.py $
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
CasoResumenOpts = {
  'Caso': {'normal':
         {'PPublicaciones': False,
          'Personas_relacionadas': False,
          'Pfecha_final': True,
          'Pfecha_inicio': True,
          'Pfrecepcion': False,
          'Pmonitoreo': True,
          'PrtCasosRelacionados': False,
          'PrtDescriptor': True,
          'PrtID': False,
          'PrtLocalidades': True,
          'PrtTitulo1': False,
          'PrtTitulo10': False,
          'PrtTitulo2': False,
          'PrtTitulo3': False,
          'PrtTitulo4': False,
          'PrtTitulo5': True,
          'PrtTitulo7': False,
          'PrtTitulo8': True,
          'PrtTitulo9': False,
          'actos': True,
          'archivos': False,
          'comentarios': False,
          'descripcion_narrativa': False,
          'exportar': False,
          'fuentes': False,
          'intervenciones': True,
          'localidades': True,
          'no_persona_afectadas': True,
          'observaciones': False,
          'proyecto_conjunto': False,
          'proyecto_grupo': False,
          'proyecto_se': False,
          'resumen_descripcion': True,
          'strDerechosAfectados': False,
          'strTemas': False} },
 'DetallesBio': {'normal': {'PFecha_final': True,
                 'PFecha_info_vigente': True,
                 'PFecha_inicial': True,
                 'PersonaVin/strRoles': True,
                 'comentarios': True,
                 'descriptorVin': True,
                 'exportar': True,
                 'observaciones': True,
                 'puesto': True,
                 'rango': True}},
 'PPublicaciones': {'normal':{'Descriptor': True,
                    'Liga_publicacion': True,
                    'Nombre_del_sitio': True,
                    'PConfiabilidad': True,
                    'PIdioma': True,
                    'PLengua_indigena': True,
                    'PPersonareferenciada/Descriptor': True,
                    'PTipopublicacion': True,
                    'Pfecha': True,
                    'Pfecha_consulta': True,
                    'PrtID': True,
                    'comentarios': True,
                    'exportar': True,
                    'observaciones': True,
                    'titulo': True}},
 'Personas_relacionadas': {'normal':{'Descriptor': True,
                           'DetallesBio': True,
                           'Direcciones': True,
                           'Idiomas': True,
                           'Lenguas': True,
                           'Lugar_de_origen': True,
                           'OrigenEtnico': True,
                           'Pciudadania_o_sede': True,
                           'Pescolaridad': True,
                           'Pestado_civil': True,
                           'Pestado_nac_u_origen': True,
                           'Pfecha_nac_o_fund': True,
                           'Pfrecepcion': True,
                           'Pmonitoreo': True,
                           'Pmpio_nac_u_origen': True,
                           'Pocupacion': True,
                           'Ppais_nac_u_origen': True,
                           'Preligion': True,
                           'PrtID': True,
                           'Psexo': True,
                           'Ptipo': True,
                           'archivos': True,
                           'comentarios': True,
                           'descripcion_del_grupo': True,
                           'exportar': True,
                           'habla_lengua_local': True,
                           'no_dependientes': True,
                           'observaciones': True,
                           'otro_nombre': True,
                           'proyecto_conjunto': True,
                           'proyecto_grupo': True,
                           'proyecto_se': True,
                           'strRoles': True}},
 'RolPerpetradores': {'normal':{'Pgradoinvolucramiento': False,
                      'PrtID': False,
                      'Ptipoperpetrador': False,
                      'Pultimostatusperpetrador': False,
                      'exportar': False,
                      'observaciones': False,
                      'persona/Descriptor': True}},
 'actos': {'normal':{'PEstatusvdh': False,
           'PEstatusvictima': True,
           'PLocalidad/PrtDescriptor': False,
           'PLocalidad/notas_localidad': False,
           'PLocalidad/notas_municipio': False,
           'PLocalidad/strEstado': False,
           'PLocalidad/strLocalidad': False,
           'PLocalidad/strMpio': False,
           'PLocalidad/strPais': False,
           'PTipodeacto': True,
           'PTipodelugar': False,
           'Pfechafin': True,
           'Pfechainicio': True,
           'PrtID': False,
           'Pvictima/Descriptor': True,
           'RolPerpetradores': True,
           'edad_victima': False,
           'exportar': False,
           'observaciones': False,
           'strCaracRelevantes': False,
           'strLegisInt': False,
           'strLegisNac': False}},
 'fuentes': {'normal':{'PConexion_info': True,
             'PConfiabilidad': True,
             'PIdioma': True,
             'PLengua_indigena': True,
             'PPersona/Descriptor': True,
             'PPersona_como_fuente/Descriptor': True,
             'Pfecha': True,
             'PrtID': True,
             'comentarios': True,
             'exportar': True,
             'observaciones': True}},
 'intervenciones': {'normal':{'Pfecha': True,
                    'Pinterviniente/Descriptor': True,
                    'PrtID': False,
                    'comentarios': False,
                    'contraparte/Descriptor': False,
                    'exportar': False,
                    'impacto': False,
                    'observaciones': False,
                    'respuesta': False,
                    'solicitante/Descriptor': False,
                    'tipo': True}},
 'localidades': {'normal':{'strEstado': True,
                 'strLocalidad': False,
                 'strMpio': False,
                 'strPais': False}}
                 }

