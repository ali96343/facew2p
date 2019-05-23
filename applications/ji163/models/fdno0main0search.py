#
# table for controller: no_main_search
#

from gluon.contrib.populate import populate

db.define_table('dno0main0search', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dno0main0search.id ).count():
    db.dno0main0search.insert( f0= 'sx1229', f1= '(1229)Toggle navigation')
    db.dno0main0search.insert( f0= 'aa1234', f1= '(1234)Dashboard')
    db.dno0main0search.insert( f0= 'aa1236', f1= '(1236)Tables')
    db.dno0main0search.insert( f0= 'aa1238', f1= '(1238)General')
    db.dno0main0search.insert( f0= 'aa1240', f1= '(1240)Validation')
    db.dno0main0search.insert( f0= 'aa1242', f1= '(1242)WYSIWYG')
    db.dno0main0search.insert( f0= 'he1245', f1= '(1245)Archie')
    db.dno0main0search.insert( f0= 'aa1246', f1= '(1246)Administrator')
    db.dno0main0search.insert( f0= 'ba1247', f1= '(1247)Last Access :')
    db.dno0main0search.insert( f0= 'lb1248', f1= '(1248)Menu')
    db.dno0main0search.insert( f0= 'sx1250', f1= '(1250)Layouts')
    db.dno0main0search.insert( f0= 'sx1269', f1= '(1269)Components')
    db.dno0main0search.insert( f0= 'sx1281', f1= '(1281)Tables')
    db.dno0main0search.insert( f0= 'aa1296', f1= '(1296)Level 2')
    db.dno0main0search.insert( f0= 'aa1297', f1= '(1297)Level 2')
    db.dno0main0search.insert( f0= 'aa1298', f1= '(1298)Level 3')
    db.dno0main0search.insert( f0= 'aa1299', f1= '(1299)Level 3')
    db.dno0main0search.insert( f0= 'aa1300', f1= '(1300)Level 4')
    db.dno0main0search.insert( f0= 'aa1301', f1= '(1301)Level 4')
    db.dno0main0search.insert( f0= 'aa1302', f1= '(1302)Level 5')
    db.dno0main0search.insert( f0= 'aa1303', f1= '(1303)Level 5')
    db.dno0main0search.insert( f0= 'aa1304', f1= '(1304)Level 5')
    db.dno0main0search.insert( f0= 'aa1305', f1= '(1305)Level 4')
    db.dno0main0search.insert( f0= 'aa1306', f1= '(1306)Level 2')
    db.dno0main0search.insert( f0= 'aa1307', f1= '(1307)Level 1')
    db.dno0main0search.insert( f0= 'aa1308', f1= '(1308)Level 2')
    db.dno0main0search.insert( f0= 'aa1309', f1= '(1309)Level 2')
    db.dno0main0search.insert( f0= 'aa1310', f1= '(1310)Level 2')
    db.dno0main0search.insert( f0= 'hh1311', f1= '(1311)Code')
    db.dno0main0search.insert( f0= 'bu1312', f1= '(1312)&times;')
    db.dno0main0search.insert( f0= 'sp1313', f1= '(1313)Warning!')
    db.dno0main0search.insert( f0= 'sx1314', f1= '(1314)1,4,4,7,5,9,10')
    db.dno0main0search.insert( f0= 'sx1315', f1= '(1315)Loading..')
    db.dno0main0search.insert( f0= 'sx1316', f1= '(1316)Loading..')
    db.dno0main0search.insert( f0= 'sx1317', f1= '(1317)1,3,4,5,3,5')
    db.dno0main0search.insert( f0= 'bu1318', f1= '(1318)Default')
    db.dno0main0search.insert( f0= 'bu1319', f1= '(1319)Primary')
    db.dno0main0search.insert( f0= 'bu1320', f1= '(1320)Info')
    db.dno0main0search.insert( f0= 'bu1321', f1= '(1321)Success')
    db.dno0main0search.insert( f0= 'bu1322', f1= '(1322)Danger')
    db.dno0main0search.insert( f0= 'bu1323', f1= '(1323)Warning')
    db.dno0main0search.insert( f0= 'bu1324', f1= '(1324)Inverse')
    db.dno0main0search.insert( f0= 'bu1325', f1= '(1325)btn-metis-1')
    db.dno0main0search.insert( f0= 'bu1326', f1= '(1326)btn-metis-2')
    db.dno0main0search.insert( f0= 'bu1327', f1= '(1327)btn-metis-3')
    db.dno0main0search.insert( f0= 'bu1328', f1= '(1328)btn-metis-4')
    db.dno0main0search.insert( f0= 'bu1329', f1= '(1329)btn-metis-5')
    db.dno0main0search.insert( f0= 'bu1330', f1= '(1330)btn-metis-6')
    db.dno0main0search.insert( f0= 'si1331', f1= '(1331)20%')
    db.dno0main0search.insert( f0= 'sp1332', f1= '(1332)Default')
    db.dno0main0search.insert( f0= 'si1333', f1= '(1333)40%')
    db.dno0main0search.insert( f0= 'sp1334', f1= '(1334)Success')
    db.dno0main0search.insert( f0= 'si1335', f1= '(1335)60%')
    db.dno0main0search.insert( f0= 'sp1336', f1= '(1336)warning')
    db.dno0main0search.insert( f0= 'si1337', f1= '(1337)80%')
    db.dno0main0search.insert( f0= 'sp1338', f1= '(1338)Danger')
    db.dno0main0search.insert( f0= 'pa1339', f1= '(1339)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dno0main0search.insert( f0= 'bu1340', f1= '(1340)&times;')
    db.dno0main0search.insert( f0= 'hd1341', f1= '(1341)Modal title')
    db.dno0main0search.insert( f0= 'bu1342', f1= '(1342)Close')
    db.commit()
#
