#
# table for controller: blank
#

from gluon.contrib.populate import populate

db.define_table('dblank', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dblank.id ).count():
    db.dblank.insert( f0= 'sx330', f1= '(330)Toggle sidebar')
    db.dblank.insert( f0= 'sx332', f1= '(332)Software Update')
    db.dblank.insert( f0= 'sx333', f1= '(333)65%')
    db.dblank.insert( f0= 'sx334', f1= '(334)Hardware Upgrade')
    db.dblank.insert( f0= 'sx335', f1= '(335)35%')
    db.dblank.insert( f0= 'sx336', f1= '(336)Unit Testing')
    db.dblank.insert( f0= 'sx337', f1= '(337)15%')
    db.dblank.insert( f0= 'sx338', f1= '(338)Bug Fixes')
    db.dblank.insert( f0= 'sx339', f1= '(339)90%')
    db.dblank.insert( f0= 'sx340', f1= '(340)+12')
    db.dblank.insert( f0= 'sx341', f1= '(341)+8')
    db.dblank.insert( f0= 'sx342', f1= '(342)+11')
    db.dblank.insert( f0= 'sx344', f1= '(344)Alex:')
    db.dblank.insert( f0= 'sp345', f1= '(345)a moment ago')
    db.dblank.insert( f0= 'sx347', f1= '(347)Susan:')
    db.dblank.insert( f0= 'sp348', f1= '(348)20 minutes ago')
    db.dblank.insert( f0= 'sx350', f1= '(350)Bob:')
    db.dblank.insert( f0= 'sp351', f1= '(351)3:15 pm')
    db.dblank.insert( f0= 'sx353', f1= '(353)Kate:')
    db.dblank.insert( f0= 'sp354', f1= '(354)1:33 pm')
    db.dblank.insert( f0= 'sx356', f1= '(356)Fred:')
    db.dblank.insert( f0= 'sp357', f1= '(357)10:09 am')
    db.dblank.insert( f0= 'ic360', f1= '(360)Welcome,')
    db.dblank.insert( f0= 'sx363', f1= '(363)Dashboard')
    db.dblank.insert( f0= 'sx377', f1= '(377)Tables')
    db.dblank.insert( f0= 'sx380', f1= '(380)Forms')
    db.dblank.insert( f0= 'sx387', f1= '(387)Widgets')
    db.dblank.insert( f0= 'sx390', f1= '(390)Gallery')
    db.dblank.insert( f0= 'sx391', f1= '(391)More Pages')
    db.dblank.insert( f0= 'aa405', f1= '(405)Home')
    db.dblank.insert( f0= 'aa406', f1= '(406)Other Pages')
    db.dblank.insert( f0= 'lb407', f1= '(407)Blank Page')
    db.dblank.insert( f0= 'pb408', f1= '(408)Search ...')
    db.dblank.insert( f0= 'bb409', f1= '(409).container')
    db.dblank.insert( f0= 'sx410', f1= '(410)Ace')
    db.commit()
#
