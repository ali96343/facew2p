#
# table for controller: password_meter
#

from gluon.contrib.populate import populate

db.define_table('dpassword0meter', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dpassword0meter.id ).count():
    populate(db.dpassword0meter, 5)
    db.commit()
#
