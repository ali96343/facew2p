#
# table for controller: index_2
#

from gluon.contrib.populate import populate

db.define_table('dindex02', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dindex02.id ).count():
    populate(db.dindex02, 5)
    db.commit()
#
