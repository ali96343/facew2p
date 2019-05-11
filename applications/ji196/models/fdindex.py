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
    db.dindex.insert( f0= 'aa2470', f1= '(2470)Dashboard 1')
    db.dindex.insert( f0= 'aa2472', f1= '(2472)Dashboard 2')
    db.dindex.insert( f0= 'aa2474', f1= '(2474)Dashboard 3')
    db.dindex.insert( f0= 'aa2476', f1= '(2476)Dashboard 4')
    db.dindex.insert( f0= 'aa2482', f1= '(2482)Login')
    db.dindex.insert( f0= 'aa2484', f1= '(2484)Register')
    db.dindex.insert( f0= 'aa2486', f1= '(2486)Forget Password')
    db.dindex.insert( f0= 'aa2488', f1= '(2488)Button')
    db.dindex.insert( f0= 'aa2490', f1= '(2490)Badges')
    db.dindex.insert( f0= 'aa2492', f1= '(2492)Tabs')
    db.dindex.insert( f0= 'aa2494', f1= '(2494)Cards')
    db.dindex.insert( f0= 'aa2496', f1= '(2496)Alerts')
    db.dindex.insert( f0= 'aa2498', f1= '(2498)Progress Bars')
    db.dindex.insert( f0= 'aa2500', f1= '(2500)Modals')
    db.dindex.insert( f0= 'aa2502', f1= '(2502)Switchs')
    db.dindex.insert( f0= 'aa2504', f1= '(2504)Grids')
    db.dindex.insert( f0= 'aa2506', f1= '(2506)Fontawesome Icon')
    db.dindex.insert( f0= 'aa2508', f1= '(2508)Typography')
    db.dindex.insert( f0= 'aa2511', f1= '(2511)Dashboard 1')
    db.dindex.insert( f0= 'aa2513', f1= '(2513)Dashboard 2')
    db.dindex.insert( f0= 'aa2515', f1= '(2515)Dashboard 3')
    db.dindex.insert( f0= 'aa2517', f1= '(2517)Dashboard 4')
    db.dindex.insert( f0= 'aa2523', f1= '(2523)Login')
    db.dindex.insert( f0= 'aa2525', f1= '(2525)Register')
    db.dindex.insert( f0= 'aa2527', f1= '(2527)Forget Password')
    db.dindex.insert( f0= 'aa2529', f1= '(2529)Button')
    db.dindex.insert( f0= 'aa2531', f1= '(2531)Badges')
    db.dindex.insert( f0= 'aa2533', f1= '(2533)Tabs')
    db.dindex.insert( f0= 'aa2535', f1= '(2535)Cards')
    db.dindex.insert( f0= 'aa2537', f1= '(2537)Alerts')
    db.dindex.insert( f0= 'aa2539', f1= '(2539)Progress Bars')
    db.dindex.insert( f0= 'aa2541', f1= '(2541)Modals')
    db.dindex.insert( f0= 'aa2543', f1= '(2543)Switchs')
    db.dindex.insert( f0= 'aa2545', f1= '(2545)Grids')
    db.dindex.insert( f0= 'aa2547', f1= '(2547)Fontawesome Icon')
    db.dindex.insert( f0= 'aa2549', f1= '(2549)Typography')
    db.dindex.insert( f0= 'pb2550', f1= '(2550)Search for datas &amp; reports...')
    db.dindex.insert( f0= 'sx2551', f1= '(2551)1')
    db.dindex.insert( f0= 'pa2552', f1= '(2552)You have 2 news message')
    db.dindex.insert( f0= 'hh2554', f1= '(2554)Michelle Moreno')
    db.dindex.insert( f0= 'pa2555', f1= '(2555)Have sent a photo')
    db.dindex.insert( f0= 'sx2556', f1= '(2556)3 min ago')
    db.dindex.insert( f0= 'hh2558', f1= '(2558)Diane Myers')
    db.dindex.insert( f0= 'pa2559', f1= '(2559)You are now connected on message')
    db.dindex.insert( f0= 'sx2560', f1= '(2560)Yesterday')
    db.dindex.insert( f0= 'aa2561', f1= '(2561)View all messages')
    db.dindex.insert( f0= 'sx2562', f1= '(2562)1')
    db.dindex.insert( f0= 'pa2563', f1= '(2563)You have 3 New Emails')
    db.dindex.insert( f0= 'pa2565', f1= '(2565)Meeting about new dashboard...')
    db.dindex.insert( f0= 'sp2566', f1= '(2566)Cynthia Harvey, 3 min ago')
    db.dindex.insert( f0= 'pa2568', f1= '(2568)Meeting about new dashboard...')
    db.dindex.insert( f0= 'sp2569', f1= '(2569)Cynthia Harvey, Yesterday')
    db.dindex.insert( f0= 'pa2571', f1= '(2571)Meeting about new dashboard...')
    db.dindex.insert( f0= 'sp2572', f1= '(2572)Cynthia Harvey, April 12,,2018')
    db.dindex.insert( f0= 'aa2573', f1= '(2573)See all emails')
    db.dindex.insert( f0= 'sx2574', f1= '(2574)3')
    db.dindex.insert( f0= 'pa2575', f1= '(2575)You have 3 Notifications')
    db.dindex.insert( f0= 'pa2576', f1= '(2576)You got a email notification')
    db.dindex.insert( f0= 'sx2577', f1= '(2577)April 12, 2018 06:50')
    db.dindex.insert( f0= 'pa2578', f1= '(2578)Your account has been blocked')
    db.dindex.insert( f0= 'sx2579', f1= '(2579)April 12, 2018 06:50')
    db.dindex.insert( f0= 'pa2580', f1= '(2580)You got a new file')
    db.dindex.insert( f0= 'sx2581', f1= '(2581)April 12, 2018 06:50')
    db.dindex.insert( f0= 'aa2582', f1= '(2582)All notifications')
    db.dindex.insert( f0= 'aa2584', f1= '(2584)john doe')
    db.dindex.insert( f0= 'aa2586', f1= '(2586)john doe')
    db.dindex.insert( f0= 'sx2587', f1= '(2587)johndoe@example.com')
    db.dindex.insert( f0= 'hb2588', f1= '(2588)overview')
    db.dindex.insert( f0= 'hh2589', f1= '(2589)10368')
    db.dindex.insert( f0= 'sp2590', f1= '(2590)members online')
    db.dindex.insert( f0= 'hh2591', f1= '(2591)388,688')
    db.dindex.insert( f0= 'sp2592', f1= '(2592)items solid')
    db.dindex.insert( f0= 'hh2593', f1= '(2593)1,086')
    db.dindex.insert( f0= 'sp2594', f1= '(2594)this week')
    db.dindex.insert( f0= 'hh2595', f1= '(2595)$1,060,386')
    db.dindex.insert( f0= 'sp2596', f1= '(2596)total earnings')
    db.dindex.insert( f0= 'hc2597', f1= '(2597)recent reports')
    db.dindex.insert( f0= 'sp2598', f1= '(2598)products')
    db.dindex.insert( f0= 'sp2599', f1= '(2599)services')
    db.dindex.insert( f0= 'sx2600', f1= '(2600)25%')
    db.dindex.insert( f0= 'sx2601', f1= '(2601)products')
    db.dindex.insert( f0= 'sx2602', f1= '(2602)10%')
    db.dindex.insert( f0= 'sx2603', f1= '(2603)services')
    db.dindex.insert( f0= 'hc2604', f1= '(2604)char by %')
    db.dindex.insert( f0= 'sp2605', f1= '(2605)products')
    db.dindex.insert( f0= 'sp2606', f1= '(2606)services')
    db.dindex.insert( f0= 'hb2607', f1= '(2607)Earnings By Items')
    db.dindex.insert( f0= 'hb2627', f1= '(2627)Top countries')
    db.dindex.insert( f0= 'pa2636', f1= '(2636)Tasks for John Doe')
    db.dindex.insert( f0= 'aa2637', f1= '(2637)Meeting about plan for Admin Template 2018')
    db.dindex.insert( f0= 'sx2638', f1= '(2638)10:00 AM')
    db.dindex.insert( f0= 'aa2639', f1= '(2639)Create new task for Dashboard')
    db.dindex.insert( f0= 'sx2640', f1= '(2640)11:00 AM')
    db.dindex.insert( f0= 'aa2641', f1= '(2641)Meeting about plan for Admin Template 2018')
    db.dindex.insert( f0= 'sx2642', f1= '(2642)02:00 PM')
    db.dindex.insert( f0= 'aa2643', f1= '(2643)Create new task for Dashboard')
    db.dindex.insert( f0= 'sx2644', f1= '(2644)03:30 PM')
    db.dindex.insert( f0= 'aa2645', f1= '(2645)Meeting about plan for Admin Template 2018')
    db.dindex.insert( f0= 'sx2646', f1= '(2646)10:00 AM')
    db.dindex.insert( f0= 'aa2647', f1= '(2647)Create new task for Dashboard')
    db.dindex.insert( f0= 'sx2648', f1= '(2648)11:00 AM')
    db.dindex.insert( f0= 'bu2649', f1= '(2649)load more')
    db.dindex.insert( f0= 'sp2651', f1= '(2651)2')
    db.dindex.insert( f0= 'he2653', f1= '(2653)John Smith')
    db.dindex.insert( f0= 'pa2654', f1= '(2654)Have sent a photo')
    db.dindex.insert( f0= 'sp2655', f1= '(2655)12 Min ago')
    db.dindex.insert( f0= 'he2657', f1= '(2657)Nicholas Martinez')
    db.dindex.insert( f0= 'pa2658', f1= '(2658)You are now connected on message')
    db.dindex.insert( f0= 'sp2659', f1= '(2659)11:00 PM')
    db.dindex.insert( f0= 'he2661', f1= '(2661)Michelle Sims')
    db.dindex.insert( f0= 'pa2662', f1= '(2662)Lorem ipsum dolor sit amet')
    db.dindex.insert( f0= 'sp2663', f1= '(2663)Yesterday')
    db.dindex.insert( f0= 'he2665', f1= '(2665)Michelle Sims')
    db.dindex.insert( f0= 'pa2666', f1= '(2666)Purus feugiat finibus')
    db.dindex.insert( f0= 'sp2667', f1= '(2667)Sunday')
    db.dindex.insert( f0= 'he2669', f1= '(2669)Michelle Sims')
    db.dindex.insert( f0= 'pa2670', f1= '(2670)Lorem ipsum dolor sit amet')
    db.dindex.insert( f0= 'sp2671', f1= '(2671)Yesterday')
    db.dindex.insert( f0= 'he2673', f1= '(2673)Michelle Sims')
    db.dindex.insert( f0= 'pa2674', f1= '(2674)Purus feugiat finibus')
    db.dindex.insert( f0= 'sp2675', f1= '(2675)Sunday')
    db.dindex.insert( f0= 'bu2676', f1= '(2676)load more')
    db.dindex.insert( f0= 'aa2678', f1= '(2678)John Smith')
    db.dindex.insert( f0= 'sx2679', f1= '(2679)12 Min ago')
    db.dindex.insert( f0= 'di2681', f1= '(2681)Lorem ipsum dolor sit amet, consectetur adipiscing elit non iaculis')
    db.dindex.insert( f0= 'di2682', f1= '(2682)Donec tempor, sapien ac viverra')
    db.dindex.insert( f0= 'sx2683', f1= '(2683)30 Sec ago')
    db.dindex.insert( f0= 'di2684', f1= '(2684)Lorem ipsum dolor sit amet, consectetur adipiscing elit non iaculis')
    db.dindex.insert( f0= 'pb2685', f1= '(2685)Type a message')
    db.dindex.insert( f0= 'pc2686', f1= '(2686).')
    db.dindex.insert( f0= 'pf2687', f1= '(2687)Copyright  2018 Colorlib. All rights reserved. Template by')
    db.dindex.insert( f0= 'aa2688', f1= '(2688)Colorlib')
    db.commit()
#
