#
# table for controller: tables
#

from gluon.contrib.populate import populate

db.define_table('dtables', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtables.id ).count():
    db.dtables.insert( f0= 'aa116', f1= '(116)Start Bootstrap')
    db.dtables.insert( f0= 'pb117', f1= '(117)Search for...')
    db.dtables.insert( f0= 'sx118', f1= '(118)9+')
    db.dtables.insert( f0= 'aa119', f1= '(119)Action')
    db.dtables.insert( f0= 'aa120', f1= '(120)Another action')
    db.dtables.insert( f0= 'aa121', f1= '(121)Something else here')
    db.dtables.insert( f0= 'aa122', f1= '(122)Action')
    db.dtables.insert( f0= 'aa123', f1= '(123)Another action')
    db.dtables.insert( f0= 'aa124', f1= '(124)Something else here')
    db.dtables.insert( f0= 'aa125', f1= '(125)Settings')
    db.dtables.insert( f0= 'aa126', f1= '(126)Activity Log')
    db.dtables.insert( f0= 'aa127', f1= '(127)Logout')
    db.dtables.insert( f0= 'sp129', f1= '(129)Dashboard')
    db.dtables.insert( f0= 'sp130', f1= '(130)Pages')
    db.dtables.insert( f0= 'hf131', f1= '(131)Login Screens:')
    db.dtables.insert( f0= 'aa133', f1= '(133)Login')
    db.dtables.insert( f0= 'aa135', f1= '(135)Register')
    db.dtables.insert( f0= 'aa137', f1= '(137)Forgot Password')
    db.dtables.insert( f0= 'hf138', f1= '(138)Other Pages:')
    db.dtables.insert( f0= 'aa140', f1= '(140)404 Page')
    db.dtables.insert( f0= 'aa142', f1= '(142)Blank Page')
    db.dtables.insert( f0= 'sp144', f1= '(144)Charts')
    db.dtables.insert( f0= 'sp146', f1= '(146)Tables')
    db.dtables.insert( f0= 'aa147', f1= '(147)Dashboard')
    db.dtables.insert( f0= 'lb148', f1= '(148)Tables')
    db.dtables.insert( f0= 'di206', f1= '(206)Updated yesterday at 11:59 PM')
    db.dtables.insert( f0= 'sp207', f1= '(207)Copyright  Your Website 2019')
    db.dtables.insert( f0= 'he208', f1= '(208)Ready to Leave?')
    db.dtables.insert( f0= 'sx209', f1= '(209)')
    db.dtables.insert( f0= 'di210', f1= '(210)Select Logout below if you are ready to end your current session.')
    db.dtables.insert( f0= 'bu211', f1= '(211)Cancel')
    db.dtables.insert( f0= 'aa213', f1= '(213)Logout')
    db.commit()
#
