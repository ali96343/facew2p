#
# table for controller: view_email
#

from gluon.contrib.populate import populate

db.define_table('dview0email', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dview0email.id ).count():
    db.dview0email.insert( f0= 'sp2803', f1= '(2803)outdated')
    db.dview0email.insert( f0= 'pc2804', f1= '(2804)to improve your experience.')
    db.dview0email.insert( f0= 'aa2805', f1= '(2805)upgrade your browser')
    db.dview0email.insert( f0= 'hh2807', f1= '(2807)Messages')
    db.dview0email.insert( f0= 'hh2809', f1= '(2809)David Belle')
    db.dview0email.insert( f0= 'pa2810', f1= '(2810)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dview0email.insert( f0= 'hh2812', f1= '(2812)Jonathan Morris')
    db.dview0email.insert( f0= 'pa2813', f1= '(2813)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dview0email.insert( f0= 'hh2815', f1= '(2815)Fredric Mitchell')
    db.dview0email.insert( f0= 'pa2816', f1= '(2816)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dview0email.insert( f0= 'hh2818', f1= '(2818)David Belle')
    db.dview0email.insert( f0= 'pa2819', f1= '(2819)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dview0email.insert( f0= 'hh2821', f1= '(2821)Glenn Jecobs')
    db.dview0email.insert( f0= 'pa2822', f1= '(2822)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dview0email.insert( f0= 'aa2823', f1= '(2823)View All')
    db.dview0email.insert( f0= 'hh2824', f1= '(2824)Notification')
    db.dview0email.insert( f0= 'hh2826', f1= '(2826)David Belle')
    db.dview0email.insert( f0= 'pa2827', f1= '(2827)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dview0email.insert( f0= 'hh2829', f1= '(2829)Jonathan Morris')
    db.dview0email.insert( f0= 'pa2830', f1= '(2830)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dview0email.insert( f0= 'hh2832', f1= '(2832)Fredric Mitchell')
    db.dview0email.insert( f0= 'pa2833', f1= '(2833)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dview0email.insert( f0= 'hh2835', f1= '(2835)David Belle')
    db.dview0email.insert( f0= 'pa2836', f1= '(2836)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dview0email.insert( f0= 'hh2838', f1= '(2838)Glenn Jecobs')
    db.dview0email.insert( f0= 'pa2839', f1= '(2839)Cum sociis natoque penatibus et magnis dis parturient montes')
    db.dview0email.insert( f0= 'aa2840', f1= '(2840)View All')
    db.dview0email.insert( f0= 'hh2841', f1= '(2841)Tasks')
    db.dview0email.insert( f0= 'pa2842', f1= '(2842)HTML5 Validation Report')
    db.dview0email.insert( f0= 'sp2843', f1= '(2843)95%')
    db.dview0email.insert( f0= 'pa2844', f1= '(2844)Google Chrome Extension')
    db.dview0email.insert( f0= 'sp2845', f1= '(2845)85%')
    db.dview0email.insert( f0= 'pa2846', f1= '(2846)Social Internet Projects')
    db.dview0email.insert( f0= 'sp2847', f1= '(2847)75%')
    db.dview0email.insert( f0= 'pa2848', f1= '(2848)Bootstrap Admin')
    db.dview0email.insert( f0= 'sp2849', f1= '(2849)65%')
    db.dview0email.insert( f0= 'pa2850', f1= '(2850)Youtube App')
    db.dview0email.insert( f0= 'sp2851', f1= '(2851)55%')
    db.dview0email.insert( f0= 'aa2852', f1= '(2852)View All')
    db.dview0email.insert( f0= 'hh2853', f1= '(2853)Chat')
    db.dview0email.insert( f0= 'pb2854', f1= '(2854)Search People')
    db.dview0email.insert( f0= 'hh2856', f1= '(2856)David Belle')
    db.dview0email.insert( f0= 'pa2857', f1= '(2857)Available')
    db.dview0email.insert( f0= 'hh2859', f1= '(2859)Jonathan Morris')
    db.dview0email.insert( f0= 'pa2860', f1= '(2860)Last seen 3 hours ago')
    db.dview0email.insert( f0= 'hh2862', f1= '(2862)Fredric Mitchell')
    db.dview0email.insert( f0= 'pa2863', f1= '(2863)Last seen 2 minutes ago')
    db.dview0email.insert( f0= 'hh2865', f1= '(2865)David Belle')
    db.dview0email.insert( f0= 'pa2866', f1= '(2866)Available')
    db.dview0email.insert( f0= 'hh2868', f1= '(2868)Glenn Jecobs')
    db.dview0email.insert( f0= 'pa2869', f1= '(2869)Available')
    db.dview0email.insert( f0= 'aa2870', f1= '(2870)View All')
    db.dview0email.insert( f0= 'aa2871', f1= '(2871)Home')
    db.dview0email.insert( f0= 'aa2873', f1= '(2873)Dashboard One')
    db.dview0email.insert( f0= 'aa2875', f1= '(2875)Dashboard Two')
    db.dview0email.insert( f0= 'aa2877', f1= '(2877)Dashboard Three')
    db.dview0email.insert( f0= 'aa2879', f1= '(2879)Dashboard Four')
    db.dview0email.insert( f0= 'aa2881', f1= '(2881)Analytics')
    db.dview0email.insert( f0= 'aa2883', f1= '(2883)Widgets')
    db.dview0email.insert( f0= 'aa2884', f1= '(2884)Email')
    db.dview0email.insert( f0= 'aa2886', f1= '(2886)Inbox')
    db.dview0email.insert( f0= 'aa2888', f1= '(2888)View Email')
    db.dview0email.insert( f0= 'aa2890', f1= '(2890)Compose Email')
    db.dview0email.insert( f0= 'aa2891', f1= '(2891)Interface')
    db.dview0email.insert( f0= 'aa2893', f1= '(2893)Animations')
    db.dview0email.insert( f0= 'aa2895', f1= '(2895)Google Map')
    db.dview0email.insert( f0= 'aa2897', f1= '(2897)Data Maps')
    db.dview0email.insert( f0= 'aa2899', f1= '(2899)Code Editor')
    db.dview0email.insert( f0= 'aa2901', f1= '(2901)Images Cropper')
    db.dview0email.insert( f0= 'aa2903', f1= '(2903)Wizard')
    db.dview0email.insert( f0= 'aa2904', f1= '(2904)Charts')
    db.dview0email.insert( f0= 'aa2906', f1= '(2906)Flot Charts')
    db.dview0email.insert( f0= 'aa2908', f1= '(2908)Bar Charts')
    db.dview0email.insert( f0= 'aa2910', f1= '(2910)Line Charts')
    db.dview0email.insert( f0= 'aa2912', f1= '(2912)Area Charts')
    db.dview0email.insert( f0= 'aa2913', f1= '(2913)Tables')
    db.dview0email.insert( f0= 'aa2915', f1= '(2915)Normal Table')
    db.dview0email.insert( f0= 'aa2917', f1= '(2917)Data Table')
    db.dview0email.insert( f0= 'aa2918', f1= '(2918)Forms')
    db.dview0email.insert( f0= 'aa2920', f1= '(2920)Form Elements')
    db.dview0email.insert( f0= 'aa2922', f1= '(2922)Form Components')
    db.dview0email.insert( f0= 'aa2924', f1= '(2924)Form Examples')
    db.dview0email.insert( f0= 'aa2925', f1= '(2925)App views')
    db.dview0email.insert( f0= 'aa2927', f1= '(2927)Notifications')
    db.dview0email.insert( f0= 'aa2929', f1= '(2929)Alerts')
    db.dview0email.insert( f0= 'aa2931', f1= '(2931)Modals')
    db.dview0email.insert( f0= 'aa2933', f1= '(2933)Buttons')
    db.dview0email.insert( f0= 'aa2935', f1= '(2935)Tabs')
    db.dview0email.insert( f0= 'aa2937', f1= '(2937)Accordion')
    db.dview0email.insert( f0= 'aa2939', f1= '(2939)Dialogs')
    db.dview0email.insert( f0= 'aa2941', f1= '(2941)Popovers')
    db.dview0email.insert( f0= 'aa2943', f1= '(2943)Tooltips')
    db.dview0email.insert( f0= 'aa2945', f1= '(2945)Dropdowns')
    db.dview0email.insert( f0= 'aa2946', f1= '(2946)Pages')
    db.dview0email.insert( f0= 'aa2948', f1= '(2948)Contact')
    db.dview0email.insert( f0= 'aa2950', f1= '(2950)Invoice')
    db.dview0email.insert( f0= 'aa2952', f1= '(2952)Typography')
    db.dview0email.insert( f0= 'aa2954', f1= '(2954)Color')
    db.dview0email.insert( f0= 'aa2956', f1= '(2956)Login Register')
    db.dview0email.insert( f0= 'aa2958', f1= '(2958)404 Page')
    db.dview0email.insert( f0= 'aa2960', f1= '(2960)Dashboard One')
    db.dview0email.insert( f0= 'aa2962', f1= '(2962)Dashboard Two')
    db.dview0email.insert( f0= 'aa2964', f1= '(2964)Dashboard Three')
    db.dview0email.insert( f0= 'aa2966', f1= '(2966)Dashboard Four')
    db.dview0email.insert( f0= 'aa2968', f1= '(2968)Analytics')
    db.dview0email.insert( f0= 'aa2970', f1= '(2970)Widgets')
    db.dview0email.insert( f0= 'aa2972', f1= '(2972)Inbox')
    db.dview0email.insert( f0= 'aa2974', f1= '(2974)View Email')
    db.dview0email.insert( f0= 'aa2976', f1= '(2976)Compose Email')
    db.dview0email.insert( f0= 'aa2978', f1= '(2978)Animations')
    db.dview0email.insert( f0= 'aa2980', f1= '(2980)Google Map')
    db.dview0email.insert( f0= 'aa2982', f1= '(2982)Data Maps')
    db.dview0email.insert( f0= 'aa2984', f1= '(2984)Code Editor')
    db.dview0email.insert( f0= 'aa2986', f1= '(2986)Images Cropper')
    db.dview0email.insert( f0= 'aa2988', f1= '(2988)Wizard')
    db.dview0email.insert( f0= 'aa2990', f1= '(2990)Flot Charts')
    db.dview0email.insert( f0= 'aa2992', f1= '(2992)Bar Charts')
    db.dview0email.insert( f0= 'aa2994', f1= '(2994)Line Charts')
    db.dview0email.insert( f0= 'aa2996', f1= '(2996)Area Charts')
    db.dview0email.insert( f0= 'aa2998', f1= '(2998)Normal Table')
    db.dview0email.insert( f0= 'aa3000', f1= '(3000)Data Table')
    db.dview0email.insert( f0= 'aa3002', f1= '(3002)Form Elements')
    db.dview0email.insert( f0= 'aa3004', f1= '(3004)Form Components')
    db.dview0email.insert( f0= 'aa3006', f1= '(3006)Form Examples')
    db.dview0email.insert( f0= 'aa3008', f1= '(3008)Notifications')
    db.dview0email.insert( f0= 'aa3010', f1= '(3010)Alerts')
    db.dview0email.insert( f0= 'aa3012', f1= '(3012)Modals')
    db.dview0email.insert( f0= 'aa3014', f1= '(3014)Buttons')
    db.dview0email.insert( f0= 'aa3016', f1= '(3016)Tabs')
    db.dview0email.insert( f0= 'aa3018', f1= '(3018)Accordion')
    db.dview0email.insert( f0= 'aa3020', f1= '(3020)Dialogs')
    db.dview0email.insert( f0= 'aa3022', f1= '(3022)Popovers')
    db.dview0email.insert( f0= 'aa3024', f1= '(3024)Tooltips')
    db.dview0email.insert( f0= 'aa3026', f1= '(3026)Dropdowns')
    db.dview0email.insert( f0= 'aa3028', f1= '(3028)Contact')
    db.dview0email.insert( f0= 'aa3030', f1= '(3030)Invoice')
    db.dview0email.insert( f0= 'aa3032', f1= '(3032)Typography')
    db.dview0email.insert( f0= 'aa3034', f1= '(3034)Color')
    db.dview0email.insert( f0= 'aa3036', f1= '(3036)Login Register')
    db.dview0email.insert( f0= 'aa3038', f1= '(3038)404 Page')
    db.dview0email.insert( f0= 'hh3039', f1= '(3039)View Email')
    db.dview0email.insert( f0= 'sx3040', f1= '(3040)Admin Template')
    db.dview0email.insert( f0= 'pf3041', f1= '(3041)Welcome to Notika')
    db.dview0email.insert( f0= 'aa3042', f1= '(3042)Compose')
    db.dview0email.insert( f0= 'sx3043', f1= '(3043)12')
    db.dview0email.insert( f0= 'hh3044', f1= '(3044)Email view')
    db.dview0email.insert( f0= 'pa3045', f1= '(3045)08:26 PM (2 hours ago)')
    db.dview0email.insert( f0= 'bb3046', f1= '(3046)Subject:')
    db.dview0email.insert( f0= 'pc3047', f1= '(3047)Lorem Ipsum has been the industry s standard dummy text ever')
    db.dview0email.insert( f0= 'bb3048', f1= '(3048)Email:')
    db.dview0email.insert( f0= 'aa3049', f1= '(3049)example.@email.com')
    db.dview0email.insert( f0= 'bb3050', f1= '(3050)Date:')
    db.dview0email.insert( f0= 'pc3051', f1= '(3051)15.03.2018')
    db.dview0email.insert( f0= 'hh3052', f1= '(3052)Hello Mamunur Roshid!')
    db.dview0email.insert( f0= 'bb3053', f1= '(3053)dustrys standard dummy text')
    db.dview0email.insert( f0= 'pf3054', f1= '(3054)Dummy text of the printing and typesetting industry. Lorem Ipsum has been the')
    db.dview0email.insert( f0= 'aa3055', f1= '(3055)Read more')
    db.dview0email.insert( f0= 'pa3056', f1= '(3056)All the Lorem Ipsum generators on the Internet tend to repeat the predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence crisity structures, to generate Lorem Ipsum which looks reasonable. recently with.Dummy text of the printing and typesetting industryunknown printer took a galley of type. when an unknown printer took a galley of types and scrambleded it s stambanner to make a type specimenen book.survived not only five centuries, but also the leap into the electronic typesetting, remaining essentially unchanged.')
    db.dview0email.insert( f0= 'sx3057', f1= '(3057)Thanks and Regards')
    db.dview0email.insert( f0= 'sp3058', f1= '(3058)Mark Smith')
    db.commit()
#
