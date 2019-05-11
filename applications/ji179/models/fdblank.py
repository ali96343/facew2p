#
# table for controller: blank
#

from gluon.contrib.populate import populate

db.define_table('dblank', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dblank.id ).count():
    db.dblank.insert( f0= 'pb6', f1= '(6)Search for...')
    db.dblank.insert( f0= 'sx7', f1= '(7)9+')
    db.dblank.insert( f0= 'aa8', f1= '(8)Action')
    db.dblank.insert( f0= 'aa9', f1= '(9)Another action')
    db.dblank.insert( f0= 'aa10', f1= '(10)Something else here')
    db.dblank.insert( f0= 'sx11', f1= '(11)7')
    db.dblank.insert( f0= 'aa12', f1= '(12)Action')
    db.dblank.insert( f0= 'aa13', f1= '(13)Another action')
    db.dblank.insert( f0= 'aa14', f1= '(14)Something else here')
    db.dblank.insert( f0= 'aa15', f1= '(15)Settings')
    db.dblank.insert( f0= 'aa16', f1= '(16)Activity Log')
    db.dblank.insert( f0= 'aa17', f1= '(17)Logout')
    db.dblank.insert( f0= 'sp19', f1= '(19)Dashboard')
    db.dblank.insert( f0= 'sp20', f1= '(20)Pages')
    db.dblank.insert( f0= 'hf21', f1= '(21)Login Screens:')
    db.dblank.insert( f0= 'hf25', f1= '(25)Other Pages:')
    db.dblank.insert( f0= 'sp29', f1= '(29)Charts')
    db.dblank.insert( f0= 'sp31', f1= '(31)Tables')
    db.dblank.insert( f0= 'aa33', f1= '(33)Dashboard')
    db.dblank.insert( f0= 'lb34', f1= '(34)Blank Page')
    db.dblank.insert( f0= 'hh35', f1= '(35)Blank Page')
    db.dblank.insert( f0= 'pa36', f1= '(36)This is a great starting point for new custom pages.')
    db.dblank.insert( f0= 'sp37', f1= '(37)Copyright  Your Website 2019')
    db.dblank.insert( f0= 'he38', f1= '(38)Ready to Leave?')
    db.dblank.insert( f0= 'sx39', f1= '(39)')
    db.dblank.insert( f0= 'di40', f1= '(40)Select Logout below if you are ready to end your current session.')
    db.dblank.insert( f0= 'bu41', f1= '(41)Cancel')
    db.commit()
#
