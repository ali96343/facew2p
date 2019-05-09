#
# table for controller: alert
#

from gluon.contrib.populate import populate

db.define_table('dalert', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dalert.id ).count():
    populate(db.dalert, 5)
    db.commit()
#
