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
    db.dblank.insert( f0= 'sp7', f1= '(7)Dashboard')
    db.dblank.insert( f0= 'sp8', f1= '(8)Components')
    db.dblank.insert( f0= 'hf9', f1= '(9)Custom Components:')
    db.dblank.insert( f0= 'aa11', f1= '(11)Buttons')
    db.dblank.insert( f0= 'aa13', f1= '(13)Cards')
    db.dblank.insert( f0= 'sp14', f1= '(14)Utilities')
    db.dblank.insert( f0= 'hf15', f1= '(15)Custom Utilities:')
    db.dblank.insert( f0= 'aa17', f1= '(17)Colors')
    db.dblank.insert( f0= 'aa19', f1= '(19)Borders')
    db.dblank.insert( f0= 'aa21', f1= '(21)Animations')
    db.dblank.insert( f0= 'aa23', f1= '(23)Other')
    db.dblank.insert( f0= 'sp24', f1= '(24)Pages')
    db.dblank.insert( f0= 'hf25', f1= '(25)Login Screens:')
    db.dblank.insert( f0= 'aa27', f1= '(27)Login')
    db.dblank.insert( f0= 'aa29', f1= '(29)Register')
    db.dblank.insert( f0= 'aa31', f1= '(31)Forgot Password')
    db.dblank.insert( f0= 'hf32', f1= '(32)Other Pages:')
    db.dblank.insert( f0= 'aa34', f1= '(34)404 Page')
    db.dblank.insert( f0= 'aa36', f1= '(36)Blank Page')
    db.dblank.insert( f0= 'sp38', f1= '(38)Charts')
    db.dblank.insert( f0= 'sp40', f1= '(40)Tables')
    db.dblank.insert( f0= 'pb41', f1= '(41)Search for...')
    db.dblank.insert( f0= 'pb42', f1= '(42)Search for...')
    db.dblank.insert( f0= 'sx43', f1= '(43)3+')
    db.dblank.insert( f0= 'di44', f1= '(44)December 12, 2019')
    db.dblank.insert( f0= 'sx45', f1= '(45)A new monthly report is ready to download!')
    db.dblank.insert( f0= 'di46', f1= '(46)December 7, 2019')
    db.dblank.insert( f0= 'di47', f1= '(47)December 2, 2019')
    db.dblank.insert( f0= 'aa48', f1= '(48)Show All Alerts')
    db.dblank.insert( f0= 'di49', f1= '(49)Hi there! I am wondering if you can help me with a problem I ve been having.')
    db.dblank.insert( f0= 'di50', f1= '(50)Emily Fowler  58m')
    db.dblank.insert( f0= 'di51', f1= '(51)I have the photos that you ordered last month, how would you like them sent to you?')
    db.dblank.insert( f0= 'di52', f1= '(52)Jae Chun  1d')
    db.dblank.insert( f0= 'di53', f1= '(53)Last month s report looks great, I am very happy with the progress so far, keep up the good work!')
    db.dblank.insert( f0= 'di54', f1= '(54)Morgan Alvarez  2d')
    db.dblank.insert( f0= 'di55', f1= '(55)Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren t good...')
    db.dblank.insert( f0= 'di56', f1= '(56)Chicken the Dog  2w')
    db.dblank.insert( f0= 'aa57', f1= '(57)Read More Messages')
    db.dblank.insert( f0= 'sx58', f1= '(58)Valerie Luna')
    db.dblank.insert( f0= 'ha59', f1= '(59)Blank Page')
    db.dblank.insert( f0= 'sp60', f1= '(60)Copyright &copy; Your Website 2019')
    db.dblank.insert( f0= 'he61', f1= '(61)Ready to Leave?')
    db.dblank.insert( f0= 'sx62', f1= '(62)')
    db.dblank.insert( f0= 'di63', f1= '(63)Select Logout below if you are ready to end your current session.')
    db.dblank.insert( f0= 'bu64', f1= '(64)Cancel')
    db.dblank.insert( f0= 'aa66', f1= '(66)Logout')
    db.commit()
#
