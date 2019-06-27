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
    db.dinvoice.insert( f0= 'sx1184', f1= '(1184)Toggle sidebar')
    db.dinvoice.insert( f0= 'sx1186', f1= '(1186)Software Update')
    db.dinvoice.insert( f0= 'sx1187', f1= '(1187)65%')
    db.dinvoice.insert( f0= 'sx1188', f1= '(1188)Hardware Upgrade')
    db.dinvoice.insert( f0= 'sx1189', f1= '(1189)35%')
    db.dinvoice.insert( f0= 'sx1190', f1= '(1190)Unit Testing')
    db.dinvoice.insert( f0= 'sx1191', f1= '(1191)15%')
    db.dinvoice.insert( f0= 'sx1192', f1= '(1192)Bug Fixes')
    db.dinvoice.insert( f0= 'sx1193', f1= '(1193)90%')
    db.dinvoice.insert( f0= 'sx1194', f1= '(1194)+12')
    db.dinvoice.insert( f0= 'sx1195', f1= '(1195)+8')
    db.dinvoice.insert( f0= 'sx1196', f1= '(1196)+11')
    db.dinvoice.insert( f0= 'sx1198', f1= '(1198)Alex:')
    db.dinvoice.insert( f0= 'sp1199', f1= '(1199)a moment ago')
    db.dinvoice.insert( f0= 'sx1201', f1= '(1201)Susan:')
    db.dinvoice.insert( f0= 'sp1202', f1= '(1202)20 minutes ago')
    db.dinvoice.insert( f0= 'sx1204', f1= '(1204)Bob:')
    db.dinvoice.insert( f0= 'sp1205', f1= '(1205)3:15 pm')
    db.dinvoice.insert( f0= 'sx1207', f1= '(1207)Kate:')
    db.dinvoice.insert( f0= 'sp1208', f1= '(1208)1:33 pm')
    db.dinvoice.insert( f0= 'sx1210', f1= '(1210)Fred:')
    db.dinvoice.insert( f0= 'sp1211', f1= '(1211)10:09 am')
    db.dinvoice.insert( f0= 'ic1214', f1= '(1214)Welcome,')
    db.dinvoice.insert( f0= 'sx1217', f1= '(1217)Dashboard')
    db.dinvoice.insert( f0= 'sx1231', f1= '(1231)Tables')
    db.dinvoice.insert( f0= 'sx1234', f1= '(1234)Forms')
    db.dinvoice.insert( f0= 'sx1241', f1= '(1241)Widgets')
    db.dinvoice.insert( f0= 'sx1244', f1= '(1244)Gallery')
    db.dinvoice.insert( f0= 'sx1245', f1= '(1245)More Pages')
    db.dinvoice.insert( f0= 'aa1259', f1= '(1259)Home')
    db.dinvoice.insert( f0= 'aa1260', f1= '(1260)More Pages')
    db.dinvoice.insert( f0= 'lb1261', f1= '(1261)Invoice')
    db.dinvoice.insert( f0= 'pb1262', f1= '(1262)Search ...')
    db.dinvoice.insert( f0= 'bb1263', f1= '(1263).container')
    db.dinvoice.insert( f0= 'sx1264', f1= '(1264)Invoice:')
    db.dinvoice.insert( f0= 'sx1266', f1= '(1266)Date:')
    db.dinvoice.insert( f0= 'sx1267', f1= '(1267)04/04/2014')
    db.dinvoice.insert( f0= 'bb1268', f1= '(1268)Company Info')
    db.dinvoice.insert( f0= 'bb1270', f1= '(1270)Customer Info')
    db.dinvoice.insert( f0= 'aa1271', f1= '(1271)google.com')
    db.dinvoice.insert( f0= 'aa1272', f1= '(1272)yahoo.com')
    db.dinvoice.insert( f0= 'sx1273', f1= '(1273)$395')
    db.dinvoice.insert( f0= 'di1274', f1= '(1274)Extra Information')
    db.dinvoice.insert( f0= 'sx1275', f1= '(1275)Ace')
    db.commit()
#
