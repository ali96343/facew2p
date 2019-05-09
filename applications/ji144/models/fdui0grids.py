#
# table for controller: ui_grids
#

from gluon.contrib.populate import populate

db.define_table('dui0grids', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dui0grids.id ).count():
    populate(db.dui0grids, 5)
    db.commit()
#
