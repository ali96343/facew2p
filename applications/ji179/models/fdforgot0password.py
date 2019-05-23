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
    db.dforgot0password.insert( f0= 'di241', f1= '(241)Reset Password')
    db.dforgot0password.insert( f0= 'hh242', f1= '(242)Forgot your password?')
    db.dforgot0password.insert( f0= 'pa243', f1= '(243)Enter your email address and we will send you instructions on how to reset your password.')
    db.dforgot0password.insert( f0= 'pb244', f1= '(244)Enter email address')
    db.dforgot0password.insert( f0= 'aa246', f1= '(246)Reset Password')
    db.dforgot0password.insert( f0= 'aa248', f1= '(248)Register an Account')
    db.dforgot0password.insert( f0= 'aa250', f1= '(250)Login Page')
    db.commit()
#
