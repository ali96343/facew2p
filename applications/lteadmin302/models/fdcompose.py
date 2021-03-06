#
# table for controller: compose
#

from gluon.contrib.populate import populate

db.define_table('dcompose', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcompose.id ).count():
    db.dcompose.insert( f0= 'aa2323', f1= '(2323)Home')
    db.dcompose.insert( f0= 'aa2324', f1= '(2324)Contact')
    db.dcompose.insert( f0= 'pb2325', f1= '(2325)Search')
    db.dcompose.insert( f0= 'sx2326', f1= '(2326)3')
    db.dcompose.insert( f0= 'pc2328', f1= '(2328)Call me whenever you can...')
    db.dcompose.insert( f0= 'pc2329', f1= '(2329)4 Hours Ago')
    db.dcompose.insert( f0= 'pc2331', f1= '(2331)I got your message bro')
    db.dcompose.insert( f0= 'pc2332', f1= '(2332)4 Hours Ago')
    db.dcompose.insert( f0= 'pc2334', f1= '(2334)The subject goes here')
    db.dcompose.insert( f0= 'pc2335', f1= '(2335)4 Hours Ago')
    db.dcompose.insert( f0= 'aa2336', f1= '(2336)See All Messages')
    db.dcompose.insert( f0= 'sx2337', f1= '(2337)15 Notifications')
    db.dcompose.insert( f0= 'sx2338', f1= '(2338)3 mins')
    db.dcompose.insert( f0= 'sx2339', f1= '(2339)12 hours')
    db.dcompose.insert( f0= 'sx2340', f1= '(2340)2 days')
    db.dcompose.insert( f0= 'aa2341', f1= '(2341)See All Notifications')
    db.dcompose.insert( f0= 'sx2344', f1= '(2344)AdminLTE 3')
    db.dcompose.insert( f0= 'aa2346', f1= '(2346)Alexander Pierce')
    db.dcompose.insert( f0= 'pa2348', f1= '(2348)Dashboard v1')
    db.dcompose.insert( f0= 'pa2350', f1= '(2350)Dashboard v2')
    db.dcompose.insert( f0= 'pa2352', f1= '(2352)Dashboard v3')
    db.dcompose.insert( f0= 'sx2354', f1= '(2354)New')
    db.dcompose.insert( f0= 'sx2355', f1= '(2355)6')
    db.dcompose.insert( f0= 'pa2357', f1= '(2357)Top Navigation')
    db.dcompose.insert( f0= 'pa2359', f1= '(2359)Top Navigation + Sidebar')
    db.dcompose.insert( f0= 'pa2361', f1= '(2361)Boxed')
    db.dcompose.insert( f0= 'pa2363', f1= '(2363)Fixed Sidebar')
    db.dcompose.insert( f0= 'pa2365', f1= '(2365)Fixed Navbar')
    db.dcompose.insert( f0= 'pa2367', f1= '(2367)Fixed Footer')
    db.dcompose.insert( f0= 'pa2369', f1= '(2369)Collapsed Sidebar')
    db.dcompose.insert( f0= 'pa2371', f1= '(2371)ChartJS')
    db.dcompose.insert( f0= 'pa2373', f1= '(2373)Flot')
    db.dcompose.insert( f0= 'pa2375', f1= '(2375)Inline')
    db.dcompose.insert( f0= 'pa2377', f1= '(2377)General')
    db.dcompose.insert( f0= 'pa2379', f1= '(2379)Icons')
    db.dcompose.insert( f0= 'pa2381', f1= '(2381)Buttons')
    db.dcompose.insert( f0= 'pa2383', f1= '(2383)Sliders')
    db.dcompose.insert( f0= 'pa2385', f1= '(2385)Modals & Alerts')
    db.dcompose.insert( f0= 'pa2387', f1= '(2387)Navbar & Tabs')
    db.dcompose.insert( f0= 'pa2389', f1= '(2389)Timeline')
    db.dcompose.insert( f0= 'pa2391', f1= '(2391)Ribbons')
    db.dcompose.insert( f0= 'pa2393', f1= '(2393)General Elements')
    db.dcompose.insert( f0= 'pa2395', f1= '(2395)Advanced Elements')
    db.dcompose.insert( f0= 'pa2397', f1= '(2397)Editors')
    db.dcompose.insert( f0= 'pa2399', f1= '(2399)Validation')
    db.dcompose.insert( f0= 'pa2401', f1= '(2401)Simple Tables')
    db.dcompose.insert( f0= 'pa2403', f1= '(2403)DataTables')
    db.dcompose.insert( f0= 'pa2405', f1= '(2405)jsGrid')
    db.dcompose.insert( f0= 'lb2406', f1= '(2406)EXAMPLES')
    db.dcompose.insert( f0= 'sx2408', f1= '(2408)2')
    db.dcompose.insert( f0= 'pa2410', f1= '(2410)Inbox')
    db.dcompose.insert( f0= 'pa2412', f1= '(2412)Compose')
    db.dcompose.insert( f0= 'pa2414', f1= '(2414)Read')
    db.dcompose.insert( f0= 'pa2416', f1= '(2416)Invoice')
    db.dcompose.insert( f0= 'pa2418', f1= '(2418)Profile')
    db.dcompose.insert( f0= 'pa2420', f1= '(2420)E-commerce')
    db.dcompose.insert( f0= 'pa2422', f1= '(2422)Projects')
    db.dcompose.insert( f0= 'pa2424', f1= '(2424)Project Add')
    db.dcompose.insert( f0= 'pa2426', f1= '(2426)Project Edit')
    db.dcompose.insert( f0= 'pa2428', f1= '(2428)Project Detail')
    db.dcompose.insert( f0= 'pa2430', f1= '(2430)Contacts')
    db.dcompose.insert( f0= 'pa2432', f1= '(2432)Login')
    db.dcompose.insert( f0= 'pa2434', f1= '(2434)Register')
    db.dcompose.insert( f0= 'pa2436', f1= '(2436)Forgot Password')
    db.dcompose.insert( f0= 'pa2438', f1= '(2438)Recover Password')
    db.dcompose.insert( f0= 'pa2440', f1= '(2440)Lockscreen')
    db.dcompose.insert( f0= 'pa2442', f1= '(2442)Legacy User Menu')
    db.dcompose.insert( f0= 'pa2444', f1= '(2444)Language Menu')
    db.dcompose.insert( f0= 'pa2446', f1= '(2446)Error 404')
    db.dcompose.insert( f0= 'pa2448', f1= '(2448)Error 500')
    db.dcompose.insert( f0= 'pa2450', f1= '(2450)Pace')
    db.dcompose.insert( f0= 'pa2452', f1= '(2452)Blank Page')
    db.dcompose.insert( f0= 'pa2454', f1= '(2454)Starter Page')
    db.dcompose.insert( f0= 'lb2455', f1= '(2455)MISCELLANEOUS')
    db.dcompose.insert( f0= 'pa2456', f1= '(2456)Documentation')
    db.dcompose.insert( f0= 'lb2457', f1= '(2457)MULTI LEVEL EXAMPLE')
    db.dcompose.insert( f0= 'pa2458', f1= '(2458)Level 1')
    db.dcompose.insert( f0= 'pa2459', f1= '(2459)Level 2')
    db.dcompose.insert( f0= 'pa2460', f1= '(2460)Level 3')
    db.dcompose.insert( f0= 'pa2461', f1= '(2461)Level 3')
    db.dcompose.insert( f0= 'pa2462', f1= '(2462)Level 3')
    db.dcompose.insert( f0= 'pa2463', f1= '(2463)Level 2')
    db.dcompose.insert( f0= 'pa2464', f1= '(2464)Level 1')
    db.dcompose.insert( f0= 'lb2465', f1= '(2465)LABELS')
    db.dcompose.insert( f0= 'pc2466', f1= '(2466)Important')
    db.dcompose.insert( f0= 'pa2467', f1= '(2467)Warning')
    db.dcompose.insert( f0= 'pa2468', f1= '(2468)Informational')
    db.dcompose.insert( f0= 'hh2469', f1= '(2469)Compose')
    db.dcompose.insert( f0= 'aa2470', f1= '(2470)Home')
    db.dcompose.insert( f0= 'lb2471', f1= '(2471)Compose')
    db.dcompose.insert( f0= 'aa2473', f1= '(2473)Back to Inbox')
    db.dcompose.insert( f0= 'hc2474', f1= '(2474)Folders')
    db.dcompose.insert( f0= 'hc2475', f1= '(2475)Labels')
    db.dcompose.insert( f0= 'ia2476', f1= '(2476)Important')
    db.dcompose.insert( f0= 'ia2477', f1= '(2477)Promotions')
    db.dcompose.insert( f0= 'ia2478', f1= '(2478)Social')
    db.dcompose.insert( f0= 'hc2479', f1= '(2479)Compose New Message')
    db.dcompose.insert( f0= 'pb2480', f1= '(2480)To:')
    db.dcompose.insert( f0= 'pb2481', f1= '(2481)Subject:')
    db.dcompose.insert( f0= 'hh2482', f1= '(2482)Subheading')
    db.dcompose.insert( f0= 'la2483', f1= '(2483)List item one')
    db.dcompose.insert( f0= 'la2484', f1= '(2484)List item two')
    db.dcompose.insert( f0= 'la2485', f1= '(2485)List item three')
    db.dcompose.insert( f0= 'la2486', f1= '(2486)List item four')
    db.dcompose.insert( f0= 'pa2487', f1= '(2487)Thank you,')
    db.dcompose.insert( f0= 'pa2488', f1= '(2488)John Doe')
    db.dcompose.insert( f0= 'pc2489', f1= '(2489)Max. 32MB')
    db.dcompose.insert( f0= 'bb2490', f1= '(2490)Version')
    db.dcompose.insert( f0= 'aa2491', f1= '(2491)AdminLTE.io')
    db.commit()
#
