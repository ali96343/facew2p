#
# table for controller: fixed_header_mini_sidebar
#

from gluon.contrib.populate import populate

db.define_table('dfixed0header0mini0sidebar', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dfixed0header0mini0sidebar.id ).count():
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4248', f1= '(4248)Toggle navigation')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4253', f1= '(4253)Dashboard')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4255', f1= '(4255)Tables')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4257', f1= '(4257)General')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4259', f1= '(4259)Validation')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4261', f1= '(4261)WYSIWYG')
    db.dfixed0header0mini0sidebar.insert( f0= 'pb4263', f1= '(4263)Live Search ...')
    db.dfixed0header0mini0sidebar.insert( f0= 'he4265', f1= '(4265)Archie')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4266', f1= '(4266)Administrator')
    db.dfixed0header0mini0sidebar.insert( f0= 'ba4267', f1= '(4267)Last Access :')
    db.dfixed0header0mini0sidebar.insert( f0= 'lb4268', f1= '(4268)Menu')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4270', f1= '(4270)Layouts')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4289', f1= '(4289)Components')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4301', f1= '(4301)Tables')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4316', f1= '(4316)Level 2')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4317', f1= '(4317)Level 2')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4318', f1= '(4318)Level 3')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4319', f1= '(4319)Level 3')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4320', f1= '(4320)Level 4')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4321', f1= '(4321)Level 4')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4322', f1= '(4322)Level 5')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4323', f1= '(4323)Level 5')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4324', f1= '(4324)Level 5')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4325', f1= '(4325)Level 4')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4326', f1= '(4326)Level 2')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4327', f1= '(4327)Level 1')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4328', f1= '(4328)Level 2')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4329', f1= '(4329)Level 2')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4330', f1= '(4330)Level 2')
    db.dfixed0header0mini0sidebar.insert( f0= 'hh4331', f1= '(4331)Code')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4332', f1= '(4332)&times;')
    db.dfixed0header0mini0sidebar.insert( f0= 'sp4333', f1= '(4333)Warning!')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4334', f1= '(4334)1,4,4,7,5,9,10')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4335', f1= '(4335)Loading..')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4336', f1= '(4336)Loading..')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4337', f1= '(4337)1,3,4,5,3,5')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4338', f1= '(4338)Default')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4339', f1= '(4339)Primary')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4340', f1= '(4340)Info')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4341', f1= '(4341)Success')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4342', f1= '(4342)Danger')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4343', f1= '(4343)Warning')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4344', f1= '(4344)Inverse')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4345', f1= '(4345)btn-metis-1')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4346', f1= '(4346)btn-metis-2')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4347', f1= '(4347)btn-metis-3')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4348', f1= '(4348)btn-metis-4')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4349', f1= '(4349)btn-metis-5')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4350', f1= '(4350)btn-metis-6')
    db.dfixed0header0mini0sidebar.insert( f0= 'si4351', f1= '(4351)20%')
    db.dfixed0header0mini0sidebar.insert( f0= 'sp4352', f1= '(4352)Default')
    db.dfixed0header0mini0sidebar.insert( f0= 'si4353', f1= '(4353)40%')
    db.dfixed0header0mini0sidebar.insert( f0= 'sp4354', f1= '(4354)Success')
    db.dfixed0header0mini0sidebar.insert( f0= 'si4355', f1= '(4355)60%')
    db.dfixed0header0mini0sidebar.insert( f0= 'sp4356', f1= '(4356)warning')
    db.dfixed0header0mini0sidebar.insert( f0= 'si4357', f1= '(4357)80%')
    db.dfixed0header0mini0sidebar.insert( f0= 'sp4358', f1= '(4358)Danger')
    db.dfixed0header0mini0sidebar.insert( f0= 'pa4359', f1= '(4359)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4360', f1= '(4360)&times;')
    db.dfixed0header0mini0sidebar.insert( f0= 'hd4361', f1= '(4361)Modal title')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4362', f1= '(4362)Close')
    db.commit()
#
