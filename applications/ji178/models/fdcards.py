#
# table for controller: cards
#

from gluon.contrib.populate import populate

db.define_table('dcards', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcards.id ).count():
    db.dcards.insert( f0= 'sp302', f1= '(302)Dashboard')
    db.dcards.insert( f0= 'sp303', f1= '(303)Components')
    db.dcards.insert( f0= 'hf304', f1= '(304)Custom Components:')
    db.dcards.insert( f0= 'sp307', f1= '(307)Utilities')
    db.dcards.insert( f0= 'hf308', f1= '(308)Custom Utilities:')
    db.dcards.insert( f0= 'sp313', f1= '(313)Pages')
    db.dcards.insert( f0= 'hf314', f1= '(314)Login Screens:')
    db.dcards.insert( f0= 'hf318', f1= '(318)Other Pages:')
    db.dcards.insert( f0= 'sp322', f1= '(322)Charts')
    db.dcards.insert( f0= 'sp324', f1= '(324)Tables')
    db.dcards.insert( f0= 'pb325', f1= '(325)Search for...')
    db.dcards.insert( f0= 'pb326', f1= '(326)Search for...')
    db.dcards.insert( f0= 'sx327', f1= '(327)3+')
    db.dcards.insert( f0= 'di328', f1= '(328)December 12, 2019')
    db.dcards.insert( f0= 'sx329', f1= '(329)A new monthly report is ready to download!')
    db.dcards.insert( f0= 'di330', f1= '(330)December 7, 2019')
    db.dcards.insert( f0= 'di331', f1= '(331)December 2, 2019')
    db.dcards.insert( f0= 'aa332', f1= '(332)Show All Alerts')
    db.dcards.insert( f0= 'sx333', f1= '(333)7')
    db.dcards.insert( f0= 'di334', f1= '(334)Hi there! I am wondering if you can help me with a problem I ve been having.')
    db.dcards.insert( f0= 'di335', f1= '(335)Emily Fowler  58m')
    db.dcards.insert( f0= 'di336', f1= '(336)I have the photos that you ordered last month, how would you like them sent to you?')
    db.dcards.insert( f0= 'di337', f1= '(337)Jae Chun  1d')
    db.dcards.insert( f0= 'di338', f1= '(338)Morgan Alvarez  2d')
    db.dcards.insert( f0= 'di339', f1= '(339)Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren t good...')
    db.dcards.insert( f0= 'di340', f1= '(340)Chicken the Dog  2w')
    db.dcards.insert( f0= 'aa341', f1= '(341)Read More Messages')
    db.dcards.insert( f0= 'sx342', f1= '(342)Valerie Luna')
    db.dcards.insert( f0= 'ha343', f1= '(343)Cards')
    db.dcards.insert( f0= 'di344', f1= '(344)Earnings (Monthly)')
    db.dcards.insert( f0= 'di345', f1= '(345)$40,000')
    db.dcards.insert( f0= 'di346', f1= '(346)Earnings (Annual)')
    db.dcards.insert( f0= 'di347', f1= '(347)$215,000')
    db.dcards.insert( f0= 'di348', f1= '(348)Tasks')
    db.dcards.insert( f0= 'di349', f1= '(349)50%')
    db.dcards.insert( f0= 'di350', f1= '(350)Pending Requests')
    db.dcards.insert( f0= 'di351', f1= '(351)18')
    db.dcards.insert( f0= 'hf352', f1= '(352)Basic Card Example')
    db.dcards.insert( f0= 'hf353', f1= '(353)Dropdown Card Example')
    db.dcards.insert( f0= 'di354', f1= '(354)Dropdown Header:')
    db.dcards.insert( f0= 'aa355', f1= '(355)Action')
    db.dcards.insert( f0= 'aa356', f1= '(356)Another action')
    db.dcards.insert( f0= 'aa357', f1= '(357)Something else here')
    db.dcards.insert( f0= 'hf358', f1= '(358)Collapsable Card Example')
    db.dcards.insert( f0= 'sp359', f1= '(359)Click on the card header')
    db.dcards.insert( f0= 'sp360', f1= '(360)Copyright &copy; Your Website 2019')
    db.dcards.insert( f0= 'he361', f1= '(361)Ready to Leave?')
    db.dcards.insert( f0= 'sx362', f1= '(362)')
    db.dcards.insert( f0= 'di363', f1= '(363)Select Logout below if you are ready to end your current session.')
    db.dcards.insert( f0= 'bu364', f1= '(364)Cancel')
    db.commit()
#
