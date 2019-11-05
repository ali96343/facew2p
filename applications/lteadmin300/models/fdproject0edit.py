#
# table for controller: projectIIedit
#

from gluon.contrib.populate import populate

db.define_table('dproject0edit', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dproject0edit.id ).count():
    db.dproject0edit.insert( f0= 'aa4465', f1= '(4465)Home')
    db.dproject0edit.insert( f0= 'aa4466', f1= '(4466)Contact')
    db.dproject0edit.insert( f0= 'pb4467', f1= '(4467)Search')
    db.dproject0edit.insert( f0= 'sx4468', f1= '(4468)3')
    db.dproject0edit.insert( f0= 'pc4470', f1= '(4470)Call me whenever you can...')
    db.dproject0edit.insert( f0= 'pc4471', f1= '(4471)4 Hours Ago')
    db.dproject0edit.insert( f0= 'pc4473', f1= '(4473)I got your message bro')
    db.dproject0edit.insert( f0= 'pc4474', f1= '(4474)4 Hours Ago')
    db.dproject0edit.insert( f0= 'pc4476', f1= '(4476)The subject goes here')
    db.dproject0edit.insert( f0= 'pc4477', f1= '(4477)4 Hours Ago')
    db.dproject0edit.insert( f0= 'aa4478', f1= '(4478)See All Messages')
    db.dproject0edit.insert( f0= 'sx4479', f1= '(4479)15 Notifications')
    db.dproject0edit.insert( f0= 'sx4480', f1= '(4480)3 mins')
    db.dproject0edit.insert( f0= 'sx4481', f1= '(4481)12 hours')
    db.dproject0edit.insert( f0= 'sx4482', f1= '(4482)2 days')
    db.dproject0edit.insert( f0= 'aa4483', f1= '(4483)See All Notifications')
    db.dproject0edit.insert( f0= 'sx4486', f1= '(4486)AdminLTE 3')
    db.dproject0edit.insert( f0= 'aa4488', f1= '(4488)Alexander Pierce')
    db.dproject0edit.insert( f0= 'pa4490', f1= '(4490)Dashboard v1')
    db.dproject0edit.insert( f0= 'pa4492', f1= '(4492)Dashboard v2')
    db.dproject0edit.insert( f0= 'pa4494', f1= '(4494)Dashboard v3')
    db.dproject0edit.insert( f0= 'sx4496', f1= '(4496)New')
    db.dproject0edit.insert( f0= 'sx4497', f1= '(4497)6')
    db.dproject0edit.insert( f0= 'pa4499', f1= '(4499)Top Navigation')
    db.dproject0edit.insert( f0= 'pa4501', f1= '(4501)Boxed')
    db.dproject0edit.insert( f0= 'pa4503', f1= '(4503)Fixed Sidebar')
    db.dproject0edit.insert( f0= 'pa4505', f1= '(4505)Fixed Navbar')
    db.dproject0edit.insert( f0= 'pa4507', f1= '(4507)Fixed Footer')
    db.dproject0edit.insert( f0= 'pa4509', f1= '(4509)Collapsed Sidebar')
    db.dproject0edit.insert( f0= 'pa4511', f1= '(4511)ChartJS')
    db.dproject0edit.insert( f0= 'pa4513', f1= '(4513)Flot')
    db.dproject0edit.insert( f0= 'pa4515', f1= '(4515)Inline')
    db.dproject0edit.insert( f0= 'pa4517', f1= '(4517)General')
    db.dproject0edit.insert( f0= 'pa4519', f1= '(4519)Icons')
    db.dproject0edit.insert( f0= 'pa4521', f1= '(4521)Buttons')
    db.dproject0edit.insert( f0= 'pa4523', f1= '(4523)Sliders')
    db.dproject0edit.insert( f0= 'pa4525', f1= '(4525)Modals & Alerts')
    db.dproject0edit.insert( f0= 'pa4527', f1= '(4527)Navbar & Tabs')
    db.dproject0edit.insert( f0= 'pa4529', f1= '(4529)Timeline')
    db.dproject0edit.insert( f0= 'pa4531', f1= '(4531)Ribbons')
    db.dproject0edit.insert( f0= 'pa4533', f1= '(4533)General Elements')
    db.dproject0edit.insert( f0= 'pa4535', f1= '(4535)Advanced Elements')
    db.dproject0edit.insert( f0= 'pa4537', f1= '(4537)Editors')
    db.dproject0edit.insert( f0= 'pa4539', f1= '(4539)Simple Tables')
    db.dproject0edit.insert( f0= 'pa4541', f1= '(4541)DataTables')
    db.dproject0edit.insert( f0= 'pa4543', f1= '(4543)jsGrid')
    db.dproject0edit.insert( f0= 'lb4544', f1= '(4544)EXAMPLES')
    db.dproject0edit.insert( f0= 'sx4546', f1= '(4546)2')
    db.dproject0edit.insert( f0= 'pa4549', f1= '(4549)Inbox')
    db.dproject0edit.insert( f0= 'pa4551', f1= '(4551)Compose')
    db.dproject0edit.insert( f0= 'pa4553', f1= '(4553)Read')
    db.dproject0edit.insert( f0= 'pa4555', f1= '(4555)Invoice')
    db.dproject0edit.insert( f0= 'pa4557', f1= '(4557)Profile')
    db.dproject0edit.insert( f0= 'pa4559', f1= '(4559)E-commerce')
    db.dproject0edit.insert( f0= 'pa4561', f1= '(4561)Projects')
    db.dproject0edit.insert( f0= 'pa4563', f1= '(4563)Project Add')
    db.dproject0edit.insert( f0= 'pa4565', f1= '(4565)Project Edit')
    db.dproject0edit.insert( f0= 'pa4567', f1= '(4567)Project Detail')
    db.dproject0edit.insert( f0= 'pa4569', f1= '(4569)Contacts')
    db.dproject0edit.insert( f0= 'pa4571', f1= '(4571)Login')
    db.dproject0edit.insert( f0= 'pa4573', f1= '(4573)Register')
    db.dproject0edit.insert( f0= 'pa4575', f1= '(4575)Forgot Password')
    db.dproject0edit.insert( f0= 'pa4577', f1= '(4577)Recover Password')
    db.dproject0edit.insert( f0= 'pa4579', f1= '(4579)Lockscreen')
    db.dproject0edit.insert( f0= 'pa4581', f1= '(4581)Legacy User Menu')
    db.dproject0edit.insert( f0= 'pa4583', f1= '(4583)Language Menu')
    db.dproject0edit.insert( f0= 'pa4585', f1= '(4585)Error 404')
    db.dproject0edit.insert( f0= 'pa4587', f1= '(4587)Error 500')
    db.dproject0edit.insert( f0= 'pa4589', f1= '(4589)Pace')
    db.dproject0edit.insert( f0= 'pa4591', f1= '(4591)Blank Page')
    db.dproject0edit.insert( f0= 'pa4593', f1= '(4593)Starter Page')
    db.dproject0edit.insert( f0= 'lb4594', f1= '(4594)MISCELLANEOUS')
    db.dproject0edit.insert( f0= 'pa4595', f1= '(4595)Documentation')
    db.dproject0edit.insert( f0= 'lb4596', f1= '(4596)MULTI LEVEL EXAMPLE')
    db.dproject0edit.insert( f0= 'pa4597', f1= '(4597)Level 1')
    db.dproject0edit.insert( f0= 'pa4598', f1= '(4598)Level 2')
    db.dproject0edit.insert( f0= 'pa4599', f1= '(4599)Level 3')
    db.dproject0edit.insert( f0= 'pa4600', f1= '(4600)Level 3')
    db.dproject0edit.insert( f0= 'pa4601', f1= '(4601)Level 3')
    db.dproject0edit.insert( f0= 'pa4602', f1= '(4602)Level 2')
    db.dproject0edit.insert( f0= 'pa4603', f1= '(4603)Level 1')
    db.dproject0edit.insert( f0= 'lb4604', f1= '(4604)LABELS')
    db.dproject0edit.insert( f0= 'pc4605', f1= '(4605)Important')
    db.dproject0edit.insert( f0= 'pa4606', f1= '(4606)Warning')
    db.dproject0edit.insert( f0= 'pa4607', f1= '(4607)Informational')
    db.dproject0edit.insert( f0= 'hh4608', f1= '(4608)Project Edit')
    db.dproject0edit.insert( f0= 'aa4609', f1= '(4609)Home')
    db.dproject0edit.insert( f0= 'lb4610', f1= '(4610)Project Edit')
    db.dproject0edit.insert( f0= 'hc4611', f1= '(4611)General')
    db.dproject0edit.insert( f0= 'hc4612', f1= '(4612)Budget')
    db.dproject0edit.insert( f0= 'hc4613', f1= '(4613)Files')
    db.dproject0edit.insert( f0= 'aa4614', f1= '(4614)Cancel')
    db.dproject0edit.insert( f0= 'bb4615', f1= '(4615)Version')
    db.dproject0edit.insert( f0= 'aa4616', f1= '(4616)AdminLTE.io')
    db.commit()
#
