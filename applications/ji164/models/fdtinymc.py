#
# table for controller: tinymc
#

from gluon.contrib.populate import populate

db.define_table('dtinymc', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtinymc.id ).count():
    db.dtinymc.insert( f0= 'sp6805', f1= '(6805)outdated')
    db.dtinymc.insert( f0= 'pc6806', f1= '(6806)to improve your experience.')
    db.dtinymc.insert( f0= 'aa6807', f1= '(6807)upgrade your browser')
    db.dtinymc.insert( f0= 'sx6812', f1= '(6812)Ecommerce')
    db.dtinymc.insert( f0= 'sx6814', f1= '(6814)Dashboard v.1')
    db.dtinymc.insert( f0= 'sx6816', f1= '(6816)Dashboard v.2')
    db.dtinymc.insert( f0= 'sx6818', f1= '(6818)Dashboard v.3')
    db.dtinymc.insert( f0= 'sx6820', f1= '(6820)Product List')
    db.dtinymc.insert( f0= 'sx6822', f1= '(6822)Product Edit')
    db.dtinymc.insert( f0= 'sx6824', f1= '(6824)Product Detail')
    db.dtinymc.insert( f0= 'sx6826', f1= '(6826)Product Cart')
    db.dtinymc.insert( f0= 'sx6828', f1= '(6828)Product Payment')
    db.dtinymc.insert( f0= 'sx6830', f1= '(6830)Analytics')
    db.dtinymc.insert( f0= 'sx6832', f1= '(6832)Widgets')
    db.dtinymc.insert( f0= 'sx6834', f1= '(6834)Mailbox')
    db.dtinymc.insert( f0= 'sx6836', f1= '(6836)Inbox')
    db.dtinymc.insert( f0= 'sx6838', f1= '(6838)View Mail')
    db.dtinymc.insert( f0= 'sx6840', f1= '(6840)Compose Mail')
    db.dtinymc.insert( f0= 'sx6842', f1= '(6842)Interface')
    db.dtinymc.insert( f0= 'sx6844', f1= '(6844)Google Map')
    db.dtinymc.insert( f0= 'sx6846', f1= '(6846)Data Maps')
    db.dtinymc.insert( f0= 'sx6848', f1= '(6848)Pdf Viewer')
    db.dtinymc.insert( f0= 'sx6850', f1= '(6850)X-Editable')
    db.dtinymc.insert( f0= 'sx6852', f1= '(6852)Code Editor')
    db.dtinymc.insert( f0= 'sx6854', f1= '(6854)Tree View')
    db.dtinymc.insert( f0= 'sx6856', f1= '(6856)Preloader')
    db.dtinymc.insert( f0= 'sx6858', f1= '(6858)Images Cropper')
    db.dtinymc.insert( f0= 'sx6860', f1= '(6860)Miscellaneous')
    db.dtinymc.insert( f0= 'sx6862', f1= '(6862)File Manager')
    db.dtinymc.insert( f0= 'sx6864', f1= '(6864)Blog')
    db.dtinymc.insert( f0= 'sx6866', f1= '(6866)Blog Details')
    db.dtinymc.insert( f0= 'sx6868', f1= '(6868)404 Page')
    db.dtinymc.insert( f0= 'sx6870', f1= '(6870)500 Page')
    db.dtinymc.insert( f0= 'sx6872', f1= '(6872)Charts')
    db.dtinymc.insert( f0= 'sx6874', f1= '(6874)Bar Charts')
    db.dtinymc.insert( f0= 'sx6876', f1= '(6876)Line Charts')
    db.dtinymc.insert( f0= 'sx6878', f1= '(6878)Area Charts')
    db.dtinymc.insert( f0= 'sx6880', f1= '(6880)Rounded Charts')
    db.dtinymc.insert( f0= 'sx6882', f1= '(6882)C3 Charts')
    db.dtinymc.insert( f0= 'sx6884', f1= '(6884)Sparkline Charts')
    db.dtinymc.insert( f0= 'sx6886', f1= '(6886)Peity Charts')
    db.dtinymc.insert( f0= 'sx6888', f1= '(6888)Data Tables')
    db.dtinymc.insert( f0= 'sx6890', f1= '(6890)Static Table')
    db.dtinymc.insert( f0= 'sx6892', f1= '(6892)Data Table')
    db.dtinymc.insert( f0= 'sx6894', f1= '(6894)Forms Elements')
    db.dtinymc.insert( f0= 'sx6896', f1= '(6896)Bc Form Elements')
    db.dtinymc.insert( f0= 'sx6898', f1= '(6898)Ad Form Elements')
    db.dtinymc.insert( f0= 'sx6900', f1= '(6900)Password Meter')
    db.dtinymc.insert( f0= 'sx6902', f1= '(6902)Multi Upload')
    db.dtinymc.insert( f0= 'sx6904', f1= '(6904)Text Editor')
    db.dtinymc.insert( f0= 'sx6906', f1= '(6906)Dual List Box')
    db.dtinymc.insert( f0= 'sx6908', f1= '(6908)App views')
    db.dtinymc.insert( f0= 'sx6910', f1= '(6910)Notifications')
    db.dtinymc.insert( f0= 'sx6912', f1= '(6912)Alerts')
    db.dtinymc.insert( f0= 'sx6914', f1= '(6914)Modals')
    db.dtinymc.insert( f0= 'sx6916', f1= '(6916)Buttons')
    db.dtinymc.insert( f0= 'sx6918', f1= '(6918)Tabs')
    db.dtinymc.insert( f0= 'sx6920', f1= '(6920)Accordion')
    db.dtinymc.insert( f0= 'sx6921', f1= '(6921)Pages')
    db.dtinymc.insert( f0= 'sx6923', f1= '(6923)Login')
    db.dtinymc.insert( f0= 'sx6925', f1= '(6925)Register')
    db.dtinymc.insert( f0= 'sx6927', f1= '(6927)Lock')
    db.dtinymc.insert( f0= 'sx6929', f1= '(6929)Password Recovery')
    db.dtinymc.insert( f0= 'sx6930', f1= '(6930)Landing Page')
    db.dtinymc.insert( f0= 'aa6933', f1= '(6933)Home')
    db.dtinymc.insert( f0= 'aa6934', f1= '(6934)About')
    db.dtinymc.insert( f0= 'aa6935', f1= '(6935)Services')
    db.dtinymc.insert( f0= 'aa6936', f1= '(6936)Support')
    db.dtinymc.insert( f0= 'hh6937', f1= '(6937)Message')
    db.dtinymc.insert( f0= 'sx6939', f1= '(6939)16 Sept')
    db.dtinymc.insert( f0= 'hh6940', f1= '(6940)Advanda Cro')
    db.dtinymc.insert( f0= 'pa6941', f1= '(6941)Please done this project as soon possible.')
    db.dtinymc.insert( f0= 'sx6943', f1= '(6943)16 Sept')
    db.dtinymc.insert( f0= 'hh6944', f1= '(6944)Sulaiman din')
    db.dtinymc.insert( f0= 'pa6945', f1= '(6945)Please done this project as soon possible.')
    db.dtinymc.insert( f0= 'sx6947', f1= '(6947)16 Sept')
    db.dtinymc.insert( f0= 'hh6948', f1= '(6948)Victor Jara')
    db.dtinymc.insert( f0= 'pa6949', f1= '(6949)Please done this project as soon possible.')
    db.dtinymc.insert( f0= 'sx6951', f1= '(6951)16 Sept')
    db.dtinymc.insert( f0= 'hh6952', f1= '(6952)Victor Jara')
    db.dtinymc.insert( f0= 'pa6953', f1= '(6953)Please done this project as soon possible.')
    db.dtinymc.insert( f0= 'aa6954', f1= '(6954)View All Messages')
    db.dtinymc.insert( f0= 'hh6955', f1= '(6955)Notifications')
    db.dtinymc.insert( f0= 'sx6956', f1= '(6956)16 Sept')
    db.dtinymc.insert( f0= 'hh6957', f1= '(6957)Advanda Cro')
    db.dtinymc.insert( f0= 'pa6958', f1= '(6958)Please done this project as soon possible.')
    db.dtinymc.insert( f0= 'sx6959', f1= '(6959)16 Sept')
    db.dtinymc.insert( f0= 'hh6960', f1= '(6960)Sulaiman din')
    db.dtinymc.insert( f0= 'pa6961', f1= '(6961)Please done this project as soon possible.')
    db.dtinymc.insert( f0= 'sx6962', f1= '(6962)16 Sept')
    db.dtinymc.insert( f0= 'hh6963', f1= '(6963)Victor Jara')
    db.dtinymc.insert( f0= 'pa6964', f1= '(6964)Please done this project as soon possible.')
    db.dtinymc.insert( f0= 'sx6965', f1= '(6965)16 Sept')
    db.dtinymc.insert( f0= 'hh6966', f1= '(6966)Victor Jara')
    db.dtinymc.insert( f0= 'pa6967', f1= '(6967)Please done this project as soon possible.')
    db.dtinymc.insert( f0= 'aa6968', f1= '(6968)View All Notification')
    db.dtinymc.insert( f0= 'sx6969', f1= '(6969)Advanda Cro')
    db.dtinymc.insert( f0= 'aa6973', f1= '(6973)News')
    db.dtinymc.insert( f0= 'aa6974', f1= '(6974)Activity')
    db.dtinymc.insert( f0= 'aa6975', f1= '(6975)Settings')
    db.dtinymc.insert( f0= 'pa6976', f1= '(6976)You have 10 New News.')
    db.dtinymc.insert( f0= 'pa6978', f1= '(6978)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtinymc.insert( f0= 'sp6979', f1= '(6979)Yesterday 2:45 pm')
    db.dtinymc.insert( f0= 'pa6981', f1= '(6981)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtinymc.insert( f0= 'sp6982', f1= '(6982)Yesterday 2:45 pm')
    db.dtinymc.insert( f0= 'pa6984', f1= '(6984)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtinymc.insert( f0= 'sp6985', f1= '(6985)Yesterday 2:45 pm')
    db.dtinymc.insert( f0= 'pa6987', f1= '(6987)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtinymc.insert( f0= 'sp6988', f1= '(6988)Yesterday 2:45 pm')
    db.dtinymc.insert( f0= 'pa6990', f1= '(6990)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtinymc.insert( f0= 'sp6991', f1= '(6991)Yesterday 2:45 pm')
    db.dtinymc.insert( f0= 'pa6993', f1= '(6993)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtinymc.insert( f0= 'sp6994', f1= '(6994)Yesterday 2:45 pm')
    db.dtinymc.insert( f0= 'pa6996', f1= '(6996)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtinymc.insert( f0= 'sp6997', f1= '(6997)Yesterday 2:45 pm')
    db.dtinymc.insert( f0= 'pa6999', f1= '(6999)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtinymc.insert( f0= 'sp7000', f1= '(7000)Yesterday 2:45 pm')
    db.dtinymc.insert( f0= 'pa7002', f1= '(7002)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtinymc.insert( f0= 'sp7003', f1= '(7003)Yesterday 2:45 pm')
    db.dtinymc.insert( f0= 'pa7005', f1= '(7005)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtinymc.insert( f0= 'sp7006', f1= '(7006)Yesterday 2:45 pm')
    db.dtinymc.insert( f0= 'pa7007', f1= '(7007)You have 20 Recent Activity.')
    db.dtinymc.insert( f0= 'hh7008', f1= '(7008)New User Registered')
    db.dtinymc.insert( f0= 'pa7009', f1= '(7009)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtinymc.insert( f0= 'sx7010', f1= '(7010)1 hours ago')
    db.dtinymc.insert( f0= 'hh7011', f1= '(7011)New Order Received')
    db.dtinymc.insert( f0= 'pa7012', f1= '(7012)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtinymc.insert( f0= 'sx7013', f1= '(7013)2 hours ago')
    db.dtinymc.insert( f0= 'hh7014', f1= '(7014)New Order Received')
    db.dtinymc.insert( f0= 'pa7015', f1= '(7015)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtinymc.insert( f0= 'sx7016', f1= '(7016)3 hours ago')
    db.dtinymc.insert( f0= 'hh7017', f1= '(7017)New Order Received')
    db.dtinymc.insert( f0= 'pa7018', f1= '(7018)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtinymc.insert( f0= 'sx7019', f1= '(7019)4 hours ago')
    db.dtinymc.insert( f0= 'hh7020', f1= '(7020)New User Registered')
    db.dtinymc.insert( f0= 'pa7021', f1= '(7021)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtinymc.insert( f0= 'sx7022', f1= '(7022)5 hours ago')
    db.dtinymc.insert( f0= 'hh7023', f1= '(7023)New Order')
    db.dtinymc.insert( f0= 'pa7024', f1= '(7024)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtinymc.insert( f0= 'sx7025', f1= '(7025)6 hours ago')
    db.dtinymc.insert( f0= 'hh7026', f1= '(7026)New User')
    db.dtinymc.insert( f0= 'pa7027', f1= '(7027)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtinymc.insert( f0= 'sx7028', f1= '(7028)7 hours ago')
    db.dtinymc.insert( f0= 'hh7029', f1= '(7029)New Order')
    db.dtinymc.insert( f0= 'pa7030', f1= '(7030)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtinymc.insert( f0= 'sx7031', f1= '(7031)9 hours ago')
    db.dtinymc.insert( f0= 'pa7032', f1= '(7032)You have 20 Settings. 5 not completed.')
    db.dtinymc.insert( f0= 'hh7033', f1= '(7033)Show notifications')
    db.dtinymc.insert( f0= 'hh7034', f1= '(7034)Disable Chat')
    db.dtinymc.insert( f0= 'hh7035', f1= '(7035)Enable history')
    db.dtinymc.insert( f0= 'hh7036', f1= '(7036)Show charts')
    db.dtinymc.insert( f0= 'hh7037', f1= '(7037)Update everyday')
    db.dtinymc.insert( f0= 'hh7038', f1= '(7038)Global search')
    db.dtinymc.insert( f0= 'hh7039', f1= '(7039)Offline users')
    db.dtinymc.insert( f0= 'aa7041', f1= '(7041)Dashboard v.1')
    db.dtinymc.insert( f0= 'aa7043', f1= '(7043)Dashboard v.2')
    db.dtinymc.insert( f0= 'aa7045', f1= '(7045)Dashboard v.3')
    db.dtinymc.insert( f0= 'aa7047', f1= '(7047)Product List')
    db.dtinymc.insert( f0= 'aa7049', f1= '(7049)Product Edit')
    db.dtinymc.insert( f0= 'aa7051', f1= '(7051)Product Detail')
    db.dtinymc.insert( f0= 'aa7053', f1= '(7053)Product Cart')
    db.dtinymc.insert( f0= 'aa7055', f1= '(7055)Product Payment')
    db.dtinymc.insert( f0= 'aa7057', f1= '(7057)Analytics')
    db.dtinymc.insert( f0= 'aa7059', f1= '(7059)Widgets')
    db.dtinymc.insert( f0= 'aa7061', f1= '(7061)Inbox')
    db.dtinymc.insert( f0= 'aa7063', f1= '(7063)View Mail')
    db.dtinymc.insert( f0= 'aa7065', f1= '(7065)Compose Mail')
    db.dtinymc.insert( f0= 'aa7067', f1= '(7067)File Manager')
    db.dtinymc.insert( f0= 'aa7069', f1= '(7069)Contacts Client')
    db.dtinymc.insert( f0= 'aa7071', f1= '(7071)Project')
    db.dtinymc.insert( f0= 'aa7073', f1= '(7073)Project Details')
    db.dtinymc.insert( f0= 'aa7075', f1= '(7075)Blog')
    db.dtinymc.insert( f0= 'aa7077', f1= '(7077)Blog Details')
    db.dtinymc.insert( f0= 'aa7079', f1= '(7079)404 Page')
    db.dtinymc.insert( f0= 'aa7081', f1= '(7081)500 Page')
    db.dtinymc.insert( f0= 'aa7083', f1= '(7083)Google Map')
    db.dtinymc.insert( f0= 'aa7085', f1= '(7085)Data Maps')
    db.dtinymc.insert( f0= 'aa7087', f1= '(7087)Pdf Viewer')
    db.dtinymc.insert( f0= 'aa7089', f1= '(7089)X-Editable')
    db.dtinymc.insert( f0= 'aa7091', f1= '(7091)Code Editor')
    db.dtinymc.insert( f0= 'aa7093', f1= '(7093)Tree View')
    db.dtinymc.insert( f0= 'aa7095', f1= '(7095)Preloader')
    db.dtinymc.insert( f0= 'aa7097', f1= '(7097)Images Cropper')
    db.dtinymc.insert( f0= 'aa7099', f1= '(7099)Bar Charts')
    db.dtinymc.insert( f0= 'aa7101', f1= '(7101)Line Charts')
    db.dtinymc.insert( f0= 'aa7103', f1= '(7103)Area Charts')
    db.dtinymc.insert( f0= 'aa7105', f1= '(7105)Rounded Charts')
    db.dtinymc.insert( f0= 'aa7107', f1= '(7107)C3 Charts')
    db.dtinymc.insert( f0= 'aa7109', f1= '(7109)Sparkline Charts')
    db.dtinymc.insert( f0= 'aa7111', f1= '(7111)Peity Charts')
    db.dtinymc.insert( f0= 'aa7113', f1= '(7113)Static Table')
    db.dtinymc.insert( f0= 'aa7115', f1= '(7115)Data Table')
    db.dtinymc.insert( f0= 'aa7117', f1= '(7117)Basic Form Elements')
    db.dtinymc.insert( f0= 'aa7119', f1= '(7119)Advanced Form Elements')
    db.dtinymc.insert( f0= 'aa7121', f1= '(7121)Password Meter')
    db.dtinymc.insert( f0= 'aa7123', f1= '(7123)Multi Upload')
    db.dtinymc.insert( f0= 'aa7125', f1= '(7125)Text Editor')
    db.dtinymc.insert( f0= 'aa7127', f1= '(7127)Dual List Box')
    db.dtinymc.insert( f0= 'aa7129', f1= '(7129)Basic Form Elements')
    db.dtinymc.insert( f0= 'aa7131', f1= '(7131)Advanced Form Elements')
    db.dtinymc.insert( f0= 'aa7133', f1= '(7133)Password Meter')
    db.dtinymc.insert( f0= 'aa7135', f1= '(7135)Multi Upload')
    db.dtinymc.insert( f0= 'aa7137', f1= '(7137)Text Editor')
    db.dtinymc.insert( f0= 'aa7139', f1= '(7139)Dual List Box')
    db.dtinymc.insert( f0= 'aa7141', f1= '(7141)Login')
    db.dtinymc.insert( f0= 'aa7143', f1= '(7143)Register')
    db.dtinymc.insert( f0= 'aa7145', f1= '(7145)Lock')
    db.dtinymc.insert( f0= 'aa7147', f1= '(7147)Password Recovery')
    db.dtinymc.insert( f0= 'pb7148', f1= '(7148)Search...')
    db.dtinymc.insert( f0= 'aa7149', f1= '(7149)Home')
    db.dtinymc.insert( f0= 'sx7150', f1= '(7150)Text Editor')
    db.dtinymc.insert( f0= 'hh7151', f1= '(7151)Basic Summernote WYSIWYG editor')
    db.dtinymc.insert( f0= 'pa7152', f1= '(7152)The fastest way to get Summernote WYSIWYG editor is powerfull JavaScript plugin. you can easily maintance typography system.')
    db.dtinymc.insert( f0= 'hh7153', f1= '(7153)Typography Summernote WYSIWYG editor')
    db.dtinymc.insert( f0= 'pa7154', f1= '(7154)The fastest way to get Summernote WYSIWYG editor is powerfull JavaScript plugin. you can easily maintance typography system.')
    db.dtinymc.insert( f0= 'sx7155', f1= '(7155)Summernote WYSIWYG editor')
    db.dtinymc.insert( f0= 'pc7156', f1= '(7156)The fastest way to get Summernote WYSIWYG editor is powerfull JavaScript plugin. you can easily maintance typography system')
    db.dtinymc.insert( f0= 'sx7158', f1= '(7158)The fastest way to get Summernote WYSIWYG editor is powerfull JavaScript plugin. you can easily maintance typography system')
    db.dtinymc.insert( f0= 'hh7159', f1= '(7159)Table Summernote WYSIWYG editor')
    db.dtinymc.insert( f0= 'pa7160', f1= '(7160)The fastest way to get Summernote WYSIWYG editor is powerfull JavaScript plugin. you can easily maintance typography system.')
    db.dtinymc.insert( f0= 'hh7161', f1= '(7161)Images Summernote WYSIWYG editor')
    db.dtinymc.insert( f0= 'pa7162', f1= '(7162)The fastest way to get Summernote WYSIWYG editor is powerfull JavaScript plugin. you can easily maintance typography system.')
    db.dtinymc.insert( f0= 'hb7163', f1= '(7163)Summernote WYSIWYG editor')
    db.dtinymc.insert( f0= 'sx7165', f1= '(7165)The fastest way to get Summernote WYSIWYG editor is powerfull JavaScript plugin. you can easily maintance typography system.')
    db.dtinymc.insert( f0= 'pc7167', f1= '(7167)All rights reserved.')
    db.dtinymc.insert( f0= 'pf7168', f1= '(7168)Copyright &copy; 2018')
    db.commit()
#
