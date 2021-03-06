#
# table for controller: sliders
#

from gluon.contrib.populate import populate

db.define_table('dsliders', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dsliders.id ).count():
    db.dsliders.insert( f0= 'bb3924', f1= '(3924)A')
    db.dsliders.insert( f0= 'sx3925', f1= '(3925)LT')
    db.dsliders.insert( f0= 'bb3926', f1= '(3926)Admin')
    db.dsliders.insert( f0= 'sx3927', f1= '(3927)LTE')
    db.dsliders.insert( f0= 'sx3928', f1= '(3928)Toggle navigation')
    db.dsliders.insert( f0= 'sx3929', f1= '(3929)4')
    db.dsliders.insert( f0= 'lb3930', f1= '(3930)You have 4 messages')
    db.dsliders.insert( f0= 'ib3932', f1= '(3932)5 mins')
    db.dsliders.insert( f0= 'pa3933', f1= '(3933)Why not buy a new awesome theme?')
    db.dsliders.insert( f0= 'ib3935', f1= '(3935)2 hours')
    db.dsliders.insert( f0= 'pa3936', f1= '(3936)Why not buy a new awesome theme?')
    db.dsliders.insert( f0= 'ib3938', f1= '(3938)Today')
    db.dsliders.insert( f0= 'pa3939', f1= '(3939)Why not buy a new awesome theme?')
    db.dsliders.insert( f0= 'ib3941', f1= '(3941)Yesterday')
    db.dsliders.insert( f0= 'pa3942', f1= '(3942)Why not buy a new awesome theme?')
    db.dsliders.insert( f0= 'ib3944', f1= '(3944)2 days')
    db.dsliders.insert( f0= 'pa3945', f1= '(3945)Why not buy a new awesome theme?')
    db.dsliders.insert( f0= 'aa3946', f1= '(3946)See All Messages')
    db.dsliders.insert( f0= 'lb3947', f1= '(3947)You have 10 notifications')
    db.dsliders.insert( f0= 'aa3948', f1= '(3948)View all')
    db.dsliders.insert( f0= 'sx3949', f1= '(3949)9')
    db.dsliders.insert( f0= 'lb3950', f1= '(3950)You have 9 tasks')
    db.dsliders.insert( f0= 'sx3951', f1= '(3951)20% Complete')
    db.dsliders.insert( f0= 'sx3952', f1= '(3952)40% Complete')
    db.dsliders.insert( f0= 'sx3953', f1= '(3953)60% Complete')
    db.dsliders.insert( f0= 'sx3954', f1= '(3954)80% Complete')
    db.dsliders.insert( f0= 'aa3955', f1= '(3955)View all tasks')
    db.dsliders.insert( f0= 'sx3957', f1= '(3957)Alexander Pierce')
    db.dsliders.insert( f0= 'ic3959', f1= '(3959)Member since Nov. 2012')
    db.dsliders.insert( f0= 'aa3960', f1= '(3960)Followers')
    db.dsliders.insert( f0= 'aa3961', f1= '(3961)Sales')
    db.dsliders.insert( f0= 'aa3962', f1= '(3962)Friends')
    db.dsliders.insert( f0= 'aa3963', f1= '(3963)Profile')
    db.dsliders.insert( f0= 'aa3964', f1= '(3964)Sign out')
    db.dsliders.insert( f0= 'pa3966', f1= '(3966)Alexander Pierce')
    db.dsliders.insert( f0= 'ia3967', f1= '(3967)Online')
    db.dsliders.insert( f0= 'pb3968', f1= '(3968)Search...')
    db.dsliders.insert( f0= 'lb3969', f1= '(3969)MAIN NAVIGATION')
    db.dsliders.insert( f0= 'sp3970', f1= '(3970)Dashboard')
    db.dsliders.insert( f0= 'ia3972', f1= '(3972)Dashboard v1')
    db.dsliders.insert( f0= 'ia3974', f1= '(3974)Dashboard v2')
    db.dsliders.insert( f0= 'sp3975', f1= '(3975)Layout Options')
    db.dsliders.insert( f0= 'sx3976', f1= '(3976)4')
    db.dsliders.insert( f0= 'ia3978', f1= '(3978)Top Navigation')
    db.dsliders.insert( f0= 'ia3980', f1= '(3980)Boxed')
    db.dsliders.insert( f0= 'ia3982', f1= '(3982)Fixed')
    db.dsliders.insert( f0= 'ia3984', f1= '(3984)Collapsed Sidebar')
    db.dsliders.insert( f0= 'sp3986', f1= '(3986)Widgets')
    db.dsliders.insert( f0= 'ic3987', f1= '(3987)new')
    db.dsliders.insert( f0= 'sp3988', f1= '(3988)Charts')
    db.dsliders.insert( f0= 'ia3990', f1= '(3990)ChartJS')
    db.dsliders.insert( f0= 'ia3992', f1= '(3992)Morris')
    db.dsliders.insert( f0= 'ia3994', f1= '(3994)Flot')
    db.dsliders.insert( f0= 'ia3996', f1= '(3996)Inline charts')
    db.dsliders.insert( f0= 'sp3997', f1= '(3997)UI Elements')
    db.dsliders.insert( f0= 'ia3999', f1= '(3999)General')
    db.dsliders.insert( f0= 'ia4001', f1= '(4001)Icons')
    db.dsliders.insert( f0= 'ia4003', f1= '(4003)Buttons')
    db.dsliders.insert( f0= 'ia4005', f1= '(4005)Sliders')
    db.dsliders.insert( f0= 'ia4007', f1= '(4007)Timeline')
    db.dsliders.insert( f0= 'ia4009', f1= '(4009)Modals')
    db.dsliders.insert( f0= 'sp4010', f1= '(4010)Forms')
    db.dsliders.insert( f0= 'ia4012', f1= '(4012)General Elements')
    db.dsliders.insert( f0= 'ia4014', f1= '(4014)Advanced Elements')
    db.dsliders.insert( f0= 'ia4016', f1= '(4016)Editors')
    db.dsliders.insert( f0= 'sp4017', f1= '(4017)Tables')
    db.dsliders.insert( f0= 'ia4019', f1= '(4019)Simple tables')
    db.dsliders.insert( f0= 'ia4021', f1= '(4021)Data tables')
    db.dsliders.insert( f0= 'sp4023', f1= '(4023)Calendar')
    db.dsliders.insert( f0= 'ic4024', f1= '(4024)3')
    db.dsliders.insert( f0= 'sp4026', f1= '(4026)Mailbox')
    db.dsliders.insert( f0= 'ic4027', f1= '(4027)5')
    db.dsliders.insert( f0= 'sp4028', f1= '(4028)Examples')
    db.dsliders.insert( f0= 'ia4030', f1= '(4030)Invoice')
    db.dsliders.insert( f0= 'ia4032', f1= '(4032)Profile')
    db.dsliders.insert( f0= 'ia4034', f1= '(4034)Login')
    db.dsliders.insert( f0= 'ia4036', f1= '(4036)Register')
    db.dsliders.insert( f0= 'ia4038', f1= '(4038)Lockscreen')
    db.dsliders.insert( f0= 'ia4040', f1= '(4040)404 Error')
    db.dsliders.insert( f0= 'ia4042', f1= '(4042)500 Error')
    db.dsliders.insert( f0= 'ia4044', f1= '(4044)Blank Page')
    db.dsliders.insert( f0= 'ia4046', f1= '(4046)Pace Page')
    db.dsliders.insert( f0= 'sp4047', f1= '(4047)Multilevel')
    db.dsliders.insert( f0= 'ia4048', f1= '(4048)Level One')
    db.dsliders.insert( f0= 'ia4049', f1= '(4049)Level Two')
    db.dsliders.insert( f0= 'ia4050', f1= '(4050)Level Three')
    db.dsliders.insert( f0= 'ia4051', f1= '(4051)Level Three')
    db.dsliders.insert( f0= 'ia4052', f1= '(4052)Level One')
    db.dsliders.insert( f0= 'sp4053', f1= '(4053)Documentation')
    db.dsliders.insert( f0= 'lb4054', f1= '(4054)LABELS')
    db.dsliders.insert( f0= 'sp4055', f1= '(4055)Important')
    db.dsliders.insert( f0= 'sp4056', f1= '(4056)Warning')
    db.dsliders.insert( f0= 'sp4057', f1= '(4057)Information')
    db.dsliders.insert( f0= 'ic4058', f1= '(4058)range sliders')
    db.dsliders.insert( f0= 'ia4059', f1= '(4059)Home')
    db.dsliders.insert( f0= 'aa4060', f1= '(4060)UI')
    db.dsliders.insert( f0= 'lb4061', f1= '(4061)Sliders')
    db.dsliders.insert( f0= 'hc4062', f1= '(4062)Bootstrap Slider')
    db.dsliders.insert( f0= 'pa4063', f1= '(4063)data-slider-id= red')
    db.dsliders.insert( f0= 'pa4064', f1= '(4064)data-slider-id= blue')
    db.dsliders.insert( f0= 'pa4065', f1= '(4065)data-slider-id= green')
    db.dsliders.insert( f0= 'pa4066', f1= '(4066)data-slider-id= yellow')
    db.dsliders.insert( f0= 'pa4067', f1= '(4067)data-slider-id= aqua')
    db.dsliders.insert( f0= 'pc4068', f1= '(4068)data-slider-id= purple')
    db.dsliders.insert( f0= 'bb4069', f1= '(4069)Version')
    db.dsliders.insert( f0= 'aa4070', f1= '(4070)AdminLTE')
    db.dsliders.insert( f0= 'hc4071', f1= '(4071)Recent Activity')
    db.dsliders.insert( f0= 'hd4072', f1= '(4072)Langdon s Birthday')
    db.dsliders.insert( f0= 'pa4073', f1= '(4073)Will be 23 on April 24th')
    db.dsliders.insert( f0= 'hd4074', f1= '(4074)Frodo Updated His Profile')
    db.dsliders.insert( f0= 'pa4075', f1= '(4075)New phone +1(800)555-1234')
    db.dsliders.insert( f0= 'hd4076', f1= '(4076)Nora Joined Mailing List')
    db.dsliders.insert( f0= 'pa4077', f1= '(4077)nora@example.com')
    db.dsliders.insert( f0= 'hd4078', f1= '(4078)Cron Job 254 Executed')
    db.dsliders.insert( f0= 'pa4079', f1= '(4079)Execution time 5 seconds')
    db.dsliders.insert( f0= 'hc4080', f1= '(4080)Tasks Progress')
    db.dsliders.insert( f0= 'di4081', f1= '(4081)Stats Tab Content')
    db.dsliders.insert( f0= 'hc4082', f1= '(4082)General Settings')
    db.dsliders.insert( f0= 'hc4083', f1= '(4083)Chat Settings')
    db.commit()
#
