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
    db.dflot.insert( f0= 'bb5967', f1= '(5967)A')
    db.dflot.insert( f0= 'sx5968', f1= '(5968)LT')
    db.dflot.insert( f0= 'bb5969', f1= '(5969)Admin')
    db.dflot.insert( f0= 'sx5970', f1= '(5970)LTE')
    db.dflot.insert( f0= 'sx5971', f1= '(5971)Toggle navigation')
    db.dflot.insert( f0= 'sx5972', f1= '(5972)4')
    db.dflot.insert( f0= 'lb5973', f1= '(5973)You have 4 messages')
    db.dflot.insert( f0= 'ib5975', f1= '(5975)5 mins')
    db.dflot.insert( f0= 'pa5976', f1= '(5976)Why not buy a new awesome theme?')
    db.dflot.insert( f0= 'ib5978', f1= '(5978)2 hours')
    db.dflot.insert( f0= 'pa5979', f1= '(5979)Why not buy a new awesome theme?')
    db.dflot.insert( f0= 'ib5981', f1= '(5981)Today')
    db.dflot.insert( f0= 'pa5982', f1= '(5982)Why not buy a new awesome theme?')
    db.dflot.insert( f0= 'ib5984', f1= '(5984)Yesterday')
    db.dflot.insert( f0= 'pa5985', f1= '(5985)Why not buy a new awesome theme?')
    db.dflot.insert( f0= 'ib5987', f1= '(5987)2 days')
    db.dflot.insert( f0= 'pa5988', f1= '(5988)Why not buy a new awesome theme?')
    db.dflot.insert( f0= 'aa5989', f1= '(5989)See All Messages')
    db.dflot.insert( f0= 'lb5990', f1= '(5990)You have 10 notifications')
    db.dflot.insert( f0= 'aa5991', f1= '(5991)View all')
    db.dflot.insert( f0= 'sx5992', f1= '(5992)9')
    db.dflot.insert( f0= 'lb5993', f1= '(5993)You have 9 tasks')
    db.dflot.insert( f0= 'sx5994', f1= '(5994)20% Complete')
    db.dflot.insert( f0= 'sx5995', f1= '(5995)40% Complete')
    db.dflot.insert( f0= 'sx5996', f1= '(5996)60% Complete')
    db.dflot.insert( f0= 'sx5997', f1= '(5997)80% Complete')
    db.dflot.insert( f0= 'aa5998', f1= '(5998)View all tasks')
    db.dflot.insert( f0= 'sx6000', f1= '(6000)Alexander Pierce')
    db.dflot.insert( f0= 'ic6002', f1= '(6002)Member since Nov. 2012')
    db.dflot.insert( f0= 'aa6003', f1= '(6003)Followers')
    db.dflot.insert( f0= 'aa6004', f1= '(6004)Sales')
    db.dflot.insert( f0= 'aa6005', f1= '(6005)Friends')
    db.dflot.insert( f0= 'aa6006', f1= '(6006)Profile')
    db.dflot.insert( f0= 'aa6007', f1= '(6007)Sign out')
    db.dflot.insert( f0= 'pa6009', f1= '(6009)Alexander Pierce')
    db.dflot.insert( f0= 'ia6010', f1= '(6010)Online')
    db.dflot.insert( f0= 'pb6011', f1= '(6011)Search...')
    db.dflot.insert( f0= 'lb6012', f1= '(6012)MAIN NAVIGATION')
    db.dflot.insert( f0= 'sp6013', f1= '(6013)Dashboard')
    db.dflot.insert( f0= 'ia6015', f1= '(6015)Dashboard v1')
    db.dflot.insert( f0= 'ia6017', f1= '(6017)Dashboard v2')
    db.dflot.insert( f0= 'sp6018', f1= '(6018)Layout Options')
    db.dflot.insert( f0= 'sx6019', f1= '(6019)4')
    db.dflot.insert( f0= 'ia6021', f1= '(6021)Top Navigation')
    db.dflot.insert( f0= 'ia6023', f1= '(6023)Boxed')
    db.dflot.insert( f0= 'ia6025', f1= '(6025)Fixed')
    db.dflot.insert( f0= 'ia6027', f1= '(6027)Collapsed Sidebar')
    db.dflot.insert( f0= 'sp6029', f1= '(6029)Widgets')
    db.dflot.insert( f0= 'ic6030', f1= '(6030)new')
    db.dflot.insert( f0= 'sp6031', f1= '(6031)Charts')
    db.dflot.insert( f0= 'ia6033', f1= '(6033)ChartJS')
    db.dflot.insert( f0= 'ia6035', f1= '(6035)Morris')
    db.dflot.insert( f0= 'ia6037', f1= '(6037)Flot')
    db.dflot.insert( f0= 'ia6039', f1= '(6039)Inline charts')
    db.dflot.insert( f0= 'sp6040', f1= '(6040)UI Elements')
    db.dflot.insert( f0= 'ia6042', f1= '(6042)General')
    db.dflot.insert( f0= 'ia6044', f1= '(6044)Icons')
    db.dflot.insert( f0= 'ia6046', f1= '(6046)Buttons')
    db.dflot.insert( f0= 'ia6048', f1= '(6048)Sliders')
    db.dflot.insert( f0= 'ia6050', f1= '(6050)Timeline')
    db.dflot.insert( f0= 'ia6052', f1= '(6052)Modals')
    db.dflot.insert( f0= 'sp6053', f1= '(6053)Forms')
    db.dflot.insert( f0= 'ia6055', f1= '(6055)General Elements')
    db.dflot.insert( f0= 'ia6057', f1= '(6057)Advanced Elements')
    db.dflot.insert( f0= 'ia6059', f1= '(6059)Editors')
    db.dflot.insert( f0= 'sp6060', f1= '(6060)Tables')
    db.dflot.insert( f0= 'ia6062', f1= '(6062)Simple tables')
    db.dflot.insert( f0= 'ia6064', f1= '(6064)Data tables')
    db.dflot.insert( f0= 'sp6066', f1= '(6066)Calendar')
    db.dflot.insert( f0= 'ic6067', f1= '(6067)3')
    db.dflot.insert( f0= 'sp6069', f1= '(6069)Mailbox')
    db.dflot.insert( f0= 'ic6070', f1= '(6070)5')
    db.dflot.insert( f0= 'sp6071', f1= '(6071)Examples')
    db.dflot.insert( f0= 'ia6073', f1= '(6073)Invoice')
    db.dflot.insert( f0= 'ia6075', f1= '(6075)Profile')
    db.dflot.insert( f0= 'ia6077', f1= '(6077)Login')
    db.dflot.insert( f0= 'ia6079', f1= '(6079)Register')
    db.dflot.insert( f0= 'ia6081', f1= '(6081)Lockscreen')
    db.dflot.insert( f0= 'ia6083', f1= '(6083)404 Error')
    db.dflot.insert( f0= 'ia6085', f1= '(6085)500 Error')
    db.dflot.insert( f0= 'ia6087', f1= '(6087)Blank Page')
    db.dflot.insert( f0= 'ia6089', f1= '(6089)Pace Page')
    db.dflot.insert( f0= 'sp6090', f1= '(6090)Multilevel')
    db.dflot.insert( f0= 'ia6091', f1= '(6091)Level One')
    db.dflot.insert( f0= 'ia6092', f1= '(6092)Level Two')
    db.dflot.insert( f0= 'ia6093', f1= '(6093)Level Three')
    db.dflot.insert( f0= 'ia6094', f1= '(6094)Level Three')
    db.dflot.insert( f0= 'ia6095', f1= '(6095)Level One')
    db.dflot.insert( f0= 'sp6096', f1= '(6096)Documentation')
    db.dflot.insert( f0= 'lb6097', f1= '(6097)LABELS')
    db.dflot.insert( f0= 'sp6098', f1= '(6098)Important')
    db.dflot.insert( f0= 'sp6099', f1= '(6099)Warning')
    db.dflot.insert( f0= 'sp6100', f1= '(6100)Information')
    db.dflot.insert( f0= 'ic6101', f1= '(6101)preview sample')
    db.dflot.insert( f0= 'ia6102', f1= '(6102)Home')
    db.dflot.insert( f0= 'aa6103', f1= '(6103)Charts')
    db.dflot.insert( f0= 'lb6104', f1= '(6104)Flot')
    db.dflot.insert( f0= 'hc6105', f1= '(6105)Interactive Area Chart')
    db.dflot.insert( f0= 'bu6106', f1= '(6106)On')
    db.dflot.insert( f0= 'bu6107', f1= '(6107)Off')
    db.dflot.insert( f0= 'hc6108', f1= '(6108)Line Chart')
    db.dflot.insert( f0= 'hc6109', f1= '(6109)Full Width Area Chart')
    db.dflot.insert( f0= 'hc6110', f1= '(6110)Bar Chart')
    db.dflot.insert( f0= 'hc6111', f1= '(6111)Donut Chart')
    db.dflot.insert( f0= 'bb6112', f1= '(6112)Version')
    db.dflot.insert( f0= 'aa6113', f1= '(6113)AdminLTE')
    db.dflot.insert( f0= 'hc6114', f1= '(6114)Recent Activity')
    db.dflot.insert( f0= 'hd6115', f1= '(6115)Langdon s Birthday')
    db.dflot.insert( f0= 'pa6116', f1= '(6116)Will be 23 on April 24th')
    db.dflot.insert( f0= 'hd6117', f1= '(6117)Frodo Updated His Profile')
    db.dflot.insert( f0= 'pa6118', f1= '(6118)New phone +1(800)555-1234')
    db.dflot.insert( f0= 'hd6119', f1= '(6119)Nora Joined Mailing List')
    db.dflot.insert( f0= 'pa6120', f1= '(6120)nora@example.com')
    db.dflot.insert( f0= 'hd6121', f1= '(6121)Cron Job 254 Executed')
    db.dflot.insert( f0= 'pa6122', f1= '(6122)Execution time 5 seconds')
    db.dflot.insert( f0= 'hc6123', f1= '(6123)Tasks Progress')
    db.dflot.insert( f0= 'di6124', f1= '(6124)Stats Tab Content')
    db.dflot.insert( f0= 'hc6125', f1= '(6125)General Settings')
    db.dflot.insert( f0= 'hc6126', f1= '(6126)Chat Settings')
    db.commit()
#
