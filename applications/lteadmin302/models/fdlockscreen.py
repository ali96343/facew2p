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
    db.dlockscreen.insert( f0= 'bb5836', f1= '(5836)Admin')
    db.dlockscreen.insert( f0= 'di5837', f1= '(5837)John Doe')
    db.dlockscreen.insert( f0= 'pb5839', f1= '(5839)password')
    db.dlockscreen.insert( f0= 'aa5841', f1= '(5841)Or sign in as a different user')
    db.dlockscreen.insert( f0= 'aa5842', f1= '(5842)AdminLTE.io')
    db.commit()
#
