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
    db.dtables.insert( f0= 'sp450', f1= '(450)Dashboard')
    db.dtables.insert( f0= 'sp451', f1= '(451)Components')
    db.dtables.insert( f0= 'hf452', f1= '(452)Custom Components:')
    db.dtables.insert( f0= 'sp455', f1= '(455)Utilities')
    db.dtables.insert( f0= 'hf456', f1= '(456)Custom Utilities:')
    db.dtables.insert( f0= 'sp461', f1= '(461)Pages')
    db.dtables.insert( f0= 'hf462', f1= '(462)Login Screens:')
    db.dtables.insert( f0= 'hf466', f1= '(466)Other Pages:')
    db.dtables.insert( f0= 'sp470', f1= '(470)Charts')
    db.dtables.insert( f0= 'sp472', f1= '(472)Tables')
    db.dtables.insert( f0= 'pb473', f1= '(473)Search for...')
    db.dtables.insert( f0= 'pb474', f1= '(474)Search for...')
    db.dtables.insert( f0= 'sx475', f1= '(475)3+')
    db.dtables.insert( f0= 'di476', f1= '(476)December 12, 2019')
    db.dtables.insert( f0= 'sx477', f1= '(477)A new monthly report is ready to download!')
    db.dtables.insert( f0= 'di478', f1= '(478)December 7, 2019')
    db.dtables.insert( f0= 'di479', f1= '(479)December 2, 2019')
    db.dtables.insert( f0= 'aa480', f1= '(480)Show All Alerts')
    db.dtables.insert( f0= 'sx481', f1= '(481)7')
    db.dtables.insert( f0= 'di482', f1= '(482)Hi there! I am wondering if you can help me with a problem I ve been having.')
    db.dtables.insert( f0= 'di483', f1= '(483)Emily Fowler  58m')
    db.dtables.insert( f0= 'di484', f1= '(484)I have the photos that you ordered last month, how would you like them sent to you?')
    db.dtables.insert( f0= 'di485', f1= '(485)Jae Chun  1d')
    db.dtables.insert( f0= 'di486', f1= '(486)Morgan Alvarez  2d')
    db.dtables.insert( f0= 'di487', f1= '(487)Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren t good...')
    db.dtables.insert( f0= 'di488', f1= '(488)Chicken the Dog  2w')
    db.dtables.insert( f0= 'aa489', f1= '(489)Read More Messages')
    db.dtables.insert( f0= 'sx490', f1= '(490)Valerie Luna')
    db.dtables.insert( f0= 'ha491', f1= '(491)Tables')
    db.dtables.insert( f0= 'pc492', f1= '(492).')
    db.dtables.insert( f0= 'aa493', f1= '(493)official DataTables documentation')
    db.dtables.insert( f0= 'hf494', f1= '(494)DataTables Example')
    db.dtables.insert( f0= 'sp552', f1= '(552)Copyright &copy; Your Website 2019')
    db.dtables.insert( f0= 'he553', f1= '(553)Ready to Leave?')
    db.dtables.insert( f0= 'sx554', f1= '(554)')
    db.dtables.insert( f0= 'di555', f1= '(555)Select Logout below if you are ready to end your current session.')
    db.dtables.insert( f0= 'bu556', f1= '(556)Cancel')
    db.commit()
#
