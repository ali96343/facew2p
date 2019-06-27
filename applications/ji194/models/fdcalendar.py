#
# table for controller: calendar
#

from gluon.contrib.populate import populate

db.define_table('dcalendar', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcalendar.id ).count():
    db.dcalendar.insert( f0= 'sx4396', f1= '(4396)Toggle sidebar')
    db.dcalendar.insert( f0= 'sx4398', f1= '(4398)Software Update')
    db.dcalendar.insert( f0= 'sx4399', f1= '(4399)65%')
    db.dcalendar.insert( f0= 'sx4400', f1= '(4400)Hardware Upgrade')
    db.dcalendar.insert( f0= 'sx4401', f1= '(4401)35%')
    db.dcalendar.insert( f0= 'sx4402', f1= '(4402)Unit Testing')
    db.dcalendar.insert( f0= 'sx4403', f1= '(4403)15%')
    db.dcalendar.insert( f0= 'sx4404', f1= '(4404)Bug Fixes')
    db.dcalendar.insert( f0= 'sx4405', f1= '(4405)90%')
    db.dcalendar.insert( f0= 'sx4406', f1= '(4406)+12')
    db.dcalendar.insert( f0= 'sx4407', f1= '(4407)+8')
    db.dcalendar.insert( f0= 'sx4408', f1= '(4408)+11')
    db.dcalendar.insert( f0= 'sx4410', f1= '(4410)Alex:')
    db.dcalendar.insert( f0= 'sp4411', f1= '(4411)a moment ago')
    db.dcalendar.insert( f0= 'sx4413', f1= '(4413)Susan:')
    db.dcalendar.insert( f0= 'sp4414', f1= '(4414)20 minutes ago')
    db.dcalendar.insert( f0= 'sx4416', f1= '(4416)Bob:')
    db.dcalendar.insert( f0= 'sp4417', f1= '(4417)3:15 pm')
    db.dcalendar.insert( f0= 'sx4419', f1= '(4419)Kate:')
    db.dcalendar.insert( f0= 'sp4420', f1= '(4420)1:33 pm')
    db.dcalendar.insert( f0= 'sx4422', f1= '(4422)Fred:')
    db.dcalendar.insert( f0= 'sp4423', f1= '(4423)10:09 am')
    db.dcalendar.insert( f0= 'ic4426', f1= '(4426)Welcome,')
    db.dcalendar.insert( f0= 'sx4429', f1= '(4429)Dashboard')
    db.dcalendar.insert( f0= 'sx4443', f1= '(4443)Tables')
    db.dcalendar.insert( f0= 'sx4446', f1= '(4446)Forms')
    db.dcalendar.insert( f0= 'sx4453', f1= '(4453)Widgets')
    db.dcalendar.insert( f0= 'sx4456', f1= '(4456)Gallery')
    db.dcalendar.insert( f0= 'sx4457', f1= '(4457)More Pages')
    db.dcalendar.insert( f0= 'aa4471', f1= '(4471)Home')
    db.dcalendar.insert( f0= 'lb4472', f1= '(4472)Calendar')
    db.dcalendar.insert( f0= 'pb4473', f1= '(4473)Search ...')
    db.dcalendar.insert( f0= 'bb4474', f1= '(4474).container')
    db.dcalendar.insert( f0= 'hh4475', f1= '(4475)Draggable events')
    db.dcalendar.insert( f0= 'sx4476', f1= '(4476)Remove after drop')
    db.dcalendar.insert( f0= 'sx4477', f1= '(4477)Ace')
    db.dcalendar.insert( f0= 'bu4489', f1= '(4489)&times;')
    db.commit()
#
