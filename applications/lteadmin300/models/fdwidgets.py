#
# table for controller: widgets
#

from gluon.contrib.populate import populate

db.define_table('dwidgets', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dwidgets.id ).count():
    db.dwidgets.insert( f0= 'aa6476', f1= '(6476)Home')
    db.dwidgets.insert( f0= 'aa6477', f1= '(6477)Contact')
    db.dwidgets.insert( f0= 'pb6478', f1= '(6478)Search')
    db.dwidgets.insert( f0= 'sx6479', f1= '(6479)3')
    db.dwidgets.insert( f0= 'pc6481', f1= '(6481)Call me whenever you can...')
    db.dwidgets.insert( f0= 'pc6482', f1= '(6482)4 Hours Ago')
    db.dwidgets.insert( f0= 'pc6484', f1= '(6484)I got your message bro')
    db.dwidgets.insert( f0= 'pc6485', f1= '(6485)4 Hours Ago')
    db.dwidgets.insert( f0= 'pc6487', f1= '(6487)The subject goes here')
    db.dwidgets.insert( f0= 'pc6488', f1= '(6488)4 Hours Ago')
    db.dwidgets.insert( f0= 'aa6489', f1= '(6489)See All Messages')
    db.dwidgets.insert( f0= 'sx6490', f1= '(6490)15 Notifications')
    db.dwidgets.insert( f0= 'sx6491', f1= '(6491)3 mins')
    db.dwidgets.insert( f0= 'sx6492', f1= '(6492)12 hours')
    db.dwidgets.insert( f0= 'sx6493', f1= '(6493)2 days')
    db.dwidgets.insert( f0= 'aa6494', f1= '(6494)See All Notifications')
    db.dwidgets.insert( f0= 'sx6497', f1= '(6497)AdminLTE 3')
    db.dwidgets.insert( f0= 'aa6499', f1= '(6499)Alexander Pierce')
    db.dwidgets.insert( f0= 'pa6501', f1= '(6501)Dashboard v1')
    db.dwidgets.insert( f0= 'pa6503', f1= '(6503)Dashboard v2')
    db.dwidgets.insert( f0= 'pa6505', f1= '(6505)Dashboard v3')
    db.dwidgets.insert( f0= 'sx6507', f1= '(6507)New')
    db.dwidgets.insert( f0= 'sx6508', f1= '(6508)6')
    db.dwidgets.insert( f0= 'pa6510', f1= '(6510)Top Navigation')
    db.dwidgets.insert( f0= 'pa6512', f1= '(6512)Boxed')
    db.dwidgets.insert( f0= 'pa6514', f1= '(6514)Fixed Sidebar')
    db.dwidgets.insert( f0= 'pa6516', f1= '(6516)Fixed Navbar')
    db.dwidgets.insert( f0= 'pa6518', f1= '(6518)Fixed Footer')
    db.dwidgets.insert( f0= 'pa6520', f1= '(6520)Collapsed Sidebar')
    db.dwidgets.insert( f0= 'pa6522', f1= '(6522)ChartJS')
    db.dwidgets.insert( f0= 'pa6524', f1= '(6524)Flot')
    db.dwidgets.insert( f0= 'pa6526', f1= '(6526)Inline')
    db.dwidgets.insert( f0= 'pa6528', f1= '(6528)General')
    db.dwidgets.insert( f0= 'pa6530', f1= '(6530)Icons')
    db.dwidgets.insert( f0= 'pa6532', f1= '(6532)Buttons')
    db.dwidgets.insert( f0= 'pa6534', f1= '(6534)Sliders')
    db.dwidgets.insert( f0= 'pa6536', f1= '(6536)Modals & Alerts')
    db.dwidgets.insert( f0= 'pa6538', f1= '(6538)Navbar & Tabs')
    db.dwidgets.insert( f0= 'pa6540', f1= '(6540)Timeline')
    db.dwidgets.insert( f0= 'pa6542', f1= '(6542)Ribbons')
    db.dwidgets.insert( f0= 'pa6544', f1= '(6544)General Elements')
    db.dwidgets.insert( f0= 'pa6546', f1= '(6546)Advanced Elements')
    db.dwidgets.insert( f0= 'pa6548', f1= '(6548)Editors')
    db.dwidgets.insert( f0= 'pa6550', f1= '(6550)Simple Tables')
    db.dwidgets.insert( f0= 'pa6552', f1= '(6552)DataTables')
    db.dwidgets.insert( f0= 'pa6554', f1= '(6554)jsGrid')
    db.dwidgets.insert( f0= 'lb6555', f1= '(6555)EXAMPLES')
    db.dwidgets.insert( f0= 'sx6557', f1= '(6557)2')
    db.dwidgets.insert( f0= 'pa6560', f1= '(6560)Inbox')
    db.dwidgets.insert( f0= 'pa6562', f1= '(6562)Compose')
    db.dwidgets.insert( f0= 'pa6564', f1= '(6564)Read')
    db.dwidgets.insert( f0= 'pa6566', f1= '(6566)Invoice')
    db.dwidgets.insert( f0= 'pa6568', f1= '(6568)Profile')
    db.dwidgets.insert( f0= 'pa6570', f1= '(6570)E-commerce')
    db.dwidgets.insert( f0= 'pa6572', f1= '(6572)Projects')
    db.dwidgets.insert( f0= 'pa6574', f1= '(6574)Project Add')
    db.dwidgets.insert( f0= 'pa6576', f1= '(6576)Project Edit')
    db.dwidgets.insert( f0= 'pa6578', f1= '(6578)Project Detail')
    db.dwidgets.insert( f0= 'pa6580', f1= '(6580)Contacts')
    db.dwidgets.insert( f0= 'pa6582', f1= '(6582)Login')
    db.dwidgets.insert( f0= 'pa6584', f1= '(6584)Register')
    db.dwidgets.insert( f0= 'pa6586', f1= '(6586)Forgot Password')
    db.dwidgets.insert( f0= 'pa6588', f1= '(6588)Recover Password')
    db.dwidgets.insert( f0= 'pa6590', f1= '(6590)Lockscreen')
    db.dwidgets.insert( f0= 'pa6592', f1= '(6592)Legacy User Menu')
    db.dwidgets.insert( f0= 'pa6594', f1= '(6594)Language Menu')
    db.dwidgets.insert( f0= 'pa6596', f1= '(6596)Error 404')
    db.dwidgets.insert( f0= 'pa6598', f1= '(6598)Error 500')
    db.dwidgets.insert( f0= 'pa6600', f1= '(6600)Pace')
    db.dwidgets.insert( f0= 'pa6602', f1= '(6602)Blank Page')
    db.dwidgets.insert( f0= 'pa6604', f1= '(6604)Starter Page')
    db.dwidgets.insert( f0= 'lb6605', f1= '(6605)MISCELLANEOUS')
    db.dwidgets.insert( f0= 'pa6606', f1= '(6606)Documentation')
    db.dwidgets.insert( f0= 'lb6607', f1= '(6607)MULTI LEVEL EXAMPLE')
    db.dwidgets.insert( f0= 'pa6608', f1= '(6608)Level 1')
    db.dwidgets.insert( f0= 'pa6609', f1= '(6609)Level 2')
    db.dwidgets.insert( f0= 'pa6610', f1= '(6610)Level 3')
    db.dwidgets.insert( f0= 'pa6611', f1= '(6611)Level 3')
    db.dwidgets.insert( f0= 'pa6612', f1= '(6612)Level 3')
    db.dwidgets.insert( f0= 'pa6613', f1= '(6613)Level 2')
    db.dwidgets.insert( f0= 'pa6614', f1= '(6614)Level 1')
    db.dwidgets.insert( f0= 'lb6615', f1= '(6615)LABELS')
    db.dwidgets.insert( f0= 'pc6616', f1= '(6616)Important')
    db.dwidgets.insert( f0= 'pa6617', f1= '(6617)Warning')
    db.dwidgets.insert( f0= 'pa6618', f1= '(6618)Informational')
    db.dwidgets.insert( f0= 'hh6619', f1= '(6619)Widgets')
    db.dwidgets.insert( f0= 'aa6620', f1= '(6620)Home')
    db.dwidgets.insert( f0= 'lb6621', f1= '(6621)Widgets')
    db.dwidgets.insert( f0= 'he6622', f1= '(6622)Info Box')
    db.dwidgets.insert( f0= 'sx6623', f1= '(6623)Messages')
    db.dwidgets.insert( f0= 'sx6624', f1= '(6624)Bookmarks')
    db.dwidgets.insert( f0= 'sx6625', f1= '(6625)Uploads')
    db.dwidgets.insert( f0= 'sx6626', f1= '(6626)Likes')
    db.dwidgets.insert( f0= 'sx6627', f1= '(6627)Bookmarks')
    db.dwidgets.insert( f0= 'sx6628', f1= '(6628)Likes')
    db.dwidgets.insert( f0= 'sx6629', f1= '(6629)Events')
    db.dwidgets.insert( f0= 'sx6630', f1= '(6630)Comments')
    db.dwidgets.insert( f0= 'sx6631', f1= '(6631)Bookmarks')
    db.dwidgets.insert( f0= 'sx6632', f1= '(6632)Likes')
    db.dwidgets.insert( f0= 'sx6633', f1= '(6633)Events')
    db.dwidgets.insert( f0= 'sx6634', f1= '(6634)Comments')
    db.dwidgets.insert( f0= 'he6635', f1= '(6635)Small Box')
    db.dwidgets.insert( f0= 'pa6636', f1= '(6636)New Orders')
    db.dwidgets.insert( f0= 'pa6637', f1= '(6637)Bounce Rate')
    db.dwidgets.insert( f0= 'pa6638', f1= '(6638)User Registrations')
    db.dwidgets.insert( f0= 'pa6639', f1= '(6639)Unique Visitors')
    db.dwidgets.insert( f0= 'pa6640', f1= '(6640)New Orders')
    db.dwidgets.insert( f0= 'pa6641', f1= '(6641)Bounce Rate')
    db.dwidgets.insert( f0= 'hd6642', f1= '(6642)Cards')
    db.dwidgets.insert( f0= 'he6643', f1= '(6643)Abilities')
    db.dwidgets.insert( f0= 'hc6644', f1= '(6644)Expandable')
    db.dwidgets.insert( f0= 'hc6645', f1= '(6645)Collapsable')
    db.dwidgets.insert( f0= 'hc6646', f1= '(6646)Removable')
    db.dwidgets.insert( f0= 'hc6647', f1= '(6647)Maximizable')
    db.dwidgets.insert( f0= 'hc6648', f1= '(6648)Card Refresh')
    db.dwidgets.insert( f0= 'hc6649', f1= '(6649)All together')
    db.dwidgets.insert( f0= 'hc6650', f1= '(6650)Loading state')
    db.dwidgets.insert( f0= 'hc6651', f1= '(6651)Loading state (dark)')
    db.dwidgets.insert( f0= 'he6652', f1= '(6652)Colors Variations')
    db.dwidgets.insert( f0= 'hc6653', f1= '(6653)Primary Outline')
    db.dwidgets.insert( f0= 'hc6654', f1= '(6654)Success Outline')
    db.dwidgets.insert( f0= 'hc6655', f1= '(6655)Warning Outline')
    db.dwidgets.insert( f0= 'hc6656', f1= '(6656)Danger Outline')
    db.dwidgets.insert( f0= 'hc6657', f1= '(6657)Primary Outline')
    db.dwidgets.insert( f0= 'hc6658', f1= '(6658)Success Outline')
    db.dwidgets.insert( f0= 'hc6659', f1= '(6659)Warning Outline')
    db.dwidgets.insert( f0= 'hc6660', f1= '(6660)Danger Outline')
    db.dwidgets.insert( f0= 'hc6661', f1= '(6661)Primary')
    db.dwidgets.insert( f0= 'hc6662', f1= '(6662)Success')
    db.dwidgets.insert( f0= 'hc6663', f1= '(6663)Warning')
    db.dwidgets.insert( f0= 'hc6664', f1= '(6664)Danger')
    db.dwidgets.insert( f0= 'hc6665', f1= '(6665)Primary Gradient')
    db.dwidgets.insert( f0= 'hc6666', f1= '(6666)Success Gradient')
    db.dwidgets.insert( f0= 'hc6667', f1= '(6667)Warning Gradient')
    db.dwidgets.insert( f0= 'hc6668', f1= '(6668)Danger Gradient')
    db.dwidgets.insert( f0= 'hd6669', f1= '(6669)Direct Chat')
    db.dwidgets.insert( f0= 'hc6670', f1= '(6670)Direct Chat')
    db.dwidgets.insert( f0= 'sx6671', f1= '(6671)3')
    db.dwidgets.insert( f0= 'sx6672', f1= '(6672)Alexander Pierce')
    db.dwidgets.insert( f0= 'sx6673', f1= '(6673)23 Jan 2:00 pm')
    db.dwidgets.insert( f0= 'sx6675', f1= '(6675)Sarah Bullock')
    db.dwidgets.insert( f0= 'sx6676', f1= '(6676)23 Jan 2:05 pm')
    db.dwidgets.insert( f0= 'sx6679', f1= '(6679)How have you been? I was...')
    db.dwidgets.insert( f0= 'pb6680', f1= '(6680)Type Message ...')
    db.dwidgets.insert( f0= 'bu6681', f1= '(6681)Send')
    db.dwidgets.insert( f0= 'hc6682', f1= '(6682)Direct Chat')
    db.dwidgets.insert( f0= 'sx6683', f1= '(6683)3')
    db.dwidgets.insert( f0= 'sx6684', f1= '(6684)Alexander Pierce')
    db.dwidgets.insert( f0= 'sx6685', f1= '(6685)23 Jan 2:00 pm')
    db.dwidgets.insert( f0= 'sx6687', f1= '(6687)Sarah Bullock')
    db.dwidgets.insert( f0= 'sx6688', f1= '(6688)23 Jan 2:05 pm')
    db.dwidgets.insert( f0= 'sx6691', f1= '(6691)How have you been? I was...')
    db.dwidgets.insert( f0= 'pb6692', f1= '(6692)Type Message ...')
    db.dwidgets.insert( f0= 'bu6693', f1= '(6693)Send')
    db.dwidgets.insert( f0= 'hc6694', f1= '(6694)Direct Chat')
    db.dwidgets.insert( f0= 'sx6695', f1= '(6695)3')
    db.dwidgets.insert( f0= 'sx6696', f1= '(6696)Alexander Pierce')
    db.dwidgets.insert( f0= 'sx6697', f1= '(6697)23 Jan 2:00 pm')
    db.dwidgets.insert( f0= 'sx6699', f1= '(6699)Sarah Bullock')
    db.dwidgets.insert( f0= 'sx6700', f1= '(6700)23 Jan 2:05 pm')
    db.dwidgets.insert( f0= 'sx6703', f1= '(6703)How have you been? I was...')
    db.dwidgets.insert( f0= 'pb6704', f1= '(6704)Type Message ...')
    db.dwidgets.insert( f0= 'bu6705', f1= '(6705)Send')
    db.dwidgets.insert( f0= 'hc6706', f1= '(6706)Direct Chat')
    db.dwidgets.insert( f0= 'sx6707', f1= '(6707)3')
    db.dwidgets.insert( f0= 'sx6708', f1= '(6708)Alexander Pierce')
    db.dwidgets.insert( f0= 'sx6709', f1= '(6709)23 Jan 2:00 pm')
    db.dwidgets.insert( f0= 'sx6711', f1= '(6711)Sarah Bullock')
    db.dwidgets.insert( f0= 'sx6712', f1= '(6712)23 Jan 2:05 pm')
    db.dwidgets.insert( f0= 'sx6715', f1= '(6715)How have you been? I was...')
    db.dwidgets.insert( f0= 'pb6716', f1= '(6716)Type Message ...')
    db.dwidgets.insert( f0= 'bu6717', f1= '(6717)Send')
    db.dwidgets.insert( f0= 'hc6718', f1= '(6718)Social Widgets')
    db.dwidgets.insert( f0= 'hc6720', f1= '(6720)Nadia Carmichael')
    db.dwidgets.insert( f0= 'he6721', f1= '(6721)Lead Developer')
    db.dwidgets.insert( f0= 'sx6722', f1= '(6722)5')
    db.dwidgets.insert( f0= 'hc6723', f1= '(6723)Alexander Pierce')
    db.dwidgets.insert( f0= 'he6724', f1= '(6724)Founder & CEO')
    db.dwidgets.insert( f0= 'sx6726', f1= '(6726)SALES')
    db.dwidgets.insert( f0= 'sx6727', f1= '(6727)FOLLOWERS')
    db.dwidgets.insert( f0= 'sx6728', f1= '(6728)PRODUCTS')
    db.dwidgets.insert( f0= 'hc6730', f1= '(6730)Elizabeth Pierce')
    db.dwidgets.insert( f0= 'he6731', f1= '(6731)Web Designer')
    db.dwidgets.insert( f0= 'sx6733', f1= '(6733)SALES')
    db.dwidgets.insert( f0= 'sx6734', f1= '(6734)FOLLOWERS')
    db.dwidgets.insert( f0= 'sx6735', f1= '(6735)PRODUCTS')
    db.dwidgets.insert( f0= 'aa6737', f1= '(6737)Jonathan Burke Jr.')
    db.dwidgets.insert( f0= 'sx6738', f1= '(6738)Shared publicly - 7:30 PM Today')
    db.dwidgets.insert( f0= 'pa6740', f1= '(6740)I took this photo this morning. What do you guys think?')
    db.dwidgets.insert( f0= 'sx6741', f1= '(6741)127 likes - 3 comments')
    db.dwidgets.insert( f0= 'sx6743', f1= '(6743)8:03 PM Today')
    db.dwidgets.insert( f0= 'sx6745', f1= '(6745)8:03 PM Today')
    db.dwidgets.insert( f0= 'pb6747', f1= '(6747)Press enter to post comment')
    db.dwidgets.insert( f0= 'aa6749', f1= '(6749)Jonathan Burke Jr.')
    db.dwidgets.insert( f0= 'sx6750', f1= '(6750)Shared publicly - 7:30 PM Today')
    db.dwidgets.insert( f0= 'aa6752', f1= '(6752)Lorem ipsum text generator')
    db.dwidgets.insert( f0= 'aa6753', f1= '(6753)more')
    db.dwidgets.insert( f0= 'sx6754', f1= '(6754)45 likes - 2 comments')
    db.dwidgets.insert( f0= 'sx6756', f1= '(6756)8:03 PM Today')
    db.dwidgets.insert( f0= 'sx6758', f1= '(6758)8:03 PM Today')
    db.dwidgets.insert( f0= 'pb6760', f1= '(6760)Press enter to post comment')
    db.dwidgets.insert( f0= 'bb6761', f1= '(6761)Version')
    db.dwidgets.insert( f0= 'aa6762', f1= '(6762)AdminLTE.io')
    db.commit()
#
