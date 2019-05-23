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
    db.dutilities0border.insert( f0= 'sp654', f1= '(654)Dashboard')
    db.dutilities0border.insert( f0= 'sp655', f1= '(655)Components')
    db.dutilities0border.insert( f0= 'hf656', f1= '(656)Custom Components:')
    db.dutilities0border.insert( f0= 'aa658', f1= '(658)Buttons')
    db.dutilities0border.insert( f0= 'aa660', f1= '(660)Cards')
    db.dutilities0border.insert( f0= 'sp661', f1= '(661)Utilities')
    db.dutilities0border.insert( f0= 'hf662', f1= '(662)Custom Utilities:')
    db.dutilities0border.insert( f0= 'aa664', f1= '(664)Colors')
    db.dutilities0border.insert( f0= 'aa666', f1= '(666)Borders')
    db.dutilities0border.insert( f0= 'aa668', f1= '(668)Animations')
    db.dutilities0border.insert( f0= 'aa670', f1= '(670)Other')
    db.dutilities0border.insert( f0= 'sp671', f1= '(671)Pages')
    db.dutilities0border.insert( f0= 'hf672', f1= '(672)Login Screens:')
    db.dutilities0border.insert( f0= 'aa674', f1= '(674)Login')
    db.dutilities0border.insert( f0= 'aa676', f1= '(676)Register')
    db.dutilities0border.insert( f0= 'aa678', f1= '(678)Forgot Password')
    db.dutilities0border.insert( f0= 'hf679', f1= '(679)Other Pages:')
    db.dutilities0border.insert( f0= 'aa681', f1= '(681)404 Page')
    db.dutilities0border.insert( f0= 'aa683', f1= '(683)Blank Page')
    db.dutilities0border.insert( f0= 'sp685', f1= '(685)Charts')
    db.dutilities0border.insert( f0= 'sp687', f1= '(687)Tables')
    db.dutilities0border.insert( f0= 'pb688', f1= '(688)Search for...')
    db.dutilities0border.insert( f0= 'pb689', f1= '(689)Search for...')
    db.dutilities0border.insert( f0= 'sx690', f1= '(690)3+')
    db.dutilities0border.insert( f0= 'di691', f1= '(691)December 12, 2019')
    db.dutilities0border.insert( f0= 'sx692', f1= '(692)A new monthly report is ready to download!')
    db.dutilities0border.insert( f0= 'di693', f1= '(693)December 7, 2019')
    db.dutilities0border.insert( f0= 'di694', f1= '(694)December 2, 2019')
    db.dutilities0border.insert( f0= 'aa695', f1= '(695)Show All Alerts')
    db.dutilities0border.insert( f0= 'di696', f1= '(696)Hi there! I am wondering if you can help me with a problem I ve been having.')
    db.dutilities0border.insert( f0= 'di697', f1= '(697)Emily Fowler  58m')
    db.dutilities0border.insert( f0= 'di698', f1= '(698)I have the photos that you ordered last month, how would you like them sent to you?')
    db.dutilities0border.insert( f0= 'di699', f1= '(699)Jae Chun  1d')
    db.dutilities0border.insert( f0= 'di700', f1= '(700)Last month s report looks great, I am very happy with the progress so far, keep up the good work!')
    db.dutilities0border.insert( f0= 'di701', f1= '(701)Morgan Alvarez  2d')
    db.dutilities0border.insert( f0= 'di702', f1= '(702)Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren t good...')
    db.dutilities0border.insert( f0= 'di703', f1= '(703)Chicken the Dog  2w')
    db.dutilities0border.insert( f0= 'aa704', f1= '(704)Read More Messages')
    db.dutilities0border.insert( f0= 'sx705', f1= '(705)Valerie Luna')
    db.dutilities0border.insert( f0= 'ha706', f1= '(706)Border Utilities')
    db.dutilities0border.insert( f0= 'pc707', f1= '(707)page. The custom utilities below were created to extend this theme past the default utility classes built into Bootstrap s framework.')
    db.dutilities0border.insert( f0= 'aa708', f1= '(708)Bootstrap Documentation')
    db.dutilities0border.insert( f0= 'sp709', f1= '(709)Copyright &copy; Your Website 2019')
    db.dutilities0border.insert( f0= 'he710', f1= '(710)Ready to Leave?')
    db.dutilities0border.insert( f0= 'sx711', f1= '(711)')
    db.dutilities0border.insert( f0= 'di712', f1= '(712)Select Logout below if you are ready to end your current session.')
    db.dutilities0border.insert( f0= 'bu713', f1= '(713)Cancel')
    db.dutilities0border.insert( f0= 'aa715', f1= '(715)Logout')
    db.commit()
#
