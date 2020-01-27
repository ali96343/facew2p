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
    db.drecover0password.insert( f0= 'bb5802', f1= '(5802)Admin')
    db.drecover0password.insert( f0= 'pc5803', f1= '(5803)You are only one step a way from your new password, recover your password now.')
    db.drecover0password.insert( f0= 'pb5805', f1= '(5805)Password')
    db.drecover0password.insert( f0= 'pb5806', f1= '(5806)Confirm Password')
    db.drecover0password.insert( f0= 'bu5807', f1= '(5807)Change password')
    db.drecover0password.insert( f0= 'aa5809', f1= '(5809)Login')
    db.commit()
#
