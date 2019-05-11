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
    db.dregister.insert( f0= 'pb1658', f1= '(1658)Username')
    db.dregister.insert( f0= 'pb1659', f1= '(1659)Email')
    db.dregister.insert( f0= 'pb1660', f1= '(1660)Password')
    db.dregister.insert( f0= 'bu1661', f1= '(1661)register')
    db.dregister.insert( f0= 'bu1662', f1= '(1662)register with twitter')
    db.dregister.insert( f0= 'aa1663', f1= '(1663)Sign In')
    db.commit()
#
