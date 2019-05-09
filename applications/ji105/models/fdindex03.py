#
# table for controller: index_3
#

from gluon.contrib.populate import populate

db.define_table('dindex03', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dindex03.id ).count():
    populate(db.dindex03, 5)
    db.commit()
#
