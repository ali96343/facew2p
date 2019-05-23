#
# table for controller: data_maps
#

from gluon.contrib.populate import populate

db.define_table('ddata0maps', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.ddata0maps.id ).count():
    db.ddata0maps.insert( f0= 'sp10669', f1= '(10669)outdated')
    db.ddata0maps.insert( f0= 'pc10670', f1= '(10670)to improve your experience.')
    db.ddata0maps.insert( f0= 'aa10671', f1= '(10671)upgrade your browser')
    db.ddata0maps.insert( f0= 'sx10676', f1= '(10676)Ecommerce')
    db.ddata0maps.insert( f0= 'sx10678', f1= '(10678)Dashboard v.1')
    db.ddata0maps.insert( f0= 'sx10680', f1= '(10680)Dashboard v.2')
    db.ddata0maps.insert( f0= 'sx10682', f1= '(10682)Dashboard v.3')
    db.ddata0maps.insert( f0= 'sx10684', f1= '(10684)Product List')
    db.ddata0maps.insert( f0= 'sx10686', f1= '(10686)Product Edit')
    db.ddata0maps.insert( f0= 'sx10688', f1= '(10688)Product Detail')
    db.ddata0maps.insert( f0= 'sx10690', f1= '(10690)Product Cart')
    db.ddata0maps.insert( f0= 'sx10692', f1= '(10692)Product Payment')
    db.ddata0maps.insert( f0= 'sx10694', f1= '(10694)Analytics')
    db.ddata0maps.insert( f0= 'sx10696', f1= '(10696)Widgets')
    db.ddata0maps.insert( f0= 'sx10698', f1= '(10698)Mailbox')
    db.ddata0maps.insert( f0= 'sx10700', f1= '(10700)Inbox')
    db.ddata0maps.insert( f0= 'sx10702', f1= '(10702)View Mail')
    db.ddata0maps.insert( f0= 'sx10704', f1= '(10704)Compose Mail')
    db.ddata0maps.insert( f0= 'sx10706', f1= '(10706)Interface')
    db.ddata0maps.insert( f0= 'sx10708', f1= '(10708)Google Map')
    db.ddata0maps.insert( f0= 'sx10710', f1= '(10710)Data Maps')
    db.ddata0maps.insert( f0= 'sx10712', f1= '(10712)Pdf Viewer')
    db.ddata0maps.insert( f0= 'sx10714', f1= '(10714)X-Editable')
    db.ddata0maps.insert( f0= 'sx10716', f1= '(10716)Code Editor')
    db.ddata0maps.insert( f0= 'sx10718', f1= '(10718)Tree View')
    db.ddata0maps.insert( f0= 'sx10720', f1= '(10720)Preloader')
    db.ddata0maps.insert( f0= 'sx10722', f1= '(10722)Images Cropper')
    db.ddata0maps.insert( f0= 'sx10724', f1= '(10724)Miscellaneous')
    db.ddata0maps.insert( f0= 'sx10726', f1= '(10726)File Manager')
    db.ddata0maps.insert( f0= 'sx10728', f1= '(10728)Blog')
    db.ddata0maps.insert( f0= 'sx10730', f1= '(10730)Blog Details')
    db.ddata0maps.insert( f0= 'sx10732', f1= '(10732)404 Page')
    db.ddata0maps.insert( f0= 'sx10734', f1= '(10734)500 Page')
    db.ddata0maps.insert( f0= 'sx10736', f1= '(10736)Charts')
    db.ddata0maps.insert( f0= 'sx10738', f1= '(10738)Bar Charts')
    db.ddata0maps.insert( f0= 'sx10740', f1= '(10740)Line Charts')
    db.ddata0maps.insert( f0= 'sx10742', f1= '(10742)Area Charts')
    db.ddata0maps.insert( f0= 'sx10744', f1= '(10744)Rounded Charts')
    db.ddata0maps.insert( f0= 'sx10746', f1= '(10746)C3 Charts')
    db.ddata0maps.insert( f0= 'sx10748', f1= '(10748)Sparkline Charts')
    db.ddata0maps.insert( f0= 'sx10750', f1= '(10750)Peity Charts')
    db.ddata0maps.insert( f0= 'sx10752', f1= '(10752)Data Tables')
    db.ddata0maps.insert( f0= 'sx10754', f1= '(10754)Static Table')
    db.ddata0maps.insert( f0= 'sx10756', f1= '(10756)Data Table')
    db.ddata0maps.insert( f0= 'sx10758', f1= '(10758)Forms Elements')
    db.ddata0maps.insert( f0= 'sx10760', f1= '(10760)Bc Form Elements')
    db.ddata0maps.insert( f0= 'sx10762', f1= '(10762)Ad Form Elements')
    db.ddata0maps.insert( f0= 'sx10764', f1= '(10764)Password Meter')
    db.ddata0maps.insert( f0= 'sx10766', f1= '(10766)Multi Upload')
    db.ddata0maps.insert( f0= 'sx10768', f1= '(10768)Text Editor')
    db.ddata0maps.insert( f0= 'sx10770', f1= '(10770)Dual List Box')
    db.ddata0maps.insert( f0= 'sx10772', f1= '(10772)App views')
    db.ddata0maps.insert( f0= 'sx10774', f1= '(10774)Notifications')
    db.ddata0maps.insert( f0= 'sx10776', f1= '(10776)Alerts')
    db.ddata0maps.insert( f0= 'sx10778', f1= '(10778)Modals')
    db.ddata0maps.insert( f0= 'sx10780', f1= '(10780)Buttons')
    db.ddata0maps.insert( f0= 'sx10782', f1= '(10782)Tabs')
    db.ddata0maps.insert( f0= 'sx10784', f1= '(10784)Accordion')
    db.ddata0maps.insert( f0= 'sx10785', f1= '(10785)Pages')
    db.ddata0maps.insert( f0= 'sx10787', f1= '(10787)Login')
    db.ddata0maps.insert( f0= 'sx10789', f1= '(10789)Register')
    db.ddata0maps.insert( f0= 'sx10791', f1= '(10791)Lock')
    db.ddata0maps.insert( f0= 'sx10793', f1= '(10793)Password Recovery')
    db.ddata0maps.insert( f0= 'sx10794', f1= '(10794)Landing Page')
    db.ddata0maps.insert( f0= 'aa10797', f1= '(10797)Home')
    db.ddata0maps.insert( f0= 'aa10798', f1= '(10798)About')
    db.ddata0maps.insert( f0= 'aa10799', f1= '(10799)Services')
    db.ddata0maps.insert( f0= 'aa10800', f1= '(10800)Support')
    db.ddata0maps.insert( f0= 'hh10801', f1= '(10801)Message')
    db.ddata0maps.insert( f0= 'sx10803', f1= '(10803)16 Sept')
    db.ddata0maps.insert( f0= 'hh10804', f1= '(10804)Advanda Cro')
    db.ddata0maps.insert( f0= 'pa10805', f1= '(10805)Please done this project as soon possible.')
    db.ddata0maps.insert( f0= 'sx10807', f1= '(10807)16 Sept')
    db.ddata0maps.insert( f0= 'hh10808', f1= '(10808)Sulaiman din')
    db.ddata0maps.insert( f0= 'pa10809', f1= '(10809)Please done this project as soon possible.')
    db.ddata0maps.insert( f0= 'sx10811', f1= '(10811)16 Sept')
    db.ddata0maps.insert( f0= 'hh10812', f1= '(10812)Victor Jara')
    db.ddata0maps.insert( f0= 'pa10813', f1= '(10813)Please done this project as soon possible.')
    db.ddata0maps.insert( f0= 'sx10815', f1= '(10815)16 Sept')
    db.ddata0maps.insert( f0= 'hh10816', f1= '(10816)Victor Jara')
    db.ddata0maps.insert( f0= 'pa10817', f1= '(10817)Please done this project as soon possible.')
    db.ddata0maps.insert( f0= 'aa10818', f1= '(10818)View All Messages')
    db.ddata0maps.insert( f0= 'hh10819', f1= '(10819)Notifications')
    db.ddata0maps.insert( f0= 'sx10820', f1= '(10820)16 Sept')
    db.ddata0maps.insert( f0= 'hh10821', f1= '(10821)Advanda Cro')
    db.ddata0maps.insert( f0= 'pa10822', f1= '(10822)Please done this project as soon possible.')
    db.ddata0maps.insert( f0= 'sx10823', f1= '(10823)16 Sept')
    db.ddata0maps.insert( f0= 'hh10824', f1= '(10824)Sulaiman din')
    db.ddata0maps.insert( f0= 'pa10825', f1= '(10825)Please done this project as soon possible.')
    db.ddata0maps.insert( f0= 'sx10826', f1= '(10826)16 Sept')
    db.ddata0maps.insert( f0= 'hh10827', f1= '(10827)Victor Jara')
    db.ddata0maps.insert( f0= 'pa10828', f1= '(10828)Please done this project as soon possible.')
    db.ddata0maps.insert( f0= 'sx10829', f1= '(10829)16 Sept')
    db.ddata0maps.insert( f0= 'hh10830', f1= '(10830)Victor Jara')
    db.ddata0maps.insert( f0= 'pa10831', f1= '(10831)Please done this project as soon possible.')
    db.ddata0maps.insert( f0= 'aa10832', f1= '(10832)View All Notification')
    db.ddata0maps.insert( f0= 'sx10833', f1= '(10833)Advanda Cro')
    db.ddata0maps.insert( f0= 'aa10837', f1= '(10837)News')
    db.ddata0maps.insert( f0= 'aa10838', f1= '(10838)Activity')
    db.ddata0maps.insert( f0= 'aa10839', f1= '(10839)Settings')
    db.ddata0maps.insert( f0= 'pa10840', f1= '(10840)You have 10 New News.')
    db.ddata0maps.insert( f0= 'pa10842', f1= '(10842)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.ddata0maps.insert( f0= 'sp10843', f1= '(10843)Yesterday 2:45 pm')
    db.ddata0maps.insert( f0= 'pa10845', f1= '(10845)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.ddata0maps.insert( f0= 'sp10846', f1= '(10846)Yesterday 2:45 pm')
    db.ddata0maps.insert( f0= 'pa10848', f1= '(10848)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.ddata0maps.insert( f0= 'sp10849', f1= '(10849)Yesterday 2:45 pm')
    db.ddata0maps.insert( f0= 'pa10851', f1= '(10851)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.ddata0maps.insert( f0= 'sp10852', f1= '(10852)Yesterday 2:45 pm')
    db.ddata0maps.insert( f0= 'pa10854', f1= '(10854)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.ddata0maps.insert( f0= 'sp10855', f1= '(10855)Yesterday 2:45 pm')
    db.ddata0maps.insert( f0= 'pa10857', f1= '(10857)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.ddata0maps.insert( f0= 'sp10858', f1= '(10858)Yesterday 2:45 pm')
    db.ddata0maps.insert( f0= 'pa10860', f1= '(10860)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.ddata0maps.insert( f0= 'sp10861', f1= '(10861)Yesterday 2:45 pm')
    db.ddata0maps.insert( f0= 'pa10863', f1= '(10863)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.ddata0maps.insert( f0= 'sp10864', f1= '(10864)Yesterday 2:45 pm')
    db.ddata0maps.insert( f0= 'pa10866', f1= '(10866)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.ddata0maps.insert( f0= 'sp10867', f1= '(10867)Yesterday 2:45 pm')
    db.ddata0maps.insert( f0= 'pa10869', f1= '(10869)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.ddata0maps.insert( f0= 'sp10870', f1= '(10870)Yesterday 2:45 pm')
    db.ddata0maps.insert( f0= 'pa10871', f1= '(10871)You have 20 Recent Activity.')
    db.ddata0maps.insert( f0= 'hh10872', f1= '(10872)New User Registered')
    db.ddata0maps.insert( f0= 'pa10873', f1= '(10873)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.ddata0maps.insert( f0= 'sx10874', f1= '(10874)1 hours ago')
    db.ddata0maps.insert( f0= 'hh10875', f1= '(10875)New Order Received')
    db.ddata0maps.insert( f0= 'pa10876', f1= '(10876)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.ddata0maps.insert( f0= 'sx10877', f1= '(10877)2 hours ago')
    db.ddata0maps.insert( f0= 'hh10878', f1= '(10878)New Order Received')
    db.ddata0maps.insert( f0= 'pa10879', f1= '(10879)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.ddata0maps.insert( f0= 'sx10880', f1= '(10880)3 hours ago')
    db.ddata0maps.insert( f0= 'hh10881', f1= '(10881)New Order Received')
    db.ddata0maps.insert( f0= 'pa10882', f1= '(10882)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.ddata0maps.insert( f0= 'sx10883', f1= '(10883)4 hours ago')
    db.ddata0maps.insert( f0= 'hh10884', f1= '(10884)New User Registered')
    db.ddata0maps.insert( f0= 'pa10885', f1= '(10885)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.ddata0maps.insert( f0= 'sx10886', f1= '(10886)5 hours ago')
    db.ddata0maps.insert( f0= 'hh10887', f1= '(10887)New Order')
    db.ddata0maps.insert( f0= 'pa10888', f1= '(10888)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.ddata0maps.insert( f0= 'sx10889', f1= '(10889)6 hours ago')
    db.ddata0maps.insert( f0= 'hh10890', f1= '(10890)New User')
    db.ddata0maps.insert( f0= 'pa10891', f1= '(10891)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.ddata0maps.insert( f0= 'sx10892', f1= '(10892)7 hours ago')
    db.ddata0maps.insert( f0= 'hh10893', f1= '(10893)New Order')
    db.ddata0maps.insert( f0= 'pa10894', f1= '(10894)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.ddata0maps.insert( f0= 'sx10895', f1= '(10895)9 hours ago')
    db.ddata0maps.insert( f0= 'pa10896', f1= '(10896)You have 20 Settings. 5 not completed.')
    db.ddata0maps.insert( f0= 'hh10897', f1= '(10897)Show notifications')
    db.ddata0maps.insert( f0= 'hh10898', f1= '(10898)Disable Chat')
    db.ddata0maps.insert( f0= 'hh10899', f1= '(10899)Enable history')
    db.ddata0maps.insert( f0= 'hh10900', f1= '(10900)Show charts')
    db.ddata0maps.insert( f0= 'hh10901', f1= '(10901)Update everyday')
    db.ddata0maps.insert( f0= 'hh10902', f1= '(10902)Global search')
    db.ddata0maps.insert( f0= 'hh10903', f1= '(10903)Offline users')
    db.ddata0maps.insert( f0= 'aa10905', f1= '(10905)Dashboard v.1')
    db.ddata0maps.insert( f0= 'aa10907', f1= '(10907)Dashboard v.2')
    db.ddata0maps.insert( f0= 'aa10909', f1= '(10909)Dashboard v.3')
    db.ddata0maps.insert( f0= 'aa10911', f1= '(10911)Product List')
    db.ddata0maps.insert( f0= 'aa10913', f1= '(10913)Product Edit')
    db.ddata0maps.insert( f0= 'aa10915', f1= '(10915)Product Detail')
    db.ddata0maps.insert( f0= 'aa10917', f1= '(10917)Product Cart')
    db.ddata0maps.insert( f0= 'aa10919', f1= '(10919)Product Payment')
    db.ddata0maps.insert( f0= 'aa10921', f1= '(10921)Analytics')
    db.ddata0maps.insert( f0= 'aa10923', f1= '(10923)Widgets')
    db.ddata0maps.insert( f0= 'aa10925', f1= '(10925)Inbox')
    db.ddata0maps.insert( f0= 'aa10927', f1= '(10927)View Mail')
    db.ddata0maps.insert( f0= 'aa10929', f1= '(10929)Compose Mail')
    db.ddata0maps.insert( f0= 'aa10931', f1= '(10931)File Manager')
    db.ddata0maps.insert( f0= 'aa10933', f1= '(10933)Contacts Client')
    db.ddata0maps.insert( f0= 'aa10935', f1= '(10935)Project')
    db.ddata0maps.insert( f0= 'aa10937', f1= '(10937)Project Details')
    db.ddata0maps.insert( f0= 'aa10939', f1= '(10939)Blog')
    db.ddata0maps.insert( f0= 'aa10941', f1= '(10941)Blog Details')
    db.ddata0maps.insert( f0= 'aa10943', f1= '(10943)404 Page')
    db.ddata0maps.insert( f0= 'aa10945', f1= '(10945)500 Page')
    db.ddata0maps.insert( f0= 'aa10947', f1= '(10947)Google Map')
    db.ddata0maps.insert( f0= 'aa10949', f1= '(10949)Data Maps')
    db.ddata0maps.insert( f0= 'aa10951', f1= '(10951)Pdf Viewer')
    db.ddata0maps.insert( f0= 'aa10953', f1= '(10953)X-Editable')
    db.ddata0maps.insert( f0= 'aa10955', f1= '(10955)Code Editor')
    db.ddata0maps.insert( f0= 'aa10957', f1= '(10957)Tree View')
    db.ddata0maps.insert( f0= 'aa10959', f1= '(10959)Preloader')
    db.ddata0maps.insert( f0= 'aa10961', f1= '(10961)Images Cropper')
    db.ddata0maps.insert( f0= 'aa10963', f1= '(10963)Bar Charts')
    db.ddata0maps.insert( f0= 'aa10965', f1= '(10965)Line Charts')
    db.ddata0maps.insert( f0= 'aa10967', f1= '(10967)Area Charts')
    db.ddata0maps.insert( f0= 'aa10969', f1= '(10969)Rounded Charts')
    db.ddata0maps.insert( f0= 'aa10971', f1= '(10971)C3 Charts')
    db.ddata0maps.insert( f0= 'aa10973', f1= '(10973)Sparkline Charts')
    db.ddata0maps.insert( f0= 'aa10975', f1= '(10975)Peity Charts')
    db.ddata0maps.insert( f0= 'aa10977', f1= '(10977)Static Table')
    db.ddata0maps.insert( f0= 'aa10979', f1= '(10979)Data Table')
    db.ddata0maps.insert( f0= 'aa10981', f1= '(10981)Basic Form Elements')
    db.ddata0maps.insert( f0= 'aa10983', f1= '(10983)Advanced Form Elements')
    db.ddata0maps.insert( f0= 'aa10985', f1= '(10985)Password Meter')
    db.ddata0maps.insert( f0= 'aa10987', f1= '(10987)Multi Upload')
    db.ddata0maps.insert( f0= 'aa10989', f1= '(10989)Text Editor')
    db.ddata0maps.insert( f0= 'aa10991', f1= '(10991)Dual List Box')
    db.ddata0maps.insert( f0= 'aa10993', f1= '(10993)Basic Form Elements')
    db.ddata0maps.insert( f0= 'aa10995', f1= '(10995)Advanced Form Elements')
    db.ddata0maps.insert( f0= 'aa10997', f1= '(10997)Password Meter')
    db.ddata0maps.insert( f0= 'aa10999', f1= '(10999)Multi Upload')
    db.ddata0maps.insert( f0= 'aa11001', f1= '(11001)Text Editor')
    db.ddata0maps.insert( f0= 'aa11003', f1= '(11003)Dual List Box')
    db.ddata0maps.insert( f0= 'aa11005', f1= '(11005)Login')
    db.ddata0maps.insert( f0= 'aa11007', f1= '(11007)Register')
    db.ddata0maps.insert( f0= 'aa11009', f1= '(11009)Lock')
    db.ddata0maps.insert( f0= 'aa11011', f1= '(11011)Password Recovery')
    db.ddata0maps.insert( f0= 'pb11012', f1= '(11012)Search...')
    db.ddata0maps.insert( f0= 'aa11013', f1= '(11013)Home')
    db.ddata0maps.insert( f0= 'sx11014', f1= '(11014)Data Maps')
    db.ddata0maps.insert( f0= 'hh11015', f1= '(11015)Data Map Style 1')
    db.ddata0maps.insert( f0= 'hh11016', f1= '(11016)Data Map Style 2')
    db.ddata0maps.insert( f0= 'hh11017', f1= '(11017)Data Map Style 3')
    db.ddata0maps.insert( f0= 'hh11018', f1= '(11018)Data Map Style 4')
    db.ddata0maps.insert( f0= 'hh11019', f1= '(11019)Data Map Style 5')
    db.ddata0maps.insert( f0= 'hh11020', f1= '(11020)Data Map Style 6')
    db.ddata0maps.insert( f0= 'pc11021', f1= '(11021)All rights reserved.')
    db.ddata0maps.insert( f0= 'pf11022', f1= '(11022)Copyright  2018')
    db.commit()
#
