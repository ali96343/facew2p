#
# table for controller: lockscreen
#

from gluon.contrib.populate import populate

db.define_table('dlockscreen', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dlockscreen.id ).count():
    db.dlockscreen.insert( f0= 'bb3716', f1= '(3716)Admin')
    db.dlockscreen.insert( f0= 'di3717', f1= '(3717)John Doe')
    db.dlockscreen.insert( f0= 'pb3719', f1= '(3719)password')
    db.dlockscreen.insert( f0= 'aa3721', f1= '(3721)Or sign in as a different user')
    db.commit()
#
