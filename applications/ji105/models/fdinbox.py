#
# table for controller: inbox
#

from gluon.contrib.populate import populate

db.define_table('dinbox', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dinbox.id ).count():
    populate(db.dinbox, 5)
    db.commit()
#
