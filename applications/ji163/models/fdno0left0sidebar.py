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
    db.dno0left0sidebar.insert( f0= 'sx3973', f1= '(3973)Toggle navigation')
    db.dno0left0sidebar.insert( f0= 'sx3976', f1= '(3976)5')
    db.dno0left0sidebar.insert( f0= 'sx3977', f1= '(3977)4')
    db.dno0left0sidebar.insert( f0= 'aa3980', f1= '(3980)Dashboard')
    db.dno0left0sidebar.insert( f0= 'aa3982', f1= '(3982)Tables')
    db.dno0left0sidebar.insert( f0= 'aa3984', f1= '(3984)General')
    db.dno0left0sidebar.insert( f0= 'aa3986', f1= '(3986)Validation')
    db.dno0left0sidebar.insert( f0= 'aa3988', f1= '(3988)WYSIWYG')
    db.dno0left0sidebar.insert( f0= 'aa3990', f1= '(3990)Wizard &amp; File Upload')
    db.dno0left0sidebar.insert( f0= 'pb3991', f1= '(3991)Live Search ...')
    db.dno0left0sidebar.insert( f0= 'hh3992', f1= '(3992)Code')
    db.dno0left0sidebar.insert( f0= 'bu3993', f1= '(3993)&times;')
    db.dno0left0sidebar.insert( f0= 'sp3994', f1= '(3994)Warning!')
    db.dno0left0sidebar.insert( f0= 'sx3995', f1= '(3995)1,4,4,7,5,9,10')
    db.dno0left0sidebar.insert( f0= 'sx3996', f1= '(3996)Loading..')
    db.dno0left0sidebar.insert( f0= 'sx3997', f1= '(3997)Loading..')
    db.dno0left0sidebar.insert( f0= 'sx3998', f1= '(3998)1,3,4,5,3,5')
    db.dno0left0sidebar.insert( f0= 'bu3999', f1= '(3999)Default')
    db.dno0left0sidebar.insert( f0= 'bu4000', f1= '(4000)Primary')
    db.dno0left0sidebar.insert( f0= 'bu4001', f1= '(4001)Info')
    db.dno0left0sidebar.insert( f0= 'bu4002', f1= '(4002)Success')
    db.dno0left0sidebar.insert( f0= 'bu4003', f1= '(4003)Danger')
    db.dno0left0sidebar.insert( f0= 'bu4004', f1= '(4004)Warning')
    db.dno0left0sidebar.insert( f0= 'bu4005', f1= '(4005)Inverse')
    db.dno0left0sidebar.insert( f0= 'bu4006', f1= '(4006)btn-metis-1')
    db.dno0left0sidebar.insert( f0= 'bu4007', f1= '(4007)btn-metis-2')
    db.dno0left0sidebar.insert( f0= 'bu4008', f1= '(4008)btn-metis-3')
    db.dno0left0sidebar.insert( f0= 'bu4009', f1= '(4009)btn-metis-4')
    db.dno0left0sidebar.insert( f0= 'bu4010', f1= '(4010)btn-metis-5')
    db.dno0left0sidebar.insert( f0= 'bu4011', f1= '(4011)btn-metis-6')
    db.dno0left0sidebar.insert( f0= 'si4012', f1= '(4012)20%')
    db.dno0left0sidebar.insert( f0= 'sp4013', f1= '(4013)Default')
    db.dno0left0sidebar.insert( f0= 'si4014', f1= '(4014)40%')
    db.dno0left0sidebar.insert( f0= 'sp4015', f1= '(4015)Success')
    db.dno0left0sidebar.insert( f0= 'si4016', f1= '(4016)60%')
    db.dno0left0sidebar.insert( f0= 'sp4017', f1= '(4017)warning')
    db.dno0left0sidebar.insert( f0= 'si4018', f1= '(4018)80%')
    db.dno0left0sidebar.insert( f0= 'sp4019', f1= '(4019)Danger')
    db.dno0left0sidebar.insert( f0= 'pa4020', f1= '(4020)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dno0left0sidebar.insert( f0= 'bu4021', f1= '(4021)&times;')
    db.dno0left0sidebar.insert( f0= 'hd4022', f1= '(4022)Modal title')
    db.dno0left0sidebar.insert( f0= 'bu4023', f1= '(4023)Close')
    db.commit()
#
