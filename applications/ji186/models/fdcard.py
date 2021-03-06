#
# table for controller: card
#

from gluon.contrib.populate import populate

db.define_table('dcard', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcard.id ).count():
    db.dcard.insert( f0= 'aa3232', f1= '(3232)Dashboard 1')
    db.dcard.insert( f0= 'aa3234', f1= '(3234)Dashboard 2')
    db.dcard.insert( f0= 'aa3236', f1= '(3236)Dashboard 3')
    db.dcard.insert( f0= 'aa3238', f1= '(3238)Dashboard 4')
    db.dcard.insert( f0= 'aa3244', f1= '(3244)Login')
    db.dcard.insert( f0= 'aa3246', f1= '(3246)Register')
    db.dcard.insert( f0= 'aa3248', f1= '(3248)Forget Password')
    db.dcard.insert( f0= 'aa3250', f1= '(3250)Button')
    db.dcard.insert( f0= 'aa3252', f1= '(3252)Badges')
    db.dcard.insert( f0= 'aa3254', f1= '(3254)Tabs')
    db.dcard.insert( f0= 'aa3256', f1= '(3256)Cards')
    db.dcard.insert( f0= 'aa3258', f1= '(3258)Alerts')
    db.dcard.insert( f0= 'aa3260', f1= '(3260)Progress Bars')
    db.dcard.insert( f0= 'aa3262', f1= '(3262)Modals')
    db.dcard.insert( f0= 'aa3264', f1= '(3264)Switchs')
    db.dcard.insert( f0= 'aa3266', f1= '(3266)Grids')
    db.dcard.insert( f0= 'aa3268', f1= '(3268)Fontawesome Icon')
    db.dcard.insert( f0= 'aa3270', f1= '(3270)Typography')
    db.dcard.insert( f0= 'aa3273', f1= '(3273)Dashboard 1')
    db.dcard.insert( f0= 'aa3275', f1= '(3275)Dashboard 2')
    db.dcard.insert( f0= 'aa3277', f1= '(3277)Dashboard 3')
    db.dcard.insert( f0= 'aa3279', f1= '(3279)Dashboard 4')
    db.dcard.insert( f0= 'aa3285', f1= '(3285)Login')
    db.dcard.insert( f0= 'aa3287', f1= '(3287)Register')
    db.dcard.insert( f0= 'aa3289', f1= '(3289)Forget Password')
    db.dcard.insert( f0= 'aa3291', f1= '(3291)Button')
    db.dcard.insert( f0= 'aa3293', f1= '(3293)Badges')
    db.dcard.insert( f0= 'aa3295', f1= '(3295)Tabs')
    db.dcard.insert( f0= 'aa3297', f1= '(3297)Cards')
    db.dcard.insert( f0= 'aa3299', f1= '(3299)Alerts')
    db.dcard.insert( f0= 'aa3301', f1= '(3301)Progress Bars')
    db.dcard.insert( f0= 'aa3303', f1= '(3303)Modals')
    db.dcard.insert( f0= 'aa3305', f1= '(3305)Switchs')
    db.dcard.insert( f0= 'aa3307', f1= '(3307)Grids')
    db.dcard.insert( f0= 'aa3309', f1= '(3309)Fontawesome Icon')
    db.dcard.insert( f0= 'aa3311', f1= '(3311)Typography')
    db.dcard.insert( f0= 'pb3312', f1= '(3312)Search for datas &amp; reports...')
    db.dcard.insert( f0= 'pa3313', f1= '(3313)You have 2 news message')
    db.dcard.insert( f0= 'hh3315', f1= '(3315)Michelle Moreno')
    db.dcard.insert( f0= 'pa3316', f1= '(3316)Have sent a photo')
    db.dcard.insert( f0= 'sx3317', f1= '(3317)3 min ago')
    db.dcard.insert( f0= 'hh3319', f1= '(3319)Diane Myers')
    db.dcard.insert( f0= 'pa3320', f1= '(3320)You are now connected on message')
    db.dcard.insert( f0= 'sx3321', f1= '(3321)Yesterday')
    db.dcard.insert( f0= 'aa3322', f1= '(3322)View all messages')
    db.dcard.insert( f0= 'pa3323', f1= '(3323)You have 3 New Emails')
    db.dcard.insert( f0= 'pa3325', f1= '(3325)Meeting about new dashboard...')
    db.dcard.insert( f0= 'sp3326', f1= '(3326)Cynthia Harvey, 3 min ago')
    db.dcard.insert( f0= 'pa3328', f1= '(3328)Meeting about new dashboard...')
    db.dcard.insert( f0= 'sp3329', f1= '(3329)Cynthia Harvey, Yesterday')
    db.dcard.insert( f0= 'pa3331', f1= '(3331)Meeting about new dashboard...')
    db.dcard.insert( f0= 'sp3332', f1= '(3332)Cynthia Harvey, April 12,,2018')
    db.dcard.insert( f0= 'aa3333', f1= '(3333)See all emails')
    db.dcard.insert( f0= 'pa3334', f1= '(3334)You have 3 Notifications')
    db.dcard.insert( f0= 'pa3335', f1= '(3335)You got a email notification')
    db.dcard.insert( f0= 'sx3336', f1= '(3336)April 12, 2018 06:50')
    db.dcard.insert( f0= 'pa3337', f1= '(3337)Your account has been blocked')
    db.dcard.insert( f0= 'sx3338', f1= '(3338)April 12, 2018 06:50')
    db.dcard.insert( f0= 'pa3339', f1= '(3339)You got a new file')
    db.dcard.insert( f0= 'sx3340', f1= '(3340)April 12, 2018 06:50')
    db.dcard.insert( f0= 'aa3341', f1= '(3341)All notifications')
    db.dcard.insert( f0= 'aa3343', f1= '(3343)john doe')
    db.dcard.insert( f0= 'aa3345', f1= '(3345)john doe')
    db.dcard.insert( f0= 'sx3346', f1= '(3346)johndoe@example.com')
    db.dcard.insert( f0= 'he3348', f1= '(3348)Steven Lee')
    db.dcard.insert( f0= 'he3350', f1= '(3350)Steven Lee')
    db.dcard.insert( f0= 'he3352', f1= '(3352)Steven Lee')
    db.dcard.insert( f0= 'hb3354', f1= '(3354)Jim Doe')
    db.dcard.insert( f0= 'pa3355', f1= '(3355)Project Manager')
    db.dcard.insert( f0= 'sx3356', f1= '(3356)10')
    db.dcard.insert( f0= 'sx3357', f1= '(3357)15')
    db.dcard.insert( f0= 'sx3358', f1= '(3358)11')
    db.dcard.insert( f0= 'sx3359', f1= '(3359)03')
    db.dcard.insert( f0= 'sx3360', f1= '(3360)Success')
    db.dcard.insert( f0= 'sx3361', f1= '(3361)49')
    db.dcard.insert( f0= 'hd3363', f1= '(3363)Card Image Title')
    db.dcard.insert( f0= 'hd3365', f1= '(3365)Card Image Title')
    db.dcard.insert( f0= 'hd3367', f1= '(3367)Card Image Title')
    db.commit()
#
