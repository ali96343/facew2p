#
# table for controller: editors
#

from gluon.contrib.populate import populate

db.define_table('deditors', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.deditors.id ).count():
    db.deditors.insert( f0= 'bb2303', f1= '(2303)A')
    db.deditors.insert( f0= 'sx2304', f1= '(2304)LT')
    db.deditors.insert( f0= 'bb2305', f1= '(2305)Admin')
    db.deditors.insert( f0= 'sx2306', f1= '(2306)LTE')
    db.deditors.insert( f0= 'sx2307', f1= '(2307)Toggle navigation')
    db.deditors.insert( f0= 'sx2308', f1= '(2308)4')
    db.deditors.insert( f0= 'lb2309', f1= '(2309)You have 4 messages')
    db.deditors.insert( f0= 'ib2311', f1= '(2311)5 mins')
    db.deditors.insert( f0= 'pa2312', f1= '(2312)Why not buy a new awesome theme?')
    db.deditors.insert( f0= 'ib2314', f1= '(2314)2 hours')
    db.deditors.insert( f0= 'pa2315', f1= '(2315)Why not buy a new awesome theme?')
    db.deditors.insert( f0= 'ib2317', f1= '(2317)Today')
    db.deditors.insert( f0= 'pa2318', f1= '(2318)Why not buy a new awesome theme?')
    db.deditors.insert( f0= 'ib2320', f1= '(2320)Yesterday')
    db.deditors.insert( f0= 'pa2321', f1= '(2321)Why not buy a new awesome theme?')
    db.deditors.insert( f0= 'ib2323', f1= '(2323)2 days')
    db.deditors.insert( f0= 'pa2324', f1= '(2324)Why not buy a new awesome theme?')
    db.deditors.insert( f0= 'aa2325', f1= '(2325)See All Messages')
    db.deditors.insert( f0= 'lb2326', f1= '(2326)You have 10 notifications')
    db.deditors.insert( f0= 'aa2327', f1= '(2327)View all')
    db.deditors.insert( f0= 'sx2328', f1= '(2328)9')
    db.deditors.insert( f0= 'lb2329', f1= '(2329)You have 9 tasks')
    db.deditors.insert( f0= 'sx2330', f1= '(2330)20% Complete')
    db.deditors.insert( f0= 'sx2331', f1= '(2331)40% Complete')
    db.deditors.insert( f0= 'sx2332', f1= '(2332)60% Complete')
    db.deditors.insert( f0= 'sx2333', f1= '(2333)80% Complete')
    db.deditors.insert( f0= 'aa2334', f1= '(2334)View all tasks')
    db.deditors.insert( f0= 'sx2336', f1= '(2336)Alexander Pierce')
    db.deditors.insert( f0= 'ic2338', f1= '(2338)Member since Nov. 2012')
    db.deditors.insert( f0= 'aa2339', f1= '(2339)Followers')
    db.deditors.insert( f0= 'aa2340', f1= '(2340)Sales')
    db.deditors.insert( f0= 'aa2341', f1= '(2341)Friends')
    db.deditors.insert( f0= 'aa2342', f1= '(2342)Profile')
    db.deditors.insert( f0= 'aa2343', f1= '(2343)Sign out')
    db.deditors.insert( f0= 'pa2345', f1= '(2345)Alexander Pierce')
    db.deditors.insert( f0= 'ia2346', f1= '(2346)Online')
    db.deditors.insert( f0= 'pb2347', f1= '(2347)Search...')
    db.deditors.insert( f0= 'lb2348', f1= '(2348)MAIN NAVIGATION')
    db.deditors.insert( f0= 'sp2349', f1= '(2349)Dashboard')
    db.deditors.insert( f0= 'ia2351', f1= '(2351)Dashboard v1')
    db.deditors.insert( f0= 'ia2353', f1= '(2353)Dashboard v2')
    db.deditors.insert( f0= 'sp2354', f1= '(2354)Layout Options')
    db.deditors.insert( f0= 'sx2355', f1= '(2355)4')
    db.deditors.insert( f0= 'ia2357', f1= '(2357)Top Navigation')
    db.deditors.insert( f0= 'ia2359', f1= '(2359)Boxed')
    db.deditors.insert( f0= 'ia2361', f1= '(2361)Fixed')
    db.deditors.insert( f0= 'ia2363', f1= '(2363)Collapsed Sidebar')
    db.deditors.insert( f0= 'sp2365', f1= '(2365)Widgets')
    db.deditors.insert( f0= 'ic2366', f1= '(2366)new')
    db.deditors.insert( f0= 'sp2367', f1= '(2367)Charts')
    db.deditors.insert( f0= 'ia2369', f1= '(2369)ChartJS')
    db.deditors.insert( f0= 'ia2371', f1= '(2371)Morris')
    db.deditors.insert( f0= 'ia2373', f1= '(2373)Flot')
    db.deditors.insert( f0= 'ia2375', f1= '(2375)Inline charts')
    db.deditors.insert( f0= 'sp2376', f1= '(2376)UI Elements')
    db.deditors.insert( f0= 'ia2378', f1= '(2378)General')
    db.deditors.insert( f0= 'ia2380', f1= '(2380)Icons')
    db.deditors.insert( f0= 'ia2382', f1= '(2382)Buttons')
    db.deditors.insert( f0= 'ia2384', f1= '(2384)Sliders')
    db.deditors.insert( f0= 'ia2386', f1= '(2386)Timeline')
    db.deditors.insert( f0= 'ia2388', f1= '(2388)Modals')
    db.deditors.insert( f0= 'sp2389', f1= '(2389)Forms')
    db.deditors.insert( f0= 'ia2391', f1= '(2391)General Elements')
    db.deditors.insert( f0= 'ia2393', f1= '(2393)Advanced Elements')
    db.deditors.insert( f0= 'ia2395', f1= '(2395)Editors')
    db.deditors.insert( f0= 'sp2396', f1= '(2396)Tables')
    db.deditors.insert( f0= 'ia2398', f1= '(2398)Simple tables')
    db.deditors.insert( f0= 'ia2400', f1= '(2400)Data tables')
    db.deditors.insert( f0= 'sp2402', f1= '(2402)Calendar')
    db.deditors.insert( f0= 'ic2403', f1= '(2403)3')
    db.deditors.insert( f0= 'sp2405', f1= '(2405)Mailbox')
    db.deditors.insert( f0= 'ic2406', f1= '(2406)5')
    db.deditors.insert( f0= 'sp2407', f1= '(2407)Examples')
    db.deditors.insert( f0= 'ia2409', f1= '(2409)Invoice')
    db.deditors.insert( f0= 'ia2411', f1= '(2411)Profile')
    db.deditors.insert( f0= 'ia2413', f1= '(2413)Login')
    db.deditors.insert( f0= 'ia2415', f1= '(2415)Register')
    db.deditors.insert( f0= 'ia2417', f1= '(2417)Lockscreen')
    db.deditors.insert( f0= 'ia2419', f1= '(2419)404 Error')
    db.deditors.insert( f0= 'ia2421', f1= '(2421)500 Error')
    db.deditors.insert( f0= 'ia2423', f1= '(2423)Blank Page')
    db.deditors.insert( f0= 'ia2425', f1= '(2425)Pace Page')
    db.deditors.insert( f0= 'sp2426', f1= '(2426)Multilevel')
    db.deditors.insert( f0= 'ia2427', f1= '(2427)Level One')
    db.deditors.insert( f0= 'ia2428', f1= '(2428)Level Two')
    db.deditors.insert( f0= 'ia2429', f1= '(2429)Level Three')
    db.deditors.insert( f0= 'ia2430', f1= '(2430)Level Three')
    db.deditors.insert( f0= 'ia2431', f1= '(2431)Level One')
    db.deditors.insert( f0= 'sp2432', f1= '(2432)Documentation')
    db.deditors.insert( f0= 'lb2433', f1= '(2433)LABELS')
    db.deditors.insert( f0= 'sp2434', f1= '(2434)Important')
    db.deditors.insert( f0= 'sp2435', f1= '(2435)Warning')
    db.deditors.insert( f0= 'sp2436', f1= '(2436)Information')
    db.deditors.insert( f0= 'ic2437', f1= '(2437)Advanced form element')
    db.deditors.insert( f0= 'ia2438', f1= '(2438)Home')
    db.deditors.insert( f0= 'aa2439', f1= '(2439)Forms')
    db.deditors.insert( f0= 'lb2440', f1= '(2440)Editors')
    db.deditors.insert( f0= 'ic2441', f1= '(2441)Advanced and full of features')
    db.deditors.insert( f0= 'ic2442', f1= '(2442)Simple and fast')
    db.deditors.insert( f0= 'pb2443', f1= '(2443)Place some text here')
    db.deditors.insert( f0= 'bb2444', f1= '(2444)Version')
    db.deditors.insert( f0= 'aa2445', f1= '(2445)AdminLTE')
    db.deditors.insert( f0= 'hc2446', f1= '(2446)Recent Activity')
    db.deditors.insert( f0= 'hd2447', f1= '(2447)Langdon s Birthday')
    db.deditors.insert( f0= 'pa2448', f1= '(2448)Will be 23 on April 24th')
    db.deditors.insert( f0= 'hd2449', f1= '(2449)Frodo Updated His Profile')
    db.deditors.insert( f0= 'pa2450', f1= '(2450)New phone +1(800)555-1234')
    db.deditors.insert( f0= 'hd2451', f1= '(2451)Nora Joined Mailing List')
    db.deditors.insert( f0= 'pa2452', f1= '(2452)nora@example.com')
    db.deditors.insert( f0= 'hd2453', f1= '(2453)Cron Job 254 Executed')
    db.deditors.insert( f0= 'pa2454', f1= '(2454)Execution time 5 seconds')
    db.deditors.insert( f0= 'hc2455', f1= '(2455)Tasks Progress')
    db.deditors.insert( f0= 'di2456', f1= '(2456)Stats Tab Content')
    db.deditors.insert( f0= 'hc2457', f1= '(2457)General Settings')
    db.deditors.insert( f0= 'hc2458', f1= '(2458)Chat Settings')
    db.commit()
#
