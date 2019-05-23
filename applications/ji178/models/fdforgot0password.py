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
    db.dforgot0password.insert( f0= 'ha744', f1= '(744)Forgot Your Password?')
    db.dforgot0password.insert( f0= 'pc745', f1= '(745)We get it, stuff happens. Just enter your email address below and we ll send you a link to reset your password!')
    db.dforgot0password.insert( f0= 'pb746', f1= '(746)Enter Email Address...')
    db.dforgot0password.insert( f0= 'aa749', f1= '(749)Create an Account!')
    db.dforgot0password.insert( f0= 'aa751', f1= '(751)Already have an account? Login!')
    db.commit()
#
