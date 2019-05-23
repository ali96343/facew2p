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
    db.dregister.insert( f0= 'di258', f1= '(258)Register an Account')
    db.dregister.insert( f0= 'pb259', f1= '(259)First name')
    db.dregister.insert( f0= 'pb260', f1= '(260)Last name')
    db.dregister.insert( f0= 'pb261', f1= '(261)Email address')
    db.dregister.insert( f0= 'pb262', f1= '(262)Password')
    db.dregister.insert( f0= 'pb263', f1= '(263)Confirm password')
    db.dregister.insert( f0= 'aa265', f1= '(265)Register')
    db.dregister.insert( f0= 'aa267', f1= '(267)Login Page')
    db.dregister.insert( f0= 'aa269', f1= '(269)Forgot Password?')
    db.commit()
#
