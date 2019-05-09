#
# table for controller: index
#

from gluon.contrib.populate import populate

db.define_table('dindex', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dindex.id ).count():
    db.dindex.insert( f0= 'aa289', f1= '(289)Start Bootstrap')
    db.dindex.insert( f0= 'pb290', f1= '(290)Search for...')
    db.dindex.insert( f0= 'sx291', f1= '(291)9+')
    db.dindex.insert( f0= 'aa292', f1= '(292)Action')
    db.dindex.insert( f0= 'aa293', f1= '(293)Another action')
    db.dindex.insert( f0= 'aa294', f1= '(294)Something else here')
    db.dindex.insert( f0= 'sx295', f1= '(295)7')
    db.dindex.insert( f0= 'aa296', f1= '(296)Action')
    db.dindex.insert( f0= 'aa297', f1= '(297)Another action')
    db.dindex.insert( f0= 'aa298', f1= '(298)Something else here')
    db.dindex.insert( f0= 'aa299', f1= '(299)Settings')
    db.dindex.insert( f0= 'aa300', f1= '(300)Activity Log')
    db.dindex.insert( f0= 'aa301', f1= '(301)Logout')
    db.dindex.insert( f0= 'sp303', f1= '(303)Dashboard')
    db.dindex.insert( f0= 'sp304', f1= '(304)Pages')
    db.dindex.insert( f0= 'hf305', f1= '(305)Login Screens:')
    db.dindex.insert( f0= 'aa307', f1= '(307)Login')
    db.dindex.insert( f0= 'aa309', f1= '(309)Register')
    db.dindex.insert( f0= 'aa311', f1= '(311)Forgot Password')
    db.dindex.insert( f0= 'hf312', f1= '(312)Other Pages:')
    db.dindex.insert( f0= 'aa314', f1= '(314)404 Page')
    db.dindex.insert( f0= 'aa316', f1= '(316)Blank Page')
    db.dindex.insert( f0= 'sp318', f1= '(318)Charts')
    db.dindex.insert( f0= 'sp320', f1= '(320)Tables')
    db.dindex.insert( f0= 'aa321', f1= '(321)Dashboard')
    db.dindex.insert( f0= 'lb322', f1= '(322)Overview')
    db.dindex.insert( f0= 'di323', f1= '(323)26 New Messages!')
    db.dindex.insert( f0= 'sx324', f1= '(324)View Details')
    db.dindex.insert( f0= 'di325', f1= '(325)11 New Tasks!')
    db.dindex.insert( f0= 'sx326', f1= '(326)View Details')
    db.dindex.insert( f0= 'di327', f1= '(327)123 New Orders!')
    db.dindex.insert( f0= 'sx328', f1= '(328)View Details')
    db.dindex.insert( f0= 'di329', f1= '(329)13 New Tickets!')
    db.dindex.insert( f0= 'sx330', f1= '(330)View Details')
    db.dindex.insert( f0= 'di331', f1= '(331)Updated yesterday at 11:59 PM')
    db.dindex.insert( f0= 'di389', f1= '(389)Updated yesterday at 11:59 PM')
    db.dindex.insert( f0= 'sp390', f1= '(390)Copyright  Your Website 2018')
    db.dindex.insert( f0= 'he391', f1= '(391)Ready to Leave?')
    db.dindex.insert( f0= 'sx392', f1= '(392)')
    db.dindex.insert( f0= 'di393', f1= '(393)Select Logout below if you are ready to end your current session.')
    db.dindex.insert( f0= 'bu394', f1= '(394)Cancel')
    db.dindex.insert( f0= 'aa396', f1= '(396)Logout')
    db.commit()
#
