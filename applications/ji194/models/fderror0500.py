#
# table for controller: errorII500
#

from gluon.contrib.populate import populate

db.define_table('derror0500', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.derror0500.id ).count():
    db.derror0500.insert( f0= 'sx4607', f1= '(4607)Toggle sidebar')
    db.derror0500.insert( f0= 'sx4609', f1= '(4609)Software Update')
    db.derror0500.insert( f0= 'sx4610', f1= '(4610)65%')
    db.derror0500.insert( f0= 'sx4611', f1= '(4611)Hardware Upgrade')
    db.derror0500.insert( f0= 'sx4612', f1= '(4612)35%')
    db.derror0500.insert( f0= 'sx4613', f1= '(4613)Unit Testing')
    db.derror0500.insert( f0= 'sx4614', f1= '(4614)15%')
    db.derror0500.insert( f0= 'sx4615', f1= '(4615)Bug Fixes')
    db.derror0500.insert( f0= 'sx4616', f1= '(4616)90%')
    db.derror0500.insert( f0= 'sx4617', f1= '(4617)+12')
    db.derror0500.insert( f0= 'sx4618', f1= '(4618)+8')
    db.derror0500.insert( f0= 'sx4619', f1= '(4619)+11')
    db.derror0500.insert( f0= 'sx4621', f1= '(4621)Alex:')
    db.derror0500.insert( f0= 'sp4622', f1= '(4622)a moment ago')
    db.derror0500.insert( f0= 'sx4624', f1= '(4624)Susan:')
    db.derror0500.insert( f0= 'sp4625', f1= '(4625)20 minutes ago')
    db.derror0500.insert( f0= 'sx4627', f1= '(4627)Bob:')
    db.derror0500.insert( f0= 'sp4628', f1= '(4628)3:15 pm')
    db.derror0500.insert( f0= 'sx4630', f1= '(4630)Kate:')
    db.derror0500.insert( f0= 'sp4631', f1= '(4631)1:33 pm')
    db.derror0500.insert( f0= 'sx4633', f1= '(4633)Fred:')
    db.derror0500.insert( f0= 'sp4634', f1= '(4634)10:09 am')
    db.derror0500.insert( f0= 'ic4637', f1= '(4637)Welcome,')
    db.derror0500.insert( f0= 'sx4640', f1= '(4640)Dashboard')
    db.derror0500.insert( f0= 'sx4654', f1= '(4654)Tables')
    db.derror0500.insert( f0= 'sx4657', f1= '(4657)Forms')
    db.derror0500.insert( f0= 'sx4664', f1= '(4664)Widgets')
    db.derror0500.insert( f0= 'sx4667', f1= '(4667)Gallery')
    db.derror0500.insert( f0= 'sx4668', f1= '(4668)More Pages')
    db.derror0500.insert( f0= 'aa4682', f1= '(4682)Home')
    db.derror0500.insert( f0= 'aa4683', f1= '(4683)Other Pages')
    db.derror0500.insert( f0= 'lb4684', f1= '(4684)Error 500')
    db.derror0500.insert( f0= 'pb4685', f1= '(4685)Search ...')
    db.derror0500.insert( f0= 'bb4686', f1= '(4686).container')
    db.derror0500.insert( f0= 'hd4687', f1= '(4687)Meanwhile, try one of the following:')
    db.derror0500.insert( f0= 'sx4688', f1= '(4688)Ace')
    db.commit()
#
