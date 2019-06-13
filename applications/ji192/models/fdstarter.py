#
# table for controller: starter
#

from gluon.contrib.populate import populate

db.define_table('dstarter', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dstarter.id ).count():
    db.dstarter.insert( f0= 'sx5823', f1= '(5823)LT')
    db.dstarter.insert( f0= 'bb5824', f1= '(5824)Admin')
    db.dstarter.insert( f0= 'sx5825', f1= '(5825)LTE')
    db.dstarter.insert( f0= 'sx5826', f1= '(5826)Toggle navigation')
    db.dstarter.insert( f0= 'lb5827', f1= '(5827)You have 4 messages')
    db.dstarter.insert( f0= 'ib5829', f1= '(5829)5 mins')
    db.dstarter.insert( f0= 'pa5830', f1= '(5830)Why not buy a new awesome theme?')
    db.dstarter.insert( f0= 'aa5831', f1= '(5831)See All Messages')
    db.dstarter.insert( f0= 'sx5832', f1= '(5832)10')
    db.dstarter.insert( f0= 'lb5833', f1= '(5833)You have 10 notifications')
    db.dstarter.insert( f0= 'aa5834', f1= '(5834)View all')
    db.dstarter.insert( f0= 'lb5835', f1= '(5835)You have 9 tasks')
    db.dstarter.insert( f0= 'ic5836', f1= '(5836)20%')
    db.dstarter.insert( f0= 'sx5837', f1= '(5837)20% Complete')
    db.dstarter.insert( f0= 'aa5838', f1= '(5838)View all tasks')
    db.dstarter.insert( f0= 'sx5840', f1= '(5840)Alexander Pierce')
    db.dstarter.insert( f0= 'ic5842', f1= '(5842)Member since Nov. 2012')
    db.dstarter.insert( f0= 'aa5843', f1= '(5843)Followers')
    db.dstarter.insert( f0= 'aa5844', f1= '(5844)Sales')
    db.dstarter.insert( f0= 'aa5845', f1= '(5845)Friends')
    db.dstarter.insert( f0= 'aa5846', f1= '(5846)Profile')
    db.dstarter.insert( f0= 'aa5847', f1= '(5847)Sign out')
    db.dstarter.insert( f0= 'pa5849', f1= '(5849)Alexander Pierce')
    db.dstarter.insert( f0= 'ia5850', f1= '(5850)Online')
    db.dstarter.insert( f0= 'pb5851', f1= '(5851)Search...')
    db.dstarter.insert( f0= 'lb5852', f1= '(5852)HEADER')
    db.dstarter.insert( f0= 'sp5853', f1= '(5853)Link')
    db.dstarter.insert( f0= 'sp5854', f1= '(5854)Another Link')
    db.dstarter.insert( f0= 'sp5855', f1= '(5855)Multilevel')
    db.dstarter.insert( f0= 'aa5856', f1= '(5856)Link in level 2')
    db.dstarter.insert( f0= 'aa5857', f1= '(5857)Link in level 2')
    db.dstarter.insert( f0= 'ic5858', f1= '(5858)Optional description')
    db.dstarter.insert( f0= 'ia5859', f1= '(5859)Level')
    db.dstarter.insert( f0= 'lb5860', f1= '(5860)Here')
    db.dstarter.insert( f0= 'aa5861', f1= '(5861)Company')
    db.dstarter.insert( f0= 'hc5862', f1= '(5862)Recent Activity')
    db.dstarter.insert( f0= 'hd5863', f1= '(5863)Langdon s Birthday')
    db.dstarter.insert( f0= 'pa5864', f1= '(5864)Will be 23 on April 24th')
    db.dstarter.insert( f0= 'hc5865', f1= '(5865)Tasks Progress')
    db.dstarter.insert( f0= 'sx5866', f1= '(5866)70%')
    db.dstarter.insert( f0= 'di5867', f1= '(5867)Stats Tab Content')
    db.dstarter.insert( f0= 'hc5868', f1= '(5868)General Settings')
    db.commit()
#
