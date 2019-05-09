#
# table for controller: x_editable
#

from gluon.contrib.populate import populate

db.define_table('dx0editable', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dx0editable.id ).count():
    populate(db.dx0editable, 5)
    db.commit()
#
