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
    db.dblank.insert( f0= 'aa7', f1= '(7)Start Bootstrap')
    db.dblank.insert( f0= 'pb8', f1= '(8)Search for...')
    db.dblank.insert( f0= 'sx9', f1= '(9)9+')
    db.dblank.insert( f0= 'aa10', f1= '(10)Action')
    db.dblank.insert( f0= 'aa11', f1= '(11)Another action')
    db.dblank.insert( f0= 'aa12', f1= '(12)Something else here')
    db.dblank.insert( f0= 'sx13', f1= '(13)7')
    db.dblank.insert( f0= 'aa14', f1= '(14)Action')
    db.dblank.insert( f0= 'aa15', f1= '(15)Another action')
    db.dblank.insert( f0= 'aa16', f1= '(16)Something else here')
    db.dblank.insert( f0= 'aa17', f1= '(17)Settings')
    db.dblank.insert( f0= 'aa18', f1= '(18)Activity Log')
    db.dblank.insert( f0= 'aa19', f1= '(19)Logout')
    db.dblank.insert( f0= 'sp21', f1= '(21)Dashboard')
    db.dblank.insert( f0= 'sp22', f1= '(22)Pages')
    db.dblank.insert( f0= 'hf23', f1= '(23)Login Screens:')
    db.dblank.insert( f0= 'aa25', f1= '(25)Login')
    db.dblank.insert( f0= 'aa27', f1= '(27)Register')
    db.dblank.insert( f0= 'aa29', f1= '(29)Forgot Password')
    db.dblank.insert( f0= 'hf30', f1= '(30)Other Pages:')
    db.dblank.insert( f0= 'aa32', f1= '(32)404 Page')
    db.dblank.insert( f0= 'aa34', f1= '(34)Blank Page')
    db.dblank.insert( f0= 'sp36', f1= '(36)Charts')
    db.dblank.insert( f0= 'sp38', f1= '(38)Tables')
    db.dblank.insert( f0= 'aa40', f1= '(40)Dashboard')
    db.dblank.insert( f0= 'lb41', f1= '(41)Blank Page')
    db.dblank.insert( f0= 'hh42', f1= '(42)Blank Page')
    db.dblank.insert( f0= 'pa43', f1= '(43)This is a great starting point for new custom pages.')
    db.dblank.insert( f0= 'sp44', f1= '(44)Copyright  Your Website 2018')
    db.dblank.insert( f0= 'he45', f1= '(45)Ready to Leave?')
    db.dblank.insert( f0= 'sx46', f1= '(46)')
    db.dblank.insert( f0= 'di47', f1= '(47)Select Logout below if you are ready to end your current session.')
    db.dblank.insert( f0= 'bu48', f1= '(48)Cancel')
    db.dblank.insert( f0= 'aa50', f1= '(50)Logout')
    db.commit()
#
