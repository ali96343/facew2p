#
# table for controller: forms_basic
#

from gluon.contrib.populate import populate

db.define_table('dforms0basic', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dforms0basic.id ).count():
    populate(db.dforms0basic, 5)
    db.commit()
#
