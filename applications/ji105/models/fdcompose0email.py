#
# table for controller: compose_email
#

from gluon.contrib.populate import populate

db.define_table('dcompose0email', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcompose0email.id ).count():
    populate(db.dcompose0email, 5)
    db.commit()
#
