#
# table for controller: X404
#

from gluon.contrib.populate import populate

db.define_table('d404', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.d404.id ).count():
    db.d404.insert( f0= 'sp859', f1= '(859)Dashboard')
    db.d404.insert( f0= 'sp860', f1= '(860)Components')
    db.d404.insert( f0= 'hf861', f1= '(861)Custom Components:')
    db.d404.insert( f0= 'sp864', f1= '(864)Utilities')
    db.d404.insert( f0= 'hf865', f1= '(865)Custom Utilities:')
    db.d404.insert( f0= 'sp870', f1= '(870)Pages')
    db.d404.insert( f0= 'hf871', f1= '(871)Login Screens:')
    db.d404.insert( f0= 'hf875', f1= '(875)Other Pages:')
    db.d404.insert( f0= 'sp879', f1= '(879)Charts')
    db.d404.insert( f0= 'sp881', f1= '(881)Tables')
    db.d404.insert( f0= 'pb882', f1= '(882)Search for...')
    db.d404.insert( f0= 'pb883', f1= '(883)Search for...')
    db.d404.insert( f0= 'sx884', f1= '(884)3+')
    db.d404.insert( f0= 'di885', f1= '(885)December 12, 2019')
    db.d404.insert( f0= 'sx886', f1= '(886)A new monthly report is ready to download!')
    db.d404.insert( f0= 'di887', f1= '(887)December 7, 2019')
    db.d404.insert( f0= 'di888', f1= '(888)December 2, 2019')
    db.d404.insert( f0= 'aa889', f1= '(889)Show All Alerts')
    db.d404.insert( f0= 'sx890', f1= '(890)7')
    db.d404.insert( f0= 'di891', f1= '(891)Hi there! I am wondering if you can help me with a problem I ve been having.')
    db.d404.insert( f0= 'di892', f1= '(892)Emily Fowler  58m')
    db.d404.insert( f0= 'di893', f1= '(893)I have the photos that you ordered last month, how would you like them sent to you?')
    db.d404.insert( f0= 'di894', f1= '(894)Jae Chun  1d')
    db.d404.insert( f0= 'di895', f1= '(895)Morgan Alvarez  2d')
    db.d404.insert( f0= 'di896', f1= '(896)Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren t good...')
    db.d404.insert( f0= 'di897', f1= '(897)Chicken the Dog  2w')
    db.d404.insert( f0= 'aa898', f1= '(898)Read More Messages')
    db.d404.insert( f0= 'sx899', f1= '(899)Valerie Luna')
    db.d404.insert( f0= 'di900', f1= '(900)404')
    db.d404.insert( f0= 'pc901', f1= '(901)Page Not Found')
    db.d404.insert( f0= 'pc902', f1= '(902)It looks like you found a glitch in the matrix...')
    db.d404.insert( f0= 'aa904', f1= '(904)&larr; Back to Dashboard')
    db.d404.insert( f0= 'sp905', f1= '(905)Copyright &copy; Your Website 2019')
    db.d404.insert( f0= 'he906', f1= '(906)Ready to Leave?')
    db.d404.insert( f0= 'sx907', f1= '(907)')
    db.d404.insert( f0= 'di908', f1= '(908)Select Logout below if you are ready to end your current session.')
    db.d404.insert( f0= 'bu909', f1= '(909)Cancel')
    db.commit()
#
