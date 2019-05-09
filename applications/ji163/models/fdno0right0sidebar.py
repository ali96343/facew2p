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
    db.dno0right0sidebar.insert( f0= 'sx2721', f1= '(2721)Toggle navigation')
    db.dno0right0sidebar.insert( f0= 'sx2724', f1= '(2724)5')
    db.dno0right0sidebar.insert( f0= 'sx2725', f1= '(2725)4')
    db.dno0right0sidebar.insert( f0= 'aa2728', f1= '(2728)Dashboard')
    db.dno0right0sidebar.insert( f0= 'aa2730', f1= '(2730)Tables')
    db.dno0right0sidebar.insert( f0= 'aa2732', f1= '(2732)General')
    db.dno0right0sidebar.insert( f0= 'aa2734', f1= '(2734)Validation')
    db.dno0right0sidebar.insert( f0= 'aa2736', f1= '(2736)WYSIWYG')
    db.dno0right0sidebar.insert( f0= 'aa2738', f1= '(2738)Wizard &amp; File Upload')
    db.dno0right0sidebar.insert( f0= 'pb2739', f1= '(2739)Live Search ...')
    db.dno0right0sidebar.insert( f0= 'sx2741', f1= '(2741)16')
    db.dno0right0sidebar.insert( f0= 'he2742', f1= '(2742)Archie')
    db.dno0right0sidebar.insert( f0= 'aa2743', f1= '(2743)Administrator')
    db.dno0right0sidebar.insert( f0= 'ba2744', f1= '(2744)Last Access :')
    db.dno0right0sidebar.insert( f0= 'lb2745', f1= '(2745)Menu')
    db.dno0right0sidebar.insert( f0= 'sx2747', f1= '(2747)&nbsp;Dashboard')
    db.dno0right0sidebar.insert( f0= 'sx2748', f1= '(2748)Layouts')
    db.dno0right0sidebar.insert( f0= 'sx2767', f1= '(2767)Components')
    db.dno0right0sidebar.insert( f0= 'sx2779', f1= '(2779)Tables')
    db.dno0right0sidebar.insert( f0= 'aa2794', f1= '(2794)Level 2')
    db.dno0right0sidebar.insert( f0= 'aa2795', f1= '(2795)Level 2')
    db.dno0right0sidebar.insert( f0= 'aa2796', f1= '(2796)Level 3')
    db.dno0right0sidebar.insert( f0= 'aa2797', f1= '(2797)Level 3')
    db.dno0right0sidebar.insert( f0= 'aa2798', f1= '(2798)Level 4')
    db.dno0right0sidebar.insert( f0= 'aa2799', f1= '(2799)Level 4')
    db.dno0right0sidebar.insert( f0= 'aa2800', f1= '(2800)Level 5')
    db.dno0right0sidebar.insert( f0= 'aa2801', f1= '(2801)Level 5')
    db.dno0right0sidebar.insert( f0= 'aa2802', f1= '(2802)Level 5')
    db.dno0right0sidebar.insert( f0= 'aa2803', f1= '(2803)Level 4')
    db.dno0right0sidebar.insert( f0= 'aa2804', f1= '(2804)Level 2')
    db.dno0right0sidebar.insert( f0= 'aa2805', f1= '(2805)Level 1')
    db.dno0right0sidebar.insert( f0= 'aa2806', f1= '(2806)Level 2')
    db.dno0right0sidebar.insert( f0= 'aa2807', f1= '(2807)Level 2')
    db.dno0right0sidebar.insert( f0= 'aa2808', f1= '(2808)Level 2')
    db.dno0right0sidebar.insert( f0= 'hh2809', f1= '(2809)Code')
    db.dno0right0sidebar.insert( f0= 'pa2810', f1= '(2810)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dno0right0sidebar.insert( f0= 'bu2811', f1= '(2811)&times;')
    db.dno0right0sidebar.insert( f0= 'hd2812', f1= '(2812)Modal title')
    db.dno0right0sidebar.insert( f0= 'bu2813', f1= '(2813)Close')
    db.commit()
#
