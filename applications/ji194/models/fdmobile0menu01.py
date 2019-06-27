#
# table for controller: mobileIImenuII1
#

from gluon.contrib.populate import populate

db.define_table('dmobile0menu01', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dmobile0menu01.id ).count():
    db.dmobile0menu01.insert( f0= 'sx849', f1= '(849)Toggle sidebar')
    db.dmobile0menu01.insert( f0= 'sx851', f1= '(851)Software Update')
    db.dmobile0menu01.insert( f0= 'sx852', f1= '(852)65%')
    db.dmobile0menu01.insert( f0= 'sx853', f1= '(853)Hardware Upgrade')
    db.dmobile0menu01.insert( f0= 'sx854', f1= '(854)35%')
    db.dmobile0menu01.insert( f0= 'sx855', f1= '(855)Unit Testing')
    db.dmobile0menu01.insert( f0= 'sx856', f1= '(856)15%')
    db.dmobile0menu01.insert( f0= 'sx857', f1= '(857)Bug Fixes')
    db.dmobile0menu01.insert( f0= 'sx858', f1= '(858)90%')
    db.dmobile0menu01.insert( f0= 'sx859', f1= '(859)+12')
    db.dmobile0menu01.insert( f0= 'sx860', f1= '(860)+8')
    db.dmobile0menu01.insert( f0= 'sx861', f1= '(861)+11')
    db.dmobile0menu01.insert( f0= 'sx863', f1= '(863)Alex:')
    db.dmobile0menu01.insert( f0= 'sp864', f1= '(864)a moment ago')
    db.dmobile0menu01.insert( f0= 'sx866', f1= '(866)Susan:')
    db.dmobile0menu01.insert( f0= 'sp867', f1= '(867)20 minutes ago')
    db.dmobile0menu01.insert( f0= 'sx869', f1= '(869)Bob:')
    db.dmobile0menu01.insert( f0= 'sp870', f1= '(870)3:15 pm')
    db.dmobile0menu01.insert( f0= 'sx872', f1= '(872)Kate:')
    db.dmobile0menu01.insert( f0= 'sp873', f1= '(873)1:33 pm')
    db.dmobile0menu01.insert( f0= 'sx875', f1= '(875)Fred:')
    db.dmobile0menu01.insert( f0= 'sp876', f1= '(876)10:09 am')
    db.dmobile0menu01.insert( f0= 'ic879', f1= '(879)Welcome,')
    db.dmobile0menu01.insert( f0= 'sx882', f1= '(882)Dashboard')
    db.dmobile0menu01.insert( f0= 'sx896', f1= '(896)Tables')
    db.dmobile0menu01.insert( f0= 'sx899', f1= '(899)Forms')
    db.dmobile0menu01.insert( f0= 'sx906', f1= '(906)Widgets')
    db.dmobile0menu01.insert( f0= 'sx909', f1= '(909)Gallery')
    db.dmobile0menu01.insert( f0= 'sx910', f1= '(910)More Pages')
    db.dmobile0menu01.insert( f0= 'aa924', f1= '(924)Home')
    db.dmobile0menu01.insert( f0= 'aa925', f1= '(925)Layouts')
    db.dmobile0menu01.insert( f0= 'lb926', f1= '(926)Default Mobile Menu')
    db.dmobile0menu01.insert( f0= 'pb927', f1= '(927)Search ...')
    db.dmobile0menu01.insert( f0= 'bb928', f1= '(928).container')
    db.dmobile0menu01.insert( f0= 'hh929', f1= '(929)Default Responsive(mobile) Menu')
    db.dmobile0menu01.insert( f0= 'sx930', f1= '(930)mobile menu')
    db.dmobile0menu01.insert( f0= 'sx931', f1= '(931)992px')
    db.dmobile0menu01.insert( f0= 'sx932', f1= '(932)992px')
    db.dmobile0menu01.insert( f0= 'sx933', f1= '(933)Ace')
    db.dmobile0menu01.insert( f0= 'sx940', f1= '(940)Toggle sidebar')
    db.dmobile0menu01.insert( f0= 'sx941', f1= '(941)Toggle sidebar')
    db.commit()
#
