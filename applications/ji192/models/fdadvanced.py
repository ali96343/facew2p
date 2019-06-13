#
# table for controller: advanced
#

from gluon.contrib.populate import populate

db.define_table('dadvanced', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dadvanced.id ).count():
    db.dadvanced.insert( f0= 'sx396', f1= '(396)LT')
    db.dadvanced.insert( f0= 'bb397', f1= '(397)Admin')
    db.dadvanced.insert( f0= 'sx398', f1= '(398)LTE')
    db.dadvanced.insert( f0= 'sx399', f1= '(399)Toggle navigation')
    db.dadvanced.insert( f0= 'lb400', f1= '(400)You have 4 messages')
    db.dadvanced.insert( f0= 'ib402', f1= '(402)5 mins')
    db.dadvanced.insert( f0= 'pa403', f1= '(403)Why not buy a new awesome theme?')
    db.dadvanced.insert( f0= 'ib405', f1= '(405)2 hours')
    db.dadvanced.insert( f0= 'pa406', f1= '(406)Why not buy a new awesome theme?')
    db.dadvanced.insert( f0= 'ib408', f1= '(408)Today')
    db.dadvanced.insert( f0= 'pa409', f1= '(409)Why not buy a new awesome theme?')
    db.dadvanced.insert( f0= 'ib411', f1= '(411)Yesterday')
    db.dadvanced.insert( f0= 'pa412', f1= '(412)Why not buy a new awesome theme?')
    db.dadvanced.insert( f0= 'ib414', f1= '(414)2 days')
    db.dadvanced.insert( f0= 'pa415', f1= '(415)Why not buy a new awesome theme?')
    db.dadvanced.insert( f0= 'aa416', f1= '(416)See All Messages')
    db.dadvanced.insert( f0= 'sx417', f1= '(417)10')
    db.dadvanced.insert( f0= 'lb418', f1= '(418)You have 10 notifications')
    db.dadvanced.insert( f0= 'aa419', f1= '(419)View all')
    db.dadvanced.insert( f0= 'lb420', f1= '(420)You have 9 tasks')
    db.dadvanced.insert( f0= 'ic421', f1= '(421)20%')
    db.dadvanced.insert( f0= 'sx422', f1= '(422)20% Complete')
    db.dadvanced.insert( f0= 'ic423', f1= '(423)40%')
    db.dadvanced.insert( f0= 'sx424', f1= '(424)40% Complete')
    db.dadvanced.insert( f0= 'ic425', f1= '(425)60%')
    db.dadvanced.insert( f0= 'sx426', f1= '(426)60% Complete')
    db.dadvanced.insert( f0= 'ic427', f1= '(427)80%')
    db.dadvanced.insert( f0= 'sx428', f1= '(428)80% Complete')
    db.dadvanced.insert( f0= 'aa429', f1= '(429)View all tasks')
    db.dadvanced.insert( f0= 'sx431', f1= '(431)Alexander Pierce')
    db.dadvanced.insert( f0= 'ic433', f1= '(433)Member since Nov. 2012')
    db.dadvanced.insert( f0= 'aa434', f1= '(434)Followers')
    db.dadvanced.insert( f0= 'aa435', f1= '(435)Sales')
    db.dadvanced.insert( f0= 'aa436', f1= '(436)Friends')
    db.dadvanced.insert( f0= 'aa437', f1= '(437)Profile')
    db.dadvanced.insert( f0= 'aa438', f1= '(438)Sign out')
    db.dadvanced.insert( f0= 'pa440', f1= '(440)Alexander Pierce')
    db.dadvanced.insert( f0= 'ia441', f1= '(441)Online')
    db.dadvanced.insert( f0= 'pb442', f1= '(442)Search...')
    db.dadvanced.insert( f0= 'lb443', f1= '(443)MAIN NAVIGATION')
    db.dadvanced.insert( f0= 'sp444', f1= '(444)Dashboard')
    db.dadvanced.insert( f0= 'ia446', f1= '(446)Dashboard v1')
    db.dadvanced.insert( f0= 'ia448', f1= '(448)Dashboard v2')
    db.dadvanced.insert( f0= 'sp449', f1= '(449)Layout Options')
    db.dadvanced.insert( f0= 'ia451', f1= '(451)Top Navigation')
    db.dadvanced.insert( f0= 'ia453', f1= '(453)Boxed')
    db.dadvanced.insert( f0= 'ia455', f1= '(455)Fixed')
    db.dadvanced.insert( f0= 'ia457', f1= '(457)Collapsed Sidebar')
    db.dadvanced.insert( f0= 'sp459', f1= '(459)Widgets')
    db.dadvanced.insert( f0= 'ic460', f1= '(460)new')
    db.dadvanced.insert( f0= 'sp461', f1= '(461)Charts')
    db.dadvanced.insert( f0= 'ia463', f1= '(463)ChartJS')
    db.dadvanced.insert( f0= 'ia465', f1= '(465)Morris')
    db.dadvanced.insert( f0= 'ia467', f1= '(467)Flot')
    db.dadvanced.insert( f0= 'ia469', f1= '(469)Inline charts')
    db.dadvanced.insert( f0= 'sp470', f1= '(470)UI Elements')
    db.dadvanced.insert( f0= 'ia472', f1= '(472)General')
    db.dadvanced.insert( f0= 'ia474', f1= '(474)Icons')
    db.dadvanced.insert( f0= 'ia476', f1= '(476)Buttons')
    db.dadvanced.insert( f0= 'ia478', f1= '(478)Sliders')
    db.dadvanced.insert( f0= 'ia480', f1= '(480)Timeline')
    db.dadvanced.insert( f0= 'ia482', f1= '(482)Modals')
    db.dadvanced.insert( f0= 'sp483', f1= '(483)Forms')
    db.dadvanced.insert( f0= 'ia485', f1= '(485)General Elements')
    db.dadvanced.insert( f0= 'ia487', f1= '(487)Advanced Elements')
    db.dadvanced.insert( f0= 'ia489', f1= '(489)Editors')
    db.dadvanced.insert( f0= 'sp490', f1= '(490)Tables')
    db.dadvanced.insert( f0= 'ia492', f1= '(492)Simple tables')
    db.dadvanced.insert( f0= 'ia494', f1= '(494)Data tables')
    db.dadvanced.insert( f0= 'sp496', f1= '(496)Calendar')
    db.dadvanced.insert( f0= 'ic497', f1= '(497)17')
    db.dadvanced.insert( f0= 'sp499', f1= '(499)Mailbox')
    db.dadvanced.insert( f0= 'ic500', f1= '(500)12')
    db.dadvanced.insert( f0= 'ic501', f1= '(501)16')
    db.dadvanced.insert( f0= 'sp502', f1= '(502)Examples')
    db.dadvanced.insert( f0= 'ia504', f1= '(504)Invoice')
    db.dadvanced.insert( f0= 'ia506', f1= '(506)Profile')
    db.dadvanced.insert( f0= 'ia508', f1= '(508)Login')
    db.dadvanced.insert( f0= 'ia510', f1= '(510)Register')
    db.dadvanced.insert( f0= 'ia512', f1= '(512)Lockscreen')
    db.dadvanced.insert( f0= 'ia514', f1= '(514)404 Error')
    db.dadvanced.insert( f0= 'ia516', f1= '(516)500 Error')
    db.dadvanced.insert( f0= 'ia518', f1= '(518)Blank Page')
    db.dadvanced.insert( f0= 'ia520', f1= '(520)Pace Page')
    db.dadvanced.insert( f0= 'sp521', f1= '(521)Multilevel')
    db.dadvanced.insert( f0= 'ia522', f1= '(522)Level One')
    db.dadvanced.insert( f0= 'ia523', f1= '(523)Level Two')
    db.dadvanced.insert( f0= 'ia524', f1= '(524)Level Three')
    db.dadvanced.insert( f0= 'ia525', f1= '(525)Level Three')
    db.dadvanced.insert( f0= 'ia526', f1= '(526)Level One')
    db.dadvanced.insert( f0= 'sp527', f1= '(527)Documentation')
    db.dadvanced.insert( f0= 'lb528', f1= '(528)LABELS')
    db.dadvanced.insert( f0= 'sp529', f1= '(529)Important')
    db.dadvanced.insert( f0= 'sp530', f1= '(530)Warning')
    db.dadvanced.insert( f0= 'sp531', f1= '(531)Information')
    db.dadvanced.insert( f0= 'ic532', f1= '(532)Preview')
    db.dadvanced.insert( f0= 'ia533', f1= '(533)Home')
    db.dadvanced.insert( f0= 'aa534', f1= '(534)Forms')
    db.dadvanced.insert( f0= 'lb535', f1= '(535)Advanced Elements')
    db.dadvanced.insert( f0= 'hc536', f1= '(536)Select2')
    db.dadvanced.insert( f0= 'pb537', f1= '(537)Select a State')
    db.dadvanced.insert( f0= 'aa538', f1= '(538)Select2 documentation')
    db.dadvanced.insert( f0= 'hc539', f1= '(539)Input masks')
    db.dadvanced.insert( f0= 'hc542', f1= '(542)Color & Time Picker')
    db.dadvanced.insert( f0= 'hc543', f1= '(543)Date picker')
    db.dadvanced.insert( f0= 'aa544', f1= '(544)Documentation')
    db.dadvanced.insert( f0= 'bb545', f1= '(545)Version')
    db.dadvanced.insert( f0= 'hc547', f1= '(547)Recent Activity')
    db.dadvanced.insert( f0= 'hd548', f1= '(548)Langdon s Birthday')
    db.dadvanced.insert( f0= 'pa549', f1= '(549)Will be 23 on April 24th')
    db.dadvanced.insert( f0= 'hd550', f1= '(550)Frodo Updated His Profile')
    db.dadvanced.insert( f0= 'pa551', f1= '(551)New phone +1(800)555-1234')
    db.dadvanced.insert( f0= 'hd552', f1= '(552)Nora Joined Mailing List')
    db.dadvanced.insert( f0= 'pa553', f1= '(553)nora@example.com')
    db.dadvanced.insert( f0= 'hd554', f1= '(554)Cron Job 254 Executed')
    db.dadvanced.insert( f0= 'pa555', f1= '(555)Execution time 5 seconds')
    db.dadvanced.insert( f0= 'hc556', f1= '(556)Tasks Progress')
    db.dadvanced.insert( f0= 'sx557', f1= '(557)70%')
    db.dadvanced.insert( f0= 'sx558', f1= '(558)95%')
    db.dadvanced.insert( f0= 'sx559', f1= '(559)50%')
    db.dadvanced.insert( f0= 'sx560', f1= '(560)68%')
    db.dadvanced.insert( f0= 'di561', f1= '(561)Stats Tab Content')
    db.dadvanced.insert( f0= 'hc562', f1= '(562)General Settings')
    db.dadvanced.insert( f0= 'hc563', f1= '(563)Chat Settings')
    db.commit()
#
