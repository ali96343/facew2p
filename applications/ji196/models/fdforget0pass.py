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
    db.dforget0pass.insert( f0= 'pb3198', f1= '(3198)Email')
    db.dforget0pass.insert( f0= 'bu3199', f1= '(3199)submit')
    db.commit()
#
