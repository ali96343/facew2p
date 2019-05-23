#
# table for controller: page_register
#

from gluon.contrib.populate import populate

db.define_table('dpage0register', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dpage0register.id ).count():
    db.dpage0register.insert( f0= 'pb145', f1= '(145)User Name')
    db.dpage0register.insert( f0= 'pb146', f1= '(146)Email')
    db.dpage0register.insert( f0= 'pb147', f1= '(147)Password')
    db.dpage0register.insert( f0= 'bu148', f1= '(148)Register')
    db.dpage0register.insert( f0= 'pf149', f1= '(149)Already have account ?')
    db.dpage0register.insert( f0= 'aa150', f1= '(150)Sign in')
    db.commit()
#
