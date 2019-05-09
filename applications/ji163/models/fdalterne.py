#
# table for controller: alterne
#

from gluon.contrib.populate import populate

db.define_table('dalterne', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dalterne.id ).count():
    db.dalterne.insert( f0= 'sx3221', f1= '(3221)Toggle navigation')
    db.dalterne.insert( f0= 'sx3224', f1= '(3224)5')
    db.dalterne.insert( f0= 'sx3225', f1= '(3225)4')
    db.dalterne.insert( f0= 'aa3228', f1= '(3228)Dashboard')
    db.dalterne.insert( f0= 'aa3230', f1= '(3230)Tables')
    db.dalterne.insert( f0= 'aa3232', f1= '(3232)General')
    db.dalterne.insert( f0= 'aa3234', f1= '(3234)Validation')
    db.dalterne.insert( f0= 'aa3236', f1= '(3236)WYSIWYG')
    db.dalterne.insert( f0= 'aa3238', f1= '(3238)Wizard &amp; File Upload')
    db.dalterne.insert( f0= 'pb3239', f1= '(3239)Live Search ...')
    db.dalterne.insert( f0= 'sx3241', f1= '(3241)16')
    db.dalterne.insert( f0= 'he3242', f1= '(3242)Archie')
    db.dalterne.insert( f0= 'aa3243', f1= '(3243)Administrator')
    db.dalterne.insert( f0= 'ba3244', f1= '(3244)Last Access :')
    db.dalterne.insert( f0= 'lb3245', f1= '(3245)Menu')
    db.dalterne.insert( f0= 'sx3247', f1= '(3247)&nbsp;Dashboard')
    db.dalterne.insert( f0= 'sx3248', f1= '(3248)Layouts')
    db.dalterne.insert( f0= 'sx3267', f1= '(3267)Components')
    db.dalterne.insert( f0= 'sx3279', f1= '(3279)Tables')
    db.dalterne.insert( f0= 'aa3294', f1= '(3294)Level 2')
    db.dalterne.insert( f0= 'aa3295', f1= '(3295)Level 2')
    db.dalterne.insert( f0= 'aa3296', f1= '(3296)Level 3')
    db.dalterne.insert( f0= 'aa3297', f1= '(3297)Level 3')
    db.dalterne.insert( f0= 'aa3298', f1= '(3298)Level 4')
    db.dalterne.insert( f0= 'aa3299', f1= '(3299)Level 4')
    db.dalterne.insert( f0= 'aa3300', f1= '(3300)Level 5')
    db.dalterne.insert( f0= 'aa3301', f1= '(3301)Level 5')
    db.dalterne.insert( f0= 'aa3302', f1= '(3302)Level 5')
    db.dalterne.insert( f0= 'aa3303', f1= '(3303)Level 4')
    db.dalterne.insert( f0= 'aa3304', f1= '(3304)Level 2')
    db.dalterne.insert( f0= 'aa3305', f1= '(3305)Level 1')
    db.dalterne.insert( f0= 'aa3306', f1= '(3306)Level 2')
    db.dalterne.insert( f0= 'aa3307', f1= '(3307)Level 2')
    db.dalterne.insert( f0= 'aa3308', f1= '(3308)Level 2')
    db.dalterne.insert( f0= 'sp3309', f1= '(3309)2.345')
    db.dalterne.insert( f0= 'sx3310', f1= '(3310)-16%')
    db.dalterne.insert( f0= 'sp3311', f1= '(3311)165')
    db.dalterne.insert( f0= 'sx3312', f1= '(3312)+23%')
    db.dalterne.insert( f0= 'sp3313', f1= '(3313)$2 345.00')
    db.dalterne.insert( f0= 'sx3314', f1= '(3314)0%')
    db.dalterne.insert( f0= 'sp3315', f1= '(3315)$678.00')
    db.dalterne.insert( f0= 'sx3316', f1= '(3316)-10%')
    db.dalterne.insert( f0= 'sp3317', f1= '(3317)default')
    db.dalterne.insert( f0= 'sx3318', f1= '(3318)2')
    db.dalterne.insert( f0= 'sp3319', f1= '(3319)danger')
    db.dalterne.insert( f0= 'sx3320', f1= '(3320)2')
    db.dalterne.insert( f0= 'sp3321', f1= '(3321)No Label')
    db.dalterne.insert( f0= 'sp3322', f1= '(3322)success')
    db.dalterne.insert( f0= 'sx3323', f1= '(3323)-456')
    db.dalterne.insert( f0= 'sp3324', f1= '(3324)warning')
    db.dalterne.insert( f0= 'sx3325', f1= '(3325)+25')
    db.dalterne.insert( f0= 'sp3326', f1= '(3326)')
    db.dalterne.insert( f0= 'sx3327', f1= '(3327)3.14159265')
    db.dalterne.insert( f0= 'sp3328', f1= '(3328)')
    db.dalterne.insert( f0= 'sx3329', f1= '(3329)2.71828')
    db.dalterne.insert( f0= 'sp3330', f1= '(3330)')
    db.dalterne.insert( f0= 'sx3331', f1= '(3331)1.618')
    db.dalterne.insert( f0= 'hh3332', f1= '(3332)Line Chart')
    db.dalterne.insert( f0= 'hh3340', f1= '(3340)Calendar')
    db.dalterne.insert( f0= 'bu3341', f1= '(3341)&times;')
    db.dalterne.insert( f0= 'sp3342', f1= '(3342)Warning!')
    db.dalterne.insert( f0= 'sx3343', f1= '(3343)1,4,4,7,5,9,10')
    db.dalterne.insert( f0= 'sx3344', f1= '(3344)Loading..')
    db.dalterne.insert( f0= 'sx3345', f1= '(3345)Loading..')
    db.dalterne.insert( f0= 'sx3346', f1= '(3346)1,3,4,5,3,5')
    db.dalterne.insert( f0= 'bu3347', f1= '(3347)Default')
    db.dalterne.insert( f0= 'bu3348', f1= '(3348)Primary')
    db.dalterne.insert( f0= 'bu3349', f1= '(3349)Info')
    db.dalterne.insert( f0= 'bu3350', f1= '(3350)Success')
    db.dalterne.insert( f0= 'bu3351', f1= '(3351)Danger')
    db.dalterne.insert( f0= 'bu3352', f1= '(3352)Warning')
    db.dalterne.insert( f0= 'bu3353', f1= '(3353)Inverse')
    db.dalterne.insert( f0= 'bu3354', f1= '(3354)btn-metis-1')
    db.dalterne.insert( f0= 'bu3355', f1= '(3355)btn-metis-2')
    db.dalterne.insert( f0= 'bu3356', f1= '(3356)btn-metis-3')
    db.dalterne.insert( f0= 'bu3357', f1= '(3357)btn-metis-4')
    db.dalterne.insert( f0= 'bu3358', f1= '(3358)btn-metis-5')
    db.dalterne.insert( f0= 'bu3359', f1= '(3359)btn-metis-6')
    db.dalterne.insert( f0= 'si3360', f1= '(3360)20%')
    db.dalterne.insert( f0= 'sp3361', f1= '(3361)Default')
    db.dalterne.insert( f0= 'si3362', f1= '(3362)40%')
    db.dalterne.insert( f0= 'sp3363', f1= '(3363)Success')
    db.dalterne.insert( f0= 'si3364', f1= '(3364)60%')
    db.dalterne.insert( f0= 'sp3365', f1= '(3365)warning')
    db.dalterne.insert( f0= 'si3366', f1= '(3366)80%')
    db.dalterne.insert( f0= 'sp3367', f1= '(3367)Danger')
    db.dalterne.insert( f0= 'pa3368', f1= '(3368)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dalterne.insert( f0= 'bu3369', f1= '(3369)&times;')
    db.dalterne.insert( f0= 'hd3370', f1= '(3370)Modal title')
    db.dalterne.insert( f0= 'bu3371', f1= '(3371)Close')
    db.commit()
#
