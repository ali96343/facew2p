#
# table for controller: ui_tabs
#

from gluon.contrib.populate import populate

db.define_table('dui0tabs', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dui0tabs.id ).count():
    populate(db.dui0tabs, 5)
    db.commit()
#
