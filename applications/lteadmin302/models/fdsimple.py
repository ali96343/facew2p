#
# table for controller: simple
#

from gluon.contrib.populate import populate

db.define_table('dsimple', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dsimple.id ).count():
    db.dsimple.insert( f0= 'aa2502', f1= '(2502)Home')
    db.dsimple.insert( f0= 'aa2503', f1= '(2503)Contact')
    db.dsimple.insert( f0= 'pb2504', f1= '(2504)Search')
    db.dsimple.insert( f0= 'sx2505', f1= '(2505)3')
    db.dsimple.insert( f0= 'pc2507', f1= '(2507)Call me whenever you can...')
    db.dsimple.insert( f0= 'pc2508', f1= '(2508)4 Hours Ago')
    db.dsimple.insert( f0= 'pc2510', f1= '(2510)I got your message bro')
    db.dsimple.insert( f0= 'pc2511', f1= '(2511)4 Hours Ago')
    db.dsimple.insert( f0= 'pc2513', f1= '(2513)The subject goes here')
    db.dsimple.insert( f0= 'pc2514', f1= '(2514)4 Hours Ago')
    db.dsimple.insert( f0= 'aa2515', f1= '(2515)See All Messages')
    db.dsimple.insert( f0= 'sx2516', f1= '(2516)15 Notifications')
    db.dsimple.insert( f0= 'sx2517', f1= '(2517)3 mins')
    db.dsimple.insert( f0= 'sx2518', f1= '(2518)12 hours')
    db.dsimple.insert( f0= 'sx2519', f1= '(2519)2 days')
    db.dsimple.insert( f0= 'aa2520', f1= '(2520)See All Notifications')
    db.dsimple.insert( f0= 'sx2523', f1= '(2523)AdminLTE 3')
    db.dsimple.insert( f0= 'aa2525', f1= '(2525)Alexander Pierce')
    db.dsimple.insert( f0= 'pa2527', f1= '(2527)Dashboard v1')
    db.dsimple.insert( f0= 'pa2529', f1= '(2529)Dashboard v2')
    db.dsimple.insert( f0= 'pa2531', f1= '(2531)Dashboard v3')
    db.dsimple.insert( f0= 'sx2533', f1= '(2533)New')
    db.dsimple.insert( f0= 'sx2534', f1= '(2534)6')
    db.dsimple.insert( f0= 'pa2536', f1= '(2536)Top Navigation')
    db.dsimple.insert( f0= 'pa2538', f1= '(2538)Top Navigation + Sidebar')
    db.dsimple.insert( f0= 'pa2540', f1= '(2540)Boxed')
    db.dsimple.insert( f0= 'pa2542', f1= '(2542)Fixed Sidebar')
    db.dsimple.insert( f0= 'pa2544', f1= '(2544)Fixed Navbar')
    db.dsimple.insert( f0= 'pa2546', f1= '(2546)Fixed Footer')
    db.dsimple.insert( f0= 'pa2548', f1= '(2548)Collapsed Sidebar')
    db.dsimple.insert( f0= 'pa2550', f1= '(2550)ChartJS')
    db.dsimple.insert( f0= 'pa2552', f1= '(2552)Flot')
    db.dsimple.insert( f0= 'pa2554', f1= '(2554)Inline')
    db.dsimple.insert( f0= 'pa2556', f1= '(2556)General')
    db.dsimple.insert( f0= 'pa2558', f1= '(2558)Icons')
    db.dsimple.insert( f0= 'pa2560', f1= '(2560)Buttons')
    db.dsimple.insert( f0= 'pa2562', f1= '(2562)Sliders')
    db.dsimple.insert( f0= 'pa2564', f1= '(2564)Modals & Alerts')
    db.dsimple.insert( f0= 'pa2566', f1= '(2566)Navbar & Tabs')
    db.dsimple.insert( f0= 'pa2568', f1= '(2568)Timeline')
    db.dsimple.insert( f0= 'pa2570', f1= '(2570)Ribbons')
    db.dsimple.insert( f0= 'pa2572', f1= '(2572)General Elements')
    db.dsimple.insert( f0= 'pa2574', f1= '(2574)Advanced Elements')
    db.dsimple.insert( f0= 'pa2576', f1= '(2576)Editors')
    db.dsimple.insert( f0= 'pa2578', f1= '(2578)Validation')
    db.dsimple.insert( f0= 'pa2580', f1= '(2580)Simple Tables')
    db.dsimple.insert( f0= 'pa2582', f1= '(2582)DataTables')
    db.dsimple.insert( f0= 'pa2584', f1= '(2584)jsGrid')
    db.dsimple.insert( f0= 'lb2585', f1= '(2585)EXAMPLES')
    db.dsimple.insert( f0= 'sx2587', f1= '(2587)2')
    db.dsimple.insert( f0= 'pa2590', f1= '(2590)Inbox')
    db.dsimple.insert( f0= 'pa2592', f1= '(2592)Compose')
    db.dsimple.insert( f0= 'pa2594', f1= '(2594)Read')
    db.dsimple.insert( f0= 'pa2596', f1= '(2596)Invoice')
    db.dsimple.insert( f0= 'pa2598', f1= '(2598)Profile')
    db.dsimple.insert( f0= 'pa2600', f1= '(2600)E-commerce')
    db.dsimple.insert( f0= 'pa2602', f1= '(2602)Projects')
    db.dsimple.insert( f0= 'pa2604', f1= '(2604)Project Add')
    db.dsimple.insert( f0= 'pa2606', f1= '(2606)Project Edit')
    db.dsimple.insert( f0= 'pa2608', f1= '(2608)Project Detail')
    db.dsimple.insert( f0= 'pa2610', f1= '(2610)Contacts')
    db.dsimple.insert( f0= 'pa2612', f1= '(2612)Login')
    db.dsimple.insert( f0= 'pa2614', f1= '(2614)Register')
    db.dsimple.insert( f0= 'pa2616', f1= '(2616)Forgot Password')
    db.dsimple.insert( f0= 'pa2618', f1= '(2618)Recover Password')
    db.dsimple.insert( f0= 'pa2620', f1= '(2620)Lockscreen')
    db.dsimple.insert( f0= 'pa2622', f1= '(2622)Legacy User Menu')
    db.dsimple.insert( f0= 'pa2624', f1= '(2624)Language Menu')
    db.dsimple.insert( f0= 'pa2626', f1= '(2626)Error 404')
    db.dsimple.insert( f0= 'pa2628', f1= '(2628)Error 500')
    db.dsimple.insert( f0= 'pa2630', f1= '(2630)Pace')
    db.dsimple.insert( f0= 'pa2632', f1= '(2632)Blank Page')
    db.dsimple.insert( f0= 'pa2634', f1= '(2634)Starter Page')
    db.dsimple.insert( f0= 'lb2635', f1= '(2635)MISCELLANEOUS')
    db.dsimple.insert( f0= 'pa2636', f1= '(2636)Documentation')
    db.dsimple.insert( f0= 'lb2637', f1= '(2637)MULTI LEVEL EXAMPLE')
    db.dsimple.insert( f0= 'pa2638', f1= '(2638)Level 1')
    db.dsimple.insert( f0= 'pa2639', f1= '(2639)Level 2')
    db.dsimple.insert( f0= 'pa2640', f1= '(2640)Level 3')
    db.dsimple.insert( f0= 'pa2641', f1= '(2641)Level 3')
    db.dsimple.insert( f0= 'pa2642', f1= '(2642)Level 3')
    db.dsimple.insert( f0= 'pa2643', f1= '(2643)Level 2')
    db.dsimple.insert( f0= 'pa2644', f1= '(2644)Level 1')
    db.dsimple.insert( f0= 'lb2645', f1= '(2645)LABELS')
    db.dsimple.insert( f0= 'pc2646', f1= '(2646)Important')
    db.dsimple.insert( f0= 'pa2647', f1= '(2647)Warning')
    db.dsimple.insert( f0= 'pa2648', f1= '(2648)Informational')
    db.dsimple.insert( f0= 'hh2649', f1= '(2649)Simple Tables')
    db.dsimple.insert( f0= 'aa2650', f1= '(2650)Home')
    db.dsimple.insert( f0= 'lb2651', f1= '(2651)Simple Tables')
    db.dsimple.insert( f0= 'hc2652', f1= '(2652)Bordered Table')
    db.dsimple.insert( f0= 'aa2653', f1= '(2653)&laquo;')
    db.dsimple.insert( f0= 'aa2654', f1= '(2654)1')
    db.dsimple.insert( f0= 'aa2655', f1= '(2655)2')
    db.dsimple.insert( f0= 'aa2656', f1= '(2656)3')
    db.dsimple.insert( f0= 'aa2657', f1= '(2657)&raquo;')
    db.dsimple.insert( f0= 'hc2658', f1= '(2658)Condensed Full Width Table')
    db.dsimple.insert( f0= 'hc2659', f1= '(2659)Simple Full Width Table')
    db.dsimple.insert( f0= 'aa2660', f1= '(2660)&laquo;')
    db.dsimple.insert( f0= 'aa2661', f1= '(2661)1')
    db.dsimple.insert( f0= 'aa2662', f1= '(2662)2')
    db.dsimple.insert( f0= 'aa2663', f1= '(2663)3')
    db.dsimple.insert( f0= 'aa2664', f1= '(2664)&raquo;')
    db.dsimple.insert( f0= 'hc2665', f1= '(2665)Striped Full Width Table')
    db.dsimple.insert( f0= 'hc2666', f1= '(2666)Responsive Hover Table')
    db.dsimple.insert( f0= 'pb2667', f1= '(2667)Search')
    db.dsimple.insert( f0= 'sx2668', f1= '(2668)Approved')
    db.dsimple.insert( f0= 'sx2669', f1= '(2669)Pending')
    db.dsimple.insert( f0= 'sx2670', f1= '(2670)Approved')
    db.dsimple.insert( f0= 'sx2671', f1= '(2671)Denied')
    db.dsimple.insert( f0= 'hc2672', f1= '(2672)Fixed Header Table')
    db.dsimple.insert( f0= 'pb2673', f1= '(2673)Search')
    db.dsimple.insert( f0= 'sx2674', f1= '(2674)Approved')
    db.dsimple.insert( f0= 'sx2675', f1= '(2675)Pending')
    db.dsimple.insert( f0= 'sx2676', f1= '(2676)Approved')
    db.dsimple.insert( f0= 'sx2677', f1= '(2677)Denied')
    db.dsimple.insert( f0= 'sx2678', f1= '(2678)Approved')
    db.dsimple.insert( f0= 'sx2679', f1= '(2679)Pending')
    db.dsimple.insert( f0= 'sx2680', f1= '(2680)Approved')
    db.dsimple.insert( f0= 'sx2681', f1= '(2681)Denied')
    db.dsimple.insert( f0= 'bb2682', f1= '(2682)Version')
    db.dsimple.insert( f0= 'aa2683', f1= '(2683)AdminLTE.io')
    db.commit()
#
