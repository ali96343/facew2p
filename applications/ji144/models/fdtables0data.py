#
# table for controller: tables_data
#

from gluon.contrib.populate import populate

db.define_table('dtables0data', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtables0data.id ).count():
    populate(db.dtables0data, 5)
    db.commit()
#
