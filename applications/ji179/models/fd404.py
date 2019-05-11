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
    db.d404.insert( f0= 'pb368', f1= '(368)Search for...')
    db.d404.insert( f0= 'sx369', f1= '(369)9+')
    db.d404.insert( f0= 'aa370', f1= '(370)Action')
    db.d404.insert( f0= 'aa371', f1= '(371)Another action')
    db.d404.insert( f0= 'aa372', f1= '(372)Something else here')
    db.d404.insert( f0= 'sx373', f1= '(373)7')
    db.d404.insert( f0= 'aa374', f1= '(374)Action')
    db.d404.insert( f0= 'aa375', f1= '(375)Another action')
    db.d404.insert( f0= 'aa376', f1= '(376)Something else here')
    db.d404.insert( f0= 'aa377', f1= '(377)Settings')
    db.d404.insert( f0= 'aa378', f1= '(378)Activity Log')
    db.d404.insert( f0= 'aa379', f1= '(379)Logout')
    db.d404.insert( f0= 'sp381', f1= '(381)Dashboard')
    db.d404.insert( f0= 'sp382', f1= '(382)Pages')
    db.d404.insert( f0= 'hf383', f1= '(383)Login Screens:')
    db.d404.insert( f0= 'hf387', f1= '(387)Other Pages:')
    db.d404.insert( f0= 'sp391', f1= '(391)Charts')
    db.d404.insert( f0= 'sp393', f1= '(393)Tables')
    db.d404.insert( f0= 'aa395', f1= '(395)Dashboard')
    db.d404.insert( f0= 'lb396', f1= '(396)404 Error')
    db.d404.insert( f0= 'ha397', f1= '(397)404')
    db.d404.insert( f0= 'aa398', f1= '(398)go back')
    db.d404.insert( f0= 'pc400', f1= '(400).')
    db.d404.insert( f0= 'aa401', f1= '(401)return home')
    db.d404.insert( f0= 'sp402', f1= '(402)Copyright  Your Website 2019')
    db.d404.insert( f0= 'he403', f1= '(403)Ready to Leave?')
    db.d404.insert( f0= 'sx404', f1= '(404)')
    db.d404.insert( f0= 'di405', f1= '(405)Select Logout below if you are ready to end your current session.')
    db.d404.insert( f0= 'bu406', f1= '(406)Cancel')
    db.commit()
#
