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
    db.dforgot0password.insert( f0= 'bb5819', f1= '(5819)Admin')
    db.dforgot0password.insert( f0= 'pc5820', f1= '(5820)You forgot your password? Here you can easily retrieve a new password.')
    db.dforgot0password.insert( f0= 'pb5822', f1= '(5822)Email')
    db.dforgot0password.insert( f0= 'bu5823', f1= '(5823)Request new password')
    db.dforgot0password.insert( f0= 'aa5825', f1= '(5825)Login')
    db.dforgot0password.insert( f0= 'aa5827', f1= '(5827)Register a new membership')
    db.commit()
#
