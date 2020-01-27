#
# table for controller: mailbox
#

from gluon.contrib.populate import populate

db.define_table('dmailbox', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dmailbox.id ).count():
    db.dmailbox.insert( f0= 'aa5590', f1= '(5590)Home')
    db.dmailbox.insert( f0= 'aa5591', f1= '(5591)Contact')
    db.dmailbox.insert( f0= 'pb5592', f1= '(5592)Search')
    db.dmailbox.insert( f0= 'sx5593', f1= '(5593)3')
    db.dmailbox.insert( f0= 'pc5595', f1= '(5595)Call me whenever you can...')
    db.dmailbox.insert( f0= 'pc5596', f1= '(5596)4 Hours Ago')
    db.dmailbox.insert( f0= 'pc5598', f1= '(5598)I got your message bro')
    db.dmailbox.insert( f0= 'pc5599', f1= '(5599)4 Hours Ago')
    db.dmailbox.insert( f0= 'pc5601', f1= '(5601)The subject goes here')
    db.dmailbox.insert( f0= 'pc5602', f1= '(5602)4 Hours Ago')
    db.dmailbox.insert( f0= 'aa5603', f1= '(5603)See All Messages')
    db.dmailbox.insert( f0= 'sx5604', f1= '(5604)15 Notifications')
    db.dmailbox.insert( f0= 'sx5605', f1= '(5605)3 mins')
    db.dmailbox.insert( f0= 'sx5606', f1= '(5606)12 hours')
    db.dmailbox.insert( f0= 'sx5607', f1= '(5607)2 days')
    db.dmailbox.insert( f0= 'aa5608', f1= '(5608)See All Notifications')
    db.dmailbox.insert( f0= 'sx5611', f1= '(5611)AdminLTE 3')
    db.dmailbox.insert( f0= 'aa5613', f1= '(5613)Alexander Pierce')
    db.dmailbox.insert( f0= 'pa5615', f1= '(5615)Dashboard v1')
    db.dmailbox.insert( f0= 'pa5617', f1= '(5617)Dashboard v2')
    db.dmailbox.insert( f0= 'pa5619', f1= '(5619)Dashboard v3')
    db.dmailbox.insert( f0= 'sx5621', f1= '(5621)New')
    db.dmailbox.insert( f0= 'sx5622', f1= '(5622)6')
    db.dmailbox.insert( f0= 'pa5624', f1= '(5624)Top Navigation')
    db.dmailbox.insert( f0= 'pa5626', f1= '(5626)Top Navigation + Sidebar')
    db.dmailbox.insert( f0= 'pa5628', f1= '(5628)Boxed')
    db.dmailbox.insert( f0= 'pa5630', f1= '(5630)Fixed Sidebar')
    db.dmailbox.insert( f0= 'pa5632', f1= '(5632)Fixed Navbar')
    db.dmailbox.insert( f0= 'pa5634', f1= '(5634)Fixed Footer')
    db.dmailbox.insert( f0= 'pa5636', f1= '(5636)Collapsed Sidebar')
    db.dmailbox.insert( f0= 'pa5638', f1= '(5638)ChartJS')
    db.dmailbox.insert( f0= 'pa5640', f1= '(5640)Flot')
    db.dmailbox.insert( f0= 'pa5642', f1= '(5642)Inline')
    db.dmailbox.insert( f0= 'pa5644', f1= '(5644)General')
    db.dmailbox.insert( f0= 'pa5646', f1= '(5646)Icons')
    db.dmailbox.insert( f0= 'pa5648', f1= '(5648)Buttons')
    db.dmailbox.insert( f0= 'pa5650', f1= '(5650)Sliders')
    db.dmailbox.insert( f0= 'pa5652', f1= '(5652)Modals & Alerts')
    db.dmailbox.insert( f0= 'pa5654', f1= '(5654)Navbar & Tabs')
    db.dmailbox.insert( f0= 'pa5656', f1= '(5656)Timeline')
    db.dmailbox.insert( f0= 'pa5658', f1= '(5658)Ribbons')
    db.dmailbox.insert( f0= 'pa5660', f1= '(5660)General Elements')
    db.dmailbox.insert( f0= 'pa5662', f1= '(5662)Advanced Elements')
    db.dmailbox.insert( f0= 'pa5664', f1= '(5664)Editors')
    db.dmailbox.insert( f0= 'pa5666', f1= '(5666)Validation')
    db.dmailbox.insert( f0= 'pa5668', f1= '(5668)Simple Tables')
    db.dmailbox.insert( f0= 'pa5670', f1= '(5670)DataTables')
    db.dmailbox.insert( f0= 'pa5672', f1= '(5672)jsGrid')
    db.dmailbox.insert( f0= 'lb5673', f1= '(5673)EXAMPLES')
    db.dmailbox.insert( f0= 'sx5675', f1= '(5675)2')
    db.dmailbox.insert( f0= 'pa5677', f1= '(5677)Inbox')
    db.dmailbox.insert( f0= 'pa5679', f1= '(5679)Compose')
    db.dmailbox.insert( f0= 'pa5681', f1= '(5681)Read')
    db.dmailbox.insert( f0= 'pa5683', f1= '(5683)Invoice')
    db.dmailbox.insert( f0= 'pa5685', f1= '(5685)Profile')
    db.dmailbox.insert( f0= 'pa5687', f1= '(5687)E-commerce')
    db.dmailbox.insert( f0= 'pa5689', f1= '(5689)Projects')
    db.dmailbox.insert( f0= 'pa5691', f1= '(5691)Project Add')
    db.dmailbox.insert( f0= 'pa5693', f1= '(5693)Project Edit')
    db.dmailbox.insert( f0= 'pa5695', f1= '(5695)Project Detail')
    db.dmailbox.insert( f0= 'pa5697', f1= '(5697)Contacts')
    db.dmailbox.insert( f0= 'pa5699', f1= '(5699)Login')
    db.dmailbox.insert( f0= 'pa5701', f1= '(5701)Register')
    db.dmailbox.insert( f0= 'pa5703', f1= '(5703)Forgot Password')
    db.dmailbox.insert( f0= 'pa5705', f1= '(5705)Recover Password')
    db.dmailbox.insert( f0= 'pa5707', f1= '(5707)Lockscreen')
    db.dmailbox.insert( f0= 'pa5709', f1= '(5709)Legacy User Menu')
    db.dmailbox.insert( f0= 'pa5711', f1= '(5711)Language Menu')
    db.dmailbox.insert( f0= 'pa5713', f1= '(5713)Error 404')
    db.dmailbox.insert( f0= 'pa5715', f1= '(5715)Error 500')
    db.dmailbox.insert( f0= 'pa5717', f1= '(5717)Pace')
    db.dmailbox.insert( f0= 'pa5719', f1= '(5719)Blank Page')
    db.dmailbox.insert( f0= 'pa5721', f1= '(5721)Starter Page')
    db.dmailbox.insert( f0= 'lb5722', f1= '(5722)MISCELLANEOUS')
    db.dmailbox.insert( f0= 'pa5723', f1= '(5723)Documentation')
    db.dmailbox.insert( f0= 'lb5724', f1= '(5724)MULTI LEVEL EXAMPLE')
    db.dmailbox.insert( f0= 'pa5725', f1= '(5725)Level 1')
    db.dmailbox.insert( f0= 'pa5726', f1= '(5726)Level 2')
    db.dmailbox.insert( f0= 'pa5727', f1= '(5727)Level 3')
    db.dmailbox.insert( f0= 'pa5728', f1= '(5728)Level 3')
    db.dmailbox.insert( f0= 'pa5729', f1= '(5729)Level 3')
    db.dmailbox.insert( f0= 'pa5730', f1= '(5730)Level 2')
    db.dmailbox.insert( f0= 'pa5731', f1= '(5731)Level 1')
    db.dmailbox.insert( f0= 'lb5732', f1= '(5732)LABELS')
    db.dmailbox.insert( f0= 'pc5733', f1= '(5733)Important')
    db.dmailbox.insert( f0= 'pa5734', f1= '(5734)Warning')
    db.dmailbox.insert( f0= 'pa5735', f1= '(5735)Informational')
    db.dmailbox.insert( f0= 'hh5736', f1= '(5736)Inbox')
    db.dmailbox.insert( f0= 'aa5737', f1= '(5737)Home')
    db.dmailbox.insert( f0= 'lb5738', f1= '(5738)Inbox')
    db.dmailbox.insert( f0= 'aa5740', f1= '(5740)Compose')
    db.dmailbox.insert( f0= 'hc5741', f1= '(5741)Folders')
    db.dmailbox.insert( f0= 'hc5742', f1= '(5742)Labels')
    db.dmailbox.insert( f0= 'hc5743', f1= '(5743)Inbox')
    db.dmailbox.insert( f0= 'pb5744', f1= '(5744)Search Mail')
    db.dmailbox.insert( f0= 'aa5746', f1= '(5746)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5747', f1= '(5747)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'aa5749', f1= '(5749)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5750', f1= '(5750)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'aa5752', f1= '(5752)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5753', f1= '(5753)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'aa5755', f1= '(5755)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5756', f1= '(5756)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'aa5758', f1= '(5758)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5759', f1= '(5759)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'aa5761', f1= '(5761)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5762', f1= '(5762)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'aa5764', f1= '(5764)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5765', f1= '(5765)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'aa5767', f1= '(5767)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5768', f1= '(5768)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'aa5770', f1= '(5770)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5771', f1= '(5771)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'aa5773', f1= '(5773)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5774', f1= '(5774)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'aa5776', f1= '(5776)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5777', f1= '(5777)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'aa5779', f1= '(5779)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5780', f1= '(5780)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'aa5782', f1= '(5782)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5783', f1= '(5783)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'aa5785', f1= '(5785)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5786', f1= '(5786)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'aa5788', f1= '(5788)Alexander Pierce')
    db.dmailbox.insert( f0= 'bb5789', f1= '(5789)AdminLTE 3.0 Issue')
    db.dmailbox.insert( f0= 'bb5790', f1= '(5790)Version')
    db.dmailbox.insert( f0= 'aa5791', f1= '(5791)AdminLTE.io')
    db.commit()
#
