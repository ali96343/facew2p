#
# table for controller: advance_form_element
#

from gluon.contrib.populate import populate

db.define_table('dadvance0form0element', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dadvance0form0element.id ).count():
    populate(db.dadvance0form0element, 5)
    db.commit()
#
