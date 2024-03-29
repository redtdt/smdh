#-----------------------------------------------------------------------------
# Name:        listacampos.py
#
#
# RCS-ID:      $Id: listacampos.py $
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
camposEntidad = {}
camposEntidad['caso']=[ 'FRCCasoRel',
                        'FRCCasoRelTipo',
                        'FRCCasoRelObservaciones',
                        'FRCCasoRelComentarios', 
                        'listPersonaVinculosDB',
                        'textDescripcion', 
                        'checkBoxCasoConfidencialidad', 
                        'choiceTipoFechaInicial', 
                        'choiceTipoFechaFinal', 
                        'listLocalizacion', 
                        'listBoxDerechosafectados', 
                        'listBoxTemas',
                        'FCproyecto_se',
                        'FCproyecto_conjunto',
                        'FCproyecto_grupo',
                        'textCtrlResumen',
                        'textCtrlCAArchivos',
                        'textCtrlCAComentarios',
                        'textCtrlDescripcionNarrativa', 
                        'textCtrlObservaciones', 
                        'checkBoxCasoConfidencialidad',
                        'listBoxPerpetradores', 
                        'choiceMonitoreo',
                        'btnAddRelacion', 
                        'delCaso', 
                        'delLocalizacion',
                        'btnTipoRelCaso',
                        'delDerecho',
                        'delTema',
                        'btnCasoRel', 
                        'delRelacion',
                        'AddLocalizacion',
                        'btnActualizarCaso1',
                        'buttonActualizarCaso2',
                        'buttonActualizarCaso3',
                        'crGuardar', 
                        'buttonCasoDerechoafectado', 
                        'button2', 
                        'checkBoxCasoExportarRelaciones',
                        'FCtipo_frecepcion',
                        'textCtrlNoPersonasAfectadas'
                        
                        
                        
                        ]
                    
camposEntidad['casoRel'] = ['FRCCasoRelTipo', 'delRelacion',
                            'FRCCasoRel',
                            'FRCCasoRelObservaciones',
                            'FRCCasoRelComentarios']                       
camposEntidad['acto']=['FATipoacto', 'delActo',
    'FAConfidencialidad',
    'FAVictima',
    'FATipofechainicio',
    'FATipofechafin',
    'FACaracRelevante',
    'FATipodelugar',
    'FAEstatusvdh',
    'FAEstatusvictima',
    'FAedad_victima',
    'FALocalidad',
    'FAObservaciones',
    'listBoxActoPerpetradores','FIperpetrador',
    'FIconfidencialidad',
    'FIgradoinvolucramiento',
    'FItipoperpetrador',
    'FIultimostatusperpetrador',
    'textCtrlINObservaciones',
    'FALegis', 'delLegislacion',
    'FAInstr', 'delInstrInt',
    'FAlegislacion_nacional_notas',
    'FAinstrumentos_int_notas',
    'buttonNuevoActo',
    'btnTipodeacto',
    'BTNAgregarcaracrelevantes',
    'buttonSelecTipodelugar',
    'buttonRemoveTipodelugar',
    'buttonSelectEstatusVDH',
    'buttonRemoveEstatusVDH',
    'buttonEstatusdelavictima',
    'buttonRemoveEstatusdelavictima',
    'ActualizarActo',
    'btnActoLegislacion',
    'btnActoInstrInt', 'LA1','LA2','LA14']
    
camposEntidad['fuentePersonal']=['staticTextFtePersona', 'delFuentePer',
    'staticTextRelPersona',
    'checkBoxFteConfidencialidad',
    'choiceFteTipoFecha',
    'choiceFteIdioma',
    'btnAddFteLenguaIndigena',
    'btnDelFteLenguaIndigena',
    'textCtrlFteObservaciones',
    'btnAddFteConfiabilidad',
    'btnDelFteConfiabilidad',
    'textCtrlFteComentarios',
    'buttonFteNueva',
    'btnAddFtePersonaRel',
    'btnRemoveFtePersonaRel',
    'buttonFteConexionInformacion',
    'buttonRemoveFteConexionInf',
    'buttonFteActualizarDatos',
    'staticTextConexionInfo',
    'staticFteLenguaIndigena',
    'staticFteConfiabilidad'
    ]
    
camposEntidad['fuenteDocumental']=['textCtrlPubTituloParte', 
                                    'textCtrlPubDatos' ,
                                   'textCtrlPubNombreSitio', 
                                   'textCtrlPubLigaSitio', 
                                   'textCtrlPubObservaciones', 
                                   'textCtrlPubObservaciones', 
                                   'delFuenteDoc',
                                   'btnAddDocLenguaIndigena', 
                                   'btnDelDocLenguaIndigena', 
                                   'choicePubIdioma', 
                                   'txtPubTipoPub', 
                                   'choicePubTipoFecha',
                                   'btnAddPubConfiabilidad',
                                   'btnDelPubConfiabilidad',
                                   'btnAddDoc',
                                    'btnSavePub',
                                    'btnPubTipoPub',
                                    'btnRemovePubTipoPub',
                                    'buttonPubAddPerson',
                                    'buttonPubRemovePerson', 'checkBoxPubExportar',
                                    'staticDocLenguaIndigena',
                                    'staticPubConfiabilidad',
                                    'choicePubTipofechaconsulta',
                                    'staticTextPubPersona',
                                    'textCtrlPubComentarios'
                                    
                                   ]
                   
camposEntidad['involucramiento'] = ['FIperpetrador', 'delPerpetrator',
                                    'FIgradoinvolucramiento', 
                                    'FItipoperpetrador',
                                    'FIultimostatusperpetrador',
                                    'textCtrlINObservaciones',
                                    'buttonAddPerpetrador',
                                    'buttonActualizarInvol',
                                    'buttonSelPerpetrador',
                                    'buttonSelGradoInvol',
                                    'buttonRemoveGradoInvol',
                                    'buttonSelTipoPerp',
                                    'buttonRemoveTipoPerp',
                                    'buttonSelUltStatusPerp',
                                    'buttonRemoveUltStatusPerp']   
                                                    
camposEntidad['intervenciones']=['staticText17', 'delInterv',
                                'txtIntParte',
                                
                                'staticText19', 
                                'staticText18', 
                                #'txtIntEstatus', 
                                'txtIntImpacto', 
                                'txtIntRespuesta',
                                'txtIntObservaciones',
                                'txtIntComentarios',
                                'choiceIntTipofecha',
                                'buttonTipoIntervencion',
                                #'buttonRemoveTipoIntervencion',
                                'buttonDeQuien',
                                'buttonRemoveDequien',
                                'btnIntPInt',
                                #'btnRemoveIntPInt',
                                'buttonAQuien',
                                'buttonRemoveAquien',
                                #'btnIntEstatus',
                                #'buttonRemoveIntEstatus',
                                'buttonAddIntervencion',
                                'buttonIntervencionActualizar', 'checkBoxIntExportar',
                                'IFanio','IFdia','IFmes']

camposEntidad['persona']=['delIdioma',
                        'btnAddOcupacion',
                        'staticFPTipo', 'delPersona',
                          
                          'btnAddFPTipo',
                          'btnDelFPTipo',
                        
                        'FPconfidencialidad',
                        'FPNombre',
                        'FPApellido',
                        'FPOtroNombre',
                        'FPSexo',
                        'FPTipodefecha',
                        'FPTipodefecharecepcion',
                        'FPPais',
                        'FPEstado',
                        'FPMunicipio',
                        'FPLocalidad',
                        'FPCiudadania',
                        'FPEscolaridad',
                        'listPersonaVinculosDB',
                        'FPstrOcupacion',
                        'FPIdioma',
                        'FPHablayentiendeespanol',
                        'FPLengua',
                        'FPOrigenEtnico',
                        'FPReligion',
                        'FPEstadocivil',
                        'FPNodependientes',
                        'FPDescripciondelgrupo',
                        'FPDirecciones',
                        'FPMonitoreo',
                        'FPObservaciones',
                        'FPComentarios',
                        'FPArchivos',
                        'FPproyecto_grupo',
                        'FPproyecto_conjunto',
                        'FPproyecto_se',
                        'listBoxVinculos',
                        'FBDescripcion',
                        'FBConfidencialidad',
                        'FBFechaInicialTipo',
                        'FBFechaFinalTipo',
                        'FBFechaInfo_vigenteTipo',
                        'FBObservaciones',
                        'FBPuesto',
                        'FBComentarios',
                        'FBRango',
                        'btnFPPais',
                        'btnRemoveFPPais',
                        'btnFPCiudadania',
                        'btnRemoveFPCiudadania',
                        
                        'btnDelOcupacion',
                        'FPAddIdioma',
                        'FPAddLengua',
                        'FPAddOrigenEtnico',
                        'FPAddDirecciones',
                        'Pguardar2',
                        'Pguardar3',
                        'buttonVincular',
                        'btnTipoVinculo',
                        'btnPrelacionada',
                        'btnSaveVinculo',
                        'buttonPGuardar',
                        'btnCambiaTipoPersona']
camposEntidad['persona2']=['btnCambiaTipoPersona',
                            'btnAddOcupacion',
                            'btnDelOcupacion',
                            'FPAddIdioma',
                            'FPHablayentiendeespanol',
                            'FPAddLengua',
                            'delLengua',
                            'FPAddOrigenEtnico',
                            'delOrigen',
                            'FPAddDirecciones',
                            'delDireccion',
                            'Pguardar2',
                            'delIdioma'
                           ]                        
camposEntidad['persona3']=[ 'Pguardar3']
camposEntidad['DetalleBiografico']=['buttonVincular', 'delDatoBio', 'buttonVincular',
'FBDescripcion',
'btnTipoVinculo',
'btnPrelacionada',
'FBFechaInicialTipo',
'BFIdia',
'BFImes',
'BFIanio',
'FBFechaFinalTipo',
'BFFdia',
'BFFmes',
'BFFanio',
'FBFechaInfo_vigenteTipo',
'BFVdia',
'BFVmes',
'BFVanio',
'FBObservaciones',
'FBComentarios',
'FBPuesto',
'FBRango',
'btnSaveVinculo']
                        
camposEntidad['reportes']=['btnSaveCfg','btnSaveCfgAs','delModelo']                        
                        
                        

boxEntidad={'acto':['listActos','listBoxPerpetradores'],'intervenciones':['listBoxIntervenciones'],
            'fuentePersonal':['listBoxFte'], 'fuenteDocumental':['listBoxDocs'],
            'intervenciones':['listBoxIntervenciones']
           }
