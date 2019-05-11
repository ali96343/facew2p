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
    db.dlogin.insert( f0= 'ha631', f1= '(631)Welcome Back!')
    db.dlogin.insert( f0= 'pb632', f1= '(632)Enter Email Address...')
    db.dlogin.insert( f0= 'pb633', f1= '(633)Password')
    db.commit()
#
