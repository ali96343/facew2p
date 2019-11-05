#
# table for controller: topIInav
#

from gluon.contrib.populate import populate

db.define_table('dtop0nav', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtop0nav.id ).count():
    db.dtop0nav.insert( f0= 'bb5540', f1= '(5540)Admin')
    db.dtop0nav.insert( f0= 'sx5541', f1= '(5541)(current)')
    db.dtop0nav.insert( f0= 'aa5542', f1= '(5542)Link')
    db.dtop0nav.insert( f0= 'aa5543', f1= '(5543)Action')
    db.dtop0nav.insert( f0= 'aa5544', f1= '(5544)Another action')
    db.dtop0nav.insert( f0= 'aa5545', f1= '(5545)Something else here')
    db.dtop0nav.insert( f0= 'aa5546', f1= '(5546)Separated link')
    db.dtop0nav.insert( f0= 'aa5547', f1= '(5547)One more separated link')
    db.dtop0nav.insert( f0= 'pb5548', f1= '(5548)Search')
    db.dtop0nav.insert( f0= 'sx5549', f1= '(5549)4')
    db.dtop0nav.insert( f0= 'lb5550', f1= '(5550)You have 4 messages')
    db.dtop0nav.insert( f0= 'ib5552', f1= '(5552)5 mins')
    db.dtop0nav.insert( f0= 'pa5553', f1= '(5553)Why not buy a new awesome theme?')
    db.dtop0nav.insert( f0= 'aa5554', f1= '(5554)See All Messages')
    db.dtop0nav.insert( f0= 'lb5555', f1= '(5555)You have 10 notifications')
    db.dtop0nav.insert( f0= 'aa5556', f1= '(5556)View all')
    db.dtop0nav.insert( f0= 'sx5557', f1= '(5557)9')
    db.dtop0nav.insert( f0= 'lb5558', f1= '(5558)You have 9 tasks')
    db.dtop0nav.insert( f0= 'sx5559', f1= '(5559)20% Complete')
    db.dtop0nav.insert( f0= 'aa5560', f1= '(5560)View all tasks')
    db.dtop0nav.insert( f0= 'sx5562', f1= '(5562)Alexander Pierce')
    db.dtop0nav.insert( f0= 'ic5564', f1= '(5564)Member since Nov. 2012')
    db.dtop0nav.insert( f0= 'aa5565', f1= '(5565)Followers')
    db.dtop0nav.insert( f0= 'aa5566', f1= '(5566)Sales')
    db.dtop0nav.insert( f0= 'aa5567', f1= '(5567)Friends')
    db.dtop0nav.insert( f0= 'aa5568', f1= '(5568)Profile')
    db.dtop0nav.insert( f0= 'aa5569', f1= '(5569)Sign out')
    db.dtop0nav.insert( f0= 'ic5570', f1= '(5570)Example 2.0')
    db.dtop0nav.insert( f0= 'ia5571', f1= '(5571)Home')
    db.dtop0nav.insert( f0= 'aa5572', f1= '(5572)Layout')
    db.dtop0nav.insert( f0= 'lb5573', f1= '(5573)Top Navigation')
    db.dtop0nav.insert( f0= 'hh5574', f1= '(5574)Tip!')
    db.dtop0nav.insert( f0= 'hh5575', f1= '(5575)Warning!')
    db.dtop0nav.insert( f0= 'hc5576', f1= '(5576)Blank Box')
    db.dtop0nav.insert( f0= 'bb5577', f1= '(5577)Version')
    db.dtop0nav.insert( f0= 'aa5578', f1= '(5578)AdminLTE')
    db.commit()
#
