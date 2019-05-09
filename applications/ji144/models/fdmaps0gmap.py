#
# table for controller: maps_gmap
#

from gluon.contrib.populate import populate

db.define_table('dmaps0gmap', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dmaps0gmap.id ).count():
    populate(db.dmaps0gmap, 5)
    db.commit()
#
