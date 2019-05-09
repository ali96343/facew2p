#
# table for controller: no_header_sidebar
#

from gluon.contrib.populate import populate

db.define_table('dno0header0sidebar', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dno0header0sidebar.id ).count():
    db.dno0header0sidebar.insert( f0= 'sx2401', f1= '(2401)Toggle navigation')
    db.dno0header0sidebar.insert( f0= 'sx2404', f1= '(2404)5')
    db.dno0header0sidebar.insert( f0= 'sx2405', f1= '(2405)4')
    db.dno0header0sidebar.insert( f0= 'aa2408', f1= '(2408)Dashboard')
    db.dno0header0sidebar.insert( f0= 'aa2410', f1= '(2410)Tables')
    db.dno0header0sidebar.insert( f0= 'aa2412', f1= '(2412)General')
    db.dno0header0sidebar.insert( f0= 'aa2414', f1= '(2414)Validation')
    db.dno0header0sidebar.insert( f0= 'aa2416', f1= '(2416)WYSIWYG')
    db.dno0header0sidebar.insert( f0= 'aa2418', f1= '(2418)Wizard &amp; File Upload')
    db.dno0header0sidebar.insert( f0= 'hh2419', f1= '(2419)Code')
    db.dno0header0sidebar.insert( f0= 'pa2420', f1= '(2420)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dno0header0sidebar.insert( f0= 'bu2421', f1= '(2421)&times;')
    db.dno0header0sidebar.insert( f0= 'hd2422', f1= '(2422)Modal title')
    db.dno0header0sidebar.insert( f0= 'bu2423', f1= '(2423)Close')
    db.commit()
#
