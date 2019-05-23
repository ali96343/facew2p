#
# table for controller: tables_data
#

from gluon.contrib.populate import populate

db.define_table('dtables0data', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtables0data.id ).count():
    db.dtables0data.insert( f0= 'hc422', f1= '(422)UI elements')
    db.dtables0data.insert( f0= 'aa424', f1= '(424)Buttons')
    db.dtables0data.insert( f0= 'aa426', f1= '(426)Badges')
    db.dtables0data.insert( f0= 'aa428', f1= '(428)Tabs')
    db.dtables0data.insert( f0= 'aa430', f1= '(430)Social Buttons')
    db.dtables0data.insert( f0= 'aa432', f1= '(432)Cards')
    db.dtables0data.insert( f0= 'aa434', f1= '(434)Alerts')
    db.dtables0data.insert( f0= 'aa436', f1= '(436)Progress Bars')
    db.dtables0data.insert( f0= 'aa438', f1= '(438)Modals')
    db.dtables0data.insert( f0= 'aa440', f1= '(440)Switches')
    db.dtables0data.insert( f0= 'aa442', f1= '(442)Grids')
    db.dtables0data.insert( f0= 'aa444', f1= '(444)Typography')
    db.dtables0data.insert( f0= 'aa446', f1= '(446)Basic Table')
    db.dtables0data.insert( f0= 'aa448', f1= '(448)Data Table')
    db.dtables0data.insert( f0= 'aa450', f1= '(450)Basic Form')
    db.dtables0data.insert( f0= 'aa452', f1= '(452)Advanced Form')
    db.dtables0data.insert( f0= 'hc453', f1= '(453)Icons')
    db.dtables0data.insert( f0= 'aa455', f1= '(455)Font Awesome')
    db.dtables0data.insert( f0= 'aa457', f1= '(457)Themefy Icons')
    db.dtables0data.insert( f0= 'aa460', f1= '(460)Chart JS')
    db.dtables0data.insert( f0= 'aa462', f1= '(462)Flot Chart')
    db.dtables0data.insert( f0= 'aa464', f1= '(464)Peity Chart')
    db.dtables0data.insert( f0= 'aa466', f1= '(466)Google Maps')
    db.dtables0data.insert( f0= 'aa468', f1= '(468)Vector Maps')
    db.dtables0data.insert( f0= 'hc469', f1= '(469)Extras')
    db.dtables0data.insert( f0= 'aa471', f1= '(471)Login')
    db.dtables0data.insert( f0= 'aa473', f1= '(473)Register')
    db.dtables0data.insert( f0= 'aa475', f1= '(475)Forget Pass')
    db.dtables0data.insert( f0= 'pb476', f1= '(476)Search ...')
    db.dtables0data.insert( f0= 'pc477', f1= '(477)You have 3 Notification')
    db.dtables0data.insert( f0= 'pc478', f1= '(478)You have 4 Mails')
    db.dtables0data.insert( f0= 'sx480', f1= '(480)Jonathan Smith')
    db.dtables0data.insert( f0= 'sx481', f1= '(481)Just now')
    db.dtables0data.insert( f0= 'pa482', f1= '(482)Hello, this is an example msg')
    db.dtables0data.insert( f0= 'sx484', f1= '(484)Jack Sanders')
    db.dtables0data.insert( f0= 'sx485', f1= '(485)5 minutes ago')
    db.dtables0data.insert( f0= 'pa486', f1= '(486)Lorem ipsum dolor sit amet, consectetur')
    db.dtables0data.insert( f0= 'sx488', f1= '(488)Cheryl Wheeler')
    db.dtables0data.insert( f0= 'sx489', f1= '(489)10 minutes ago')
    db.dtables0data.insert( f0= 'pa490', f1= '(490)Hello, this is an example msg')
    db.dtables0data.insert( f0= 'sx492', f1= '(492)Rachel Santos')
    db.dtables0data.insert( f0= 'sx493', f1= '(493)15 minutes ago')
    db.dtables0data.insert( f0= 'pa494', f1= '(494)Lorem ipsum dolor sit amet, consectetur')
    db.dtables0data.insert( f0= 'sx496', f1= '(496)13')
    db.dtables0data.insert( f0= 'hh497', f1= '(497)Dashboard')
    db.dtables0data.insert( f0= 'aa498', f1= '(498)Dashboard')
    db.dtables0data.insert( f0= 'aa499', f1= '(499)Table')
    db.dtables0data.insert( f0= 'lb500', f1= '(500)Data table')
    db.commit()
#
