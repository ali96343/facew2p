#
# table for controller: index_3
#

from gluon.contrib.populate import populate

db.define_table('dindex03', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dindex03.id ).count():
    db.dindex03.insert( f0= 'sp8872', f1= '(8872)outdated')
    db.dindex03.insert( f0= 'pc8873', f1= '(8873)to improve your experience.')
    db.dindex03.insert( f0= 'aa8874', f1= '(8874)upgrade your browser')
    db.dindex03.insert( f0= 'hh8876', f1= '(8876)Messages')
    db.dindex03.insert( f0= 'hh8878', f1= '(8878)David Belle')
    db.dindex03.insert( f0= 'pa8879', f1= '(8879)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dindex03.insert( f0= 'hh8881', f1= '(8881)Jonathan Morris')
    db.dindex03.insert( f0= 'pa8882', f1= '(8882)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dindex03.insert( f0= 'hh8884', f1= '(8884)Fredric Mitchell')
    db.dindex03.insert( f0= 'pa8885', f1= '(8885)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dindex03.insert( f0= 'hh8887', f1= '(8887)David Belle')
    db.dindex03.insert( f0= 'pa8888', f1= '(8888)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dindex03.insert( f0= 'hh8890', f1= '(8890)Glenn Jecobs')
    db.dindex03.insert( f0= 'pa8891', f1= '(8891)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dindex03.insert( f0= 'aa8892', f1= '(8892)View All')
    db.dindex03.insert( f0= 'hh8893', f1= '(8893)Notification')
    db.dindex03.insert( f0= 'hh8895', f1= '(8895)David Belle')
    db.dindex03.insert( f0= 'pa8896', f1= '(8896)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dindex03.insert( f0= 'hh8898', f1= '(8898)Jonathan Morris')
    db.dindex03.insert( f0= 'pa8899', f1= '(8899)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dindex03.insert( f0= 'hh8901', f1= '(8901)Fredric Mitchell')
    db.dindex03.insert( f0= 'pa8902', f1= '(8902)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dindex03.insert( f0= 'hh8904', f1= '(8904)David Belle')
    db.dindex03.insert( f0= 'pa8905', f1= '(8905)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dindex03.insert( f0= 'hh8907', f1= '(8907)Glenn Jecobs')
    db.dindex03.insert( f0= 'pa8908', f1= '(8908)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dindex03.insert( f0= 'aa8909', f1= '(8909)View All')
    db.dindex03.insert( f0= 'hh8910', f1= '(8910)Tasks')
    db.dindex03.insert( f0= 'pa8911', f1= '(8911)HTML5 Validation Report')
    db.dindex03.insert( f0= 'sp8912', f1= '(8912)95%')
    db.dindex03.insert( f0= 'pa8913', f1= '(8913)Google Chrome Extension')
    db.dindex03.insert( f0= 'sp8914', f1= '(8914)85%')
    db.dindex03.insert( f0= 'pa8915', f1= '(8915)Social Internet Projects')
    db.dindex03.insert( f0= 'sp8916', f1= '(8916)75%')
    db.dindex03.insert( f0= 'pa8917', f1= '(8917)Bootstrap Admin')
    db.dindex03.insert( f0= 'sp8918', f1= '(8918)65%')
    db.dindex03.insert( f0= 'pa8919', f1= '(8919)Youtube App')
    db.dindex03.insert( f0= 'sp8920', f1= '(8920)55%')
    db.dindex03.insert( f0= 'aa8921', f1= '(8921)View All')
    db.dindex03.insert( f0= 'hh8922', f1= '(8922)Chat')
    db.dindex03.insert( f0= 'pb8923', f1= '(8923)Search People')
    db.dindex03.insert( f0= 'hh8925', f1= '(8925)David Belle')
    db.dindex03.insert( f0= 'pa8926', f1= '(8926)Available')
    db.dindex03.insert( f0= 'hh8928', f1= '(8928)Jonathan Morris')
    db.dindex03.insert( f0= 'pa8929', f1= '(8929)Last seen 3 hours ago')
    db.dindex03.insert( f0= 'hh8931', f1= '(8931)Fredric Mitchell')
    db.dindex03.insert( f0= 'pa8932', f1= '(8932)Last seen 2 minutes ago')
    db.dindex03.insert( f0= 'hh8934', f1= '(8934)David Belle')
    db.dindex03.insert( f0= 'pa8935', f1= '(8935)Available')
    db.dindex03.insert( f0= 'hh8937', f1= '(8937)Glenn Jecobs')
    db.dindex03.insert( f0= 'pa8938', f1= '(8938)Available')
    db.dindex03.insert( f0= 'aa8939', f1= '(8939)View All')
    db.dindex03.insert( f0= 'aa8940', f1= '(8940)Home')
    db.dindex03.insert( f0= 'aa8942', f1= '(8942)Dashboard One')
    db.dindex03.insert( f0= 'aa8944', f1= '(8944)Dashboard Two')
    db.dindex03.insert( f0= 'aa8946', f1= '(8946)Dashboard Three')
    db.dindex03.insert( f0= 'aa8948', f1= '(8948)Dashboard Four')
    db.dindex03.insert( f0= 'aa8950', f1= '(8950)Analytics')
    db.dindex03.insert( f0= 'aa8952', f1= '(8952)Widgets')
    db.dindex03.insert( f0= 'aa8953', f1= '(8953)Email')
    db.dindex03.insert( f0= 'aa8955', f1= '(8955)Inbox')
    db.dindex03.insert( f0= 'aa8957', f1= '(8957)View Email')
    db.dindex03.insert( f0= 'aa8959', f1= '(8959)Compose Email')
    db.dindex03.insert( f0= 'aa8960', f1= '(8960)Interface')
    db.dindex03.insert( f0= 'aa8962', f1= '(8962)Animations')
    db.dindex03.insert( f0= 'aa8964', f1= '(8964)Google Map')
    db.dindex03.insert( f0= 'aa8966', f1= '(8966)Data Maps')
    db.dindex03.insert( f0= 'aa8968', f1= '(8968)Code Editor')
    db.dindex03.insert( f0= 'aa8970', f1= '(8970)Images Cropper')
    db.dindex03.insert( f0= 'aa8972', f1= '(8972)Wizard')
    db.dindex03.insert( f0= 'aa8973', f1= '(8973)Charts')
    db.dindex03.insert( f0= 'aa8975', f1= '(8975)Flot Charts')
    db.dindex03.insert( f0= 'aa8977', f1= '(8977)Bar Charts')
    db.dindex03.insert( f0= 'aa8979', f1= '(8979)Line Charts')
    db.dindex03.insert( f0= 'aa8981', f1= '(8981)Area Charts')
    db.dindex03.insert( f0= 'aa8982', f1= '(8982)Tables')
    db.dindex03.insert( f0= 'aa8984', f1= '(8984)Normal Table')
    db.dindex03.insert( f0= 'aa8986', f1= '(8986)Data Table')
    db.dindex03.insert( f0= 'aa8987', f1= '(8987)Forms')
    db.dindex03.insert( f0= 'aa8989', f1= '(8989)Form Elements')
    db.dindex03.insert( f0= 'aa8991', f1= '(8991)Form Components')
    db.dindex03.insert( f0= 'aa8993', f1= '(8993)Form Examples')
    db.dindex03.insert( f0= 'aa8994', f1= '(8994)App views')
    db.dindex03.insert( f0= 'aa8996', f1= '(8996)Notifications')
    db.dindex03.insert( f0= 'aa8998', f1= '(8998)Alerts')
    db.dindex03.insert( f0= 'aa9000', f1= '(9000)Modals')
    db.dindex03.insert( f0= 'aa9002', f1= '(9002)Buttons')
    db.dindex03.insert( f0= 'aa9004', f1= '(9004)Tabs')
    db.dindex03.insert( f0= 'aa9006', f1= '(9006)Accordion')
    db.dindex03.insert( f0= 'aa9008', f1= '(9008)Dialogs')
    db.dindex03.insert( f0= 'aa9010', f1= '(9010)Popovers')
    db.dindex03.insert( f0= 'aa9012', f1= '(9012)Tooltips')
    db.dindex03.insert( f0= 'aa9014', f1= '(9014)Dropdowns')
    db.dindex03.insert( f0= 'aa9015', f1= '(9015)Pages')
    db.dindex03.insert( f0= 'aa9017', f1= '(9017)Contact')
    db.dindex03.insert( f0= 'aa9019', f1= '(9019)Invoice')
    db.dindex03.insert( f0= 'aa9021', f1= '(9021)Typography')
    db.dindex03.insert( f0= 'aa9023', f1= '(9023)Color')
    db.dindex03.insert( f0= 'aa9025', f1= '(9025)Login Register')
    db.dindex03.insert( f0= 'aa9027', f1= '(9027)404 Page')
    db.dindex03.insert( f0= 'aa9029', f1= '(9029)Dashboard One')
    db.dindex03.insert( f0= 'aa9031', f1= '(9031)Dashboard Two')
    db.dindex03.insert( f0= 'aa9033', f1= '(9033)Dashboard Three')
    db.dindex03.insert( f0= 'aa9035', f1= '(9035)Dashboard Four')
    db.dindex03.insert( f0= 'aa9037', f1= '(9037)Analytics')
    db.dindex03.insert( f0= 'aa9039', f1= '(9039)Widgets')
    db.dindex03.insert( f0= 'aa9041', f1= '(9041)Inbox')
    db.dindex03.insert( f0= 'aa9043', f1= '(9043)View Email')
    db.dindex03.insert( f0= 'aa9045', f1= '(9045)Compose Email')
    db.dindex03.insert( f0= 'aa9047', f1= '(9047)Animations')
    db.dindex03.insert( f0= 'aa9049', f1= '(9049)Google Map')
    db.dindex03.insert( f0= 'aa9051', f1= '(9051)Data Maps')
    db.dindex03.insert( f0= 'aa9053', f1= '(9053)Code Editor')
    db.dindex03.insert( f0= 'aa9055', f1= '(9055)Images Cropper')
    db.dindex03.insert( f0= 'aa9057', f1= '(9057)Wizard')
    db.dindex03.insert( f0= 'aa9059', f1= '(9059)Flot Charts')
    db.dindex03.insert( f0= 'aa9061', f1= '(9061)Bar Charts')
    db.dindex03.insert( f0= 'aa9063', f1= '(9063)Line Charts')
    db.dindex03.insert( f0= 'aa9065', f1= '(9065)Area Charts')
    db.dindex03.insert( f0= 'aa9067', f1= '(9067)Normal Table')
    db.dindex03.insert( f0= 'aa9069', f1= '(9069)Data Table')
    db.dindex03.insert( f0= 'aa9071', f1= '(9071)Form Elements')
    db.dindex03.insert( f0= 'aa9073', f1= '(9073)Form Components')
    db.dindex03.insert( f0= 'aa9075', f1= '(9075)Form Examples')
    db.dindex03.insert( f0= 'aa9077', f1= '(9077)Notifications')
    db.dindex03.insert( f0= 'aa9079', f1= '(9079)Alerts')
    db.dindex03.insert( f0= 'aa9081', f1= '(9081)Modals')
    db.dindex03.insert( f0= 'aa9083', f1= '(9083)Buttons')
    db.dindex03.insert( f0= 'aa9085', f1= '(9085)Tabs')
    db.dindex03.insert( f0= 'aa9087', f1= '(9087)Accordion')
    db.dindex03.insert( f0= 'aa9089', f1= '(9089)Dialogs')
    db.dindex03.insert( f0= 'aa9091', f1= '(9091)Popovers')
    db.dindex03.insert( f0= 'aa9093', f1= '(9093)Tooltips')
    db.dindex03.insert( f0= 'aa9095', f1= '(9095)Dropdowns')
    db.dindex03.insert( f0= 'aa9097', f1= '(9097)Contact')
    db.dindex03.insert( f0= 'aa9099', f1= '(9099)Invoice')
    db.dindex03.insert( f0= 'aa9101', f1= '(9101)Typography')
    db.dindex03.insert( f0= 'aa9103', f1= '(9103)Color')
    db.dindex03.insert( f0= 'aa9105', f1= '(9105)Login Register')
    db.dindex03.insert( f0= 'aa9107', f1= '(9107)404 Page')
    db.dindex03.insert( f0= 'pa9108', f1= '(9108)Website Impressions')
    db.dindex03.insert( f0= 'pa9109', f1= '(9109)Total Support Tickets')
    db.dindex03.insert( f0= 'hh9110', f1= '(9110)Sales Statistics')
    db.dindex03.insert( f0= 'pa9111', f1= '(9111)Vestibulum purus quam scelerisque, mollis nonummy metus')
    db.dindex03.insert( f0= 'hh9112', f1= '(9112)For The Past 30 Days')
    db.dindex03.insert( f0= 'pa9113', f1= '(9113)Fusce eget dolor id justo luctus the commodo vel pharetra nisi. Donec velit of libero.')
    db.dindex03.insert( f0= 'pa9114', f1= '(9114)Page Views')
    db.dindex03.insert( f0= 'pa9115', f1= '(9115)Total Clicks')
    db.dindex03.insert( f0= 'pa9117', f1= '(9117)Site Visitors')
    db.dindex03.insert( f0= 'hh9118', f1= '(9118)Email Statistics')
    db.dindex03.insert( f0= 'pa9119', f1= '(9119)Total Emails Sent')
    db.dindex03.insert( f0= 'pa9120', f1= '(9120)Bounce Rate')
    db.dindex03.insert( f0= 'pa9121', f1= '(9121)Total Opened')
    db.dindex03.insert( f0= 'pa9122', f1= '(9122)Total Ignored')
    db.dindex03.insert( f0= 'hh9123', f1= '(9123)Recent Posts')
    db.dindex03.insert( f0= 'hh9125', f1= '(9125)Smith')
    db.dindex03.insert( f0= 'pa9126', f1= '(9126)Nunc quis diam diamurabitur at dolor elementum, dictum turpis vel')
    db.dindex03.insert( f0= 'hh9128', f1= '(9128)John Deo')
    db.dindex03.insert( f0= 'pa9129', f1= '(9129)Nunc quis diam diamurabitur at dolor elementum, dictum turpis vel')
    db.dindex03.insert( f0= 'hh9131', f1= '(9131)Malika')
    db.dindex03.insert( f0= 'pa9132', f1= '(9132)Nunc quis diam diamurabitur at dolor elementum, dictum turpis vel')
    db.dindex03.insert( f0= 'hh9134', f1= '(9134)Smith')
    db.dindex03.insert( f0= 'pa9135', f1= '(9135)Nunc quis diam diamurabitur at dolor elementum, dictum turpis vel')
    db.dindex03.insert( f0= 'hh9137', f1= '(9137)John Deo')
    db.dindex03.insert( f0= 'pa9138', f1= '(9138)Nunc quis diam diamurabitur at dolor elementum, dictum turpis vel')
    db.dindex03.insert( f0= 'pa9139', f1= '(9139)View All')
    db.dindex03.insert( f0= 'hh9140', f1= '(9140)Recent Items')
    db.dindex03.insert( f0= 'hh9141', f1= '(9141)Realtime Visitors')
    db.dindex03.insert( f0= 'pa9142', f1= '(9142)Visitors last 24h')
    db.dindex03.insert( f0= 'pa9143', f1= '(9143)Visitors last 30m')
    db.dindex03.insert( f0= 'hh9144', f1= '(9144)September 4, 21:44:02 (2 Mins 56 Seconds)')
    db.dindex03.insert( f0= 'sp9146', f1= '(9146)United States')
    db.dindex03.insert( f0= 'sp9147', f1= '(9147)Firefox')
    db.dindex03.insert( f0= 'sp9148', f1= '(9148)Mac OSX')
    db.dindex03.insert( f0= 'hh9149', f1= '(9149)September 7, 20:44:02 (5 Mins 56 Seconds)')
    db.dindex03.insert( f0= 'sp9151', f1= '(9151)Australia')
    db.dindex03.insert( f0= 'sp9152', f1= '(9152)Firefox')
    db.dindex03.insert( f0= 'sp9153', f1= '(9153)Mac OSX')
    db.dindex03.insert( f0= 'hh9154', f1= '(9154)September 9, 19:44:02 (10 Mins 56 Seconds)')
    db.dindex03.insert( f0= 'sp9156', f1= '(9156)Brazil')
    db.dindex03.insert( f0= 'sp9157', f1= '(9157)Firefox')
    db.dindex03.insert( f0= 'sp9158', f1= '(9158)Mac OSX')
    db.dindex03.insert( f0= 'hh9159', f1= '(9159)Add Todo')
    db.dindex03.insert( f0= 'aa9160', f1= '(9160)Archive')
    db.dindex03.insert( f0= 'pb9161', f1= '(9161)Add new todo')
    db.dindex03.insert( f0= 'bu9162', f1= '(9162)Add')
    db.dindex03.insert( f0= 'hh9163', f1= '(9163)Chat Box')
    db.dindex03.insert( f0= 'ii9165', f1= '(9165)10:00')
    db.dindex03.insert( f0= 'ii9166', f1= '(9166)John Deo')
    db.dindex03.insert( f0= 'ii9168', f1= '(9168)10:01')
    db.dindex03.insert( f0= 'ii9169', f1= '(9169)Smith')
    db.dindex03.insert( f0= 'ii9171', f1= '(9171)10:01')
    db.dindex03.insert( f0= 'ii9172', f1= '(9172)John Deo')
    db.dindex03.insert( f0= 'ii9174', f1= '(9174)10:02')
    db.dindex03.insert( f0= 'ii9175', f1= '(9175)Smith')
    db.dindex03.insert( f0= 'ii9177', f1= '(9177)10:01')
    db.dindex03.insert( f0= 'ii9178', f1= '(9178)John Deo')
    db.dindex03.insert( f0= 'ii9180', f1= '(9180)10:02')
    db.dindex03.insert( f0= 'ii9181', f1= '(9181)Smith')
    db.dindex03.insert( f0= 'pb9182', f1= '(9182)Enter your text')
    db.dindex03.insert( f0= 'bu9183', f1= '(9183)Send')
    db.commit()
#
