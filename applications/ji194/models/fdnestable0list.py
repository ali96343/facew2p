#
# table for controller: nestableIIlist
#

from gluon.contrib.populate import populate

db.define_table('dnestable0list', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dnestable0list.id ).count():
    db.dnestable0list.insert( f0= 'sx3690', f1= '(3690)Toggle sidebar')
    db.dnestable0list.insert( f0= 'sx3692', f1= '(3692)Software Update')
    db.dnestable0list.insert( f0= 'sx3693', f1= '(3693)65%')
    db.dnestable0list.insert( f0= 'sx3694', f1= '(3694)Hardware Upgrade')
    db.dnestable0list.insert( f0= 'sx3695', f1= '(3695)35%')
    db.dnestable0list.insert( f0= 'sx3696', f1= '(3696)Unit Testing')
    db.dnestable0list.insert( f0= 'sx3697', f1= '(3697)15%')
    db.dnestable0list.insert( f0= 'sx3698', f1= '(3698)Bug Fixes')
    db.dnestable0list.insert( f0= 'sx3699', f1= '(3699)90%')
    db.dnestable0list.insert( f0= 'sx3700', f1= '(3700)+12')
    db.dnestable0list.insert( f0= 'sx3701', f1= '(3701)+8')
    db.dnestable0list.insert( f0= 'sx3702', f1= '(3702)+11')
    db.dnestable0list.insert( f0= 'sx3704', f1= '(3704)Alex:')
    db.dnestable0list.insert( f0= 'sp3705', f1= '(3705)a moment ago')
    db.dnestable0list.insert( f0= 'sx3707', f1= '(3707)Susan:')
    db.dnestable0list.insert( f0= 'sp3708', f1= '(3708)20 minutes ago')
    db.dnestable0list.insert( f0= 'sx3710', f1= '(3710)Bob:')
    db.dnestable0list.insert( f0= 'sp3711', f1= '(3711)3:15 pm')
    db.dnestable0list.insert( f0= 'sx3713', f1= '(3713)Kate:')
    db.dnestable0list.insert( f0= 'sp3714', f1= '(3714)1:33 pm')
    db.dnestable0list.insert( f0= 'sx3716', f1= '(3716)Fred:')
    db.dnestable0list.insert( f0= 'sp3717', f1= '(3717)10:09 am')
    db.dnestable0list.insert( f0= 'ic3720', f1= '(3720)Welcome,')
    db.dnestable0list.insert( f0= 'sx3723', f1= '(3723)Dashboard')
    db.dnestable0list.insert( f0= 'sx3737', f1= '(3737)Tables')
    db.dnestable0list.insert( f0= 'sx3740', f1= '(3740)Forms')
    db.dnestable0list.insert( f0= 'sx3747', f1= '(3747)Widgets')
    db.dnestable0list.insert( f0= 'sx3750', f1= '(3750)Gallery')
    db.dnestable0list.insert( f0= 'sx3751', f1= '(3751)More Pages')
    db.dnestable0list.insert( f0= 'aa3765', f1= '(3765)Home')
    db.dnestable0list.insert( f0= 'lb3766', f1= '(3766)Nestable Lists')
    db.dnestable0list.insert( f0= 'pb3767', f1= '(3767)Search ...')
    db.dnestable0list.insert( f0= 'bb3768', f1= '(3768).container')
    db.dnestable0list.insert( f0= 'di3769', f1= '(3769)Item 2')
    db.dnestable0list.insert( f0= 'sx3770', f1= '(3770)Item 4')
    db.dnestable0list.insert( f0= 'di3771', f1= '(3771)Item 6')
    db.dnestable0list.insert( f0= 'di3772', f1= '(3772)Item 7')
    db.dnestable0list.insert( f0= 'di3773', f1= '(3773)Item 8')
    db.dnestable0list.insert( f0= 'di3774', f1= '(3774)Item 9')
    db.dnestable0list.insert( f0= 'di3775', f1= '(3775)Item 10')
    db.dnestable0list.insert( f0= 'di3776', f1= '(3776)Item 12')
    db.dnestable0list.insert( f0= 'di3777', f1= '(3777)Click on an icon to start dragging')
    db.dnestable0list.insert( f0= 'di3778', f1= '(3778)Recent Posts')
    db.dnestable0list.insert( f0= 'di3779', f1= '(3779)Statistics')
    db.dnestable0list.insert( f0= 'di3780', f1= '(3780)Active Users')
    db.dnestable0list.insert( f0= 'di3781', f1= '(3781)Published Articles')
    db.dnestable0list.insert( f0= 'di3782', f1= '(3782)Visitors')
    db.dnestable0list.insert( f0= 'di3783', f1= '(3783)Menu')
    db.dnestable0list.insert( f0= 'sx3784', f1= '(3784)Ace')
    db.commit()
#
