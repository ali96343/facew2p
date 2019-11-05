#
# table for controller: profile
#

from gluon.contrib.populate import populate

db.define_table('dprofile', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dprofile.id ).count():
    db.dprofile.insert( f0= 'aa5899', f1= '(5899)Home')
    db.dprofile.insert( f0= 'aa5900', f1= '(5900)Contact')
    db.dprofile.insert( f0= 'pb5901', f1= '(5901)Search')
    db.dprofile.insert( f0= 'sx5902', f1= '(5902)3')
    db.dprofile.insert( f0= 'pc5904', f1= '(5904)Call me whenever you can...')
    db.dprofile.insert( f0= 'pc5905', f1= '(5905)4 Hours Ago')
    db.dprofile.insert( f0= 'pc5907', f1= '(5907)I got your message bro')
    db.dprofile.insert( f0= 'pc5908', f1= '(5908)4 Hours Ago')
    db.dprofile.insert( f0= 'pc5910', f1= '(5910)The subject goes here')
    db.dprofile.insert( f0= 'pc5911', f1= '(5911)4 Hours Ago')
    db.dprofile.insert( f0= 'aa5912', f1= '(5912)See All Messages')
    db.dprofile.insert( f0= 'sx5913', f1= '(5913)15 Notifications')
    db.dprofile.insert( f0= 'sx5914', f1= '(5914)3 mins')
    db.dprofile.insert( f0= 'sx5915', f1= '(5915)12 hours')
    db.dprofile.insert( f0= 'sx5916', f1= '(5916)2 days')
    db.dprofile.insert( f0= 'aa5917', f1= '(5917)See All Notifications')
    db.dprofile.insert( f0= 'sx5920', f1= '(5920)AdminLTE 3')
    db.dprofile.insert( f0= 'aa5922', f1= '(5922)Alexander Pierce')
    db.dprofile.insert( f0= 'pa5924', f1= '(5924)Dashboard v1')
    db.dprofile.insert( f0= 'pa5926', f1= '(5926)Dashboard v2')
    db.dprofile.insert( f0= 'pa5928', f1= '(5928)Dashboard v3')
    db.dprofile.insert( f0= 'sx5930', f1= '(5930)New')
    db.dprofile.insert( f0= 'sx5931', f1= '(5931)6')
    db.dprofile.insert( f0= 'pa5933', f1= '(5933)Top Navigation')
    db.dprofile.insert( f0= 'pa5935', f1= '(5935)Boxed')
    db.dprofile.insert( f0= 'pa5937', f1= '(5937)Fixed Sidebar')
    db.dprofile.insert( f0= 'pa5939', f1= '(5939)Fixed Navbar')
    db.dprofile.insert( f0= 'pa5941', f1= '(5941)Fixed Footer')
    db.dprofile.insert( f0= 'pa5943', f1= '(5943)Collapsed Sidebar')
    db.dprofile.insert( f0= 'pa5945', f1= '(5945)ChartJS')
    db.dprofile.insert( f0= 'pa5947', f1= '(5947)Flot')
    db.dprofile.insert( f0= 'pa5949', f1= '(5949)Inline')
    db.dprofile.insert( f0= 'pa5951', f1= '(5951)General')
    db.dprofile.insert( f0= 'pa5953', f1= '(5953)Icons')
    db.dprofile.insert( f0= 'pa5955', f1= '(5955)Buttons')
    db.dprofile.insert( f0= 'pa5957', f1= '(5957)Sliders')
    db.dprofile.insert( f0= 'pa5959', f1= '(5959)Modals & Alerts')
    db.dprofile.insert( f0= 'pa5961', f1= '(5961)Navbar & Tabs')
    db.dprofile.insert( f0= 'pa5963', f1= '(5963)Timeline')
    db.dprofile.insert( f0= 'pa5965', f1= '(5965)Ribbons')
    db.dprofile.insert( f0= 'pa5967', f1= '(5967)General Elements')
    db.dprofile.insert( f0= 'pa5969', f1= '(5969)Advanced Elements')
    db.dprofile.insert( f0= 'pa5971', f1= '(5971)Editors')
    db.dprofile.insert( f0= 'pa5973', f1= '(5973)Simple Tables')
    db.dprofile.insert( f0= 'pa5975', f1= '(5975)DataTables')
    db.dprofile.insert( f0= 'pa5977', f1= '(5977)jsGrid')
    db.dprofile.insert( f0= 'lb5978', f1= '(5978)EXAMPLES')
    db.dprofile.insert( f0= 'sx5980', f1= '(5980)2')
    db.dprofile.insert( f0= 'pa5983', f1= '(5983)Inbox')
    db.dprofile.insert( f0= 'pa5985', f1= '(5985)Compose')
    db.dprofile.insert( f0= 'pa5987', f1= '(5987)Read')
    db.dprofile.insert( f0= 'pa5989', f1= '(5989)Invoice')
    db.dprofile.insert( f0= 'pa5991', f1= '(5991)Profile')
    db.dprofile.insert( f0= 'pa5993', f1= '(5993)E-commerce')
    db.dprofile.insert( f0= 'pa5995', f1= '(5995)Projects')
    db.dprofile.insert( f0= 'pa5997', f1= '(5997)Project Add')
    db.dprofile.insert( f0= 'pa5999', f1= '(5999)Project Edit')
    db.dprofile.insert( f0= 'pa6001', f1= '(6001)Project Detail')
    db.dprofile.insert( f0= 'pa6003', f1= '(6003)Contacts')
    db.dprofile.insert( f0= 'pa6005', f1= '(6005)Login')
    db.dprofile.insert( f0= 'pa6007', f1= '(6007)Register')
    db.dprofile.insert( f0= 'pa6009', f1= '(6009)Forgot Password')
    db.dprofile.insert( f0= 'pa6011', f1= '(6011)Recover Password')
    db.dprofile.insert( f0= 'pa6013', f1= '(6013)Lockscreen')
    db.dprofile.insert( f0= 'pa6015', f1= '(6015)Legacy User Menu')
    db.dprofile.insert( f0= 'pa6017', f1= '(6017)Language Menu')
    db.dprofile.insert( f0= 'pa6019', f1= '(6019)Error 404')
    db.dprofile.insert( f0= 'pa6021', f1= '(6021)Error 500')
    db.dprofile.insert( f0= 'pa6023', f1= '(6023)Pace')
    db.dprofile.insert( f0= 'pa6025', f1= '(6025)Blank Page')
    db.dprofile.insert( f0= 'pa6027', f1= '(6027)Starter Page')
    db.dprofile.insert( f0= 'lb6028', f1= '(6028)MISCELLANEOUS')
    db.dprofile.insert( f0= 'pa6029', f1= '(6029)Documentation')
    db.dprofile.insert( f0= 'lb6030', f1= '(6030)MULTI LEVEL EXAMPLE')
    db.dprofile.insert( f0= 'pa6031', f1= '(6031)Level 1')
    db.dprofile.insert( f0= 'pa6032', f1= '(6032)Level 2')
    db.dprofile.insert( f0= 'pa6033', f1= '(6033)Level 3')
    db.dprofile.insert( f0= 'pa6034', f1= '(6034)Level 3')
    db.dprofile.insert( f0= 'pa6035', f1= '(6035)Level 3')
    db.dprofile.insert( f0= 'pa6036', f1= '(6036)Level 2')
    db.dprofile.insert( f0= 'pa6037', f1= '(6037)Level 1')
    db.dprofile.insert( f0= 'lb6038', f1= '(6038)LABELS')
    db.dprofile.insert( f0= 'pc6039', f1= '(6039)Important')
    db.dprofile.insert( f0= 'pa6040', f1= '(6040)Warning')
    db.dprofile.insert( f0= 'pa6041', f1= '(6041)Informational')
    db.dprofile.insert( f0= 'hh6042', f1= '(6042)Profile')
    db.dprofile.insert( f0= 'aa6043', f1= '(6043)Home')
    db.dprofile.insert( f0= 'lb6044', f1= '(6044)User Profile')
    db.dprofile.insert( f0= 'hc6046', f1= '(6046)Nina Mcintire')
    db.dprofile.insert( f0= 'pc6047', f1= '(6047)Software Engineer')
    db.dprofile.insert( f0= 'bb6048', f1= '(6048)Followers')
    db.dprofile.insert( f0= 'bb6049', f1= '(6049)Following')
    db.dprofile.insert( f0= 'bb6050', f1= '(6050)Friends')
    db.dprofile.insert( f0= 'bb6051', f1= '(6051)Follow')
    db.dprofile.insert( f0= 'hc6052', f1= '(6052)About Me')
    db.dprofile.insert( f0= 'pc6053', f1= '(6053)Malibu, California')
    db.dprofile.insert( f0= 'sx6054', f1= '(6054)UI Design')
    db.dprofile.insert( f0= 'sx6055', f1= '(6055)Coding')
    db.dprofile.insert( f0= 'sx6056', f1= '(6056)Javascript')
    db.dprofile.insert( f0= 'sx6057', f1= '(6057)PHP')
    db.dprofile.insert( f0= 'sx6058', f1= '(6058)Node.js')
    db.dprofile.insert( f0= 'pc6059', f1= '(6059)Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam fermentum enim neque.')
    db.dprofile.insert( f0= 'aa6060', f1= '(6060)Activity')
    db.dprofile.insert( f0= 'aa6061', f1= '(6061)Timeline')
    db.dprofile.insert( f0= 'aa6062', f1= '(6062)Settings')
    db.dprofile.insert( f0= 'aa6064', f1= '(6064)Jonathan Burke Jr.')
    db.dprofile.insert( f0= 'sx6065', f1= '(6065)Shared publicly - 7:30 PM today')
    db.dprofile.insert( f0= 'ia6066', f1= '(6066)Share')
    db.dprofile.insert( f0= 'ia6067', f1= '(6067)Like')
    db.dprofile.insert( f0= 'pb6068', f1= '(6068)Type a comment')
    db.dprofile.insert( f0= 'aa6070', f1= '(6070)Sarah Ross')
    db.dprofile.insert( f0= 'sx6071', f1= '(6071)Sent you a message - 3 days ago')
    db.dprofile.insert( f0= 'pb6072', f1= '(6072)Response')
    db.dprofile.insert( f0= 'bu6073', f1= '(6073)Send')
    db.dprofile.insert( f0= 'aa6075', f1= '(6075)Adam Jones')
    db.dprofile.insert( f0= 'sx6076', f1= '(6076)Posted 5 photos - 5 days ago')
    db.dprofile.insert( f0= 'ia6082', f1= '(6082)Share')
    db.dprofile.insert( f0= 'ia6083', f1= '(6083)Like')
    db.dprofile.insert( f0= 'pb6084', f1= '(6084)Type a comment')
    db.dprofile.insert( f0= 'sx6085', f1= '(6085)12:05')
    db.dprofile.insert( f0= 'aa6086', f1= '(6086)Support Team')
    db.dprofile.insert( f0= 'aa6087', f1= '(6087)Read more')
    db.dprofile.insert( f0= 'aa6088', f1= '(6088)Delete')
    db.dprofile.insert( f0= 'sx6089', f1= '(6089)5 mins ago')
    db.dprofile.insert( f0= 'aa6090', f1= '(6090)Sarah Young')
    db.dprofile.insert( f0= 'sx6091', f1= '(6091)27 mins ago')
    db.dprofile.insert( f0= 'aa6092', f1= '(6092)Jay White')
    db.dprofile.insert( f0= 'aa6093', f1= '(6093)View comment')
    db.dprofile.insert( f0= 'sx6094', f1= '(6094)2 days ago')
    db.dprofile.insert( f0= 'aa6095', f1= '(6095)Mina Lee')
    db.dprofile.insert( f0= 'pb6096', f1= '(6096)Name')
    db.dprofile.insert( f0= 'pb6097', f1= '(6097)Email')
    db.dprofile.insert( f0= 'pb6098', f1= '(6098)Name')
    db.dprofile.insert( f0= 'pb6099', f1= '(6099)Experience')
    db.dprofile.insert( f0= 'pb6100', f1= '(6100)Skills')
    db.dprofile.insert( f0= 'aa6101', f1= '(6101)terms and conditions')
    db.dprofile.insert( f0= 'bu6102', f1= '(6102)Submit')
    db.dprofile.insert( f0= 'bb6103', f1= '(6103)Version')
    db.dprofile.insert( f0= 'aa6104', f1= '(6104)AdminLTE.io')
    db.commit()
#
