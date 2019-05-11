#
# table for controller: forget_pass
#

from gluon.contrib.populate import populate

db.define_table('dforget0pass', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dforget0pass.id ).count():
    db.dforget0pass.insert( f0= 'pb3275', f1= '(3275)Email')
    db.dforget0pass.insert( f0= 'bu3276', f1= '(3276)submit')
    db.commit()
#
