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
    db.dlogin.insert( f0= 'bb5388', f1= '(5388)Admin')
    db.dlogin.insert( f0= 'pc5389', f1= '(5389)Sign in to start your session')
    db.dlogin.insert( f0= 'pb5391', f1= '(5391)Email')
    db.dlogin.insert( f0= 'pb5392', f1= '(5392)Password')
    db.dlogin.insert( f0= 'bu5393', f1= '(5393)Sign In')
    db.dlogin.insert( f0= 'pa5394', f1= '(5394)- OR -')
    db.dlogin.insert( f0= 'aa5396', f1= '(5396)I forgot my password')
    db.dlogin.insert( f0= 'aa5398', f1= '(5398)Register a new membership')
    db.commit()
#
