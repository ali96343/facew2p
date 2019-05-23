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
    db.dindex.insert( f0= 'hc2547', f1= '(2547)UI elements')
    db.dindex.insert( f0= 'aa2549', f1= '(2549)Buttons')
    db.dindex.insert( f0= 'aa2551', f1= '(2551)Badges')
    db.dindex.insert( f0= 'aa2553', f1= '(2553)Tabs')
    db.dindex.insert( f0= 'aa2555', f1= '(2555)Social Buttons')
    db.dindex.insert( f0= 'aa2557', f1= '(2557)Cards')
    db.dindex.insert( f0= 'aa2559', f1= '(2559)Alerts')
    db.dindex.insert( f0= 'aa2561', f1= '(2561)Progress Bars')
    db.dindex.insert( f0= 'aa2563', f1= '(2563)Modals')
    db.dindex.insert( f0= 'aa2565', f1= '(2565)Switches')
    db.dindex.insert( f0= 'aa2567', f1= '(2567)Grids')
    db.dindex.insert( f0= 'aa2569', f1= '(2569)Typography')
    db.dindex.insert( f0= 'aa2571', f1= '(2571)Basic Table')
    db.dindex.insert( f0= 'aa2573', f1= '(2573)Data Table')
    db.dindex.insert( f0= 'aa2575', f1= '(2575)Basic Form')
    db.dindex.insert( f0= 'aa2577', f1= '(2577)Advanced Form')
    db.dindex.insert( f0= 'hc2578', f1= '(2578)Icons')
    db.dindex.insert( f0= 'aa2580', f1= '(2580)Font Awesome')
    db.dindex.insert( f0= 'aa2582', f1= '(2582)Themefy Icons')
    db.dindex.insert( f0= 'aa2585', f1= '(2585)Chart JS')
    db.dindex.insert( f0= 'aa2587', f1= '(2587)Flot Chart')
    db.dindex.insert( f0= 'aa2589', f1= '(2589)Peity Chart')
    db.dindex.insert( f0= 'aa2591', f1= '(2591)Google Maps')
    db.dindex.insert( f0= 'aa2593', f1= '(2593)Vector Maps')
    db.dindex.insert( f0= 'hc2594', f1= '(2594)Extras')
    db.dindex.insert( f0= 'aa2596', f1= '(2596)Login')
    db.dindex.insert( f0= 'aa2598', f1= '(2598)Register')
    db.dindex.insert( f0= 'aa2600', f1= '(2600)Forget Pass')
    db.dindex.insert( f0= 'pb2601', f1= '(2601)Search ...')
    db.dindex.insert( f0= 'pc2602', f1= '(2602)You have 3 Notification')
    db.dindex.insert( f0= 'pc2603', f1= '(2603)You have 4 Mails')
    db.dindex.insert( f0= 'sx2605', f1= '(2605)Jonathan Smith')
    db.dindex.insert( f0= 'sx2606', f1= '(2606)Just now')
    db.dindex.insert( f0= 'pa2607', f1= '(2607)Hello, this is an example msg')
    db.dindex.insert( f0= 'sx2609', f1= '(2609)Jack Sanders')
    db.dindex.insert( f0= 'sx2610', f1= '(2610)5 minutes ago')
    db.dindex.insert( f0= 'pa2611', f1= '(2611)Lorem ipsum dolor sit amet, consectetur')
    db.dindex.insert( f0= 'sx2613', f1= '(2613)Cheryl Wheeler')
    db.dindex.insert( f0= 'sx2614', f1= '(2614)10 minutes ago')
    db.dindex.insert( f0= 'pa2615', f1= '(2615)Hello, this is an example msg')
    db.dindex.insert( f0= 'sx2617', f1= '(2617)Rachel Santos')
    db.dindex.insert( f0= 'sx2618', f1= '(2618)15 minutes ago')
    db.dindex.insert( f0= 'pa2619', f1= '(2619)Lorem ipsum dolor sit amet, consectetur')
    db.dindex.insert( f0= 'sx2621', f1= '(2621)13')
    db.dindex.insert( f0= 'hh2622', f1= '(2622)Dashboard')
    db.dindex.insert( f0= 'lb2623', f1= '(2623)Dashboard')
    db.dindex.insert( f0= 'sx2624', f1= '(2624)Success')
    db.dindex.insert( f0= 'sx2625', f1= '(2625)&times;')
    db.dindex.insert( f0= 'aa2626', f1= '(2626)Action')
    db.dindex.insert( f0= 'aa2627', f1= '(2627)Another action')
    db.dindex.insert( f0= 'aa2628', f1= '(2628)Something else here')
    db.dindex.insert( f0= 'sx2629', f1= '(2629)10468')
    db.dindex.insert( f0= 'pc2630', f1= '(2630)Members online')
    db.dindex.insert( f0= 'aa2631', f1= '(2631)Action')
    db.dindex.insert( f0= 'aa2632', f1= '(2632)Another action')
    db.dindex.insert( f0= 'aa2633', f1= '(2633)Something else here')
    db.dindex.insert( f0= 'sx2634', f1= '(2634)10468')
    db.dindex.insert( f0= 'pc2635', f1= '(2635)Members online')
    db.dindex.insert( f0= 'aa2636', f1= '(2636)Action')
    db.dindex.insert( f0= 'aa2637', f1= '(2637)Another action')
    db.dindex.insert( f0= 'aa2638', f1= '(2638)Something else here')
    db.dindex.insert( f0= 'sx2639', f1= '(2639)10468')
    db.dindex.insert( f0= 'pc2640', f1= '(2640)Members online')
    db.dindex.insert( f0= 'aa2641', f1= '(2641)Action')
    db.dindex.insert( f0= 'aa2642', f1= '(2642)Another action')
    db.dindex.insert( f0= 'aa2643', f1= '(2643)Something else here')
    db.dindex.insert( f0= 'sx2644', f1= '(2644)10468')
    db.dindex.insert( f0= 'pc2645', f1= '(2645)Members online')
    db.dindex.insert( f0= 'sx2646', f1= '(2646)40')
    db.dindex.insert( f0= 'sp2647', f1= '(2647)friends')
    db.dindex.insert( f0= 'sx2648', f1= '(2648)450')
    db.dindex.insert( f0= 'sp2649', f1= '(2649)feeds')
    db.dindex.insert( f0= 'sx2650', f1= '(2650)30')
    db.dindex.insert( f0= 'sp2651', f1= '(2651)friends')
    db.dindex.insert( f0= 'sx2652', f1= '(2652)450')
    db.dindex.insert( f0= 'sp2653', f1= '(2653)tweets')
    db.dindex.insert( f0= 'sx2654', f1= '(2654)40')
    db.dindex.insert( f0= 'sp2655', f1= '(2655)contacts')
    db.dindex.insert( f0= 'sx2656', f1= '(2656)250')
    db.dindex.insert( f0= 'sp2657', f1= '(2657)feeds')
    db.dindex.insert( f0= 'sx2658', f1= '(2658)94')
    db.dindex.insert( f0= 'sp2659', f1= '(2659)followers')
    db.dindex.insert( f0= 'sx2660', f1= '(2660)92')
    db.dindex.insert( f0= 'sp2661', f1= '(2661)circles')
    db.dindex.insert( f0= 'hd2662', f1= '(2662)Traffic')
    db.dindex.insert( f0= 'di2663', f1= '(2663)October 2017')
    db.dindex.insert( f0= 'di2664', f1= '(2664)Visits')
    db.dindex.insert( f0= 'sp2665', f1= '(2665)29.703 Users (40%)')
    db.dindex.insert( f0= 'di2666', f1= '(2666)Unique')
    db.dindex.insert( f0= 'sp2667', f1= '(2667)24.093 Users (20%)')
    db.dindex.insert( f0= 'di2668', f1= '(2668)Pageviews')
    db.dindex.insert( f0= 'sp2669', f1= '(2669)78.706 Views (60%)')
    db.dindex.insert( f0= 'di2670', f1= '(2670)New Users')
    db.dindex.insert( f0= 'sp2671', f1= '(2671)22.123 Users (80%)')
    db.dindex.insert( f0= 'di2672', f1= '(2672)Bounce Rate')
    db.dindex.insert( f0= 'sp2673', f1= '(2673)40.15%')
    db.dindex.insert( f0= 'hb2675', f1= '(2675)Jim Doe')
    db.dindex.insert( f0= 'pc2676', f1= '(2676)Project Manager')
    db.dindex.insert( f0= 'hh2677', f1= '(2677)750')
    db.dindex.insert( f0= 'hh2678', f1= '(2678)865')
    db.dindex.insert( f0= 'hh2679', f1= '(2679)3645')
    db.dindex.insert( f0= 'pb2680', f1= '(2680)Write your Tweet and Enter')
    db.dindex.insert( f0= 'di2681', f1= '(2681)Total Profit')
    db.dindex.insert( f0= 'di2682', f1= '(2682)1,012')
    db.dindex.insert( f0= 'di2683', f1= '(2683)New Customer')
    db.dindex.insert( f0= 'di2684', f1= '(2684)961')
    db.dindex.insert( f0= 'di2685', f1= '(2685)Active Projects')
    db.dindex.insert( f0= 'di2686', f1= '(2686)770')
    db.dindex.insert( f0= 'hh2687', f1= '(2687)World')
    db.commit()
#
