#
# table for controller: no_left_sidebar_main_search
#

from gluon.contrib.populate import populate

db.define_table('dno0left0sidebar0main0search', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dno0left0sidebar0main0search.id ).count():
    db.dno0left0sidebar0main0search.insert( f0= 'sx3277', f1= '(3277)Toggle navigation')
    db.dno0left0sidebar0main0search.insert( f0= 'aa3282', f1= '(3282)Dashboard')
    db.dno0left0sidebar0main0search.insert( f0= 'aa3284', f1= '(3284)Tables')
    db.dno0left0sidebar0main0search.insert( f0= 'aa3286', f1= '(3286)General')
    db.dno0left0sidebar0main0search.insert( f0= 'aa3288', f1= '(3288)Validation')
    db.dno0left0sidebar0main0search.insert( f0= 'aa3290', f1= '(3290)WYSIWYG')
    db.dno0left0sidebar0main0search.insert( f0= 'hh3292', f1= '(3292)Code')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3293', f1= '(3293)&times;')
    db.dno0left0sidebar0main0search.insert( f0= 'sp3294', f1= '(3294)Warning!')
    db.dno0left0sidebar0main0search.insert( f0= 'sx3295', f1= '(3295)1,4,4,7,5,9,10')
    db.dno0left0sidebar0main0search.insert( f0= 'sx3296', f1= '(3296)Loading..')
    db.dno0left0sidebar0main0search.insert( f0= 'sx3297', f1= '(3297)Loading..')
    db.dno0left0sidebar0main0search.insert( f0= 'sx3298', f1= '(3298)1,3,4,5,3,5')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3299', f1= '(3299)Default')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3300', f1= '(3300)Primary')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3301', f1= '(3301)Info')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3302', f1= '(3302)Success')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3303', f1= '(3303)Danger')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3304', f1= '(3304)Warning')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3305', f1= '(3305)Inverse')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3306', f1= '(3306)btn-metis-1')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3307', f1= '(3307)btn-metis-2')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3308', f1= '(3308)btn-metis-3')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3309', f1= '(3309)btn-metis-4')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3310', f1= '(3310)btn-metis-5')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3311', f1= '(3311)btn-metis-6')
    db.dno0left0sidebar0main0search.insert( f0= 'si3312', f1= '(3312)20%')
    db.dno0left0sidebar0main0search.insert( f0= 'sp3313', f1= '(3313)Default')
    db.dno0left0sidebar0main0search.insert( f0= 'si3314', f1= '(3314)40%')
    db.dno0left0sidebar0main0search.insert( f0= 'sp3315', f1= '(3315)Success')
    db.dno0left0sidebar0main0search.insert( f0= 'si3316', f1= '(3316)60%')
    db.dno0left0sidebar0main0search.insert( f0= 'sp3317', f1= '(3317)warning')
    db.dno0left0sidebar0main0search.insert( f0= 'si3318', f1= '(3318)80%')
    db.dno0left0sidebar0main0search.insert( f0= 'sp3319', f1= '(3319)Danger')
    db.dno0left0sidebar0main0search.insert( f0= 'pa3320', f1= '(3320)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3321', f1= '(3321)&times;')
    db.dno0left0sidebar0main0search.insert( f0= 'hd3322', f1= '(3322)Modal title')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3323', f1= '(3323)Close')
    db.commit()
#
