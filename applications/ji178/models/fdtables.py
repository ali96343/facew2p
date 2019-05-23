#
# table for controller: tables
#

from gluon.contrib.populate import populate

db.define_table('dtables', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtables.id ).count():
    db.dtables.insert( f0= 'sp521', f1= '(521)Dashboard')
    db.dtables.insert( f0= 'sp522', f1= '(522)Components')
    db.dtables.insert( f0= 'hf523', f1= '(523)Custom Components:')
    db.dtables.insert( f0= 'aa525', f1= '(525)Buttons')
    db.dtables.insert( f0= 'aa527', f1= '(527)Cards')
    db.dtables.insert( f0= 'sp528', f1= '(528)Utilities')
    db.dtables.insert( f0= 'hf529', f1= '(529)Custom Utilities:')
    db.dtables.insert( f0= 'aa531', f1= '(531)Colors')
    db.dtables.insert( f0= 'aa533', f1= '(533)Borders')
    db.dtables.insert( f0= 'aa535', f1= '(535)Animations')
    db.dtables.insert( f0= 'aa537', f1= '(537)Other')
    db.dtables.insert( f0= 'sp538', f1= '(538)Pages')
    db.dtables.insert( f0= 'hf539', f1= '(539)Login Screens:')
    db.dtables.insert( f0= 'aa541', f1= '(541)Login')
    db.dtables.insert( f0= 'aa543', f1= '(543)Register')
    db.dtables.insert( f0= 'aa545', f1= '(545)Forgot Password')
    db.dtables.insert( f0= 'hf546', f1= '(546)Other Pages:')
    db.dtables.insert( f0= 'aa548', f1= '(548)404 Page')
    db.dtables.insert( f0= 'aa550', f1= '(550)Blank Page')
    db.dtables.insert( f0= 'sp552', f1= '(552)Charts')
    db.dtables.insert( f0= 'sp554', f1= '(554)Tables')
    db.dtables.insert( f0= 'pb555', f1= '(555)Search for...')
    db.dtables.insert( f0= 'pb556', f1= '(556)Search for...')
    db.dtables.insert( f0= 'sx557', f1= '(557)3+')
    db.dtables.insert( f0= 'di558', f1= '(558)December 12, 2019')
    db.dtables.insert( f0= 'sx559', f1= '(559)A new monthly report is ready to download!')
    db.dtables.insert( f0= 'di560', f1= '(560)December 7, 2019')
    db.dtables.insert( f0= 'di561', f1= '(561)December 2, 2019')
    db.dtables.insert( f0= 'aa562', f1= '(562)Show All Alerts')
    db.dtables.insert( f0= 'di563', f1= '(563)Hi there! I am wondering if you can help me with a problem I ve been having.')
    db.dtables.insert( f0= 'di564', f1= '(564)Emily Fowler  58m')
    db.dtables.insert( f0= 'di565', f1= '(565)I have the photos that you ordered last month, how would you like them sent to you?')
    db.dtables.insert( f0= 'di566', f1= '(566)Jae Chun  1d')
    db.dtables.insert( f0= 'di567', f1= '(567)Last month s report looks great, I am very happy with the progress so far, keep up the good work!')
    db.dtables.insert( f0= 'di568', f1= '(568)Morgan Alvarez  2d')
    db.dtables.insert( f0= 'di569', f1= '(569)Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren t good...')
    db.dtables.insert( f0= 'di570', f1= '(570)Chicken the Dog  2w')
    db.dtables.insert( f0= 'aa571', f1= '(571)Read More Messages')
    db.dtables.insert( f0= 'sx572', f1= '(572)Valerie Luna')
    db.dtables.insert( f0= 'ha573', f1= '(573)Tables')
    db.dtables.insert( f0= 'aa574', f1= '(574)official DataTables documentation')
    db.dtables.insert( f0= 'hf575', f1= '(575)DataTables Example')
    db.dtables.insert( f0= 'sp633', f1= '(633)Copyright &copy; Your Website 2019')
    db.dtables.insert( f0= 'he634', f1= '(634)Ready to Leave?')
    db.dtables.insert( f0= 'sx635', f1= '(635)')
    db.dtables.insert( f0= 'di636', f1= '(636)Select Logout below if you are ready to end your current session.')
    db.dtables.insert( f0= 'bu637', f1= '(637)Cancel')
    db.dtables.insert( f0= 'aa639', f1= '(639)Logout')
    db.commit()
#
