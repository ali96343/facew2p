#
# table for controller: contact
#

from gluon.contrib.populate import populate

db.define_table('dcontact', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcontact.id ).count():
    db.dcontact.insert( f0= 'sp7608', f1= '(7608)outdated')
    db.dcontact.insert( f0= 'pc7609', f1= '(7609)to improve your experience.')
    db.dcontact.insert( f0= 'aa7610', f1= '(7610)upgrade your browser')
    db.dcontact.insert( f0= 'hh7612', f1= '(7612)Messages')
    db.dcontact.insert( f0= 'hh7614', f1= '(7614)David Belle')
    db.dcontact.insert( f0= 'pa7615', f1= '(7615)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dcontact.insert( f0= 'hh7617', f1= '(7617)Jonathan Morris')
    db.dcontact.insert( f0= 'pa7618', f1= '(7618)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dcontact.insert( f0= 'hh7620', f1= '(7620)Fredric Mitchell')
    db.dcontact.insert( f0= 'pa7621', f1= '(7621)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dcontact.insert( f0= 'hh7623', f1= '(7623)David Belle')
    db.dcontact.insert( f0= 'pa7624', f1= '(7624)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dcontact.insert( f0= 'hh7626', f1= '(7626)Glenn Jecobs')
    db.dcontact.insert( f0= 'pa7627', f1= '(7627)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dcontact.insert( f0= 'aa7628', f1= '(7628)View All')
    db.dcontact.insert( f0= 'hh7629', f1= '(7629)Notification')
    db.dcontact.insert( f0= 'hh7631', f1= '(7631)David Belle')
    db.dcontact.insert( f0= 'pa7632', f1= '(7632)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dcontact.insert( f0= 'hh7634', f1= '(7634)Jonathan Morris')
    db.dcontact.insert( f0= 'pa7635', f1= '(7635)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dcontact.insert( f0= 'hh7637', f1= '(7637)Fredric Mitchell')
    db.dcontact.insert( f0= 'pa7638', f1= '(7638)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dcontact.insert( f0= 'hh7640', f1= '(7640)David Belle')
    db.dcontact.insert( f0= 'pa7641', f1= '(7641)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dcontact.insert( f0= 'hh7643', f1= '(7643)Glenn Jecobs')
    db.dcontact.insert( f0= 'pa7644', f1= '(7644)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dcontact.insert( f0= 'aa7645', f1= '(7645)View All')
    db.dcontact.insert( f0= 'hh7646', f1= '(7646)Tasks')
    db.dcontact.insert( f0= 'pa7647', f1= '(7647)HTML5 Validation Report')
    db.dcontact.insert( f0= 'sp7648', f1= '(7648)95%')
    db.dcontact.insert( f0= 'pa7649', f1= '(7649)Google Chrome Extension')
    db.dcontact.insert( f0= 'sp7650', f1= '(7650)85%')
    db.dcontact.insert( f0= 'pa7651', f1= '(7651)Social Internet Projects')
    db.dcontact.insert( f0= 'sp7652', f1= '(7652)93%')
    db.dcontact.insert( f0= 'pa7653', f1= '(7653)Bootstrap Admin Template')
    db.dcontact.insert( f0= 'sp7654', f1= '(7654)93%')
    db.dcontact.insert( f0= 'pa7655', f1= '(7655)Youtube Client App')
    db.dcontact.insert( f0= 'sp7656', f1= '(7656)93%')
    db.dcontact.insert( f0= 'aa7657', f1= '(7657)View All')
    db.dcontact.insert( f0= 'hh7658', f1= '(7658)Chat')
    db.dcontact.insert( f0= 'pb7659', f1= '(7659)Search People')
    db.dcontact.insert( f0= 'hh7661', f1= '(7661)David Belle')
    db.dcontact.insert( f0= 'pa7662', f1= '(7662)Available')
    db.dcontact.insert( f0= 'hh7664', f1= '(7664)Jonathan Morris')
    db.dcontact.insert( f0= 'pa7665', f1= '(7665)Last seen 3 hours ago')
    db.dcontact.insert( f0= 'hh7667', f1= '(7667)Fredric Mitchell')
    db.dcontact.insert( f0= 'pa7668', f1= '(7668)Last seen 2 minutes ago')
    db.dcontact.insert( f0= 'hh7670', f1= '(7670)David Belle')
    db.dcontact.insert( f0= 'pa7671', f1= '(7671)Available')
    db.dcontact.insert( f0= 'hh7673', f1= '(7673)Glenn Jecobs')
    db.dcontact.insert( f0= 'pa7674', f1= '(7674)Available')
    db.dcontact.insert( f0= 'aa7675', f1= '(7675)View All')
    db.dcontact.insert( f0= 'aa7676', f1= '(7676)Home')
    db.dcontact.insert( f0= 'aa7678', f1= '(7678)Dashboard One')
    db.dcontact.insert( f0= 'aa7680', f1= '(7680)Dashboard Two')
    db.dcontact.insert( f0= 'aa7682', f1= '(7682)Dashboard Three')
    db.dcontact.insert( f0= 'aa7684', f1= '(7684)Dashboard Four')
    db.dcontact.insert( f0= 'aa7686', f1= '(7686)Analytics')
    db.dcontact.insert( f0= 'aa7688', f1= '(7688)Widgets')
    db.dcontact.insert( f0= 'aa7689', f1= '(7689)Email')
    db.dcontact.insert( f0= 'aa7691', f1= '(7691)Inbox')
    db.dcontact.insert( f0= 'aa7693', f1= '(7693)View Email')
    db.dcontact.insert( f0= 'aa7695', f1= '(7695)Compose Email')
    db.dcontact.insert( f0= 'aa7696', f1= '(7696)Interface')
    db.dcontact.insert( f0= 'aa7698', f1= '(7698)Animations')
    db.dcontact.insert( f0= 'aa7700', f1= '(7700)Google Map')
    db.dcontact.insert( f0= 'aa7702', f1= '(7702)Data Maps')
    db.dcontact.insert( f0= 'aa7704', f1= '(7704)Code Editor')
    db.dcontact.insert( f0= 'aa7706', f1= '(7706)Images Cropper')
    db.dcontact.insert( f0= 'aa7708', f1= '(7708)Wizard')
    db.dcontact.insert( f0= 'aa7709', f1= '(7709)Charts')
    db.dcontact.insert( f0= 'aa7711', f1= '(7711)Flot Charts')
    db.dcontact.insert( f0= 'aa7713', f1= '(7713)Bar Charts')
    db.dcontact.insert( f0= 'aa7715', f1= '(7715)Line Charts')
    db.dcontact.insert( f0= 'aa7717', f1= '(7717)Area Charts')
    db.dcontact.insert( f0= 'aa7718', f1= '(7718)Tables')
    db.dcontact.insert( f0= 'aa7720', f1= '(7720)Normal Table')
    db.dcontact.insert( f0= 'aa7722', f1= '(7722)Data Table')
    db.dcontact.insert( f0= 'aa7723', f1= '(7723)Forms')
    db.dcontact.insert( f0= 'aa7725', f1= '(7725)Form Elements')
    db.dcontact.insert( f0= 'aa7727', f1= '(7727)Form Components')
    db.dcontact.insert( f0= 'aa7729', f1= '(7729)Form Examples')
    db.dcontact.insert( f0= 'aa7730', f1= '(7730)App views')
    db.dcontact.insert( f0= 'aa7732', f1= '(7732)Notifications')
    db.dcontact.insert( f0= 'aa7734', f1= '(7734)Alerts')
    db.dcontact.insert( f0= 'aa7736', f1= '(7736)Modals')
    db.dcontact.insert( f0= 'aa7738', f1= '(7738)Buttons')
    db.dcontact.insert( f0= 'aa7740', f1= '(7740)Tabs')
    db.dcontact.insert( f0= 'aa7742', f1= '(7742)Accordion')
    db.dcontact.insert( f0= 'aa7744', f1= '(7744)Dialogs')
    db.dcontact.insert( f0= 'aa7746', f1= '(7746)Popovers')
    db.dcontact.insert( f0= 'aa7748', f1= '(7748)Tooltips')
    db.dcontact.insert( f0= 'aa7750', f1= '(7750)Dropdowns')
    db.dcontact.insert( f0= 'aa7751', f1= '(7751)Pages')
    db.dcontact.insert( f0= 'aa7753', f1= '(7753)Contact')
    db.dcontact.insert( f0= 'aa7755', f1= '(7755)Invoice')
    db.dcontact.insert( f0= 'aa7757', f1= '(7757)Typography')
    db.dcontact.insert( f0= 'aa7759', f1= '(7759)Color')
    db.dcontact.insert( f0= 'aa7761', f1= '(7761)Login Register')
    db.dcontact.insert( f0= 'aa7763', f1= '(7763)404 Page')
    db.dcontact.insert( f0= 'aa7765', f1= '(7765)Dashboard One')
    db.dcontact.insert( f0= 'aa7767', f1= '(7767)Dashboard Two')
    db.dcontact.insert( f0= 'aa7769', f1= '(7769)Dashboard Three')
    db.dcontact.insert( f0= 'aa7771', f1= '(7771)Dashboard Four')
    db.dcontact.insert( f0= 'aa7773', f1= '(7773)Analytics')
    db.dcontact.insert( f0= 'aa7775', f1= '(7775)Widgets')
    db.dcontact.insert( f0= 'aa7777', f1= '(7777)Inbox')
    db.dcontact.insert( f0= 'aa7779', f1= '(7779)View Email')
    db.dcontact.insert( f0= 'aa7781', f1= '(7781)Compose Email')
    db.dcontact.insert( f0= 'aa7783', f1= '(7783)Animations')
    db.dcontact.insert( f0= 'aa7785', f1= '(7785)Google Map')
    db.dcontact.insert( f0= 'aa7787', f1= '(7787)Data Maps')
    db.dcontact.insert( f0= 'aa7789', f1= '(7789)Code Editor')
    db.dcontact.insert( f0= 'aa7791', f1= '(7791)Images Cropper')
    db.dcontact.insert( f0= 'aa7793', f1= '(7793)Wizard')
    db.dcontact.insert( f0= 'aa7795', f1= '(7795)Flot Charts')
    db.dcontact.insert( f0= 'aa7797', f1= '(7797)Bar Charts')
    db.dcontact.insert( f0= 'aa7799', f1= '(7799)Line Charts')
    db.dcontact.insert( f0= 'aa7801', f1= '(7801)Area Charts')
    db.dcontact.insert( f0= 'aa7803', f1= '(7803)Normal Table')
    db.dcontact.insert( f0= 'aa7805', f1= '(7805)Data Table')
    db.dcontact.insert( f0= 'aa7807', f1= '(7807)Form Elements')
    db.dcontact.insert( f0= 'aa7809', f1= '(7809)Form Components')
    db.dcontact.insert( f0= 'aa7811', f1= '(7811)Form Examples')
    db.dcontact.insert( f0= 'aa7813', f1= '(7813)Notifications')
    db.dcontact.insert( f0= 'aa7815', f1= '(7815)Alerts')
    db.dcontact.insert( f0= 'aa7817', f1= '(7817)Modals')
    db.dcontact.insert( f0= 'aa7819', f1= '(7819)Buttons')
    db.dcontact.insert( f0= 'aa7821', f1= '(7821)Tabs')
    db.dcontact.insert( f0= 'aa7823', f1= '(7823)Accordion')
    db.dcontact.insert( f0= 'aa7825', f1= '(7825)Dialogs')
    db.dcontact.insert( f0= 'aa7827', f1= '(7827)Popovers')
    db.dcontact.insert( f0= 'aa7829', f1= '(7829)Tooltips')
    db.dcontact.insert( f0= 'aa7831', f1= '(7831)Dropdowns')
    db.dcontact.insert( f0= 'aa7833', f1= '(7833)Contact')
    db.dcontact.insert( f0= 'aa7835', f1= '(7835)Invoice')
    db.dcontact.insert( f0= 'aa7837', f1= '(7837)Typography')
    db.dcontact.insert( f0= 'aa7839', f1= '(7839)Color')
    db.dcontact.insert( f0= 'aa7841', f1= '(7841)Login Register')
    db.dcontact.insert( f0= 'aa7843', f1= '(7843)404 Page')
    db.dcontact.insert( f0= 'hh7844', f1= '(7844)Contact')
    db.dcontact.insert( f0= 'sx7845', f1= '(7845)Admin Template')
    db.dcontact.insert( f0= 'pf7846', f1= '(7846)Welcome to Notika')
    db.dcontact.insert( f0= 'hh7848', f1= '(7848)John Deo')
    db.dcontact.insert( f0= 'pc7849', f1= '(7849)USA, LA, aus')
    db.dcontact.insert( f0= 'pa7850', f1= '(7850)Lorem ipsum dolor sit amete of the, consectetur adipiscing elitable. Vestibulum tincidunt.')
    db.dcontact.insert( f0= 'hh7851', f1= '(7851)Likes:')
    db.dcontact.insert( f0= 'pa7852', f1= '(7852)956')
    db.dcontact.insert( f0= 'hh7853', f1= '(7853)Comments:')
    db.dcontact.insert( f0= 'pa7854', f1= '(7854)434')
    db.dcontact.insert( f0= 'hh7855', f1= '(7855)Views:')
    db.dcontact.insert( f0= 'pa7856', f1= '(7856)676')
    db.dcontact.insert( f0= 'hh7858', f1= '(7858)Smith')
    db.dcontact.insert( f0= 'pc7859', f1= '(7859)Aus, LA, aus')
    db.dcontact.insert( f0= 'pa7860', f1= '(7860)Lorem ipsum dolor sit amete of the, consectetur adipiscing elitable. Vestibulum tincidunt.')
    db.dcontact.insert( f0= 'hh7861', f1= '(7861)Likes:')
    db.dcontact.insert( f0= 'pa7862', f1= '(7862)956')
    db.dcontact.insert( f0= 'hh7863', f1= '(7863)Comments:')
    db.dcontact.insert( f0= 'pa7864', f1= '(7864)434')
    db.dcontact.insert( f0= 'hh7865', f1= '(7865)Views:')
    db.dcontact.insert( f0= 'pa7866', f1= '(7866)676')
    db.dcontact.insert( f0= 'hh7868', f1= '(7868)Malika')
    db.dcontact.insert( f0= 'pc7869', f1= '(7869)Thi, LA, aus')
    db.dcontact.insert( f0= 'pa7870', f1= '(7870)Lorem ipsum dolor sit amete of the, consectetur adipiscing elitable. Vestibulum tincidunt.')
    db.dcontact.insert( f0= 'hh7871', f1= '(7871)Likes:')
    db.dcontact.insert( f0= 'pa7872', f1= '(7872)956')
    db.dcontact.insert( f0= 'hh7873', f1= '(7873)Comments:')
    db.dcontact.insert( f0= 'pa7874', f1= '(7874)434')
    db.dcontact.insert( f0= 'hh7875', f1= '(7875)Views:')
    db.dcontact.insert( f0= 'pa7876', f1= '(7876)676')
    db.dcontact.insert( f0= 'hh7878', f1= '(7878)John Deo')
    db.dcontact.insert( f0= 'pc7879', f1= '(7879)BG, LA, aus')
    db.dcontact.insert( f0= 'pa7880', f1= '(7880)Lorem ipsum dolor sit amete of the, consectetur adipiscing elitable. Vestibulum tincidunt.')
    db.dcontact.insert( f0= 'hh7881', f1= '(7881)Likes:')
    db.dcontact.insert( f0= 'pa7882', f1= '(7882)956')
    db.dcontact.insert( f0= 'hh7883', f1= '(7883)Comments:')
    db.dcontact.insert( f0= 'pa7884', f1= '(7884)434')
    db.dcontact.insert( f0= 'hh7885', f1= '(7885)Views:')
    db.dcontact.insert( f0= 'pa7886', f1= '(7886)676')
    db.dcontact.insert( f0= 'hh7888', f1= '(7888)John Deo')
    db.dcontact.insert( f0= 'pc7889', f1= '(7889)In, LA, aus')
    db.dcontact.insert( f0= 'pa7890', f1= '(7890)Lorem ipsum dolor sit amete of the, consectetur adipiscing elitable. Vestibulum tincidunt.')
    db.dcontact.insert( f0= 'hh7891', f1= '(7891)Likes:')
    db.dcontact.insert( f0= 'pa7892', f1= '(7892)956')
    db.dcontact.insert( f0= 'hh7893', f1= '(7893)Comments:')
    db.dcontact.insert( f0= 'pa7894', f1= '(7894)434')
    db.dcontact.insert( f0= 'hh7895', f1= '(7895)Views:')
    db.dcontact.insert( f0= 'pa7896', f1= '(7896)676')
    db.dcontact.insert( f0= 'hh7898', f1= '(7898)Smith')
    db.dcontact.insert( f0= 'pc7899', f1= '(7899)Pk, LA, aus')
    db.dcontact.insert( f0= 'pa7900', f1= '(7900)Lorem ipsum dolor sit amete of the, consectetur adipiscing elitable. Vestibulum tincidunt.')
    db.dcontact.insert( f0= 'hh7901', f1= '(7901)Likes:')
    db.dcontact.insert( f0= 'pa7902', f1= '(7902)956')
    db.dcontact.insert( f0= 'hh7903', f1= '(7903)Comments:')
    db.dcontact.insert( f0= 'pa7904', f1= '(7904)434')
    db.dcontact.insert( f0= 'hh7905', f1= '(7905)Views:')
    db.dcontact.insert( f0= 'pa7906', f1= '(7906)676')
    db.dcontact.insert( f0= 'hh7908', f1= '(7908)Malika')
    db.dcontact.insert( f0= 'pc7909', f1= '(7909)London, LA, aus')
    db.dcontact.insert( f0= 'pa7910', f1= '(7910)Lorem ipsum dolor sit amete of the, consectetur adipiscing elitable. Vestibulum tincidunt.')
    db.dcontact.insert( f0= 'hh7911', f1= '(7911)Likes:')
    db.dcontact.insert( f0= 'pa7912', f1= '(7912)956')
    db.dcontact.insert( f0= 'hh7913', f1= '(7913)Comments:')
    db.dcontact.insert( f0= 'pa7914', f1= '(7914)434')
    db.dcontact.insert( f0= 'hh7915', f1= '(7915)Views:')
    db.dcontact.insert( f0= 'pa7916', f1= '(7916)676')
    db.dcontact.insert( f0= 'hh7918', f1= '(7918)John Deo')
    db.dcontact.insert( f0= 'pc7919', f1= '(7919)Aus, LA, aus')
    db.dcontact.insert( f0= 'pa7920', f1= '(7920)Lorem ipsum dolor sit amete of the, consectetur adipiscing elitable. Vestibulum tincidunt.')
    db.dcontact.insert( f0= 'hh7921', f1= '(7921)Likes:')
    db.dcontact.insert( f0= 'pa7922', f1= '(7922)956')
    db.dcontact.insert( f0= 'hh7923', f1= '(7923)Comments:')
    db.dcontact.insert( f0= 'pa7924', f1= '(7924)434')
    db.dcontact.insert( f0= 'hh7925', f1= '(7925)Views:')
    db.dcontact.insert( f0= 'pa7926', f1= '(7926)676')
    db.commit()
#
