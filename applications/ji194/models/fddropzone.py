#
# table for controller: dropzone
#

from gluon.contrib.populate import populate

db.define_table('ddropzone', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.ddropzone.id ).count():
    db.ddropzone.insert( f0= 'sx3586', f1= '(3586)Toggle sidebar')
    db.ddropzone.insert( f0= 'sx3588', f1= '(3588)Software Update')
    db.ddropzone.insert( f0= 'sx3589', f1= '(3589)65%')
    db.ddropzone.insert( f0= 'sx3590', f1= '(3590)Hardware Upgrade')
    db.ddropzone.insert( f0= 'sx3591', f1= '(3591)35%')
    db.ddropzone.insert( f0= 'sx3592', f1= '(3592)Unit Testing')
    db.ddropzone.insert( f0= 'sx3593', f1= '(3593)15%')
    db.ddropzone.insert( f0= 'sx3594', f1= '(3594)Bug Fixes')
    db.ddropzone.insert( f0= 'sx3595', f1= '(3595)90%')
    db.ddropzone.insert( f0= 'sx3596', f1= '(3596)+12')
    db.ddropzone.insert( f0= 'sx3597', f1= '(3597)+8')
    db.ddropzone.insert( f0= 'sx3598', f1= '(3598)+11')
    db.ddropzone.insert( f0= 'sx3600', f1= '(3600)Alex:')
    db.ddropzone.insert( f0= 'sp3601', f1= '(3601)a moment ago')
    db.ddropzone.insert( f0= 'sx3603', f1= '(3603)Susan:')
    db.ddropzone.insert( f0= 'sp3604', f1= '(3604)20 minutes ago')
    db.ddropzone.insert( f0= 'sx3606', f1= '(3606)Bob:')
    db.ddropzone.insert( f0= 'sp3607', f1= '(3607)3:15 pm')
    db.ddropzone.insert( f0= 'sx3609', f1= '(3609)Kate:')
    db.ddropzone.insert( f0= 'sp3610', f1= '(3610)1:33 pm')
    db.ddropzone.insert( f0= 'sx3612', f1= '(3612)Fred:')
    db.ddropzone.insert( f0= 'sp3613', f1= '(3613)10:09 am')
    db.ddropzone.insert( f0= 'ic3616', f1= '(3616)Welcome,')
    db.ddropzone.insert( f0= 'sx3619', f1= '(3619)Dashboard')
    db.ddropzone.insert( f0= 'sx3633', f1= '(3633)Tables')
    db.ddropzone.insert( f0= 'sx3636', f1= '(3636)Forms')
    db.ddropzone.insert( f0= 'sx3643', f1= '(3643)Widgets')
    db.ddropzone.insert( f0= 'sx3646', f1= '(3646)Gallery')
    db.ddropzone.insert( f0= 'sx3647', f1= '(3647)More Pages')
    db.ddropzone.insert( f0= 'aa3661', f1= '(3661)Home')
    db.ddropzone.insert( f0= 'aa3662', f1= '(3662)Forms')
    db.ddropzone.insert( f0= 'lb3663', f1= '(3663)Dropzone File Upload')
    db.ddropzone.insert( f0= 'pb3664', f1= '(3664)Search ...')
    db.ddropzone.insert( f0= 'bb3665', f1= '(3665).container')
    db.ddropzone.insert( f0= 'sx3666', f1= '(3666)Ace')
    db.ddropzone.insert( f0= 'sx3674', f1= '(3674)Drop files')
    db.ddropzone.insert( f0= 'sx3675', f1= '(3675)(or click)')
    db.commit()
#
