#
# table for controller: page_login
#

from gluon.contrib.populate import populate

db.define_table('dpage0login', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dpage0login.id ).count():
    db.dpage0login.insert( f0= 'pb267', f1= '(267)Email')
    db.dpage0login.insert( f0= 'pb268', f1= '(268)Password')
    db.dpage0login.insert( f0= 'aa269', f1= '(269)Forgotten Password?')
    db.dpage0login.insert( f0= 'bu270', f1= '(270)Sign in')
    db.dpage0login.insert( f0= 'pf271', f1= '(271)Don t have account ?')
    db.dpage0login.insert( f0= 'aa272', f1= '(272)Sign Up Here')
    db.commit()
#
