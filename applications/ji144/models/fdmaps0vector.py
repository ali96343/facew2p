#
# table for controller: maps_vector
#

from gluon.contrib.populate import populate

db.define_table('dmaps0vector', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dmaps0vector.id ).count():
    populate(db.dmaps0vector, 5)
    db.commit()
#
