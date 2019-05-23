#
# table for controller: product_edit
#

from gluon.contrib.populate import populate

db.define_table('dproduct0edit', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dproduct0edit.id ).count():
    db.dproduct0edit.insert( f0= 'sp6392', f1= '(6392)outdated')
    db.dproduct0edit.insert( f0= 'pc6393', f1= '(6393)to improve your experience.')
    db.dproduct0edit.insert( f0= 'aa6394', f1= '(6394)upgrade your browser')
    db.dproduct0edit.insert( f0= 'sx6399', f1= '(6399)Ecommerce')
    db.dproduct0edit.insert( f0= 'sx6401', f1= '(6401)Dashboard v.1')
    db.dproduct0edit.insert( f0= 'sx6403', f1= '(6403)Dashboard v.2')
    db.dproduct0edit.insert( f0= 'sx6405', f1= '(6405)Dashboard v.3')
    db.dproduct0edit.insert( f0= 'sx6407', f1= '(6407)Product List')
    db.dproduct0edit.insert( f0= 'sx6409', f1= '(6409)Product Edit')
    db.dproduct0edit.insert( f0= 'sx6411', f1= '(6411)Product Detail')
    db.dproduct0edit.insert( f0= 'sx6413', f1= '(6413)Product Cart')
    db.dproduct0edit.insert( f0= 'sx6415', f1= '(6415)Product Payment')
    db.dproduct0edit.insert( f0= 'sx6417', f1= '(6417)Analytics')
    db.dproduct0edit.insert( f0= 'sx6419', f1= '(6419)Widgets')
    db.dproduct0edit.insert( f0= 'sx6421', f1= '(6421)Mailbox')
    db.dproduct0edit.insert( f0= 'sx6423', f1= '(6423)Inbox')
    db.dproduct0edit.insert( f0= 'sx6425', f1= '(6425)View Mail')
    db.dproduct0edit.insert( f0= 'sx6427', f1= '(6427)Compose Mail')
    db.dproduct0edit.insert( f0= 'sx6429', f1= '(6429)Interface')
    db.dproduct0edit.insert( f0= 'sx6431', f1= '(6431)Google Map')
    db.dproduct0edit.insert( f0= 'sx6433', f1= '(6433)Data Maps')
    db.dproduct0edit.insert( f0= 'sx6435', f1= '(6435)Pdf Viewer')
    db.dproduct0edit.insert( f0= 'sx6437', f1= '(6437)X-Editable')
    db.dproduct0edit.insert( f0= 'sx6439', f1= '(6439)Code Editor')
    db.dproduct0edit.insert( f0= 'sx6441', f1= '(6441)Tree View')
    db.dproduct0edit.insert( f0= 'sx6443', f1= '(6443)Preloader')
    db.dproduct0edit.insert( f0= 'sx6445', f1= '(6445)Images Cropper')
    db.dproduct0edit.insert( f0= 'sx6447', f1= '(6447)Miscellaneous')
    db.dproduct0edit.insert( f0= 'sx6449', f1= '(6449)File Manager')
    db.dproduct0edit.insert( f0= 'sx6451', f1= '(6451)Blog')
    db.dproduct0edit.insert( f0= 'sx6453', f1= '(6453)Blog Details')
    db.dproduct0edit.insert( f0= 'sx6455', f1= '(6455)404 Page')
    db.dproduct0edit.insert( f0= 'sx6457', f1= '(6457)500 Page')
    db.dproduct0edit.insert( f0= 'sx6459', f1= '(6459)Charts')
    db.dproduct0edit.insert( f0= 'sx6461', f1= '(6461)Bar Charts')
    db.dproduct0edit.insert( f0= 'sx6463', f1= '(6463)Line Charts')
    db.dproduct0edit.insert( f0= 'sx6465', f1= '(6465)Area Charts')
    db.dproduct0edit.insert( f0= 'sx6467', f1= '(6467)Rounded Charts')
    db.dproduct0edit.insert( f0= 'sx6469', f1= '(6469)C3 Charts')
    db.dproduct0edit.insert( f0= 'sx6471', f1= '(6471)Sparkline Charts')
    db.dproduct0edit.insert( f0= 'sx6473', f1= '(6473)Peity Charts')
    db.dproduct0edit.insert( f0= 'sx6475', f1= '(6475)Data Tables')
    db.dproduct0edit.insert( f0= 'sx6477', f1= '(6477)Static Table')
    db.dproduct0edit.insert( f0= 'sx6479', f1= '(6479)Data Table')
    db.dproduct0edit.insert( f0= 'sx6481', f1= '(6481)Forms Elements')
    db.dproduct0edit.insert( f0= 'sx6483', f1= '(6483)Bc Form Elements')
    db.dproduct0edit.insert( f0= 'sx6485', f1= '(6485)Ad Form Elements')
    db.dproduct0edit.insert( f0= 'sx6487', f1= '(6487)Password Meter')
    db.dproduct0edit.insert( f0= 'sx6489', f1= '(6489)Multi Upload')
    db.dproduct0edit.insert( f0= 'sx6491', f1= '(6491)Text Editor')
    db.dproduct0edit.insert( f0= 'sx6493', f1= '(6493)Dual List Box')
    db.dproduct0edit.insert( f0= 'sx6495', f1= '(6495)App views')
    db.dproduct0edit.insert( f0= 'sx6497', f1= '(6497)Notifications')
    db.dproduct0edit.insert( f0= 'sx6499', f1= '(6499)Alerts')
    db.dproduct0edit.insert( f0= 'sx6501', f1= '(6501)Modals')
    db.dproduct0edit.insert( f0= 'sx6503', f1= '(6503)Buttons')
    db.dproduct0edit.insert( f0= 'sx6505', f1= '(6505)Tabs')
    db.dproduct0edit.insert( f0= 'sx6507', f1= '(6507)Accordion')
    db.dproduct0edit.insert( f0= 'sx6508', f1= '(6508)Pages')
    db.dproduct0edit.insert( f0= 'sx6510', f1= '(6510)Login')
    db.dproduct0edit.insert( f0= 'sx6512', f1= '(6512)Register')
    db.dproduct0edit.insert( f0= 'sx6514', f1= '(6514)Lock')
    db.dproduct0edit.insert( f0= 'sx6516', f1= '(6516)Password Recovery')
    db.dproduct0edit.insert( f0= 'sx6517', f1= '(6517)Landing Page')
    db.dproduct0edit.insert( f0= 'aa6520', f1= '(6520)Home')
    db.dproduct0edit.insert( f0= 'aa6521', f1= '(6521)About')
    db.dproduct0edit.insert( f0= 'aa6522', f1= '(6522)Services')
    db.dproduct0edit.insert( f0= 'aa6523', f1= '(6523)Support')
    db.dproduct0edit.insert( f0= 'hh6524', f1= '(6524)Message')
    db.dproduct0edit.insert( f0= 'sx6526', f1= '(6526)16 Sept')
    db.dproduct0edit.insert( f0= 'hh6527', f1= '(6527)Advanda Cro')
    db.dproduct0edit.insert( f0= 'pa6528', f1= '(6528)Please done this project as soon possible.')
    db.dproduct0edit.insert( f0= 'sx6530', f1= '(6530)16 Sept')
    db.dproduct0edit.insert( f0= 'hh6531', f1= '(6531)Sulaiman din')
    db.dproduct0edit.insert( f0= 'pa6532', f1= '(6532)Please done this project as soon possible.')
    db.dproduct0edit.insert( f0= 'sx6534', f1= '(6534)16 Sept')
    db.dproduct0edit.insert( f0= 'hh6535', f1= '(6535)Victor Jara')
    db.dproduct0edit.insert( f0= 'pa6536', f1= '(6536)Please done this project as soon possible.')
    db.dproduct0edit.insert( f0= 'sx6538', f1= '(6538)16 Sept')
    db.dproduct0edit.insert( f0= 'hh6539', f1= '(6539)Victor Jara')
    db.dproduct0edit.insert( f0= 'pa6540', f1= '(6540)Please done this project as soon possible.')
    db.dproduct0edit.insert( f0= 'aa6541', f1= '(6541)View All Messages')
    db.dproduct0edit.insert( f0= 'hh6542', f1= '(6542)Notifications')
    db.dproduct0edit.insert( f0= 'sx6543', f1= '(6543)16 Sept')
    db.dproduct0edit.insert( f0= 'hh6544', f1= '(6544)Advanda Cro')
    db.dproduct0edit.insert( f0= 'pa6545', f1= '(6545)Please done this project as soon possible.')
    db.dproduct0edit.insert( f0= 'sx6546', f1= '(6546)16 Sept')
    db.dproduct0edit.insert( f0= 'hh6547', f1= '(6547)Sulaiman din')
    db.dproduct0edit.insert( f0= 'pa6548', f1= '(6548)Please done this project as soon possible.')
    db.dproduct0edit.insert( f0= 'sx6549', f1= '(6549)16 Sept')
    db.dproduct0edit.insert( f0= 'hh6550', f1= '(6550)Victor Jara')
    db.dproduct0edit.insert( f0= 'pa6551', f1= '(6551)Please done this project as soon possible.')
    db.dproduct0edit.insert( f0= 'sx6552', f1= '(6552)16 Sept')
    db.dproduct0edit.insert( f0= 'hh6553', f1= '(6553)Victor Jara')
    db.dproduct0edit.insert( f0= 'pa6554', f1= '(6554)Please done this project as soon possible.')
    db.dproduct0edit.insert( f0= 'aa6555', f1= '(6555)View All Notification')
    db.dproduct0edit.insert( f0= 'sx6556', f1= '(6556)Advanda Cro')
    db.dproduct0edit.insert( f0= 'aa6560', f1= '(6560)News')
    db.dproduct0edit.insert( f0= 'aa6561', f1= '(6561)Activity')
    db.dproduct0edit.insert( f0= 'aa6562', f1= '(6562)Settings')
    db.dproduct0edit.insert( f0= 'pa6563', f1= '(6563)You have 10 New News.')
    db.dproduct0edit.insert( f0= 'pa6565', f1= '(6565)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dproduct0edit.insert( f0= 'sp6566', f1= '(6566)Yesterday 2:45 pm')
    db.dproduct0edit.insert( f0= 'pa6568', f1= '(6568)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dproduct0edit.insert( f0= 'sp6569', f1= '(6569)Yesterday 2:45 pm')
    db.dproduct0edit.insert( f0= 'pa6571', f1= '(6571)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dproduct0edit.insert( f0= 'sp6572', f1= '(6572)Yesterday 2:45 pm')
    db.dproduct0edit.insert( f0= 'pa6574', f1= '(6574)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dproduct0edit.insert( f0= 'sp6575', f1= '(6575)Yesterday 2:45 pm')
    db.dproduct0edit.insert( f0= 'pa6577', f1= '(6577)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dproduct0edit.insert( f0= 'sp6578', f1= '(6578)Yesterday 2:45 pm')
    db.dproduct0edit.insert( f0= 'pa6580', f1= '(6580)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dproduct0edit.insert( f0= 'sp6581', f1= '(6581)Yesterday 2:45 pm')
    db.dproduct0edit.insert( f0= 'pa6583', f1= '(6583)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dproduct0edit.insert( f0= 'sp6584', f1= '(6584)Yesterday 2:45 pm')
    db.dproduct0edit.insert( f0= 'pa6586', f1= '(6586)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dproduct0edit.insert( f0= 'sp6587', f1= '(6587)Yesterday 2:45 pm')
    db.dproduct0edit.insert( f0= 'pa6589', f1= '(6589)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dproduct0edit.insert( f0= 'sp6590', f1= '(6590)Yesterday 2:45 pm')
    db.dproduct0edit.insert( f0= 'pa6592', f1= '(6592)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dproduct0edit.insert( f0= 'sp6593', f1= '(6593)Yesterday 2:45 pm')
    db.dproduct0edit.insert( f0= 'pa6594', f1= '(6594)You have 20 Recent Activity.')
    db.dproduct0edit.insert( f0= 'hh6595', f1= '(6595)New User Registered')
    db.dproduct0edit.insert( f0= 'pa6596', f1= '(6596)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dproduct0edit.insert( f0= 'sx6597', f1= '(6597)1 hours ago')
    db.dproduct0edit.insert( f0= 'hh6598', f1= '(6598)New Order Received')
    db.dproduct0edit.insert( f0= 'pa6599', f1= '(6599)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dproduct0edit.insert( f0= 'sx6600', f1= '(6600)2 hours ago')
    db.dproduct0edit.insert( f0= 'hh6601', f1= '(6601)New Order Received')
    db.dproduct0edit.insert( f0= 'pa6602', f1= '(6602)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dproduct0edit.insert( f0= 'sx6603', f1= '(6603)3 hours ago')
    db.dproduct0edit.insert( f0= 'hh6604', f1= '(6604)New Order Received')
    db.dproduct0edit.insert( f0= 'pa6605', f1= '(6605)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dproduct0edit.insert( f0= 'sx6606', f1= '(6606)4 hours ago')
    db.dproduct0edit.insert( f0= 'hh6607', f1= '(6607)New User Registered')
    db.dproduct0edit.insert( f0= 'pa6608', f1= '(6608)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dproduct0edit.insert( f0= 'sx6609', f1= '(6609)5 hours ago')
    db.dproduct0edit.insert( f0= 'hh6610', f1= '(6610)New Order')
    db.dproduct0edit.insert( f0= 'pa6611', f1= '(6611)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dproduct0edit.insert( f0= 'sx6612', f1= '(6612)6 hours ago')
    db.dproduct0edit.insert( f0= 'hh6613', f1= '(6613)New User')
    db.dproduct0edit.insert( f0= 'pa6614', f1= '(6614)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dproduct0edit.insert( f0= 'sx6615', f1= '(6615)7 hours ago')
    db.dproduct0edit.insert( f0= 'hh6616', f1= '(6616)New Order')
    db.dproduct0edit.insert( f0= 'pa6617', f1= '(6617)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dproduct0edit.insert( f0= 'sx6618', f1= '(6618)9 hours ago')
    db.dproduct0edit.insert( f0= 'pa6619', f1= '(6619)You have 20 Settings. 5 not completed.')
    db.dproduct0edit.insert( f0= 'hh6620', f1= '(6620)Show notifications')
    db.dproduct0edit.insert( f0= 'hh6621', f1= '(6621)Disable Chat')
    db.dproduct0edit.insert( f0= 'hh6622', f1= '(6622)Enable history')
    db.dproduct0edit.insert( f0= 'hh6623', f1= '(6623)Show charts')
    db.dproduct0edit.insert( f0= 'hh6624', f1= '(6624)Update everyday')
    db.dproduct0edit.insert( f0= 'hh6625', f1= '(6625)Global search')
    db.dproduct0edit.insert( f0= 'hh6626', f1= '(6626)Offline users')
    db.dproduct0edit.insert( f0= 'aa6628', f1= '(6628)Dashboard v.1')
    db.dproduct0edit.insert( f0= 'aa6630', f1= '(6630)Dashboard v.2')
    db.dproduct0edit.insert( f0= 'aa6632', f1= '(6632)Dashboard v.3')
    db.dproduct0edit.insert( f0= 'aa6634', f1= '(6634)Product List')
    db.dproduct0edit.insert( f0= 'aa6636', f1= '(6636)Product Edit')
    db.dproduct0edit.insert( f0= 'aa6638', f1= '(6638)Product Detail')
    db.dproduct0edit.insert( f0= 'aa6640', f1= '(6640)Product Cart')
    db.dproduct0edit.insert( f0= 'aa6642', f1= '(6642)Product Payment')
    db.dproduct0edit.insert( f0= 'aa6644', f1= '(6644)Analytics')
    db.dproduct0edit.insert( f0= 'aa6646', f1= '(6646)Widgets')
    db.dproduct0edit.insert( f0= 'aa6648', f1= '(6648)Inbox')
    db.dproduct0edit.insert( f0= 'aa6650', f1= '(6650)View Mail')
    db.dproduct0edit.insert( f0= 'aa6652', f1= '(6652)Compose Mail')
    db.dproduct0edit.insert( f0= 'aa6654', f1= '(6654)File Manager')
    db.dproduct0edit.insert( f0= 'aa6656', f1= '(6656)Contacts Client')
    db.dproduct0edit.insert( f0= 'aa6658', f1= '(6658)Project')
    db.dproduct0edit.insert( f0= 'aa6660', f1= '(6660)Project Details')
    db.dproduct0edit.insert( f0= 'aa6662', f1= '(6662)Blog')
    db.dproduct0edit.insert( f0= 'aa6664', f1= '(6664)Blog Details')
    db.dproduct0edit.insert( f0= 'aa6666', f1= '(6666)404 Page')
    db.dproduct0edit.insert( f0= 'aa6668', f1= '(6668)500 Page')
    db.dproduct0edit.insert( f0= 'aa6670', f1= '(6670)Google Map')
    db.dproduct0edit.insert( f0= 'aa6672', f1= '(6672)Data Maps')
    db.dproduct0edit.insert( f0= 'aa6674', f1= '(6674)Pdf Viewer')
    db.dproduct0edit.insert( f0= 'aa6676', f1= '(6676)X-Editable')
    db.dproduct0edit.insert( f0= 'aa6678', f1= '(6678)Code Editor')
    db.dproduct0edit.insert( f0= 'aa6680', f1= '(6680)Tree View')
    db.dproduct0edit.insert( f0= 'aa6682', f1= '(6682)Preloader')
    db.dproduct0edit.insert( f0= 'aa6684', f1= '(6684)Images Cropper')
    db.dproduct0edit.insert( f0= 'aa6686', f1= '(6686)Bar Charts')
    db.dproduct0edit.insert( f0= 'aa6688', f1= '(6688)Line Charts')
    db.dproduct0edit.insert( f0= 'aa6690', f1= '(6690)Area Charts')
    db.dproduct0edit.insert( f0= 'aa6692', f1= '(6692)Rounded Charts')
    db.dproduct0edit.insert( f0= 'aa6694', f1= '(6694)C3 Charts')
    db.dproduct0edit.insert( f0= 'aa6696', f1= '(6696)Sparkline Charts')
    db.dproduct0edit.insert( f0= 'aa6698', f1= '(6698)Peity Charts')
    db.dproduct0edit.insert( f0= 'aa6700', f1= '(6700)Static Table')
    db.dproduct0edit.insert( f0= 'aa6702', f1= '(6702)Data Table')
    db.dproduct0edit.insert( f0= 'aa6704', f1= '(6704)Basic Form Elements')
    db.dproduct0edit.insert( f0= 'aa6706', f1= '(6706)Advanced Form Elements')
    db.dproduct0edit.insert( f0= 'aa6708', f1= '(6708)Password Meter')
    db.dproduct0edit.insert( f0= 'aa6710', f1= '(6710)Multi Upload')
    db.dproduct0edit.insert( f0= 'aa6712', f1= '(6712)Text Editor')
    db.dproduct0edit.insert( f0= 'aa6714', f1= '(6714)Dual List Box')
    db.dproduct0edit.insert( f0= 'aa6716', f1= '(6716)Basic Form Elements')
    db.dproduct0edit.insert( f0= 'aa6718', f1= '(6718)Advanced Form Elements')
    db.dproduct0edit.insert( f0= 'aa6720', f1= '(6720)Password Meter')
    db.dproduct0edit.insert( f0= 'aa6722', f1= '(6722)Multi Upload')
    db.dproduct0edit.insert( f0= 'aa6724', f1= '(6724)Text Editor')
    db.dproduct0edit.insert( f0= 'aa6726', f1= '(6726)Dual List Box')
    db.dproduct0edit.insert( f0= 'aa6728', f1= '(6728)Login')
    db.dproduct0edit.insert( f0= 'aa6730', f1= '(6730)Register')
    db.dproduct0edit.insert( f0= 'aa6732', f1= '(6732)Lock')
    db.dproduct0edit.insert( f0= 'aa6734', f1= '(6734)Password Recovery')
    db.dproduct0edit.insert( f0= 'pb6735', f1= '(6735)Search...')
    db.dproduct0edit.insert( f0= 'aa6736', f1= '(6736)Home')
    db.dproduct0edit.insert( f0= 'sx6737', f1= '(6737)Product Edit')
    db.dproduct0edit.insert( f0= 'pb6738', f1= '(6738)First Name')
    db.dproduct0edit.insert( f0= 'pb6739', f1= '(6739)Product Title')
    db.dproduct0edit.insert( f0= 'pb6740', f1= '(6740)Regular Price')
    db.dproduct0edit.insert( f0= 'pb6741', f1= '(6741)Tax')
    db.dproduct0edit.insert( f0= 'pb6742', f1= '(6742)Quantity')
    db.dproduct0edit.insert( f0= 'pb6743', f1= '(6743)Last Name')
    db.dproduct0edit.insert( f0= 'pb6744', f1= '(6744)Product Description')
    db.dproduct0edit.insert( f0= 'pb6745', f1= '(6745)Sale Price')
    db.dproduct0edit.insert( f0= 'pb6746', f1= '(6746)Category')
    db.dproduct0edit.insert( f0= 'sx6748', f1= '(6748)TT')
    db.dproduct0edit.insert( f0= 'pb6749', f1= '(6749)Label Name')
    db.dproduct0edit.insert( f0= 'sx6751', f1= '(6751)TT')
    db.dproduct0edit.insert( f0= 'pb6752', f1= '(6752)Label Name')
    db.dproduct0edit.insert( f0= 'sx6754', f1= '(6754)TT')
    db.dproduct0edit.insert( f0= 'pb6755', f1= '(6755)Label Name')
    db.dproduct0edit.insert( f0= 'pa6756', f1= '(6756)No reviews yet.')
    db.dproduct0edit.insert( f0= 'pa6757', f1= '(6757)Your Rating')
    db.dproduct0edit.insert( f0= 'pb6758', f1= '(6758)User Name')
    db.dproduct0edit.insert( f0= 'pb6759', f1= '(6759)Last Name')
    db.dproduct0edit.insert( f0= 'pb6760', f1= '(6760)Email')
    db.dproduct0edit.insert( f0= 'pc6761', f1= '(6761)All rights reserved.')
    db.dproduct0edit.insert( f0= 'pf6762', f1= '(6762)Copyright &copy; 2018')
    db.commit()
#
