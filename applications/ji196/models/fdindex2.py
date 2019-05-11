#
# table for controller: index2
#

from gluon.contrib.populate import populate

db.define_table('dindex2', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dindex2.id ).count():
    db.dindex2.insert( f0= 'hd791', f1= '(791)john doe')
    db.dindex2.insert( f0= 'aa792', f1= '(792)Sign out')
    db.dindex2.insert( f0= 'sx798', f1= '(798)3')
    db.dindex2.insert( f0= 'pb817', f1= '(817)Search for datas &amp; reports...')
    db.dindex2.insert( f0= 'pa818', f1= '(818)You have 3 Notifications')
    db.dindex2.insert( f0= 'pa819', f1= '(819)You got a email notification')
    db.dindex2.insert( f0= 'sx820', f1= '(820)April 12, 2018 06:50')
    db.dindex2.insert( f0= 'pa821', f1= '(821)Your account has been blocked')
    db.dindex2.insert( f0= 'sx822', f1= '(822)April 12, 2018 06:50')
    db.dindex2.insert( f0= 'pa823', f1= '(823)You got a new file')
    db.dindex2.insert( f0= 'sx824', f1= '(824)April 12, 2018 06:50')
    db.dindex2.insert( f0= 'aa825', f1= '(825)All notifications')
    db.dindex2.insert( f0= 'hd828', f1= '(828)john doe')
    db.dindex2.insert( f0= 'aa829', f1= '(829)Sign out')
    db.dindex2.insert( f0= 'sx835', f1= '(835)3')
    db.dindex2.insert( f0= 'sx853', f1= '(853)You are here:')
    db.dindex2.insert( f0= 'aa854', f1= '(854)Home')
    db.dindex2.insert( f0= 'sp855', f1= '(855)/')
    db.dindex2.insert( f0= 'lb856', f1= '(856)Dashboard')
    db.dindex2.insert( f0= 'hb857', f1= '(857)10,368')
    db.dindex2.insert( f0= 'sx858', f1= '(858)members online')
    db.dindex2.insert( f0= 'hb859', f1= '(859)388,688')
    db.dindex2.insert( f0= 'sx860', f1= '(860)items sold')
    db.dindex2.insert( f0= 'hb861', f1= '(861)1,086')
    db.dindex2.insert( f0= 'sx862', f1= '(862)this week')
    db.dindex2.insert( f0= 'hb863', f1= '(863)$1,060,386')
    db.dindex2.insert( f0= 'sx864', f1= '(864)total earnings')
    db.dindex2.insert( f0= 'hc865', f1= '(865)recent reports')
    db.dindex2.insert( f0= 'sp866', f1= '(866)products')
    db.dindex2.insert( f0= 'sp867', f1= '(867)Services')
    db.dindex2.insert( f0= 'hc868', f1= '(868)task progress')
    db.dindex2.insert( f0= 'sx869', f1= '(869)Web Design')
    db.dindex2.insert( f0= 'sx870', f1= '(870)HTML5/CSS3')
    db.dindex2.insert( f0= 'sx871', f1= '(871)WordPress')
    db.dindex2.insert( f0= 'sx872', f1= '(872)Support')
    db.dindex2.insert( f0= 'hh873', f1= '(873)lori lynch')
    db.dindex2.insert( f0= 'aa874', f1= '(874)johndoe@gmail.com')
    db.dindex2.insert( f0= 'sx875', f1= '(875)admin')
    db.dindex2.insert( f0= 'hh876', f1= '(876)lori lynch')
    db.dindex2.insert( f0= 'aa877', f1= '(877)johndoe@gmail.com')
    db.dindex2.insert( f0= 'sx878', f1= '(878)user')
    db.dindex2.insert( f0= 'hh879', f1= '(879)lori lynch')
    db.dindex2.insert( f0= 'aa880', f1= '(880)johndoe@gmail.com')
    db.dindex2.insert( f0= 'sx881', f1= '(881)user')
    db.dindex2.insert( f0= 'hh882', f1= '(882)lori lynch')
    db.dindex2.insert( f0= 'aa883', f1= '(883)johndoe@gmail.com')
    db.dindex2.insert( f0= 'sx884', f1= '(884)member')
    db.dindex2.insert( f0= 'bu885', f1= '(885)load more')
    db.dindex2.insert( f0= 'pc891', f1= '(891).')
    db.dindex2.insert( f0= 'pf892', f1= '(892)Copyright  2018 Colorlib. All rights reserved. Template by')
    db.dindex2.insert( f0= 'aa893', f1= '(893)Colorlib')
    db.commit()
#
