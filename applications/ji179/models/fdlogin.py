#
# table for controller: login
#

from gluon.contrib.populate import populate

db.define_table('dlogin', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dlogin.id ).count():
    db.dlogin.insert( f0= 'di207', f1= '(207)Login')
    db.dlogin.insert( f0= 'pb208', f1= '(208)Email address')
    db.dlogin.insert( f0= 'pb209', f1= '(209)Password')
    db.commit()
#
