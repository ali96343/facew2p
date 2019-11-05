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
    db.dlogin.insert( f0= 'bb3673', f1= '(3673)Admin')
    db.dlogin.insert( f0= 'pc3674', f1= '(3674)Sign in to start your session')
    db.dlogin.insert( f0= 'pb3676', f1= '(3676)Email')
    db.dlogin.insert( f0= 'pb3677', f1= '(3677)Password')
    db.dlogin.insert( f0= 'bu3678', f1= '(3678)Sign In')
    db.dlogin.insert( f0= 'pa3679', f1= '(3679)- OR -')
    db.dlogin.insert( f0= 'aa3680', f1= '(3680)I forgot my password')
    db.dlogin.insert( f0= 'aa3682', f1= '(3682)Register a new membership')
    db.commit()
#
