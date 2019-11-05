#
# table for controller: flot
#

from gluon.contrib.populate import populate

db.define_table('dflot', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dflot.id ).count():
    db.dflot.insert( f0= 'aa8075', f1= '(8075)Home')
    db.dflot.insert( f0= 'aa8076', f1= '(8076)Contact')
    db.dflot.insert( f0= 'pb8077', f1= '(8077)Search')
    db.dflot.insert( f0= 'sx8078', f1= '(8078)3')
    db.dflot.insert( f0= 'pc8080', f1= '(8080)Call me whenever you can...')
    db.dflot.insert( f0= 'pc8081', f1= '(8081)4 Hours Ago')
    db.dflot.insert( f0= 'pc8083', f1= '(8083)I got your message bro')
    db.dflot.insert( f0= 'pc8084', f1= '(8084)4 Hours Ago')
    db.dflot.insert( f0= 'pc8086', f1= '(8086)The subject goes here')
    db.dflot.insert( f0= 'pc8087', f1= '(8087)4 Hours Ago')
    db.dflot.insert( f0= 'aa8088', f1= '(8088)See All Messages')
    db.dflot.insert( f0= 'sx8089', f1= '(8089)15 Notifications')
    db.dflot.insert( f0= 'sx8090', f1= '(8090)3 mins')
    db.dflot.insert( f0= 'sx8091', f1= '(8091)12 hours')
    db.dflot.insert( f0= 'sx8092', f1= '(8092)2 days')
    db.dflot.insert( f0= 'aa8093', f1= '(8093)See All Notifications')
    db.dflot.insert( f0= 'sx8096', f1= '(8096)AdminLTE 3')
    db.dflot.insert( f0= 'aa8098', f1= '(8098)Alexander Pierce')
    db.dflot.insert( f0= 'pa8100', f1= '(8100)Dashboard v1')
    db.dflot.insert( f0= 'pa8102', f1= '(8102)Dashboard v2')
    db.dflot.insert( f0= 'pa8104', f1= '(8104)Dashboard v3')
    db.dflot.insert( f0= 'sx8106', f1= '(8106)New')
    db.dflot.insert( f0= 'sx8107', f1= '(8107)6')
    db.dflot.insert( f0= 'pa8109', f1= '(8109)Top Navigation')
    db.dflot.insert( f0= 'pa8111', f1= '(8111)Boxed')
    db.dflot.insert( f0= 'pa8113', f1= '(8113)Fixed Sidebar')
    db.dflot.insert( f0= 'pa8115', f1= '(8115)Fixed Navbar')
    db.dflot.insert( f0= 'pa8117', f1= '(8117)Fixed Footer')
    db.dflot.insert( f0= 'pa8119', f1= '(8119)Collapsed Sidebar')
    db.dflot.insert( f0= 'pa8121', f1= '(8121)ChartJS')
    db.dflot.insert( f0= 'pa8123', f1= '(8123)Flot')
    db.dflot.insert( f0= 'pa8125', f1= '(8125)Inline')
    db.dflot.insert( f0= 'pa8127', f1= '(8127)General')
    db.dflot.insert( f0= 'pa8129', f1= '(8129)Icons')
    db.dflot.insert( f0= 'pa8131', f1= '(8131)Buttons')
    db.dflot.insert( f0= 'pa8133', f1= '(8133)Sliders')
    db.dflot.insert( f0= 'pa8135', f1= '(8135)Modals & Alerts')
    db.dflot.insert( f0= 'pa8137', f1= '(8137)Navbar & Tabs')
    db.dflot.insert( f0= 'pa8139', f1= '(8139)Timeline')
    db.dflot.insert( f0= 'pa8141', f1= '(8141)Ribbons')
    db.dflot.insert( f0= 'pa8143', f1= '(8143)General Elements')
    db.dflot.insert( f0= 'pa8145', f1= '(8145)Advanced Elements')
    db.dflot.insert( f0= 'pa8147', f1= '(8147)Editors')
    db.dflot.insert( f0= 'pa8149', f1= '(8149)Simple Tables')
    db.dflot.insert( f0= 'pa8151', f1= '(8151)DataTables')
    db.dflot.insert( f0= 'pa8153', f1= '(8153)jsGrid')
    db.dflot.insert( f0= 'lb8154', f1= '(8154)EXAMPLES')
    db.dflot.insert( f0= 'sx8156', f1= '(8156)2')
    db.dflot.insert( f0= 'pa8159', f1= '(8159)Inbox')
    db.dflot.insert( f0= 'pa8161', f1= '(8161)Compose')
    db.dflot.insert( f0= 'pa8163', f1= '(8163)Read')
    db.dflot.insert( f0= 'pa8165', f1= '(8165)Invoice')
    db.dflot.insert( f0= 'pa8167', f1= '(8167)Profile')
    db.dflot.insert( f0= 'pa8169', f1= '(8169)E-commerce')
    db.dflot.insert( f0= 'pa8171', f1= '(8171)Projects')
    db.dflot.insert( f0= 'pa8173', f1= '(8173)Project Add')
    db.dflot.insert( f0= 'pa8175', f1= '(8175)Project Edit')
    db.dflot.insert( f0= 'pa8177', f1= '(8177)Project Detail')
    db.dflot.insert( f0= 'pa8179', f1= '(8179)Contacts')
    db.dflot.insert( f0= 'pa8181', f1= '(8181)Login')
    db.dflot.insert( f0= 'pa8183', f1= '(8183)Register')
    db.dflot.insert( f0= 'pa8185', f1= '(8185)Forgot Password')
    db.dflot.insert( f0= 'pa8187', f1= '(8187)Recover Password')
    db.dflot.insert( f0= 'pa8189', f1= '(8189)Lockscreen')
    db.dflot.insert( f0= 'pa8191', f1= '(8191)Legacy User Menu')
    db.dflot.insert( f0= 'pa8193', f1= '(8193)Language Menu')
    db.dflot.insert( f0= 'pa8195', f1= '(8195)Error 404')
    db.dflot.insert( f0= 'pa8197', f1= '(8197)Error 500')
    db.dflot.insert( f0= 'pa8199', f1= '(8199)Pace')
    db.dflot.insert( f0= 'pa8201', f1= '(8201)Blank Page')
    db.dflot.insert( f0= 'pa8203', f1= '(8203)Starter Page')
    db.dflot.insert( f0= 'lb8204', f1= '(8204)MISCELLANEOUS')
    db.dflot.insert( f0= 'pa8205', f1= '(8205)Documentation')
    db.dflot.insert( f0= 'lb8206', f1= '(8206)MULTI LEVEL EXAMPLE')
    db.dflot.insert( f0= 'pa8207', f1= '(8207)Level 1')
    db.dflot.insert( f0= 'pa8208', f1= '(8208)Level 2')
    db.dflot.insert( f0= 'pa8209', f1= '(8209)Level 3')
    db.dflot.insert( f0= 'pa8210', f1= '(8210)Level 3')
    db.dflot.insert( f0= 'pa8211', f1= '(8211)Level 3')
    db.dflot.insert( f0= 'pa8212', f1= '(8212)Level 2')
    db.dflot.insert( f0= 'pa8213', f1= '(8213)Level 1')
    db.dflot.insert( f0= 'lb8214', f1= '(8214)LABELS')
    db.dflot.insert( f0= 'pc8215', f1= '(8215)Important')
    db.dflot.insert( f0= 'pa8216', f1= '(8216)Warning')
    db.dflot.insert( f0= 'pa8217', f1= '(8217)Informational')
    db.dflot.insert( f0= 'hh8218', f1= '(8218)Flot Charts')
    db.dflot.insert( f0= 'aa8219', f1= '(8219)Home')
    db.dflot.insert( f0= 'lb8220', f1= '(8220)Flot')
    db.dflot.insert( f0= 'bu8221', f1= '(8221)On')
    db.dflot.insert( f0= 'bu8222', f1= '(8222)Off')
    db.dflot.insert( f0= 'bb8223', f1= '(8223)Version')
    db.dflot.insert( f0= 'aa8224', f1= '(8224)AdminLTE.io')
    db.commit()
#
