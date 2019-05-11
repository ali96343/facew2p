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
    db.dblank.insert( f0= 'sp12', f1= '(12)Utilities')
    db.dblank.insert( f0= 'hf13', f1= '(13)Custom Utilities:')
    db.dblank.insert( f0= 'sp18', f1= '(18)Pages')
    db.dblank.insert( f0= 'hf19', f1= '(19)Login Screens:')
    db.dblank.insert( f0= 'hf23', f1= '(23)Other Pages:')
    db.dblank.insert( f0= 'sp27', f1= '(27)Charts')
    db.dblank.insert( f0= 'sp29', f1= '(29)Tables')
    db.dblank.insert( f0= 'pb30', f1= '(30)Search for...')
    db.dblank.insert( f0= 'pb31', f1= '(31)Search for...')
    db.dblank.insert( f0= 'sx32', f1= '(32)3+')
    db.dblank.insert( f0= 'di33', f1= '(33)December 12, 2019')
    db.dblank.insert( f0= 'sx34', f1= '(34)A new monthly report is ready to download!')
    db.dblank.insert( f0= 'di35', f1= '(35)December 7, 2019')
    db.dblank.insert( f0= 'di36', f1= '(36)December 2, 2019')
    db.dblank.insert( f0= 'aa37', f1= '(37)Show All Alerts')
    db.dblank.insert( f0= 'sx38', f1= '(38)7')
    db.dblank.insert( f0= 'di39', f1= '(39)Hi there! I am wondering if you can help me with a problem I ve been having.')
    db.dblank.insert( f0= 'di40', f1= '(40)Emily Fowler  58m')
    db.dblank.insert( f0= 'di41', f1= '(41)I have the photos that you ordered last month, how would you like them sent to you?')
    db.dblank.insert( f0= 'di42', f1= '(42)Jae Chun  1d')
    db.dblank.insert( f0= 'di43', f1= '(43)Morgan Alvarez  2d')
    db.dblank.insert( f0= 'di44', f1= '(44)Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren t good...')
    db.dblank.insert( f0= 'di45', f1= '(45)Chicken the Dog  2w')
    db.dblank.insert( f0= 'aa46', f1= '(46)Read More Messages')
    db.dblank.insert( f0= 'sx47', f1= '(47)Valerie Luna')
    db.dblank.insert( f0= 'ha48', f1= '(48)Blank Page')
    db.dblank.insert( f0= 'sp49', f1= '(49)Copyright &copy; Your Website 2019')
    db.dblank.insert( f0= 'he50', f1= '(50)Ready to Leave?')
    db.dblank.insert( f0= 'sx51', f1= '(51)')
    db.dblank.insert( f0= 'di52', f1= '(52)Select Logout below if you are ready to end your current session.')
    db.dblank.insert( f0= 'bu53', f1= '(53)Cancel')
    db.commit()
#
