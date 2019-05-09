#
# table for controller: X404
#

from gluon.contrib.populate import populate

db.define_table('d404', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.d404.id ).count():
    db.d404.insert( f0= 'aa413', f1= '(413)Start Bootstrap')
    db.d404.insert( f0= 'pb414', f1= '(414)Search for...')
    db.d404.insert( f0= 'sx415', f1= '(415)9+')
    db.d404.insert( f0= 'aa416', f1= '(416)Action')
    db.d404.insert( f0= 'aa417', f1= '(417)Another action')
    db.d404.insert( f0= 'aa418', f1= '(418)Something else here')
    db.d404.insert( f0= 'sx419', f1= '(419)7')
    db.d404.insert( f0= 'aa420', f1= '(420)Action')
    db.d404.insert( f0= 'aa421', f1= '(421)Another action')
    db.d404.insert( f0= 'aa422', f1= '(422)Something else here')
    db.d404.insert( f0= 'aa423', f1= '(423)Settings')
    db.d404.insert( f0= 'aa424', f1= '(424)Activity Log')
    db.d404.insert( f0= 'aa425', f1= '(425)Logout')
    db.d404.insert( f0= 'sp427', f1= '(427)Dashboard')
    db.d404.insert( f0= 'sp428', f1= '(428)Pages')
    db.d404.insert( f0= 'hf429', f1= '(429)Login Screens:')
    db.d404.insert( f0= 'aa431', f1= '(431)Login')
    db.d404.insert( f0= 'aa433', f1= '(433)Register')
    db.d404.insert( f0= 'aa435', f1= '(435)Forgot Password')
    db.d404.insert( f0= 'hf436', f1= '(436)Other Pages:')
    db.d404.insert( f0= 'aa438', f1= '(438)404 Page')
    db.d404.insert( f0= 'aa440', f1= '(440)Blank Page')
    db.d404.insert( f0= 'sp442', f1= '(442)Charts')
    db.d404.insert( f0= 'sp444', f1= '(444)Tables')
    db.d404.insert( f0= 'aa446', f1= '(446)Dashboard')
    db.d404.insert( f0= 'lb447', f1= '(447)404 Error')
    db.d404.insert( f0= 'ha448', f1= '(448)404')
    db.d404.insert( f0= 'aa449', f1= '(449)go back')
    db.d404.insert( f0= 'pc451', f1= '(451).')
    db.d404.insert( f0= 'aa452', f1= '(452)return home')
    db.d404.insert( f0= 'sp453', f1= '(453)Copyright  Your Website 2018')
    db.d404.insert( f0= 'he454', f1= '(454)Ready to Leave?')
    db.d404.insert( f0= 'sx455', f1= '(455)')
    db.d404.insert( f0= 'di456', f1= '(456)Select Logout below if you are ready to end your current session.')
    db.d404.insert( f0= 'bu457', f1= '(457)Cancel')
    db.d404.insert( f0= 'aa459', f1= '(459)Logout')
    db.commit()
#
