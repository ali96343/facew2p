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
    db.dlogin.insert( f0= 'bb3476', f1= '(3476)Admin')
    db.dlogin.insert( f0= 'pc3477', f1= '(3477)Sign in to start your session')
    db.dlogin.insert( f0= 'pb3478', f1= '(3478)Email')
    db.dlogin.insert( f0= 'pb3479', f1= '(3479)Password')
    db.dlogin.insert( f0= 'bu3480', f1= '(3480)Sign In')
    db.dlogin.insert( f0= 'pa3481', f1= '(3481)- OR -')
    db.dlogin.insert( f0= 'aa3482', f1= '(3482)I forgot my password')
    db.dlogin.insert( f0= 'aa3484', f1= '(3484)Register a new membership')
    db.commit()
#
