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
    db.dlogin.insert( f0= 'pb2968', f1= '(2968)Username')
    db.dlogin.insert( f0= 'pb2969', f1= '(2969)Password')
    db.dlogin.insert( f0= 'bu2970', f1= '(2970)Sign in')
    db.dlogin.insert( f0= 'pc2971', f1= '(2971)Enter your valid e-mail')
    db.dlogin.insert( f0= 'pb2972', f1= '(2972)mail@domain.com')
    db.dlogin.insert( f0= 'bu2973', f1= '(2973)Recover Password')
    db.dlogin.insert( f0= 'pb2974', f1= '(2974)username')
    db.dlogin.insert( f0= 'pb2975', f1= '(2975)mail@domain.com')
    db.dlogin.insert( f0= 'pb2976', f1= '(2976)password')
    db.dlogin.insert( f0= 'pb2977', f1= '(2977)re-password')
    db.dlogin.insert( f0= 'bu2978', f1= '(2978)Register')
    db.dlogin.insert( f0= 'aa2979', f1= '(2979)Login')
    db.dlogin.insert( f0= 'aa2980', f1= '(2980)Forgot Password')
    db.dlogin.insert( f0= 'aa2981', f1= '(2981)Signup')
    db.commit()
#
