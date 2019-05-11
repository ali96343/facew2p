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
    db.dindex.insert( f0= 'pb252', f1= '(252)Search for...')
    db.dindex.insert( f0= 'sx253', f1= '(253)9+')
    db.dindex.insert( f0= 'aa254', f1= '(254)Action')
    db.dindex.insert( f0= 'aa255', f1= '(255)Another action')
    db.dindex.insert( f0= 'aa256', f1= '(256)Something else here')
    db.dindex.insert( f0= 'sx257', f1= '(257)7')
    db.dindex.insert( f0= 'aa258', f1= '(258)Action')
    db.dindex.insert( f0= 'aa259', f1= '(259)Another action')
    db.dindex.insert( f0= 'aa260', f1= '(260)Something else here')
    db.dindex.insert( f0= 'aa261', f1= '(261)Settings')
    db.dindex.insert( f0= 'aa262', f1= '(262)Activity Log')
    db.dindex.insert( f0= 'aa263', f1= '(263)Logout')
    db.dindex.insert( f0= 'sp265', f1= '(265)Dashboard')
    db.dindex.insert( f0= 'sp266', f1= '(266)Pages')
    db.dindex.insert( f0= 'hf267', f1= '(267)Login Screens:')
    db.dindex.insert( f0= 'hf271', f1= '(271)Other Pages:')
    db.dindex.insert( f0= 'sp275', f1= '(275)Charts')
    db.dindex.insert( f0= 'sp277', f1= '(277)Tables')
    db.dindex.insert( f0= 'aa278', f1= '(278)Dashboard')
    db.dindex.insert( f0= 'lb279', f1= '(279)Overview')
    db.dindex.insert( f0= 'di280', f1= '(280)26 New Messages!')
    db.dindex.insert( f0= 'sx281', f1= '(281)View Details')
    db.dindex.insert( f0= 'di282', f1= '(282)11 New Tasks!')
    db.dindex.insert( f0= 'sx283', f1= '(283)View Details')
    db.dindex.insert( f0= 'di284', f1= '(284)123 New Orders!')
    db.dindex.insert( f0= 'sx285', f1= '(285)View Details')
    db.dindex.insert( f0= 'di286', f1= '(286)13 New Tickets!')
    db.dindex.insert( f0= 'sx287', f1= '(287)View Details')
    db.dindex.insert( f0= 'di288', f1= '(288)Updated yesterday at 11:59 PM')
    db.dindex.insert( f0= 'di346', f1= '(346)Updated yesterday at 11:59 PM')
    db.dindex.insert( f0= 'sp347', f1= '(347)Copyright  Your Website 2019')
    db.dindex.insert( f0= 'he348', f1= '(348)Ready to Leave?')
    db.dindex.insert( f0= 'sx349', f1= '(349)')
    db.dindex.insert( f0= 'di350', f1= '(350)Select Logout below if you are ready to end your current session.')
    db.dindex.insert( f0= 'bu351', f1= '(351)Cancel')
    db.commit()
#
