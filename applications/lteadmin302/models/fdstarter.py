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
    db.dstarter.insert( f0= 'aa8354', f1= '(8354)Home')
    db.dstarter.insert( f0= 'aa8355', f1= '(8355)Contact')
    db.dstarter.insert( f0= 'pb8356', f1= '(8356)Search')
    db.dstarter.insert( f0= 'sx8357', f1= '(8357)3')
    db.dstarter.insert( f0= 'pc8359', f1= '(8359)Call me whenever you can...')
    db.dstarter.insert( f0= 'pc8360', f1= '(8360)4 Hours Ago')
    db.dstarter.insert( f0= 'pc8362', f1= '(8362)I got your message bro')
    db.dstarter.insert( f0= 'pc8363', f1= '(8363)4 Hours Ago')
    db.dstarter.insert( f0= 'pc8365', f1= '(8365)The subject goes here')
    db.dstarter.insert( f0= 'pc8366', f1= '(8366)4 Hours Ago')
    db.dstarter.insert( f0= 'aa8367', f1= '(8367)See All Messages')
    db.dstarter.insert( f0= 'sx8368', f1= '(8368)15 Notifications')
    db.dstarter.insert( f0= 'sx8369', f1= '(8369)3 mins')
    db.dstarter.insert( f0= 'sx8370', f1= '(8370)12 hours')
    db.dstarter.insert( f0= 'sx8371', f1= '(8371)2 days')
    db.dstarter.insert( f0= 'aa8372', f1= '(8372)See All Notifications')
    db.dstarter.insert( f0= 'sx8375', f1= '(8375)AdminLTE 3')
    db.dstarter.insert( f0= 'aa8377', f1= '(8377)Alexander Pierce')
    db.dstarter.insert( f0= 'pa8378', f1= '(8378)Active Page')
    db.dstarter.insert( f0= 'pa8379', f1= '(8379)Inactive Page')
    db.dstarter.insert( f0= 'sx8380', f1= '(8380)New')
    db.dstarter.insert( f0= 'ha8381', f1= '(8381)Starter Page')
    db.dstarter.insert( f0= 'aa8382', f1= '(8382)Home')
    db.dstarter.insert( f0= 'lb8383', f1= '(8383)Starter Page')
    db.dstarter.insert( f0= 'he8384', f1= '(8384)Card title')
    db.dstarter.insert( f0= 'aa8385', f1= '(8385)Card link')
    db.dstarter.insert( f0= 'aa8386', f1= '(8386)Another link')
    db.dstarter.insert( f0= 'he8387', f1= '(8387)Card title')
    db.dstarter.insert( f0= 'aa8388', f1= '(8388)Card link')
    db.dstarter.insert( f0= 'aa8389', f1= '(8389)Another link')
    db.dstarter.insert( f0= 'he8390', f1= '(8390)Featured')
    db.dstarter.insert( f0= 'hf8391', f1= '(8391)Special title treatment')
    db.dstarter.insert( f0= 'pc8392', f1= '(8392)With supporting text below as a natural lead-in to additional content.')
    db.dstarter.insert( f0= 'aa8393', f1= '(8393)Go somewhere')
    db.dstarter.insert( f0= 'he8394', f1= '(8394)Featured')
    db.dstarter.insert( f0= 'hf8395', f1= '(8395)Special title treatment')
    db.dstarter.insert( f0= 'pc8396', f1= '(8396)With supporting text below as a natural lead-in to additional content.')
    db.dstarter.insert( f0= 'aa8397', f1= '(8397)Go somewhere')
    db.dstarter.insert( f0= 'hh8398', f1= '(8398)Title')
    db.dstarter.insert( f0= 'pa8399', f1= '(8399)Sidebar content')
    db.dstarter.insert( f0= 'aa8400', f1= '(8400)AdminLTE.io')
    db.commit()
#
