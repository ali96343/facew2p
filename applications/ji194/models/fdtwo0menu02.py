#
# table for controller: twoIImenuII2
#

from gluon.contrib.populate import populate

db.define_table('dtwo0menu02', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtwo0menu02.id ).count():
    db.dtwo0menu02.insert( f0= 'sx3378', f1= '(3378)Toggle user menu')
    db.dtwo0menu02.insert( f0= 'sx3380', f1= '(3380)Toggle sidebar')
    db.dtwo0menu02.insert( f0= 'sx3381', f1= '(3381)Software Update')
    db.dtwo0menu02.insert( f0= 'sx3382', f1= '(3382)65%')
    db.dtwo0menu02.insert( f0= 'sx3383', f1= '(3383)Hardware Upgrade')
    db.dtwo0menu02.insert( f0= 'sx3384', f1= '(3384)35%')
    db.dtwo0menu02.insert( f0= 'sx3385', f1= '(3385)Unit Testing')
    db.dtwo0menu02.insert( f0= 'sx3386', f1= '(3386)15%')
    db.dtwo0menu02.insert( f0= 'sx3387', f1= '(3387)Bug Fixes')
    db.dtwo0menu02.insert( f0= 'sx3388', f1= '(3388)90%')
    db.dtwo0menu02.insert( f0= 'sx3390', f1= '(3390)Alex:')
    db.dtwo0menu02.insert( f0= 'sp3391', f1= '(3391)a moment ago')
    db.dtwo0menu02.insert( f0= 'sx3393', f1= '(3393)Susan:')
    db.dtwo0menu02.insert( f0= 'sp3394', f1= '(3394)20 minutes ago')
    db.dtwo0menu02.insert( f0= 'sx3396', f1= '(3396)Bob:')
    db.dtwo0menu02.insert( f0= 'sp3397', f1= '(3397)3:15 pm')
    db.dtwo0menu02.insert( f0= 'sx3399', f1= '(3399)Kate:')
    db.dtwo0menu02.insert( f0= 'sp3400', f1= '(3400)1:33 pm')
    db.dtwo0menu02.insert( f0= 'sx3402', f1= '(3402)Fred:')
    db.dtwo0menu02.insert( f0= 'sp3403', f1= '(3403)10:09 am')
    db.dtwo0menu02.insert( f0= 'ic3406', f1= '(3406)Welcome,')
    db.dtwo0menu02.insert( f0= 'pb3408', f1= '(3408)search')
    db.dtwo0menu02.insert( f0= 'sx3410', f1= '(3410)Dashboard')
    db.dtwo0menu02.insert( f0= 'sx3424', f1= '(3424)Tables')
    db.dtwo0menu02.insert( f0= 'sx3427', f1= '(3427)Forms')
    db.dtwo0menu02.insert( f0= 'sx3434', f1= '(3434)Widgets')
    db.dtwo0menu02.insert( f0= 'sx3437', f1= '(3437)Gallery')
    db.dtwo0menu02.insert( f0= 'sx3438', f1= '(3438)More Pages')
    db.dtwo0menu02.insert( f0= 'bb3452', f1= '(3452).container')
    db.dtwo0menu02.insert( f0= 'hh3453', f1= '(3453)Two Menu Style')
    db.dtwo0menu02.insert( f0= 'sx3454', f1= '(3454)Toggle sidebar')
    db.dtwo0menu02.insert( f0= 'sx3455', f1= '(3455)Dashboard')
    db.dtwo0menu02.insert( f0= 'sx3456', f1= '(3456)Widgets')
    db.dtwo0menu02.insert( f0= 'sx3457', f1= '(3457)Gallery')
    db.dtwo0menu02.insert( f0= 'sx3458', f1= '(3458)More Pages')
    db.dtwo0menu02.insert( f0= 'sx3459', f1= '(3459)Ace')
    db.commit()
#
