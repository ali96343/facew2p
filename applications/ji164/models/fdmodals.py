#
# table for controller: modals
#

from gluon.contrib.populate import populate

db.define_table('dmodals', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dmodals.id ).count():
    db.dmodals.insert( f0= 'sp4671', f1= '(4671)outdated')
    db.dmodals.insert( f0= 'pc4672', f1= '(4672)to improve your experience.')
    db.dmodals.insert( f0= 'aa4673', f1= '(4673)upgrade your browser')
    db.dmodals.insert( f0= 'sx4678', f1= '(4678)Ecommerce')
    db.dmodals.insert( f0= 'sx4680', f1= '(4680)Dashboard v.1')
    db.dmodals.insert( f0= 'sx4682', f1= '(4682)Dashboard v.2')
    db.dmodals.insert( f0= 'sx4684', f1= '(4684)Dashboard v.3')
    db.dmodals.insert( f0= 'sx4686', f1= '(4686)Product List')
    db.dmodals.insert( f0= 'sx4688', f1= '(4688)Product Edit')
    db.dmodals.insert( f0= 'sx4690', f1= '(4690)Product Detail')
    db.dmodals.insert( f0= 'sx4692', f1= '(4692)Product Cart')
    db.dmodals.insert( f0= 'sx4694', f1= '(4694)Product Payment')
    db.dmodals.insert( f0= 'sx4696', f1= '(4696)Analytics')
    db.dmodals.insert( f0= 'sx4698', f1= '(4698)Widgets')
    db.dmodals.insert( f0= 'sx4700', f1= '(4700)Mailbox')
    db.dmodals.insert( f0= 'sx4702', f1= '(4702)Inbox')
    db.dmodals.insert( f0= 'sx4704', f1= '(4704)View Mail')
    db.dmodals.insert( f0= 'sx4706', f1= '(4706)Compose Mail')
    db.dmodals.insert( f0= 'sx4708', f1= '(4708)Interface')
    db.dmodals.insert( f0= 'sx4710', f1= '(4710)Google Map')
    db.dmodals.insert( f0= 'sx4712', f1= '(4712)Data Maps')
    db.dmodals.insert( f0= 'sx4714', f1= '(4714)Pdf Viewer')
    db.dmodals.insert( f0= 'sx4716', f1= '(4716)X-Editable')
    db.dmodals.insert( f0= 'sx4718', f1= '(4718)Code Editor')
    db.dmodals.insert( f0= 'sx4720', f1= '(4720)Tree View')
    db.dmodals.insert( f0= 'sx4722', f1= '(4722)Preloader')
    db.dmodals.insert( f0= 'sx4724', f1= '(4724)Images Cropper')
    db.dmodals.insert( f0= 'sx4726', f1= '(4726)Miscellaneous')
    db.dmodals.insert( f0= 'sx4728', f1= '(4728)File Manager')
    db.dmodals.insert( f0= 'sx4730', f1= '(4730)Blog')
    db.dmodals.insert( f0= 'sx4732', f1= '(4732)Blog Details')
    db.dmodals.insert( f0= 'sx4734', f1= '(4734)404 Page')
    db.dmodals.insert( f0= 'sx4736', f1= '(4736)500 Page')
    db.dmodals.insert( f0= 'sx4738', f1= '(4738)Charts')
    db.dmodals.insert( f0= 'sx4740', f1= '(4740)Bar Charts')
    db.dmodals.insert( f0= 'sx4742', f1= '(4742)Line Charts')
    db.dmodals.insert( f0= 'sx4744', f1= '(4744)Area Charts')
    db.dmodals.insert( f0= 'sx4746', f1= '(4746)Rounded Charts')
    db.dmodals.insert( f0= 'sx4748', f1= '(4748)C3 Charts')
    db.dmodals.insert( f0= 'sx4750', f1= '(4750)Sparkline Charts')
    db.dmodals.insert( f0= 'sx4752', f1= '(4752)Peity Charts')
    db.dmodals.insert( f0= 'sx4754', f1= '(4754)Data Tables')
    db.dmodals.insert( f0= 'sx4756', f1= '(4756)Static Table')
    db.dmodals.insert( f0= 'sx4758', f1= '(4758)Data Table')
    db.dmodals.insert( f0= 'sx4760', f1= '(4760)Forms Elements')
    db.dmodals.insert( f0= 'sx4762', f1= '(4762)Bc Form Elements')
    db.dmodals.insert( f0= 'sx4764', f1= '(4764)Ad Form Elements')
    db.dmodals.insert( f0= 'sx4766', f1= '(4766)Password Meter')
    db.dmodals.insert( f0= 'sx4768', f1= '(4768)Multi Upload')
    db.dmodals.insert( f0= 'sx4770', f1= '(4770)Text Editor')
    db.dmodals.insert( f0= 'sx4772', f1= '(4772)Dual List Box')
    db.dmodals.insert( f0= 'sx4774', f1= '(4774)App views')
    db.dmodals.insert( f0= 'sx4776', f1= '(4776)Notifications')
    db.dmodals.insert( f0= 'sx4778', f1= '(4778)Alerts')
    db.dmodals.insert( f0= 'sx4780', f1= '(4780)Modals')
    db.dmodals.insert( f0= 'sx4782', f1= '(4782)Buttons')
    db.dmodals.insert( f0= 'sx4784', f1= '(4784)Tabs')
    db.dmodals.insert( f0= 'sx4786', f1= '(4786)Accordion')
    db.dmodals.insert( f0= 'sx4787', f1= '(4787)Pages')
    db.dmodals.insert( f0= 'sx4789', f1= '(4789)Login')
    db.dmodals.insert( f0= 'sx4791', f1= '(4791)Register')
    db.dmodals.insert( f0= 'sx4793', f1= '(4793)Lock')
    db.dmodals.insert( f0= 'sx4795', f1= '(4795)Password Recovery')
    db.dmodals.insert( f0= 'sx4796', f1= '(4796)Landing Page')
    db.dmodals.insert( f0= 'aa4799', f1= '(4799)Home')
    db.dmodals.insert( f0= 'aa4800', f1= '(4800)About')
    db.dmodals.insert( f0= 'aa4801', f1= '(4801)Services')
    db.dmodals.insert( f0= 'aa4802', f1= '(4802)Support')
    db.dmodals.insert( f0= 'hh4803', f1= '(4803)Message')
    db.dmodals.insert( f0= 'sx4805', f1= '(4805)16 Sept')
    db.dmodals.insert( f0= 'hh4806', f1= '(4806)Advanda Cro')
    db.dmodals.insert( f0= 'pa4807', f1= '(4807)Please done this project as soon possible.')
    db.dmodals.insert( f0= 'sx4809', f1= '(4809)16 Sept')
    db.dmodals.insert( f0= 'hh4810', f1= '(4810)Sulaiman din')
    db.dmodals.insert( f0= 'pa4811', f1= '(4811)Please done this project as soon possible.')
    db.dmodals.insert( f0= 'sx4813', f1= '(4813)16 Sept')
    db.dmodals.insert( f0= 'hh4814', f1= '(4814)Victor Jara')
    db.dmodals.insert( f0= 'pa4815', f1= '(4815)Please done this project as soon possible.')
    db.dmodals.insert( f0= 'sx4817', f1= '(4817)16 Sept')
    db.dmodals.insert( f0= 'hh4818', f1= '(4818)Victor Jara')
    db.dmodals.insert( f0= 'pa4819', f1= '(4819)Please done this project as soon possible.')
    db.dmodals.insert( f0= 'aa4820', f1= '(4820)View All Messages')
    db.dmodals.insert( f0= 'hh4821', f1= '(4821)Notifications')
    db.dmodals.insert( f0= 'sx4822', f1= '(4822)16 Sept')
    db.dmodals.insert( f0= 'hh4823', f1= '(4823)Advanda Cro')
    db.dmodals.insert( f0= 'pa4824', f1= '(4824)Please done this project as soon possible.')
    db.dmodals.insert( f0= 'sx4825', f1= '(4825)16 Sept')
    db.dmodals.insert( f0= 'hh4826', f1= '(4826)Sulaiman din')
    db.dmodals.insert( f0= 'pa4827', f1= '(4827)Please done this project as soon possible.')
    db.dmodals.insert( f0= 'sx4828', f1= '(4828)16 Sept')
    db.dmodals.insert( f0= 'hh4829', f1= '(4829)Victor Jara')
    db.dmodals.insert( f0= 'pa4830', f1= '(4830)Please done this project as soon possible.')
    db.dmodals.insert( f0= 'sx4831', f1= '(4831)16 Sept')
    db.dmodals.insert( f0= 'hh4832', f1= '(4832)Victor Jara')
    db.dmodals.insert( f0= 'pa4833', f1= '(4833)Please done this project as soon possible.')
    db.dmodals.insert( f0= 'aa4834', f1= '(4834)View All Notification')
    db.dmodals.insert( f0= 'sx4835', f1= '(4835)Advanda Cro')
    db.dmodals.insert( f0= 'aa4839', f1= '(4839)News')
    db.dmodals.insert( f0= 'aa4840', f1= '(4840)Activity')
    db.dmodals.insert( f0= 'aa4841', f1= '(4841)Settings')
    db.dmodals.insert( f0= 'pa4842', f1= '(4842)You have 10 New News.')
    db.dmodals.insert( f0= 'pa4844', f1= '(4844)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dmodals.insert( f0= 'sp4845', f1= '(4845)Yesterday 2:45 pm')
    db.dmodals.insert( f0= 'pa4847', f1= '(4847)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dmodals.insert( f0= 'sp4848', f1= '(4848)Yesterday 2:45 pm')
    db.dmodals.insert( f0= 'pa4850', f1= '(4850)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dmodals.insert( f0= 'sp4851', f1= '(4851)Yesterday 2:45 pm')
    db.dmodals.insert( f0= 'pa4853', f1= '(4853)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dmodals.insert( f0= 'sp4854', f1= '(4854)Yesterday 2:45 pm')
    db.dmodals.insert( f0= 'pa4856', f1= '(4856)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dmodals.insert( f0= 'sp4857', f1= '(4857)Yesterday 2:45 pm')
    db.dmodals.insert( f0= 'pa4859', f1= '(4859)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dmodals.insert( f0= 'sp4860', f1= '(4860)Yesterday 2:45 pm')
    db.dmodals.insert( f0= 'pa4862', f1= '(4862)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dmodals.insert( f0= 'sp4863', f1= '(4863)Yesterday 2:45 pm')
    db.dmodals.insert( f0= 'pa4865', f1= '(4865)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dmodals.insert( f0= 'sp4866', f1= '(4866)Yesterday 2:45 pm')
    db.dmodals.insert( f0= 'pa4868', f1= '(4868)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dmodals.insert( f0= 'sp4869', f1= '(4869)Yesterday 2:45 pm')
    db.dmodals.insert( f0= 'pa4871', f1= '(4871)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dmodals.insert( f0= 'sp4872', f1= '(4872)Yesterday 2:45 pm')
    db.dmodals.insert( f0= 'pa4873', f1= '(4873)You have 20 Recent Activity.')
    db.dmodals.insert( f0= 'hh4874', f1= '(4874)New User Registered')
    db.dmodals.insert( f0= 'pa4875', f1= '(4875)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dmodals.insert( f0= 'sx4876', f1= '(4876)1 hours ago')
    db.dmodals.insert( f0= 'hh4877', f1= '(4877)New Order Received')
    db.dmodals.insert( f0= 'pa4878', f1= '(4878)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dmodals.insert( f0= 'sx4879', f1= '(4879)2 hours ago')
    db.dmodals.insert( f0= 'hh4880', f1= '(4880)New Order Received')
    db.dmodals.insert( f0= 'pa4881', f1= '(4881)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dmodals.insert( f0= 'sx4882', f1= '(4882)3 hours ago')
    db.dmodals.insert( f0= 'hh4883', f1= '(4883)New Order Received')
    db.dmodals.insert( f0= 'pa4884', f1= '(4884)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dmodals.insert( f0= 'sx4885', f1= '(4885)4 hours ago')
    db.dmodals.insert( f0= 'hh4886', f1= '(4886)New User Registered')
    db.dmodals.insert( f0= 'pa4887', f1= '(4887)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dmodals.insert( f0= 'sx4888', f1= '(4888)5 hours ago')
    db.dmodals.insert( f0= 'hh4889', f1= '(4889)New Order')
    db.dmodals.insert( f0= 'pa4890', f1= '(4890)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dmodals.insert( f0= 'sx4891', f1= '(4891)6 hours ago')
    db.dmodals.insert( f0= 'hh4892', f1= '(4892)New User')
    db.dmodals.insert( f0= 'pa4893', f1= '(4893)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dmodals.insert( f0= 'sx4894', f1= '(4894)7 hours ago')
    db.dmodals.insert( f0= 'hh4895', f1= '(4895)New Order')
    db.dmodals.insert( f0= 'pa4896', f1= '(4896)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dmodals.insert( f0= 'sx4897', f1= '(4897)9 hours ago')
    db.dmodals.insert( f0= 'pa4898', f1= '(4898)You have 20 Settings. 5 not completed.')
    db.dmodals.insert( f0= 'hh4899', f1= '(4899)Show notifications')
    db.dmodals.insert( f0= 'hh4900', f1= '(4900)Disable Chat')
    db.dmodals.insert( f0= 'hh4901', f1= '(4901)Enable history')
    db.dmodals.insert( f0= 'hh4902', f1= '(4902)Show charts')
    db.dmodals.insert( f0= 'hh4903', f1= '(4903)Update everyday')
    db.dmodals.insert( f0= 'hh4904', f1= '(4904)Global search')
    db.dmodals.insert( f0= 'hh4905', f1= '(4905)Offline users')
    db.dmodals.insert( f0= 'aa4907', f1= '(4907)Dashboard v.1')
    db.dmodals.insert( f0= 'aa4909', f1= '(4909)Dashboard v.2')
    db.dmodals.insert( f0= 'aa4911', f1= '(4911)Dashboard v.3')
    db.dmodals.insert( f0= 'aa4913', f1= '(4913)Product List')
    db.dmodals.insert( f0= 'aa4915', f1= '(4915)Product Edit')
    db.dmodals.insert( f0= 'aa4917', f1= '(4917)Product Detail')
    db.dmodals.insert( f0= 'aa4919', f1= '(4919)Product Cart')
    db.dmodals.insert( f0= 'aa4921', f1= '(4921)Product Payment')
    db.dmodals.insert( f0= 'aa4923', f1= '(4923)Analytics')
    db.dmodals.insert( f0= 'aa4925', f1= '(4925)Widgets')
    db.dmodals.insert( f0= 'aa4927', f1= '(4927)Inbox')
    db.dmodals.insert( f0= 'aa4929', f1= '(4929)View Mail')
    db.dmodals.insert( f0= 'aa4931', f1= '(4931)Compose Mail')
    db.dmodals.insert( f0= 'aa4933', f1= '(4933)File Manager')
    db.dmodals.insert( f0= 'aa4935', f1= '(4935)Contacts Client')
    db.dmodals.insert( f0= 'aa4937', f1= '(4937)Project')
    db.dmodals.insert( f0= 'aa4939', f1= '(4939)Project Details')
    db.dmodals.insert( f0= 'aa4941', f1= '(4941)Blog')
    db.dmodals.insert( f0= 'aa4943', f1= '(4943)Blog Details')
    db.dmodals.insert( f0= 'aa4945', f1= '(4945)404 Page')
    db.dmodals.insert( f0= 'aa4947', f1= '(4947)500 Page')
    db.dmodals.insert( f0= 'aa4949', f1= '(4949)Google Map')
    db.dmodals.insert( f0= 'aa4951', f1= '(4951)Data Maps')
    db.dmodals.insert( f0= 'aa4953', f1= '(4953)Pdf Viewer')
    db.dmodals.insert( f0= 'aa4955', f1= '(4955)X-Editable')
    db.dmodals.insert( f0= 'aa4957', f1= '(4957)Code Editor')
    db.dmodals.insert( f0= 'aa4959', f1= '(4959)Tree View')
    db.dmodals.insert( f0= 'aa4961', f1= '(4961)Preloader')
    db.dmodals.insert( f0= 'aa4963', f1= '(4963)Images Cropper')
    db.dmodals.insert( f0= 'aa4965', f1= '(4965)Bar Charts')
    db.dmodals.insert( f0= 'aa4967', f1= '(4967)Line Charts')
    db.dmodals.insert( f0= 'aa4969', f1= '(4969)Area Charts')
    db.dmodals.insert( f0= 'aa4971', f1= '(4971)Rounded Charts')
    db.dmodals.insert( f0= 'aa4973', f1= '(4973)C3 Charts')
    db.dmodals.insert( f0= 'aa4975', f1= '(4975)Sparkline Charts')
    db.dmodals.insert( f0= 'aa4977', f1= '(4977)Peity Charts')
    db.dmodals.insert( f0= 'aa4979', f1= '(4979)Static Table')
    db.dmodals.insert( f0= 'aa4981', f1= '(4981)Data Table')
    db.dmodals.insert( f0= 'aa4983', f1= '(4983)Basic Form Elements')
    db.dmodals.insert( f0= 'aa4985', f1= '(4985)Advanced Form Elements')
    db.dmodals.insert( f0= 'aa4987', f1= '(4987)Password Meter')
    db.dmodals.insert( f0= 'aa4989', f1= '(4989)Multi Upload')
    db.dmodals.insert( f0= 'aa4991', f1= '(4991)Text Editor')
    db.dmodals.insert( f0= 'aa4993', f1= '(4993)Dual List Box')
    db.dmodals.insert( f0= 'aa4995', f1= '(4995)Basic Form Elements')
    db.dmodals.insert( f0= 'aa4997', f1= '(4997)Advanced Form Elements')
    db.dmodals.insert( f0= 'aa4999', f1= '(4999)Password Meter')
    db.dmodals.insert( f0= 'aa5001', f1= '(5001)Multi Upload')
    db.dmodals.insert( f0= 'aa5003', f1= '(5003)Text Editor')
    db.dmodals.insert( f0= 'aa5005', f1= '(5005)Dual List Box')
    db.dmodals.insert( f0= 'aa5007', f1= '(5007)Login')
    db.dmodals.insert( f0= 'aa5009', f1= '(5009)Register')
    db.dmodals.insert( f0= 'aa5011', f1= '(5011)Lock')
    db.dmodals.insert( f0= 'aa5013', f1= '(5013)Password Recovery')
    db.dmodals.insert( f0= 'pb5014', f1= '(5014)Search...')
    db.dmodals.insert( f0= 'aa5015', f1= '(5015)Home')
    db.dmodals.insert( f0= 'sx5016', f1= '(5016)Modals')
    db.dmodals.insert( f0= 'hh5017', f1= '(5017)Custom Animate Modals Bootstrap')
    db.dmodals.insert( f0= 'hh5018', f1= '(5018)Alert Modal')
    db.dmodals.insert( f0= 'aa5019', f1= '(5019)Primary')
    db.dmodals.insert( f0= 'aa5020', f1= '(5020)Information')
    db.dmodals.insert( f0= 'aa5021', f1= '(5021)Warning')
    db.dmodals.insert( f0= 'aa5022', f1= '(5022)Danger')
    db.dmodals.insert( f0= 'aa5023', f1= '(5023)Alert')
    db.dmodals.insert( f0= 'hh5024', f1= '(5024)Awesome!')
    db.dmodals.insert( f0= 'pa5025', f1= '(5025)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5026', f1= '(5026)Cancel')
    db.dmodals.insert( f0= 'aa5027', f1= '(5027)Process')
    db.dmodals.insert( f0= 'hh5028', f1= '(5028)Information!')
    db.dmodals.insert( f0= 'pa5029', f1= '(5029)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5030', f1= '(5030)Cancel')
    db.dmodals.insert( f0= 'aa5031', f1= '(5031)Process')
    db.dmodals.insert( f0= 'hh5032', f1= '(5032)Warning!')
    db.dmodals.insert( f0= 'pa5033', f1= '(5033)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5034', f1= '(5034)Cancel')
    db.dmodals.insert( f0= 'aa5035', f1= '(5035)Process')
    db.dmodals.insert( f0= 'hh5036', f1= '(5036)Danger!')
    db.dmodals.insert( f0= 'pa5037', f1= '(5037)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5038', f1= '(5038)Cancel')
    db.dmodals.insert( f0= 'aa5039', f1= '(5039)Process')
    db.dmodals.insert( f0= 'hh5040', f1= '(5040)Alert!')
    db.dmodals.insert( f0= 'pa5041', f1= '(5041)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5042', f1= '(5042)Cancel')
    db.dmodals.insert( f0= 'aa5043', f1= '(5043)Process')
    db.dmodals.insert( f0= 'hh5044', f1= '(5044)Black Footer Modal')
    db.dmodals.insert( f0= 'aa5045', f1= '(5045)Primary')
    db.dmodals.insert( f0= 'aa5046', f1= '(5046)Information')
    db.dmodals.insert( f0= 'aa5047', f1= '(5047)Warning')
    db.dmodals.insert( f0= 'aa5048', f1= '(5048)Danger')
    db.dmodals.insert( f0= 'aa5049', f1= '(5049)Alert')
    db.dmodals.insert( f0= 'hh5050', f1= '(5050)Awesome!')
    db.dmodals.insert( f0= 'pa5051', f1= '(5051)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5052', f1= '(5052)Cancel')
    db.dmodals.insert( f0= 'aa5053', f1= '(5053)Process')
    db.dmodals.insert( f0= 'hh5054', f1= '(5054)Information!')
    db.dmodals.insert( f0= 'pa5055', f1= '(5055)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5056', f1= '(5056)Cancel')
    db.dmodals.insert( f0= 'aa5057', f1= '(5057)Process')
    db.dmodals.insert( f0= 'hh5058', f1= '(5058)Warning!')
    db.dmodals.insert( f0= 'pa5059', f1= '(5059)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5060', f1= '(5060)Cancel')
    db.dmodals.insert( f0= 'aa5061', f1= '(5061)Process')
    db.dmodals.insert( f0= 'hh5062', f1= '(5062)Danger!')
    db.dmodals.insert( f0= 'pa5063', f1= '(5063)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5064', f1= '(5064)Cancel')
    db.dmodals.insert( f0= 'aa5065', f1= '(5065)Process')
    db.dmodals.insert( f0= 'hh5066', f1= '(5066)Alert!')
    db.dmodals.insert( f0= 'pa5067', f1= '(5067)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5068', f1= '(5068)Cancel')
    db.dmodals.insert( f0= 'aa5069', f1= '(5069)Process')
    db.dmodals.insert( f0= 'hh5070', f1= '(5070)Header BG Color Modal')
    db.dmodals.insert( f0= 'aa5071', f1= '(5071)Primary')
    db.dmodals.insert( f0= 'aa5072', f1= '(5072)Information')
    db.dmodals.insert( f0= 'aa5073', f1= '(5073)Warning')
    db.dmodals.insert( f0= 'aa5074', f1= '(5074)Danger')
    db.dmodals.insert( f0= 'aa5075', f1= '(5075)Alert')
    db.dmodals.insert( f0= 'hd5076', f1= '(5076)BG Color Header Modal')
    db.dmodals.insert( f0= 'hh5077', f1= '(5077)Awesome!')
    db.dmodals.insert( f0= 'pa5078', f1= '(5078)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5079', f1= '(5079)Cancel')
    db.dmodals.insert( f0= 'aa5080', f1= '(5080)Process')
    db.dmodals.insert( f0= 'hd5081', f1= '(5081)BG Color Header Modal')
    db.dmodals.insert( f0= 'hh5082', f1= '(5082)Information!')
    db.dmodals.insert( f0= 'pa5083', f1= '(5083)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5084', f1= '(5084)Cancel')
    db.dmodals.insert( f0= 'aa5085', f1= '(5085)Process')
    db.dmodals.insert( f0= 'hd5086', f1= '(5086)BG Color Header Modal')
    db.dmodals.insert( f0= 'hh5087', f1= '(5087)Warning!')
    db.dmodals.insert( f0= 'pa5088', f1= '(5088)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5089', f1= '(5089)Cancel')
    db.dmodals.insert( f0= 'aa5090', f1= '(5090)Process')
    db.dmodals.insert( f0= 'hd5091', f1= '(5091)BG Color Header Modal')
    db.dmodals.insert( f0= 'hh5092', f1= '(5092)Danger!')
    db.dmodals.insert( f0= 'pa5093', f1= '(5093)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5094', f1= '(5094)Cancel')
    db.dmodals.insert( f0= 'aa5095', f1= '(5095)Process')
    db.dmodals.insert( f0= 'hd5096', f1= '(5096)BG Color Header Modal')
    db.dmodals.insert( f0= 'hh5097', f1= '(5097)Alert!')
    db.dmodals.insert( f0= 'pa5098', f1= '(5098)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5099', f1= '(5099)Cancel')
    db.dmodals.insert( f0= 'aa5100', f1= '(5100)Process')
    db.dmodals.insert( f0= 'hh5101', f1= '(5101)Black Background Modal')
    db.dmodals.insert( f0= 'aa5102', f1= '(5102)Primary')
    db.dmodals.insert( f0= 'aa5103', f1= '(5103)Information')
    db.dmodals.insert( f0= 'aa5104', f1= '(5104)Warning')
    db.dmodals.insert( f0= 'aa5105', f1= '(5105)Danger')
    db.dmodals.insert( f0= 'aa5106', f1= '(5106)Alert')
    db.dmodals.insert( f0= 'hh5107', f1= '(5107)Awesome!')
    db.dmodals.insert( f0= 'pa5108', f1= '(5108)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5109', f1= '(5109)Cancel')
    db.dmodals.insert( f0= 'aa5110', f1= '(5110)Process')
    db.dmodals.insert( f0= 'hh5111', f1= '(5111)Information!')
    db.dmodals.insert( f0= 'pa5112', f1= '(5112)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5113', f1= '(5113)Cancel')
    db.dmodals.insert( f0= 'aa5114', f1= '(5114)Process')
    db.dmodals.insert( f0= 'hh5115', f1= '(5115)Warning!')
    db.dmodals.insert( f0= 'pa5116', f1= '(5116)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5117', f1= '(5117)Cancel')
    db.dmodals.insert( f0= 'aa5118', f1= '(5118)Process')
    db.dmodals.insert( f0= 'hh5119', f1= '(5119)Danger!')
    db.dmodals.insert( f0= 'pa5120', f1= '(5120)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5121', f1= '(5121)Cancel')
    db.dmodals.insert( f0= 'aa5122', f1= '(5122)Process')
    db.dmodals.insert( f0= 'hh5123', f1= '(5123)Alert!')
    db.dmodals.insert( f0= 'pa5124', f1= '(5124)The Modal plugin is a dialog box/popup window that is displayed on top of the current page')
    db.dmodals.insert( f0= 'aa5125', f1= '(5125)Cancel')
    db.dmodals.insert( f0= 'aa5126', f1= '(5126)Process')
    db.dmodals.insert( f0= 'pc5127', f1= '(5127)All rights reserved.')
    db.dmodals.insert( f0= 'pf5128', f1= '(5128)Copyright &copy; 2018')
    db.commit()
#
