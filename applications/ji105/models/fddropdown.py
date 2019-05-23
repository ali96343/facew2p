#
# table for controller: dropdown
#

from gluon.contrib.populate import populate

db.define_table('ddropdown', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.ddropdown.id ).count():
    db.ddropdown.insert( f0= 'sp5666', f1= '(5666)outdated')
    db.ddropdown.insert( f0= 'pc5667', f1= '(5667)to improve your experience.')
    db.ddropdown.insert( f0= 'aa5668', f1= '(5668)upgrade your browser')
    db.ddropdown.insert( f0= 'hh5670', f1= '(5670)Messages')
    db.ddropdown.insert( f0= 'hh5672', f1= '(5672)David Belle')
    db.ddropdown.insert( f0= 'pa5673', f1= '(5673)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.ddropdown.insert( f0= 'hh5675', f1= '(5675)Jonathan Morris')
    db.ddropdown.insert( f0= 'pa5676', f1= '(5676)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.ddropdown.insert( f0= 'hh5678', f1= '(5678)Fredric Mitchell')
    db.ddropdown.insert( f0= 'pa5679', f1= '(5679)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.ddropdown.insert( f0= 'hh5681', f1= '(5681)David Belle')
    db.ddropdown.insert( f0= 'pa5682', f1= '(5682)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.ddropdown.insert( f0= 'hh5684', f1= '(5684)Glenn Jecobs')
    db.ddropdown.insert( f0= 'pa5685', f1= '(5685)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.ddropdown.insert( f0= 'aa5686', f1= '(5686)View All')
    db.ddropdown.insert( f0= 'hh5687', f1= '(5687)Notification')
    db.ddropdown.insert( f0= 'hh5689', f1= '(5689)David Belle')
    db.ddropdown.insert( f0= 'pa5690', f1= '(5690)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.ddropdown.insert( f0= 'hh5692', f1= '(5692)Jonathan Morris')
    db.ddropdown.insert( f0= 'pa5693', f1= '(5693)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.ddropdown.insert( f0= 'hh5695', f1= '(5695)Fredric Mitchell')
    db.ddropdown.insert( f0= 'pa5696', f1= '(5696)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.ddropdown.insert( f0= 'hh5698', f1= '(5698)David Belle')
    db.ddropdown.insert( f0= 'pa5699', f1= '(5699)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.ddropdown.insert( f0= 'hh5701', f1= '(5701)Glenn Jecobs')
    db.ddropdown.insert( f0= 'pa5702', f1= '(5702)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.ddropdown.insert( f0= 'aa5703', f1= '(5703)View All')
    db.ddropdown.insert( f0= 'hh5704', f1= '(5704)Tasks')
    db.ddropdown.insert( f0= 'pa5705', f1= '(5705)HTML5 Validation Report')
    db.ddropdown.insert( f0= 'sp5706', f1= '(5706)95%')
    db.ddropdown.insert( f0= 'pa5707', f1= '(5707)Google Chrome Extension')
    db.ddropdown.insert( f0= 'sp5708', f1= '(5708)85%')
    db.ddropdown.insert( f0= 'pa5709', f1= '(5709)Social Internet Projects')
    db.ddropdown.insert( f0= 'sp5710', f1= '(5710)93%')
    db.ddropdown.insert( f0= 'pa5711', f1= '(5711)Bootstrap Admin Template')
    db.ddropdown.insert( f0= 'sp5712', f1= '(5712)93%')
    db.ddropdown.insert( f0= 'pa5713', f1= '(5713)Youtube Client App')
    db.ddropdown.insert( f0= 'sp5714', f1= '(5714)93%')
    db.ddropdown.insert( f0= 'aa5715', f1= '(5715)View All')
    db.ddropdown.insert( f0= 'hh5716', f1= '(5716)Chat')
    db.ddropdown.insert( f0= 'pb5717', f1= '(5717)Search People')
    db.ddropdown.insert( f0= 'hh5719', f1= '(5719)David Belle')
    db.ddropdown.insert( f0= 'pa5720', f1= '(5720)Available')
    db.ddropdown.insert( f0= 'hh5722', f1= '(5722)Jonathan Morris')
    db.ddropdown.insert( f0= 'pa5723', f1= '(5723)Last seen 3 hours ago')
    db.ddropdown.insert( f0= 'hh5725', f1= '(5725)Fredric Mitchell')
    db.ddropdown.insert( f0= 'pa5726', f1= '(5726)Last seen 2 minutes ago')
    db.ddropdown.insert( f0= 'hh5728', f1= '(5728)David Belle')
    db.ddropdown.insert( f0= 'pa5729', f1= '(5729)Available')
    db.ddropdown.insert( f0= 'hh5731', f1= '(5731)Glenn Jecobs')
    db.ddropdown.insert( f0= 'pa5732', f1= '(5732)Available')
    db.ddropdown.insert( f0= 'aa5733', f1= '(5733)View All')
    db.ddropdown.insert( f0= 'aa5734', f1= '(5734)Home')
    db.ddropdown.insert( f0= 'aa5736', f1= '(5736)Dashboard One')
    db.ddropdown.insert( f0= 'aa5738', f1= '(5738)Dashboard Two')
    db.ddropdown.insert( f0= 'aa5740', f1= '(5740)Dashboard Three')
    db.ddropdown.insert( f0= 'aa5742', f1= '(5742)Dashboard Four')
    db.ddropdown.insert( f0= 'aa5744', f1= '(5744)Analytics')
    db.ddropdown.insert( f0= 'aa5746', f1= '(5746)Widgets')
    db.ddropdown.insert( f0= 'aa5747', f1= '(5747)Email')
    db.ddropdown.insert( f0= 'aa5749', f1= '(5749)Inbox')
    db.ddropdown.insert( f0= 'aa5751', f1= '(5751)View Email')
    db.ddropdown.insert( f0= 'aa5753', f1= '(5753)Compose Email')
    db.ddropdown.insert( f0= 'aa5754', f1= '(5754)Interface')
    db.ddropdown.insert( f0= 'aa5756', f1= '(5756)Animations')
    db.ddropdown.insert( f0= 'aa5758', f1= '(5758)Google Map')
    db.ddropdown.insert( f0= 'aa5760', f1= '(5760)Data Maps')
    db.ddropdown.insert( f0= 'aa5762', f1= '(5762)Code Editor')
    db.ddropdown.insert( f0= 'aa5764', f1= '(5764)Images Cropper')
    db.ddropdown.insert( f0= 'aa5766', f1= '(5766)Wizard')
    db.ddropdown.insert( f0= 'aa5767', f1= '(5767)Charts')
    db.ddropdown.insert( f0= 'aa5769', f1= '(5769)Flot Charts')
    db.ddropdown.insert( f0= 'aa5771', f1= '(5771)Bar Charts')
    db.ddropdown.insert( f0= 'aa5773', f1= '(5773)Line Charts')
    db.ddropdown.insert( f0= 'aa5775', f1= '(5775)Area Charts')
    db.ddropdown.insert( f0= 'aa5776', f1= '(5776)Tables')
    db.ddropdown.insert( f0= 'aa5778', f1= '(5778)Normal Table')
    db.ddropdown.insert( f0= 'aa5780', f1= '(5780)Data Table')
    db.ddropdown.insert( f0= 'aa5781', f1= '(5781)Forms')
    db.ddropdown.insert( f0= 'aa5783', f1= '(5783)Form Elements')
    db.ddropdown.insert( f0= 'aa5785', f1= '(5785)Form Components')
    db.ddropdown.insert( f0= 'aa5787', f1= '(5787)Form Examples')
    db.ddropdown.insert( f0= 'aa5788', f1= '(5788)App views')
    db.ddropdown.insert( f0= 'aa5790', f1= '(5790)Notifications')
    db.ddropdown.insert( f0= 'aa5792', f1= '(5792)Alerts')
    db.ddropdown.insert( f0= 'aa5794', f1= '(5794)Modals')
    db.ddropdown.insert( f0= 'aa5796', f1= '(5796)Buttons')
    db.ddropdown.insert( f0= 'aa5798', f1= '(5798)Tabs')
    db.ddropdown.insert( f0= 'aa5800', f1= '(5800)Accordion')
    db.ddropdown.insert( f0= 'aa5802', f1= '(5802)Dialogs')
    db.ddropdown.insert( f0= 'aa5804', f1= '(5804)Popovers')
    db.ddropdown.insert( f0= 'aa5806', f1= '(5806)Tooltips')
    db.ddropdown.insert( f0= 'aa5808', f1= '(5808)Dropdowns')
    db.ddropdown.insert( f0= 'aa5809', f1= '(5809)Pages')
    db.ddropdown.insert( f0= 'aa5811', f1= '(5811)Contact')
    db.ddropdown.insert( f0= 'aa5813', f1= '(5813)Invoice')
    db.ddropdown.insert( f0= 'aa5815', f1= '(5815)Typography')
    db.ddropdown.insert( f0= 'aa5817', f1= '(5817)Color')
    db.ddropdown.insert( f0= 'aa5819', f1= '(5819)Login Register')
    db.ddropdown.insert( f0= 'aa5821', f1= '(5821)404 Page')
    db.ddropdown.insert( f0= 'aa5823', f1= '(5823)Dashboard One')
    db.ddropdown.insert( f0= 'aa5825', f1= '(5825)Dashboard Two')
    db.ddropdown.insert( f0= 'aa5827', f1= '(5827)Dashboard Three')
    db.ddropdown.insert( f0= 'aa5829', f1= '(5829)Dashboard Four')
    db.ddropdown.insert( f0= 'aa5831', f1= '(5831)Analytics')
    db.ddropdown.insert( f0= 'aa5833', f1= '(5833)Widgets')
    db.ddropdown.insert( f0= 'aa5835', f1= '(5835)Inbox')
    db.ddropdown.insert( f0= 'aa5837', f1= '(5837)View Email')
    db.ddropdown.insert( f0= 'aa5839', f1= '(5839)Compose Email')
    db.ddropdown.insert( f0= 'aa5841', f1= '(5841)Animations')
    db.ddropdown.insert( f0= 'aa5843', f1= '(5843)Google Map')
    db.ddropdown.insert( f0= 'aa5845', f1= '(5845)Data Maps')
    db.ddropdown.insert( f0= 'aa5847', f1= '(5847)Code Editor')
    db.ddropdown.insert( f0= 'aa5849', f1= '(5849)Images Cropper')
    db.ddropdown.insert( f0= 'aa5851', f1= '(5851)Wizard')
    db.ddropdown.insert( f0= 'aa5853', f1= '(5853)Flot Charts')
    db.ddropdown.insert( f0= 'aa5855', f1= '(5855)Bar Charts')
    db.ddropdown.insert( f0= 'aa5857', f1= '(5857)Line Charts')
    db.ddropdown.insert( f0= 'aa5859', f1= '(5859)Area Charts')
    db.ddropdown.insert( f0= 'aa5861', f1= '(5861)Normal Table')
    db.ddropdown.insert( f0= 'aa5863', f1= '(5863)Data Table')
    db.ddropdown.insert( f0= 'aa5865', f1= '(5865)Form Elements')
    db.ddropdown.insert( f0= 'aa5867', f1= '(5867)Form Components')
    db.ddropdown.insert( f0= 'aa5869', f1= '(5869)Form Examples')
    db.ddropdown.insert( f0= 'aa5871', f1= '(5871)Notifications')
    db.ddropdown.insert( f0= 'aa5873', f1= '(5873)Alerts')
    db.ddropdown.insert( f0= 'aa5875', f1= '(5875)Modals')
    db.ddropdown.insert( f0= 'aa5877', f1= '(5877)Buttons')
    db.ddropdown.insert( f0= 'aa5879', f1= '(5879)Tabs')
    db.ddropdown.insert( f0= 'aa5881', f1= '(5881)Accordion')
    db.ddropdown.insert( f0= 'aa5883', f1= '(5883)Dialogs')
    db.ddropdown.insert( f0= 'aa5885', f1= '(5885)Popovers')
    db.ddropdown.insert( f0= 'aa5887', f1= '(5887)Tooltips')
    db.ddropdown.insert( f0= 'aa5889', f1= '(5889)Dropdowns')
    db.ddropdown.insert( f0= 'aa5891', f1= '(5891)Contact')
    db.ddropdown.insert( f0= 'aa5893', f1= '(5893)Invoice')
    db.ddropdown.insert( f0= 'aa5895', f1= '(5895)Typography')
    db.ddropdown.insert( f0= 'aa5897', f1= '(5897)Color')
    db.ddropdown.insert( f0= 'aa5899', f1= '(5899)Login Register')
    db.ddropdown.insert( f0= 'aa5901', f1= '(5901)404 Page')
    db.ddropdown.insert( f0= 'hh5902', f1= '(5902)Dropdown')
    db.ddropdown.insert( f0= 'sx5903', f1= '(5903)Admin Template')
    db.ddropdown.insert( f0= 'pf5904', f1= '(5904)Welcome to Notika')
    db.ddropdown.insert( f0= 'hh5905', f1= '(5905)Dropdown Basic Previews (After triggering)')
    db.ddropdown.insert( f0= 'pa5906', f1= '(5906)Toggleable, contextual menu for displaying lists of links. Please refer the Colors page for all the available color options')
    db.ddropdown.insert( f0= 'aa5907', f1= '(5907)Action')
    db.ddropdown.insert( f0= 'aa5908', f1= '(5908)Another action')
    db.ddropdown.insert( f0= 'aa5909', f1= '(5909)Separated link')
    db.ddropdown.insert( f0= 'aa5910', f1= '(5910)Action')
    db.ddropdown.insert( f0= 'aa5911', f1= '(5911)Another action')
    db.ddropdown.insert( f0= 'aa5912', f1= '(5912)Separated link')
    db.ddropdown.insert( f0= 'aa5913', f1= '(5913)Action')
    db.ddropdown.insert( f0= 'aa5914', f1= '(5914)Another action')
    db.ddropdown.insert( f0= 'aa5915', f1= '(5915)Separated link')
    db.ddropdown.insert( f0= 'aa5916', f1= '(5916)Action')
    db.ddropdown.insert( f0= 'aa5917', f1= '(5917)Another action')
    db.ddropdown.insert( f0= 'aa5918', f1= '(5918)Separated link')
    db.ddropdown.insert( f0= 'aa5919', f1= '(5919)Action')
    db.ddropdown.insert( f0= 'aa5920', f1= '(5920)Another action')
    db.ddropdown.insert( f0= 'aa5921', f1= '(5921)Separated link')
    db.ddropdown.insert( f0= 'aa5922', f1= '(5922)Action')
    db.ddropdown.insert( f0= 'aa5923', f1= '(5923)Another action')
    db.ddropdown.insert( f0= 'aa5924', f1= '(5924)Separated link')
    db.ddropdown.insert( f0= 'aa5925', f1= '(5925)Action')
    db.ddropdown.insert( f0= 'aa5926', f1= '(5926)Another action')
    db.ddropdown.insert( f0= 'aa5927', f1= '(5927)Separated link')
    db.ddropdown.insert( f0= 'aa5928', f1= '(5928)Action')
    db.ddropdown.insert( f0= 'aa5929', f1= '(5929)Another action')
    db.ddropdown.insert( f0= 'aa5930', f1= '(5930)Separated link')
    db.ddropdown.insert( f0= 'aa5931', f1= '(5931)Action')
    db.ddropdown.insert( f0= 'aa5932', f1= '(5932)Another action')
    db.ddropdown.insert( f0= 'aa5933', f1= '(5933)Separated link')
    db.ddropdown.insert( f0= 'aa5934', f1= '(5934)Action')
    db.ddropdown.insert( f0= 'aa5935', f1= '(5935)Another action')
    db.ddropdown.insert( f0= 'aa5936', f1= '(5936)Separated link')
    db.ddropdown.insert( f0= 'hh5937', f1= '(5937)Toggle Animations')
    db.ddropdown.insert( f0= 'pa5938', f1= '(5938)Toggle animations are relies on basic 3 attributes, Animations In, Animation Out and Animation Duration. Make sure to give these values in the data-animation data attribute.')
    db.ddropdown.insert( f0= 'bu5939', f1= '(5939)Fade In')
    db.ddropdown.insert( f0= 'aa5940', f1= '(5940)Action')
    db.ddropdown.insert( f0= 'aa5941', f1= '(5941)Another action')
    db.ddropdown.insert( f0= 'aa5942', f1= '(5942)Something else here')
    db.ddropdown.insert( f0= 'aa5943', f1= '(5943)Separated link')
    db.ddropdown.insert( f0= 'bu5944', f1= '(5944)fade In Up')
    db.ddropdown.insert( f0= 'aa5945', f1= '(5945)Action')
    db.ddropdown.insert( f0= 'aa5946', f1= '(5946)Another action')
    db.ddropdown.insert( f0= 'aa5947', f1= '(5947)Something else here')
    db.ddropdown.insert( f0= 'aa5948', f1= '(5948)Separated link')
    db.ddropdown.insert( f0= 'bu5949', f1= '(5949)fade In Left')
    db.ddropdown.insert( f0= 'aa5950', f1= '(5950)Action')
    db.ddropdown.insert( f0= 'aa5951', f1= '(5951)Another action')
    db.ddropdown.insert( f0= 'aa5952', f1= '(5952)Something else here')
    db.ddropdown.insert( f0= 'aa5953', f1= '(5953)Separated link')
    db.ddropdown.insert( f0= 'bu5954', f1= '(5954)shake')
    db.ddropdown.insert( f0= 'aa5955', f1= '(5955)Action')
    db.ddropdown.insert( f0= 'aa5956', f1= '(5956)Another action')
    db.ddropdown.insert( f0= 'aa5957', f1= '(5957)Something else here')
    db.ddropdown.insert( f0= 'aa5958', f1= '(5958)Separated link')
    db.ddropdown.insert( f0= 'bu5959', f1= '(5959)swing')
    db.ddropdown.insert( f0= 'aa5960', f1= '(5960)Action')
    db.ddropdown.insert( f0= 'aa5961', f1= '(5961)Another action')
    db.ddropdown.insert( f0= 'aa5962', f1= '(5962)Something else here')
    db.ddropdown.insert( f0= 'aa5963', f1= '(5963)Separated link')
    db.ddropdown.insert( f0= 'bu5964', f1= '(5964)jello')
    db.ddropdown.insert( f0= 'aa5965', f1= '(5965)Action')
    db.ddropdown.insert( f0= 'aa5966', f1= '(5966)Another action')
    db.ddropdown.insert( f0= 'aa5967', f1= '(5967)Something else here')
    db.ddropdown.insert( f0= 'aa5968', f1= '(5968)Separated link')
    db.ddropdown.insert( f0= 'bu5969', f1= '(5969)bounceIn')
    db.ddropdown.insert( f0= 'aa5970', f1= '(5970)Action')
    db.ddropdown.insert( f0= 'aa5971', f1= '(5971)Another action')
    db.ddropdown.insert( f0= 'aa5972', f1= '(5972)Something else here')
    db.ddropdown.insert( f0= 'aa5973', f1= '(5973)Separated link')
    db.ddropdown.insert( f0= 'bu5974', f1= '(5974)bounceInUp')
    db.ddropdown.insert( f0= 'aa5975', f1= '(5975)Action')
    db.ddropdown.insert( f0= 'aa5976', f1= '(5976)Another action')
    db.ddropdown.insert( f0= 'aa5977', f1= '(5977)Something else here')
    db.ddropdown.insert( f0= 'aa5978', f1= '(5978)Separated link')
    db.ddropdown.insert( f0= 'bu5979', f1= '(5979)flip')
    db.ddropdown.insert( f0= 'aa5980', f1= '(5980)Action')
    db.ddropdown.insert( f0= 'aa5981', f1= '(5981)Another action')
    db.ddropdown.insert( f0= 'aa5982', f1= '(5982)Something else here')
    db.ddropdown.insert( f0= 'aa5983', f1= '(5983)Separated link')
    db.ddropdown.insert( f0= 'bu5984', f1= '(5984)flipInX')
    db.ddropdown.insert( f0= 'aa5985', f1= '(5985)Action')
    db.ddropdown.insert( f0= 'aa5986', f1= '(5986)Another action')
    db.ddropdown.insert( f0= 'aa5987', f1= '(5987)Something else here')
    db.ddropdown.insert( f0= 'aa5988', f1= '(5988)Separated link')
    db.ddropdown.insert( f0= 'bu5989', f1= '(5989)flipInY')
    db.ddropdown.insert( f0= 'aa5990', f1= '(5990)Action')
    db.ddropdown.insert( f0= 'aa5991', f1= '(5991)Another action')
    db.ddropdown.insert( f0= 'aa5992', f1= '(5992)Something else here')
    db.ddropdown.insert( f0= 'aa5993', f1= '(5993)Separated link')
    db.ddropdown.insert( f0= 'bu5994', f1= '(5994)rotateIn')
    db.ddropdown.insert( f0= 'aa5995', f1= '(5995)Action')
    db.ddropdown.insert( f0= 'aa5996', f1= '(5996)Another action')
    db.ddropdown.insert( f0= 'aa5997', f1= '(5997)Something else here')
    db.ddropdown.insert( f0= 'aa5998', f1= '(5998)Separated link')
    db.ddropdown.insert( f0= 'bu5999', f1= '(5999)zoomIn')
    db.ddropdown.insert( f0= 'aa6000', f1= '(6000)Action')
    db.ddropdown.insert( f0= 'aa6001', f1= '(6001)Another action')
    db.ddropdown.insert( f0= 'aa6002', f1= '(6002)Something else here')
    db.ddropdown.insert( f0= 'aa6003', f1= '(6003)Separated link')
    db.ddropdown.insert( f0= 'hh6004', f1= '(6004)Dropdown links with icon')
    db.ddropdown.insert( f0= 'pa6005', f1= '(6005)Toggleable, contextual menu for displaying lists of links. Using notika custom icon here.')
    db.commit()
#
