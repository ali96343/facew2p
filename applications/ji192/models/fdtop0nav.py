#
# table for controller: top_nav
#

from gluon.contrib.populate import populate

db.define_table('dtop0nav', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtop0nav.id ).count():
    db.dtop0nav.insert( f0= 'bb5429', f1= '(5429)Admin')
    db.dtop0nav.insert( f0= 'sx5430', f1= '(5430)(current)')
    db.dtop0nav.insert( f0= 'aa5431', f1= '(5431)Link')
    db.dtop0nav.insert( f0= 'aa5432', f1= '(5432)Action')
    db.dtop0nav.insert( f0= 'aa5433', f1= '(5433)Another action')
    db.dtop0nav.insert( f0= 'aa5434', f1= '(5434)Something else here')
    db.dtop0nav.insert( f0= 'aa5435', f1= '(5435)Separated link')
    db.dtop0nav.insert( f0= 'aa5436', f1= '(5436)One more separated link')
    db.dtop0nav.insert( f0= 'pb5437', f1= '(5437)Search')
    db.dtop0nav.insert( f0= 'lb5438', f1= '(5438)You have 4 messages')
    db.dtop0nav.insert( f0= 'ib5440', f1= '(5440)5 mins')
    db.dtop0nav.insert( f0= 'pa5441', f1= '(5441)Why not buy a new awesome theme?')
    db.dtop0nav.insert( f0= 'aa5442', f1= '(5442)See All Messages')
    db.dtop0nav.insert( f0= 'sx5443', f1= '(5443)10')
    db.dtop0nav.insert( f0= 'lb5444', f1= '(5444)You have 10 notifications')
    db.dtop0nav.insert( f0= 'aa5445', f1= '(5445)View all')
    db.dtop0nav.insert( f0= 'lb5446', f1= '(5446)You have 9 tasks')
    db.dtop0nav.insert( f0= 'ic5447', f1= '(5447)20%')
    db.dtop0nav.insert( f0= 'sx5448', f1= '(5448)20% Complete')
    db.dtop0nav.insert( f0= 'aa5449', f1= '(5449)View all tasks')
    db.dtop0nav.insert( f0= 'sx5451', f1= '(5451)Alexander Pierce')
    db.dtop0nav.insert( f0= 'ic5453', f1= '(5453)Member since Nov. 2012')
    db.dtop0nav.insert( f0= 'aa5454', f1= '(5454)Followers')
    db.dtop0nav.insert( f0= 'aa5455', f1= '(5455)Sales')
    db.dtop0nav.insert( f0= 'aa5456', f1= '(5456)Friends')
    db.dtop0nav.insert( f0= 'aa5457', f1= '(5457)Profile')
    db.dtop0nav.insert( f0= 'aa5458', f1= '(5458)Sign out')
    db.dtop0nav.insert( f0= 'ic5459', f1= '(5459)Example 2.0')
    db.dtop0nav.insert( f0= 'ia5460', f1= '(5460)Home')
    db.dtop0nav.insert( f0= 'aa5461', f1= '(5461)Layout')
    db.dtop0nav.insert( f0= 'lb5462', f1= '(5462)Top Navigation')
    db.dtop0nav.insert( f0= 'hh5463', f1= '(5463)Tip!')
    db.dtop0nav.insert( f0= 'hh5464', f1= '(5464)Warning!')
    db.dtop0nav.insert( f0= 'hc5465', f1= '(5465)Blank Box')
    db.dtop0nav.insert( f0= 'bb5466', f1= '(5466)Version')
    db.commit()
#
