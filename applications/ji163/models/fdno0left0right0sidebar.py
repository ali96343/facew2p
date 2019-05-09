#
# table for controller: no_left_right_sidebar
#

from gluon.contrib.populate import populate

db.define_table('dno0left0right0sidebar', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dno0left0right0sidebar.id ).count():
    db.dno0left0right0sidebar.insert( f0= 'sx4218', f1= '(4218)Toggle navigation')
    db.dno0left0right0sidebar.insert( f0= 'sx4221', f1= '(4221)5')
    db.dno0left0right0sidebar.insert( f0= 'sx4222', f1= '(4222)4')
    db.dno0left0right0sidebar.insert( f0= 'aa4225', f1= '(4225)Dashboard')
    db.dno0left0right0sidebar.insert( f0= 'aa4227', f1= '(4227)Tables')
    db.dno0left0right0sidebar.insert( f0= 'aa4229', f1= '(4229)General')
    db.dno0left0right0sidebar.insert( f0= 'aa4231', f1= '(4231)Validation')
    db.dno0left0right0sidebar.insert( f0= 'aa4233', f1= '(4233)WYSIWYG')
    db.dno0left0right0sidebar.insert( f0= 'aa4235', f1= '(4235)Wizard &amp; File Upload')
    db.dno0left0right0sidebar.insert( f0= 'pb4236', f1= '(4236)Live Search ...')
    db.dno0left0right0sidebar.insert( f0= 'hh4237', f1= '(4237)Code')
    db.dno0left0right0sidebar.insert( f0= 'pa4238', f1= '(4238)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dno0left0right0sidebar.insert( f0= 'bu4239', f1= '(4239)&times;')
    db.dno0left0right0sidebar.insert( f0= 'hd4240', f1= '(4240)Modal title')
    db.dno0left0right0sidebar.insert( f0= 'bu4241', f1= '(4241)Close')
    db.commit()
#
