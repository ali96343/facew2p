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
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4404', f1= '(4404)Toggle navigation')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4407', f1= '(4407)5')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4408', f1= '(4408)4')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4411', f1= '(4411)Dashboard')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4413', f1= '(4413)Tables')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4415', f1= '(4415)General')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4417', f1= '(4417)Validation')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4419', f1= '(4419)WYSIWYG')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4421', f1= '(4421)Wizard &amp; File Upload')
    db.dfixed0header0mini0sidebar.insert( f0= 'pb4422', f1= '(4422)Live Search ...')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4424', f1= '(4424)16')
    db.dfixed0header0mini0sidebar.insert( f0= 'he4425', f1= '(4425)Archie')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4426', f1= '(4426)Administrator')
    db.dfixed0header0mini0sidebar.insert( f0= 'ba4427', f1= '(4427)Last Access :')
    db.dfixed0header0mini0sidebar.insert( f0= 'lb4428', f1= '(4428)Menu')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4430', f1= '(4430)&nbsp;Dashboard')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4431', f1= '(4431)Layouts')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4450', f1= '(4450)Components')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4462', f1= '(4462)Tables')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4477', f1= '(4477)Level 2')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4478', f1= '(4478)Level 2')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4479', f1= '(4479)Level 3')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4480', f1= '(4480)Level 3')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4481', f1= '(4481)Level 4')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4482', f1= '(4482)Level 4')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4483', f1= '(4483)Level 5')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4484', f1= '(4484)Level 5')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4485', f1= '(4485)Level 5')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4486', f1= '(4486)Level 4')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4487', f1= '(4487)Level 2')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4488', f1= '(4488)Level 1')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4489', f1= '(4489)Level 2')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4490', f1= '(4490)Level 2')
    db.dfixed0header0mini0sidebar.insert( f0= 'aa4491', f1= '(4491)Level 2')
    db.dfixed0header0mini0sidebar.insert( f0= 'hh4492', f1= '(4492)Code')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4493', f1= '(4493)&times;')
    db.dfixed0header0mini0sidebar.insert( f0= 'sp4494', f1= '(4494)Warning!')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4495', f1= '(4495)1,4,4,7,5,9,10')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4496', f1= '(4496)Loading..')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4497', f1= '(4497)Loading..')
    db.dfixed0header0mini0sidebar.insert( f0= 'sx4498', f1= '(4498)1,3,4,5,3,5')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4499', f1= '(4499)Default')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4500', f1= '(4500)Primary')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4501', f1= '(4501)Info')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4502', f1= '(4502)Success')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4503', f1= '(4503)Danger')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4504', f1= '(4504)Warning')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4505', f1= '(4505)Inverse')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4506', f1= '(4506)btn-metis-1')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4507', f1= '(4507)btn-metis-2')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4508', f1= '(4508)btn-metis-3')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4509', f1= '(4509)btn-metis-4')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4510', f1= '(4510)btn-metis-5')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4511', f1= '(4511)btn-metis-6')
    db.dfixed0header0mini0sidebar.insert( f0= 'si4512', f1= '(4512)20%')
    db.dfixed0header0mini0sidebar.insert( f0= 'sp4513', f1= '(4513)Default')
    db.dfixed0header0mini0sidebar.insert( f0= 'si4514', f1= '(4514)40%')
    db.dfixed0header0mini0sidebar.insert( f0= 'sp4515', f1= '(4515)Success')
    db.dfixed0header0mini0sidebar.insert( f0= 'si4516', f1= '(4516)60%')
    db.dfixed0header0mini0sidebar.insert( f0= 'sp4517', f1= '(4517)warning')
    db.dfixed0header0mini0sidebar.insert( f0= 'si4518', f1= '(4518)80%')
    db.dfixed0header0mini0sidebar.insert( f0= 'sp4519', f1= '(4519)Danger')
    db.dfixed0header0mini0sidebar.insert( f0= 'pa4520', f1= '(4520)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4521', f1= '(4521)&times;')
    db.dfixed0header0mini0sidebar.insert( f0= 'hd4522', f1= '(4522)Modal title')
    db.dfixed0header0mini0sidebar.insert( f0= 'bu4523', f1= '(4523)Close')
    db.commit()
#
