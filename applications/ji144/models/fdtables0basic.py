#
# table for controller: tables_basic
#

from gluon.contrib.populate import populate

db.define_table('dtables0basic', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtables0basic.id ).count():
    db.dtables0basic.insert( f0= 'hc837', f1= '(837)UI elements')
    db.dtables0basic.insert( f0= 'aa839', f1= '(839)Buttons')
    db.dtables0basic.insert( f0= 'aa841', f1= '(841)Badges')
    db.dtables0basic.insert( f0= 'aa843', f1= '(843)Tabs')
    db.dtables0basic.insert( f0= 'aa845', f1= '(845)Social Buttons')
    db.dtables0basic.insert( f0= 'aa847', f1= '(847)Cards')
    db.dtables0basic.insert( f0= 'aa849', f1= '(849)Alerts')
    db.dtables0basic.insert( f0= 'aa851', f1= '(851)Progress Bars')
    db.dtables0basic.insert( f0= 'aa853', f1= '(853)Modals')
    db.dtables0basic.insert( f0= 'aa855', f1= '(855)Switches')
    db.dtables0basic.insert( f0= 'aa857', f1= '(857)Grids')
    db.dtables0basic.insert( f0= 'aa859', f1= '(859)Typography')
    db.dtables0basic.insert( f0= 'aa861', f1= '(861)Basic Table')
    db.dtables0basic.insert( f0= 'aa863', f1= '(863)Data Table')
    db.dtables0basic.insert( f0= 'aa865', f1= '(865)Basic Form')
    db.dtables0basic.insert( f0= 'aa867', f1= '(867)Advanced Form')
    db.dtables0basic.insert( f0= 'hc868', f1= '(868)Icons')
    db.dtables0basic.insert( f0= 'aa870', f1= '(870)Font Awesome')
    db.dtables0basic.insert( f0= 'aa872', f1= '(872)Themefy Icons')
    db.dtables0basic.insert( f0= 'aa875', f1= '(875)Chart JS')
    db.dtables0basic.insert( f0= 'aa877', f1= '(877)Flot Chart')
    db.dtables0basic.insert( f0= 'aa879', f1= '(879)Peity Chart')
    db.dtables0basic.insert( f0= 'aa881', f1= '(881)Google Maps')
    db.dtables0basic.insert( f0= 'aa883', f1= '(883)Vector Maps')
    db.dtables0basic.insert( f0= 'hc884', f1= '(884)Extras')
    db.dtables0basic.insert( f0= 'aa886', f1= '(886)Login')
    db.dtables0basic.insert( f0= 'aa888', f1= '(888)Register')
    db.dtables0basic.insert( f0= 'aa890', f1= '(890)Forget Pass')
    db.dtables0basic.insert( f0= 'pb891', f1= '(891)Search ...')
    db.dtables0basic.insert( f0= 'pc892', f1= '(892)You have 3 Notification')
    db.dtables0basic.insert( f0= 'pc893', f1= '(893)You have 4 Mails')
    db.dtables0basic.insert( f0= 'sx895', f1= '(895)Jonathan Smith')
    db.dtables0basic.insert( f0= 'sx896', f1= '(896)Just now')
    db.dtables0basic.insert( f0= 'pa897', f1= '(897)Hello, this is an example msg')
    db.dtables0basic.insert( f0= 'sx899', f1= '(899)Jack Sanders')
    db.dtables0basic.insert( f0= 'sx900', f1= '(900)5 minutes ago')
    db.dtables0basic.insert( f0= 'pa901', f1= '(901)Lorem ipsum dolor sit amet, consectetur')
    db.dtables0basic.insert( f0= 'sx903', f1= '(903)Cheryl Wheeler')
    db.dtables0basic.insert( f0= 'sx904', f1= '(904)10 minutes ago')
    db.dtables0basic.insert( f0= 'pa905', f1= '(905)Hello, this is an example msg')
    db.dtables0basic.insert( f0= 'sx907', f1= '(907)Rachel Santos')
    db.dtables0basic.insert( f0= 'sx908', f1= '(908)15 minutes ago')
    db.dtables0basic.insert( f0= 'pa909', f1= '(909)Lorem ipsum dolor sit amet, consectetur')
    db.dtables0basic.insert( f0= 'sx911', f1= '(911)13')
    db.dtables0basic.insert( f0= 'hh912', f1= '(912)Dashboard')
    db.dtables0basic.insert( f0= 'aa913', f1= '(913)Dashboard')
    db.dtables0basic.insert( f0= 'aa914', f1= '(914)Table')
    db.dtables0basic.insert( f0= 'lb915', f1= '(915)Basic table')
    db.commit()
#
