#
# table for controller: readIImail
#

from gluon.contrib.populate import populate

db.define_table('dread0mail', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dread0mail.id ).count():
    db.dread0mail.insert( f0= 'aa499', f1= '(499)Home')
    db.dread0mail.insert( f0= 'aa500', f1= '(500)Contact')
    db.dread0mail.insert( f0= 'pb501', f1= '(501)Search')
    db.dread0mail.insert( f0= 'sx502', f1= '(502)3')
    db.dread0mail.insert( f0= 'pc504', f1= '(504)Call me whenever you can...')
    db.dread0mail.insert( f0= 'pc505', f1= '(505)4 Hours Ago')
    db.dread0mail.insert( f0= 'pc507', f1= '(507)I got your message bro')
    db.dread0mail.insert( f0= 'pc508', f1= '(508)4 Hours Ago')
    db.dread0mail.insert( f0= 'pc510', f1= '(510)The subject goes here')
    db.dread0mail.insert( f0= 'pc511', f1= '(511)4 Hours Ago')
    db.dread0mail.insert( f0= 'aa512', f1= '(512)See All Messages')
    db.dread0mail.insert( f0= 'sx513', f1= '(513)15 Notifications')
    db.dread0mail.insert( f0= 'sx514', f1= '(514)3 mins')
    db.dread0mail.insert( f0= 'sx515', f1= '(515)12 hours')
    db.dread0mail.insert( f0= 'sx516', f1= '(516)2 days')
    db.dread0mail.insert( f0= 'aa517', f1= '(517)See All Notifications')
    db.dread0mail.insert( f0= 'sx520', f1= '(520)AdminLTE 3')
    db.dread0mail.insert( f0= 'aa522', f1= '(522)Alexander Pierce')
    db.dread0mail.insert( f0= 'pa524', f1= '(524)Dashboard v1')
    db.dread0mail.insert( f0= 'pa526', f1= '(526)Dashboard v2')
    db.dread0mail.insert( f0= 'pa528', f1= '(528)Dashboard v3')
    db.dread0mail.insert( f0= 'sx530', f1= '(530)New')
    db.dread0mail.insert( f0= 'sx531', f1= '(531)6')
    db.dread0mail.insert( f0= 'pa533', f1= '(533)Top Navigation')
    db.dread0mail.insert( f0= 'pa535', f1= '(535)Boxed')
    db.dread0mail.insert( f0= 'pa537', f1= '(537)Fixed Sidebar')
    db.dread0mail.insert( f0= 'pa539', f1= '(539)Fixed Navbar')
    db.dread0mail.insert( f0= 'pa541', f1= '(541)Fixed Footer')
    db.dread0mail.insert( f0= 'pa543', f1= '(543)Collapsed Sidebar')
    db.dread0mail.insert( f0= 'pa545', f1= '(545)ChartJS')
    db.dread0mail.insert( f0= 'pa547', f1= '(547)Flot')
    db.dread0mail.insert( f0= 'pa549', f1= '(549)Inline')
    db.dread0mail.insert( f0= 'pa551', f1= '(551)General')
    db.dread0mail.insert( f0= 'pa553', f1= '(553)Icons')
    db.dread0mail.insert( f0= 'pa555', f1= '(555)Buttons')
    db.dread0mail.insert( f0= 'pa557', f1= '(557)Sliders')
    db.dread0mail.insert( f0= 'pa559', f1= '(559)Modals & Alerts')
    db.dread0mail.insert( f0= 'pa561', f1= '(561)Navbar & Tabs')
    db.dread0mail.insert( f0= 'pa563', f1= '(563)Timeline')
    db.dread0mail.insert( f0= 'pa565', f1= '(565)Ribbons')
    db.dread0mail.insert( f0= 'pa567', f1= '(567)General Elements')
    db.dread0mail.insert( f0= 'pa569', f1= '(569)Advanced Elements')
    db.dread0mail.insert( f0= 'pa571', f1= '(571)Editors')
    db.dread0mail.insert( f0= 'pa573', f1= '(573)Simple Tables')
    db.dread0mail.insert( f0= 'pa575', f1= '(575)DataTables')
    db.dread0mail.insert( f0= 'pa577', f1= '(577)jsGrid')
    db.dread0mail.insert( f0= 'lb578', f1= '(578)EXAMPLES')
    db.dread0mail.insert( f0= 'sx580', f1= '(580)2')
    db.dread0mail.insert( f0= 'pa582', f1= '(582)Inbox')
    db.dread0mail.insert( f0= 'pa584', f1= '(584)Compose')
    db.dread0mail.insert( f0= 'pa586', f1= '(586)Read')
    db.dread0mail.insert( f0= 'pa588', f1= '(588)Invoice')
    db.dread0mail.insert( f0= 'pa590', f1= '(590)Profile')
    db.dread0mail.insert( f0= 'pa592', f1= '(592)E-commerce')
    db.dread0mail.insert( f0= 'pa594', f1= '(594)Projects')
    db.dread0mail.insert( f0= 'pa596', f1= '(596)Project Add')
    db.dread0mail.insert( f0= 'pa598', f1= '(598)Project Edit')
    db.dread0mail.insert( f0= 'pa600', f1= '(600)Project Detail')
    db.dread0mail.insert( f0= 'pa602', f1= '(602)Contacts')
    db.dread0mail.insert( f0= 'pa604', f1= '(604)Login')
    db.dread0mail.insert( f0= 'pa606', f1= '(606)Register')
    db.dread0mail.insert( f0= 'pa608', f1= '(608)Forgot Password')
    db.dread0mail.insert( f0= 'pa610', f1= '(610)Recover Password')
    db.dread0mail.insert( f0= 'pa612', f1= '(612)Lockscreen')
    db.dread0mail.insert( f0= 'pa614', f1= '(614)Legacy User Menu')
    db.dread0mail.insert( f0= 'pa616', f1= '(616)Language Menu')
    db.dread0mail.insert( f0= 'pa618', f1= '(618)Error 404')
    db.dread0mail.insert( f0= 'pa620', f1= '(620)Error 500')
    db.dread0mail.insert( f0= 'pa622', f1= '(622)Pace')
    db.dread0mail.insert( f0= 'pa624', f1= '(624)Blank Page')
    db.dread0mail.insert( f0= 'pa626', f1= '(626)Starter Page')
    db.dread0mail.insert( f0= 'lb627', f1= '(627)MISCELLANEOUS')
    db.dread0mail.insert( f0= 'pa628', f1= '(628)Documentation')
    db.dread0mail.insert( f0= 'lb629', f1= '(629)MULTI LEVEL EXAMPLE')
    db.dread0mail.insert( f0= 'pa630', f1= '(630)Level 1')
    db.dread0mail.insert( f0= 'pa631', f1= '(631)Level 2')
    db.dread0mail.insert( f0= 'pa632', f1= '(632)Level 3')
    db.dread0mail.insert( f0= 'pa633', f1= '(633)Level 3')
    db.dread0mail.insert( f0= 'pa634', f1= '(634)Level 3')
    db.dread0mail.insert( f0= 'pa635', f1= '(635)Level 2')
    db.dread0mail.insert( f0= 'pa636', f1= '(636)Level 1')
    db.dread0mail.insert( f0= 'lb637', f1= '(637)LABELS')
    db.dread0mail.insert( f0= 'pc638', f1= '(638)Important')
    db.dread0mail.insert( f0= 'pa639', f1= '(639)Warning')
    db.dread0mail.insert( f0= 'pa640', f1= '(640)Informational')
    db.dread0mail.insert( f0= 'hh641', f1= '(641)Compose')
    db.dread0mail.insert( f0= 'aa642', f1= '(642)Home')
    db.dread0mail.insert( f0= 'lb643', f1= '(643)Compose')
    db.dread0mail.insert( f0= 'aa645', f1= '(645)Back to Inbox')
    db.dread0mail.insert( f0= 'hc646', f1= '(646)Folders')
    db.dread0mail.insert( f0= 'hc647', f1= '(647)Labels')
    db.dread0mail.insert( f0= 'ia648', f1= '(648)Important')
    db.dread0mail.insert( f0= 'ia649', f1= '(649)Promotions')
    db.dread0mail.insert( f0= 'ia650', f1= '(650)Social')
    db.dread0mail.insert( f0= 'hc651', f1= '(651)Read Mail')
    db.dread0mail.insert( f0= 'hh652', f1= '(652)Message Subject Is Placed Here')
    db.dread0mail.insert( f0= 'ma653', f1= '(653)support@adminlte.io')
    db.dread0mail.insert( f0= 'sx654', f1= '(654)15 Feb. 2015 11:03 PM')
    db.dread0mail.insert( f0= 'pa655', f1= '(655)Hello John,')
    db.dread0mail.insert( f0= 'pc656', f1= '(656)Jane')
    db.dread0mail.insert( f0= 'pf657', f1= '(657)Thanks,')
    db.dread0mail.insert( f0= 'ia658', f1= '(658)Sep2014-report.pdf')
    db.dread0mail.insert( f0= 'sp659', f1= '(659)1,245 KB')
    db.dread0mail.insert( f0= 'ia660', f1= '(660)App Description.docx')
    db.dread0mail.insert( f0= 'sp661', f1= '(661)1,245 KB')
    db.dread0mail.insert( f0= 'ia663', f1= '(663)photo1.png')
    db.dread0mail.insert( f0= 'sp664', f1= '(664)2.67 MB')
    db.dread0mail.insert( f0= 'ia666', f1= '(666)photo2.png')
    db.dread0mail.insert( f0= 'sp667', f1= '(667)1.9 MB')
    db.dread0mail.insert( f0= 'bb668', f1= '(668)Version')
    db.dread0mail.insert( f0= 'aa669', f1= '(669)AdminLTE.io')
    db.commit()
#
