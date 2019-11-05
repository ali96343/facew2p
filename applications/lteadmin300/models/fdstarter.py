#
# table for controller: starter
#

from gluon.contrib.populate import populate

db.define_table('dstarter', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dstarter.id ).count():
    db.dstarter.insert( f0= 'aa8020', f1= '(8020)Home')
    db.dstarter.insert( f0= 'aa8021', f1= '(8021)Contact')
    db.dstarter.insert( f0= 'pb8022', f1= '(8022)Search')
    db.dstarter.insert( f0= 'sx8023', f1= '(8023)3')
    db.dstarter.insert( f0= 'pc8025', f1= '(8025)Call me whenever you can...')
    db.dstarter.insert( f0= 'pc8026', f1= '(8026)4 Hours Ago')
    db.dstarter.insert( f0= 'pc8028', f1= '(8028)I got your message bro')
    db.dstarter.insert( f0= 'pc8029', f1= '(8029)4 Hours Ago')
    db.dstarter.insert( f0= 'pc8031', f1= '(8031)The subject goes here')
    db.dstarter.insert( f0= 'pc8032', f1= '(8032)4 Hours Ago')
    db.dstarter.insert( f0= 'aa8033', f1= '(8033)See All Messages')
    db.dstarter.insert( f0= 'sx8034', f1= '(8034)15 Notifications')
    db.dstarter.insert( f0= 'sx8035', f1= '(8035)3 mins')
    db.dstarter.insert( f0= 'sx8036', f1= '(8036)12 hours')
    db.dstarter.insert( f0= 'sx8037', f1= '(8037)2 days')
    db.dstarter.insert( f0= 'aa8038', f1= '(8038)See All Notifications')
    db.dstarter.insert( f0= 'sx8041', f1= '(8041)AdminLTE 3')
    db.dstarter.insert( f0= 'aa8043', f1= '(8043)Alexander Pierce')
    db.dstarter.insert( f0= 'pa8044', f1= '(8044)Active Page')
    db.dstarter.insert( f0= 'pa8045', f1= '(8045)Inactive Page')
    db.dstarter.insert( f0= 'sx8046', f1= '(8046)New')
    db.dstarter.insert( f0= 'ha8047', f1= '(8047)Starter Page')
    db.dstarter.insert( f0= 'aa8048', f1= '(8048)Home')
    db.dstarter.insert( f0= 'lb8049', f1= '(8049)Starter Page')
    db.dstarter.insert( f0= 'he8050', f1= '(8050)Card title')
    db.dstarter.insert( f0= 'aa8051', f1= '(8051)Card link')
    db.dstarter.insert( f0= 'aa8052', f1= '(8052)Another link')
    db.dstarter.insert( f0= 'he8053', f1= '(8053)Card title')
    db.dstarter.insert( f0= 'aa8054', f1= '(8054)Card link')
    db.dstarter.insert( f0= 'aa8055', f1= '(8055)Another link')
    db.dstarter.insert( f0= 'he8056', f1= '(8056)Featured')
    db.dstarter.insert( f0= 'hf8057', f1= '(8057)Special title treatment')
    db.dstarter.insert( f0= 'pc8058', f1= '(8058)With supporting text below as a natural lead-in to additional content.')
    db.dstarter.insert( f0= 'aa8059', f1= '(8059)Go somewhere')
    db.dstarter.insert( f0= 'he8060', f1= '(8060)Featured')
    db.dstarter.insert( f0= 'hf8061', f1= '(8061)Special title treatment')
    db.dstarter.insert( f0= 'pc8062', f1= '(8062)With supporting text below as a natural lead-in to additional content.')
    db.dstarter.insert( f0= 'aa8063', f1= '(8063)Go somewhere')
    db.dstarter.insert( f0= 'hh8064', f1= '(8064)Title')
    db.dstarter.insert( f0= 'pa8065', f1= '(8065)Sidebar content')
    db.dstarter.insert( f0= 'aa8066', f1= '(8066)AdminLTE.io')
    db.commit()
#
