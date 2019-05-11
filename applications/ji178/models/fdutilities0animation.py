#
# table for controller: utilities_animation
#

from gluon.contrib.populate import populate

db.define_table('dutilities0animation', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dutilities0animation.id ).count():
    db.dutilities0animation.insert( f0= 'sp685', f1= '(685)Dashboard')
    db.dutilities0animation.insert( f0= 'sp686', f1= '(686)Components')
    db.dutilities0animation.insert( f0= 'hf687', f1= '(687)Custom Components:')
    db.dutilities0animation.insert( f0= 'sp690', f1= '(690)Utilities')
    db.dutilities0animation.insert( f0= 'hf691', f1= '(691)Custom Utilities:')
    db.dutilities0animation.insert( f0= 'sp696', f1= '(696)Pages')
    db.dutilities0animation.insert( f0= 'hf697', f1= '(697)Login Screens:')
    db.dutilities0animation.insert( f0= 'hf701', f1= '(701)Other Pages:')
    db.dutilities0animation.insert( f0= 'sp705', f1= '(705)Charts')
    db.dutilities0animation.insert( f0= 'sp707', f1= '(707)Tables')
    db.dutilities0animation.insert( f0= 'pb708', f1= '(708)Search for...')
    db.dutilities0animation.insert( f0= 'pb709', f1= '(709)Search for...')
    db.dutilities0animation.insert( f0= 'sx710', f1= '(710)3+')
    db.dutilities0animation.insert( f0= 'di711', f1= '(711)December 12, 2019')
    db.dutilities0animation.insert( f0= 'sx712', f1= '(712)A new monthly report is ready to download!')
    db.dutilities0animation.insert( f0= 'di713', f1= '(713)December 7, 2019')
    db.dutilities0animation.insert( f0= 'di714', f1= '(714)December 2, 2019')
    db.dutilities0animation.insert( f0= 'aa715', f1= '(715)Show All Alerts')
    db.dutilities0animation.insert( f0= 'sx716', f1= '(716)7')
    db.dutilities0animation.insert( f0= 'di717', f1= '(717)Hi there! I am wondering if you can help me with a problem I ve been having.')
    db.dutilities0animation.insert( f0= 'di718', f1= '(718)Emily Fowler  58m')
    db.dutilities0animation.insert( f0= 'di719', f1= '(719)I have the photos that you ordered last month, how would you like them sent to you?')
    db.dutilities0animation.insert( f0= 'di720', f1= '(720)Jae Chun  1d')
    db.dutilities0animation.insert( f0= 'di721', f1= '(721)Morgan Alvarez  2d')
    db.dutilities0animation.insert( f0= 'di722', f1= '(722)Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren t good...')
    db.dutilities0animation.insert( f0= 'di723', f1= '(723)Chicken the Dog  2w')
    db.dutilities0animation.insert( f0= 'aa724', f1= '(724)Read More Messages')
    db.dutilities0animation.insert( f0= 'sx725', f1= '(725)Valerie Luna')
    db.dutilities0animation.insert( f0= 'ha726', f1= '(726)Animation Utilities')
    db.dutilities0animation.insert( f0= 'pc727', f1= '(727)page. The custom utilities below were created to extend this theme past the default utility classes built into Bootstrap s framework.')
    db.dutilities0animation.insert( f0= 'aa728', f1= '(728)Bootstrap Documentation')
    db.dutilities0animation.insert( f0= 'hf729', f1= '(729)Grow In Animation Utilty')
    db.dutilities0animation.insert( f0= 'di730', f1= '(730)Navbar Dropdown Example:')
    db.dutilities0animation.insert( f0= 'aa731', f1= '(731)Navbar')
    db.dutilities0animation.insert( f0= 'aa732', f1= '(732)Action')
    db.dutilities0animation.insert( f0= 'aa733', f1= '(733)Another action')
    db.dutilities0animation.insert( f0= 'aa734', f1= '(734)Something else here')
    db.dutilities0animation.insert( f0= 'pc735', f1= '(735)Note: This utility animates the CSS transform property, meaning it will override any existing transforms on an element being animated! In this theme, the grow in animation is only being used on dropdowns within the navbar.')
    db.dutilities0animation.insert( f0= 'hf736', f1= '(736)Fade In Animation Utilty')
    db.dutilities0animation.insert( f0= 'di737', f1= '(737)Navbar Dropdown Example:')
    db.dutilities0animation.insert( f0= 'aa738', f1= '(738)Navbar')
    db.dutilities0animation.insert( f0= 'aa739', f1= '(739)Action')
    db.dutilities0animation.insert( f0= 'aa740', f1= '(740)Another action')
    db.dutilities0animation.insert( f0= 'aa741', f1= '(741)Something else here')
    db.dutilities0animation.insert( f0= 'di742', f1= '(742)Dropdown Button Example:')
    db.dutilities0animation.insert( f0= 'aa743', f1= '(743)Action')
    db.dutilities0animation.insert( f0= 'aa744', f1= '(744)Another action')
    db.dutilities0animation.insert( f0= 'aa745', f1= '(745)Something else here')
    db.dutilities0animation.insert( f0= 'pc746', f1= '(746)Note: This utility animates the CSS opacity property, meaning it will override any existing opacity on an element being animated!')
    db.dutilities0animation.insert( f0= 'sp747', f1= '(747)Copyright &copy; Your Website 2019')
    db.dutilities0animation.insert( f0= 'he748', f1= '(748)Ready to Leave?')
    db.dutilities0animation.insert( f0= 'sx749', f1= '(749)')
    db.dutilities0animation.insert( f0= 'di750', f1= '(750)Select Logout below if you are ready to end your current session.')
    db.dutilities0animation.insert( f0= 'bu751', f1= '(751)Cancel')
    db.commit()
#
