#
# table for controller: collapsedIIsidebar
#

from gluon.contrib.populate import populate

db.define_table('dcollapsed0sidebar', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcollapsed0sidebar.id ).count():
    db.dcollapsed0sidebar.insert( f0= 'aa2834', f1= '(2834)Home')
    db.dcollapsed0sidebar.insert( f0= 'aa2835', f1= '(2835)Contact')
    db.dcollapsed0sidebar.insert( f0= 'pb2836', f1= '(2836)Search')
    db.dcollapsed0sidebar.insert( f0= 'sx2837', f1= '(2837)3')
    db.dcollapsed0sidebar.insert( f0= 'pc2839', f1= '(2839)Call me whenever you can...')
    db.dcollapsed0sidebar.insert( f0= 'pc2840', f1= '(2840)4 Hours Ago')
    db.dcollapsed0sidebar.insert( f0= 'pc2842', f1= '(2842)I got your message bro')
    db.dcollapsed0sidebar.insert( f0= 'pc2843', f1= '(2843)4 Hours Ago')
    db.dcollapsed0sidebar.insert( f0= 'pc2845', f1= '(2845)The subject goes here')
    db.dcollapsed0sidebar.insert( f0= 'pc2846', f1= '(2846)4 Hours Ago')
    db.dcollapsed0sidebar.insert( f0= 'aa2847', f1= '(2847)See All Messages')
    db.dcollapsed0sidebar.insert( f0= 'sx2848', f1= '(2848)15 Notifications')
    db.dcollapsed0sidebar.insert( f0= 'sx2849', f1= '(2849)3 mins')
    db.dcollapsed0sidebar.insert( f0= 'sx2850', f1= '(2850)12 hours')
    db.dcollapsed0sidebar.insert( f0= 'sx2851', f1= '(2851)2 days')
    db.dcollapsed0sidebar.insert( f0= 'aa2852', f1= '(2852)See All Notifications')
    db.dcollapsed0sidebar.insert( f0= 'sx2855', f1= '(2855)AdminLTE 3')
    db.dcollapsed0sidebar.insert( f0= 'aa2857', f1= '(2857)Alexander Pierce')
    db.dcollapsed0sidebar.insert( f0= 'pa2859', f1= '(2859)Dashboard v1')
    db.dcollapsed0sidebar.insert( f0= 'pa2861', f1= '(2861)Dashboard v2')
    db.dcollapsed0sidebar.insert( f0= 'pa2863', f1= '(2863)Dashboard v3')
    db.dcollapsed0sidebar.insert( f0= 'sx2865', f1= '(2865)New')
    db.dcollapsed0sidebar.insert( f0= 'sx2866', f1= '(2866)6')
    db.dcollapsed0sidebar.insert( f0= 'pa2868', f1= '(2868)Top Navigation')
    db.dcollapsed0sidebar.insert( f0= 'pa2870', f1= '(2870)Boxed')
    db.dcollapsed0sidebar.insert( f0= 'pa2872', f1= '(2872)Fixed Sidebar')
    db.dcollapsed0sidebar.insert( f0= 'pa2874', f1= '(2874)Fixed Navbar')
    db.dcollapsed0sidebar.insert( f0= 'pa2876', f1= '(2876)Fixed Footer')
    db.dcollapsed0sidebar.insert( f0= 'pa2878', f1= '(2878)Collapsed Sidebar')
    db.dcollapsed0sidebar.insert( f0= 'pa2880', f1= '(2880)ChartJS')
    db.dcollapsed0sidebar.insert( f0= 'pa2882', f1= '(2882)Flot')
    db.dcollapsed0sidebar.insert( f0= 'pa2884', f1= '(2884)Inline')
    db.dcollapsed0sidebar.insert( f0= 'pa2886', f1= '(2886)General')
    db.dcollapsed0sidebar.insert( f0= 'pa2888', f1= '(2888)Icons')
    db.dcollapsed0sidebar.insert( f0= 'pa2890', f1= '(2890)Buttons')
    db.dcollapsed0sidebar.insert( f0= 'pa2892', f1= '(2892)Sliders')
    db.dcollapsed0sidebar.insert( f0= 'pa2894', f1= '(2894)Modals & Alerts')
    db.dcollapsed0sidebar.insert( f0= 'pa2896', f1= '(2896)Navbar & Tabs')
    db.dcollapsed0sidebar.insert( f0= 'pa2898', f1= '(2898)Timeline')
    db.dcollapsed0sidebar.insert( f0= 'pa2900', f1= '(2900)Ribbons')
    db.dcollapsed0sidebar.insert( f0= 'pa2902', f1= '(2902)General Elements')
    db.dcollapsed0sidebar.insert( f0= 'pa2904', f1= '(2904)Advanced Elements')
    db.dcollapsed0sidebar.insert( f0= 'pa2906', f1= '(2906)Editors')
    db.dcollapsed0sidebar.insert( f0= 'pa2908', f1= '(2908)Simple Tables')
    db.dcollapsed0sidebar.insert( f0= 'pa2910', f1= '(2910)DataTables')
    db.dcollapsed0sidebar.insert( f0= 'pa2912', f1= '(2912)jsGrid')
    db.dcollapsed0sidebar.insert( f0= 'lb2913', f1= '(2913)EXAMPLES')
    db.dcollapsed0sidebar.insert( f0= 'sx2915', f1= '(2915)2')
    db.dcollapsed0sidebar.insert( f0= 'pa2918', f1= '(2918)Inbox')
    db.dcollapsed0sidebar.insert( f0= 'pa2920', f1= '(2920)Compose')
    db.dcollapsed0sidebar.insert( f0= 'pa2922', f1= '(2922)Read')
    db.dcollapsed0sidebar.insert( f0= 'pa2924', f1= '(2924)Invoice')
    db.dcollapsed0sidebar.insert( f0= 'pa2926', f1= '(2926)Profile')
    db.dcollapsed0sidebar.insert( f0= 'pa2928', f1= '(2928)E-commerce')
    db.dcollapsed0sidebar.insert( f0= 'pa2930', f1= '(2930)Projects')
    db.dcollapsed0sidebar.insert( f0= 'pa2932', f1= '(2932)Project Add')
    db.dcollapsed0sidebar.insert( f0= 'pa2934', f1= '(2934)Project Edit')
    db.dcollapsed0sidebar.insert( f0= 'pa2936', f1= '(2936)Project Detail')
    db.dcollapsed0sidebar.insert( f0= 'pa2938', f1= '(2938)Contacts')
    db.dcollapsed0sidebar.insert( f0= 'pa2940', f1= '(2940)Login')
    db.dcollapsed0sidebar.insert( f0= 'pa2942', f1= '(2942)Register')
    db.dcollapsed0sidebar.insert( f0= 'pa2944', f1= '(2944)Forgot Password')
    db.dcollapsed0sidebar.insert( f0= 'pa2946', f1= '(2946)Recover Password')
    db.dcollapsed0sidebar.insert( f0= 'pa2948', f1= '(2948)Lockscreen')
    db.dcollapsed0sidebar.insert( f0= 'pa2950', f1= '(2950)Legacy User Menu')
    db.dcollapsed0sidebar.insert( f0= 'pa2952', f1= '(2952)Language Menu')
    db.dcollapsed0sidebar.insert( f0= 'pa2954', f1= '(2954)Error 404')
    db.dcollapsed0sidebar.insert( f0= 'pa2956', f1= '(2956)Error 500')
    db.dcollapsed0sidebar.insert( f0= 'pa2958', f1= '(2958)Pace')
    db.dcollapsed0sidebar.insert( f0= 'pa2960', f1= '(2960)Blank Page')
    db.dcollapsed0sidebar.insert( f0= 'pa2962', f1= '(2962)Starter Page')
    db.dcollapsed0sidebar.insert( f0= 'lb2963', f1= '(2963)MISCELLANEOUS')
    db.dcollapsed0sidebar.insert( f0= 'pa2964', f1= '(2964)Documentation')
    db.dcollapsed0sidebar.insert( f0= 'lb2965', f1= '(2965)MULTI LEVEL EXAMPLE')
    db.dcollapsed0sidebar.insert( f0= 'pa2966', f1= '(2966)Level 1')
    db.dcollapsed0sidebar.insert( f0= 'pa2967', f1= '(2967)Level 2')
    db.dcollapsed0sidebar.insert( f0= 'pa2968', f1= '(2968)Level 3')
    db.dcollapsed0sidebar.insert( f0= 'pa2969', f1= '(2969)Level 3')
    db.dcollapsed0sidebar.insert( f0= 'pa2970', f1= '(2970)Level 3')
    db.dcollapsed0sidebar.insert( f0= 'pa2971', f1= '(2971)Level 2')
    db.dcollapsed0sidebar.insert( f0= 'pa2972', f1= '(2972)Level 1')
    db.dcollapsed0sidebar.insert( f0= 'lb2973', f1= '(2973)LABELS')
    db.dcollapsed0sidebar.insert( f0= 'pc2974', f1= '(2974)Important')
    db.dcollapsed0sidebar.insert( f0= 'pa2975', f1= '(2975)Warning')
    db.dcollapsed0sidebar.insert( f0= 'pa2976', f1= '(2976)Informational')
    db.dcollapsed0sidebar.insert( f0= 'hh2977', f1= '(2977)Collapsed Sidebar')
    db.dcollapsed0sidebar.insert( f0= 'aa2978', f1= '(2978)Home')
    db.dcollapsed0sidebar.insert( f0= 'aa2979', f1= '(2979)Layout')
    db.dcollapsed0sidebar.insert( f0= 'lb2980', f1= '(2980)Collapsed Sidebar')
    db.dcollapsed0sidebar.insert( f0= 'hc2981', f1= '(2981)Title')
    db.dcollapsed0sidebar.insert( f0= 'bb2982', f1= '(2982)Version')
    db.dcollapsed0sidebar.insert( f0= 'aa2983', f1= '(2983)AdminLTE.io')
    db.commit()
#
