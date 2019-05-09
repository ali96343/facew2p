#
# table for controller: wizard
#

from gluon.contrib.populate import populate

db.define_table('dwizard', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dwizard.id ).count():
    populate(db.dwizard, 5)
    db.commit()
#
