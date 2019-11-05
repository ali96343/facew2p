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
    db.dlockscreen.insert( f0= 'bb3907', f1= '(3907)Admin')
    db.dlockscreen.insert( f0= 'di3908', f1= '(3908)John Doe')
    db.dlockscreen.insert( f0= 'pb3910', f1= '(3910)password')
    db.dlockscreen.insert( f0= 'aa3912', f1= '(3912)Or sign in as a different user')
    db.commit()
#
