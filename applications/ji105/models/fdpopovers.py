#
# table for controller: popovers
#

from gluon.contrib.populate import populate

db.define_table('dpopovers', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dpopovers.id ).count():
    populate(db.dpopovers, 5)
    db.commit()
#
