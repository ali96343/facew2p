#
# table for controller: X500
#

from gluon.contrib.populate import populate

db.define_table('d500', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.d500.id ).count():
    populate(db.d500, 5)
    db.commit()
#
