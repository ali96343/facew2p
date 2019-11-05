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
    db.dregister.insert( f0= 'bb4656', f1= '(4656)Admin')
    db.dregister.insert( f0= 'pc4657', f1= '(4657)Register a new membership')
    db.dregister.insert( f0= 'pb4659', f1= '(4659)Full name')
    db.dregister.insert( f0= 'pb4660', f1= '(4660)Email')
    db.dregister.insert( f0= 'pb4661', f1= '(4661)Password')
    db.dregister.insert( f0= 'pb4662', f1= '(4662)Retype password')
    db.dregister.insert( f0= 'aa4663', f1= '(4663)terms')
    db.dregister.insert( f0= 'bu4664', f1= '(4664)Register')
    db.dregister.insert( f0= 'pa4665', f1= '(4665)- OR -')
    db.dregister.insert( f0= 'aa4667', f1= '(4667)I already have a membership')
    db.commit()
#
