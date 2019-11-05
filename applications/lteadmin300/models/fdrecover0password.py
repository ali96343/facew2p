#
# table for controller: recoverIIpassword
#

from gluon.contrib.populate import populate

db.define_table('drecover0password', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.drecover0password.id ).count():
    db.drecover0password.insert( f0= 'bb5682', f1= '(5682)Admin')
    db.drecover0password.insert( f0= 'pc5683', f1= '(5683)You are only one step a way from your new password, recover your password now.')
    db.drecover0password.insert( f0= 'pb5685', f1= '(5685)Password')
    db.drecover0password.insert( f0= 'pb5686', f1= '(5686)Confirm Password')
    db.drecover0password.insert( f0= 'bu5687', f1= '(5687)Change password')
    db.drecover0password.insert( f0= 'aa5689', f1= '(5689)Login')
    db.commit()
#
