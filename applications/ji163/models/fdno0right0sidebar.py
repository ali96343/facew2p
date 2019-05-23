#
# table for controller: no_right_sidebar
#

from gluon.contrib.populate import populate

db.define_table('dno0right0sidebar', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dno0right0sidebar.id ).count():
    db.dno0right0sidebar.insert( f0= 'sx2626', f1= '(2626)Toggle navigation')
    db.dno0right0sidebar.insert( f0= 'aa2631', f1= '(2631)Dashboard')
    db.dno0right0sidebar.insert( f0= 'aa2633', f1= '(2633)Tables')
    db.dno0right0sidebar.insert( f0= 'aa2635', f1= '(2635)General')
    db.dno0right0sidebar.insert( f0= 'aa2637', f1= '(2637)Validation')
    db.dno0right0sidebar.insert( f0= 'aa2639', f1= '(2639)WYSIWYG')
    db.dno0right0sidebar.insert( f0= 'pb2641', f1= '(2641)Live Search ...')
    db.dno0right0sidebar.insert( f0= 'he2643', f1= '(2643)Archie')
    db.dno0right0sidebar.insert( f0= 'aa2644', f1= '(2644)Administrator')
    db.dno0right0sidebar.insert( f0= 'ba2645', f1= '(2645)Last Access :')
    db.dno0right0sidebar.insert( f0= 'lb2646', f1= '(2646)Menu')
    db.dno0right0sidebar.insert( f0= 'sx2648', f1= '(2648)Layouts')
    db.dno0right0sidebar.insert( f0= 'sx2667', f1= '(2667)Components')
    db.dno0right0sidebar.insert( f0= 'sx2679', f1= '(2679)Tables')
    db.dno0right0sidebar.insert( f0= 'aa2694', f1= '(2694)Level 2')
    db.dno0right0sidebar.insert( f0= 'aa2695', f1= '(2695)Level 2')
    db.dno0right0sidebar.insert( f0= 'aa2696', f1= '(2696)Level 3')
    db.dno0right0sidebar.insert( f0= 'aa2697', f1= '(2697)Level 3')
    db.dno0right0sidebar.insert( f0= 'aa2698', f1= '(2698)Level 4')
    db.dno0right0sidebar.insert( f0= 'aa2699', f1= '(2699)Level 4')
    db.dno0right0sidebar.insert( f0= 'aa2700', f1= '(2700)Level 5')
    db.dno0right0sidebar.insert( f0= 'aa2701', f1= '(2701)Level 5')
    db.dno0right0sidebar.insert( f0= 'aa2702', f1= '(2702)Level 5')
    db.dno0right0sidebar.insert( f0= 'aa2703', f1= '(2703)Level 4')
    db.dno0right0sidebar.insert( f0= 'aa2704', f1= '(2704)Level 2')
    db.dno0right0sidebar.insert( f0= 'aa2705', f1= '(2705)Level 1')
    db.dno0right0sidebar.insert( f0= 'aa2706', f1= '(2706)Level 2')
    db.dno0right0sidebar.insert( f0= 'aa2707', f1= '(2707)Level 2')
    db.dno0right0sidebar.insert( f0= 'aa2708', f1= '(2708)Level 2')
    db.dno0right0sidebar.insert( f0= 'hh2709', f1= '(2709)Code')
    db.dno0right0sidebar.insert( f0= 'pa2710', f1= '(2710)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dno0right0sidebar.insert( f0= 'bu2711', f1= '(2711)&times;')
    db.dno0right0sidebar.insert( f0= 'hd2712', f1= '(2712)Modal title')
    db.dno0right0sidebar.insert( f0= 'bu2713', f1= '(2713)Close')
    db.commit()
#
