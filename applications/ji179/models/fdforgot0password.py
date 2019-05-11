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
    db.dforgot0password.insert( f0= 'di220', f1= '(220)Reset Password')
    db.dforgot0password.insert( f0= 'hh221', f1= '(221)Forgot your password?')
    db.dforgot0password.insert( f0= 'pa222', f1= '(222)Enter your email address and we will send you instructions on how to reset your password.')
    db.dforgot0password.insert( f0= 'pb223', f1= '(223)Enter email address')
    db.commit()
#
