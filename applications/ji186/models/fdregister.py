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
    db.dregister.insert( f0= 'pb1621', f1= '(1621)Username')
    db.dregister.insert( f0= 'pb1622', f1= '(1622)Email')
    db.dregister.insert( f0= 'pb1623', f1= '(1623)Password')
    db.dregister.insert( f0= 'bu1624', f1= '(1624)register')
    db.dregister.insert( f0= 'bu1625', f1= '(1625)register with facebook')
    db.dregister.insert( f0= 'bu1626', f1= '(1626)register with twitter')
    db.dregister.insert( f0= 'aa1627', f1= '(1627)Sign In')
    db.commit()
#
