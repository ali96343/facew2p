#
# table for controller: no_left_sidebar
#

from gluon.contrib.populate import populate

db.define_table('dno0left0sidebar', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dno0left0sidebar.id ).count():
    db.dno0left0sidebar.insert( f0= 'sx3833', f1= '(3833)Toggle navigation')
    db.dno0left0sidebar.insert( f0= 'aa3838', f1= '(3838)Dashboard')
    db.dno0left0sidebar.insert( f0= 'aa3840', f1= '(3840)Tables')
    db.dno0left0sidebar.insert( f0= 'aa3842', f1= '(3842)General')
    db.dno0left0sidebar.insert( f0= 'aa3844', f1= '(3844)Validation')
    db.dno0left0sidebar.insert( f0= 'aa3846', f1= '(3846)WYSIWYG')
    db.dno0left0sidebar.insert( f0= 'pb3848', f1= '(3848)Live Search ...')
    db.dno0left0sidebar.insert( f0= 'hh3849', f1= '(3849)Code')
    db.dno0left0sidebar.insert( f0= 'bu3850', f1= '(3850)&times;')
    db.dno0left0sidebar.insert( f0= 'sp3851', f1= '(3851)Warning!')
    db.dno0left0sidebar.insert( f0= 'sx3852', f1= '(3852)1,4,4,7,5,9,10')
    db.dno0left0sidebar.insert( f0= 'sx3853', f1= '(3853)Loading..')
    db.dno0left0sidebar.insert( f0= 'sx3854', f1= '(3854)Loading..')
    db.dno0left0sidebar.insert( f0= 'sx3855', f1= '(3855)1,3,4,5,3,5')
    db.dno0left0sidebar.insert( f0= 'bu3856', f1= '(3856)Default')
    db.dno0left0sidebar.insert( f0= 'bu3857', f1= '(3857)Primary')
    db.dno0left0sidebar.insert( f0= 'bu3858', f1= '(3858)Info')
    db.dno0left0sidebar.insert( f0= 'bu3859', f1= '(3859)Success')
    db.dno0left0sidebar.insert( f0= 'bu3860', f1= '(3860)Danger')
    db.dno0left0sidebar.insert( f0= 'bu3861', f1= '(3861)Warning')
    db.dno0left0sidebar.insert( f0= 'bu3862', f1= '(3862)Inverse')
    db.dno0left0sidebar.insert( f0= 'bu3863', f1= '(3863)btn-metis-1')
    db.dno0left0sidebar.insert( f0= 'bu3864', f1= '(3864)btn-metis-2')
    db.dno0left0sidebar.insert( f0= 'bu3865', f1= '(3865)btn-metis-3')
    db.dno0left0sidebar.insert( f0= 'bu3866', f1= '(3866)btn-metis-4')
    db.dno0left0sidebar.insert( f0= 'bu3867', f1= '(3867)btn-metis-5')
    db.dno0left0sidebar.insert( f0= 'bu3868', f1= '(3868)btn-metis-6')
    db.dno0left0sidebar.insert( f0= 'si3869', f1= '(3869)20%')
    db.dno0left0sidebar.insert( f0= 'sp3870', f1= '(3870)Default')
    db.dno0left0sidebar.insert( f0= 'si3871', f1= '(3871)40%')
    db.dno0left0sidebar.insert( f0= 'sp3872', f1= '(3872)Success')
    db.dno0left0sidebar.insert( f0= 'si3873', f1= '(3873)60%')
    db.dno0left0sidebar.insert( f0= 'sp3874', f1= '(3874)warning')
    db.dno0left0sidebar.insert( f0= 'si3875', f1= '(3875)80%')
    db.dno0left0sidebar.insert( f0= 'sp3876', f1= '(3876)Danger')
    db.dno0left0sidebar.insert( f0= 'pa3877', f1= '(3877)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dno0left0sidebar.insert( f0= 'bu3878', f1= '(3878)&times;')
    db.dno0left0sidebar.insert( f0= 'hd3879', f1= '(3879)Modal title')
    db.dno0left0sidebar.insert( f0= 'bu3880', f1= '(3880)Close')
    db.commit()
#
