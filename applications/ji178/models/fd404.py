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
    db.d404.insert( f0= 'sp983', f1= '(983)Dashboard')
    db.d404.insert( f0= 'sp984', f1= '(984)Components')
    db.d404.insert( f0= 'hf985', f1= '(985)Custom Components:')
    db.d404.insert( f0= 'aa987', f1= '(987)Buttons')
    db.d404.insert( f0= 'aa989', f1= '(989)Cards')
    db.d404.insert( f0= 'sp990', f1= '(990)Utilities')
    db.d404.insert( f0= 'hf991', f1= '(991)Custom Utilities:')
    db.d404.insert( f0= 'aa993', f1= '(993)Colors')
    db.d404.insert( f0= 'aa995', f1= '(995)Borders')
    db.d404.insert( f0= 'aa997', f1= '(997)Animations')
    db.d404.insert( f0= 'aa999', f1= '(999)Other')
    db.d404.insert( f0= 'sp1000', f1= '(1000)Pages')
    db.d404.insert( f0= 'hf1001', f1= '(1001)Login Screens:')
    db.d404.insert( f0= 'aa1003', f1= '(1003)Login')
    db.d404.insert( f0= 'aa1005', f1= '(1005)Register')
    db.d404.insert( f0= 'aa1007', f1= '(1007)Forgot Password')
    db.d404.insert( f0= 'hf1008', f1= '(1008)Other Pages:')
    db.d404.insert( f0= 'aa1010', f1= '(1010)404 Page')
    db.d404.insert( f0= 'aa1012', f1= '(1012)Blank Page')
    db.d404.insert( f0= 'sp1014', f1= '(1014)Charts')
    db.d404.insert( f0= 'sp1016', f1= '(1016)Tables')
    db.d404.insert( f0= 'pb1017', f1= '(1017)Search for...')
    db.d404.insert( f0= 'pb1018', f1= '(1018)Search for...')
    db.d404.insert( f0= 'sx1019', f1= '(1019)3+')
    db.d404.insert( f0= 'di1020', f1= '(1020)December 12, 2019')
    db.d404.insert( f0= 'sx1021', f1= '(1021)A new monthly report is ready to download!')
    db.d404.insert( f0= 'di1022', f1= '(1022)December 7, 2019')
    db.d404.insert( f0= 'di1023', f1= '(1023)December 2, 2019')
    db.d404.insert( f0= 'aa1024', f1= '(1024)Show All Alerts')
    db.d404.insert( f0= 'di1025', f1= '(1025)Hi there! I am wondering if you can help me with a problem I ve been having.')
    db.d404.insert( f0= 'di1026', f1= '(1026)Emily Fowler  58m')
    db.d404.insert( f0= 'di1027', f1= '(1027)I have the photos that you ordered last month, how would you like them sent to you?')
    db.d404.insert( f0= 'di1028', f1= '(1028)Jae Chun  1d')
    db.d404.insert( f0= 'di1029', f1= '(1029)Last month s report looks great, I am very happy with the progress so far, keep up the good work!')
    db.d404.insert( f0= 'di1030', f1= '(1030)Morgan Alvarez  2d')
    db.d404.insert( f0= 'di1031', f1= '(1031)Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren t good...')
    db.d404.insert( f0= 'di1032', f1= '(1032)Chicken the Dog  2w')
    db.d404.insert( f0= 'aa1033', f1= '(1033)Read More Messages')
    db.d404.insert( f0= 'sx1034', f1= '(1034)Valerie Luna')
    db.d404.insert( f0= 'di1035', f1= '(1035)404')
    db.d404.insert( f0= 'pc1036', f1= '(1036)Page Not Found')
    db.d404.insert( f0= 'pc1037', f1= '(1037)It looks like you found a glitch in the matrix...')
    db.d404.insert( f0= 'sp1039', f1= '(1039)Copyright &copy; Your Website 2019')
    db.d404.insert( f0= 'he1040', f1= '(1040)Ready to Leave?')
    db.d404.insert( f0= 'sx1041', f1= '(1041)')
    db.d404.insert( f0= 'di1042', f1= '(1042)Select Logout below if you are ready to end your current session.')
    db.d404.insert( f0= 'bu1043', f1= '(1043)Cancel')
    db.d404.insert( f0= 'aa1045', f1= '(1045)Logout')
    db.commit()
#
