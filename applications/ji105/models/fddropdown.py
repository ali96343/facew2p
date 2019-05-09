#
# table for controller: dropdown
#

from gluon.contrib.populate import populate

db.define_table('ddropdown', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.ddropdown.id ).count():
    populate(db.ddropdown, 5)
    db.commit()
#
