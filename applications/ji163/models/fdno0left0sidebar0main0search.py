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
    db.dno0left0sidebar0main0search.insert( f0= 'sx3396', f1= '(3396)Toggle navigation')
    db.dno0left0sidebar0main0search.insert( f0= 'sx3399', f1= '(3399)5')
    db.dno0left0sidebar0main0search.insert( f0= 'sx3400', f1= '(3400)4')
    db.dno0left0sidebar0main0search.insert( f0= 'aa3403', f1= '(3403)Dashboard')
    db.dno0left0sidebar0main0search.insert( f0= 'aa3405', f1= '(3405)Tables')
    db.dno0left0sidebar0main0search.insert( f0= 'aa3407', f1= '(3407)General')
    db.dno0left0sidebar0main0search.insert( f0= 'aa3409', f1= '(3409)Validation')
    db.dno0left0sidebar0main0search.insert( f0= 'aa3411', f1= '(3411)WYSIWYG')
    db.dno0left0sidebar0main0search.insert( f0= 'aa3413', f1= '(3413)Wizard &amp; File Upload')
    db.dno0left0sidebar0main0search.insert( f0= 'hh3414', f1= '(3414)Code')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3415', f1= '(3415)&times;')
    db.dno0left0sidebar0main0search.insert( f0= 'sp3416', f1= '(3416)Warning!')
    db.dno0left0sidebar0main0search.insert( f0= 'sx3417', f1= '(3417)1,4,4,7,5,9,10')
    db.dno0left0sidebar0main0search.insert( f0= 'sx3418', f1= '(3418)Loading..')
    db.dno0left0sidebar0main0search.insert( f0= 'sx3419', f1= '(3419)Loading..')
    db.dno0left0sidebar0main0search.insert( f0= 'sx3420', f1= '(3420)1,3,4,5,3,5')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3421', f1= '(3421)Default')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3422', f1= '(3422)Primary')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3423', f1= '(3423)Info')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3424', f1= '(3424)Success')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3425', f1= '(3425)Danger')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3426', f1= '(3426)Warning')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3427', f1= '(3427)Inverse')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3428', f1= '(3428)btn-metis-1')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3429', f1= '(3429)btn-metis-2')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3430', f1= '(3430)btn-metis-3')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3431', f1= '(3431)btn-metis-4')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3432', f1= '(3432)btn-metis-5')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3433', f1= '(3433)btn-metis-6')
    db.dno0left0sidebar0main0search.insert( f0= 'si3434', f1= '(3434)20%')
    db.dno0left0sidebar0main0search.insert( f0= 'sp3435', f1= '(3435)Default')
    db.dno0left0sidebar0main0search.insert( f0= 'si3436', f1= '(3436)40%')
    db.dno0left0sidebar0main0search.insert( f0= 'sp3437', f1= '(3437)Success')
    db.dno0left0sidebar0main0search.insert( f0= 'si3438', f1= '(3438)60%')
    db.dno0left0sidebar0main0search.insert( f0= 'sp3439', f1= '(3439)warning')
    db.dno0left0sidebar0main0search.insert( f0= 'si3440', f1= '(3440)80%')
    db.dno0left0sidebar0main0search.insert( f0= 'sp3441', f1= '(3441)Danger')
    db.dno0left0sidebar0main0search.insert( f0= 'pa3442', f1= '(3442)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3443', f1= '(3443)&times;')
    db.dno0left0sidebar0main0search.insert( f0= 'hd3444', f1= '(3444)Modal title')
    db.dno0left0sidebar0main0search.insert( f0= 'bu3445', f1= '(3445)Close')
    db.commit()
#
