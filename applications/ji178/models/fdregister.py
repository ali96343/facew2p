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
    db.dregister.insert( f0= 'ha663', f1= '(663)Create an Account!')
    db.dregister.insert( f0= 'pb664', f1= '(664)First Name')
    db.dregister.insert( f0= 'pb665', f1= '(665)Last Name')
    db.dregister.insert( f0= 'pb666', f1= '(666)Email Address')
    db.dregister.insert( f0= 'pb667', f1= '(667)Password')
    db.dregister.insert( f0= 'pb668', f1= '(668)Repeat Password')
    db.commit()
#
