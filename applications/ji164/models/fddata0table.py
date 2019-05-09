#
# table for controller: data_table
#

from gluon.contrib.populate import populate

db.define_table('ddata0table', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.ddata0table.id ).count():
    populate(db.ddata0table, 5)
    db.commit()
#
