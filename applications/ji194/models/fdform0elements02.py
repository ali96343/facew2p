#
# table for controller: formIIelementsII2
#

from gluon.contrib.populate import populate

db.define_table('dform0elements02', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dform0elements02.id ).count():
    db.dform0elements02.insert( f0= 'sx117', f1= '(117)Toggle sidebar')
    db.dform0elements02.insert( f0= 'sx119', f1= '(119)Software Update')
    db.dform0elements02.insert( f0= 'sx120', f1= '(120)65%')
    db.dform0elements02.insert( f0= 'sx121', f1= '(121)Hardware Upgrade')
    db.dform0elements02.insert( f0= 'sx122', f1= '(122)35%')
    db.dform0elements02.insert( f0= 'sx123', f1= '(123)Unit Testing')
    db.dform0elements02.insert( f0= 'sx124', f1= '(124)15%')
    db.dform0elements02.insert( f0= 'sx125', f1= '(125)Bug Fixes')
    db.dform0elements02.insert( f0= 'sx126', f1= '(126)90%')
    db.dform0elements02.insert( f0= 'sx127', f1= '(127)+12')
    db.dform0elements02.insert( f0= 'sx128', f1= '(128)+8')
    db.dform0elements02.insert( f0= 'sx129', f1= '(129)+11')
    db.dform0elements02.insert( f0= 'sx131', f1= '(131)Alex:')
    db.dform0elements02.insert( f0= 'sp132', f1= '(132)a moment ago')
    db.dform0elements02.insert( f0= 'sx134', f1= '(134)Susan:')
    db.dform0elements02.insert( f0= 'sp135', f1= '(135)20 minutes ago')
    db.dform0elements02.insert( f0= 'sx137', f1= '(137)Bob:')
    db.dform0elements02.insert( f0= 'sp138', f1= '(138)3:15 pm')
    db.dform0elements02.insert( f0= 'sx140', f1= '(140)Kate:')
    db.dform0elements02.insert( f0= 'sp141', f1= '(141)1:33 pm')
    db.dform0elements02.insert( f0= 'sx143', f1= '(143)Fred:')
    db.dform0elements02.insert( f0= 'sp144', f1= '(144)10:09 am')
    db.dform0elements02.insert( f0= 'ic147', f1= '(147)Welcome,')
    db.dform0elements02.insert( f0= 'sx150', f1= '(150)Dashboard')
    db.dform0elements02.insert( f0= 'sx164', f1= '(164)Tables')
    db.dform0elements02.insert( f0= 'sx167', f1= '(167)Forms')
    db.dform0elements02.insert( f0= 'sx174', f1= '(174)Widgets')
    db.dform0elements02.insert( f0= 'sx177', f1= '(177)Gallery')
    db.dform0elements02.insert( f0= 'sx178', f1= '(178)More Pages')
    db.dform0elements02.insert( f0= 'aa192', f1= '(192)Home')
    db.dform0elements02.insert( f0= 'aa193', f1= '(193)Forms')
    db.dform0elements02.insert( f0= 'lb194', f1= '(194)Form Elements 2')
    db.dform0elements02.insert( f0= 'pb195', f1= '(195)Search ...')
    db.dform0elements02.insert( f0= 'bb196', f1= '(196).container')
    db.dform0elements02.insert( f0= 'hh197', f1= '(197)More Elements')
    db.dform0elements02.insert( f0= 'pb198', f1= '(198)States of USA')
    db.dform0elements02.insert( f0= 'pb199', f1= '(199)Click to Choose...')
    db.dform0elements02.insert( f0= 'sx200', f1= '(200)style:')
    db.dform0elements02.insert( f0= 'sx201', f1= '(201)Ace')
    db.dform0elements02.insert( f0= 'sx213', f1= '(213)Filtered')
    db.commit()
#
