#
# table for controller: login_register
#

from gluon.contrib.populate import populate

db.define_table('dlogin0register', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dlogin0register.id ).count():
    populate(db.dlogin0register, 5)
    db.commit()
#
