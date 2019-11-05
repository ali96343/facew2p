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
    db.dtop0nav.insert( f0= 'sx7347', f1= '(7347)AdminLTE 3')
    db.dtop0nav.insert( f0= 'aa7349', f1= '(7349)Home')
    db.dtop0nav.insert( f0= 'aa7350', f1= '(7350)Contact')
    db.dtop0nav.insert( f0= 'aa7351', f1= '(7351)Dropdown')
    db.dtop0nav.insert( f0= 'aa7352', f1= '(7352)Some action')
    db.dtop0nav.insert( f0= 'aa7353', f1= '(7353)Some other action')
    db.dtop0nav.insert( f0= 'aa7354', f1= '(7354)Hover for action')
    db.dtop0nav.insert( f0= 'aa7355', f1= '(7355)level 2')
    db.dtop0nav.insert( f0= 'aa7356', f1= '(7356)level 2')
    db.dtop0nav.insert( f0= 'aa7357', f1= '(7357)3rd level')
    db.dtop0nav.insert( f0= 'aa7358', f1= '(7358)3rd level')
    db.dtop0nav.insert( f0= 'aa7359', f1= '(7359)level 2')
    db.dtop0nav.insert( f0= 'aa7360', f1= '(7360)level 2')
    db.dtop0nav.insert( f0= 'pb7361', f1= '(7361)Search')
    db.dtop0nav.insert( f0= 'sx7362', f1= '(7362)3')
    db.dtop0nav.insert( f0= 'pc7364', f1= '(7364)Call me whenever you can...')
    db.dtop0nav.insert( f0= 'pc7365', f1= '(7365)4 Hours Ago')
    db.dtop0nav.insert( f0= 'pc7367', f1= '(7367)I got your message bro')
    db.dtop0nav.insert( f0= 'pc7368', f1= '(7368)4 Hours Ago')
    db.dtop0nav.insert( f0= 'pc7370', f1= '(7370)The subject goes here')
    db.dtop0nav.insert( f0= 'pc7371', f1= '(7371)4 Hours Ago')
    db.dtop0nav.insert( f0= 'aa7372', f1= '(7372)See All Messages')
    db.dtop0nav.insert( f0= 'sx7373', f1= '(7373)15 Notifications')
    db.dtop0nav.insert( f0= 'sx7374', f1= '(7374)3 mins')
    db.dtop0nav.insert( f0= 'sx7375', f1= '(7375)12 hours')
    db.dtop0nav.insert( f0= 'sx7376', f1= '(7376)2 days')
    db.dtop0nav.insert( f0= 'aa7377', f1= '(7377)See All Notifications')
    db.dtop0nav.insert( f0= 'ic7378', f1= '(7378)Example 3.0')
    db.dtop0nav.insert( f0= 'aa7379', f1= '(7379)Home')
    db.dtop0nav.insert( f0= 'aa7380', f1= '(7380)Layout')
    db.dtop0nav.insert( f0= 'lb7381', f1= '(7381)Top Navigation')
    db.dtop0nav.insert( f0= 'he7382', f1= '(7382)Card title')
    db.dtop0nav.insert( f0= 'aa7383', f1= '(7383)Card link')
    db.dtop0nav.insert( f0= 'aa7384', f1= '(7384)Another link')
    db.dtop0nav.insert( f0= 'he7385', f1= '(7385)Card title')
    db.dtop0nav.insert( f0= 'aa7386', f1= '(7386)Card link')
    db.dtop0nav.insert( f0= 'aa7387', f1= '(7387)Another link')
    db.dtop0nav.insert( f0= 'he7388', f1= '(7388)Featured')
    db.dtop0nav.insert( f0= 'hf7389', f1= '(7389)Special title treatment')
    db.dtop0nav.insert( f0= 'pc7390', f1= '(7390)With supporting text below as a natural lead-in to additional content.')
    db.dtop0nav.insert( f0= 'aa7391', f1= '(7391)Go somewhere')
    db.dtop0nav.insert( f0= 'he7392', f1= '(7392)Featured')
    db.dtop0nav.insert( f0= 'hf7393', f1= '(7393)Special title treatment')
    db.dtop0nav.insert( f0= 'pc7394', f1= '(7394)With supporting text below as a natural lead-in to additional content.')
    db.dtop0nav.insert( f0= 'aa7395', f1= '(7395)Go somewhere')
    db.dtop0nav.insert( f0= 'hh7396', f1= '(7396)Title')
    db.dtop0nav.insert( f0= 'pa7397', f1= '(7397)Sidebar content')
    db.dtop0nav.insert( f0= 'aa7398', f1= '(7398)AdminLTE.io')
    db.commit()
#
