#
# table for controller: form_examples
#

from gluon.contrib.populate import populate

db.define_table('dform0examples', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dform0examples.id ).count():
    db.dform0examples.insert( f0= 'sp8572', f1= '(8572)outdated')
    db.dform0examples.insert( f0= 'pc8573', f1= '(8573)to improve your experience.')
    db.dform0examples.insert( f0= 'aa8574', f1= '(8574)upgrade your browser')
    db.dform0examples.insert( f0= 'hh8576', f1= '(8576)Messages')
    db.dform0examples.insert( f0= 'hh8578', f1= '(8578)David Belle')
    db.dform0examples.insert( f0= 'pa8579', f1= '(8579)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dform0examples.insert( f0= 'hh8581', f1= '(8581)Jonathan Morris')
    db.dform0examples.insert( f0= 'pa8582', f1= '(8582)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dform0examples.insert( f0= 'hh8584', f1= '(8584)Fredric Mitchell')
    db.dform0examples.insert( f0= 'pa8585', f1= '(8585)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dform0examples.insert( f0= 'hh8587', f1= '(8587)David Belle')
    db.dform0examples.insert( f0= 'pa8588', f1= '(8588)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dform0examples.insert( f0= 'hh8590', f1= '(8590)Glenn Jecobs')
    db.dform0examples.insert( f0= 'pa8591', f1= '(8591)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dform0examples.insert( f0= 'aa8592', f1= '(8592)View All')
    db.dform0examples.insert( f0= 'hh8593', f1= '(8593)Notification')
    db.dform0examples.insert( f0= 'hh8595', f1= '(8595)David Belle')
    db.dform0examples.insert( f0= 'pa8596', f1= '(8596)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dform0examples.insert( f0= 'hh8598', f1= '(8598)Jonathan Morris')
    db.dform0examples.insert( f0= 'pa8599', f1= '(8599)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dform0examples.insert( f0= 'hh8601', f1= '(8601)Fredric Mitchell')
    db.dform0examples.insert( f0= 'pa8602', f1= '(8602)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dform0examples.insert( f0= 'hh8604', f1= '(8604)David Belle')
    db.dform0examples.insert( f0= 'pa8605', f1= '(8605)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dform0examples.insert( f0= 'hh8607', f1= '(8607)Glenn Jecobs')
    db.dform0examples.insert( f0= 'pa8608', f1= '(8608)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dform0examples.insert( f0= 'aa8609', f1= '(8609)View All')
    db.dform0examples.insert( f0= 'hh8610', f1= '(8610)Tasks')
    db.dform0examples.insert( f0= 'pa8611', f1= '(8611)HTML5 Validation Report')
    db.dform0examples.insert( f0= 'sp8612', f1= '(8612)95%')
    db.dform0examples.insert( f0= 'pa8613', f1= '(8613)Google Chrome Extension')
    db.dform0examples.insert( f0= 'sp8614', f1= '(8614)85%')
    db.dform0examples.insert( f0= 'pa8615', f1= '(8615)Social Internet Projects')
    db.dform0examples.insert( f0= 'sp8616', f1= '(8616)75%')
    db.dform0examples.insert( f0= 'pa8617', f1= '(8617)Bootstrap Admin')
    db.dform0examples.insert( f0= 'sp8618', f1= '(8618)65%')
    db.dform0examples.insert( f0= 'pa8619', f1= '(8619)Youtube App')
    db.dform0examples.insert( f0= 'sp8620', f1= '(8620)55%')
    db.dform0examples.insert( f0= 'aa8621', f1= '(8621)View All')
    db.dform0examples.insert( f0= 'hh8622', f1= '(8622)Chat')
    db.dform0examples.insert( f0= 'pb8623', f1= '(8623)Search People')
    db.dform0examples.insert( f0= 'hh8625', f1= '(8625)David Belle')
    db.dform0examples.insert( f0= 'pa8626', f1= '(8626)Available')
    db.dform0examples.insert( f0= 'hh8628', f1= '(8628)Jonathan Morris')
    db.dform0examples.insert( f0= 'pa8629', f1= '(8629)Last seen 3 hours ago')
    db.dform0examples.insert( f0= 'hh8631', f1= '(8631)Fredric Mitchell')
    db.dform0examples.insert( f0= 'pa8632', f1= '(8632)Last seen 2 minutes ago')
    db.dform0examples.insert( f0= 'hh8634', f1= '(8634)David Belle')
    db.dform0examples.insert( f0= 'pa8635', f1= '(8635)Available')
    db.dform0examples.insert( f0= 'hh8637', f1= '(8637)Glenn Jecobs')
    db.dform0examples.insert( f0= 'pa8638', f1= '(8638)Available')
    db.dform0examples.insert( f0= 'aa8639', f1= '(8639)View All')
    db.dform0examples.insert( f0= 'aa8640', f1= '(8640)Home')
    db.dform0examples.insert( f0= 'aa8642', f1= '(8642)Dashboard One')
    db.dform0examples.insert( f0= 'aa8644', f1= '(8644)Dashboard Two')
    db.dform0examples.insert( f0= 'aa8646', f1= '(8646)Dashboard Three')
    db.dform0examples.insert( f0= 'aa8648', f1= '(8648)Dashboard Four')
    db.dform0examples.insert( f0= 'aa8650', f1= '(8650)Analytics')
    db.dform0examples.insert( f0= 'aa8652', f1= '(8652)Widgets')
    db.dform0examples.insert( f0= 'aa8653', f1= '(8653)Email')
    db.dform0examples.insert( f0= 'aa8655', f1= '(8655)Inbox')
    db.dform0examples.insert( f0= 'aa8657', f1= '(8657)View Email')
    db.dform0examples.insert( f0= 'aa8659', f1= '(8659)Compose Email')
    db.dform0examples.insert( f0= 'aa8660', f1= '(8660)Interface')
    db.dform0examples.insert( f0= 'aa8662', f1= '(8662)Animations')
    db.dform0examples.insert( f0= 'aa8664', f1= '(8664)Google Map')
    db.dform0examples.insert( f0= 'aa8666', f1= '(8666)Data Maps')
    db.dform0examples.insert( f0= 'aa8668', f1= '(8668)Code Editor')
    db.dform0examples.insert( f0= 'aa8670', f1= '(8670)Images Cropper')
    db.dform0examples.insert( f0= 'aa8672', f1= '(8672)Wizard')
    db.dform0examples.insert( f0= 'aa8673', f1= '(8673)Charts')
    db.dform0examples.insert( f0= 'aa8675', f1= '(8675)Flot Charts')
    db.dform0examples.insert( f0= 'aa8677', f1= '(8677)Bar Charts')
    db.dform0examples.insert( f0= 'aa8679', f1= '(8679)Line Charts')
    db.dform0examples.insert( f0= 'aa8681', f1= '(8681)Area Charts')
    db.dform0examples.insert( f0= 'aa8682', f1= '(8682)Tables')
    db.dform0examples.insert( f0= 'aa8684', f1= '(8684)Normal Table')
    db.dform0examples.insert( f0= 'aa8686', f1= '(8686)Data Table')
    db.dform0examples.insert( f0= 'aa8687', f1= '(8687)Forms')
    db.dform0examples.insert( f0= 'aa8689', f1= '(8689)Form Elements')
    db.dform0examples.insert( f0= 'aa8691', f1= '(8691)Form Components')
    db.dform0examples.insert( f0= 'aa8693', f1= '(8693)Form Examples')
    db.dform0examples.insert( f0= 'aa8694', f1= '(8694)App views')
    db.dform0examples.insert( f0= 'aa8696', f1= '(8696)Notifications')
    db.dform0examples.insert( f0= 'aa8698', f1= '(8698)Alerts')
    db.dform0examples.insert( f0= 'aa8700', f1= '(8700)Modals')
    db.dform0examples.insert( f0= 'aa8702', f1= '(8702)Buttons')
    db.dform0examples.insert( f0= 'aa8704', f1= '(8704)Tabs')
    db.dform0examples.insert( f0= 'aa8706', f1= '(8706)Accordion')
    db.dform0examples.insert( f0= 'aa8708', f1= '(8708)Dialogs')
    db.dform0examples.insert( f0= 'aa8710', f1= '(8710)Popovers')
    db.dform0examples.insert( f0= 'aa8712', f1= '(8712)Tooltips')
    db.dform0examples.insert( f0= 'aa8714', f1= '(8714)Dropdowns')
    db.dform0examples.insert( f0= 'aa8715', f1= '(8715)Pages')
    db.dform0examples.insert( f0= 'aa8717', f1= '(8717)Contact')
    db.dform0examples.insert( f0= 'aa8719', f1= '(8719)Invoice')
    db.dform0examples.insert( f0= 'aa8721', f1= '(8721)Typography')
    db.dform0examples.insert( f0= 'aa8723', f1= '(8723)Color')
    db.dform0examples.insert( f0= 'aa8725', f1= '(8725)Login Register')
    db.dform0examples.insert( f0= 'aa8727', f1= '(8727)404 Page')
    db.dform0examples.insert( f0= 'aa8729', f1= '(8729)Dashboard One')
    db.dform0examples.insert( f0= 'aa8731', f1= '(8731)Dashboard Two')
    db.dform0examples.insert( f0= 'aa8733', f1= '(8733)Dashboard Three')
    db.dform0examples.insert( f0= 'aa8735', f1= '(8735)Dashboard Four')
    db.dform0examples.insert( f0= 'aa8737', f1= '(8737)Analytics')
    db.dform0examples.insert( f0= 'aa8739', f1= '(8739)Widgets')
    db.dform0examples.insert( f0= 'aa8741', f1= '(8741)Inbox')
    db.dform0examples.insert( f0= 'aa8743', f1= '(8743)View Email')
    db.dform0examples.insert( f0= 'aa8745', f1= '(8745)Compose Email')
    db.dform0examples.insert( f0= 'aa8747', f1= '(8747)Animations')
    db.dform0examples.insert( f0= 'aa8749', f1= '(8749)Google Map')
    db.dform0examples.insert( f0= 'aa8751', f1= '(8751)Data Maps')
    db.dform0examples.insert( f0= 'aa8753', f1= '(8753)Code Editor')
    db.dform0examples.insert( f0= 'aa8755', f1= '(8755)Images Cropper')
    db.dform0examples.insert( f0= 'aa8757', f1= '(8757)Wizard')
    db.dform0examples.insert( f0= 'aa8759', f1= '(8759)Flot Charts')
    db.dform0examples.insert( f0= 'aa8761', f1= '(8761)Bar Charts')
    db.dform0examples.insert( f0= 'aa8763', f1= '(8763)Line Charts')
    db.dform0examples.insert( f0= 'aa8765', f1= '(8765)Area Charts')
    db.dform0examples.insert( f0= 'aa8767', f1= '(8767)Normal Table')
    db.dform0examples.insert( f0= 'aa8769', f1= '(8769)Data Table')
    db.dform0examples.insert( f0= 'aa8771', f1= '(8771)Form Elements')
    db.dform0examples.insert( f0= 'aa8773', f1= '(8773)Form Components')
    db.dform0examples.insert( f0= 'aa8775', f1= '(8775)Form Examples')
    db.dform0examples.insert( f0= 'aa8777', f1= '(8777)Notifications')
    db.dform0examples.insert( f0= 'aa8779', f1= '(8779)Alerts')
    db.dform0examples.insert( f0= 'aa8781', f1= '(8781)Modals')
    db.dform0examples.insert( f0= 'aa8783', f1= '(8783)Buttons')
    db.dform0examples.insert( f0= 'aa8785', f1= '(8785)Tabs')
    db.dform0examples.insert( f0= 'aa8787', f1= '(8787)Accordion')
    db.dform0examples.insert( f0= 'aa8789', f1= '(8789)Dialogs')
    db.dform0examples.insert( f0= 'aa8791', f1= '(8791)Popovers')
    db.dform0examples.insert( f0= 'aa8793', f1= '(8793)Tooltips')
    db.dform0examples.insert( f0= 'aa8795', f1= '(8795)Dropdowns')
    db.dform0examples.insert( f0= 'aa8797', f1= '(8797)Contact')
    db.dform0examples.insert( f0= 'aa8799', f1= '(8799)Invoice')
    db.dform0examples.insert( f0= 'aa8801', f1= '(8801)Typography')
    db.dform0examples.insert( f0= 'aa8803', f1= '(8803)Color')
    db.dform0examples.insert( f0= 'aa8805', f1= '(8805)Login Register')
    db.dform0examples.insert( f0= 'aa8807', f1= '(8807)404 Page')
    db.dform0examples.insert( f0= 'hh8808', f1= '(8808)Form Examples')
    db.dform0examples.insert( f0= 'sx8809', f1= '(8809)Admin Template')
    db.dform0examples.insert( f0= 'pf8810', f1= '(8810)Welcome to Notika')
    db.dform0examples.insert( f0= 'hh8811', f1= '(8811)Basic Example')
    db.dform0examples.insert( f0= 'pf8812', f1= '(8812)Individual form controls automatically receive some global styling. All textual input , textarea , and select elements with')
    db.dform0examples.insert( f0= 'pb8813', f1= '(8813)Enter Email')
    db.dform0examples.insert( f0= 'pb8814', f1= '(8814)Password')
    db.dform0examples.insert( f0= 'bu8815', f1= '(8815)Submit')
    db.dform0examples.insert( f0= 'hh8816', f1= '(8816)Inline Form')
    db.dform0examples.insert( f0= 'pb8817', f1= '(8817)Enter Email')
    db.dform0examples.insert( f0= 'pb8818', f1= '(8818)Password')
    db.dform0examples.insert( f0= 'bu8819', f1= '(8819)Submit')
    db.dform0examples.insert( f0= 'hh8820', f1= '(8820)Horizontal Form')
    db.dform0examples.insert( f0= 'pb8821', f1= '(8821)Enter Email')
    db.dform0examples.insert( f0= 'pb8822', f1= '(8822)Password')
    db.dform0examples.insert( f0= 'bu8823', f1= '(8823)Submit')
    db.commit()
#
