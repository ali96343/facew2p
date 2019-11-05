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
    db.dlogin.insert( f0= 'bb5276', f1= '(5276)Admin')
    db.dlogin.insert( f0= 'pc5277', f1= '(5277)Sign in to start your session')
    db.dlogin.insert( f0= 'pb5279', f1= '(5279)Email')
    db.dlogin.insert( f0= 'pb5280', f1= '(5280)Password')
    db.dlogin.insert( f0= 'bu5281', f1= '(5281)Sign In')
    db.dlogin.insert( f0= 'pa5282', f1= '(5282)- OR -')
    db.dlogin.insert( f0= 'aa5284', f1= '(5284)I forgot my password')
    db.dlogin.insert( f0= 'aa5286', f1= '(5286)Register a new membership')
    db.commit()
#
