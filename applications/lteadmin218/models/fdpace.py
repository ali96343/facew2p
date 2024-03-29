#
# table for controller: pace
#

from gluon.contrib.populate import populate

db.define_table('dpace', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dpace.id ).count():
    db.dpace.insert( f0= 'bb1101', f1= '(1101)A')
    db.dpace.insert( f0= 'sx1102', f1= '(1102)LT')
    db.dpace.insert( f0= 'bb1103', f1= '(1103)Admin')
    db.dpace.insert( f0= 'sx1104', f1= '(1104)LTE')
    db.dpace.insert( f0= 'sx1105', f1= '(1105)Toggle navigation')
    db.dpace.insert( f0= 'sx1106', f1= '(1106)4')
    db.dpace.insert( f0= 'lb1107', f1= '(1107)You have 4 messages')
    db.dpace.insert( f0= 'ib1109', f1= '(1109)5 mins')
    db.dpace.insert( f0= 'pa1110', f1= '(1110)Why not buy a new awesome theme?')
    db.dpace.insert( f0= 'aa1111', f1= '(1111)See All Messages')
    db.dpace.insert( f0= 'lb1112', f1= '(1112)You have 10 notifications')
    db.dpace.insert( f0= 'aa1113', f1= '(1113)View all')
    db.dpace.insert( f0= 'sx1114', f1= '(1114)9')
    db.dpace.insert( f0= 'lb1115', f1= '(1115)You have 9 tasks')
    db.dpace.insert( f0= 'sx1116', f1= '(1116)20% Complete')
    db.dpace.insert( f0= 'aa1117', f1= '(1117)View all tasks')
    db.dpace.insert( f0= 'sx1119', f1= '(1119)Alexander Pierce')
    db.dpace.insert( f0= 'ic1121', f1= '(1121)Member since Nov. 2012')
    db.dpace.insert( f0= 'aa1122', f1= '(1122)Followers')
    db.dpace.insert( f0= 'aa1123', f1= '(1123)Sales')
    db.dpace.insert( f0= 'aa1124', f1= '(1124)Friends')
    db.dpace.insert( f0= 'aa1125', f1= '(1125)Profile')
    db.dpace.insert( f0= 'aa1126', f1= '(1126)Sign out')
    db.dpace.insert( f0= 'pa1128', f1= '(1128)Alexander Pierce')
    db.dpace.insert( f0= 'ia1129', f1= '(1129)Online')
    db.dpace.insert( f0= 'pb1130', f1= '(1130)Search...')
    db.dpace.insert( f0= 'lb1131', f1= '(1131)MAIN NAVIGATION')
    db.dpace.insert( f0= 'sp1132', f1= '(1132)Dashboard')
    db.dpace.insert( f0= 'ia1134', f1= '(1134)Dashboard v1')
    db.dpace.insert( f0= 'ia1136', f1= '(1136)Dashboard v2')
    db.dpace.insert( f0= 'sp1137', f1= '(1137)Layout Options')
    db.dpace.insert( f0= 'sx1138', f1= '(1138)4')
    db.dpace.insert( f0= 'ia1140', f1= '(1140)Top Navigation')
    db.dpace.insert( f0= 'ia1142', f1= '(1142)Boxed')
    db.dpace.insert( f0= 'ia1144', f1= '(1144)Fixed')
    db.dpace.insert( f0= 'ia1146', f1= '(1146)Collapsed Sidebar')
    db.dpace.insert( f0= 'sp1148', f1= '(1148)Widgets')
    db.dpace.insert( f0= 'ic1149', f1= '(1149)Hot')
    db.dpace.insert( f0= 'sp1150', f1= '(1150)Charts')
    db.dpace.insert( f0= 'ia1152', f1= '(1152)ChartJS')
    db.dpace.insert( f0= 'ia1154', f1= '(1154)Morris')
    db.dpace.insert( f0= 'ia1156', f1= '(1156)Flot')
    db.dpace.insert( f0= 'ia1158', f1= '(1158)Inline charts')
    db.dpace.insert( f0= 'sp1159', f1= '(1159)UI Elements')
    db.dpace.insert( f0= 'ia1161', f1= '(1161)General')
    db.dpace.insert( f0= 'ia1163', f1= '(1163)Icons')
    db.dpace.insert( f0= 'ia1165', f1= '(1165)Buttons')
    db.dpace.insert( f0= 'ia1167', f1= '(1167)Sliders')
    db.dpace.insert( f0= 'ia1169', f1= '(1169)Timeline')
    db.dpace.insert( f0= 'ia1171', f1= '(1171)Modals')
    db.dpace.insert( f0= 'sp1172', f1= '(1172)Forms')
    db.dpace.insert( f0= 'ia1174', f1= '(1174)General Elements')
    db.dpace.insert( f0= 'ia1176', f1= '(1176)Advanced Elements')
    db.dpace.insert( f0= 'ia1178', f1= '(1178)Editors')
    db.dpace.insert( f0= 'sp1179', f1= '(1179)Tables')
    db.dpace.insert( f0= 'ia1181', f1= '(1181)Simple tables')
    db.dpace.insert( f0= 'ia1183', f1= '(1183)Data tables')
    db.dpace.insert( f0= 'sp1185', f1= '(1185)Calendar')
    db.dpace.insert( f0= 'ic1186', f1= '(1186)3')
    db.dpace.insert( f0= 'sp1188', f1= '(1188)Mailbox')
    db.dpace.insert( f0= 'ic1189', f1= '(1189)5')
    db.dpace.insert( f0= 'sp1190', f1= '(1190)Examples')
    db.dpace.insert( f0= 'ia1192', f1= '(1192)Invoice')
    db.dpace.insert( f0= 'ia1194', f1= '(1194)Profile')
    db.dpace.insert( f0= 'ia1196', f1= '(1196)Login')
    db.dpace.insert( f0= 'ia1198', f1= '(1198)Register')
    db.dpace.insert( f0= 'ia1200', f1= '(1200)Lockscreen')
    db.dpace.insert( f0= 'ia1202', f1= '(1202)404 Error')
    db.dpace.insert( f0= 'ia1204', f1= '(1204)500 Error')
    db.dpace.insert( f0= 'ia1206', f1= '(1206)Blank Page')
    db.dpace.insert( f0= 'ia1208', f1= '(1208)Pace Page')
    db.dpace.insert( f0= 'sp1209', f1= '(1209)Multilevel')
    db.dpace.insert( f0= 'ia1210', f1= '(1210)Level One')
    db.dpace.insert( f0= 'ia1211', f1= '(1211)Level Two')
    db.dpace.insert( f0= 'ia1212', f1= '(1212)Level Three')
    db.dpace.insert( f0= 'ia1213', f1= '(1213)Level Three')
    db.dpace.insert( f0= 'ia1214', f1= '(1214)Level One')
    db.dpace.insert( f0= 'sp1215', f1= '(1215)Documentation')
    db.dpace.insert( f0= 'lb1216', f1= '(1216)LABELS')
    db.dpace.insert( f0= 'sp1217', f1= '(1217)Important')
    db.dpace.insert( f0= 'sp1218', f1= '(1218)Warning')
    db.dpace.insert( f0= 'sp1219', f1= '(1219)Information')
    db.dpace.insert( f0= 'ic1220', f1= '(1220)Loading example')
    db.dpace.insert( f0= 'ia1221', f1= '(1221)Home')
    db.dpace.insert( f0= 'aa1222', f1= '(1222)Examples')
    db.dpace.insert( f0= 'lb1223', f1= '(1223)Pace page')
    db.dpace.insert( f0= 'hc1224', f1= '(1224)Title')
    db.dpace.insert( f0= 'bb1225', f1= '(1225)Version')
    db.dpace.insert( f0= 'aa1226', f1= '(1226)AdminLTE')
    db.dpace.insert( f0= 'hc1227', f1= '(1227)Recent Activity')
    db.dpace.insert( f0= 'hd1228', f1= '(1228)Langdon s Birthday')
    db.dpace.insert( f0= 'pa1229', f1= '(1229)Will be 23 on April 24th')
    db.dpace.insert( f0= 'hd1230', f1= '(1230)Frodo Updated His Profile')
    db.dpace.insert( f0= 'pa1231', f1= '(1231)New phone +1(800)555-1234')
    db.dpace.insert( f0= 'hd1232', f1= '(1232)Nora Joined Mailing List')
    db.dpace.insert( f0= 'pa1233', f1= '(1233)nora@example.com')
    db.dpace.insert( f0= 'hd1234', f1= '(1234)Cron Job 254 Executed')
    db.dpace.insert( f0= 'pa1235', f1= '(1235)Execution time 5 seconds')
    db.dpace.insert( f0= 'hc1236', f1= '(1236)Tasks Progress')
    db.dpace.insert( f0= 'di1237', f1= '(1237)Stats Tab Content')
    db.dpace.insert( f0= 'hc1238', f1= '(1238)General Settings')
    db.dpace.insert( f0= 'hc1239', f1= '(1239)Chat Settings')
    db.commit()
#
