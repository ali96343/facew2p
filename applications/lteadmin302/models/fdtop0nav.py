#
# table for controller: topIInav
#

from gluon.contrib.populate import populate

db.define_table('dtop0nav', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtop0nav.id ).count():
    db.dtop0nav.insert( f0= 'sx7667', f1= '(7667)AdminLTE 3')
    db.dtop0nav.insert( f0= 'aa7669', f1= '(7669)Home')
    db.dtop0nav.insert( f0= 'aa7670', f1= '(7670)Contact')
    db.dtop0nav.insert( f0= 'aa7671', f1= '(7671)Dropdown')
    db.dtop0nav.insert( f0= 'aa7672', f1= '(7672)Some action')
    db.dtop0nav.insert( f0= 'aa7673', f1= '(7673)Some other action')
    db.dtop0nav.insert( f0= 'aa7674', f1= '(7674)Hover for action')
    db.dtop0nav.insert( f0= 'aa7675', f1= '(7675)level 2')
    db.dtop0nav.insert( f0= 'aa7676', f1= '(7676)level 2')
    db.dtop0nav.insert( f0= 'aa7677', f1= '(7677)3rd level')
    db.dtop0nav.insert( f0= 'aa7678', f1= '(7678)3rd level')
    db.dtop0nav.insert( f0= 'aa7679', f1= '(7679)level 2')
    db.dtop0nav.insert( f0= 'aa7680', f1= '(7680)level 2')
    db.dtop0nav.insert( f0= 'pb7681', f1= '(7681)Search')
    db.dtop0nav.insert( f0= 'sx7682', f1= '(7682)3')
    db.dtop0nav.insert( f0= 'pc7684', f1= '(7684)Call me whenever you can...')
    db.dtop0nav.insert( f0= 'pc7685', f1= '(7685)4 Hours Ago')
    db.dtop0nav.insert( f0= 'pc7687', f1= '(7687)I got your message bro')
    db.dtop0nav.insert( f0= 'pc7688', f1= '(7688)4 Hours Ago')
    db.dtop0nav.insert( f0= 'pc7690', f1= '(7690)The subject goes here')
    db.dtop0nav.insert( f0= 'pc7691', f1= '(7691)4 Hours Ago')
    db.dtop0nav.insert( f0= 'aa7692', f1= '(7692)See All Messages')
    db.dtop0nav.insert( f0= 'sx7693', f1= '(7693)15 Notifications')
    db.dtop0nav.insert( f0= 'sx7694', f1= '(7694)3 mins')
    db.dtop0nav.insert( f0= 'sx7695', f1= '(7695)12 hours')
    db.dtop0nav.insert( f0= 'sx7696', f1= '(7696)2 days')
    db.dtop0nav.insert( f0= 'aa7697', f1= '(7697)See All Notifications')
    db.dtop0nav.insert( f0= 'ic7698', f1= '(7698)Example 3.0')
    db.dtop0nav.insert( f0= 'aa7699', f1= '(7699)Home')
    db.dtop0nav.insert( f0= 'aa7700', f1= '(7700)Layout')
    db.dtop0nav.insert( f0= 'lb7701', f1= '(7701)Top Navigation')
    db.dtop0nav.insert( f0= 'he7702', f1= '(7702)Card title')
    db.dtop0nav.insert( f0= 'aa7703', f1= '(7703)Card link')
    db.dtop0nav.insert( f0= 'aa7704', f1= '(7704)Another link')
    db.dtop0nav.insert( f0= 'he7705', f1= '(7705)Card title')
    db.dtop0nav.insert( f0= 'aa7706', f1= '(7706)Card link')
    db.dtop0nav.insert( f0= 'aa7707', f1= '(7707)Another link')
    db.dtop0nav.insert( f0= 'he7708', f1= '(7708)Featured')
    db.dtop0nav.insert( f0= 'hf7709', f1= '(7709)Special title treatment')
    db.dtop0nav.insert( f0= 'pc7710', f1= '(7710)With supporting text below as a natural lead-in to additional content.')
    db.dtop0nav.insert( f0= 'aa7711', f1= '(7711)Go somewhere')
    db.dtop0nav.insert( f0= 'he7712', f1= '(7712)Featured')
    db.dtop0nav.insert( f0= 'hf7713', f1= '(7713)Special title treatment')
    db.dtop0nav.insert( f0= 'pc7714', f1= '(7714)With supporting text below as a natural lead-in to additional content.')
    db.dtop0nav.insert( f0= 'aa7715', f1= '(7715)Go somewhere')
    db.dtop0nav.insert( f0= 'hh7716', f1= '(7716)Title')
    db.dtop0nav.insert( f0= 'pa7717', f1= '(7717)Sidebar content')
    db.dtop0nav.insert( f0= 'aa7718', f1= '(7718)AdminLTE.io')
    db.commit()
#
