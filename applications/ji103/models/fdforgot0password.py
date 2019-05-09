#
# table for controller: forgot_password
#

from gluon.contrib.populate import populate

db.define_table('dforgot0password', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dforgot0password.id ).count():
    db.dforgot0password.insert( f0= 'di249', f1= '(249)Reset Password')
    db.dforgot0password.insert( f0= 'hh250', f1= '(250)Forgot your password?')
    db.dforgot0password.insert( f0= 'pa251', f1= '(251)Enter your email address and we will send you instructions on how to reset your password.')
    db.dforgot0password.insert( f0= 'pb252', f1= '(252)Enter email address')
    db.dforgot0password.insert( f0= 'aa254', f1= '(254)Reset Password')
    db.dforgot0password.insert( f0= 'aa256', f1= '(256)Register an Account')
    db.dforgot0password.insert( f0= 'aa258', f1= '(258)Login Page')
    db.commit()
#
