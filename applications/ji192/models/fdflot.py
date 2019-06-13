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
    db.dflot.insert( f0= 'sx5881', f1= '(5881)LT')
    db.dflot.insert( f0= 'bb5882', f1= '(5882)Admin')
    db.dflot.insert( f0= 'sx5883', f1= '(5883)LTE')
    db.dflot.insert( f0= 'sx5884', f1= '(5884)Toggle navigation')
    db.dflot.insert( f0= 'lb5885', f1= '(5885)You have 4 messages')
    db.dflot.insert( f0= 'ib5887', f1= '(5887)5 mins')
    db.dflot.insert( f0= 'pa5888', f1= '(5888)Why not buy a new awesome theme?')
    db.dflot.insert( f0= 'ib5890', f1= '(5890)2 hours')
    db.dflot.insert( f0= 'pa5891', f1= '(5891)Why not buy a new awesome theme?')
    db.dflot.insert( f0= 'ib5893', f1= '(5893)Today')
    db.dflot.insert( f0= 'pa5894', f1= '(5894)Why not buy a new awesome theme?')
    db.dflot.insert( f0= 'ib5896', f1= '(5896)Yesterday')
    db.dflot.insert( f0= 'pa5897', f1= '(5897)Why not buy a new awesome theme?')
    db.dflot.insert( f0= 'ib5899', f1= '(5899)2 days')
    db.dflot.insert( f0= 'pa5900', f1= '(5900)Why not buy a new awesome theme?')
    db.dflot.insert( f0= 'aa5901', f1= '(5901)See All Messages')
    db.dflot.insert( f0= 'sx5902', f1= '(5902)10')
    db.dflot.insert( f0= 'lb5903', f1= '(5903)You have 10 notifications')
    db.dflot.insert( f0= 'aa5904', f1= '(5904)View all')
    db.dflot.insert( f0= 'lb5905', f1= '(5905)You have 9 tasks')
    db.dflot.insert( f0= 'ic5906', f1= '(5906)20%')
    db.dflot.insert( f0= 'sx5907', f1= '(5907)20% Complete')
    db.dflot.insert( f0= 'ic5908', f1= '(5908)40%')
    db.dflot.insert( f0= 'sx5909', f1= '(5909)40% Complete')
    db.dflot.insert( f0= 'ic5910', f1= '(5910)60%')
    db.dflot.insert( f0= 'sx5911', f1= '(5911)60% Complete')
    db.dflot.insert( f0= 'ic5912', f1= '(5912)80%')
    db.dflot.insert( f0= 'sx5913', f1= '(5913)80% Complete')
    db.dflot.insert( f0= 'aa5914', f1= '(5914)View all tasks')
    db.dflot.insert( f0= 'sx5916', f1= '(5916)Alexander Pierce')
    db.dflot.insert( f0= 'ic5918', f1= '(5918)Member since Nov. 2012')
    db.dflot.insert( f0= 'aa5919', f1= '(5919)Followers')
    db.dflot.insert( f0= 'aa5920', f1= '(5920)Sales')
    db.dflot.insert( f0= 'aa5921', f1= '(5921)Friends')
    db.dflot.insert( f0= 'aa5922', f1= '(5922)Profile')
    db.dflot.insert( f0= 'aa5923', f1= '(5923)Sign out')
    db.dflot.insert( f0= 'pa5925', f1= '(5925)Alexander Pierce')
    db.dflot.insert( f0= 'ia5926', f1= '(5926)Online')
    db.dflot.insert( f0= 'pb5927', f1= '(5927)Search...')
    db.dflot.insert( f0= 'lb5928', f1= '(5928)MAIN NAVIGATION')
    db.dflot.insert( f0= 'sp5929', f1= '(5929)Dashboard')
    db.dflot.insert( f0= 'ia5931', f1= '(5931)Dashboard v1')
    db.dflot.insert( f0= 'ia5933', f1= '(5933)Dashboard v2')
    db.dflot.insert( f0= 'sp5934', f1= '(5934)Layout Options')
    db.dflot.insert( f0= 'ia5936', f1= '(5936)Top Navigation')
    db.dflot.insert( f0= 'ia5938', f1= '(5938)Boxed')
    db.dflot.insert( f0= 'ia5940', f1= '(5940)Fixed')
    db.dflot.insert( f0= 'ia5942', f1= '(5942)Collapsed Sidebar')
    db.dflot.insert( f0= 'sp5944', f1= '(5944)Widgets')
    db.dflot.insert( f0= 'ic5945', f1= '(5945)new')
    db.dflot.insert( f0= 'sp5946', f1= '(5946)Charts')
    db.dflot.insert( f0= 'ia5948', f1= '(5948)ChartJS')
    db.dflot.insert( f0= 'ia5950', f1= '(5950)Morris')
    db.dflot.insert( f0= 'ia5952', f1= '(5952)Flot')
    db.dflot.insert( f0= 'ia5954', f1= '(5954)Inline charts')
    db.dflot.insert( f0= 'sp5955', f1= '(5955)UI Elements')
    db.dflot.insert( f0= 'ia5957', f1= '(5957)General')
    db.dflot.insert( f0= 'ia5959', f1= '(5959)Icons')
    db.dflot.insert( f0= 'ia5961', f1= '(5961)Buttons')
    db.dflot.insert( f0= 'ia5963', f1= '(5963)Sliders')
    db.dflot.insert( f0= 'ia5965', f1= '(5965)Timeline')
    db.dflot.insert( f0= 'ia5967', f1= '(5967)Modals')
    db.dflot.insert( f0= 'sp5968', f1= '(5968)Forms')
    db.dflot.insert( f0= 'ia5970', f1= '(5970)General Elements')
    db.dflot.insert( f0= 'ia5972', f1= '(5972)Advanced Elements')
    db.dflot.insert( f0= 'ia5974', f1= '(5974)Editors')
    db.dflot.insert( f0= 'sp5975', f1= '(5975)Tables')
    db.dflot.insert( f0= 'ia5977', f1= '(5977)Simple tables')
    db.dflot.insert( f0= 'ia5979', f1= '(5979)Data tables')
    db.dflot.insert( f0= 'sp5981', f1= '(5981)Calendar')
    db.dflot.insert( f0= 'ic5982', f1= '(5982)17')
    db.dflot.insert( f0= 'sp5984', f1= '(5984)Mailbox')
    db.dflot.insert( f0= 'ic5985', f1= '(5985)12')
    db.dflot.insert( f0= 'ic5986', f1= '(5986)16')
    db.dflot.insert( f0= 'sp5987', f1= '(5987)Examples')
    db.dflot.insert( f0= 'ia5989', f1= '(5989)Invoice')
    db.dflot.insert( f0= 'ia5991', f1= '(5991)Profile')
    db.dflot.insert( f0= 'ia5993', f1= '(5993)Login')
    db.dflot.insert( f0= 'ia5995', f1= '(5995)Register')
    db.dflot.insert( f0= 'ia5997', f1= '(5997)Lockscreen')
    db.dflot.insert( f0= 'ia5999', f1= '(5999)404 Error')
    db.dflot.insert( f0= 'ia6001', f1= '(6001)500 Error')
    db.dflot.insert( f0= 'ia6003', f1= '(6003)Blank Page')
    db.dflot.insert( f0= 'ia6005', f1= '(6005)Pace Page')
    db.dflot.insert( f0= 'sp6006', f1= '(6006)Multilevel')
    db.dflot.insert( f0= 'ia6007', f1= '(6007)Level One')
    db.dflot.insert( f0= 'ia6008', f1= '(6008)Level Two')
    db.dflot.insert( f0= 'ia6009', f1= '(6009)Level Three')
    db.dflot.insert( f0= 'ia6010', f1= '(6010)Level Three')
    db.dflot.insert( f0= 'ia6011', f1= '(6011)Level One')
    db.dflot.insert( f0= 'sp6012', f1= '(6012)Documentation')
    db.dflot.insert( f0= 'lb6013', f1= '(6013)LABELS')
    db.dflot.insert( f0= 'sp6014', f1= '(6014)Important')
    db.dflot.insert( f0= 'sp6015', f1= '(6015)Warning')
    db.dflot.insert( f0= 'sp6016', f1= '(6016)Information')
    db.dflot.insert( f0= 'ic6017', f1= '(6017)preview sample')
    db.dflot.insert( f0= 'ia6018', f1= '(6018)Home')
    db.dflot.insert( f0= 'aa6019', f1= '(6019)Charts')
    db.dflot.insert( f0= 'lb6020', f1= '(6020)Flot')
    db.dflot.insert( f0= 'hc6021', f1= '(6021)Interactive Area Chart')
    db.dflot.insert( f0= 'bu6022', f1= '(6022)On')
    db.dflot.insert( f0= 'bu6023', f1= '(6023)Off')
    db.dflot.insert( f0= 'hc6024', f1= '(6024)Line Chart')
    db.dflot.insert( f0= 'hc6025', f1= '(6025)Full Width Area Chart')
    db.dflot.insert( f0= 'hc6026', f1= '(6026)Bar Chart')
    db.dflot.insert( f0= 'hc6027', f1= '(6027)Donut Chart')
    db.dflot.insert( f0= 'bb6028', f1= '(6028)Version')
    db.dflot.insert( f0= 'hc6030', f1= '(6030)Recent Activity')
    db.dflot.insert( f0= 'hd6031', f1= '(6031)Langdon s Birthday')
    db.dflot.insert( f0= 'pa6032', f1= '(6032)Will be 23 on April 24th')
    db.dflot.insert( f0= 'hd6033', f1= '(6033)Frodo Updated His Profile')
    db.dflot.insert( f0= 'pa6034', f1= '(6034)New phone +1(800)555-1234')
    db.dflot.insert( f0= 'hd6035', f1= '(6035)Nora Joined Mailing List')
    db.dflot.insert( f0= 'pa6036', f1= '(6036)nora@example.com')
    db.dflot.insert( f0= 'hd6037', f1= '(6037)Cron Job 254 Executed')
    db.dflot.insert( f0= 'pa6038', f1= '(6038)Execution time 5 seconds')
    db.dflot.insert( f0= 'hc6039', f1= '(6039)Tasks Progress')
    db.dflot.insert( f0= 'sx6040', f1= '(6040)70%')
    db.dflot.insert( f0= 'sx6041', f1= '(6041)95%')
    db.dflot.insert( f0= 'sx6042', f1= '(6042)50%')
    db.dflot.insert( f0= 'sx6043', f1= '(6043)68%')
    db.dflot.insert( f0= 'di6044', f1= '(6044)Stats Tab Content')
    db.dflot.insert( f0= 'hc6045', f1= '(6045)General Settings')
    db.dflot.insert( f0= 'hc6046', f1= '(6046)Chat Settings')
    db.commit()
#
