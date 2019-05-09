#
# table for controller: form_components
#

from gluon.contrib.populate import populate

db.define_table('dform0components', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dform0components.id ).count():
    populate(db.dform0components, 5)
    db.commit()
#
