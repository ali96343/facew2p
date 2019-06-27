#
# table for controller: mobileIImenuII2
#

from gluon.contrib.populate import populate

db.define_table('dmobile0menu02', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dmobile0menu02.id ).count():
    db.dmobile0menu02.insert( f0= 'sx228', f1= '(228)Software Update')
    db.dmobile0menu02.insert( f0= 'sx229', f1= '(229)65%')
    db.dmobile0menu02.insert( f0= 'sx230', f1= '(230)Hardware Upgrade')
    db.dmobile0menu02.insert( f0= 'sx231', f1= '(231)35%')
    db.dmobile0menu02.insert( f0= 'sx232', f1= '(232)Unit Testing')
    db.dmobile0menu02.insert( f0= 'sx233', f1= '(233)15%')
    db.dmobile0menu02.insert( f0= 'sx234', f1= '(234)Bug Fixes')
    db.dmobile0menu02.insert( f0= 'sx235', f1= '(235)90%')
    db.dmobile0menu02.insert( f0= 'sx236', f1= '(236)+12')
    db.dmobile0menu02.insert( f0= 'sx237', f1= '(237)+8')
    db.dmobile0menu02.insert( f0= 'sx238', f1= '(238)+11')
    db.dmobile0menu02.insert( f0= 'sx240', f1= '(240)Alex:')
    db.dmobile0menu02.insert( f0= 'sp241', f1= '(241)a moment ago')
    db.dmobile0menu02.insert( f0= 'sx243', f1= '(243)Susan:')
    db.dmobile0menu02.insert( f0= 'sp244', f1= '(244)20 minutes ago')
    db.dmobile0menu02.insert( f0= 'sx246', f1= '(246)Bob:')
    db.dmobile0menu02.insert( f0= 'sp247', f1= '(247)3:15 pm')
    db.dmobile0menu02.insert( f0= 'sx249', f1= '(249)Kate:')
    db.dmobile0menu02.insert( f0= 'sp250', f1= '(250)1:33 pm')
    db.dmobile0menu02.insert( f0= 'sx252', f1= '(252)Fred:')
    db.dmobile0menu02.insert( f0= 'sp253', f1= '(253)10:09 am')
    db.dmobile0menu02.insert( f0= 'ic256', f1= '(256)Welcome,')
    db.dmobile0menu02.insert( f0= 'sx259', f1= '(259)Dashboard')
    db.dmobile0menu02.insert( f0= 'sx273', f1= '(273)Tables')
    db.dmobile0menu02.insert( f0= 'sx276', f1= '(276)Forms')
    db.dmobile0menu02.insert( f0= 'sx283', f1= '(283)Widgets')
    db.dmobile0menu02.insert( f0= 'sx286', f1= '(286)Gallery')
    db.dmobile0menu02.insert( f0= 'sx287', f1= '(287)More Pages')
    db.dmobile0menu02.insert( f0= 'aa301', f1= '(301)Home')
    db.dmobile0menu02.insert( f0= 'aa302', f1= '(302)Layouts')
    db.dmobile0menu02.insert( f0= 'lb303', f1= '(303)Mobile Menu 2')
    db.dmobile0menu02.insert( f0= 'pb304', f1= '(304)Search ...')
    db.dmobile0menu02.insert( f0= 'bb305', f1= '(305).container')
    db.dmobile0menu02.insert( f0= 'hh306', f1= '(306)Minimized Responsive(mobile) Menu')
    db.dmobile0menu02.insert( f0= 'sx307', f1= '(307)mobile menu')
    db.dmobile0menu02.insert( f0= 'sx308', f1= '(308)992px')
    db.dmobile0menu02.insert( f0= 'sx309', f1= '(309)992px')
    db.dmobile0menu02.insert( f0= 'sx310', f1= '(310)Ace')
    db.commit()
#
