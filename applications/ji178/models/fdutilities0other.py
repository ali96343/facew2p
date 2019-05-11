#
# table for controller: utilities_other
#

from gluon.contrib.populate import populate

db.define_table('dutilities0other', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dutilities0other.id ).count():
    db.dutilities0other.insert( f0= 'sp377', f1= '(377)Dashboard')
    db.dutilities0other.insert( f0= 'sp378', f1= '(378)Components')
    db.dutilities0other.insert( f0= 'hf379', f1= '(379)Custom Components:')
    db.dutilities0other.insert( f0= 'sp382', f1= '(382)Utilities')
    db.dutilities0other.insert( f0= 'hf383', f1= '(383)Custom Utilities:')
    db.dutilities0other.insert( f0= 'sp388', f1= '(388)Pages')
    db.dutilities0other.insert( f0= 'hf389', f1= '(389)Login Screens:')
    db.dutilities0other.insert( f0= 'hf393', f1= '(393)Other Pages:')
    db.dutilities0other.insert( f0= 'sp397', f1= '(397)Charts')
    db.dutilities0other.insert( f0= 'sp399', f1= '(399)Tables')
    db.dutilities0other.insert( f0= 'pb400', f1= '(400)Search for...')
    db.dutilities0other.insert( f0= 'pb401', f1= '(401)Search for...')
    db.dutilities0other.insert( f0= 'sx402', f1= '(402)3+')
    db.dutilities0other.insert( f0= 'di403', f1= '(403)December 12, 2019')
    db.dutilities0other.insert( f0= 'sx404', f1= '(404)A new monthly report is ready to download!')
    db.dutilities0other.insert( f0= 'di405', f1= '(405)December 7, 2019')
    db.dutilities0other.insert( f0= 'di406', f1= '(406)December 2, 2019')
    db.dutilities0other.insert( f0= 'aa407', f1= '(407)Show All Alerts')
    db.dutilities0other.insert( f0= 'sx408', f1= '(408)7')
    db.dutilities0other.insert( f0= 'di409', f1= '(409)Hi there! I am wondering if you can help me with a problem I ve been having.')
    db.dutilities0other.insert( f0= 'di410', f1= '(410)Emily Fowler  58m')
    db.dutilities0other.insert( f0= 'di411', f1= '(411)I have the photos that you ordered last month, how would you like them sent to you?')
    db.dutilities0other.insert( f0= 'di412', f1= '(412)Jae Chun  1d')
    db.dutilities0other.insert( f0= 'di413', f1= '(413)Morgan Alvarez  2d')
    db.dutilities0other.insert( f0= 'di414', f1= '(414)Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren t good...')
    db.dutilities0other.insert( f0= 'di415', f1= '(415)Chicken the Dog  2w')
    db.dutilities0other.insert( f0= 'aa416', f1= '(416)Read More Messages')
    db.dutilities0other.insert( f0= 'sx417', f1= '(417)Valerie Luna')
    db.dutilities0other.insert( f0= 'ha418', f1= '(418)Other Utilities')
    db.dutilities0other.insert( f0= 'pc419', f1= '(419)page. The custom utilities below were created to extend this theme past the default utility classes built into Bootstrap s framework.')
    db.dutilities0other.insert( f0= 'aa420', f1= '(420)Bootstrap Documentation')
    db.dutilities0other.insert( f0= 'hf421', f1= '(421)Overflow Hidden Utilty')
    db.dutilities0other.insert( f0= 'hf422', f1= '(422)Progress Small Utility')
    db.dutilities0other.insert( f0= 'di423', f1= '(423)Normal Progress Bar')
    db.dutilities0other.insert( f0= 'di424', f1= '(424)Small Progress Bar')
    db.dutilities0other.insert( f0= 'hf425', f1= '(425)Dropdown - No Arrow')
    db.dutilities0other.insert( f0= 'aa426', f1= '(426)Action')
    db.dutilities0other.insert( f0= 'aa427', f1= '(427)Another action')
    db.dutilities0other.insert( f0= 'aa428', f1= '(428)Something else here')
    db.dutilities0other.insert( f0= 'hf429', f1= '(429)Rotation Utilities')
    db.dutilities0other.insert( f0= 'di430', f1= '(430).rotate-15')
    db.dutilities0other.insert( f0= 'di431', f1= '(431).rotate-n-15')
    db.dutilities0other.insert( f0= 'sp432', f1= '(432)Copyright &copy; Your Website 2019')
    db.dutilities0other.insert( f0= 'he433', f1= '(433)Ready to Leave?')
    db.dutilities0other.insert( f0= 'sx434', f1= '(434)')
    db.dutilities0other.insert( f0= 'di435', f1= '(435)Select Logout below if you are ready to end your current session.')
    db.dutilities0other.insert( f0= 'bu436', f1= '(436)Cancel')
    db.commit()
#
