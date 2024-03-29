#
# table for controller: gallery
#

from gluon.contrib.populate import populate

db.define_table('dgallery', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dgallery.id ).count():
    db.dgallery.insert( f0= 'aa6609', f1= '(6609)Home')
    db.dgallery.insert( f0= 'aa6610', f1= '(6610)Contact')
    db.dgallery.insert( f0= 'pb6611', f1= '(6611)Search')
    db.dgallery.insert( f0= 'sx6612', f1= '(6612)3')
    db.dgallery.insert( f0= 'pc6614', f1= '(6614)Call me whenever you can...')
    db.dgallery.insert( f0= 'pc6615', f1= '(6615)4 Hours Ago')
    db.dgallery.insert( f0= 'pc6617', f1= '(6617)I got your message bro')
    db.dgallery.insert( f0= 'pc6618', f1= '(6618)4 Hours Ago')
    db.dgallery.insert( f0= 'pc6620', f1= '(6620)The subject goes here')
    db.dgallery.insert( f0= 'pc6621', f1= '(6621)4 Hours Ago')
    db.dgallery.insert( f0= 'aa6622', f1= '(6622)See All Messages')
    db.dgallery.insert( f0= 'sx6623', f1= '(6623)15 Notifications')
    db.dgallery.insert( f0= 'sx6624', f1= '(6624)3 mins')
    db.dgallery.insert( f0= 'sx6625', f1= '(6625)12 hours')
    db.dgallery.insert( f0= 'sx6626', f1= '(6626)2 days')
    db.dgallery.insert( f0= 'aa6627', f1= '(6627)See All Notifications')
    db.dgallery.insert( f0= 'sx6630', f1= '(6630)AdminLTE 3')
    db.dgallery.insert( f0= 'aa6632', f1= '(6632)Alexander Pierce')
    db.dgallery.insert( f0= 'pa6634', f1= '(6634)Dashboard v1')
    db.dgallery.insert( f0= 'pa6636', f1= '(6636)Dashboard v2')
    db.dgallery.insert( f0= 'pa6638', f1= '(6638)Dashboard v3')
    db.dgallery.insert( f0= 'sx6640', f1= '(6640)New')
    db.dgallery.insert( f0= 'sx6641', f1= '(6641)6')
    db.dgallery.insert( f0= 'pa6643', f1= '(6643)Top Navigation')
    db.dgallery.insert( f0= 'pa6645', f1= '(6645)Top Navigation + Sidebar')
    db.dgallery.insert( f0= 'pa6647', f1= '(6647)Boxed')
    db.dgallery.insert( f0= 'pa6649', f1= '(6649)Fixed Sidebar')
    db.dgallery.insert( f0= 'pa6651', f1= '(6651)Fixed Navbar')
    db.dgallery.insert( f0= 'pa6653', f1= '(6653)Fixed Footer')
    db.dgallery.insert( f0= 'pa6655', f1= '(6655)Collapsed Sidebar')
    db.dgallery.insert( f0= 'pa6657', f1= '(6657)ChartJS')
    db.dgallery.insert( f0= 'pa6659', f1= '(6659)Flot')
    db.dgallery.insert( f0= 'pa6661', f1= '(6661)Inline')
    db.dgallery.insert( f0= 'pa6663', f1= '(6663)General')
    db.dgallery.insert( f0= 'pa6665', f1= '(6665)Icons')
    db.dgallery.insert( f0= 'pa6667', f1= '(6667)Buttons')
    db.dgallery.insert( f0= 'pa6669', f1= '(6669)Sliders')
    db.dgallery.insert( f0= 'pa6671', f1= '(6671)Modals & Alerts')
    db.dgallery.insert( f0= 'pa6673', f1= '(6673)Navbar & Tabs')
    db.dgallery.insert( f0= 'pa6675', f1= '(6675)Timeline')
    db.dgallery.insert( f0= 'pa6677', f1= '(6677)Ribbons')
    db.dgallery.insert( f0= 'pa6679', f1= '(6679)General Elements')
    db.dgallery.insert( f0= 'pa6681', f1= '(6681)Advanced Elements')
    db.dgallery.insert( f0= 'pa6683', f1= '(6683)Editors')
    db.dgallery.insert( f0= 'pa6685', f1= '(6685)Validation')
    db.dgallery.insert( f0= 'pa6687', f1= '(6687)Simple Tables')
    db.dgallery.insert( f0= 'pa6689', f1= '(6689)DataTables')
    db.dgallery.insert( f0= 'pa6691', f1= '(6691)jsGrid')
    db.dgallery.insert( f0= 'lb6692', f1= '(6692)EXAMPLES')
    db.dgallery.insert( f0= 'sx6694', f1= '(6694)2')
    db.dgallery.insert( f0= 'pa6697', f1= '(6697)Inbox')
    db.dgallery.insert( f0= 'pa6699', f1= '(6699)Compose')
    db.dgallery.insert( f0= 'pa6701', f1= '(6701)Read')
    db.dgallery.insert( f0= 'pa6703', f1= '(6703)Invoice')
    db.dgallery.insert( f0= 'pa6705', f1= '(6705)Profile')
    db.dgallery.insert( f0= 'pa6707', f1= '(6707)E-commerce')
    db.dgallery.insert( f0= 'pa6709', f1= '(6709)Projects')
    db.dgallery.insert( f0= 'pa6711', f1= '(6711)Project Add')
    db.dgallery.insert( f0= 'pa6713', f1= '(6713)Project Edit')
    db.dgallery.insert( f0= 'pa6715', f1= '(6715)Project Detail')
    db.dgallery.insert( f0= 'pa6717', f1= '(6717)Contacts')
    db.dgallery.insert( f0= 'pa6719', f1= '(6719)Login')
    db.dgallery.insert( f0= 'pa6721', f1= '(6721)Register')
    db.dgallery.insert( f0= 'pa6723', f1= '(6723)Forgot Password')
    db.dgallery.insert( f0= 'pa6725', f1= '(6725)Recover Password')
    db.dgallery.insert( f0= 'pa6727', f1= '(6727)Lockscreen')
    db.dgallery.insert( f0= 'pa6729', f1= '(6729)Legacy User Menu')
    db.dgallery.insert( f0= 'pa6731', f1= '(6731)Language Menu')
    db.dgallery.insert( f0= 'pa6733', f1= '(6733)Error 404')
    db.dgallery.insert( f0= 'pa6735', f1= '(6735)Error 500')
    db.dgallery.insert( f0= 'pa6737', f1= '(6737)Pace')
    db.dgallery.insert( f0= 'pa6739', f1= '(6739)Blank Page')
    db.dgallery.insert( f0= 'pa6741', f1= '(6741)Starter Page')
    db.dgallery.insert( f0= 'lb6742', f1= '(6742)MISCELLANEOUS')
    db.dgallery.insert( f0= 'pa6743', f1= '(6743)Documentation')
    db.dgallery.insert( f0= 'lb6744', f1= '(6744)MULTI LEVEL EXAMPLE')
    db.dgallery.insert( f0= 'pa6745', f1= '(6745)Level 1')
    db.dgallery.insert( f0= 'pa6746', f1= '(6746)Level 2')
    db.dgallery.insert( f0= 'pa6747', f1= '(6747)Level 3')
    db.dgallery.insert( f0= 'pa6748', f1= '(6748)Level 3')
    db.dgallery.insert( f0= 'pa6749', f1= '(6749)Level 3')
    db.dgallery.insert( f0= 'pa6750', f1= '(6750)Level 2')
    db.dgallery.insert( f0= 'pa6751', f1= '(6751)Level 1')
    db.dgallery.insert( f0= 'lb6752', f1= '(6752)LABELS')
    db.dgallery.insert( f0= 'pc6753', f1= '(6753)Important')
    db.dgallery.insert( f0= 'pa6754', f1= '(6754)Warning')
    db.dgallery.insert( f0= 'pa6755', f1= '(6755)Informational')
    db.dgallery.insert( f0= 'hh6756', f1= '(6756)Gallery')
    db.dgallery.insert( f0= 'aa6757', f1= '(6757)Home')
    db.dgallery.insert( f0= 'lb6758', f1= '(6758)Gallery')
    db.dgallery.insert( f0= 'aa6759', f1= '(6759)All items')
    db.dgallery.insert( f0= 'aa6760', f1= '(6760)Category 1 (WHITE)')
    db.dgallery.insert( f0= 'aa6761', f1= '(6761)Category 2 (BLACK)')
    db.dgallery.insert( f0= 'aa6762', f1= '(6762)Category 3 (COLORED)')
    db.dgallery.insert( f0= 'aa6763', f1= '(6763)Category 4 (COLORED, BLACK)')
    db.dgallery.insert( f0= 'aa6764', f1= '(6764)Shuffle items')
    db.dgallery.insert( f0= 'aa6765', f1= '(6765)Ascending')
    db.dgallery.insert( f0= 'aa6766', f1= '(6766)Descending')
    db.dgallery.insert( f0= 'bb6767', f1= '(6767)Version')
    db.dgallery.insert( f0= 'aa6768', f1= '(6768)AdminLTE.io')
    db.commit()
#
