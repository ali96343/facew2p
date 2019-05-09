#
# table for controller: index_4
#

from gluon.contrib.populate import populate

db.define_table('dindex04', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dindex04.id ).count():
    populate(db.dindex04, 5)
    db.commit()
#
