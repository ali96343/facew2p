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
    db.dblank.insert( f0= 'aa6', f1= '(6)Start Bootstrap')
    db.dblank.insert( f0= 'pb7', f1= '(7)Search for...')
    db.dblank.insert( f0= 'sx8', f1= '(8)9+')
    db.dblank.insert( f0= 'aa9', f1= '(9)Action')
    db.dblank.insert( f0= 'aa10', f1= '(10)Another action')
    db.dblank.insert( f0= 'aa11', f1= '(11)Something else here')
    db.dblank.insert( f0= 'aa12', f1= '(12)Action')
    db.dblank.insert( f0= 'aa13', f1= '(13)Another action')
    db.dblank.insert( f0= 'aa14', f1= '(14)Something else here')
    db.dblank.insert( f0= 'aa15', f1= '(15)Settings')
    db.dblank.insert( f0= 'aa16', f1= '(16)Activity Log')
    db.dblank.insert( f0= 'aa17', f1= '(17)Logout')
    db.dblank.insert( f0= 'sp19', f1= '(19)Dashboard')
    db.dblank.insert( f0= 'sp20', f1= '(20)Pages')
    db.dblank.insert( f0= 'hf21', f1= '(21)Login Screens:')
    db.dblank.insert( f0= 'aa23', f1= '(23)Login')
    db.dblank.insert( f0= 'aa25', f1= '(25)Register')
    db.dblank.insert( f0= 'aa27', f1= '(27)Forgot Password')
    db.dblank.insert( f0= 'hf28', f1= '(28)Other Pages:')
    db.dblank.insert( f0= 'aa30', f1= '(30)404 Page')
    db.dblank.insert( f0= 'aa32', f1= '(32)Blank Page')
    db.dblank.insert( f0= 'sp34', f1= '(34)Charts')
    db.dblank.insert( f0= 'sp36', f1= '(36)Tables')
    db.dblank.insert( f0= 'aa38', f1= '(38)Dashboard')
    db.dblank.insert( f0= 'lb39', f1= '(39)Blank Page')
    db.dblank.insert( f0= 'hh40', f1= '(40)Blank Page')
    db.dblank.insert( f0= 'pa41', f1= '(41)This is a great starting point for new custom pages.')
    db.dblank.insert( f0= 'sp42', f1= '(42)Copyright  Your Website 2019')
    db.dblank.insert( f0= 'he43', f1= '(43)Ready to Leave?')
    db.dblank.insert( f0= 'sx44', f1= '(44)')
    db.dblank.insert( f0= 'di45', f1= '(45)Select Logout below if you are ready to end your current session.')
    db.dblank.insert( f0= 'bu46', f1= '(46)Cancel')
    db.dblank.insert( f0= 'aa48', f1= '(48)Logout')
    db.commit()
#
