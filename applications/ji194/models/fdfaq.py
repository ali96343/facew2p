#
# table for controller: faq
#

from gluon.contrib.populate import populate

db.define_table('dfaq', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dfaq.id ).count():
    db.dfaq.insert( f0= 'sx4292', f1= '(4292)Toggle sidebar')
    db.dfaq.insert( f0= 'sx4294', f1= '(4294)Software Update')
    db.dfaq.insert( f0= 'sx4295', f1= '(4295)65%')
    db.dfaq.insert( f0= 'sx4296', f1= '(4296)Hardware Upgrade')
    db.dfaq.insert( f0= 'sx4297', f1= '(4297)35%')
    db.dfaq.insert( f0= 'sx4298', f1= '(4298)Unit Testing')
    db.dfaq.insert( f0= 'sx4299', f1= '(4299)15%')
    db.dfaq.insert( f0= 'sx4300', f1= '(4300)Bug Fixes')
    db.dfaq.insert( f0= 'sx4301', f1= '(4301)90%')
    db.dfaq.insert( f0= 'sx4302', f1= '(4302)+12')
    db.dfaq.insert( f0= 'sx4303', f1= '(4303)+8')
    db.dfaq.insert( f0= 'sx4304', f1= '(4304)+11')
    db.dfaq.insert( f0= 'sx4306', f1= '(4306)Alex:')
    db.dfaq.insert( f0= 'sp4307', f1= '(4307)a moment ago')
    db.dfaq.insert( f0= 'sx4309', f1= '(4309)Susan:')
    db.dfaq.insert( f0= 'sp4310', f1= '(4310)20 minutes ago')
    db.dfaq.insert( f0= 'sx4312', f1= '(4312)Bob:')
    db.dfaq.insert( f0= 'sp4313', f1= '(4313)3:15 pm')
    db.dfaq.insert( f0= 'sx4315', f1= '(4315)Kate:')
    db.dfaq.insert( f0= 'sp4316', f1= '(4316)1:33 pm')
    db.dfaq.insert( f0= 'sx4318', f1= '(4318)Fred:')
    db.dfaq.insert( f0= 'sp4319', f1= '(4319)10:09 am')
    db.dfaq.insert( f0= 'ic4322', f1= '(4322)Welcome,')
    db.dfaq.insert( f0= 'sx4325', f1= '(4325)Dashboard')
    db.dfaq.insert( f0= 'sx4339', f1= '(4339)Tables')
    db.dfaq.insert( f0= 'sx4342', f1= '(4342)Forms')
    db.dfaq.insert( f0= 'sx4349', f1= '(4349)Widgets')
    db.dfaq.insert( f0= 'sx4352', f1= '(4352)Gallery')
    db.dfaq.insert( f0= 'sx4353', f1= '(4353)More Pages')
    db.dfaq.insert( f0= 'aa4367', f1= '(4367)Home')
    db.dfaq.insert( f0= 'aa4368', f1= '(4368)Other Pages')
    db.dfaq.insert( f0= 'lb4369', f1= '(4369)FAQ')
    db.dfaq.insert( f0= 'pb4370', f1= '(4370)Search ...')
    db.dfaq.insert( f0= 'bb4371', f1= '(4371).container')
    db.dfaq.insert( f0= 'aa4372', f1= '(4372)Affiliates')
    db.dfaq.insert( f0= 'aa4373', f1= '(4373)Merchants')
    db.dfaq.insert( f0= 'sx4374', f1= '(4374)Ace')
    db.commit()
#
