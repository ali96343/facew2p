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
    db.dindex.insert( f0= 'aa279', f1= '(279)Start Bootstrap')
    db.dindex.insert( f0= 'pb280', f1= '(280)Search for...')
    db.dindex.insert( f0= 'sx281', f1= '(281)9+')
    db.dindex.insert( f0= 'aa282', f1= '(282)Action')
    db.dindex.insert( f0= 'aa283', f1= '(283)Another action')
    db.dindex.insert( f0= 'aa284', f1= '(284)Something else here')
    db.dindex.insert( f0= 'aa285', f1= '(285)Action')
    db.dindex.insert( f0= 'aa286', f1= '(286)Another action')
    db.dindex.insert( f0= 'aa287', f1= '(287)Something else here')
    db.dindex.insert( f0= 'aa288', f1= '(288)Settings')
    db.dindex.insert( f0= 'aa289', f1= '(289)Activity Log')
    db.dindex.insert( f0= 'aa290', f1= '(290)Logout')
    db.dindex.insert( f0= 'sp292', f1= '(292)Dashboard')
    db.dindex.insert( f0= 'sp293', f1= '(293)Pages')
    db.dindex.insert( f0= 'hf294', f1= '(294)Login Screens:')
    db.dindex.insert( f0= 'aa296', f1= '(296)Login')
    db.dindex.insert( f0= 'aa298', f1= '(298)Register')
    db.dindex.insert( f0= 'aa300', f1= '(300)Forgot Password')
    db.dindex.insert( f0= 'hf301', f1= '(301)Other Pages:')
    db.dindex.insert( f0= 'aa303', f1= '(303)404 Page')
    db.dindex.insert( f0= 'aa305', f1= '(305)Blank Page')
    db.dindex.insert( f0= 'sp307', f1= '(307)Charts')
    db.dindex.insert( f0= 'sp309', f1= '(309)Tables')
    db.dindex.insert( f0= 'aa310', f1= '(310)Dashboard')
    db.dindex.insert( f0= 'lb311', f1= '(311)Overview')
    db.dindex.insert( f0= 'di312', f1= '(312)26 New Messages!')
    db.dindex.insert( f0= 'sx313', f1= '(313)View Details')
    db.dindex.insert( f0= 'di314', f1= '(314)11 New Tasks!')
    db.dindex.insert( f0= 'sx315', f1= '(315)View Details')
    db.dindex.insert( f0= 'di316', f1= '(316)123 New Orders!')
    db.dindex.insert( f0= 'sx317', f1= '(317)View Details')
    db.dindex.insert( f0= 'di318', f1= '(318)13 New Tickets!')
    db.dindex.insert( f0= 'sx319', f1= '(319)View Details')
    db.dindex.insert( f0= 'di320', f1= '(320)Updated yesterday at 11:59 PM')
    db.dindex.insert( f0= 'di378', f1= '(378)Updated yesterday at 11:59 PM')
    db.dindex.insert( f0= 'sp379', f1= '(379)Copyright  Your Website 2019')
    db.dindex.insert( f0= 'he380', f1= '(380)Ready to Leave?')
    db.dindex.insert( f0= 'sx381', f1= '(381)')
    db.dindex.insert( f0= 'di382', f1= '(382)Select Logout below if you are ready to end your current session.')
    db.dindex.insert( f0= 'bu383', f1= '(383)Cancel')
    db.dindex.insert( f0= 'aa385', f1= '(385)Logout')
    db.commit()
#
