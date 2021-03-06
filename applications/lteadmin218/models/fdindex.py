#
# table for controller: index
#

from gluon.contrib.populate import populate

db.define_table('dindex', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dindex.id ).count():
    db.dindex.insert( f0= 'bb4960', f1= '(4960)A')
    db.dindex.insert( f0= 'sx4961', f1= '(4961)LT')
    db.dindex.insert( f0= 'bb4962', f1= '(4962)Admin')
    db.dindex.insert( f0= 'sx4963', f1= '(4963)LTE')
    db.dindex.insert( f0= 'sx4964', f1= '(4964)Toggle navigation')
    db.dindex.insert( f0= 'sx4965', f1= '(4965)4')
    db.dindex.insert( f0= 'lb4966', f1= '(4966)You have 4 messages')
    db.dindex.insert( f0= 'ib4968', f1= '(4968)5 mins')
    db.dindex.insert( f0= 'pa4969', f1= '(4969)Why not buy a new awesome theme?')
    db.dindex.insert( f0= 'ib4971', f1= '(4971)2 hours')
    db.dindex.insert( f0= 'pa4972', f1= '(4972)Why not buy a new awesome theme?')
    db.dindex.insert( f0= 'ib4974', f1= '(4974)Today')
    db.dindex.insert( f0= 'pa4975', f1= '(4975)Why not buy a new awesome theme?')
    db.dindex.insert( f0= 'ib4977', f1= '(4977)Yesterday')
    db.dindex.insert( f0= 'pa4978', f1= '(4978)Why not buy a new awesome theme?')
    db.dindex.insert( f0= 'ib4980', f1= '(4980)2 days')
    db.dindex.insert( f0= 'pa4981', f1= '(4981)Why not buy a new awesome theme?')
    db.dindex.insert( f0= 'aa4982', f1= '(4982)See All Messages')
    db.dindex.insert( f0= 'lb4983', f1= '(4983)You have 10 notifications')
    db.dindex.insert( f0= 'aa4984', f1= '(4984)View all')
    db.dindex.insert( f0= 'sx4985', f1= '(4985)9')
    db.dindex.insert( f0= 'lb4986', f1= '(4986)You have 9 tasks')
    db.dindex.insert( f0= 'sx4987', f1= '(4987)20% Complete')
    db.dindex.insert( f0= 'sx4988', f1= '(4988)40% Complete')
    db.dindex.insert( f0= 'sx4989', f1= '(4989)60% Complete')
    db.dindex.insert( f0= 'sx4990', f1= '(4990)80% Complete')
    db.dindex.insert( f0= 'aa4991', f1= '(4991)View all tasks')
    db.dindex.insert( f0= 'sx4993', f1= '(4993)Alexander Pierce')
    db.dindex.insert( f0= 'ic4995', f1= '(4995)Member since Nov. 2012')
    db.dindex.insert( f0= 'aa4996', f1= '(4996)Followers')
    db.dindex.insert( f0= 'aa4997', f1= '(4997)Sales')
    db.dindex.insert( f0= 'aa4998', f1= '(4998)Friends')
    db.dindex.insert( f0= 'aa4999', f1= '(4999)Profile')
    db.dindex.insert( f0= 'aa5000', f1= '(5000)Sign out')
    db.dindex.insert( f0= 'pa5002', f1= '(5002)Alexander Pierce')
    db.dindex.insert( f0= 'ia5003', f1= '(5003)Online')
    db.dindex.insert( f0= 'pb5004', f1= '(5004)Search...')
    db.dindex.insert( f0= 'lb5005', f1= '(5005)MAIN NAVIGATION')
    db.dindex.insert( f0= 'sp5006', f1= '(5006)Dashboard')
    db.dindex.insert( f0= 'ia5008', f1= '(5008)Dashboard v1')
    db.dindex.insert( f0= 'ia5010', f1= '(5010)Dashboard v2')
    db.dindex.insert( f0= 'sp5011', f1= '(5011)Layout Options')
    db.dindex.insert( f0= 'sx5012', f1= '(5012)4')
    db.dindex.insert( f0= 'ia5014', f1= '(5014)Top Navigation')
    db.dindex.insert( f0= 'ia5016', f1= '(5016)Boxed')
    db.dindex.insert( f0= 'ia5018', f1= '(5018)Fixed')
    db.dindex.insert( f0= 'ia5020', f1= '(5020)Collapsed Sidebar')
    db.dindex.insert( f0= 'sp5022', f1= '(5022)Widgets')
    db.dindex.insert( f0= 'ic5023', f1= '(5023)new')
    db.dindex.insert( f0= 'sp5024', f1= '(5024)Charts')
    db.dindex.insert( f0= 'ia5026', f1= '(5026)ChartJS')
    db.dindex.insert( f0= 'ia5028', f1= '(5028)Morris')
    db.dindex.insert( f0= 'ia5030', f1= '(5030)Flot')
    db.dindex.insert( f0= 'ia5032', f1= '(5032)Inline charts')
    db.dindex.insert( f0= 'sp5033', f1= '(5033)UI Elements')
    db.dindex.insert( f0= 'ia5035', f1= '(5035)General')
    db.dindex.insert( f0= 'ia5037', f1= '(5037)Icons')
    db.dindex.insert( f0= 'ia5039', f1= '(5039)Buttons')
    db.dindex.insert( f0= 'ia5041', f1= '(5041)Sliders')
    db.dindex.insert( f0= 'ia5043', f1= '(5043)Timeline')
    db.dindex.insert( f0= 'ia5045', f1= '(5045)Modals')
    db.dindex.insert( f0= 'sp5046', f1= '(5046)Forms')
    db.dindex.insert( f0= 'ia5048', f1= '(5048)General Elements')
    db.dindex.insert( f0= 'ia5050', f1= '(5050)Advanced Elements')
    db.dindex.insert( f0= 'ia5052', f1= '(5052)Editors')
    db.dindex.insert( f0= 'sp5053', f1= '(5053)Tables')
    db.dindex.insert( f0= 'ia5055', f1= '(5055)Simple tables')
    db.dindex.insert( f0= 'ia5057', f1= '(5057)Data tables')
    db.dindex.insert( f0= 'sp5059', f1= '(5059)Calendar')
    db.dindex.insert( f0= 'ic5060', f1= '(5060)3')
    db.dindex.insert( f0= 'sp5062', f1= '(5062)Mailbox')
    db.dindex.insert( f0= 'ic5063', f1= '(5063)5')
    db.dindex.insert( f0= 'sp5064', f1= '(5064)Examples')
    db.dindex.insert( f0= 'ia5066', f1= '(5066)Invoice')
    db.dindex.insert( f0= 'ia5068', f1= '(5068)Profile')
    db.dindex.insert( f0= 'ia5070', f1= '(5070)Login')
    db.dindex.insert( f0= 'ia5072', f1= '(5072)Register')
    db.dindex.insert( f0= 'ia5074', f1= '(5074)Lockscreen')
    db.dindex.insert( f0= 'ia5076', f1= '(5076)404 Error')
    db.dindex.insert( f0= 'ia5078', f1= '(5078)500 Error')
    db.dindex.insert( f0= 'ia5080', f1= '(5080)Blank Page')
    db.dindex.insert( f0= 'ia5082', f1= '(5082)Pace Page')
    db.dindex.insert( f0= 'sp5083', f1= '(5083)Multilevel')
    db.dindex.insert( f0= 'ia5084', f1= '(5084)Level One')
    db.dindex.insert( f0= 'ia5085', f1= '(5085)Level Two')
    db.dindex.insert( f0= 'ia5086', f1= '(5086)Level Three')
    db.dindex.insert( f0= 'ia5087', f1= '(5087)Level Three')
    db.dindex.insert( f0= 'ia5088', f1= '(5088)Level One')
    db.dindex.insert( f0= 'sp5089', f1= '(5089)Documentation')
    db.dindex.insert( f0= 'lb5090', f1= '(5090)LABELS')
    db.dindex.insert( f0= 'sp5091', f1= '(5091)Important')
    db.dindex.insert( f0= 'sp5092', f1= '(5092)Warning')
    db.dindex.insert( f0= 'sp5093', f1= '(5093)Information')
    db.dindex.insert( f0= 'ic5094', f1= '(5094)Control panel')
    db.dindex.insert( f0= 'ia5095', f1= '(5095)Home')
    db.dindex.insert( f0= 'lb5096', f1= '(5096)Dashboard')
    db.dindex.insert( f0= 'pa5097', f1= '(5097)New Orders')
    db.dindex.insert( f0= 'pa5098', f1= '(5098)Bounce Rate')
    db.dindex.insert( f0= 'pa5099', f1= '(5099)User Registrations')
    db.dindex.insert( f0= 'pa5100', f1= '(5100)Unique Visitors')
    db.dindex.insert( f0= 'aa5101', f1= '(5101)Area')
    db.dindex.insert( f0= 'aa5102', f1= '(5102)Donut')
    db.dindex.insert( f0= 'hc5103', f1= '(5103)Chat')
    db.dindex.insert( f0= 'ib5105', f1= '(5105)2:15')
    db.dindex.insert( f0= 'hh5106', f1= '(5106)Attachments:')
    db.dindex.insert( f0= 'bu5107', f1= '(5107)Open')
    db.dindex.insert( f0= 'ib5109', f1= '(5109)5:15')
    db.dindex.insert( f0= 'ib5111', f1= '(5111)5:30')
    db.dindex.insert( f0= 'pb5112', f1= '(5112)Type message...')
    db.dindex.insert( f0= 'hc5113', f1= '(5113)To Do List')
    db.dindex.insert( f0= 'aa5114', f1= '(5114)&laquo;')
    db.dindex.insert( f0= 'aa5115', f1= '(5115)1')
    db.dindex.insert( f0= 'aa5116', f1= '(5116)2')
    db.dindex.insert( f0= 'aa5117', f1= '(5117)3')
    db.dindex.insert( f0= 'aa5118', f1= '(5118)&raquo;')
    db.dindex.insert( f0= 'sx5119', f1= '(5119)Design a nice theme')
    db.dindex.insert( f0= 'ib5120', f1= '(5120)2 mins')
    db.dindex.insert( f0= 'sx5121', f1= '(5121)Make the theme responsive')
    db.dindex.insert( f0= 'ib5122', f1= '(5122)4 hours')
    db.dindex.insert( f0= 'sx5123', f1= '(5123)Let theme shine like a star')
    db.dindex.insert( f0= 'ib5124', f1= '(5124)1 day')
    db.dindex.insert( f0= 'sx5125', f1= '(5125)Let theme shine like a star')
    db.dindex.insert( f0= 'ib5126', f1= '(5126)3 days')
    db.dindex.insert( f0= 'sx5127', f1= '(5127)Check your messages and notifications')
    db.dindex.insert( f0= 'ib5128', f1= '(5128)1 week')
    db.dindex.insert( f0= 'sx5129', f1= '(5129)Let theme shine like a star')
    db.dindex.insert( f0= 'ib5130', f1= '(5130)1 month')
    db.dindex.insert( f0= 'hc5131', f1= '(5131)Quick Email')
    db.dindex.insert( f0= 'pb5132', f1= '(5132)Email to:')
    db.dindex.insert( f0= 'pb5133', f1= '(5133)Subject')
    db.dindex.insert( f0= 'pb5134', f1= '(5134)Message')
    db.dindex.insert( f0= 'di5135', f1= '(5135)Visitors')
    db.dindex.insert( f0= 'di5136', f1= '(5136)Online')
    db.dindex.insert( f0= 'di5137', f1= '(5137)Exists')
    db.dindex.insert( f0= 'hc5138', f1= '(5138)Sales Graph')
    db.dindex.insert( f0= 'di5139', f1= '(5139)Mail-Orders')
    db.dindex.insert( f0= 'di5140', f1= '(5140)Online')
    db.dindex.insert( f0= 'di5141', f1= '(5141)In-Store')
    db.dindex.insert( f0= 'hc5142', f1= '(5142)Calendar')
    db.dindex.insert( f0= 'aa5143', f1= '(5143)Add new event')
    db.dindex.insert( f0= 'aa5144', f1= '(5144)Clear events')
    db.dindex.insert( f0= 'aa5145', f1= '(5145)View calendar')
    db.dindex.insert( f0= 'sx5146', f1= '(5146)Task #1')
    db.dindex.insert( f0= 'sx5147', f1= '(5147)Task #2')
    db.dindex.insert( f0= 'sx5148', f1= '(5148)Task #3')
    db.dindex.insert( f0= 'sx5149', f1= '(5149)Task #4')
    db.dindex.insert( f0= 'bb5150', f1= '(5150)Version')
    db.dindex.insert( f0= 'aa5151', f1= '(5151)AdminLTE')
    db.dindex.insert( f0= 'hc5152', f1= '(5152)Recent Activity')
    db.dindex.insert( f0= 'hd5153', f1= '(5153)Langdon s Birthday')
    db.dindex.insert( f0= 'pa5154', f1= '(5154)Will be 23 on April 24th')
    db.dindex.insert( f0= 'hd5155', f1= '(5155)Frodo Updated His Profile')
    db.dindex.insert( f0= 'pa5156', f1= '(5156)New phone +1(800)555-1234')
    db.dindex.insert( f0= 'hd5157', f1= '(5157)Nora Joined Mailing List')
    db.dindex.insert( f0= 'pa5158', f1= '(5158)nora@example.com')
    db.dindex.insert( f0= 'hd5159', f1= '(5159)Cron Job 254 Executed')
    db.dindex.insert( f0= 'pa5160', f1= '(5160)Execution time 5 seconds')
    db.dindex.insert( f0= 'hc5161', f1= '(5161)Tasks Progress')
    db.dindex.insert( f0= 'di5162', f1= '(5162)Stats Tab Content')
    db.dindex.insert( f0= 'hc5163', f1= '(5163)General Settings')
    db.dindex.insert( f0= 'hc5164', f1= '(5164)Chat Settings')
    db.commit()
#
