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
    db.dlogin.insert( f0= 'di232', f1= '(232)Login')
    db.dlogin.insert( f0= 'pb233', f1= '(233)Email address')
    db.dlogin.insert( f0= 'pb234', f1= '(234)Password')
    db.dlogin.insert( f0= 'aa236', f1= '(236)Login')
    db.dlogin.insert( f0= 'aa238', f1= '(238)Register an Account')
    db.dlogin.insert( f0= 'aa240', f1= '(240)Forgot Password?')
    db.commit()
#
