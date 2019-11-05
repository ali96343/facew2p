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
    db.dlockscreen.insert( f0= 'bb5716', f1= '(5716)Admin')
    db.dlockscreen.insert( f0= 'di5717', f1= '(5717)John Doe')
    db.dlockscreen.insert( f0= 'pb5719', f1= '(5719)password')
    db.dlockscreen.insert( f0= 'aa5721', f1= '(5721)Or sign in as a different user')
    db.dlockscreen.insert( f0= 'aa5722', f1= '(5722)AdminLTE.io')
    db.commit()
#
