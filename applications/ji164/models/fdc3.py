#
# table for controller: c3
#

from gluon.contrib.populate import populate

db.define_table('dc3', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dc3.id ).count():
    populate(db.dc3, 5)
    db.commit()
#
