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
    db.dlogin.insert( f0= 'pb1065', f1= '(1065)Email')
    db.dlogin.insert( f0= 'pb1066', f1= '(1066)Password')
    db.dlogin.insert( f0= 'aa1067', f1= '(1067)Forgotten Password?')
    db.dlogin.insert( f0= 'bu1068', f1= '(1068)sign in')
    db.dlogin.insert( f0= 'bu1069', f1= '(1069)sign in with facebook')
    db.dlogin.insert( f0= 'bu1070', f1= '(1070)sign in with twitter')
    db.dlogin.insert( f0= 'aa1071', f1= '(1071)Sign Up Here')
    db.commit()
#
