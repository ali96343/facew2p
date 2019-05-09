#
# table for controller: data_maps
#

from gluon.contrib.populate import populate

db.define_table('ddata0maps', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.ddata0maps.id ).count():
    populate(db.ddata0maps, 5)
    db.commit()
#
