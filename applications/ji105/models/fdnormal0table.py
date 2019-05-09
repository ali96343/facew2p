#
# table for controller: normal_table
#

from gluon.contrib.populate import populate

db.define_table('dnormal0table', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dnormal0table.id ).count():
    populate(db.dnormal0table, 5)
    db.commit()
#
