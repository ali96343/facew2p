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
    db.dregister.insert( f0= 'bb6420', f1= '(6420)Admin')
    db.dregister.insert( f0= 'pc6421', f1= '(6421)Register a new membership')
    db.dregister.insert( f0= 'pb6423', f1= '(6423)Full name')
    db.dregister.insert( f0= 'pb6424', f1= '(6424)Email')
    db.dregister.insert( f0= 'pb6425', f1= '(6425)Password')
    db.dregister.insert( f0= 'pb6426', f1= '(6426)Retype password')
    db.dregister.insert( f0= 'aa6427', f1= '(6427)terms')
    db.dregister.insert( f0= 'bu6428', f1= '(6428)Register')
    db.dregister.insert( f0= 'pa6429', f1= '(6429)- OR -')
    db.dregister.insert( f0= 'aa6431', f1= '(6431)I already have a membership')
    db.commit()
#
