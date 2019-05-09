#
# table for controller: lock
#

from gluon.contrib.populate import populate

db.define_table('dlock', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dlock.id ).count():
    populate(db.dlock, 5)
    db.commit()
#
