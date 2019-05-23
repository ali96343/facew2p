#
# table for controller: button
#

from gluon.contrib.populate import populate

db.define_table('dbutton', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dbutton.id ).count():
    db.dbutton.insert( f0= 'aa3606', f1= '(3606)Dashboard 1')
    db.dbutton.insert( f0= 'aa3608', f1= '(3608)Dashboard 2')
    db.dbutton.insert( f0= 'aa3610', f1= '(3610)Dashboard 3')
    db.dbutton.insert( f0= 'aa3612', f1= '(3612)Dashboard 4')
    db.dbutton.insert( f0= 'aa3618', f1= '(3618)Login')
    db.dbutton.insert( f0= 'aa3620', f1= '(3620)Register')
    db.dbutton.insert( f0= 'aa3622', f1= '(3622)Forget Password')
    db.dbutton.insert( f0= 'aa3624', f1= '(3624)Button')
    db.dbutton.insert( f0= 'aa3626', f1= '(3626)Badges')
    db.dbutton.insert( f0= 'aa3628', f1= '(3628)Tabs')
    db.dbutton.insert( f0= 'aa3630', f1= '(3630)Cards')
    db.dbutton.insert( f0= 'aa3632', f1= '(3632)Alerts')
    db.dbutton.insert( f0= 'aa3634', f1= '(3634)Progress Bars')
    db.dbutton.insert( f0= 'aa3636', f1= '(3636)Modals')
    db.dbutton.insert( f0= 'aa3638', f1= '(3638)Switchs')
    db.dbutton.insert( f0= 'aa3640', f1= '(3640)Grids')
    db.dbutton.insert( f0= 'aa3642', f1= '(3642)Fontawesome Icon')
    db.dbutton.insert( f0= 'aa3644', f1= '(3644)Typography')
    db.dbutton.insert( f0= 'aa3647', f1= '(3647)Dashboard 1')
    db.dbutton.insert( f0= 'aa3649', f1= '(3649)Dashboard 2')
    db.dbutton.insert( f0= 'aa3651', f1= '(3651)Dashboard 3')
    db.dbutton.insert( f0= 'aa3653', f1= '(3653)Dashboard 4')
    db.dbutton.insert( f0= 'aa3659', f1= '(3659)Login')
    db.dbutton.insert( f0= 'aa3661', f1= '(3661)Register')
    db.dbutton.insert( f0= 'aa3663', f1= '(3663)Forget Password')
    db.dbutton.insert( f0= 'aa3665', f1= '(3665)Button')
    db.dbutton.insert( f0= 'aa3667', f1= '(3667)Badges')
    db.dbutton.insert( f0= 'aa3669', f1= '(3669)Tabs')
    db.dbutton.insert( f0= 'aa3671', f1= '(3671)Cards')
    db.dbutton.insert( f0= 'aa3673', f1= '(3673)Alerts')
    db.dbutton.insert( f0= 'aa3675', f1= '(3675)Progress Bars')
    db.dbutton.insert( f0= 'aa3677', f1= '(3677)Modals')
    db.dbutton.insert( f0= 'aa3679', f1= '(3679)Switchs')
    db.dbutton.insert( f0= 'aa3681', f1= '(3681)Grids')
    db.dbutton.insert( f0= 'aa3683', f1= '(3683)Fontawesome Icon')
    db.dbutton.insert( f0= 'aa3685', f1= '(3685)Typography')
    db.dbutton.insert( f0= 'pb3686', f1= '(3686)Search for datas &amp; reports...')
    db.dbutton.insert( f0= 'pa3687', f1= '(3687)You have 2 news message')
    db.dbutton.insert( f0= 'hh3689', f1= '(3689)Michelle Moreno')
    db.dbutton.insert( f0= 'pa3690', f1= '(3690)Have sent a photo')
    db.dbutton.insert( f0= 'sx3691', f1= '(3691)3 min ago')
    db.dbutton.insert( f0= 'hh3693', f1= '(3693)Diane Myers')
    db.dbutton.insert( f0= 'pa3694', f1= '(3694)You are now connected on message')
    db.dbutton.insert( f0= 'sx3695', f1= '(3695)Yesterday')
    db.dbutton.insert( f0= 'aa3696', f1= '(3696)View all messages')
    db.dbutton.insert( f0= 'pa3697', f1= '(3697)You have 3 New Emails')
    db.dbutton.insert( f0= 'pa3699', f1= '(3699)Meeting about new dashboard...')
    db.dbutton.insert( f0= 'sp3700', f1= '(3700)Cynthia Harvey, 3 min ago')
    db.dbutton.insert( f0= 'pa3702', f1= '(3702)Meeting about new dashboard...')
    db.dbutton.insert( f0= 'sp3703', f1= '(3703)Cynthia Harvey, Yesterday')
    db.dbutton.insert( f0= 'pa3705', f1= '(3705)Meeting about new dashboard...')
    db.dbutton.insert( f0= 'sp3706', f1= '(3706)Cynthia Harvey, April 12,,2018')
    db.dbutton.insert( f0= 'aa3707', f1= '(3707)See all emails')
    db.dbutton.insert( f0= 'pa3708', f1= '(3708)You have 3 Notifications')
    db.dbutton.insert( f0= 'pa3709', f1= '(3709)You got a email notification')
    db.dbutton.insert( f0= 'sx3710', f1= '(3710)April 12, 2018 06:50')
    db.dbutton.insert( f0= 'pa3711', f1= '(3711)Your account has been blocked')
    db.dbutton.insert( f0= 'sx3712', f1= '(3712)April 12, 2018 06:50')
    db.dbutton.insert( f0= 'pa3713', f1= '(3713)You got a new file')
    db.dbutton.insert( f0= 'sx3714', f1= '(3714)April 12, 2018 06:50')
    db.dbutton.insert( f0= 'aa3715', f1= '(3715)All notifications')
    db.dbutton.insert( f0= 'aa3717', f1= '(3717)john doe')
    db.dbutton.insert( f0= 'aa3719', f1= '(3719)john doe')
    db.dbutton.insert( f0= 'sx3720', f1= '(3720)johndoe@example.com')
    db.dbutton.insert( f0= 'sp3721', f1= '(3721)Badges')
    db.dbutton.insert( f0= 'bu3722', f1= '(3722)Primary')
    db.dbutton.insert( f0= 'bu3723', f1= '(3723)Secondary')
    db.dbutton.insert( f0= 'bu3724', f1= '(3724)Success')
    db.dbutton.insert( f0= 'bu3725', f1= '(3725)Danger')
    db.dbutton.insert( f0= 'bu3726', f1= '(3726)Warning')
    db.dbutton.insert( f0= 'bu3727', f1= '(3727)Info')
    db.dbutton.insert( f0= 'bu3728', f1= '(3728)Link')
    db.dbutton.insert( f0= 'sp3729', f1= '(3729)Button tags')
    db.dbutton.insert( f0= 'aa3730', f1= '(3730)Link')
    db.dbutton.insert( f0= 'bu3731', f1= '(3731)Button')
    db.dbutton.insert( f0= 'sp3732', f1= '(3732)Disabled state')
    db.dbutton.insert( f0= 'bu3733', f1= '(3733)Primary')
    db.dbutton.insert( f0= 'bu3734', f1= '(3734)Secondary')
    db.dbutton.insert( f0= 'bu3735', f1= '(3735)Success')
    db.dbutton.insert( f0= 'bu3736', f1= '(3736)Danger')
    db.dbutton.insert( f0= 'bu3737', f1= '(3737)Warning')
    db.dbutton.insert( f0= 'bu3738', f1= '(3738)Info')
    db.dbutton.insert( f0= 'bu3739', f1= '(3739)Link')
    db.dbutton.insert( f0= 'sp3740', f1= '(3740)Button with Icons')
    db.dbutton.insert( f0= 'sp3741', f1= '(3741)Small Button')
    db.dbutton.insert( f0= 'bu3742', f1= '(3742)Primary')
    db.dbutton.insert( f0= 'bu3743', f1= '(3743)Secondary')
    db.dbutton.insert( f0= 'bu3744', f1= '(3744)Success')
    db.dbutton.insert( f0= 'bu3745', f1= '(3745)Warning')
    db.dbutton.insert( f0= 'bu3746', f1= '(3746)Danger')
    db.dbutton.insert( f0= 'bu3747', f1= '(3747)Link')
    db.dbutton.insert( f0= 'sp3748', f1= '(3748)Small Button with Icons')
    db.dbutton.insert( f0= 'sp3749', f1= '(3749)Large Button')
    db.dbutton.insert( f0= 'bu3750', f1= '(3750)Primary')
    db.dbutton.insert( f0= 'bu3751', f1= '(3751)Secondary')
    db.dbutton.insert( f0= 'bu3752', f1= '(3752)Success')
    db.dbutton.insert( f0= 'bu3753', f1= '(3753)Warning')
    db.dbutton.insert( f0= 'bu3754', f1= '(3754)Danger')
    db.dbutton.insert( f0= 'bu3755', f1= '(3755)Link')
    db.dbutton.insert( f0= 'sp3756', f1= '(3756)Large Active Button')
    db.dbutton.insert( f0= 'bu3757', f1= '(3757)Primary')
    db.dbutton.insert( f0= 'bu3758', f1= '(3758)Secondary')
    db.dbutton.insert( f0= 'bu3759', f1= '(3759)Success')
    db.dbutton.insert( f0= 'bu3760', f1= '(3760)Warning')
    db.dbutton.insert( f0= 'bu3761', f1= '(3761)Danger')
    db.dbutton.insert( f0= 'bu3762', f1= '(3762)Link')
    db.dbutton.insert( f0= 'sp3763', f1= '(3763)Block Level Buttons')
    db.dbutton.insert( f0= 'bu3764', f1= '(3764)Block level button')
    db.dbutton.insert( f0= 'bu3765', f1= '(3765)Block level button')
    db.dbutton.insert( f0= 'bu3766', f1= '(3766)Primary')
    db.dbutton.insert( f0= 'bu3767', f1= '(3767)Secondary')
    db.dbutton.insert( f0= 'bu3768', f1= '(3768)Success')
    db.dbutton.insert( f0= 'bu3769', f1= '(3769)Warning')
    db.dbutton.insert( f0= 'bu3770', f1= '(3770)Danger')
    db.dbutton.insert( f0= 'bu3771', f1= '(3771)Link')
    db.dbutton.insert( f0= 'sp3772', f1= '(3772)Outline Buttons')
    db.dbutton.insert( f0= 'bu3773', f1= '(3773)Primary')
    db.dbutton.insert( f0= 'bu3774', f1= '(3774)Secondary')
    db.dbutton.insert( f0= 'bu3775', f1= '(3775)Success')
    db.dbutton.insert( f0= 'bu3776', f1= '(3776)Danger')
    db.dbutton.insert( f0= 'bu3777', f1= '(3777)Warning')
    db.dbutton.insert( f0= 'bu3778', f1= '(3778)Info')
    db.dbutton.insert( f0= 'bu3779', f1= '(3779)Link')
    db.dbutton.insert( f0= 'sp3780', f1= '(3780)Button tags')
    db.dbutton.insert( f0= 'aa3781', f1= '(3781)Link')
    db.dbutton.insert( f0= 'bu3782', f1= '(3782)Button')
    db.dbutton.insert( f0= 'sp3783', f1= '(3783)Disabled state')
    db.dbutton.insert( f0= 'bu3784', f1= '(3784)Primary')
    db.dbutton.insert( f0= 'bu3785', f1= '(3785)Secondary')
    db.dbutton.insert( f0= 'bu3786', f1= '(3786)Success')
    db.dbutton.insert( f0= 'bu3787', f1= '(3787)Danger')
    db.dbutton.insert( f0= 'bu3788', f1= '(3788)Warning')
    db.dbutton.insert( f0= 'bu3789', f1= '(3789)Info')
    db.dbutton.insert( f0= 'bu3790', f1= '(3790)Link')
    db.dbutton.insert( f0= 'sp3791', f1= '(3791)Button with Icons')
    db.dbutton.insert( f0= 'sp3792', f1= '(3792)Small Button')
    db.dbutton.insert( f0= 'bu3793', f1= '(3793)Primary')
    db.dbutton.insert( f0= 'bu3794', f1= '(3794)Secondary')
    db.dbutton.insert( f0= 'bu3795', f1= '(3795)Success')
    db.dbutton.insert( f0= 'bu3796', f1= '(3796)Warning')
    db.dbutton.insert( f0= 'bu3797', f1= '(3797)Danger')
    db.dbutton.insert( f0= 'bu3798', f1= '(3798)Link')
    db.dbutton.insert( f0= 'sp3799', f1= '(3799)Small Button with Icons')
    db.dbutton.insert( f0= 'sp3800', f1= '(3800)Large Button')
    db.dbutton.insert( f0= 'bu3801', f1= '(3801)Primary')
    db.dbutton.insert( f0= 'bu3802', f1= '(3802)Secondary')
    db.dbutton.insert( f0= 'bu3803', f1= '(3803)Success')
    db.dbutton.insert( f0= 'bu3804', f1= '(3804)Warning')
    db.dbutton.insert( f0= 'bu3805', f1= '(3805)Danger')
    db.dbutton.insert( f0= 'bu3806', f1= '(3806)Link')
    db.dbutton.insert( f0= 'sp3807', f1= '(3807)Large Active Button')
    db.dbutton.insert( f0= 'bu3808', f1= '(3808)Primary')
    db.dbutton.insert( f0= 'bu3809', f1= '(3809)Secondary')
    db.dbutton.insert( f0= 'bu3810', f1= '(3810)Success')
    db.dbutton.insert( f0= 'bu3811', f1= '(3811)Warning')
    db.dbutton.insert( f0= 'bu3812', f1= '(3812)Danger')
    db.dbutton.insert( f0= 'bu3813', f1= '(3813)Link')
    db.dbutton.insert( f0= 'sp3814', f1= '(3814)Block Level Buttons')
    db.dbutton.insert( f0= 'bu3815', f1= '(3815)Block level button')
    db.dbutton.insert( f0= 'bu3816', f1= '(3816)Block level button')
    db.dbutton.insert( f0= 'bu3817', f1= '(3817)Primary')
    db.dbutton.insert( f0= 'bu3818', f1= '(3818)Secondary')
    db.dbutton.insert( f0= 'bu3819', f1= '(3819)Success')
    db.dbutton.insert( f0= 'bu3820', f1= '(3820)Warning')
    db.dbutton.insert( f0= 'bu3821', f1= '(3821)Danger')
    db.dbutton.insert( f0= 'bu3822', f1= '(3822)Link')
    db.commit()
#
