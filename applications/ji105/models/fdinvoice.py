#
# table for controller: invoice
#

from gluon.contrib.populate import populate

db.define_table('dinvoice', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dinvoice.id ).count():
    db.dinvoice.insert( f0= 'sp2495', f1= '(2495)outdated')
    db.dinvoice.insert( f0= 'pc2496', f1= '(2496)to improve your experience.')
    db.dinvoice.insert( f0= 'aa2497', f1= '(2497)upgrade your browser')
    db.dinvoice.insert( f0= 'hh2499', f1= '(2499)Messages')
    db.dinvoice.insert( f0= 'hh2501', f1= '(2501)David Belle')
    db.dinvoice.insert( f0= 'pa2502', f1= '(2502)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinvoice.insert( f0= 'hh2504', f1= '(2504)Jonathan Morris')
    db.dinvoice.insert( f0= 'pa2505', f1= '(2505)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinvoice.insert( f0= 'hh2507', f1= '(2507)Fredric Mitchell')
    db.dinvoice.insert( f0= 'pa2508', f1= '(2508)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinvoice.insert( f0= 'hh2510', f1= '(2510)David Belle')
    db.dinvoice.insert( f0= 'pa2511', f1= '(2511)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinvoice.insert( f0= 'hh2513', f1= '(2513)Glenn Jecobs')
    db.dinvoice.insert( f0= 'pa2514', f1= '(2514)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinvoice.insert( f0= 'aa2515', f1= '(2515)View All')
    db.dinvoice.insert( f0= 'hh2516', f1= '(2516)Notification')
    db.dinvoice.insert( f0= 'hh2518', f1= '(2518)David Belle')
    db.dinvoice.insert( f0= 'pa2519', f1= '(2519)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinvoice.insert( f0= 'hh2521', f1= '(2521)Jonathan Morris')
    db.dinvoice.insert( f0= 'pa2522', f1= '(2522)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinvoice.insert( f0= 'hh2524', f1= '(2524)Fredric Mitchell')
    db.dinvoice.insert( f0= 'pa2525', f1= '(2525)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinvoice.insert( f0= 'hh2527', f1= '(2527)David Belle')
    db.dinvoice.insert( f0= 'pa2528', f1= '(2528)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinvoice.insert( f0= 'hh2530', f1= '(2530)Glenn Jecobs')
    db.dinvoice.insert( f0= 'pa2531', f1= '(2531)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dinvoice.insert( f0= 'aa2532', f1= '(2532)View All')
    db.dinvoice.insert( f0= 'hh2533', f1= '(2533)Tasks')
    db.dinvoice.insert( f0= 'pa2534', f1= '(2534)HTML5 Validation Report')
    db.dinvoice.insert( f0= 'sp2535', f1= '(2535)95%')
    db.dinvoice.insert( f0= 'pa2536', f1= '(2536)Google Chrome Extension')
    db.dinvoice.insert( f0= 'sp2537', f1= '(2537)85%')
    db.dinvoice.insert( f0= 'pa2538', f1= '(2538)Social Internet Projects')
    db.dinvoice.insert( f0= 'sp2539', f1= '(2539)93%')
    db.dinvoice.insert( f0= 'pa2540', f1= '(2540)Bootstrap Admin Template')
    db.dinvoice.insert( f0= 'sp2541', f1= '(2541)93%')
    db.dinvoice.insert( f0= 'pa2542', f1= '(2542)Youtube Client App')
    db.dinvoice.insert( f0= 'sp2543', f1= '(2543)93%')
    db.dinvoice.insert( f0= 'aa2544', f1= '(2544)View All')
    db.dinvoice.insert( f0= 'hh2545', f1= '(2545)Chat')
    db.dinvoice.insert( f0= 'pb2546', f1= '(2546)Search People')
    db.dinvoice.insert( f0= 'hh2548', f1= '(2548)David Belle')
    db.dinvoice.insert( f0= 'pa2549', f1= '(2549)Available')
    db.dinvoice.insert( f0= 'hh2551', f1= '(2551)Jonathan Morris')
    db.dinvoice.insert( f0= 'pa2552', f1= '(2552)Last seen 3 hours ago')
    db.dinvoice.insert( f0= 'hh2554', f1= '(2554)Fredric Mitchell')
    db.dinvoice.insert( f0= 'pa2555', f1= '(2555)Last seen 2 minutes ago')
    db.dinvoice.insert( f0= 'hh2557', f1= '(2557)David Belle')
    db.dinvoice.insert( f0= 'pa2558', f1= '(2558)Available')
    db.dinvoice.insert( f0= 'hh2560', f1= '(2560)Glenn Jecobs')
    db.dinvoice.insert( f0= 'pa2561', f1= '(2561)Available')
    db.dinvoice.insert( f0= 'aa2562', f1= '(2562)View All')
    db.dinvoice.insert( f0= 'aa2563', f1= '(2563)Home')
    db.dinvoice.insert( f0= 'aa2565', f1= '(2565)Dashboard One')
    db.dinvoice.insert( f0= 'aa2567', f1= '(2567)Dashboard Two')
    db.dinvoice.insert( f0= 'aa2569', f1= '(2569)Dashboard Three')
    db.dinvoice.insert( f0= 'aa2571', f1= '(2571)Dashboard Four')
    db.dinvoice.insert( f0= 'aa2573', f1= '(2573)Analytics')
    db.dinvoice.insert( f0= 'aa2575', f1= '(2575)Widgets')
    db.dinvoice.insert( f0= 'aa2576', f1= '(2576)Email')
    db.dinvoice.insert( f0= 'aa2578', f1= '(2578)Inbox')
    db.dinvoice.insert( f0= 'aa2580', f1= '(2580)View Email')
    db.dinvoice.insert( f0= 'aa2582', f1= '(2582)Compose Email')
    db.dinvoice.insert( f0= 'aa2583', f1= '(2583)Interface')
    db.dinvoice.insert( f0= 'aa2585', f1= '(2585)Animations')
    db.dinvoice.insert( f0= 'aa2587', f1= '(2587)Google Map')
    db.dinvoice.insert( f0= 'aa2589', f1= '(2589)Data Maps')
    db.dinvoice.insert( f0= 'aa2591', f1= '(2591)Code Editor')
    db.dinvoice.insert( f0= 'aa2593', f1= '(2593)Images Cropper')
    db.dinvoice.insert( f0= 'aa2595', f1= '(2595)Wizard')
    db.dinvoice.insert( f0= 'aa2596', f1= '(2596)Charts')
    db.dinvoice.insert( f0= 'aa2598', f1= '(2598)Flot Charts')
    db.dinvoice.insert( f0= 'aa2600', f1= '(2600)Bar Charts')
    db.dinvoice.insert( f0= 'aa2602', f1= '(2602)Line Charts')
    db.dinvoice.insert( f0= 'aa2604', f1= '(2604)Area Charts')
    db.dinvoice.insert( f0= 'aa2605', f1= '(2605)Tables')
    db.dinvoice.insert( f0= 'aa2607', f1= '(2607)Normal Table')
    db.dinvoice.insert( f0= 'aa2609', f1= '(2609)Data Table')
    db.dinvoice.insert( f0= 'aa2610', f1= '(2610)Forms')
    db.dinvoice.insert( f0= 'aa2612', f1= '(2612)Form Elements')
    db.dinvoice.insert( f0= 'aa2614', f1= '(2614)Form Components')
    db.dinvoice.insert( f0= 'aa2616', f1= '(2616)Form Examples')
    db.dinvoice.insert( f0= 'aa2617', f1= '(2617)App views')
    db.dinvoice.insert( f0= 'aa2619', f1= '(2619)Notifications')
    db.dinvoice.insert( f0= 'aa2621', f1= '(2621)Alerts')
    db.dinvoice.insert( f0= 'aa2623', f1= '(2623)Modals')
    db.dinvoice.insert( f0= 'aa2625', f1= '(2625)Buttons')
    db.dinvoice.insert( f0= 'aa2627', f1= '(2627)Tabs')
    db.dinvoice.insert( f0= 'aa2629', f1= '(2629)Accordion')
    db.dinvoice.insert( f0= 'aa2631', f1= '(2631)Dialogs')
    db.dinvoice.insert( f0= 'aa2633', f1= '(2633)Popovers')
    db.dinvoice.insert( f0= 'aa2635', f1= '(2635)Tooltips')
    db.dinvoice.insert( f0= 'aa2637', f1= '(2637)Dropdowns')
    db.dinvoice.insert( f0= 'aa2638', f1= '(2638)Pages')
    db.dinvoice.insert( f0= 'aa2640', f1= '(2640)Contact')
    db.dinvoice.insert( f0= 'aa2642', f1= '(2642)Invoice')
    db.dinvoice.insert( f0= 'aa2644', f1= '(2644)Typography')
    db.dinvoice.insert( f0= 'aa2646', f1= '(2646)Color')
    db.dinvoice.insert( f0= 'aa2648', f1= '(2648)Login Register')
    db.dinvoice.insert( f0= 'aa2650', f1= '(2650)404 Page')
    db.dinvoice.insert( f0= 'aa2652', f1= '(2652)Dashboard One')
    db.dinvoice.insert( f0= 'aa2654', f1= '(2654)Dashboard Two')
    db.dinvoice.insert( f0= 'aa2656', f1= '(2656)Dashboard Three')
    db.dinvoice.insert( f0= 'aa2658', f1= '(2658)Dashboard Four')
    db.dinvoice.insert( f0= 'aa2660', f1= '(2660)Analytics')
    db.dinvoice.insert( f0= 'aa2662', f1= '(2662)Widgets')
    db.dinvoice.insert( f0= 'aa2664', f1= '(2664)Inbox')
    db.dinvoice.insert( f0= 'aa2666', f1= '(2666)View Email')
    db.dinvoice.insert( f0= 'aa2668', f1= '(2668)Compose Email')
    db.dinvoice.insert( f0= 'aa2670', f1= '(2670)Animations')
    db.dinvoice.insert( f0= 'aa2672', f1= '(2672)Google Map')
    db.dinvoice.insert( f0= 'aa2674', f1= '(2674)Data Maps')
    db.dinvoice.insert( f0= 'aa2676', f1= '(2676)Code Editor')
    db.dinvoice.insert( f0= 'aa2678', f1= '(2678)Images Cropper')
    db.dinvoice.insert( f0= 'aa2680', f1= '(2680)Wizard')
    db.dinvoice.insert( f0= 'aa2682', f1= '(2682)Flot Charts')
    db.dinvoice.insert( f0= 'aa2684', f1= '(2684)Bar Charts')
    db.dinvoice.insert( f0= 'aa2686', f1= '(2686)Line Charts')
    db.dinvoice.insert( f0= 'aa2688', f1= '(2688)Area Charts')
    db.dinvoice.insert( f0= 'aa2690', f1= '(2690)Normal Table')
    db.dinvoice.insert( f0= 'aa2692', f1= '(2692)Data Table')
    db.dinvoice.insert( f0= 'aa2694', f1= '(2694)Form Elements')
    db.dinvoice.insert( f0= 'aa2696', f1= '(2696)Form Components')
    db.dinvoice.insert( f0= 'aa2698', f1= '(2698)Form Examples')
    db.dinvoice.insert( f0= 'aa2700', f1= '(2700)Notifications')
    db.dinvoice.insert( f0= 'aa2702', f1= '(2702)Alerts')
    db.dinvoice.insert( f0= 'aa2704', f1= '(2704)Modals')
    db.dinvoice.insert( f0= 'aa2706', f1= '(2706)Buttons')
    db.dinvoice.insert( f0= 'aa2708', f1= '(2708)Tabs')
    db.dinvoice.insert( f0= 'aa2710', f1= '(2710)Accordion')
    db.dinvoice.insert( f0= 'aa2712', f1= '(2712)Dialogs')
    db.dinvoice.insert( f0= 'aa2714', f1= '(2714)Popovers')
    db.dinvoice.insert( f0= 'aa2716', f1= '(2716)Tooltips')
    db.dinvoice.insert( f0= 'aa2718', f1= '(2718)Dropdowns')
    db.dinvoice.insert( f0= 'aa2720', f1= '(2720)Contact')
    db.dinvoice.insert( f0= 'aa2722', f1= '(2722)Invoice')
    db.dinvoice.insert( f0= 'aa2724', f1= '(2724)Typography')
    db.dinvoice.insert( f0= 'aa2726', f1= '(2726)Color')
    db.dinvoice.insert( f0= 'aa2728', f1= '(2728)Login Register')
    db.dinvoice.insert( f0= 'aa2730', f1= '(2730)404 Page')
    db.dinvoice.insert( f0= 'hh2731', f1= '(2731)Invoice')
    db.dinvoice.insert( f0= 'sx2732', f1= '(2732)Admin Template')
    db.dinvoice.insert( f0= 'pf2733', f1= '(2733)Welcome to Notika')
    db.dinvoice.insert( f0= 'sp2735', f1= '(2735)Invoice from')
    db.dinvoice.insert( f0= 'hh2736', f1= '(2736)David Designs LLC')
    db.dinvoice.insert( f0= 'pa2737', f1= '(2737)44, Qube Towers uttara Media City, Dubai, Bangladesh')
    db.dinvoice.insert( f0= 'sp2738', f1= '(2738)01962067309')
    db.dinvoice.insert( f0= 'sp2739', f1= '(2739)David@notika.com')
    db.dinvoice.insert( f0= 'sp2740', f1= '(2740)Invoice to')
    db.dinvoice.insert( f0= 'hh2741', f1= '(2741)Mallinda Hollaway')
    db.dinvoice.insert( f0= 'pa2742', f1= '(2742)10098 ABC Towers Uttara Silicon Oasis, Dubai, Bangladesh.')
    db.dinvoice.insert( f0= 'sp2743', f1= '(2743)01955239099')
    db.dinvoice.insert( f0= 'sp2744', f1= '(2744)Mall@notika.com')
    db.dinvoice.insert( f0= 'hh2745', f1= '(2745)456656')
    db.dinvoice.insert( f0= 'sp2746', f1= '(2746)Date')
    db.dinvoice.insert( f0= 'hh2747', f1= '(2747)20/03/2018')
    db.dinvoice.insert( f0= 'sp2748', f1= '(2748)Whatever')
    db.dinvoice.insert( f0= 'hh2749', f1= '(2749)472-000')
    db.dinvoice.insert( f0= 'sp2750', f1= '(2750)Grand Total')
    db.dinvoice.insert( f0= 'hh2751', f1= '(2751)$25,980')
    db.dinvoice.insert( f0= 'hh2752', f1= '(2752)Remarks')
    db.dinvoice.insert( f0= 'pa2753', f1= '(2753)Ornare non tortor. Nam quis ipsum vitae dolor porttitor interdum. Curabitur faucibus erat vel ante fermentum lacinia. Integer porttitor laoreet suscipit. Sed cursus cursus massa ut pellentesque. Phasellus vehicula dictum arcu, eu interdum massa bibendum. Ornare non tortor. Nam quis ipsum vitae dolor porttitor interdum. Curabitur faucibus erat vel ante fermentum lacinia. Integer porttitor laoreet suscipit. Sed cursus cursus massa ut pellentesque. Phasellus vehicula dictum arcu, eu interdum massa bibendum.')
    db.dinvoice.insert( f0= 'hh2754', f1= '(2754)Notika For Your Business')
    db.dinvoice.insert( f0= 'pc2755', f1= '(2755)Ornare non tortor. Nam quis ipsum vitae dolor porttitor interdum. Curabitur faucibus erat vel ante fermentum lacinia. Integer porttitor laoreet suscipit. Sed cursus cursus massa ut pellentesque. Phasellus vehicula dictum arcu, eu interdum massa bibendum. Ornare non tortor. Nam quis ipsum vitae dolor porttitor interdum. Curabitur faucibus erat vel ante fermentum lacinia. Integer porttitor laoreet suscipit. Sed cursus cursus massa ut pellentesque. Phasellus vehicula dictum arcu, eu interdum massa bibendum.')
    db.commit()
#
