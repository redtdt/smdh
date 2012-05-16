#-----------------------------------------------------------------------------
# Name:        modulosqlimg.py
#
#
# RCS-ID:      $Id: modulosqlimg.py $
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
from sqlalchemy import MetaData, Table, Column, Sequence, ForeignKey
from sqlalchemy import Integer, String, sql, Date, TEXT, Unicode, create_engine, Binary
from sqlalchemy.orm import create_session, mapper, relation, backref, aliased
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.orm import PropComparator, column_property, deferred
import videocap



#db='imagenes'
#user='admin'
#passwd='redtdt'
#host='localhost'
#spec = 'postgres://'+user+':'+passwd+'@'+host+'/'+db
#metadata = MetaData(spec)   
uni=False

def GeneraImagen(metadata, dataObject):
    

    imagen = Table('imagen',metadata,
              
            Column('id',Integer,
                   Sequence('pagina_id_seq', optional=True), primary_key=True),
            Column('imagen', Binary()),
            Column('nombre',TEXT(convert_unicode=uni)),
            Column('tipo',Integer)

            )

    class Imagen(dataObject):
        "imagen"
        def __init__(self):
            self.nombre = ''

    ImagenMapper = mapper(Imagen,imagen)
    return imagen, Imagen, ImagenMapper


#engine = create_engine(spec, echo=False)
#session = create_session(bind=engine)
#metadata.create_all()

def obtieneFoto(self, status):
    if not hasattr(status, 'cam'):
        status.cam=None
    if not status.cam:
        status.cam = videocap.initCam()
    if not status.cam:
        print "no hay camara!!!!"
        return None
    videocap.Snapshot(status.cam, "tmpfoto.jpg")
    contenido=file2Field("tmpfoto.jpg")
    if contenido:
        Img = status.Imagen()
        Img.imagen= contenido
        status.session.add(Img)
        status.session.flush()
        id = Img.id
        Img2=status.session.query(status.Imagen).filter(status.Imagen.id == id).first()
        contenido2 = Img2.imagen
        field2File(contenido2, "0123.jpg")
        return True
    return None
        


def file2Field(name):
    f=file(name, 'rb')
    contenido = f.read()
    f.close()
    return contenido

def field2File(contenido, name, path=None):
    f=file(str(path)+name, 'wb')
    f.write(contenido)
    f.close()


