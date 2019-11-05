#
# table for controller: forgotIIpassword
#

from gluon.contrib.populate import populate

db.define_table('dforgot0password', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dforgot0password.id ).count():
    db.dforgot0password.insert( f0= 'bb5699', f1= '(5699)Admin')
    db.dforgot0password.insert( f0= 'pc5700', f1= '(5700)You forgot your password? Here you can easily retrieve a new password.')
    db.dforgot0password.insert( f0= 'pb5702', f1= '(5702)Email')
    db.dforgot0password.insert( f0= 'bu5703', f1= '(5703)Request new password')
    db.dforgot0password.insert( f0= 'aa5705', f1= '(5705)Login')
    db.dforgot0password.insert( f0= 'aa5707', f1= '(5707)Register a new membership')
    db.commit()
#
