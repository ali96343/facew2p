#
# table for controller: page_login
#

from gluon.contrib.populate import populate

db.define_table('dpage0login', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dpage0login.id ).count():
    populate(db.dpage0login, 5)
    db.commit()
#
