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
    db.dlogin.insert( f0= 'ha725', f1= '(725)Welcome Back!')
    db.dlogin.insert( f0= 'pb726', f1= '(726)Enter Email Address...')
    db.dlogin.insert( f0= 'pb727', f1= '(727)Password')
    db.dlogin.insert( f0= 'aa732', f1= '(732)Forgot Password?')
    db.dlogin.insert( f0= 'aa734', f1= '(734)Create an Account!')
    db.commit()
#
