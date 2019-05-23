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
    db.dlogin.insert( f0= 'pb2863', f1= '(2863)Username')
    db.dlogin.insert( f0= 'pb2864', f1= '(2864)Password')
    db.dlogin.insert( f0= 'bu2865', f1= '(2865)Sign in')
    db.dlogin.insert( f0= 'pc2866', f1= '(2866)Enter your valid e-mail')
    db.dlogin.insert( f0= 'pb2867', f1= '(2867)mail@domain.com')
    db.dlogin.insert( f0= 'bu2868', f1= '(2868)Recover Password')
    db.dlogin.insert( f0= 'pb2869', f1= '(2869)username')
    db.dlogin.insert( f0= 'pb2870', f1= '(2870)mail@domain.com')
    db.dlogin.insert( f0= 'pb2871', f1= '(2871)password')
    db.dlogin.insert( f0= 'pb2872', f1= '(2872)re-password')
    db.dlogin.insert( f0= 'bu2873', f1= '(2873)Register')
    db.dlogin.insert( f0= 'aa2874', f1= '(2874)Login')
    db.dlogin.insert( f0= 'aa2875', f1= '(2875)Forgot Password')
    db.dlogin.insert( f0= 'aa2876', f1= '(2876)Signup')
    db.commit()
#
