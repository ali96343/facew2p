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
    db.d404.insert( f0= 'aa401', f1= '(401)Start Bootstrap')
    db.d404.insert( f0= 'pb402', f1= '(402)Search for...')
    db.d404.insert( f0= 'sx403', f1= '(403)9+')
    db.d404.insert( f0= 'aa404', f1= '(404)Action')
    db.d404.insert( f0= 'aa405', f1= '(405)Another action')
    db.d404.insert( f0= 'aa406', f1= '(406)Something else here')
    db.d404.insert( f0= 'aa407', f1= '(407)Action')
    db.d404.insert( f0= 'aa408', f1= '(408)Another action')
    db.d404.insert( f0= 'aa409', f1= '(409)Something else here')
    db.d404.insert( f0= 'aa410', f1= '(410)Settings')
    db.d404.insert( f0= 'aa411', f1= '(411)Activity Log')
    db.d404.insert( f0= 'aa412', f1= '(412)Logout')
    db.d404.insert( f0= 'sp414', f1= '(414)Dashboard')
    db.d404.insert( f0= 'sp415', f1= '(415)Pages')
    db.d404.insert( f0= 'hf416', f1= '(416)Login Screens:')
    db.d404.insert( f0= 'aa418', f1= '(418)Login')
    db.d404.insert( f0= 'aa420', f1= '(420)Register')
    db.d404.insert( f0= 'aa422', f1= '(422)Forgot Password')
    db.d404.insert( f0= 'hf423', f1= '(423)Other Pages:')
    db.d404.insert( f0= 'aa425', f1= '(425)404 Page')
    db.d404.insert( f0= 'aa427', f1= '(427)Blank Page')
    db.d404.insert( f0= 'sp429', f1= '(429)Charts')
    db.d404.insert( f0= 'sp431', f1= '(431)Tables')
    db.d404.insert( f0= 'aa433', f1= '(433)Dashboard')
    db.d404.insert( f0= 'lb434', f1= '(434)404 Error')
    db.d404.insert( f0= 'ha435', f1= '(435)404')
    db.d404.insert( f0= 'aa436', f1= '(436)go back')
    db.d404.insert( f0= 'aa438', f1= '(438)return home')
    db.d404.insert( f0= 'sp439', f1= '(439)Copyright  Your Website 2019')
    db.d404.insert( f0= 'he440', f1= '(440)Ready to Leave?')
    db.d404.insert( f0= 'sx441', f1= '(441)')
    db.d404.insert( f0= 'di442', f1= '(442)Select Logout below if you are ready to end your current session.')
    db.d404.insert( f0= 'bu443', f1= '(443)Cancel')
    db.d404.insert( f0= 'aa445', f1= '(445)Logout')
    db.commit()
#
