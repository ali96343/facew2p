#
# table for controller: peity
#

from gluon.contrib.populate import populate

db.define_table('dpeity', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dpeity.id ).count():
    populate(db.dpeity, 5)
    db.commit()
#
