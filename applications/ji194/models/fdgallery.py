#
# table for controller: gallery
#

from gluon.contrib.populate import populate

db.define_table('dgallery', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dgallery.id ).count():
    db.dgallery.insert( f0= 'sx3806', f1= '(3806)Toggle sidebar')
    db.dgallery.insert( f0= 'sx3808', f1= '(3808)Software Update')
    db.dgallery.insert( f0= 'sx3809', f1= '(3809)65%')
    db.dgallery.insert( f0= 'sx3810', f1= '(3810)Hardware Upgrade')
    db.dgallery.insert( f0= 'sx3811', f1= '(3811)35%')
    db.dgallery.insert( f0= 'sx3812', f1= '(3812)Unit Testing')
    db.dgallery.insert( f0= 'sx3813', f1= '(3813)15%')
    db.dgallery.insert( f0= 'sx3814', f1= '(3814)Bug Fixes')
    db.dgallery.insert( f0= 'sx3815', f1= '(3815)90%')
    db.dgallery.insert( f0= 'sx3816', f1= '(3816)+12')
    db.dgallery.insert( f0= 'sx3817', f1= '(3817)+8')
    db.dgallery.insert( f0= 'sx3818', f1= '(3818)+11')
    db.dgallery.insert( f0= 'sx3820', f1= '(3820)Alex:')
    db.dgallery.insert( f0= 'sp3821', f1= '(3821)a moment ago')
    db.dgallery.insert( f0= 'sx3823', f1= '(3823)Susan:')
    db.dgallery.insert( f0= 'sp3824', f1= '(3824)20 minutes ago')
    db.dgallery.insert( f0= 'sx3826', f1= '(3826)Bob:')
    db.dgallery.insert( f0= 'sp3827', f1= '(3827)3:15 pm')
    db.dgallery.insert( f0= 'sx3829', f1= '(3829)Kate:')
    db.dgallery.insert( f0= 'sp3830', f1= '(3830)1:33 pm')
    db.dgallery.insert( f0= 'sx3832', f1= '(3832)Fred:')
    db.dgallery.insert( f0= 'sp3833', f1= '(3833)10:09 am')
    db.dgallery.insert( f0= 'ic3836', f1= '(3836)Welcome,')
    db.dgallery.insert( f0= 'sx3839', f1= '(3839)Dashboard')
    db.dgallery.insert( f0= 'sx3853', f1= '(3853)Tables')
    db.dgallery.insert( f0= 'sx3856', f1= '(3856)Forms')
    db.dgallery.insert( f0= 'sx3863', f1= '(3863)Widgets')
    db.dgallery.insert( f0= 'sx3866', f1= '(3866)Gallery')
    db.dgallery.insert( f0= 'sx3867', f1= '(3867)More Pages')
    db.dgallery.insert( f0= 'aa3881', f1= '(3881)Home')
    db.dgallery.insert( f0= 'lb3882', f1= '(3882)Gallery')
    db.dgallery.insert( f0= 'pb3883', f1= '(3883)Search ...')
    db.dgallery.insert( f0= 'bb3884', f1= '(3884).container')
    db.dgallery.insert( f0= 'sx3887', f1= '(3887)breakfast')
    db.dgallery.insert( f0= 'sx3888', f1= '(3888)fruits')
    db.dgallery.insert( f0= 'sx3889', f1= '(3889)toast')
    db.dgallery.insert( f0= 'sx3890', f1= '(3890)diet')
    db.dgallery.insert( f0= 'di3893', f1= '(3893)Sample Caption on Hover')
    db.dgallery.insert( f0= 'di3896', f1= '(3896)Sample Caption on Hover')
    db.dgallery.insert( f0= 'sx3899', f1= '(3899)fountain')
    db.dgallery.insert( f0= 'sx3900', f1= '(3900)recreation')
    db.dgallery.insert( f0= 'sp3902', f1= '(3902)Some Title!')
    db.dgallery.insert( f0= 'sx3910', f1= '(3910)Ace')
    db.commit()
#
