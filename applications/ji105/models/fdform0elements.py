#
# table for controller: form_elements
#

from gluon.contrib.populate import populate

db.define_table('dform0elements', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dform0elements.id ).count():
    populate(db.dform0elements, 5)
    db.commit()
#
