#
# table for controller: errorII404
#

from gluon.contrib.populate import populate

db.define_table('derror0404', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.derror0404.id ).count():
    db.derror0404.insert( f0= 'sx4503', f1= '(4503)Toggle sidebar')
    db.derror0404.insert( f0= 'sx4505', f1= '(4505)Software Update')
    db.derror0404.insert( f0= 'sx4506', f1= '(4506)65%')
    db.derror0404.insert( f0= 'sx4507', f1= '(4507)Hardware Upgrade')
    db.derror0404.insert( f0= 'sx4508', f1= '(4508)35%')
    db.derror0404.insert( f0= 'sx4509', f1= '(4509)Unit Testing')
    db.derror0404.insert( f0= 'sx4510', f1= '(4510)15%')
    db.derror0404.insert( f0= 'sx4511', f1= '(4511)Bug Fixes')
    db.derror0404.insert( f0= 'sx4512', f1= '(4512)90%')
    db.derror0404.insert( f0= 'sx4513', f1= '(4513)+12')
    db.derror0404.insert( f0= 'sx4514', f1= '(4514)+8')
    db.derror0404.insert( f0= 'sx4515', f1= '(4515)+11')
    db.derror0404.insert( f0= 'sx4517', f1= '(4517)Alex:')
    db.derror0404.insert( f0= 'sp4518', f1= '(4518)a moment ago')
    db.derror0404.insert( f0= 'sx4520', f1= '(4520)Susan:')
    db.derror0404.insert( f0= 'sp4521', f1= '(4521)20 minutes ago')
    db.derror0404.insert( f0= 'sx4523', f1= '(4523)Bob:')
    db.derror0404.insert( f0= 'sp4524', f1= '(4524)3:15 pm')
    db.derror0404.insert( f0= 'sx4526', f1= '(4526)Kate:')
    db.derror0404.insert( f0= 'sp4527', f1= '(4527)1:33 pm')
    db.derror0404.insert( f0= 'sx4529', f1= '(4529)Fred:')
    db.derror0404.insert( f0= 'sp4530', f1= '(4530)10:09 am')
    db.derror0404.insert( f0= 'ic4533', f1= '(4533)Welcome,')
    db.derror0404.insert( f0= 'sx4536', f1= '(4536)Dashboard')
    db.derror0404.insert( f0= 'sx4550', f1= '(4550)Tables')
    db.derror0404.insert( f0= 'sx4553', f1= '(4553)Forms')
    db.derror0404.insert( f0= 'sx4560', f1= '(4560)Widgets')
    db.derror0404.insert( f0= 'sx4563', f1= '(4563)Gallery')
    db.derror0404.insert( f0= 'sx4564', f1= '(4564)More Pages')
    db.derror0404.insert( f0= 'aa4578', f1= '(4578)Home')
    db.derror0404.insert( f0= 'aa4579', f1= '(4579)Other Pages')
    db.derror0404.insert( f0= 'lb4580', f1= '(4580)Error 404')
    db.derror0404.insert( f0= 'pb4581', f1= '(4581)Search ...')
    db.derror0404.insert( f0= 'bb4582', f1= '(4582).container')
    db.derror0404.insert( f0= 'hc4583', f1= '(4583)We looked everywhere but we couldn t find it!')
    db.derror0404.insert( f0= 'pb4584', f1= '(4584)Give it a search...')
    db.derror0404.insert( f0= 'bu4585', f1= '(4585)Go!')
    db.derror0404.insert( f0= 'hd4586', f1= '(4586)Try one of the following:')
    db.derror0404.insert( f0= 'sx4587', f1= '(4587)Ace')
    db.commit()
#
