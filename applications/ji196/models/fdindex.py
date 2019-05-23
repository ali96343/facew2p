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
    db.dindex.insert( f0= 'aa2413', f1= '(2413)Dashboard 1')
    db.dindex.insert( f0= 'aa2415', f1= '(2415)Dashboard 2')
    db.dindex.insert( f0= 'aa2417', f1= '(2417)Dashboard 3')
    db.dindex.insert( f0= 'aa2419', f1= '(2419)Dashboard 4')
    db.dindex.insert( f0= 'aa2425', f1= '(2425)Login')
    db.dindex.insert( f0= 'aa2427', f1= '(2427)Register')
    db.dindex.insert( f0= 'aa2429', f1= '(2429)Forget Password')
    db.dindex.insert( f0= 'aa2431', f1= '(2431)Button')
    db.dindex.insert( f0= 'aa2433', f1= '(2433)Badges')
    db.dindex.insert( f0= 'aa2435', f1= '(2435)Tabs')
    db.dindex.insert( f0= 'aa2437', f1= '(2437)Cards')
    db.dindex.insert( f0= 'aa2439', f1= '(2439)Alerts')
    db.dindex.insert( f0= 'aa2441', f1= '(2441)Progress Bars')
    db.dindex.insert( f0= 'aa2443', f1= '(2443)Modals')
    db.dindex.insert( f0= 'aa2445', f1= '(2445)Switchs')
    db.dindex.insert( f0= 'aa2447', f1= '(2447)Grids')
    db.dindex.insert( f0= 'aa2449', f1= '(2449)Fontawesome Icon')
    db.dindex.insert( f0= 'aa2451', f1= '(2451)Typography')
    db.dindex.insert( f0= 'aa2454', f1= '(2454)Dashboard 1')
    db.dindex.insert( f0= 'aa2456', f1= '(2456)Dashboard 2')
    db.dindex.insert( f0= 'aa2458', f1= '(2458)Dashboard 3')
    db.dindex.insert( f0= 'aa2460', f1= '(2460)Dashboard 4')
    db.dindex.insert( f0= 'aa2466', f1= '(2466)Login')
    db.dindex.insert( f0= 'aa2468', f1= '(2468)Register')
    db.dindex.insert( f0= 'aa2470', f1= '(2470)Forget Password')
    db.dindex.insert( f0= 'aa2472', f1= '(2472)Button')
    db.dindex.insert( f0= 'aa2474', f1= '(2474)Badges')
    db.dindex.insert( f0= 'aa2476', f1= '(2476)Tabs')
    db.dindex.insert( f0= 'aa2478', f1= '(2478)Cards')
    db.dindex.insert( f0= 'aa2480', f1= '(2480)Alerts')
    db.dindex.insert( f0= 'aa2482', f1= '(2482)Progress Bars')
    db.dindex.insert( f0= 'aa2484', f1= '(2484)Modals')
    db.dindex.insert( f0= 'aa2486', f1= '(2486)Switchs')
    db.dindex.insert( f0= 'aa2488', f1= '(2488)Grids')
    db.dindex.insert( f0= 'aa2490', f1= '(2490)Fontawesome Icon')
    db.dindex.insert( f0= 'aa2492', f1= '(2492)Typography')
    db.dindex.insert( f0= 'pb2493', f1= '(2493)Search for datas &amp; reports...')
    db.dindex.insert( f0= 'pa2494', f1= '(2494)You have 2 news message')
    db.dindex.insert( f0= 'hh2496', f1= '(2496)Michelle Moreno')
    db.dindex.insert( f0= 'pa2497', f1= '(2497)Have sent a photo')
    db.dindex.insert( f0= 'sx2498', f1= '(2498)3 min ago')
    db.dindex.insert( f0= 'hh2500', f1= '(2500)Diane Myers')
    db.dindex.insert( f0= 'pa2501', f1= '(2501)You are now connected on message')
    db.dindex.insert( f0= 'sx2502', f1= '(2502)Yesterday')
    db.dindex.insert( f0= 'aa2503', f1= '(2503)View all messages')
    db.dindex.insert( f0= 'pa2504', f1= '(2504)You have 3 New Emails')
    db.dindex.insert( f0= 'pa2506', f1= '(2506)Meeting about new dashboard...')
    db.dindex.insert( f0= 'sp2507', f1= '(2507)Cynthia Harvey, 3 min ago')
    db.dindex.insert( f0= 'pa2509', f1= '(2509)Meeting about new dashboard...')
    db.dindex.insert( f0= 'sp2510', f1= '(2510)Cynthia Harvey, Yesterday')
    db.dindex.insert( f0= 'pa2512', f1= '(2512)Meeting about new dashboard...')
    db.dindex.insert( f0= 'sp2513', f1= '(2513)Cynthia Harvey, April 12,,2018')
    db.dindex.insert( f0= 'aa2514', f1= '(2514)See all emails')
    db.dindex.insert( f0= 'pa2515', f1= '(2515)You have 3 Notifications')
    db.dindex.insert( f0= 'pa2516', f1= '(2516)You got a email notification')
    db.dindex.insert( f0= 'sx2517', f1= '(2517)April 12, 2018 06:50')
    db.dindex.insert( f0= 'pa2518', f1= '(2518)Your account has been blocked')
    db.dindex.insert( f0= 'sx2519', f1= '(2519)April 12, 2018 06:50')
    db.dindex.insert( f0= 'pa2520', f1= '(2520)You got a new file')
    db.dindex.insert( f0= 'sx2521', f1= '(2521)April 12, 2018 06:50')
    db.dindex.insert( f0= 'aa2522', f1= '(2522)All notifications')
    db.dindex.insert( f0= 'aa2524', f1= '(2524)john doe')
    db.dindex.insert( f0= 'aa2526', f1= '(2526)john doe')
    db.dindex.insert( f0= 'sx2527', f1= '(2527)johndoe@example.com')
    db.dindex.insert( f0= 'hb2528', f1= '(2528)overview')
    db.dindex.insert( f0= 'hh2529', f1= '(2529)10368')
    db.dindex.insert( f0= 'sp2530', f1= '(2530)members online')
    db.dindex.insert( f0= 'hh2531', f1= '(2531)388,688')
    db.dindex.insert( f0= 'sp2532', f1= '(2532)items solid')
    db.dindex.insert( f0= 'hh2533', f1= '(2533)1,086')
    db.dindex.insert( f0= 'sp2534', f1= '(2534)this week')
    db.dindex.insert( f0= 'hh2535', f1= '(2535)$1,060,386')
    db.dindex.insert( f0= 'sp2536', f1= '(2536)total earnings')
    db.dindex.insert( f0= 'hc2537', f1= '(2537)recent reports')
    db.dindex.insert( f0= 'sp2538', f1= '(2538)products')
    db.dindex.insert( f0= 'sp2539', f1= '(2539)services')
    db.dindex.insert( f0= 'sx2540', f1= '(2540)25%')
    db.dindex.insert( f0= 'sx2541', f1= '(2541)products')
    db.dindex.insert( f0= 'sx2542', f1= '(2542)10%')
    db.dindex.insert( f0= 'sx2543', f1= '(2543)services')
    db.dindex.insert( f0= 'hc2544', f1= '(2544)char by %')
    db.dindex.insert( f0= 'sp2545', f1= '(2545)products')
    db.dindex.insert( f0= 'sp2546', f1= '(2546)services')
    db.dindex.insert( f0= 'hb2547', f1= '(2547)Earnings By Items')
    db.dindex.insert( f0= 'hb2567', f1= '(2567)Top countries')
    db.dindex.insert( f0= 'pa2576', f1= '(2576)Tasks for John Doe')
    db.dindex.insert( f0= 'aa2577', f1= '(2577)Meeting about plan for Admin Template 2018')
    db.dindex.insert( f0= 'sx2578', f1= '(2578)10:00 AM')
    db.dindex.insert( f0= 'aa2579', f1= '(2579)Create new task for Dashboard')
    db.dindex.insert( f0= 'sx2580', f1= '(2580)11:00 AM')
    db.dindex.insert( f0= 'aa2581', f1= '(2581)Meeting about plan for Admin Template 2018')
    db.dindex.insert( f0= 'sx2582', f1= '(2582)02:00 PM')
    db.dindex.insert( f0= 'aa2583', f1= '(2583)Create new task for Dashboard')
    db.dindex.insert( f0= 'sx2584', f1= '(2584)03:30 PM')
    db.dindex.insert( f0= 'aa2585', f1= '(2585)Meeting about plan for Admin Template 2018')
    db.dindex.insert( f0= 'sx2586', f1= '(2586)10:00 AM')
    db.dindex.insert( f0= 'aa2587', f1= '(2587)Create new task for Dashboard')
    db.dindex.insert( f0= 'sx2588', f1= '(2588)11:00 AM')
    db.dindex.insert( f0= 'bu2589', f1= '(2589)load more')
    db.dindex.insert( f0= 'he2592', f1= '(2592)John Smith')
    db.dindex.insert( f0= 'pa2593', f1= '(2593)Have sent a photo')
    db.dindex.insert( f0= 'sp2594', f1= '(2594)12 Min ago')
    db.dindex.insert( f0= 'he2596', f1= '(2596)Nicholas Martinez')
    db.dindex.insert( f0= 'pa2597', f1= '(2597)You are now connected on message')
    db.dindex.insert( f0= 'sp2598', f1= '(2598)11:00 PM')
    db.dindex.insert( f0= 'he2600', f1= '(2600)Michelle Sims')
    db.dindex.insert( f0= 'pa2601', f1= '(2601)Lorem ipsum dolor sit amet')
    db.dindex.insert( f0= 'sp2602', f1= '(2602)Yesterday')
    db.dindex.insert( f0= 'he2604', f1= '(2604)Michelle Sims')
    db.dindex.insert( f0= 'pa2605', f1= '(2605)Purus feugiat finibus')
    db.dindex.insert( f0= 'sp2606', f1= '(2606)Sunday')
    db.dindex.insert( f0= 'he2608', f1= '(2608)Michelle Sims')
    db.dindex.insert( f0= 'pa2609', f1= '(2609)Lorem ipsum dolor sit amet')
    db.dindex.insert( f0= 'sp2610', f1= '(2610)Yesterday')
    db.dindex.insert( f0= 'he2612', f1= '(2612)Michelle Sims')
    db.dindex.insert( f0= 'pa2613', f1= '(2613)Purus feugiat finibus')
    db.dindex.insert( f0= 'sp2614', f1= '(2614)Sunday')
    db.dindex.insert( f0= 'bu2615', f1= '(2615)load more')
    db.dindex.insert( f0= 'aa2617', f1= '(2617)John Smith')
    db.dindex.insert( f0= 'sx2618', f1= '(2618)12 Min ago')
    db.dindex.insert( f0= 'di2620', f1= '(2620)Lorem ipsum dolor sit amet, consectetur adipiscing elit non iaculis')
    db.dindex.insert( f0= 'di2621', f1= '(2621)Donec tempor, sapien ac viverra')
    db.dindex.insert( f0= 'sx2622', f1= '(2622)30 Sec ago')
    db.dindex.insert( f0= 'di2623', f1= '(2623)Lorem ipsum dolor sit amet, consectetur adipiscing elit non iaculis')
    db.dindex.insert( f0= 'pb2624', f1= '(2624)Type a message')
    db.commit()
#
