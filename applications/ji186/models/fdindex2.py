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
    db.dindex2.insert( f0= 'hd778', f1= '(778)john doe')
    db.dindex2.insert( f0= 'aa779', f1= '(779)Sign out')
    db.dindex2.insert( f0= 'pb803', f1= '(803)Search for datas &amp; reports...')
    db.dindex2.insert( f0= 'pa804', f1= '(804)You have 3 Notifications')
    db.dindex2.insert( f0= 'pa805', f1= '(805)You got a email notification')
    db.dindex2.insert( f0= 'sx806', f1= '(806)April 12, 2018 06:50')
    db.dindex2.insert( f0= 'pa807', f1= '(807)Your account has been blocked')
    db.dindex2.insert( f0= 'sx808', f1= '(808)April 12, 2018 06:50')
    db.dindex2.insert( f0= 'pa809', f1= '(809)You got a new file')
    db.dindex2.insert( f0= 'sx810', f1= '(810)April 12, 2018 06:50')
    db.dindex2.insert( f0= 'aa811', f1= '(811)All notifications')
    db.dindex2.insert( f0= 'hd814', f1= '(814)john doe')
    db.dindex2.insert( f0= 'aa815', f1= '(815)Sign out')
    db.dindex2.insert( f0= 'sx838', f1= '(838)You are here:')
    db.dindex2.insert( f0= 'aa839', f1= '(839)Home')
    db.dindex2.insert( f0= 'lb840', f1= '(840)Dashboard')
    db.dindex2.insert( f0= 'hb841', f1= '(841)10,368')
    db.dindex2.insert( f0= 'sx842', f1= '(842)members online')
    db.dindex2.insert( f0= 'hb843', f1= '(843)388,688')
    db.dindex2.insert( f0= 'sx844', f1= '(844)items sold')
    db.dindex2.insert( f0= 'hb845', f1= '(845)1,086')
    db.dindex2.insert( f0= 'sx846', f1= '(846)this week')
    db.dindex2.insert( f0= 'hb847', f1= '(847)$1,060,386')
    db.dindex2.insert( f0= 'sx848', f1= '(848)total earnings')
    db.dindex2.insert( f0= 'hc849', f1= '(849)recent reports')
    db.dindex2.insert( f0= 'sp850', f1= '(850)products')
    db.dindex2.insert( f0= 'sp851', f1= '(851)Services')
    db.dindex2.insert( f0= 'hc852', f1= '(852)task progress')
    db.dindex2.insert( f0= 'sx853', f1= '(853)Web Design')
    db.dindex2.insert( f0= 'sx854', f1= '(854)HTML5/CSS3')
    db.dindex2.insert( f0= 'sx855', f1= '(855)WordPress')
    db.dindex2.insert( f0= 'sx856', f1= '(856)Support')
    db.dindex2.insert( f0= 'hh857', f1= '(857)lori lynch')
    db.dindex2.insert( f0= 'aa858', f1= '(858)johndoe@gmail.com')
    db.dindex2.insert( f0= 'sx859', f1= '(859)admin')
    db.dindex2.insert( f0= 'hh860', f1= '(860)lori lynch')
    db.dindex2.insert( f0= 'aa861', f1= '(861)johndoe@gmail.com')
    db.dindex2.insert( f0= 'sx862', f1= '(862)user')
    db.dindex2.insert( f0= 'hh863', f1= '(863)lori lynch')
    db.dindex2.insert( f0= 'aa864', f1= '(864)johndoe@gmail.com')
    db.dindex2.insert( f0= 'sx865', f1= '(865)user')
    db.dindex2.insert( f0= 'hh866', f1= '(866)lori lynch')
    db.dindex2.insert( f0= 'aa867', f1= '(867)johndoe@gmail.com')
    db.dindex2.insert( f0= 'sx868', f1= '(868)member')
    db.dindex2.insert( f0= 'bu869', f1= '(869)load more')
    db.commit()
#
