#
# table for controller: buttons
#

from gluon.contrib.populate import populate

db.define_table('dbuttons', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dbuttons.id ).count():
    db.dbuttons.insert( f0= 'sp134', f1= '(134)Dashboard')
    db.dbuttons.insert( f0= 'sp135', f1= '(135)Components')
    db.dbuttons.insert( f0= 'hf136', f1= '(136)Custom Components:')
    db.dbuttons.insert( f0= 'sp139', f1= '(139)Utilities')
    db.dbuttons.insert( f0= 'hf140', f1= '(140)Custom Utilities:')
    db.dbuttons.insert( f0= 'sp145', f1= '(145)Pages')
    db.dbuttons.insert( f0= 'hf146', f1= '(146)Login Screens:')
    db.dbuttons.insert( f0= 'hf150', f1= '(150)Other Pages:')
    db.dbuttons.insert( f0= 'sp154', f1= '(154)Charts')
    db.dbuttons.insert( f0= 'sp156', f1= '(156)Tables')
    db.dbuttons.insert( f0= 'pb157', f1= '(157)Search for...')
    db.dbuttons.insert( f0= 'pb158', f1= '(158)Search for...')
    db.dbuttons.insert( f0= 'sx159', f1= '(159)3+')
    db.dbuttons.insert( f0= 'di160', f1= '(160)December 12, 2019')
    db.dbuttons.insert( f0= 'sx161', f1= '(161)A new monthly report is ready to download!')
    db.dbuttons.insert( f0= 'di162', f1= '(162)December 7, 2019')
    db.dbuttons.insert( f0= 'di163', f1= '(163)December 2, 2019')
    db.dbuttons.insert( f0= 'aa164', f1= '(164)Show All Alerts')
    db.dbuttons.insert( f0= 'sx165', f1= '(165)7')
    db.dbuttons.insert( f0= 'di166', f1= '(166)Hi there! I am wondering if you can help me with a problem I ve been having.')
    db.dbuttons.insert( f0= 'di167', f1= '(167)Emily Fowler  58m')
    db.dbuttons.insert( f0= 'di168', f1= '(168)I have the photos that you ordered last month, how would you like them sent to you?')
    db.dbuttons.insert( f0= 'di169', f1= '(169)Jae Chun  1d')
    db.dbuttons.insert( f0= 'di170', f1= '(170)Morgan Alvarez  2d')
    db.dbuttons.insert( f0= 'di171', f1= '(171)Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren t good...')
    db.dbuttons.insert( f0= 'di172', f1= '(172)Chicken the Dog  2w')
    db.dbuttons.insert( f0= 'aa173', f1= '(173)Read More Messages')
    db.dbuttons.insert( f0= 'sx174', f1= '(174)Valerie Luna')
    db.dbuttons.insert( f0= 'ha175', f1= '(175)Buttons')
    db.dbuttons.insert( f0= 'hf176', f1= '(176)Circle Buttons')
    db.dbuttons.insert( f0= 'pa177', f1= '(177)Use Font Awesome Icons (included with this theme package) along with the circle buttons as shown in the examples below!')
    db.dbuttons.insert( f0= 'hf178', f1= '(178)Brand Buttons')
    db.dbuttons.insert( f0= 'pa179', f1= '(179)Google and Facebook buttons are available featuring each company s respective brand color. They are used on the user login and registration pages.')
    db.dbuttons.insert( f0= 'pc180', f1= '(180)file.')
    db.dbuttons.insert( f0= 'pf181', f1= '(181)You can create more custom buttons by adding a new color variable in the')
    db.dbuttons.insert( f0= 'hf182', f1= '(182)Split Buttons with Icon')
    db.dbuttons.insert( f0= 'pc183', f1= '(183)helper class on the icons for additional styling, but it is not required.')
    db.dbuttons.insert( f0= 'pf184', f1= '(184)Works with any button colors, just use the')
    db.dbuttons.insert( f0= 'sx185', f1= '(185)Split Button Primary')
    db.dbuttons.insert( f0= 'sx186', f1= '(186)Split Button Success')
    db.dbuttons.insert( f0= 'sx187', f1= '(187)Split Button Info')
    db.dbuttons.insert( f0= 'sx188', f1= '(188)Split Button Warning')
    db.dbuttons.insert( f0= 'sx189', f1= '(189)Split Button Danger')
    db.dbuttons.insert( f0= 'sx190', f1= '(190)Split Button Secondary')
    db.dbuttons.insert( f0= 'sx191', f1= '(191)Split Button Primary')
    db.dbuttons.insert( f0= 'pa192', f1= '(192)Also works with small and large button classes!')
    db.dbuttons.insert( f0= 'sx193', f1= '(193)Split Button Small')
    db.dbuttons.insert( f0= 'sx194', f1= '(194)Split Button Large')
    db.dbuttons.insert( f0= 'sp195', f1= '(195)Copyright &copy; Your Website 2019')
    db.dbuttons.insert( f0= 'he196', f1= '(196)Ready to Leave?')
    db.dbuttons.insert( f0= 'sx197', f1= '(197)')
    db.dbuttons.insert( f0= 'di198', f1= '(198)Select Logout below if you are ready to end your current session.')
    db.dbuttons.insert( f0= 'bu199', f1= '(199)Cancel')
    db.commit()
#
