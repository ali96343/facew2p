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
    db.dlogin.insert( f0= 'di225', f1= '(225)Login')
    db.dlogin.insert( f0= 'pb226', f1= '(226)Email address')
    db.dlogin.insert( f0= 'pb227', f1= '(227)Password')
    db.dlogin.insert( f0= 'aa229', f1= '(229)Login')
    db.dlogin.insert( f0= 'aa231', f1= '(231)Register an Account')
    db.dlogin.insert( f0= 'aa233', f1= '(233)Forgot Password?')
    db.commit()
#
