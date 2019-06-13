#
# table for controller: blank
#

from gluon.contrib.populate import populate

db.define_table('dblank', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dblank.id ).count():
    db.dblank.insert( f0= 'sx233', f1= '(233)LT')
    db.dblank.insert( f0= 'bb234', f1= '(234)Admin')
    db.dblank.insert( f0= 'sx235', f1= '(235)LTE')
    db.dblank.insert( f0= 'sx236', f1= '(236)Toggle navigation')
    db.dblank.insert( f0= 'lb237', f1= '(237)You have 4 messages')
    db.dblank.insert( f0= 'ib239', f1= '(239)5 mins')
    db.dblank.insert( f0= 'pa240', f1= '(240)Why not buy a new awesome theme?')
    db.dblank.insert( f0= 'aa241', f1= '(241)See All Messages')
    db.dblank.insert( f0= 'sx242', f1= '(242)10')
    db.dblank.insert( f0= 'lb243', f1= '(243)You have 10 notifications')
    db.dblank.insert( f0= 'aa244', f1= '(244)View all')
    db.dblank.insert( f0= 'lb245', f1= '(245)You have 9 tasks')
    db.dblank.insert( f0= 'ic246', f1= '(246)20%')
    db.dblank.insert( f0= 'sx247', f1= '(247)20% Complete')
    db.dblank.insert( f0= 'aa248', f1= '(248)View all tasks')
    db.dblank.insert( f0= 'sx250', f1= '(250)Alexander Pierce')
    db.dblank.insert( f0= 'ic252', f1= '(252)Member since Nov. 2012')
    db.dblank.insert( f0= 'aa253', f1= '(253)Followers')
    db.dblank.insert( f0= 'aa254', f1= '(254)Sales')
    db.dblank.insert( f0= 'aa255', f1= '(255)Friends')
    db.dblank.insert( f0= 'aa256', f1= '(256)Profile')
    db.dblank.insert( f0= 'aa257', f1= '(257)Sign out')
    db.dblank.insert( f0= 'pa259', f1= '(259)Alexander Pierce')
    db.dblank.insert( f0= 'ia260', f1= '(260)Online')
    db.dblank.insert( f0= 'pb261', f1= '(261)Search...')
    db.dblank.insert( f0= 'lb262', f1= '(262)MAIN NAVIGATION')
    db.dblank.insert( f0= 'sp263', f1= '(263)Dashboard')
    db.dblank.insert( f0= 'ia265', f1= '(265)Dashboard v1')
    db.dblank.insert( f0= 'ia267', f1= '(267)Dashboard v2')
    db.dblank.insert( f0= 'sp268', f1= '(268)Layout Options')
    db.dblank.insert( f0= 'ia270', f1= '(270)Top Navigation')
    db.dblank.insert( f0= 'ia272', f1= '(272)Boxed')
    db.dblank.insert( f0= 'ia274', f1= '(274)Fixed')
    db.dblank.insert( f0= 'ia276', f1= '(276)Collapsed Sidebar')
    db.dblank.insert( f0= 'sp278', f1= '(278)Widgets')
    db.dblank.insert( f0= 'ic279', f1= '(279)Hot')
    db.dblank.insert( f0= 'sp280', f1= '(280)Charts')
    db.dblank.insert( f0= 'ia282', f1= '(282)ChartJS')
    db.dblank.insert( f0= 'ia284', f1= '(284)Morris')
    db.dblank.insert( f0= 'ia286', f1= '(286)Flot')
    db.dblank.insert( f0= 'ia288', f1= '(288)Inline charts')
    db.dblank.insert( f0= 'sp289', f1= '(289)UI Elements')
    db.dblank.insert( f0= 'ia291', f1= '(291)General')
    db.dblank.insert( f0= 'ia293', f1= '(293)Icons')
    db.dblank.insert( f0= 'ia295', f1= '(295)Buttons')
    db.dblank.insert( f0= 'ia297', f1= '(297)Sliders')
    db.dblank.insert( f0= 'ia299', f1= '(299)Timeline')
    db.dblank.insert( f0= 'ia301', f1= '(301)Modals')
    db.dblank.insert( f0= 'sp302', f1= '(302)Forms')
    db.dblank.insert( f0= 'ia304', f1= '(304)General Elements')
    db.dblank.insert( f0= 'ia306', f1= '(306)Advanced Elements')
    db.dblank.insert( f0= 'ia308', f1= '(308)Editors')
    db.dblank.insert( f0= 'sp309', f1= '(309)Tables')
    db.dblank.insert( f0= 'ia311', f1= '(311)Simple tables')
    db.dblank.insert( f0= 'ia313', f1= '(313)Data tables')
    db.dblank.insert( f0= 'sp315', f1= '(315)Calendar')
    db.dblank.insert( f0= 'ic316', f1= '(316)17')
    db.dblank.insert( f0= 'sp318', f1= '(318)Mailbox')
    db.dblank.insert( f0= 'ic319', f1= '(319)12')
    db.dblank.insert( f0= 'ic320', f1= '(320)16')
    db.dblank.insert( f0= 'sp321', f1= '(321)Examples')
    db.dblank.insert( f0= 'ia323', f1= '(323)Invoice')
    db.dblank.insert( f0= 'ia325', f1= '(325)Profile')
    db.dblank.insert( f0= 'ia327', f1= '(327)Login')
    db.dblank.insert( f0= 'ia329', f1= '(329)Register')
    db.dblank.insert( f0= 'ia331', f1= '(331)Lockscreen')
    db.dblank.insert( f0= 'ia333', f1= '(333)404 Error')
    db.dblank.insert( f0= 'ia335', f1= '(335)500 Error')
    db.dblank.insert( f0= 'ia337', f1= '(337)Blank Page')
    db.dblank.insert( f0= 'ia339', f1= '(339)Pace Page')
    db.dblank.insert( f0= 'sp340', f1= '(340)Multilevel')
    db.dblank.insert( f0= 'ia341', f1= '(341)Level One')
    db.dblank.insert( f0= 'ia342', f1= '(342)Level Two')
    db.dblank.insert( f0= 'ia343', f1= '(343)Level Three')
    db.dblank.insert( f0= 'ia344', f1= '(344)Level Three')
    db.dblank.insert( f0= 'ia345', f1= '(345)Level One')
    db.dblank.insert( f0= 'sp346', f1= '(346)Documentation')
    db.dblank.insert( f0= 'lb347', f1= '(347)LABELS')
    db.dblank.insert( f0= 'sp348', f1= '(348)Important')
    db.dblank.insert( f0= 'sp349', f1= '(349)Warning')
    db.dblank.insert( f0= 'sp350', f1= '(350)Information')
    db.dblank.insert( f0= 'ic351', f1= '(351)it all starts here')
    db.dblank.insert( f0= 'ia352', f1= '(352)Home')
    db.dblank.insert( f0= 'aa353', f1= '(353)Examples')
    db.dblank.insert( f0= 'lb354', f1= '(354)Blank page')
    db.dblank.insert( f0= 'hc355', f1= '(355)Title')
    db.dblank.insert( f0= 'bb356', f1= '(356)Version')
    db.dblank.insert( f0= 'hc358', f1= '(358)Recent Activity')
    db.dblank.insert( f0= 'hd359', f1= '(359)Langdon s Birthday')
    db.dblank.insert( f0= 'pa360', f1= '(360)Will be 23 on April 24th')
    db.dblank.insert( f0= 'hd361', f1= '(361)Frodo Updated His Profile')
    db.dblank.insert( f0= 'pa362', f1= '(362)New phone +1(800)555-1234')
    db.dblank.insert( f0= 'hd363', f1= '(363)Nora Joined Mailing List')
    db.dblank.insert( f0= 'pa364', f1= '(364)nora@example.com')
    db.dblank.insert( f0= 'hd365', f1= '(365)Cron Job 254 Executed')
    db.dblank.insert( f0= 'pa366', f1= '(366)Execution time 5 seconds')
    db.dblank.insert( f0= 'hc367', f1= '(367)Tasks Progress')
    db.dblank.insert( f0= 'sx368', f1= '(368)70%')
    db.dblank.insert( f0= 'sx369', f1= '(369)95%')
    db.dblank.insert( f0= 'sx370', f1= '(370)50%')
    db.dblank.insert( f0= 'sx371', f1= '(371)68%')
    db.dblank.insert( f0= 'di372', f1= '(372)Stats Tab Content')
    db.dblank.insert( f0= 'hc373', f1= '(373)General Settings')
    db.dblank.insert( f0= 'hc374', f1= '(374)Chat Settings')
    db.commit()
#
