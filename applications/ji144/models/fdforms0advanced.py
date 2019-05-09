#
# table for controller: forms_advanced
#

from gluon.contrib.populate import populate

db.define_table('dforms0advanced', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dforms0advanced.id ).count():
    populate(db.dforms0advanced, 5)
    db.commit()
#
