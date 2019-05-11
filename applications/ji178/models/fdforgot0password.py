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
    db.dforgot0password.insert( f0= 'ha648', f1= '(648)Forgot Your Password?')
    db.dforgot0password.insert( f0= 'pc649', f1= '(649)We get it, stuff happens. Just enter your email address below and we ll send you a link to reset your password!')
    db.dforgot0password.insert( f0= 'pb650', f1= '(650)Enter Email Address...')
    db.commit()
#
