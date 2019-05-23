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
    db.dno0header0sidebar.insert( f0= 'sx2320', f1= '(2320)Toggle navigation')
    db.dno0header0sidebar.insert( f0= 'aa2325', f1= '(2325)Dashboard')
    db.dno0header0sidebar.insert( f0= 'aa2327', f1= '(2327)Tables')
    db.dno0header0sidebar.insert( f0= 'aa2329', f1= '(2329)General')
    db.dno0header0sidebar.insert( f0= 'aa2331', f1= '(2331)Validation')
    db.dno0header0sidebar.insert( f0= 'aa2333', f1= '(2333)WYSIWYG')
    db.dno0header0sidebar.insert( f0= 'hh2335', f1= '(2335)Code')
    db.dno0header0sidebar.insert( f0= 'pa2336', f1= '(2336)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dno0header0sidebar.insert( f0= 'bu2337', f1= '(2337)&times;')
    db.dno0header0sidebar.insert( f0= 'hd2338', f1= '(2338)Modal title')
    db.dno0header0sidebar.insert( f0= 'bu2339', f1= '(2339)Close')
    db.commit()
#
