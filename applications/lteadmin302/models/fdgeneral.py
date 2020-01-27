#
# table for controller: general
#

from gluon.contrib.populate import populate

db.define_table('dgeneral', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dgeneral.id ).count():
    db.dgeneral.insert( f0= 'aa7727', f1= '(7727)Home')
    db.dgeneral.insert( f0= 'aa7728', f1= '(7728)Contact')
    db.dgeneral.insert( f0= 'pb7729', f1= '(7729)Search')
    db.dgeneral.insert( f0= 'sx7730', f1= '(7730)3')
    db.dgeneral.insert( f0= 'pc7732', f1= '(7732)Call me whenever you can...')
    db.dgeneral.insert( f0= 'pc7733', f1= '(7733)4 Hours Ago')
    db.dgeneral.insert( f0= 'pc7735', f1= '(7735)I got your message bro')
    db.dgeneral.insert( f0= 'pc7736', f1= '(7736)4 Hours Ago')
    db.dgeneral.insert( f0= 'pc7738', f1= '(7738)The subject goes here')
    db.dgeneral.insert( f0= 'pc7739', f1= '(7739)4 Hours Ago')
    db.dgeneral.insert( f0= 'aa7740', f1= '(7740)See All Messages')
    db.dgeneral.insert( f0= 'sx7741', f1= '(7741)15 Notifications')
    db.dgeneral.insert( f0= 'sx7742', f1= '(7742)3 mins')
    db.dgeneral.insert( f0= 'sx7743', f1= '(7743)12 hours')
    db.dgeneral.insert( f0= 'sx7744', f1= '(7744)2 days')
    db.dgeneral.insert( f0= 'aa7745', f1= '(7745)See All Notifications')
    db.dgeneral.insert( f0= 'sx7748', f1= '(7748)AdminLTE 3')
    db.dgeneral.insert( f0= 'aa7750', f1= '(7750)Alexander Pierce')
    db.dgeneral.insert( f0= 'pa7752', f1= '(7752)Dashboard v1')
    db.dgeneral.insert( f0= 'pa7754', f1= '(7754)Dashboard v2')
    db.dgeneral.insert( f0= 'pa7756', f1= '(7756)Dashboard v3')
    db.dgeneral.insert( f0= 'sx7758', f1= '(7758)New')
    db.dgeneral.insert( f0= 'sx7759', f1= '(7759)6')
    db.dgeneral.insert( f0= 'pa7761', f1= '(7761)Top Navigation')
    db.dgeneral.insert( f0= 'pa7763', f1= '(7763)Top Navigation + Sidebar')
    db.dgeneral.insert( f0= 'pa7765', f1= '(7765)Boxed')
    db.dgeneral.insert( f0= 'pa7767', f1= '(7767)Fixed Sidebar')
    db.dgeneral.insert( f0= 'pa7769', f1= '(7769)Fixed Navbar')
    db.dgeneral.insert( f0= 'pa7771', f1= '(7771)Fixed Footer')
    db.dgeneral.insert( f0= 'pa7773', f1= '(7773)Collapsed Sidebar')
    db.dgeneral.insert( f0= 'pa7775', f1= '(7775)ChartJS')
    db.dgeneral.insert( f0= 'pa7777', f1= '(7777)Flot')
    db.dgeneral.insert( f0= 'pa7779', f1= '(7779)Inline')
    db.dgeneral.insert( f0= 'pa7781', f1= '(7781)General')
    db.dgeneral.insert( f0= 'pa7783', f1= '(7783)Icons')
    db.dgeneral.insert( f0= 'pa7785', f1= '(7785)Buttons')
    db.dgeneral.insert( f0= 'pa7787', f1= '(7787)Sliders')
    db.dgeneral.insert( f0= 'pa7789', f1= '(7789)Modals & Alerts')
    db.dgeneral.insert( f0= 'pa7791', f1= '(7791)Navbar & Tabs')
    db.dgeneral.insert( f0= 'pa7793', f1= '(7793)Timeline')
    db.dgeneral.insert( f0= 'pa7795', f1= '(7795)Ribbons')
    db.dgeneral.insert( f0= 'pa7797', f1= '(7797)General Elements')
    db.dgeneral.insert( f0= 'pa7799', f1= '(7799)Advanced Elements')
    db.dgeneral.insert( f0= 'pa7801', f1= '(7801)Editors')
    db.dgeneral.insert( f0= 'pa7803', f1= '(7803)Validation')
    db.dgeneral.insert( f0= 'pa7805', f1= '(7805)Simple Tables')
    db.dgeneral.insert( f0= 'pa7807', f1= '(7807)DataTables')
    db.dgeneral.insert( f0= 'pa7809', f1= '(7809)jsGrid')
    db.dgeneral.insert( f0= 'lb7810', f1= '(7810)EXAMPLES')
    db.dgeneral.insert( f0= 'sx7812', f1= '(7812)2')
    db.dgeneral.insert( f0= 'pa7815', f1= '(7815)Inbox')
    db.dgeneral.insert( f0= 'pa7817', f1= '(7817)Compose')
    db.dgeneral.insert( f0= 'pa7819', f1= '(7819)Read')
    db.dgeneral.insert( f0= 'pa7821', f1= '(7821)Invoice')
    db.dgeneral.insert( f0= 'pa7823', f1= '(7823)Profile')
    db.dgeneral.insert( f0= 'pa7825', f1= '(7825)E-commerce')
    db.dgeneral.insert( f0= 'pa7827', f1= '(7827)Projects')
    db.dgeneral.insert( f0= 'pa7829', f1= '(7829)Project Add')
    db.dgeneral.insert( f0= 'pa7831', f1= '(7831)Project Edit')
    db.dgeneral.insert( f0= 'pa7833', f1= '(7833)Project Detail')
    db.dgeneral.insert( f0= 'pa7835', f1= '(7835)Contacts')
    db.dgeneral.insert( f0= 'pa7837', f1= '(7837)Login')
    db.dgeneral.insert( f0= 'pa7839', f1= '(7839)Register')
    db.dgeneral.insert( f0= 'pa7841', f1= '(7841)Forgot Password')
    db.dgeneral.insert( f0= 'pa7843', f1= '(7843)Recover Password')
    db.dgeneral.insert( f0= 'pa7845', f1= '(7845)Lockscreen')
    db.dgeneral.insert( f0= 'pa7847', f1= '(7847)Legacy User Menu')
    db.dgeneral.insert( f0= 'pa7849', f1= '(7849)Language Menu')
    db.dgeneral.insert( f0= 'pa7851', f1= '(7851)Error 404')
    db.dgeneral.insert( f0= 'pa7853', f1= '(7853)Error 500')
    db.dgeneral.insert( f0= 'pa7855', f1= '(7855)Pace')
    db.dgeneral.insert( f0= 'pa7857', f1= '(7857)Blank Page')
    db.dgeneral.insert( f0= 'pa7859', f1= '(7859)Starter Page')
    db.dgeneral.insert( f0= 'lb7860', f1= '(7860)MISCELLANEOUS')
    db.dgeneral.insert( f0= 'pa7861', f1= '(7861)Documentation')
    db.dgeneral.insert( f0= 'lb7862', f1= '(7862)MULTI LEVEL EXAMPLE')
    db.dgeneral.insert( f0= 'pa7863', f1= '(7863)Level 1')
    db.dgeneral.insert( f0= 'pa7864', f1= '(7864)Level 2')
    db.dgeneral.insert( f0= 'pa7865', f1= '(7865)Level 3')
    db.dgeneral.insert( f0= 'pa7866', f1= '(7866)Level 3')
    db.dgeneral.insert( f0= 'pa7867', f1= '(7867)Level 3')
    db.dgeneral.insert( f0= 'pa7868', f1= '(7868)Level 2')
    db.dgeneral.insert( f0= 'pa7869', f1= '(7869)Level 1')
    db.dgeneral.insert( f0= 'lb7870', f1= '(7870)LABELS')
    db.dgeneral.insert( f0= 'pc7871', f1= '(7871)Important')
    db.dgeneral.insert( f0= 'pa7872', f1= '(7872)Warning')
    db.dgeneral.insert( f0= 'pa7873', f1= '(7873)Informational')
    db.dgeneral.insert( f0= 'hh7874', f1= '(7874)Inline Charts')
    db.dgeneral.insert( f0= 'aa7875', f1= '(7875)Home')
    db.dgeneral.insert( f0= 'lb7876', f1= '(7876)Inline Charts')
    db.dgeneral.insert( f0= 'hh7877', f1= '(7877)Theme Colors')
    db.dgeneral.insert( f0= 'hd7878', f1= '(7878)Primary')
    db.dgeneral.insert( f0= 'sp7879', f1= '(7879)Disabled')
    db.dgeneral.insert( f0= 'hd7880', f1= '(7880)Secondary')
    db.dgeneral.insert( f0= 'sp7881', f1= '(7881)Disabled')
    db.dgeneral.insert( f0= 'hd7882', f1= '(7882)Info')
    db.dgeneral.insert( f0= 'sp7883', f1= '(7883)Disabled')
    db.dgeneral.insert( f0= 'hd7884', f1= '(7884)Success')
    db.dgeneral.insert( f0= 'sp7885', f1= '(7885)Disabled')
    db.dgeneral.insert( f0= 'hd7886', f1= '(7886)Warning')
    db.dgeneral.insert( f0= 'sp7887', f1= '(7887)Disabled')
    db.dgeneral.insert( f0= 'hd7888', f1= '(7888)Danger')
    db.dgeneral.insert( f0= 'sp7889', f1= '(7889)Disabled')
    db.dgeneral.insert( f0= 'he7890', f1= '(7890)Black/White Nuances')
    db.dgeneral.insert( f0= 'hd7891', f1= '(7891)Black')
    db.dgeneral.insert( f0= 'sp7892', f1= '(7892)Disabled')
    db.dgeneral.insert( f0= 'hd7893', f1= '(7893)Gray Dark')
    db.dgeneral.insert( f0= 'sp7894', f1= '(7894)Disabled')
    db.dgeneral.insert( f0= 'hd7895', f1= '(7895)Gray')
    db.dgeneral.insert( f0= 'sp7896', f1= '(7896)Disabled')
    db.dgeneral.insert( f0= 'hd7897', f1= '(7897)Light')
    db.dgeneral.insert( f0= 'sp7898', f1= '(7898)Disabled')
    db.dgeneral.insert( f0= 'he7899', f1= '(7899)Colors')
    db.dgeneral.insert( f0= 'hd7900', f1= '(7900)Indigo')
    db.dgeneral.insert( f0= 'sp7901', f1= '(7901)Disabled')
    db.dgeneral.insert( f0= 'hd7902', f1= '(7902)Lightblue')
    db.dgeneral.insert( f0= 'sp7903', f1= '(7903)Disabled')
    db.dgeneral.insert( f0= 'hd7904', f1= '(7904)Navy')
    db.dgeneral.insert( f0= 'sp7905', f1= '(7905)Disabled')
    db.dgeneral.insert( f0= 'hd7906', f1= '(7906)Purple')
    db.dgeneral.insert( f0= 'sp7907', f1= '(7907)Disabled')
    db.dgeneral.insert( f0= 'hd7908', f1= '(7908)Fuchsia')
    db.dgeneral.insert( f0= 'sp7909', f1= '(7909)Disabled')
    db.dgeneral.insert( f0= 'hd7910', f1= '(7910)Pink')
    db.dgeneral.insert( f0= 'sp7911', f1= '(7911)Disabled')
    db.dgeneral.insert( f0= 'hd7912', f1= '(7912)Maroon')
    db.dgeneral.insert( f0= 'sp7913', f1= '(7913)Disabled')
    db.dgeneral.insert( f0= 'hd7914', f1= '(7914)Orange')
    db.dgeneral.insert( f0= 'sp7915', f1= '(7915)Disabled')
    db.dgeneral.insert( f0= 'hd7916', f1= '(7916)Lime')
    db.dgeneral.insert( f0= 'sp7917', f1= '(7917)Disabled')
    db.dgeneral.insert( f0= 'hd7918', f1= '(7918)Teal')
    db.dgeneral.insert( f0= 'sp7919', f1= '(7919)Disabled')
    db.dgeneral.insert( f0= 'hd7920', f1= '(7920)Olive')
    db.dgeneral.insert( f0= 'sp7921', f1= '(7921)Disabled')
    db.dgeneral.insert( f0= 'he7922', f1= '(7922)Alerts and Callouts')
    db.dgeneral.insert( f0= 'ix7923', f1= '(7923)Alert!')
    db.dgeneral.insert( f0= 'ix7924', f1= '(7924)Alert!')
    db.dgeneral.insert( f0= 'ix7925', f1= '(7925)Alert!')
    db.dgeneral.insert( f0= 'ix7926', f1= '(7926)Alert!')
    db.dgeneral.insert( f0= 'hh7927', f1= '(7927)I am a danger callout!')
    db.dgeneral.insert( f0= 'hh7928', f1= '(7928)I am an info callout!')
    db.dgeneral.insert( f0= 'pa7929', f1= '(7929)Follow the steps to continue to payment.')
    db.dgeneral.insert( f0= 'hh7930', f1= '(7930)I am a warning callout!')
    db.dgeneral.insert( f0= 'pa7931', f1= '(7931)This is a yellow callout.')
    db.dgeneral.insert( f0= 'hh7932', f1= '(7932)I am a success callout!')
    db.dgeneral.insert( f0= 'pa7933', f1= '(7933)This is a green callout.')
    db.dgeneral.insert( f0= 'he7934', f1= '(7934)Tabs in Cards')
    db.dgeneral.insert( f0= 'hc7935', f1= '(7935)Tabs')
    db.dgeneral.insert( f0= 'aa7936', f1= '(7936)Tab 1')
    db.dgeneral.insert( f0= 'aa7937', f1= '(7937)Tab 2')
    db.dgeneral.insert( f0= 'aa7938', f1= '(7938)Tab 3')
    db.dgeneral.insert( f0= 'aa7939', f1= '(7939)Action')
    db.dgeneral.insert( f0= 'aa7940', f1= '(7940)Another action')
    db.dgeneral.insert( f0= 'aa7941', f1= '(7941)Something else here')
    db.dgeneral.insert( f0= 'aa7942', f1= '(7942)Separated link')
    db.dgeneral.insert( f0= 'he7943', f1= '(7943)Progress Bars')
    db.dgeneral.insert( f0= 'hc7944', f1= '(7944)Progress Bars Different Sizes')
    db.dgeneral.insert( f0= 'sx7945', f1= '(7945)40% Complete (success)')
    db.dgeneral.insert( f0= 'sx7946', f1= '(7946)20% Complete')
    db.dgeneral.insert( f0= 'sx7947', f1= '(7947)60% Complete (warning)')
    db.dgeneral.insert( f0= 'sx7948', f1= '(7948)60% Complete (warning)')
    db.dgeneral.insert( f0= 'hc7949', f1= '(7949)Progress bars')
    db.dgeneral.insert( f0= 'sx7950', f1= '(7950)40% Complete (success)')
    db.dgeneral.insert( f0= 'sx7951', f1= '(7951)20% Complete')
    db.dgeneral.insert( f0= 'sx7952', f1= '(7952)60% Complete (warning)')
    db.dgeneral.insert( f0= 'sx7953', f1= '(7953)80% Complete')
    db.dgeneral.insert( f0= 'hc7954', f1= '(7954)Vertical Progress Bars Different Sizes')
    db.dgeneral.insert( f0= 'pf7955', f1= '(7955)By adding the class')
    db.dgeneral.insert( f0= 'pc7956', f1= '(7956)we achieve:')
    db.dgeneral.insert( f0= 'hc7957', f1= '(7957)Vertical Progress bars')
    db.dgeneral.insert( f0= 'pc7958', f1= '(7958)we achieve:')
    db.dgeneral.insert( f0= 'pf7959', f1= '(7959)By adding the class')
    db.dgeneral.insert( f0= 'he7960', f1= '(7960)Bootstrap Accordion & Carousel')
    db.dgeneral.insert( f0= 'hc7961', f1= '(7961)Collapsible Accordion')
    db.dgeneral.insert( f0= 'hc7962', f1= '(7962)Carousel')
    db.dgeneral.insert( f0= 'sx7963', f1= '(7963)Previous')
    db.dgeneral.insert( f0= 'sx7964', f1= '(7964)Next')
    db.dgeneral.insert( f0= 'he7965', f1= '(7965)Typography')
    db.dgeneral.insert( f0= 'hh7966', f1= '(7966)h1. Bootstrap heading')
    db.dgeneral.insert( f0= 'hh7967', f1= '(7967)h2. Bootstrap heading')
    db.dgeneral.insert( f0= 'hh7968', f1= '(7968)h3. Bootstrap heading')
    db.dgeneral.insert( f0= 'hh7969', f1= '(7969)h4. Bootstrap heading')
    db.dgeneral.insert( f0= 'hh7970', f1= '(7970)h5. Bootstrap heading')
    db.dgeneral.insert( f0= 'hh7971', f1= '(7971)h6. Bootstrap heading')
    db.dgeneral.insert( f0= 'pc7972', f1= '(7972)Lead to emphasize importance')
    db.dgeneral.insert( f0= 'pc7973', f1= '(7973)Text green to emphasize success')
    db.dgeneral.insert( f0= 'pc7974', f1= '(7974)Text aqua to emphasize info')
    db.dgeneral.insert( f0= 'pc7975', f1= '(7975)Text light blue to emphasize info (2)')
    db.dgeneral.insert( f0= 'pc7976', f1= '(7976)Text red to emphasize danger')
    db.dgeneral.insert( f0= 'pc7977', f1= '(7977)Text yellow to emphasize warning')
    db.dgeneral.insert( f0= 'pc7978', f1= '(7978)Text muted to emphasize general')
    db.dgeneral.insert( f0= 'pa7979', f1= '(7979)Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.')
    db.dgeneral.insert( f0= 'pa7980', f1= '(7980)Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.')
    db.dgeneral.insert( f0= 'la7981', f1= '(7981)Lorem ipsum dolor sit amet')
    db.dgeneral.insert( f0= 'la7982', f1= '(7982)Consectetur adipiscing elit')
    db.dgeneral.insert( f0= 'la7983', f1= '(7983)Integer molestie lorem at massa')
    db.dgeneral.insert( f0= 'la7984', f1= '(7984)Facilisis in pretium nisl aliquet')
    db.dgeneral.insert( f0= 'la7985', f1= '(7985)Phasellus iaculis neque')
    db.dgeneral.insert( f0= 'la7986', f1= '(7986)Purus sodales ultricies')
    db.dgeneral.insert( f0= 'la7987', f1= '(7987)Vestibulum laoreet porttitor sem')
    db.dgeneral.insert( f0= 'la7988', f1= '(7988)Ac tristique libero volutpat at')
    db.dgeneral.insert( f0= 'la7989', f1= '(7989)Faucibus porta lacus fringilla vel')
    db.dgeneral.insert( f0= 'la7990', f1= '(7990)Aenean sit amet erat nunc')
    db.dgeneral.insert( f0= 'la7991', f1= '(7991)Eget porttitor lorem')
    db.dgeneral.insert( f0= 'la7992', f1= '(7992)Lorem ipsum dolor sit amet')
    db.dgeneral.insert( f0= 'la7993', f1= '(7993)Consectetur adipiscing elit')
    db.dgeneral.insert( f0= 'la7994', f1= '(7994)Integer molestie lorem at massa')
    db.dgeneral.insert( f0= 'la7995', f1= '(7995)Facilisis in pretium nisl aliquet')
    db.dgeneral.insert( f0= 'la7996', f1= '(7996)Phasellus iaculis neque')
    db.dgeneral.insert( f0= 'la7997', f1= '(7997)Purus sodales ultricies')
    db.dgeneral.insert( f0= 'la7998', f1= '(7998)Vestibulum laoreet porttitor sem')
    db.dgeneral.insert( f0= 'la7999', f1= '(7999)Ac tristique libero volutpat at')
    db.dgeneral.insert( f0= 'la8000', f1= '(8000)Faucibus porta lacus fringilla vel')
    db.dgeneral.insert( f0= 'la8001', f1= '(8001)Aenean sit amet erat nunc')
    db.dgeneral.insert( f0= 'la8002', f1= '(8002)Eget porttitor lorem')
    db.dgeneral.insert( f0= 'la8003', f1= '(8003)Lorem ipsum dolor sit amet')
    db.dgeneral.insert( f0= 'la8004', f1= '(8004)Consectetur adipiscing elit')
    db.dgeneral.insert( f0= 'la8005', f1= '(8005)Integer molestie lorem at massa')
    db.dgeneral.insert( f0= 'la8006', f1= '(8006)Facilisis in pretium nisl aliquet')
    db.dgeneral.insert( f0= 'la8007', f1= '(8007)Phasellus iaculis neque')
    db.dgeneral.insert( f0= 'la8008', f1= '(8008)Purus sodales ultricies')
    db.dgeneral.insert( f0= 'la8009', f1= '(8009)Vestibulum laoreet porttitor sem')
    db.dgeneral.insert( f0= 'la8010', f1= '(8010)Ac tristique libero volutpat at')
    db.dgeneral.insert( f0= 'la8011', f1= '(8011)Faucibus porta lacus fringilla vel')
    db.dgeneral.insert( f0= 'la8012', f1= '(8012)Aenean sit amet erat nunc')
    db.dgeneral.insert( f0= 'la8013', f1= '(8013)Eget porttitor lorem')
    db.dgeneral.insert( f0= 'bb8014', f1= '(8014)Version')
    db.dgeneral.insert( f0= 'aa8015', f1= '(8015)AdminLTE.io')
    db.commit()
#
