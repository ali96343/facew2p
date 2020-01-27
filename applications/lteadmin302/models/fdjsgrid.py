#
# table for controller: jsgrid
#

from gluon.contrib.populate import populate

db.define_table('djsgrid', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.djsgrid.id ).count():
    db.djsgrid.insert( f0= 'aa8190', f1= '(8190)Home')
    db.djsgrid.insert( f0= 'aa8191', f1= '(8191)Contact')
    db.djsgrid.insert( f0= 'pb8192', f1= '(8192)Search')
    db.djsgrid.insert( f0= 'sx8193', f1= '(8193)3')
    db.djsgrid.insert( f0= 'pc8195', f1= '(8195)Call me whenever you can...')
    db.djsgrid.insert( f0= 'pc8196', f1= '(8196)4 Hours Ago')
    db.djsgrid.insert( f0= 'pc8198', f1= '(8198)I got your message bro')
    db.djsgrid.insert( f0= 'pc8199', f1= '(8199)4 Hours Ago')
    db.djsgrid.insert( f0= 'pc8201', f1= '(8201)The subject goes here')
    db.djsgrid.insert( f0= 'pc8202', f1= '(8202)4 Hours Ago')
    db.djsgrid.insert( f0= 'aa8203', f1= '(8203)See All Messages')
    db.djsgrid.insert( f0= 'sx8204', f1= '(8204)15 Notifications')
    db.djsgrid.insert( f0= 'sx8205', f1= '(8205)3 mins')
    db.djsgrid.insert( f0= 'sx8206', f1= '(8206)12 hours')
    db.djsgrid.insert( f0= 'sx8207', f1= '(8207)2 days')
    db.djsgrid.insert( f0= 'aa8208', f1= '(8208)See All Notifications')
    db.djsgrid.insert( f0= 'sx8211', f1= '(8211)AdminLTE 3')
    db.djsgrid.insert( f0= 'aa8213', f1= '(8213)Alexander Pierce')
    db.djsgrid.insert( f0= 'pa8215', f1= '(8215)Dashboard v1')
    db.djsgrid.insert( f0= 'pa8217', f1= '(8217)Dashboard v2')
    db.djsgrid.insert( f0= 'pa8219', f1= '(8219)Dashboard v3')
    db.djsgrid.insert( f0= 'sx8221', f1= '(8221)New')
    db.djsgrid.insert( f0= 'sx8222', f1= '(8222)6')
    db.djsgrid.insert( f0= 'pa8224', f1= '(8224)Top Navigation')
    db.djsgrid.insert( f0= 'pa8226', f1= '(8226)Top Navigation + Sidebar')
    db.djsgrid.insert( f0= 'pa8228', f1= '(8228)Boxed')
    db.djsgrid.insert( f0= 'pa8230', f1= '(8230)Fixed Sidebar')
    db.djsgrid.insert( f0= 'pa8232', f1= '(8232)Fixed Navbar')
    db.djsgrid.insert( f0= 'pa8234', f1= '(8234)Fixed Footer')
    db.djsgrid.insert( f0= 'pa8236', f1= '(8236)Collapsed Sidebar')
    db.djsgrid.insert( f0= 'pa8238', f1= '(8238)ChartJS')
    db.djsgrid.insert( f0= 'pa8240', f1= '(8240)Flot')
    db.djsgrid.insert( f0= 'pa8242', f1= '(8242)Inline')
    db.djsgrid.insert( f0= 'pa8244', f1= '(8244)General')
    db.djsgrid.insert( f0= 'pa8246', f1= '(8246)Icons')
    db.djsgrid.insert( f0= 'pa8248', f1= '(8248)Buttons')
    db.djsgrid.insert( f0= 'pa8250', f1= '(8250)Sliders')
    db.djsgrid.insert( f0= 'pa8252', f1= '(8252)Modals & Alerts')
    db.djsgrid.insert( f0= 'pa8254', f1= '(8254)Navbar & Tabs')
    db.djsgrid.insert( f0= 'pa8256', f1= '(8256)Timeline')
    db.djsgrid.insert( f0= 'pa8258', f1= '(8258)Ribbons')
    db.djsgrid.insert( f0= 'pa8260', f1= '(8260)General Elements')
    db.djsgrid.insert( f0= 'pa8262', f1= '(8262)Advanced Elements')
    db.djsgrid.insert( f0= 'pa8264', f1= '(8264)Editors')
    db.djsgrid.insert( f0= 'pa8266', f1= '(8266)Validation')
    db.djsgrid.insert( f0= 'pa8268', f1= '(8268)Simple Tables')
    db.djsgrid.insert( f0= 'pa8270', f1= '(8270)DataTables')
    db.djsgrid.insert( f0= 'pa8272', f1= '(8272)jsGrid')
    db.djsgrid.insert( f0= 'lb8273', f1= '(8273)EXAMPLES')
    db.djsgrid.insert( f0= 'sx8275', f1= '(8275)2')
    db.djsgrid.insert( f0= 'pa8278', f1= '(8278)Inbox')
    db.djsgrid.insert( f0= 'pa8280', f1= '(8280)Compose')
    db.djsgrid.insert( f0= 'pa8282', f1= '(8282)Read')
    db.djsgrid.insert( f0= 'pa8284', f1= '(8284)Invoice')
    db.djsgrid.insert( f0= 'pa8286', f1= '(8286)Profile')
    db.djsgrid.insert( f0= 'pa8288', f1= '(8288)E-commerce')
    db.djsgrid.insert( f0= 'pa8290', f1= '(8290)Projects')
    db.djsgrid.insert( f0= 'pa8292', f1= '(8292)Project Add')
    db.djsgrid.insert( f0= 'pa8294', f1= '(8294)Project Edit')
    db.djsgrid.insert( f0= 'pa8296', f1= '(8296)Project Detail')
    db.djsgrid.insert( f0= 'pa8298', f1= '(8298)Contacts')
    db.djsgrid.insert( f0= 'pa8300', f1= '(8300)Login')
    db.djsgrid.insert( f0= 'pa8302', f1= '(8302)Register')
    db.djsgrid.insert( f0= 'pa8304', f1= '(8304)Forgot Password')
    db.djsgrid.insert( f0= 'pa8306', f1= '(8306)Recover Password')
    db.djsgrid.insert( f0= 'pa8308', f1= '(8308)Lockscreen')
    db.djsgrid.insert( f0= 'pa8310', f1= '(8310)Legacy User Menu')
    db.djsgrid.insert( f0= 'pa8312', f1= '(8312)Language Menu')
    db.djsgrid.insert( f0= 'pa8314', f1= '(8314)Error 404')
    db.djsgrid.insert( f0= 'pa8316', f1= '(8316)Error 500')
    db.djsgrid.insert( f0= 'pa8318', f1= '(8318)Pace')
    db.djsgrid.insert( f0= 'pa8320', f1= '(8320)Blank Page')
    db.djsgrid.insert( f0= 'pa8322', f1= '(8322)Starter Page')
    db.djsgrid.insert( f0= 'lb8323', f1= '(8323)MISCELLANEOUS')
    db.djsgrid.insert( f0= 'pa8324', f1= '(8324)Documentation')
    db.djsgrid.insert( f0= 'lb8325', f1= '(8325)MULTI LEVEL EXAMPLE')
    db.djsgrid.insert( f0= 'pa8326', f1= '(8326)Level 1')
    db.djsgrid.insert( f0= 'pa8327', f1= '(8327)Level 2')
    db.djsgrid.insert( f0= 'pa8328', f1= '(8328)Level 3')
    db.djsgrid.insert( f0= 'pa8329', f1= '(8329)Level 3')
    db.djsgrid.insert( f0= 'pa8330', f1= '(8330)Level 3')
    db.djsgrid.insert( f0= 'pa8331', f1= '(8331)Level 2')
    db.djsgrid.insert( f0= 'pa8332', f1= '(8332)Level 1')
    db.djsgrid.insert( f0= 'lb8333', f1= '(8333)LABELS')
    db.djsgrid.insert( f0= 'pc8334', f1= '(8334)Important')
    db.djsgrid.insert( f0= 'pa8335', f1= '(8335)Warning')
    db.djsgrid.insert( f0= 'pa8336', f1= '(8336)Informational')
    db.djsgrid.insert( f0= 'hh8337', f1= '(8337)jsGrid')
    db.djsgrid.insert( f0= 'aa8338', f1= '(8338)Home')
    db.djsgrid.insert( f0= 'lb8339', f1= '(8339)jsGrid')
    db.djsgrid.insert( f0= 'hc8340', f1= '(8340)jsGrid')
    db.djsgrid.insert( f0= 'bb8341', f1= '(8341)Version')
    db.djsgrid.insert( f0= 'aa8342', f1= '(8342)AdminLTE.io')
    db.commit()
#
