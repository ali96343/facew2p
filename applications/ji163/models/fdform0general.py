#
# table for controller: form_general
#

from gluon.contrib.populate import populate

db.define_table('dform0general', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dform0general.id ).count():
    db.dform0general.insert( f0= 'sx3637', f1= '(3637)Toggle navigation')
    db.dform0general.insert( f0= 'aa3642', f1= '(3642)Dashboard')
    db.dform0general.insert( f0= 'aa3644', f1= '(3644)Tables')
    db.dform0general.insert( f0= 'aa3646', f1= '(3646)General')
    db.dform0general.insert( f0= 'aa3648', f1= '(3648)Validation')
    db.dform0general.insert( f0= 'aa3650', f1= '(3650)WYSIWYG')
    db.dform0general.insert( f0= 'pb3652', f1= '(3652)Live Search ...')
    db.dform0general.insert( f0= 'he3654', f1= '(3654)Archie')
    db.dform0general.insert( f0= 'aa3655', f1= '(3655)Administrator')
    db.dform0general.insert( f0= 'ba3656', f1= '(3656)Last Access :')
    db.dform0general.insert( f0= 'lb3657', f1= '(3657)Menu')
    db.dform0general.insert( f0= 'sx3659', f1= '(3659)Layouts')
    db.dform0general.insert( f0= 'sx3678', f1= '(3678)Components')
    db.dform0general.insert( f0= 'sx3690', f1= '(3690)Tables')
    db.dform0general.insert( f0= 'aa3705', f1= '(3705)Level 2')
    db.dform0general.insert( f0= 'aa3706', f1= '(3706)Level 2')
    db.dform0general.insert( f0= 'aa3707', f1= '(3707)Level 3')
    db.dform0general.insert( f0= 'aa3708', f1= '(3708)Level 3')
    db.dform0general.insert( f0= 'aa3709', f1= '(3709)Level 4')
    db.dform0general.insert( f0= 'aa3710', f1= '(3710)Level 4')
    db.dform0general.insert( f0= 'aa3711', f1= '(3711)Level 5')
    db.dform0general.insert( f0= 'aa3712', f1= '(3712)Level 5')
    db.dform0general.insert( f0= 'aa3713', f1= '(3713)Level 5')
    db.dform0general.insert( f0= 'aa3714', f1= '(3714)Level 4')
    db.dform0general.insert( f0= 'aa3715', f1= '(3715)Level 2')
    db.dform0general.insert( f0= 'aa3716', f1= '(3716)Level 1')
    db.dform0general.insert( f0= 'aa3717', f1= '(3717)Level 2')
    db.dform0general.insert( f0= 'aa3718', f1= '(3718)Level 2')
    db.dform0general.insert( f0= 'aa3719', f1= '(3719)Level 2')
    db.dform0general.insert( f0= 'hh3720', f1= '(3720)Input Text Fields')
    db.dform0general.insert( f0= 'pb3721', f1= '(3721)Email')
    db.dform0general.insert( f0= 'pb3722', f1= '(3722)placeholder text')
    db.dform0general.insert( f0= 'hh3723', f1= '(3723)Selects')
    db.dform0general.insert( f0= 'pb3724', f1= '(3724)Choose a Country...')
    db.dform0general.insert( f0= 'pb3725', f1= '(3725)Choose a Country...')
    db.dform0general.insert( f0= 'pb3726', f1= '(3726)Your Favorite Football Team')
    db.dform0general.insert( f0= 'pb3727', f1= '(3727)Your Favorite Football Team')
    db.dform0general.insert( f0= 'pb3728', f1= '(3728)Your Favorite Type of Bear')
    db.dform0general.insert( f0= 'pb3729', f1= '(3729)Your Favorite Types of Bear')
    db.dform0general.insert( f0= 'pb3730', f1= '(3730)Your Favorite Types of Bear')
    db.dform0general.insert( f0= 'pb3731', f1= '(3731)Your Favorite Type of Bear')
    db.dform0general.insert( f0= 'pb3732', f1= '(3732)Your Favorite Type of Bear')
    db.dform0general.insert( f0= 'pb3733', f1= '(3733)Your Favorite Types of Bear')
    db.dform0general.insert( f0= 'hh3734', f1= '(3734)Checkbox & Radio')
    db.dform0general.insert( f0= 'hh3735', f1= '(3735)Animated Checkbox')
    db.dform0general.insert( f0= 'hh3736', f1= '(3736)Automatically jump to the next input-field')
    db.dform0general.insert( f0= 'hh3737', f1= '(3737)Masked Inputs')
    db.dform0general.insert( f0= 'sx3739', f1= '(3739)99/99/9999')
    db.dform0general.insert( f0= 'sx3741', f1= '(3741)(999) 999-9999')
    db.dform0general.insert( f0= 'sx3742', f1= '(3742)a*-999-a999')
    db.dform0general.insert( f0= 'sx3744', f1= '(3744)+33 999 999 999')
    db.dform0general.insert( f0= 'sx3745', f1= '(3745)99%')
    db.dform0general.insert( f0= 'hh3746', f1= '(3746)Color Picker')
    db.dform0general.insert( f0= 'hh3750', f1= '(3750)Date Picker')
    db.dform0general.insert( f0= 'hh3759', f1= '(3759)Date Range Picker')
    db.dform0general.insert( f0= 'hh3761', f1= '(3761)Time Picker')
    db.dform0general.insert( f0= 'hh3762', f1= '(3762)Grid Inputs')
    db.dform0general.insert( f0= 'pb3763', f1= '(3763).col-lg-1')
    db.dform0general.insert( f0= 'pb3764', f1= '(3764).col-lg-11')
    db.dform0general.insert( f0= 'pb3765', f1= '(3765).col-lg-2')
    db.dform0general.insert( f0= 'pb3766', f1= '(3766).col-lg-10')
    db.dform0general.insert( f0= 'pb3767', f1= '(3767).col-lg-3')
    db.dform0general.insert( f0= 'pb3768', f1= '(3768).col-lg-9')
    db.dform0general.insert( f0= 'pb3769', f1= '(3769).col-lg-4')
    db.dform0general.insert( f0= 'pb3770', f1= '(3770).col-lg-8')
    db.dform0general.insert( f0= 'pb3771', f1= '(3771).col-lg-5')
    db.dform0general.insert( f0= 'pb3772', f1= '(3772).col-lg-7')
    db.dform0general.insert( f0= 'pb3773', f1= '(3773).col-lg-6')
    db.dform0general.insert( f0= 'pb3774', f1= '(3774).col-lg-6')
    db.dform0general.insert( f0= 'pb3775', f1= '(3775).col-lg-4')
    db.dform0general.insert( f0= 'pb3776', f1= '(3776).col-lg-4')
    db.dform0general.insert( f0= 'pb3777', f1= '(3777).col-lg-4')
    db.dform0general.insert( f0= 'pb3778', f1= '(3778).col-lg-3')
    db.dform0general.insert( f0= 'pb3779', f1= '(3779).col-lg-4')
    db.dform0general.insert( f0= 'pb3780', f1= '(3780).col-lg-5')
    db.dform0general.insert( f0= 'bu3781', f1= '(3781)&times;')
    db.dform0general.insert( f0= 'sp3782', f1= '(3782)Warning!')
    db.dform0general.insert( f0= 'sx3783', f1= '(3783)1,4,4,7,5,9,10')
    db.dform0general.insert( f0= 'sx3784', f1= '(3784)Loading..')
    db.dform0general.insert( f0= 'sx3785', f1= '(3785)Loading..')
    db.dform0general.insert( f0= 'sx3786', f1= '(3786)1,3,4,5,3,5')
    db.dform0general.insert( f0= 'bu3787', f1= '(3787)Default')
    db.dform0general.insert( f0= 'bu3788', f1= '(3788)Primary')
    db.dform0general.insert( f0= 'bu3789', f1= '(3789)Info')
    db.dform0general.insert( f0= 'bu3790', f1= '(3790)Success')
    db.dform0general.insert( f0= 'bu3791', f1= '(3791)Danger')
    db.dform0general.insert( f0= 'bu3792', f1= '(3792)Warning')
    db.dform0general.insert( f0= 'bu3793', f1= '(3793)Inverse')
    db.dform0general.insert( f0= 'bu3794', f1= '(3794)btn-metis-1')
    db.dform0general.insert( f0= 'bu3795', f1= '(3795)btn-metis-2')
    db.dform0general.insert( f0= 'bu3796', f1= '(3796)btn-metis-3')
    db.dform0general.insert( f0= 'bu3797', f1= '(3797)btn-metis-4')
    db.dform0general.insert( f0= 'bu3798', f1= '(3798)btn-metis-5')
    db.dform0general.insert( f0= 'bu3799', f1= '(3799)btn-metis-6')
    db.dform0general.insert( f0= 'si3800', f1= '(3800)20%')
    db.dform0general.insert( f0= 'sp3801', f1= '(3801)Default')
    db.dform0general.insert( f0= 'si3802', f1= '(3802)40%')
    db.dform0general.insert( f0= 'sp3803', f1= '(3803)Success')
    db.dform0general.insert( f0= 'si3804', f1= '(3804)60%')
    db.dform0general.insert( f0= 'sp3805', f1= '(3805)warning')
    db.dform0general.insert( f0= 'si3806', f1= '(3806)80%')
    db.dform0general.insert( f0= 'sp3807', f1= '(3807)Danger')
    db.dform0general.insert( f0= 'pa3808', f1= '(3808)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dform0general.insert( f0= 'bu3809', f1= '(3809)&times;')
    db.dform0general.insert( f0= 'hd3810', f1= '(3810)Modal title')
    db.dform0general.insert( f0= 'bu3811', f1= '(3811)Close')
    db.commit()
#
