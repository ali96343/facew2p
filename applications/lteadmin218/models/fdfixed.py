#
# table for controller: fixed
#

from gluon.contrib.populate import populate

db.define_table('dfixed', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dfixed.id ).count():
    db.dfixed.insert( f0= 'bb4321', f1= '(4321)A')
    db.dfixed.insert( f0= 'sx4322', f1= '(4322)LT')
    db.dfixed.insert( f0= 'bb4323', f1= '(4323)Admin')
    db.dfixed.insert( f0= 'sx4324', f1= '(4324)LTE')
    db.dfixed.insert( f0= 'sx4325', f1= '(4325)Toggle navigation')
    db.dfixed.insert( f0= 'sx4326', f1= '(4326)4')
    db.dfixed.insert( f0= 'lb4327', f1= '(4327)You have 4 messages')
    db.dfixed.insert( f0= 'ib4329', f1= '(4329)5 mins')
    db.dfixed.insert( f0= 'pa4330', f1= '(4330)Why not buy a new awesome theme?')
    db.dfixed.insert( f0= 'aa4331', f1= '(4331)See All Messages')
    db.dfixed.insert( f0= 'lb4332', f1= '(4332)You have 10 notifications')
    db.dfixed.insert( f0= 'aa4333', f1= '(4333)View all')
    db.dfixed.insert( f0= 'sx4334', f1= '(4334)9')
    db.dfixed.insert( f0= 'lb4335', f1= '(4335)You have 9 tasks')
    db.dfixed.insert( f0= 'sx4336', f1= '(4336)20% Complete')
    db.dfixed.insert( f0= 'aa4337', f1= '(4337)View all tasks')
    db.dfixed.insert( f0= 'sx4339', f1= '(4339)Alexander Pierce')
    db.dfixed.insert( f0= 'ic4341', f1= '(4341)Member since Nov. 2012')
    db.dfixed.insert( f0= 'aa4342', f1= '(4342)Followers')
    db.dfixed.insert( f0= 'aa4343', f1= '(4343)Sales')
    db.dfixed.insert( f0= 'aa4344', f1= '(4344)Friends')
    db.dfixed.insert( f0= 'aa4345', f1= '(4345)Profile')
    db.dfixed.insert( f0= 'aa4346', f1= '(4346)Sign out')
    db.dfixed.insert( f0= 'pa4348', f1= '(4348)Alexander Pierce')
    db.dfixed.insert( f0= 'ia4349', f1= '(4349)Online')
    db.dfixed.insert( f0= 'pb4350', f1= '(4350)Search...')
    db.dfixed.insert( f0= 'lb4351', f1= '(4351)MAIN NAVIGATION')
    db.dfixed.insert( f0= 'sp4352', f1= '(4352)Dashboard')
    db.dfixed.insert( f0= 'ia4354', f1= '(4354)Dashboard v1')
    db.dfixed.insert( f0= 'ia4356', f1= '(4356)Dashboard v2')
    db.dfixed.insert( f0= 'sp4357', f1= '(4357)Layout Options')
    db.dfixed.insert( f0= 'sx4358', f1= '(4358)4')
    db.dfixed.insert( f0= 'ia4360', f1= '(4360)Top Navigation')
    db.dfixed.insert( f0= 'ia4362', f1= '(4362)Boxed')
    db.dfixed.insert( f0= 'ia4364', f1= '(4364)Fixed')
    db.dfixed.insert( f0= 'ia4366', f1= '(4366)Collapsed Sidebar')
    db.dfixed.insert( f0= 'sp4368', f1= '(4368)Widgets')
    db.dfixed.insert( f0= 'ic4369', f1= '(4369)new')
    db.dfixed.insert( f0= 'sp4370', f1= '(4370)Charts')
    db.dfixed.insert( f0= 'ia4372', f1= '(4372)ChartJS')
    db.dfixed.insert( f0= 'ia4374', f1= '(4374)Morris')
    db.dfixed.insert( f0= 'ia4376', f1= '(4376)Flot')
    db.dfixed.insert( f0= 'ia4378', f1= '(4378)Inline charts')
    db.dfixed.insert( f0= 'sp4379', f1= '(4379)UI Elements')
    db.dfixed.insert( f0= 'ia4381', f1= '(4381)General')
    db.dfixed.insert( f0= 'ia4383', f1= '(4383)Icons')
    db.dfixed.insert( f0= 'ia4385', f1= '(4385)Buttons')
    db.dfixed.insert( f0= 'ia4387', f1= '(4387)Sliders')
    db.dfixed.insert( f0= 'ia4389', f1= '(4389)Timeline')
    db.dfixed.insert( f0= 'ia4391', f1= '(4391)Modals')
    db.dfixed.insert( f0= 'sp4392', f1= '(4392)Forms')
    db.dfixed.insert( f0= 'ia4394', f1= '(4394)General Elements')
    db.dfixed.insert( f0= 'ia4396', f1= '(4396)Advanced Elements')
    db.dfixed.insert( f0= 'ia4398', f1= '(4398)Editors')
    db.dfixed.insert( f0= 'sp4399', f1= '(4399)Tables')
    db.dfixed.insert( f0= 'ia4401', f1= '(4401)Simple tables')
    db.dfixed.insert( f0= 'ia4403', f1= '(4403)Data tables')
    db.dfixed.insert( f0= 'sp4405', f1= '(4405)Calendar')
    db.dfixed.insert( f0= 'ic4406', f1= '(4406)3')
    db.dfixed.insert( f0= 'sp4408', f1= '(4408)Mailbox')
    db.dfixed.insert( f0= 'ic4409', f1= '(4409)5')
    db.dfixed.insert( f0= 'sp4410', f1= '(4410)Examples')
    db.dfixed.insert( f0= 'ia4412', f1= '(4412)Invoice')
    db.dfixed.insert( f0= 'ia4414', f1= '(4414)Profile')
    db.dfixed.insert( f0= 'ia4416', f1= '(4416)Login')
    db.dfixed.insert( f0= 'ia4418', f1= '(4418)Register')
    db.dfixed.insert( f0= 'ia4420', f1= '(4420)Lockscreen')
    db.dfixed.insert( f0= 'ia4422', f1= '(4422)404 Error')
    db.dfixed.insert( f0= 'ia4424', f1= '(4424)500 Error')
    db.dfixed.insert( f0= 'ia4426', f1= '(4426)Blank Page')
    db.dfixed.insert( f0= 'ia4428', f1= '(4428)Pace Page')
    db.dfixed.insert( f0= 'sp4429', f1= '(4429)Multilevel')
    db.dfixed.insert( f0= 'ia4430', f1= '(4430)Level One')
    db.dfixed.insert( f0= 'ia4431', f1= '(4431)Level Two')
    db.dfixed.insert( f0= 'ia4432', f1= '(4432)Level Three')
    db.dfixed.insert( f0= 'ia4433', f1= '(4433)Level Three')
    db.dfixed.insert( f0= 'ia4434', f1= '(4434)Level One')
    db.dfixed.insert( f0= 'sp4435', f1= '(4435)Documentation')
    db.dfixed.insert( f0= 'lb4436', f1= '(4436)LABELS')
    db.dfixed.insert( f0= 'sp4437', f1= '(4437)Important')
    db.dfixed.insert( f0= 'sp4438', f1= '(4438)Warning')
    db.dfixed.insert( f0= 'sp4439', f1= '(4439)Information')
    db.dfixed.insert( f0= 'ic4440', f1= '(4440)Blank example to the fixed layout')
    db.dfixed.insert( f0= 'ia4441', f1= '(4441)Home')
    db.dfixed.insert( f0= 'aa4442', f1= '(4442)Layout')
    db.dfixed.insert( f0= 'lb4443', f1= '(4443)Fixed')
    db.dfixed.insert( f0= 'hh4444', f1= '(4444)Tip!')
    db.dfixed.insert( f0= 'hc4445', f1= '(4445)Title')
    db.dfixed.insert( f0= 'bb4446', f1= '(4446)Version')
    db.dfixed.insert( f0= 'aa4447', f1= '(4447)AdminLTE')
    db.dfixed.insert( f0= 'hc4448', f1= '(4448)Recent Activity')
    db.dfixed.insert( f0= 'hd4449', f1= '(4449)Langdon s Birthday')
    db.dfixed.insert( f0= 'pa4450', f1= '(4450)Will be 23 on April 24th')
    db.dfixed.insert( f0= 'hd4451', f1= '(4451)Frodo Updated His Profile')
    db.dfixed.insert( f0= 'pa4452', f1= '(4452)New phone +1(800)555-1234')
    db.dfixed.insert( f0= 'hd4453', f1= '(4453)Nora Joined Mailing List')
    db.dfixed.insert( f0= 'pa4454', f1= '(4454)nora@example.com')
    db.dfixed.insert( f0= 'hd4455', f1= '(4455)Cron Job 254 Executed')
    db.dfixed.insert( f0= 'pa4456', f1= '(4456)Execution time 5 seconds')
    db.dfixed.insert( f0= 'hc4457', f1= '(4457)Tasks Progress')
    db.dfixed.insert( f0= 'di4458', f1= '(4458)Stats Tab Content')
    db.dfixed.insert( f0= 'hc4459', f1= '(4459)General Settings')
    db.dfixed.insert( f0= 'hc4460', f1= '(4460)Chat Settings')
    db.commit()
#
