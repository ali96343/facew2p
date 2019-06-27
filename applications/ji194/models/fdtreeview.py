#
# table for controller: treeview
#

from gluon.contrib.populate import populate

db.define_table('dtreeview', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtreeview.id ).count():
    db.dtreeview.insert( f0= 'sx955', f1= '(955)Toggle sidebar')
    db.dtreeview.insert( f0= 'sx957', f1= '(957)Software Update')
    db.dtreeview.insert( f0= 'sx958', f1= '(958)65%')
    db.dtreeview.insert( f0= 'sx959', f1= '(959)Hardware Upgrade')
    db.dtreeview.insert( f0= 'sx960', f1= '(960)35%')
    db.dtreeview.insert( f0= 'sx961', f1= '(961)Unit Testing')
    db.dtreeview.insert( f0= 'sx962', f1= '(962)15%')
    db.dtreeview.insert( f0= 'sx963', f1= '(963)Bug Fixes')
    db.dtreeview.insert( f0= 'sx964', f1= '(964)90%')
    db.dtreeview.insert( f0= 'sx965', f1= '(965)+12')
    db.dtreeview.insert( f0= 'sx966', f1= '(966)+8')
    db.dtreeview.insert( f0= 'sx967', f1= '(967)+11')
    db.dtreeview.insert( f0= 'sx969', f1= '(969)Alex:')
    db.dtreeview.insert( f0= 'sp970', f1= '(970)a moment ago')
    db.dtreeview.insert( f0= 'sx972', f1= '(972)Susan:')
    db.dtreeview.insert( f0= 'sp973', f1= '(973)20 minutes ago')
    db.dtreeview.insert( f0= 'sx975', f1= '(975)Bob:')
    db.dtreeview.insert( f0= 'sp976', f1= '(976)3:15 pm')
    db.dtreeview.insert( f0= 'sx978', f1= '(978)Kate:')
    db.dtreeview.insert( f0= 'sp979', f1= '(979)1:33 pm')
    db.dtreeview.insert( f0= 'sx981', f1= '(981)Fred:')
    db.dtreeview.insert( f0= 'sp982', f1= '(982)10:09 am')
    db.dtreeview.insert( f0= 'ic985', f1= '(985)Welcome,')
    db.dtreeview.insert( f0= 'sx988', f1= '(988)Dashboard')
    db.dtreeview.insert( f0= 'sx1002', f1= '(1002)Tables')
    db.dtreeview.insert( f0= 'sx1005', f1= '(1005)Forms')
    db.dtreeview.insert( f0= 'sx1012', f1= '(1012)Widgets')
    db.dtreeview.insert( f0= 'sx1015', f1= '(1015)Gallery')
    db.dtreeview.insert( f0= 'sx1016', f1= '(1016)More Pages')
    db.dtreeview.insert( f0= 'aa1030', f1= '(1030)Home')
    db.dtreeview.insert( f0= 'lb1031', f1= '(1031)Treeview')
    db.dtreeview.insert( f0= 'pb1032', f1= '(1032)Search ...')
    db.dtreeview.insert( f0= 'bb1033', f1= '(1033).container')
    db.dtreeview.insert( f0= 'hd1034', f1= '(1034)Choose Categories')
    db.dtreeview.insert( f0= 'sx1035', f1= '(1035)(with selectable folders)')
    db.dtreeview.insert( f0= 'sx1036', f1= '(1036)Ace')
    db.commit()
#
