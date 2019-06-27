#
# table for controller: contentIIslider
#

from gluon.contrib.populate import populate

db.define_table('dcontent0slider', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcontent0slider.id ).count():
    db.dcontent0slider.insert( f0= 'sx3479', f1= '(3479)Toggle sidebar')
    db.dcontent0slider.insert( f0= 'sx3481', f1= '(3481)Software Update')
    db.dcontent0slider.insert( f0= 'sx3482', f1= '(3482)65%')
    db.dcontent0slider.insert( f0= 'sx3483', f1= '(3483)Hardware Upgrade')
    db.dcontent0slider.insert( f0= 'sx3484', f1= '(3484)35%')
    db.dcontent0slider.insert( f0= 'sx3485', f1= '(3485)Unit Testing')
    db.dcontent0slider.insert( f0= 'sx3486', f1= '(3486)15%')
    db.dcontent0slider.insert( f0= 'sx3487', f1= '(3487)Bug Fixes')
    db.dcontent0slider.insert( f0= 'sx3488', f1= '(3488)90%')
    db.dcontent0slider.insert( f0= 'sx3489', f1= '(3489)+12')
    db.dcontent0slider.insert( f0= 'sx3490', f1= '(3490)+8')
    db.dcontent0slider.insert( f0= 'sx3491', f1= '(3491)+11')
    db.dcontent0slider.insert( f0= 'sx3493', f1= '(3493)Alex:')
    db.dcontent0slider.insert( f0= 'sp3494', f1= '(3494)a moment ago')
    db.dcontent0slider.insert( f0= 'sx3496', f1= '(3496)Susan:')
    db.dcontent0slider.insert( f0= 'sp3497', f1= '(3497)20 minutes ago')
    db.dcontent0slider.insert( f0= 'sx3499', f1= '(3499)Bob:')
    db.dcontent0slider.insert( f0= 'sp3500', f1= '(3500)3:15 pm')
    db.dcontent0slider.insert( f0= 'sx3502', f1= '(3502)Kate:')
    db.dcontent0slider.insert( f0= 'sp3503', f1= '(3503)1:33 pm')
    db.dcontent0slider.insert( f0= 'sx3505', f1= '(3505)Fred:')
    db.dcontent0slider.insert( f0= 'sp3506', f1= '(3506)10:09 am')
    db.dcontent0slider.insert( f0= 'ic3509', f1= '(3509)Welcome,')
    db.dcontent0slider.insert( f0= 'sx3512', f1= '(3512)Dashboard')
    db.dcontent0slider.insert( f0= 'sx3526', f1= '(3526)Tables')
    db.dcontent0slider.insert( f0= 'sx3529', f1= '(3529)Forms')
    db.dcontent0slider.insert( f0= 'sx3536', f1= '(3536)Widgets')
    db.dcontent0slider.insert( f0= 'sx3539', f1= '(3539)Gallery')
    db.dcontent0slider.insert( f0= 'sx3540', f1= '(3540)More Pages')
    db.dcontent0slider.insert( f0= 'aa3554', f1= '(3554)Home')
    db.dcontent0slider.insert( f0= 'lb3555', f1= '(3555)Content Sliders')
    db.dcontent0slider.insert( f0= 'pb3556', f1= '(3556)Search ...')
    db.dcontent0slider.insert( f0= 'bb3557', f1= '(3557).container')
    db.dcontent0slider.insert( f0= 'sx3558', f1= '(3558)11')
    db.dcontent0slider.insert( f0= 'sx3559', f1= '(3559)6+')
    db.dcontent0slider.insert( f0= 'sx3560', f1= '(3560)&times;')
    db.dcontent0slider.insert( f0= 'hc3561', f1= '(3561)Custom Elements and Content')
    db.dcontent0slider.insert( f0= 'bu3562', f1= '(3562)&times;')
    db.dcontent0slider.insert( f0= 'hc3563', f1= '(3563)A modal with a slider in it!')
    db.dcontent0slider.insert( f0= 'hc3564', f1= '(3564)Inside another modal')
    db.dcontent0slider.insert( f0= 'sx3565', f1= '(3565)Ace')
    db.commit()
#
