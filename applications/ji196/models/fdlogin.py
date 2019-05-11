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
    db.dlogin.insert( f0= 'pb1090', f1= '(1090)Email')
    db.dlogin.insert( f0= 'pb1091', f1= '(1091)Password')
    db.dlogin.insert( f0= 'aa1092', f1= '(1092)Forgotten Password?')
    db.dlogin.insert( f0= 'bu1093', f1= '(1093)sign in')
    db.dlogin.insert( f0= 'bu1094', f1= '(1094)sign in with twitter')
    db.dlogin.insert( f0= 'aa1095', f1= '(1095)Sign Up Here')
    db.commit()
#
