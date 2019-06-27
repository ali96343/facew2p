#
# table for controller: topIImenu
#

from gluon.contrib.populate import populate

db.define_table('dtop0menu', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtop0menu.id ).count():
    db.dtop0menu.insert( f0= 'sx3132', f1= '(3132)Toggle user menu')
    db.dtop0menu.insert( f0= 'sx3134', f1= '(3134)Toggle sidebar')
    db.dtop0menu.insert( f0= 'sx3135', f1= '(3135)Software Update')
    db.dtop0menu.insert( f0= 'sx3136', f1= '(3136)65%')
    db.dtop0menu.insert( f0= 'sx3137', f1= '(3137)Hardware Upgrade')
    db.dtop0menu.insert( f0= 'sx3138', f1= '(3138)35%')
    db.dtop0menu.insert( f0= 'sx3139', f1= '(3139)Unit Testing')
    db.dtop0menu.insert( f0= 'sx3140', f1= '(3140)15%')
    db.dtop0menu.insert( f0= 'sx3141', f1= '(3141)Bug Fixes')
    db.dtop0menu.insert( f0= 'sx3142', f1= '(3142)90%')
    db.dtop0menu.insert( f0= 'sx3144', f1= '(3144)Alex:')
    db.dtop0menu.insert( f0= 'sp3145', f1= '(3145)a moment ago')
    db.dtop0menu.insert( f0= 'sx3147', f1= '(3147)Susan:')
    db.dtop0menu.insert( f0= 'sp3148', f1= '(3148)20 minutes ago')
    db.dtop0menu.insert( f0= 'sx3150', f1= '(3150)Bob:')
    db.dtop0menu.insert( f0= 'sp3151', f1= '(3151)3:15 pm')
    db.dtop0menu.insert( f0= 'sx3153', f1= '(3153)Kate:')
    db.dtop0menu.insert( f0= 'sp3154', f1= '(3154)1:33 pm')
    db.dtop0menu.insert( f0= 'sx3156', f1= '(3156)Fred:')
    db.dtop0menu.insert( f0= 'sp3157', f1= '(3157)10:09 am')
    db.dtop0menu.insert( f0= 'ic3160', f1= '(3160)Welcome,')
    db.dtop0menu.insert( f0= 'pb3162', f1= '(3162)search')
    db.dtop0menu.insert( f0= 'sx3164', f1= '(3164)Dashboard')
    db.dtop0menu.insert( f0= 'sx3178', f1= '(3178)Tables')
    db.dtop0menu.insert( f0= 'sx3181', f1= '(3181)Forms')
    db.dtop0menu.insert( f0= 'sx3188', f1= '(3188)Widgets')
    db.dtop0menu.insert( f0= 'sx3191', f1= '(3191)Gallery')
    db.dtop0menu.insert( f0= 'sx3192', f1= '(3192)More Pages')
    db.dtop0menu.insert( f0= 'bb3206', f1= '(3206).container')
    db.dtop0menu.insert( f0= 'sx3207', f1= '(3207)top menu style')
    db.dtop0menu.insert( f0= 'sx3208', f1= '(3208)991px')
    db.dtop0menu.insert( f0= 'sx3209', f1= '(3209)Ace')
    db.commit()
#
