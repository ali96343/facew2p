#
# table for controller: password_recovery
#

from gluon.contrib.populate import populate

db.define_table('dpassword0recovery', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dpassword0recovery.id ).count():
    populate(db.dpassword0recovery, 5)
    db.commit()
#
