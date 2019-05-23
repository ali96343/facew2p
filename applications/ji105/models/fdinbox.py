#
# table for controller: inbox
#

from gluon.contrib.populate import populate

db.define_table('dinbox', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dinbox.id ).count():
    db.dinbox.insert( f0= 'sp10867', f1= '(10867)outdated')
    db.dinbox.insert( f0= 'pc10868', f1= '(10868)to improve your experience.')
    db.dinbox.insert( f0= 'aa10869', f1= '(10869)upgrade your browser')
    db.dinbox.insert( f0= 'hh10871', f1= '(10871)Messages')
    db.dinbox.insert( f0= 'hh10873', f1= '(10873)David Belle')
    db.dinbox.insert( f0= 'pa10874', f1= '(10874)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinbox.insert( f0= 'hh10876', f1= '(10876)Jonathan Morris')
    db.dinbox.insert( f0= 'pa10877', f1= '(10877)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinbox.insert( f0= 'hh10879', f1= '(10879)Fredric Mitchell')
    db.dinbox.insert( f0= 'pa10880', f1= '(10880)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinbox.insert( f0= 'hh10882', f1= '(10882)David Belle')
    db.dinbox.insert( f0= 'pa10883', f1= '(10883)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinbox.insert( f0= 'hh10885', f1= '(10885)Glenn Jecobs')
    db.dinbox.insert( f0= 'pa10886', f1= '(10886)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinbox.insert( f0= 'aa10887', f1= '(10887)View All')
    db.dinbox.insert( f0= 'hh10888', f1= '(10888)Notification')
    db.dinbox.insert( f0= 'hh10890', f1= '(10890)David Belle')
    db.dinbox.insert( f0= 'pa10891', f1= '(10891)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinbox.insert( f0= 'hh10893', f1= '(10893)Jonathan Morris')
    db.dinbox.insert( f0= 'pa10894', f1= '(10894)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinbox.insert( f0= 'hh10896', f1= '(10896)Fredric Mitchell')
    db.dinbox.insert( f0= 'pa10897', f1= '(10897)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinbox.insert( f0= 'hh10899', f1= '(10899)David Belle')
    db.dinbox.insert( f0= 'pa10900', f1= '(10900)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinbox.insert( f0= 'hh10902', f1= '(10902)Glenn Jecobs')
    db.dinbox.insert( f0= 'pa10903', f1= '(10903)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinbox.insert( f0= 'aa10904', f1= '(10904)View All')
    db.dinbox.insert( f0= 'hh10905', f1= '(10905)Tasks')
    db.dinbox.insert( f0= 'pa10906', f1= '(10906)HTML5 Validation Report')
    db.dinbox.insert( f0= 'sp10907', f1= '(10907)95%')
    db.dinbox.insert( f0= 'pa10908', f1= '(10908)Google Chrome Extension')
    db.dinbox.insert( f0= 'sp10909', f1= '(10909)85%')
    db.dinbox.insert( f0= 'pa10910', f1= '(10910)Social Internet Projects')
    db.dinbox.insert( f0= 'sp10911', f1= '(10911)75%')
    db.dinbox.insert( f0= 'pa10912', f1= '(10912)Bootstrap Admin')
    db.dinbox.insert( f0= 'sp10913', f1= '(10913)65%')
    db.dinbox.insert( f0= 'pa10914', f1= '(10914)Youtube App')
    db.dinbox.insert( f0= 'sp10915', f1= '(10915)55%')
    db.dinbox.insert( f0= 'aa10916', f1= '(10916)View All')
    db.dinbox.insert( f0= 'hh10917', f1= '(10917)Chat')
    db.dinbox.insert( f0= 'pb10918', f1= '(10918)Search People')
    db.dinbox.insert( f0= 'hh10920', f1= '(10920)David Belle')
    db.dinbox.insert( f0= 'pa10921', f1= '(10921)Available')
    db.dinbox.insert( f0= 'hh10923', f1= '(10923)Jonathan Morris')
    db.dinbox.insert( f0= 'pa10924', f1= '(10924)Last seen 3 hours ago')
    db.dinbox.insert( f0= 'hh10926', f1= '(10926)Fredric Mitchell')
    db.dinbox.insert( f0= 'pa10927', f1= '(10927)Last seen 2 minutes ago')
    db.dinbox.insert( f0= 'hh10929', f1= '(10929)David Belle')
    db.dinbox.insert( f0= 'pa10930', f1= '(10930)Available')
    db.dinbox.insert( f0= 'hh10932', f1= '(10932)Glenn Jecobs')
    db.dinbox.insert( f0= 'pa10933', f1= '(10933)Available')
    db.dinbox.insert( f0= 'aa10934', f1= '(10934)View All')
    db.dinbox.insert( f0= 'aa10935', f1= '(10935)Home')
    db.dinbox.insert( f0= 'aa10937', f1= '(10937)Dashboard One')
    db.dinbox.insert( f0= 'aa10939', f1= '(10939)Dashboard Two')
    db.dinbox.insert( f0= 'aa10941', f1= '(10941)Dashboard Three')
    db.dinbox.insert( f0= 'aa10943', f1= '(10943)Dashboard Four')
    db.dinbox.insert( f0= 'aa10945', f1= '(10945)Analytics')
    db.dinbox.insert( f0= 'aa10947', f1= '(10947)Widgets')
    db.dinbox.insert( f0= 'aa10948', f1= '(10948)Email')
    db.dinbox.insert( f0= 'aa10950', f1= '(10950)Inbox')
    db.dinbox.insert( f0= 'aa10952', f1= '(10952)View Email')
    db.dinbox.insert( f0= 'aa10954', f1= '(10954)Compose Email')
    db.dinbox.insert( f0= 'aa10955', f1= '(10955)Interface')
    db.dinbox.insert( f0= 'aa10957', f1= '(10957)Animations')
    db.dinbox.insert( f0= 'aa10959', f1= '(10959)Google Map')
    db.dinbox.insert( f0= 'aa10961', f1= '(10961)Data Maps')
    db.dinbox.insert( f0= 'aa10963', f1= '(10963)Code Editor')
    db.dinbox.insert( f0= 'aa10965', f1= '(10965)Images Cropper')
    db.dinbox.insert( f0= 'aa10967', f1= '(10967)Wizard')
    db.dinbox.insert( f0= 'aa10968', f1= '(10968)Charts')
    db.dinbox.insert( f0= 'aa10970', f1= '(10970)Flot Charts')
    db.dinbox.insert( f0= 'aa10972', f1= '(10972)Bar Charts')
    db.dinbox.insert( f0= 'aa10974', f1= '(10974)Line Charts')
    db.dinbox.insert( f0= 'aa10976', f1= '(10976)Area Charts')
    db.dinbox.insert( f0= 'aa10977', f1= '(10977)Tables')
    db.dinbox.insert( f0= 'aa10979', f1= '(10979)Normal Table')
    db.dinbox.insert( f0= 'aa10981', f1= '(10981)Data Table')
    db.dinbox.insert( f0= 'aa10982', f1= '(10982)Forms')
    db.dinbox.insert( f0= 'aa10984', f1= '(10984)Form Elements')
    db.dinbox.insert( f0= 'aa10986', f1= '(10986)Form Components')
    db.dinbox.insert( f0= 'aa10988', f1= '(10988)Form Examples')
    db.dinbox.insert( f0= 'aa10989', f1= '(10989)App views')
    db.dinbox.insert( f0= 'aa10991', f1= '(10991)Notifications')
    db.dinbox.insert( f0= 'aa10993', f1= '(10993)Alerts')
    db.dinbox.insert( f0= 'aa10995', f1= '(10995)Modals')
    db.dinbox.insert( f0= 'aa10997', f1= '(10997)Buttons')
    db.dinbox.insert( f0= 'aa10999', f1= '(10999)Tabs')
    db.dinbox.insert( f0= 'aa11001', f1= '(11001)Accordion')
    db.dinbox.insert( f0= 'aa11003', f1= '(11003)Dialogs')
    db.dinbox.insert( f0= 'aa11005', f1= '(11005)Popovers')
    db.dinbox.insert( f0= 'aa11007', f1= '(11007)Tooltips')
    db.dinbox.insert( f0= 'aa11009', f1= '(11009)Dropdowns')
    db.dinbox.insert( f0= 'aa11010', f1= '(11010)Pages')
    db.dinbox.insert( f0= 'aa11012', f1= '(11012)Contact')
    db.dinbox.insert( f0= 'aa11014', f1= '(11014)Invoice')
    db.dinbox.insert( f0= 'aa11016', f1= '(11016)Typography')
    db.dinbox.insert( f0= 'aa11018', f1= '(11018)Color')
    db.dinbox.insert( f0= 'aa11020', f1= '(11020)Login Register')
    db.dinbox.insert( f0= 'aa11022', f1= '(11022)404 Page')
    db.dinbox.insert( f0= 'aa11024', f1= '(11024)Dashboard One')
    db.dinbox.insert( f0= 'aa11026', f1= '(11026)Dashboard Two')
    db.dinbox.insert( f0= 'aa11028', f1= '(11028)Dashboard Three')
    db.dinbox.insert( f0= 'aa11030', f1= '(11030)Dashboard Four')
    db.dinbox.insert( f0= 'aa11032', f1= '(11032)Analytics')
    db.dinbox.insert( f0= 'aa11034', f1= '(11034)Widgets')
    db.dinbox.insert( f0= 'aa11036', f1= '(11036)Inbox')
    db.dinbox.insert( f0= 'aa11038', f1= '(11038)View Email')
    db.dinbox.insert( f0= 'aa11040', f1= '(11040)Compose Email')
    db.dinbox.insert( f0= 'aa11042', f1= '(11042)Animations')
    db.dinbox.insert( f0= 'aa11044', f1= '(11044)Google Map')
    db.dinbox.insert( f0= 'aa11046', f1= '(11046)Data Maps')
    db.dinbox.insert( f0= 'aa11048', f1= '(11048)Code Editor')
    db.dinbox.insert( f0= 'aa11050', f1= '(11050)Images Cropper')
    db.dinbox.insert( f0= 'aa11052', f1= '(11052)Wizard')
    db.dinbox.insert( f0= 'aa11054', f1= '(11054)Flot Charts')
    db.dinbox.insert( f0= 'aa11056', f1= '(11056)Bar Charts')
    db.dinbox.insert( f0= 'aa11058', f1= '(11058)Line Charts')
    db.dinbox.insert( f0= 'aa11060', f1= '(11060)Area Charts')
    db.dinbox.insert( f0= 'aa11062', f1= '(11062)Normal Table')
    db.dinbox.insert( f0= 'aa11064', f1= '(11064)Data Table')
    db.dinbox.insert( f0= 'aa11066', f1= '(11066)Form Elements')
    db.dinbox.insert( f0= 'aa11068', f1= '(11068)Form Components')
    db.dinbox.insert( f0= 'aa11070', f1= '(11070)Form Examples')
    db.dinbox.insert( f0= 'aa11072', f1= '(11072)Notifications')
    db.dinbox.insert( f0= 'aa11074', f1= '(11074)Alerts')
    db.dinbox.insert( f0= 'aa11076', f1= '(11076)Modals')
    db.dinbox.insert( f0= 'aa11078', f1= '(11078)Buttons')
    db.dinbox.insert( f0= 'aa11080', f1= '(11080)Tabs')
    db.dinbox.insert( f0= 'aa11082', f1= '(11082)Accordion')
    db.dinbox.insert( f0= 'aa11084', f1= '(11084)Dialogs')
    db.dinbox.insert( f0= 'aa11086', f1= '(11086)Popovers')
    db.dinbox.insert( f0= 'aa11088', f1= '(11088)Tooltips')
    db.dinbox.insert( f0= 'aa11090', f1= '(11090)Dropdowns')
    db.dinbox.insert( f0= 'aa11092', f1= '(11092)Contact')
    db.dinbox.insert( f0= 'aa11094', f1= '(11094)Invoice')
    db.dinbox.insert( f0= 'aa11096', f1= '(11096)Typography')
    db.dinbox.insert( f0= 'aa11098', f1= '(11098)Color')
    db.dinbox.insert( f0= 'aa11100', f1= '(11100)Login Register')
    db.dinbox.insert( f0= 'aa11102', f1= '(11102)404 Page')
    db.dinbox.insert( f0= 'hh11103', f1= '(11103)Inbox')
    db.dinbox.insert( f0= 'sx11104', f1= '(11104)Admin Template')
    db.dinbox.insert( f0= 'pf11105', f1= '(11105)Welcome to Notika')
    db.dinbox.insert( f0= 'aa11106', f1= '(11106)Compose')
    db.dinbox.insert( f0= 'sx11107', f1= '(11107)12')
    db.dinbox.insert( f0= 'pb11108', f1= '(11108)Search email...')
    db.dinbox.insert( f0= 'bu11109', f1= '(11109)Search')
    db.dinbox.insert( f0= 'aa11110', f1= '(11110)Jeremy Massey')
    db.dinbox.insert( f0= 'aa11111', f1= '(11111)Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
    db.dinbox.insert( f0= 'aa11112', f1= '(11112)Marshall Horne')
    db.dinbox.insert( f0= 'aa11113', f1= '(11113)Praesent nec nisl sed neque ornare maximus at ac enim.')
    db.dinbox.insert( f0= 'sx11114', f1= '(11114)Finance')
    db.dinbox.insert( f0= 'aa11115', f1= '(11115)Grant Franco')
    db.dinbox.insert( f0= 'aa11116', f1= '(11116)Ferdinand Meadows')
    db.dinbox.insert( f0= 'aa11117', f1= '(11117)Aenean hendrerit ligula eget augue gravida semper.')
    db.dinbox.insert( f0= 'sx11118', f1= '(11118)Social')
    db.dinbox.insert( f0= 'aa11119', f1= '(11119)Ivor Rios')
    db.dinbox.insert( f0= 'aa11120', f1= '(11120)Sed quis augue in nunc venenatis finibus.')
    db.dinbox.insert( f0= 'aa11121', f1= '(11121)Maxwell Murphy')
    db.dinbox.insert( f0= 'aa11122', f1= '(11122)Quisque eu tortor quis justo viverra cursus.')
    db.dinbox.insert( f0= 'aa11123', f1= '(11123)Henry Patterson')
    db.dinbox.insert( f0= 'aa11124', f1= '(11124)Aliquam nec justo interdum, ornare mi non, elementum lacus.')
    db.dinbox.insert( f0= 'aa11125', f1= '(11125)Maxwell Murphy')
    db.dinbox.insert( f0= 'aa11126', f1= '(11126)Quisque eu tortor quis justo viverra cursus.')
    db.commit()
#
