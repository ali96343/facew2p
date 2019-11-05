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
    db.dregister.insert( f0= 'bb6288', f1= '(6288)Admin')
    db.dregister.insert( f0= 'pc6289', f1= '(6289)Register a new membership')
    db.dregister.insert( f0= 'pb6291', f1= '(6291)Full name')
    db.dregister.insert( f0= 'pb6292', f1= '(6292)Email')
    db.dregister.insert( f0= 'pb6293', f1= '(6293)Password')
    db.dregister.insert( f0= 'pb6294', f1= '(6294)Retype password')
    db.dregister.insert( f0= 'aa6295', f1= '(6295)terms')
    db.dregister.insert( f0= 'bu6296', f1= '(6296)Register')
    db.dregister.insert( f0= 'pa6297', f1= '(6297)- OR -')
    db.dregister.insert( f0= 'aa6299', f1= '(6299)I already have a membership')
    db.commit()
#
