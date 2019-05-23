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
    db.dno0left0right0sidebar.insert( f0= 'sx4070', f1= '(4070)Toggle navigation')
    db.dno0left0right0sidebar.insert( f0= 'aa4075', f1= '(4075)Dashboard')
    db.dno0left0right0sidebar.insert( f0= 'aa4077', f1= '(4077)Tables')
    db.dno0left0right0sidebar.insert( f0= 'aa4079', f1= '(4079)General')
    db.dno0left0right0sidebar.insert( f0= 'aa4081', f1= '(4081)Validation')
    db.dno0left0right0sidebar.insert( f0= 'aa4083', f1= '(4083)WYSIWYG')
    db.dno0left0right0sidebar.insert( f0= 'pb4085', f1= '(4085)Live Search ...')
    db.dno0left0right0sidebar.insert( f0= 'hh4086', f1= '(4086)Code')
    db.dno0left0right0sidebar.insert( f0= 'pa4087', f1= '(4087)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dno0left0right0sidebar.insert( f0= 'bu4088', f1= '(4088)&times;')
    db.dno0left0right0sidebar.insert( f0= 'hd4089', f1= '(4089)Modal title')
    db.dno0left0right0sidebar.insert( f0= 'bu4090', f1= '(4090)Close')
    db.commit()
#
