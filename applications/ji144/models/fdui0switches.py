#
# table for controller: ui_switches
#

from gluon.contrib.populate import populate

db.define_table('dui0switches', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dui0switches.id ).count():
    db.dui0switches.insert( f0= 'hc171', f1= '(171)UI elements')
    db.dui0switches.insert( f0= 'aa173', f1= '(173)Buttons')
    db.dui0switches.insert( f0= 'aa175', f1= '(175)Badges')
    db.dui0switches.insert( f0= 'aa177', f1= '(177)Tabs')
    db.dui0switches.insert( f0= 'aa179', f1= '(179)Social Buttons')
    db.dui0switches.insert( f0= 'aa181', f1= '(181)Cards')
    db.dui0switches.insert( f0= 'aa183', f1= '(183)Alerts')
    db.dui0switches.insert( f0= 'aa185', f1= '(185)Progress Bars')
    db.dui0switches.insert( f0= 'aa187', f1= '(187)Modals')
    db.dui0switches.insert( f0= 'aa189', f1= '(189)Switches')
    db.dui0switches.insert( f0= 'aa191', f1= '(191)Grids')
    db.dui0switches.insert( f0= 'aa193', f1= '(193)Typography')
    db.dui0switches.insert( f0= 'aa195', f1= '(195)Basic Table')
    db.dui0switches.insert( f0= 'aa197', f1= '(197)Data Table')
    db.dui0switches.insert( f0= 'aa199', f1= '(199)Basic Form')
    db.dui0switches.insert( f0= 'aa201', f1= '(201)Advanced Form')
    db.dui0switches.insert( f0= 'hc202', f1= '(202)Icons')
    db.dui0switches.insert( f0= 'aa204', f1= '(204)Font Awesome')
    db.dui0switches.insert( f0= 'aa206', f1= '(206)Themefy Icons')
    db.dui0switches.insert( f0= 'aa209', f1= '(209)Chart JS')
    db.dui0switches.insert( f0= 'aa211', f1= '(211)Flot Chart')
    db.dui0switches.insert( f0= 'aa213', f1= '(213)Peity Chart')
    db.dui0switches.insert( f0= 'aa215', f1= '(215)Google Maps')
    db.dui0switches.insert( f0= 'aa217', f1= '(217)Vector Maps')
    db.dui0switches.insert( f0= 'hc218', f1= '(218)Extras')
    db.dui0switches.insert( f0= 'aa220', f1= '(220)Login')
    db.dui0switches.insert( f0= 'aa222', f1= '(222)Register')
    db.dui0switches.insert( f0= 'aa224', f1= '(224)Forget Pass')
    db.dui0switches.insert( f0= 'pb225', f1= '(225)Search ...')
    db.dui0switches.insert( f0= 'pc226', f1= '(226)You have 3 Notification')
    db.dui0switches.insert( f0= 'pc227', f1= '(227)You have 4 Mails')
    db.dui0switches.insert( f0= 'sx229', f1= '(229)Jonathan Smith')
    db.dui0switches.insert( f0= 'sx230', f1= '(230)Just now')
    db.dui0switches.insert( f0= 'pa231', f1= '(231)Hello, this is an example msg')
    db.dui0switches.insert( f0= 'sx233', f1= '(233)Jack Sanders')
    db.dui0switches.insert( f0= 'sx234', f1= '(234)5 minutes ago')
    db.dui0switches.insert( f0= 'pa235', f1= '(235)Lorem ipsum dolor sit amet, consectetur')
    db.dui0switches.insert( f0= 'sx237', f1= '(237)Cheryl Wheeler')
    db.dui0switches.insert( f0= 'sx238', f1= '(238)10 minutes ago')
    db.dui0switches.insert( f0= 'pa239', f1= '(239)Hello, this is an example msg')
    db.dui0switches.insert( f0= 'sx241', f1= '(241)Rachel Santos')
    db.dui0switches.insert( f0= 'sx242', f1= '(242)15 minutes ago')
    db.dui0switches.insert( f0= 'pa243', f1= '(243)Lorem ipsum dolor sit amet, consectetur')
    db.dui0switches.insert( f0= 'sx245', f1= '(245)13')
    db.dui0switches.insert( f0= 'hh246', f1= '(246)Dashboard')
    db.dui0switches.insert( f0= 'aa247', f1= '(247)Dashboard')
    db.dui0switches.insert( f0= 'aa248', f1= '(248)UI Elements')
    db.dui0switches.insert( f0= 'lb249', f1= '(249)Switches')
    db.commit()
#
