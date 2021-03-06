#
# table for controller: blog
#

from gluon.contrib.populate import populate

db.define_table('dblog', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dblog.id ).count():
    db.dblog.insert( f0= 'sp18524', f1= '(18524)outdated')
    db.dblog.insert( f0= 'pc18525', f1= '(18525)to improve your experience.')
    db.dblog.insert( f0= 'aa18526', f1= '(18526)upgrade your browser')
    db.dblog.insert( f0= 'sx18531', f1= '(18531)Ecommerce')
    db.dblog.insert( f0= 'sx18533', f1= '(18533)Dashboard v.1')
    db.dblog.insert( f0= 'sx18535', f1= '(18535)Dashboard v.2')
    db.dblog.insert( f0= 'sx18537', f1= '(18537)Dashboard v.3')
    db.dblog.insert( f0= 'sx18539', f1= '(18539)Product List')
    db.dblog.insert( f0= 'sx18541', f1= '(18541)Product Edit')
    db.dblog.insert( f0= 'sx18543', f1= '(18543)Product Detail')
    db.dblog.insert( f0= 'sx18545', f1= '(18545)Product Cart')
    db.dblog.insert( f0= 'sx18547', f1= '(18547)Product Payment')
    db.dblog.insert( f0= 'sx18549', f1= '(18549)Analytics')
    db.dblog.insert( f0= 'sx18551', f1= '(18551)Widgets')
    db.dblog.insert( f0= 'sx18553', f1= '(18553)Mailbox')
    db.dblog.insert( f0= 'sx18555', f1= '(18555)Inbox')
    db.dblog.insert( f0= 'sx18557', f1= '(18557)View Mail')
    db.dblog.insert( f0= 'sx18559', f1= '(18559)Compose Mail')
    db.dblog.insert( f0= 'sx18561', f1= '(18561)Interface')
    db.dblog.insert( f0= 'sx18563', f1= '(18563)Google Map')
    db.dblog.insert( f0= 'sx18565', f1= '(18565)Data Maps')
    db.dblog.insert( f0= 'sx18567', f1= '(18567)Pdf Viewer')
    db.dblog.insert( f0= 'sx18569', f1= '(18569)X-Editable')
    db.dblog.insert( f0= 'sx18571', f1= '(18571)Code Editor')
    db.dblog.insert( f0= 'sx18573', f1= '(18573)Tree View')
    db.dblog.insert( f0= 'sx18575', f1= '(18575)Preloader')
    db.dblog.insert( f0= 'sx18577', f1= '(18577)Images Cropper')
    db.dblog.insert( f0= 'sx18579', f1= '(18579)Miscellaneous')
    db.dblog.insert( f0= 'sx18581', f1= '(18581)File Manager')
    db.dblog.insert( f0= 'sx18583', f1= '(18583)Blog')
    db.dblog.insert( f0= 'sx18585', f1= '(18585)Blog Details')
    db.dblog.insert( f0= 'sx18587', f1= '(18587)404 Page')
    db.dblog.insert( f0= 'sx18589', f1= '(18589)500 Page')
    db.dblog.insert( f0= 'sx18591', f1= '(18591)Charts')
    db.dblog.insert( f0= 'sx18593', f1= '(18593)Bar Charts')
    db.dblog.insert( f0= 'sx18595', f1= '(18595)Line Charts')
    db.dblog.insert( f0= 'sx18597', f1= '(18597)Area Charts')
    db.dblog.insert( f0= 'sx18599', f1= '(18599)Rounded Charts')
    db.dblog.insert( f0= 'sx18601', f1= '(18601)C3 Charts')
    db.dblog.insert( f0= 'sx18603', f1= '(18603)Sparkline Charts')
    db.dblog.insert( f0= 'sx18605', f1= '(18605)Peity Charts')
    db.dblog.insert( f0= 'sx18607', f1= '(18607)Data Tables')
    db.dblog.insert( f0= 'sx18609', f1= '(18609)Static Table')
    db.dblog.insert( f0= 'sx18611', f1= '(18611)Data Table')
    db.dblog.insert( f0= 'sx18613', f1= '(18613)Forms Elements')
    db.dblog.insert( f0= 'sx18615', f1= '(18615)Bc Form Elements')
    db.dblog.insert( f0= 'sx18617', f1= '(18617)Ad Form Elements')
    db.dblog.insert( f0= 'sx18619', f1= '(18619)Password Meter')
    db.dblog.insert( f0= 'sx18621', f1= '(18621)Multi Upload')
    db.dblog.insert( f0= 'sx18623', f1= '(18623)Text Editor')
    db.dblog.insert( f0= 'sx18625', f1= '(18625)Dual List Box')
    db.dblog.insert( f0= 'sx18627', f1= '(18627)App views')
    db.dblog.insert( f0= 'sx18629', f1= '(18629)Notifications')
    db.dblog.insert( f0= 'sx18631', f1= '(18631)Alerts')
    db.dblog.insert( f0= 'sx18633', f1= '(18633)Modals')
    db.dblog.insert( f0= 'sx18635', f1= '(18635)Buttons')
    db.dblog.insert( f0= 'sx18637', f1= '(18637)Tabs')
    db.dblog.insert( f0= 'sx18639', f1= '(18639)Accordion')
    db.dblog.insert( f0= 'sx18640', f1= '(18640)Pages')
    db.dblog.insert( f0= 'sx18642', f1= '(18642)Login')
    db.dblog.insert( f0= 'sx18644', f1= '(18644)Register')
    db.dblog.insert( f0= 'sx18646', f1= '(18646)Lock')
    db.dblog.insert( f0= 'sx18648', f1= '(18648)Password Recovery')
    db.dblog.insert( f0= 'sx18649', f1= '(18649)Landing Page')
    db.dblog.insert( f0= 'aa18652', f1= '(18652)Home')
    db.dblog.insert( f0= 'aa18653', f1= '(18653)About')
    db.dblog.insert( f0= 'aa18654', f1= '(18654)Services')
    db.dblog.insert( f0= 'aa18655', f1= '(18655)Support')
    db.dblog.insert( f0= 'hh18656', f1= '(18656)Message')
    db.dblog.insert( f0= 'sx18658', f1= '(18658)16 Sept')
    db.dblog.insert( f0= 'hh18659', f1= '(18659)Advanda Cro')
    db.dblog.insert( f0= 'pa18660', f1= '(18660)Please done this project as soon possible.')
    db.dblog.insert( f0= 'sx18662', f1= '(18662)16 Sept')
    db.dblog.insert( f0= 'hh18663', f1= '(18663)Sulaiman din')
    db.dblog.insert( f0= 'pa18664', f1= '(18664)Please done this project as soon possible.')
    db.dblog.insert( f0= 'sx18666', f1= '(18666)16 Sept')
    db.dblog.insert( f0= 'hh18667', f1= '(18667)Victor Jara')
    db.dblog.insert( f0= 'pa18668', f1= '(18668)Please done this project as soon possible.')
    db.dblog.insert( f0= 'sx18670', f1= '(18670)16 Sept')
    db.dblog.insert( f0= 'hh18671', f1= '(18671)Victor Jara')
    db.dblog.insert( f0= 'pa18672', f1= '(18672)Please done this project as soon possible.')
    db.dblog.insert( f0= 'aa18673', f1= '(18673)View All Messages')
    db.dblog.insert( f0= 'hh18674', f1= '(18674)Notifications')
    db.dblog.insert( f0= 'sx18675', f1= '(18675)16 Sept')
    db.dblog.insert( f0= 'hh18676', f1= '(18676)Advanda Cro')
    db.dblog.insert( f0= 'pa18677', f1= '(18677)Please done this project as soon possible.')
    db.dblog.insert( f0= 'sx18678', f1= '(18678)16 Sept')
    db.dblog.insert( f0= 'hh18679', f1= '(18679)Sulaiman din')
    db.dblog.insert( f0= 'pa18680', f1= '(18680)Please done this project as soon possible.')
    db.dblog.insert( f0= 'sx18681', f1= '(18681)16 Sept')
    db.dblog.insert( f0= 'hh18682', f1= '(18682)Victor Jara')
    db.dblog.insert( f0= 'pa18683', f1= '(18683)Please done this project as soon possible.')
    db.dblog.insert( f0= 'sx18684', f1= '(18684)16 Sept')
    db.dblog.insert( f0= 'hh18685', f1= '(18685)Victor Jara')
    db.dblog.insert( f0= 'pa18686', f1= '(18686)Please done this project as soon possible.')
    db.dblog.insert( f0= 'aa18687', f1= '(18687)View All Notification')
    db.dblog.insert( f0= 'sx18688', f1= '(18688)Advanda Cro')
    db.dblog.insert( f0= 'aa18692', f1= '(18692)News')
    db.dblog.insert( f0= 'aa18693', f1= '(18693)Activity')
    db.dblog.insert( f0= 'aa18694', f1= '(18694)Settings')
    db.dblog.insert( f0= 'pa18695', f1= '(18695)You have 10 New News.')
    db.dblog.insert( f0= 'pa18697', f1= '(18697)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dblog.insert( f0= 'sp18698', f1= '(18698)Yesterday 2:45 pm')
    db.dblog.insert( f0= 'pa18700', f1= '(18700)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dblog.insert( f0= 'sp18701', f1= '(18701)Yesterday 2:45 pm')
    db.dblog.insert( f0= 'pa18703', f1= '(18703)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dblog.insert( f0= 'sp18704', f1= '(18704)Yesterday 2:45 pm')
    db.dblog.insert( f0= 'pa18706', f1= '(18706)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dblog.insert( f0= 'sp18707', f1= '(18707)Yesterday 2:45 pm')
    db.dblog.insert( f0= 'pa18709', f1= '(18709)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dblog.insert( f0= 'sp18710', f1= '(18710)Yesterday 2:45 pm')
    db.dblog.insert( f0= 'pa18712', f1= '(18712)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dblog.insert( f0= 'sp18713', f1= '(18713)Yesterday 2:45 pm')
    db.dblog.insert( f0= 'pa18715', f1= '(18715)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dblog.insert( f0= 'sp18716', f1= '(18716)Yesterday 2:45 pm')
    db.dblog.insert( f0= 'pa18718', f1= '(18718)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dblog.insert( f0= 'sp18719', f1= '(18719)Yesterday 2:45 pm')
    db.dblog.insert( f0= 'pa18721', f1= '(18721)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dblog.insert( f0= 'sp18722', f1= '(18722)Yesterday 2:45 pm')
    db.dblog.insert( f0= 'pa18724', f1= '(18724)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dblog.insert( f0= 'sp18725', f1= '(18725)Yesterday 2:45 pm')
    db.dblog.insert( f0= 'pa18726', f1= '(18726)You have 20 Recent Activity.')
    db.dblog.insert( f0= 'hh18727', f1= '(18727)New User Registered')
    db.dblog.insert( f0= 'pa18728', f1= '(18728)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dblog.insert( f0= 'sx18729', f1= '(18729)1 hours ago')
    db.dblog.insert( f0= 'hh18730', f1= '(18730)New Order Received')
    db.dblog.insert( f0= 'pa18731', f1= '(18731)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dblog.insert( f0= 'sx18732', f1= '(18732)2 hours ago')
    db.dblog.insert( f0= 'hh18733', f1= '(18733)New Order Received')
    db.dblog.insert( f0= 'pa18734', f1= '(18734)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dblog.insert( f0= 'sx18735', f1= '(18735)3 hours ago')
    db.dblog.insert( f0= 'hh18736', f1= '(18736)New Order Received')
    db.dblog.insert( f0= 'pa18737', f1= '(18737)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dblog.insert( f0= 'sx18738', f1= '(18738)4 hours ago')
    db.dblog.insert( f0= 'hh18739', f1= '(18739)New User Registered')
    db.dblog.insert( f0= 'pa18740', f1= '(18740)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dblog.insert( f0= 'sx18741', f1= '(18741)5 hours ago')
    db.dblog.insert( f0= 'hh18742', f1= '(18742)New Order')
    db.dblog.insert( f0= 'pa18743', f1= '(18743)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dblog.insert( f0= 'sx18744', f1= '(18744)6 hours ago')
    db.dblog.insert( f0= 'hh18745', f1= '(18745)New User')
    db.dblog.insert( f0= 'pa18746', f1= '(18746)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dblog.insert( f0= 'sx18747', f1= '(18747)7 hours ago')
    db.dblog.insert( f0= 'hh18748', f1= '(18748)New Order')
    db.dblog.insert( f0= 'pa18749', f1= '(18749)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dblog.insert( f0= 'sx18750', f1= '(18750)9 hours ago')
    db.dblog.insert( f0= 'pa18751', f1= '(18751)You have 20 Settings. 5 not completed.')
    db.dblog.insert( f0= 'hh18752', f1= '(18752)Show notifications')
    db.dblog.insert( f0= 'hh18753', f1= '(18753)Disable Chat')
    db.dblog.insert( f0= 'hh18754', f1= '(18754)Enable history')
    db.dblog.insert( f0= 'hh18755', f1= '(18755)Show charts')
    db.dblog.insert( f0= 'hh18756', f1= '(18756)Update everyday')
    db.dblog.insert( f0= 'hh18757', f1= '(18757)Global search')
    db.dblog.insert( f0= 'hh18758', f1= '(18758)Offline users')
    db.dblog.insert( f0= 'aa18760', f1= '(18760)Dashboard v.1')
    db.dblog.insert( f0= 'aa18762', f1= '(18762)Dashboard v.2')
    db.dblog.insert( f0= 'aa18764', f1= '(18764)Dashboard v.3')
    db.dblog.insert( f0= 'aa18766', f1= '(18766)Product List')
    db.dblog.insert( f0= 'aa18768', f1= '(18768)Product Edit')
    db.dblog.insert( f0= 'aa18770', f1= '(18770)Product Detail')
    db.dblog.insert( f0= 'aa18772', f1= '(18772)Product Cart')
    db.dblog.insert( f0= 'aa18774', f1= '(18774)Product Payment')
    db.dblog.insert( f0= 'aa18776', f1= '(18776)Analytics')
    db.dblog.insert( f0= 'aa18778', f1= '(18778)Widgets')
    db.dblog.insert( f0= 'aa18780', f1= '(18780)Inbox')
    db.dblog.insert( f0= 'aa18782', f1= '(18782)View Mail')
    db.dblog.insert( f0= 'aa18784', f1= '(18784)Compose Mail')
    db.dblog.insert( f0= 'aa18786', f1= '(18786)File Manager')
    db.dblog.insert( f0= 'aa18788', f1= '(18788)Contacts Client')
    db.dblog.insert( f0= 'aa18790', f1= '(18790)Project')
    db.dblog.insert( f0= 'aa18792', f1= '(18792)Project Details')
    db.dblog.insert( f0= 'aa18794', f1= '(18794)Blog')
    db.dblog.insert( f0= 'aa18796', f1= '(18796)Blog Details')
    db.dblog.insert( f0= 'aa18798', f1= '(18798)404 Page')
    db.dblog.insert( f0= 'aa18800', f1= '(18800)500 Page')
    db.dblog.insert( f0= 'aa18802', f1= '(18802)Google Map')
    db.dblog.insert( f0= 'aa18804', f1= '(18804)Data Maps')
    db.dblog.insert( f0= 'aa18806', f1= '(18806)Pdf Viewer')
    db.dblog.insert( f0= 'aa18808', f1= '(18808)X-Editable')
    db.dblog.insert( f0= 'aa18810', f1= '(18810)Code Editor')
    db.dblog.insert( f0= 'aa18812', f1= '(18812)Tree View')
    db.dblog.insert( f0= 'aa18814', f1= '(18814)Preloader')
    db.dblog.insert( f0= 'aa18816', f1= '(18816)Images Cropper')
    db.dblog.insert( f0= 'aa18818', f1= '(18818)Bar Charts')
    db.dblog.insert( f0= 'aa18820', f1= '(18820)Line Charts')
    db.dblog.insert( f0= 'aa18822', f1= '(18822)Area Charts')
    db.dblog.insert( f0= 'aa18824', f1= '(18824)Rounded Charts')
    db.dblog.insert( f0= 'aa18826', f1= '(18826)C3 Charts')
    db.dblog.insert( f0= 'aa18828', f1= '(18828)Sparkline Charts')
    db.dblog.insert( f0= 'aa18830', f1= '(18830)Peity Charts')
    db.dblog.insert( f0= 'aa18832', f1= '(18832)Static Table')
    db.dblog.insert( f0= 'aa18834', f1= '(18834)Data Table')
    db.dblog.insert( f0= 'aa18836', f1= '(18836)Basic Form Elements')
    db.dblog.insert( f0= 'aa18838', f1= '(18838)Advanced Form Elements')
    db.dblog.insert( f0= 'aa18840', f1= '(18840)Password Meter')
    db.dblog.insert( f0= 'aa18842', f1= '(18842)Multi Upload')
    db.dblog.insert( f0= 'aa18844', f1= '(18844)Text Editor')
    db.dblog.insert( f0= 'aa18846', f1= '(18846)Dual List Box')
    db.dblog.insert( f0= 'aa18848', f1= '(18848)Basic Form Elements')
    db.dblog.insert( f0= 'aa18850', f1= '(18850)Advanced Form Elements')
    db.dblog.insert( f0= 'aa18852', f1= '(18852)Password Meter')
    db.dblog.insert( f0= 'aa18854', f1= '(18854)Multi Upload')
    db.dblog.insert( f0= 'aa18856', f1= '(18856)Text Editor')
    db.dblog.insert( f0= 'aa18858', f1= '(18858)Dual List Box')
    db.dblog.insert( f0= 'aa18860', f1= '(18860)Login')
    db.dblog.insert( f0= 'aa18862', f1= '(18862)Register')
    db.dblog.insert( f0= 'aa18864', f1= '(18864)Lock')
    db.dblog.insert( f0= 'aa18866', f1= '(18866)Password Recovery')
    db.dblog.insert( f0= 'pb18867', f1= '(18867)Search...')
    db.dblog.insert( f0= 'aa18868', f1= '(18868)Home')
    db.dblog.insert( f0= 'sx18869', f1= '(18869)Blog')
    db.dblog.insert( f0= 'sx18871', f1= '(18871)Smith')
    db.dblog.insert( f0= 'pf18872', f1= '(18872)Created by:')
    db.dblog.insert( f0= 'pc18873', f1= '(18873)21.03.2015')
    db.dblog.insert( f0= 'hh18875', f1= '(18875)TIPS FOR BEAUTY')
    db.dblog.insert( f0= 'sx18876', f1= '(18876)22 comments')
    db.dblog.insert( f0= 'sx18878', f1= '(18878)Smith')
    db.dblog.insert( f0= 'pf18879', f1= '(18879)Created by:')
    db.dblog.insert( f0= 'pc18880', f1= '(18880)21.03.2015')
    db.dblog.insert( f0= 'hh18882', f1= '(18882)TIPS FOR BEAUTY')
    db.dblog.insert( f0= 'sx18883', f1= '(18883)22 comments')
    db.dblog.insert( f0= 'sx18885', f1= '(18885)Smith')
    db.dblog.insert( f0= 'pf18886', f1= '(18886)Created by:')
    db.dblog.insert( f0= 'pc18887', f1= '(18887)21.03.2015')
    db.dblog.insert( f0= 'hh18889', f1= '(18889)TIPS FOR BEAUTY')
    db.dblog.insert( f0= 'sx18890', f1= '(18890)22 comments')
    db.dblog.insert( f0= 'sx18892', f1= '(18892)Smith')
    db.dblog.insert( f0= 'pf18893', f1= '(18893)Created by:')
    db.dblog.insert( f0= 'pc18894', f1= '(18894)21.03.2015')
    db.dblog.insert( f0= 'hh18896', f1= '(18896)TIPS FOR BEAUTY')
    db.dblog.insert( f0= 'sx18897', f1= '(18897)22 comments')
    db.dblog.insert( f0= 'sx18899', f1= '(18899)Smith')
    db.dblog.insert( f0= 'pf18900', f1= '(18900)Created by:')
    db.dblog.insert( f0= 'pc18901', f1= '(18901)21.03.2015')
    db.dblog.insert( f0= 'hh18904', f1= '(18904)TIPS FOR BEAUTY')
    db.dblog.insert( f0= 'sx18905', f1= '(18905)22 comments')
    db.dblog.insert( f0= 'sx18907', f1= '(18907)Smith')
    db.dblog.insert( f0= 'pf18908', f1= '(18908)Created by:')
    db.dblog.insert( f0= 'pc18909', f1= '(18909)21.03.2015')
    db.dblog.insert( f0= 'hh18912', f1= '(18912)TIPS FOR BEAUTY')
    db.dblog.insert( f0= 'sx18913', f1= '(18913)22 comments')
    db.dblog.insert( f0= 'sx18915', f1= '(18915)Smith')
    db.dblog.insert( f0= 'pf18916', f1= '(18916)Created by:')
    db.dblog.insert( f0= 'pc18917', f1= '(18917)21.03.2015')
    db.dblog.insert( f0= 'hh18920', f1= '(18920)TIPS FOR BEAUTY')
    db.dblog.insert( f0= 'sx18921', f1= '(18921)22 comments')
    db.dblog.insert( f0= 'sx18923', f1= '(18923)Smith')
    db.dblog.insert( f0= 'pf18924', f1= '(18924)Created by:')
    db.dblog.insert( f0= 'pc18925', f1= '(18925)21.03.2015')
    db.dblog.insert( f0= 'hh18928', f1= '(18928)TIPS FOR BEAUTY')
    db.dblog.insert( f0= 'sx18929', f1= '(18929)22 comments')
    db.dblog.insert( f0= 'pc18930', f1= '(18930)All rights reserved.')
    db.dblog.insert( f0= 'pf18931', f1= '(18931)Copyright  2018')
    db.commit()
#
