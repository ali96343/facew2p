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
    db.dwidgets.insert( f0= 'sp9566', f1= '(9566)outdated')
    db.dwidgets.insert( f0= 'pc9567', f1= '(9567)to improve your experience.')
    db.dwidgets.insert( f0= 'aa9568', f1= '(9568)upgrade your browser')
    db.dwidgets.insert( f0= 'hh9570', f1= '(9570)Messages')
    db.dwidgets.insert( f0= 'hh9572', f1= '(9572)David Belle')
    db.dwidgets.insert( f0= 'pa9573', f1= '(9573)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dwidgets.insert( f0= 'hh9575', f1= '(9575)Jonathan Morris')
    db.dwidgets.insert( f0= 'pa9576', f1= '(9576)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dwidgets.insert( f0= 'hh9578', f1= '(9578)Fredric Mitchell')
    db.dwidgets.insert( f0= 'pa9579', f1= '(9579)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dwidgets.insert( f0= 'hh9581', f1= '(9581)David Belle')
    db.dwidgets.insert( f0= 'pa9582', f1= '(9582)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dwidgets.insert( f0= 'hh9584', f1= '(9584)Glenn Jecobs')
    db.dwidgets.insert( f0= 'pa9585', f1= '(9585)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dwidgets.insert( f0= 'aa9586', f1= '(9586)View All')
    db.dwidgets.insert( f0= 'hh9587', f1= '(9587)Notification')
    db.dwidgets.insert( f0= 'hh9589', f1= '(9589)David Belle')
    db.dwidgets.insert( f0= 'pa9590', f1= '(9590)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dwidgets.insert( f0= 'hh9592', f1= '(9592)Jonathan Morris')
    db.dwidgets.insert( f0= 'pa9593', f1= '(9593)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dwidgets.insert( f0= 'hh9595', f1= '(9595)Fredric Mitchell')
    db.dwidgets.insert( f0= 'pa9596', f1= '(9596)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dwidgets.insert( f0= 'hh9598', f1= '(9598)David Belle')
    db.dwidgets.insert( f0= 'pa9599', f1= '(9599)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dwidgets.insert( f0= 'hh9601', f1= '(9601)Glenn Jecobs')
    db.dwidgets.insert( f0= 'pa9602', f1= '(9602)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dwidgets.insert( f0= 'aa9603', f1= '(9603)View All')
    db.dwidgets.insert( f0= 'hh9604', f1= '(9604)Tasks')
    db.dwidgets.insert( f0= 'pa9605', f1= '(9605)HTML5 Validation Report')
    db.dwidgets.insert( f0= 'sp9606', f1= '(9606)95%')
    db.dwidgets.insert( f0= 'pa9607', f1= '(9607)Google Chrome Extension')
    db.dwidgets.insert( f0= 'sp9608', f1= '(9608)85%')
    db.dwidgets.insert( f0= 'pa9609', f1= '(9609)Social Internet Projects')
    db.dwidgets.insert( f0= 'sp9610', f1= '(9610)75%')
    db.dwidgets.insert( f0= 'pa9611', f1= '(9611)Bootstrap Admin')
    db.dwidgets.insert( f0= 'sp9612', f1= '(9612)65%')
    db.dwidgets.insert( f0= 'pa9613', f1= '(9613)Youtube App')
    db.dwidgets.insert( f0= 'sp9614', f1= '(9614)55%')
    db.dwidgets.insert( f0= 'aa9615', f1= '(9615)View All')
    db.dwidgets.insert( f0= 'hh9616', f1= '(9616)Chat')
    db.dwidgets.insert( f0= 'pb9617', f1= '(9617)Search People')
    db.dwidgets.insert( f0= 'hh9619', f1= '(9619)David Belle')
    db.dwidgets.insert( f0= 'pa9620', f1= '(9620)Available')
    db.dwidgets.insert( f0= 'hh9622', f1= '(9622)Jonathan Morris')
    db.dwidgets.insert( f0= 'pa9623', f1= '(9623)Last seen 3 hours ago')
    db.dwidgets.insert( f0= 'hh9625', f1= '(9625)Fredric Mitchell')
    db.dwidgets.insert( f0= 'pa9626', f1= '(9626)Last seen 2 minutes ago')
    db.dwidgets.insert( f0= 'hh9628', f1= '(9628)David Belle')
    db.dwidgets.insert( f0= 'pa9629', f1= '(9629)Available')
    db.dwidgets.insert( f0= 'hh9631', f1= '(9631)Glenn Jecobs')
    db.dwidgets.insert( f0= 'pa9632', f1= '(9632)Available')
    db.dwidgets.insert( f0= 'aa9633', f1= '(9633)View All')
    db.dwidgets.insert( f0= 'aa9634', f1= '(9634)Home')
    db.dwidgets.insert( f0= 'aa9636', f1= '(9636)Dashboard One')
    db.dwidgets.insert( f0= 'aa9638', f1= '(9638)Dashboard Two')
    db.dwidgets.insert( f0= 'aa9640', f1= '(9640)Dashboard Three')
    db.dwidgets.insert( f0= 'aa9642', f1= '(9642)Dashboard Four')
    db.dwidgets.insert( f0= 'aa9644', f1= '(9644)Analytics')
    db.dwidgets.insert( f0= 'aa9646', f1= '(9646)Widgets')
    db.dwidgets.insert( f0= 'aa9647', f1= '(9647)Email')
    db.dwidgets.insert( f0= 'aa9649', f1= '(9649)Inbox')
    db.dwidgets.insert( f0= 'aa9651', f1= '(9651)View Email')
    db.dwidgets.insert( f0= 'aa9653', f1= '(9653)Compose Email')
    db.dwidgets.insert( f0= 'aa9654', f1= '(9654)Interface')
    db.dwidgets.insert( f0= 'aa9656', f1= '(9656)Animations')
    db.dwidgets.insert( f0= 'aa9658', f1= '(9658)Google Map')
    db.dwidgets.insert( f0= 'aa9660', f1= '(9660)Data Maps')
    db.dwidgets.insert( f0= 'aa9662', f1= '(9662)Code Editor')
    db.dwidgets.insert( f0= 'aa9664', f1= '(9664)Images Cropper')
    db.dwidgets.insert( f0= 'aa9666', f1= '(9666)Wizard')
    db.dwidgets.insert( f0= 'aa9667', f1= '(9667)Charts')
    db.dwidgets.insert( f0= 'aa9669', f1= '(9669)Flot Charts')
    db.dwidgets.insert( f0= 'aa9671', f1= '(9671)Bar Charts')
    db.dwidgets.insert( f0= 'aa9673', f1= '(9673)Line Charts')
    db.dwidgets.insert( f0= 'aa9675', f1= '(9675)Area Charts')
    db.dwidgets.insert( f0= 'aa9676', f1= '(9676)Tables')
    db.dwidgets.insert( f0= 'aa9678', f1= '(9678)Normal Table')
    db.dwidgets.insert( f0= 'aa9680', f1= '(9680)Data Table')
    db.dwidgets.insert( f0= 'aa9681', f1= '(9681)Forms')
    db.dwidgets.insert( f0= 'aa9683', f1= '(9683)Form Elements')
    db.dwidgets.insert( f0= 'aa9685', f1= '(9685)Form Components')
    db.dwidgets.insert( f0= 'aa9687', f1= '(9687)Form Examples')
    db.dwidgets.insert( f0= 'aa9688', f1= '(9688)App views')
    db.dwidgets.insert( f0= 'aa9690', f1= '(9690)Notifications')
    db.dwidgets.insert( f0= 'aa9692', f1= '(9692)Alerts')
    db.dwidgets.insert( f0= 'aa9694', f1= '(9694)Modals')
    db.dwidgets.insert( f0= 'aa9696', f1= '(9696)Buttons')
    db.dwidgets.insert( f0= 'aa9698', f1= '(9698)Tabs')
    db.dwidgets.insert( f0= 'aa9700', f1= '(9700)Accordion')
    db.dwidgets.insert( f0= 'aa9702', f1= '(9702)Dialogs')
    db.dwidgets.insert( f0= 'aa9704', f1= '(9704)Popovers')
    db.dwidgets.insert( f0= 'aa9706', f1= '(9706)Tooltips')
    db.dwidgets.insert( f0= 'aa9708', f1= '(9708)Dropdowns')
    db.dwidgets.insert( f0= 'aa9709', f1= '(9709)Pages')
    db.dwidgets.insert( f0= 'aa9711', f1= '(9711)Contact')
    db.dwidgets.insert( f0= 'aa9713', f1= '(9713)Invoice')
    db.dwidgets.insert( f0= 'aa9715', f1= '(9715)Typography')
    db.dwidgets.insert( f0= 'aa9717', f1= '(9717)Color')
    db.dwidgets.insert( f0= 'aa9719', f1= '(9719)Login Register')
    db.dwidgets.insert( f0= 'aa9721', f1= '(9721)404 Page')
    db.dwidgets.insert( f0= 'aa9723', f1= '(9723)Dashboard One')
    db.dwidgets.insert( f0= 'aa9725', f1= '(9725)Dashboard Two')
    db.dwidgets.insert( f0= 'aa9727', f1= '(9727)Dashboard Three')
    db.dwidgets.insert( f0= 'aa9729', f1= '(9729)Dashboard Four')
    db.dwidgets.insert( f0= 'aa9731', f1= '(9731)Analytics')
    db.dwidgets.insert( f0= 'aa9733', f1= '(9733)Widgets')
    db.dwidgets.insert( f0= 'aa9735', f1= '(9735)Inbox')
    db.dwidgets.insert( f0= 'aa9737', f1= '(9737)View Email')
    db.dwidgets.insert( f0= 'aa9739', f1= '(9739)Compose Email')
    db.dwidgets.insert( f0= 'aa9741', f1= '(9741)Animations')
    db.dwidgets.insert( f0= 'aa9743', f1= '(9743)Google Map')
    db.dwidgets.insert( f0= 'aa9745', f1= '(9745)Data Maps')
    db.dwidgets.insert( f0= 'aa9747', f1= '(9747)Code Editor')
    db.dwidgets.insert( f0= 'aa9749', f1= '(9749)Images Cropper')
    db.dwidgets.insert( f0= 'aa9751', f1= '(9751)Wizard')
    db.dwidgets.insert( f0= 'aa9753', f1= '(9753)Flot Charts')
    db.dwidgets.insert( f0= 'aa9755', f1= '(9755)Bar Charts')
    db.dwidgets.insert( f0= 'aa9757', f1= '(9757)Line Charts')
    db.dwidgets.insert( f0= 'aa9759', f1= '(9759)Area Charts')
    db.dwidgets.insert( f0= 'aa9761', f1= '(9761)Normal Table')
    db.dwidgets.insert( f0= 'aa9763', f1= '(9763)Data Table')
    db.dwidgets.insert( f0= 'aa9765', f1= '(9765)Form Elements')
    db.dwidgets.insert( f0= 'aa9767', f1= '(9767)Form Components')
    db.dwidgets.insert( f0= 'aa9769', f1= '(9769)Form Examples')
    db.dwidgets.insert( f0= 'aa9771', f1= '(9771)Notifications')
    db.dwidgets.insert( f0= 'aa9773', f1= '(9773)Alerts')
    db.dwidgets.insert( f0= 'aa9775', f1= '(9775)Modals')
    db.dwidgets.insert( f0= 'aa9777', f1= '(9777)Buttons')
    db.dwidgets.insert( f0= 'aa9779', f1= '(9779)Tabs')
    db.dwidgets.insert( f0= 'aa9781', f1= '(9781)Accordion')
    db.dwidgets.insert( f0= 'aa9783', f1= '(9783)Dialogs')
    db.dwidgets.insert( f0= 'aa9785', f1= '(9785)Popovers')
    db.dwidgets.insert( f0= 'aa9787', f1= '(9787)Tooltips')
    db.dwidgets.insert( f0= 'aa9789', f1= '(9789)Dropdowns')
    db.dwidgets.insert( f0= 'aa9791', f1= '(9791)Contact')
    db.dwidgets.insert( f0= 'aa9793', f1= '(9793)Invoice')
    db.dwidgets.insert( f0= 'aa9795', f1= '(9795)Typography')
    db.dwidgets.insert( f0= 'aa9797', f1= '(9797)Color')
    db.dwidgets.insert( f0= 'aa9799', f1= '(9799)Login Register')
    db.dwidgets.insert( f0= 'aa9801', f1= '(9801)404 Page')
    db.dwidgets.insert( f0= 'hh9802', f1= '(9802)Widgets')
    db.dwidgets.insert( f0= 'sx9803', f1= '(9803)Admin Template')
    db.dwidgets.insert( f0= 'pf9804', f1= '(9804)Welcome to Notika')
    db.dwidgets.insert( f0= 'pa9805', f1= '(9805)Website Impressions')
    db.dwidgets.insert( f0= 'pa9806', f1= '(9806)Total Support Tickets')
    db.dwidgets.insert( f0= 'hh9807', f1= '(9807)Most Recent Signups')
    db.dwidgets.insert( f0= 'pa9808', f1= '(9808)Magna cursus malesuada lacinia')
    db.dwidgets.insert( f0= 'hh9821', f1= '(9821)Ongoing Tasks')
    db.dwidgets.insert( f0= 'pa9822', f1= '(9822)Magna cursus malesuada lacinia')
    db.dwidgets.insert( f0= 'pa9823', f1= '(9823)HTML5 Validation Report')
    db.dwidgets.insert( f0= 'sp9824', f1= '(9824)95%')
    db.dwidgets.insert( f0= 'pa9825', f1= '(9825)Google Chrome Extension')
    db.dwidgets.insert( f0= 'sp9826', f1= '(9826)85%')
    db.dwidgets.insert( f0= 'pa9827', f1= '(9827)Social Internet Projects')
    db.dwidgets.insert( f0= 'sp9828', f1= '(9828)70%')
    db.dwidgets.insert( f0= 'pa9829', f1= '(9829)Bootstrap Admin')
    db.dwidgets.insert( f0= 'sp9830', f1= '(9830)60%')
    db.dwidgets.insert( f0= 'pa9831', f1= '(9831)Youtube App')
    db.dwidgets.insert( f0= 'sp9832', f1= '(9832)50%')
    db.dwidgets.insert( f0= 'aa9833', f1= '(9833)View All Tasks')
    db.dwidgets.insert( f0= 'hh9835', f1= '(9835)The best viral website ideas!')
    db.dwidgets.insert( f0= 'aa9836', f1= '(9836)By Malinda on 9th June 2018')
    db.dwidgets.insert( f0= 'aa9837', f1= '(9837)View Article...')
    db.dwidgets.insert( f0= 'hh9838', f1= '(9838)Contact Information')
    db.dwidgets.insert( f0= 'pa9839', f1= '(9839)Fusce eget dolor id justo luctus commodo vel pharetra nisi. Donec velit libero')
    db.dwidgets.insert( f0= 'ma9840', f1= '(9840)lucid@gmail.com')
    db.dwidgets.insert( f0= 'hh9841', f1= '(9841)Sample Form')
    db.dwidgets.insert( f0= 'pa9842', f1= '(9842)Fusce eget dolor id justo luctus commodo vel pharetra nisi. Donec velit libero')
    db.dwidgets.insert( f0= 'pb9843', f1= '(9843)First Name')
    db.dwidgets.insert( f0= 'pb9844', f1= '(9844)Last Name')
    db.dwidgets.insert( f0= 'pb9845', f1= '(9845)Email Address')
    db.dwidgets.insert( f0= 'pb9846', f1= '(9846)Contact Number')
    db.dwidgets.insert( f0= 'pb9847', f1= '(9847)Message')
    db.dwidgets.insert( f0= 'bu9848', f1= '(9848)Button')
    db.dwidgets.insert( f0= 'hh9849', f1= '(9849)Team Activity')
    db.dwidgets.insert( f0= 'pa9850', f1= '(9850)Fusce eget dolor id justo luctus commodo vel pharetra nisi. Donec velit libero')
    db.dwidgets.insert( f0= 'aa9851', f1= '(9851)Tab One')
    db.dwidgets.insert( f0= 'aa9852', f1= '(9852)Tab Two')
    db.dwidgets.insert( f0= 'aa9853', f1= '(9853)Tab Three')
    db.dwidgets.insert( f0= 'pa9855', f1= '(9855)Serhoncus quis est sit amete in nisl molestie of fringilla. Nunc vitae ante magna feugiat condi. Serhoncus quis est cry int fly.')
    db.dwidgets.insert( f0= 'pa9857', f1= '(9857)Serhoncus quis est sit amete in nisl molestie of fringilla. Nunc vitae ante magna feugiat condi. Serhoncus quis est cry int fly.')
    db.dwidgets.insert( f0= 'pa9859', f1= '(9859)Serhoncus quis est sit amete in nisl molestie of fringilla. Nunc vitae ante magna feugiat condi. Serhoncus quis est cry int fly.')
    db.commit()
#
