#
# table for controller: utilities_border
#

from gluon.contrib.populate import populate

db.define_table('dutilities0border', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dutilities0border.id ).count():
    db.dutilities0border.insert( f0= 'sp572', f1= '(572)Dashboard')
    db.dutilities0border.insert( f0= 'sp573', f1= '(573)Components')
    db.dutilities0border.insert( f0= 'hf574', f1= '(574)Custom Components:')
    db.dutilities0border.insert( f0= 'sp577', f1= '(577)Utilities')
    db.dutilities0border.insert( f0= 'hf578', f1= '(578)Custom Utilities:')
    db.dutilities0border.insert( f0= 'sp583', f1= '(583)Pages')
    db.dutilities0border.insert( f0= 'hf584', f1= '(584)Login Screens:')
    db.dutilities0border.insert( f0= 'hf588', f1= '(588)Other Pages:')
    db.dutilities0border.insert( f0= 'sp592', f1= '(592)Charts')
    db.dutilities0border.insert( f0= 'sp594', f1= '(594)Tables')
    db.dutilities0border.insert( f0= 'pb595', f1= '(595)Search for...')
    db.dutilities0border.insert( f0= 'pb596', f1= '(596)Search for...')
    db.dutilities0border.insert( f0= 'sx597', f1= '(597)3+')
    db.dutilities0border.insert( f0= 'di598', f1= '(598)December 12, 2019')
    db.dutilities0border.insert( f0= 'sx599', f1= '(599)A new monthly report is ready to download!')
    db.dutilities0border.insert( f0= 'di600', f1= '(600)December 7, 2019')
    db.dutilities0border.insert( f0= 'di601', f1= '(601)December 2, 2019')
    db.dutilities0border.insert( f0= 'aa602', f1= '(602)Show All Alerts')
    db.dutilities0border.insert( f0= 'sx603', f1= '(603)7')
    db.dutilities0border.insert( f0= 'di604', f1= '(604)Hi there! I am wondering if you can help me with a problem I ve been having.')
    db.dutilities0border.insert( f0= 'di605', f1= '(605)Emily Fowler  58m')
    db.dutilities0border.insert( f0= 'di606', f1= '(606)I have the photos that you ordered last month, how would you like them sent to you?')
    db.dutilities0border.insert( f0= 'di607', f1= '(607)Jae Chun  1d')
    db.dutilities0border.insert( f0= 'di608', f1= '(608)Morgan Alvarez  2d')
    db.dutilities0border.insert( f0= 'di609', f1= '(609)Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren t good...')
    db.dutilities0border.insert( f0= 'di610', f1= '(610)Chicken the Dog  2w')
    db.dutilities0border.insert( f0= 'aa611', f1= '(611)Read More Messages')
    db.dutilities0border.insert( f0= 'sx612', f1= '(612)Valerie Luna')
    db.dutilities0border.insert( f0= 'ha613', f1= '(613)Border Utilities')
    db.dutilities0border.insert( f0= 'pc614', f1= '(614)page. The custom utilities below were created to extend this theme past the default utility classes built into Bootstrap s framework.')
    db.dutilities0border.insert( f0= 'aa615', f1= '(615)Bootstrap Documentation')
    db.dutilities0border.insert( f0= 'sp616', f1= '(616)Copyright &copy; Your Website 2019')
    db.dutilities0border.insert( f0= 'he617', f1= '(617)Ready to Leave?')
    db.dutilities0border.insert( f0= 'sx618', f1= '(618)')
    db.dutilities0border.insert( f0= 'di619', f1= '(619)Select Logout below if you are ready to end your current session.')
    db.dutilities0border.insert( f0= 'bu620', f1= '(620)Cancel')
    db.commit()
#
