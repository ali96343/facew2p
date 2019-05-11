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
    db.dregister.insert( f0= 'di234', f1= '(234)Register an Account')
    db.dregister.insert( f0= 'pb235', f1= '(235)First name')
    db.dregister.insert( f0= 'pb236', f1= '(236)Last name')
    db.dregister.insert( f0= 'pb237', f1= '(237)Email address')
    db.dregister.insert( f0= 'pb238', f1= '(238)Password')
    db.dregister.insert( f0= 'pb239', f1= '(239)Confirm password')
    db.commit()
#
