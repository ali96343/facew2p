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
    db.dregister.insert( f0= 'bb4495', f1= '(4495)Admin')
    db.dregister.insert( f0= 'pc4496', f1= '(4496)Register a new membership')
    db.dregister.insert( f0= 'pb4497', f1= '(4497)Full name')
    db.dregister.insert( f0= 'pb4498', f1= '(4498)Email')
    db.dregister.insert( f0= 'pb4499', f1= '(4499)Password')
    db.dregister.insert( f0= 'pb4500', f1= '(4500)Retype password')
    db.dregister.insert( f0= 'aa4501', f1= '(4501)terms')
    db.dregister.insert( f0= 'bu4502', f1= '(4502)Register')
    db.dregister.insert( f0= 'pa4503', f1= '(4503)- OR -')
    db.dregister.insert( f0= 'aa4505', f1= '(4505)I already have a membership')
    db.commit()
#
