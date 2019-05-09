#
# table for controller: register
#

from gluon.contrib.populate import populate

db.define_table('dregister', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dregister.id ).count():
    db.dregister.insert( f0= 'di267', f1= '(267)Register an Account')
    db.dregister.insert( f0= 'pb268', f1= '(268)First name')
    db.dregister.insert( f0= 'pb269', f1= '(269)Last name')
    db.dregister.insert( f0= 'pb270', f1= '(270)Email address')
    db.dregister.insert( f0= 'pb271', f1= '(271)Password')
    db.dregister.insert( f0= 'pb272', f1= '(272)Confirm password')
    db.dregister.insert( f0= 'aa274', f1= '(274)Register')
    db.dregister.insert( f0= 'aa276', f1= '(276)Login Page')
    db.dregister.insert( f0= 'aa278', f1= '(278)Forgot Password?')
    db.commit()
#
