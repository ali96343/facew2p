#
# table for controller: font_themify
#

from gluon.contrib.populate import populate

db.define_table('dfont0themify', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dfont0themify.id ).count():
    db.dfont0themify.insert( f0= 'hc936', f1= '(936)UI elements')
    db.dfont0themify.insert( f0= 'aa938', f1= '(938)Buttons')
    db.dfont0themify.insert( f0= 'aa940', f1= '(940)Badges')
    db.dfont0themify.insert( f0= 'aa942', f1= '(942)Tabs')
    db.dfont0themify.insert( f0= 'aa944', f1= '(944)Social Buttons')
    db.dfont0themify.insert( f0= 'aa946', f1= '(946)Cards')
    db.dfont0themify.insert( f0= 'aa948', f1= '(948)Alerts')
    db.dfont0themify.insert( f0= 'aa950', f1= '(950)Progress Bars')
    db.dfont0themify.insert( f0= 'aa952', f1= '(952)Modals')
    db.dfont0themify.insert( f0= 'aa954', f1= '(954)Switches')
    db.dfont0themify.insert( f0= 'aa956', f1= '(956)Grids')
    db.dfont0themify.insert( f0= 'aa958', f1= '(958)Typography')
    db.dfont0themify.insert( f0= 'aa960', f1= '(960)Basic Table')
    db.dfont0themify.insert( f0= 'aa962', f1= '(962)Data Table')
    db.dfont0themify.insert( f0= 'aa964', f1= '(964)Basic Form')
    db.dfont0themify.insert( f0= 'aa966', f1= '(966)Advanced Form')
    db.dfont0themify.insert( f0= 'hc967', f1= '(967)Icons')
    db.dfont0themify.insert( f0= 'aa969', f1= '(969)Font Awesome')
    db.dfont0themify.insert( f0= 'aa971', f1= '(971)Themefy Icons')
    db.dfont0themify.insert( f0= 'aa974', f1= '(974)Chart JS')
    db.dfont0themify.insert( f0= 'aa976', f1= '(976)Flot Chart')
    db.dfont0themify.insert( f0= 'aa978', f1= '(978)Peity Chart')
    db.dfont0themify.insert( f0= 'aa980', f1= '(980)Google Maps')
    db.dfont0themify.insert( f0= 'aa982', f1= '(982)Vector Maps')
    db.dfont0themify.insert( f0= 'hc983', f1= '(983)Extras')
    db.dfont0themify.insert( f0= 'aa985', f1= '(985)Login')
    db.dfont0themify.insert( f0= 'aa987', f1= '(987)Register')
    db.dfont0themify.insert( f0= 'aa989', f1= '(989)Forget Pass')
    db.dfont0themify.insert( f0= 'pb990', f1= '(990)Search ...')
    db.dfont0themify.insert( f0= 'pc991', f1= '(991)You have 3 Notification')
    db.dfont0themify.insert( f0= 'pc992', f1= '(992)You have 4 Mails')
    db.dfont0themify.insert( f0= 'sx994', f1= '(994)Jonathan Smith')
    db.dfont0themify.insert( f0= 'sx995', f1= '(995)Just now')
    db.dfont0themify.insert( f0= 'pa996', f1= '(996)Hello, this is an example msg')
    db.dfont0themify.insert( f0= 'sx998', f1= '(998)Jack Sanders')
    db.dfont0themify.insert( f0= 'sx999', f1= '(999)5 minutes ago')
    db.dfont0themify.insert( f0= 'pa1000', f1= '(1000)Lorem ipsum dolor sit amet, consectetur')
    db.dfont0themify.insert( f0= 'sx1002', f1= '(1002)Cheryl Wheeler')
    db.dfont0themify.insert( f0= 'sx1003', f1= '(1003)10 minutes ago')
    db.dfont0themify.insert( f0= 'pa1004', f1= '(1004)Hello, this is an example msg')
    db.dfont0themify.insert( f0= 'sx1006', f1= '(1006)Rachel Santos')
    db.dfont0themify.insert( f0= 'sx1007', f1= '(1007)15 minutes ago')
    db.dfont0themify.insert( f0= 'pa1008', f1= '(1008)Lorem ipsum dolor sit amet, consectetur')
    db.dfont0themify.insert( f0= 'sx1010', f1= '(1010)13')
    db.dfont0themify.insert( f0= 'hh1011', f1= '(1011)Dashboard')
    db.dfont0themify.insert( f0= 'aa1012', f1= '(1012)Dashboard')
    db.dfont0themify.insert( f0= 'aa1013', f1= '(1013)Icons')
    db.dfont0themify.insert( f0= 'lb1014', f1= '(1014)Themify')
    db.dfont0themify.insert( f0= 'sx1015', f1= '(1015)ti-arrow-up')
    db.dfont0themify.insert( f0= 'sx1016', f1= '(1016)ti-arrow-right')
    db.dfont0themify.insert( f0= 'sx1017', f1= '(1017)ti-arrow-left')
    db.dfont0themify.insert( f0= 'sx1018', f1= '(1018)ti-arrow-down')
    db.dfont0themify.insert( f0= 'sx1019', f1= '(1019)ti-arrows-vertical')
    db.dfont0themify.insert( f0= 'sx1020', f1= '(1020)ti-arrows-horizontal')
    db.dfont0themify.insert( f0= 'sx1021', f1= '(1021)ti-angle-up')
    db.dfont0themify.insert( f0= 'sx1022', f1= '(1022)ti-angle-right')
    db.dfont0themify.insert( f0= 'sx1023', f1= '(1023)ti-angle-left')
    db.dfont0themify.insert( f0= 'sx1024', f1= '(1024)ti-angle-down')
    db.dfont0themify.insert( f0= 'sx1025', f1= '(1025)ti-angle-double-up')
    db.dfont0themify.insert( f0= 'sx1026', f1= '(1026)ti-angle-double-right')
    db.dfont0themify.insert( f0= 'sx1027', f1= '(1027)ti-angle-double-left')
    db.dfont0themify.insert( f0= 'sx1028', f1= '(1028)ti-angle-double-down')
    db.dfont0themify.insert( f0= 'sx1029', f1= '(1029)ti-move')
    db.dfont0themify.insert( f0= 'sx1030', f1= '(1030)ti-fullscreen')
    db.dfont0themify.insert( f0= 'sx1031', f1= '(1031)ti-arrow-top-right')
    db.dfont0themify.insert( f0= 'sx1032', f1= '(1032)ti-arrow-top-left')
    db.dfont0themify.insert( f0= 'sx1033', f1= '(1033)ti-arrow-circle-up')
    db.dfont0themify.insert( f0= 'sx1034', f1= '(1034)ti-arrow-circle-right')
    db.dfont0themify.insert( f0= 'sx1035', f1= '(1035)ti-arrow-circle-left')
    db.dfont0themify.insert( f0= 'sx1036', f1= '(1036)ti-arrow-circle-down')
    db.dfont0themify.insert( f0= 'sx1037', f1= '(1037)ti-arrows-corner')
    db.dfont0themify.insert( f0= 'sx1038', f1= '(1038)ti-split-v')
    db.dfont0themify.insert( f0= 'sx1039', f1= '(1039)ti-split-v-alt')
    db.dfont0themify.insert( f0= 'sx1040', f1= '(1040)ti-split-h')
    db.dfont0themify.insert( f0= 'sx1041', f1= '(1041)ti-hand-point-up')
    db.dfont0themify.insert( f0= 'sx1042', f1= '(1042)ti-hand-point-right')
    db.dfont0themify.insert( f0= 'sx1043', f1= '(1043)ti-hand-point-left')
    db.dfont0themify.insert( f0= 'sx1044', f1= '(1044)ti-hand-point-down')
    db.dfont0themify.insert( f0= 'sx1045', f1= '(1045)ti-back-right')
    db.dfont0themify.insert( f0= 'sx1046', f1= '(1046)ti-back-left')
    db.dfont0themify.insert( f0= 'sx1047', f1= '(1047)ti-exchange-vertical')
    db.dfont0themify.insert( f0= 'hh1048', f1= '(1048)Web App Icons')
    db.dfont0themify.insert( f0= 'sx1049', f1= '(1049)ti-wand')
    db.dfont0themify.insert( f0= 'sx1050', f1= '(1050)ti-save')
    db.dfont0themify.insert( f0= 'sx1051', f1= '(1051)ti-save-alt')
    db.dfont0themify.insert( f0= 'sx1052', f1= '(1052)ti-direction')
    db.dfont0themify.insert( f0= 'sx1053', f1= '(1053)ti-direction-alt')
    db.dfont0themify.insert( f0= 'sx1054', f1= '(1054)ti-user')
    db.dfont0themify.insert( f0= 'sx1055', f1= '(1055)ti-link')
    db.dfont0themify.insert( f0= 'sx1056', f1= '(1056)ti-unlink')
    db.dfont0themify.insert( f0= 'sx1057', f1= '(1057)ti-trash')
    db.dfont0themify.insert( f0= 'sx1058', f1= '(1058)ti-target')
    db.dfont0themify.insert( f0= 'sx1059', f1= '(1059)ti-tag')
    db.dfont0themify.insert( f0= 'sx1060', f1= '(1060)ti-desktop')
    db.dfont0themify.insert( f0= 'sx1061', f1= '(1061)ti-tablet')
    db.dfont0themify.insert( f0= 'sx1062', f1= '(1062)ti-mobile')
    db.dfont0themify.insert( f0= 'sx1063', f1= '(1063)ti-email')
    db.dfont0themify.insert( f0= 'sx1064', f1= '(1064)ti-star')
    db.dfont0themify.insert( f0= 'sx1065', f1= '(1065)ti-spray')
    db.dfont0themify.insert( f0= 'sx1066', f1= '(1066)ti-signal')
    db.dfont0themify.insert( f0= 'sx1067', f1= '(1067)ti-shopping-cart')
    db.dfont0themify.insert( f0= 'sx1068', f1= '(1068)ti-shopping-cart-full')
    db.dfont0themify.insert( f0= 'sx1069', f1= '(1069)ti-settings')
    db.dfont0themify.insert( f0= 'sx1070', f1= '(1070)ti-search')
    db.dfont0themify.insert( f0= 'sx1071', f1= '(1071)ti-zoom-in')
    db.dfont0themify.insert( f0= 'sx1072', f1= '(1072)ti-zoom-out')
    db.dfont0themify.insert( f0= 'sx1073', f1= '(1073)ti-cut')
    db.dfont0themify.insert( f0= 'sx1074', f1= '(1074)ti-ruler')
    db.dfont0themify.insert( f0= 'sx1075', f1= '(1075)ti-ruler-alt-2')
    db.dfont0themify.insert( f0= 'sx1076', f1= '(1076)ti-ruler-pencil')
    db.dfont0themify.insert( f0= 'sx1077', f1= '(1077)ti-ruler-alt')
    db.dfont0themify.insert( f0= 'sx1078', f1= '(1078)ti-bookmark')
    db.dfont0themify.insert( f0= 'sx1079', f1= '(1079)ti-bookmark-alt')
    db.dfont0themify.insert( f0= 'sx1080', f1= '(1080)ti-reload')
    db.dfont0themify.insert( f0= 'sx1081', f1= '(1081)ti-plus')
    db.dfont0themify.insert( f0= 'sx1082', f1= '(1082)ti-minus')
    db.dfont0themify.insert( f0= 'sx1083', f1= '(1083)ti-close')
    db.dfont0themify.insert( f0= 'sx1084', f1= '(1084)ti-pin')
    db.dfont0themify.insert( f0= 'sx1085', f1= '(1085)ti-pencil')
    db.dfont0themify.insert( f0= 'sx1086', f1= '(1086)ti-pencil-alt')
    db.dfont0themify.insert( f0= 'sx1087', f1= '(1087)ti-paint-roller')
    db.dfont0themify.insert( f0= 'sx1088', f1= '(1088)ti-paint-bucket')
    db.dfont0themify.insert( f0= 'sx1089', f1= '(1089)ti-na')
    db.dfont0themify.insert( f0= 'sx1090', f1= '(1090)ti-medall')
    db.dfont0themify.insert( f0= 'sx1091', f1= '(1091)ti-medall-alt')
    db.dfont0themify.insert( f0= 'sx1092', f1= '(1092)ti-marker')
    db.dfont0themify.insert( f0= 'sx1093', f1= '(1093)ti-marker-alt')
    db.dfont0themify.insert( f0= 'sx1094', f1= '(1094)ti-lock')
    db.dfont0themify.insert( f0= 'sx1095', f1= '(1095)ti-unlock')
    db.dfont0themify.insert( f0= 'sx1096', f1= '(1096)ti-location-arrow')
    db.dfont0themify.insert( f0= 'sx1097', f1= '(1097)ti-layout')
    db.dfont0themify.insert( f0= 'sx1098', f1= '(1098)ti-layers')
    db.dfont0themify.insert( f0= 'sx1099', f1= '(1099)ti-layers-alt')
    db.dfont0themify.insert( f0= 'sx1100', f1= '(1100)ti-key')
    db.dfont0themify.insert( f0= 'sx1101', f1= '(1101)ti-image')
    db.dfont0themify.insert( f0= 'sx1102', f1= '(1102)ti-heart')
    db.dfont0themify.insert( f0= 'sx1103', f1= '(1103)ti-heart-broken')
    db.dfont0themify.insert( f0= 'sx1104', f1= '(1104)ti-hand-stop')
    db.dfont0themify.insert( f0= 'sx1105', f1= '(1105)ti-hand-open')
    db.dfont0themify.insert( f0= 'sx1106', f1= '(1106)ti-hand-drag')
    db.dfont0themify.insert( f0= 'sx1107', f1= '(1107)ti-flag')
    db.dfont0themify.insert( f0= 'sx1108', f1= '(1108)ti-flag-alt')
    db.dfont0themify.insert( f0= 'sx1109', f1= '(1109)ti-flag-alt-2')
    db.dfont0themify.insert( f0= 'sx1110', f1= '(1110)ti-eye')
    db.dfont0themify.insert( f0= 'sx1111', f1= '(1111)ti-import')
    db.dfont0themify.insert( f0= 'sx1112', f1= '(1112)ti-export')
    db.dfont0themify.insert( f0= 'sx1113', f1= '(1113)ti-cup')
    db.dfont0themify.insert( f0= 'sx1114', f1= '(1114)ti-crown')
    db.dfont0themify.insert( f0= 'sx1115', f1= '(1115)ti-comments')
    db.dfont0themify.insert( f0= 'sx1116', f1= '(1116)ti-comment')
    db.dfont0themify.insert( f0= 'sx1117', f1= '(1117)ti-comment-alt')
    db.dfont0themify.insert( f0= 'sx1118', f1= '(1118)ti-thought')
    db.dfont0themify.insert( f0= 'sx1119', f1= '(1119)ti-clip')
    db.dfont0themify.insert( f0= 'sx1120', f1= '(1120)ti-check')
    db.dfont0themify.insert( f0= 'sx1121', f1= '(1121)ti-check-box')
    db.dfont0themify.insert( f0= 'sx1122', f1= '(1122)ti-camera')
    db.dfont0themify.insert( f0= 'sx1123', f1= '(1123)ti-announcement')
    db.dfont0themify.insert( f0= 'sx1124', f1= '(1124)ti-brush')
    db.dfont0themify.insert( f0= 'sx1125', f1= '(1125)ti-brush-alt')
    db.dfont0themify.insert( f0= 'sx1126', f1= '(1126)ti-palette')
    db.dfont0themify.insert( f0= 'sx1127', f1= '(1127)ti-briefcase')
    db.dfont0themify.insert( f0= 'sx1128', f1= '(1128)ti-bolt')
    db.dfont0themify.insert( f0= 'sx1129', f1= '(1129)ti-bolt-alt')
    db.dfont0themify.insert( f0= 'sx1130', f1= '(1130)ti-blackboard')
    db.dfont0themify.insert( f0= 'sx1131', f1= '(1131)ti-bag')
    db.dfont0themify.insert( f0= 'sx1132', f1= '(1132)ti-world')
    db.dfont0themify.insert( f0= 'sx1133', f1= '(1133)ti-wheelchair')
    db.dfont0themify.insert( f0= 'sx1134', f1= '(1134)ti-car')
    db.dfont0themify.insert( f0= 'sx1135', f1= '(1135)ti-truck')
    db.dfont0themify.insert( f0= 'sx1136', f1= '(1136)ti-timer')
    db.dfont0themify.insert( f0= 'sx1137', f1= '(1137)ti-ticket')
    db.dfont0themify.insert( f0= 'sx1138', f1= '(1138)ti-thumb-up')
    db.dfont0themify.insert( f0= 'sx1139', f1= '(1139)ti-thumb-down')
    db.dfont0themify.insert( f0= 'sx1140', f1= '(1140)ti-stats-up')
    db.dfont0themify.insert( f0= 'sx1141', f1= '(1141)ti-stats-down')
    db.dfont0themify.insert( f0= 'sx1142', f1= '(1142)ti-shine')
    db.dfont0themify.insert( f0= 'sx1143', f1= '(1143)ti-shift-right')
    db.dfont0themify.insert( f0= 'sx1144', f1= '(1144)ti-shift-left')
    db.dfont0themify.insert( f0= 'sx1145', f1= '(1145)ti-shift-right-alt')
    db.dfont0themify.insert( f0= 'sx1146', f1= '(1146)ti-shift-left-alt')
    db.dfont0themify.insert( f0= 'sx1147', f1= '(1147)ti-shield')
    db.dfont0themify.insert( f0= 'sx1148', f1= '(1148)ti-notepad')
    db.dfont0themify.insert( f0= 'sx1149', f1= '(1149)ti-server')
    db.dfont0themify.insert( f0= 'sx1150', f1= '(1150)ti-pulse')
    db.dfont0themify.insert( f0= 'sx1151', f1= '(1151)ti-printer')
    db.dfont0themify.insert( f0= 'sx1152', f1= '(1152)ti-power-off')
    db.dfont0themify.insert( f0= 'sx1153', f1= '(1153)ti-plug')
    db.dfont0themify.insert( f0= 'sx1154', f1= '(1154)ti-pie-chart')
    db.dfont0themify.insert( f0= 'sx1155', f1= '(1155)ti-panel')
    db.dfont0themify.insert( f0= 'sx1156', f1= '(1156)ti-package')
    db.dfont0themify.insert( f0= 'sx1157', f1= '(1157)ti-music')
    db.dfont0themify.insert( f0= 'sx1158', f1= '(1158)ti-music-alt')
    db.dfont0themify.insert( f0= 'sx1159', f1= '(1159)ti-mouse')
    db.dfont0themify.insert( f0= 'sx1160', f1= '(1160)ti-mouse-alt')
    db.dfont0themify.insert( f0= 'sx1161', f1= '(1161)ti-money')
    db.dfont0themify.insert( f0= 'sx1162', f1= '(1162)ti-microphone')
    db.dfont0themify.insert( f0= 'sx1163', f1= '(1163)ti-menu')
    db.dfont0themify.insert( f0= 'sx1164', f1= '(1164)ti-menu-alt')
    db.dfont0themify.insert( f0= 'sx1165', f1= '(1165)ti-map')
    db.dfont0themify.insert( f0= 'sx1166', f1= '(1166)ti-map-alt')
    db.dfont0themify.insert( f0= 'sx1167', f1= '(1167)ti-location-pin')
    db.dfont0themify.insert( f0= 'sx1168', f1= '(1168)ti-light-bulb')
    db.dfont0themify.insert( f0= 'sx1169', f1= '(1169)ti-info')
    db.dfont0themify.insert( f0= 'sx1170', f1= '(1170)ti-infinite')
    db.dfont0themify.insert( f0= 'sx1171', f1= '(1171)ti-id-badge')
    db.dfont0themify.insert( f0= 'sx1172', f1= '(1172)ti-hummer')
    db.dfont0themify.insert( f0= 'sx1173', f1= '(1173)ti-home')
    db.dfont0themify.insert( f0= 'sx1174', f1= '(1174)ti-help')
    db.dfont0themify.insert( f0= 'sx1175', f1= '(1175)ti-headphone')
    db.dfont0themify.insert( f0= 'sx1176', f1= '(1176)ti-harddrives')
    db.dfont0themify.insert( f0= 'sx1177', f1= '(1177)ti-harddrive')
    db.dfont0themify.insert( f0= 'sx1178', f1= '(1178)ti-gift')
    db.dfont0themify.insert( f0= 'sx1179', f1= '(1179)ti-game')
    db.dfont0themify.insert( f0= 'sx1180', f1= '(1180)ti-filter')
    db.dfont0themify.insert( f0= 'sx1181', f1= '(1181)ti-files')
    db.dfont0themify.insert( f0= 'sx1182', f1= '(1182)ti-file')
    db.dfont0themify.insert( f0= 'sx1183', f1= '(1183)ti-zip')
    db.dfont0themify.insert( f0= 'sx1184', f1= '(1184)ti-folder')
    db.dfont0themify.insert( f0= 'sx1185', f1= '(1185)ti-envelope')
    db.dfont0themify.insert( f0= 'sx1186', f1= '(1186)ti-dashboard')
    db.dfont0themify.insert( f0= 'sx1187', f1= '(1187)ti-cloud')
    db.dfont0themify.insert( f0= 'sx1188', f1= '(1188)ti-cloud-up')
    db.dfont0themify.insert( f0= 'sx1189', f1= '(1189)ti-cloud-down')
    db.dfont0themify.insert( f0= 'sx1190', f1= '(1190)ti-clipboard')
    db.dfont0themify.insert( f0= 'sx1191', f1= '(1191)ti-calendar')
    db.dfont0themify.insert( f0= 'sx1192', f1= '(1192)ti-book')
    db.dfont0themify.insert( f0= 'sx1193', f1= '(1193)ti-bell')
    db.dfont0themify.insert( f0= 'sx1194', f1= '(1194)ti-basketball')
    db.dfont0themify.insert( f0= 'sx1195', f1= '(1195)ti-bar-chart')
    db.dfont0themify.insert( f0= 'sx1196', f1= '(1196)ti-bar-chart-alt')
    db.dfont0themify.insert( f0= 'sx1197', f1= '(1197)ti-archive')
    db.dfont0themify.insert( f0= 'sx1198', f1= '(1198)ti-anchor')
    db.dfont0themify.insert( f0= 'sx1199', f1= '(1199)ti-alert')
    db.dfont0themify.insert( f0= 'sx1200', f1= '(1200)ti-alarm-clock')
    db.dfont0themify.insert( f0= 'sx1201', f1= '(1201)ti-agenda')
    db.dfont0themify.insert( f0= 'sx1202', f1= '(1202)ti-write')
    db.dfont0themify.insert( f0= 'sx1203', f1= '(1203)ti-wallet')
    db.dfont0themify.insert( f0= 'sx1204', f1= '(1204)ti-video-clapper')
    db.dfont0themify.insert( f0= 'sx1205', f1= '(1205)ti-video-camera')
    db.dfont0themify.insert( f0= 'sx1206', f1= '(1206)ti-vector')
    db.dfont0themify.insert( f0= 'sx1207', f1= '(1207)ti-support')
    db.dfont0themify.insert( f0= 'sx1208', f1= '(1208)ti-stamp')
    db.dfont0themify.insert( f0= 'sx1209', f1= '(1209)ti-slice')
    db.dfont0themify.insert( f0= 'sx1210', f1= '(1210)ti-shortcode')
    db.dfont0themify.insert( f0= 'sx1211', f1= '(1211)ti-receipt')
    db.dfont0themify.insert( f0= 'sx1212', f1= '(1212)ti-pin2')
    db.dfont0themify.insert( f0= 'sx1213', f1= '(1213)ti-pin-alt')
    db.dfont0themify.insert( f0= 'sx1214', f1= '(1214)ti-pencil-alt2')
    db.dfont0themify.insert( f0= 'sx1215', f1= '(1215)ti-eraser')
    db.dfont0themify.insert( f0= 'sx1216', f1= '(1216)ti-more')
    db.dfont0themify.insert( f0= 'sx1217', f1= '(1217)ti-more-alt')
    db.dfont0themify.insert( f0= 'sx1218', f1= '(1218)ti-microphone-alt')
    db.dfont0themify.insert( f0= 'sx1219', f1= '(1219)ti-magnet')
    db.dfont0themify.insert( f0= 'sx1220', f1= '(1220)ti-line-double')
    db.dfont0themify.insert( f0= 'sx1221', f1= '(1221)ti-line-dotted')
    db.dfont0themify.insert( f0= 'sx1222', f1= '(1222)ti-line-dashed')
    db.dfont0themify.insert( f0= 'sx1223', f1= '(1223)ti-ink-pen')
    db.dfont0themify.insert( f0= 'sx1224', f1= '(1224)ti-info-alt')
    db.dfont0themify.insert( f0= 'sx1225', f1= '(1225)ti-help-alt')
    db.dfont0themify.insert( f0= 'sx1226', f1= '(1226)ti-headphone-alt')
    db.dfont0themify.insert( f0= 'sx1227', f1= '(1227)ti-gallery')
    db.dfont0themify.insert( f0= 'sx1228', f1= '(1228)ti-face-smile')
    db.dfont0themify.insert( f0= 'sx1229', f1= '(1229)ti-face-sad')
    db.dfont0themify.insert( f0= 'sx1230', f1= '(1230)ti-credit-card')
    db.dfont0themify.insert( f0= 'sx1231', f1= '(1231)ti-comments-smiley')
    db.dfont0themify.insert( f0= 'sx1232', f1= '(1232)ti-time')
    db.dfont0themify.insert( f0= 'sx1233', f1= '(1233)ti-share')
    db.dfont0themify.insert( f0= 'sx1234', f1= '(1234)ti-share-alt')
    db.dfont0themify.insert( f0= 'sx1235', f1= '(1235)ti-rocket')
    db.dfont0themify.insert( f0= 'sx1236', f1= '(1236)ti-new-window')
    db.dfont0themify.insert( f0= 'sx1237', f1= '(1237)ti-rss')
    db.dfont0themify.insert( f0= 'sx1238', f1= '(1238)ti-rss-alt')
    db.dfont0themify.insert( f0= 'hh1239', f1= '(1239)Control Icons')
    db.dfont0themify.insert( f0= 'sx1240', f1= '(1240)ti-control-stop')
    db.dfont0themify.insert( f0= 'sx1241', f1= '(1241)ti-control-shuffle')
    db.dfont0themify.insert( f0= 'sx1242', f1= '(1242)ti-control-play')
    db.dfont0themify.insert( f0= 'sx1243', f1= '(1243)ti-control-pause')
    db.dfont0themify.insert( f0= 'sx1244', f1= '(1244)ti-control-forward')
    db.dfont0themify.insert( f0= 'sx1245', f1= '(1245)ti-control-backward')
    db.dfont0themify.insert( f0= 'sx1246', f1= '(1246)ti-volume')
    db.dfont0themify.insert( f0= 'sx1247', f1= '(1247)ti-control-skip-forward')
    db.dfont0themify.insert( f0= 'sx1248', f1= '(1248)ti-control-skip-backward')
    db.dfont0themify.insert( f0= 'sx1249', f1= '(1249)ti-control-record')
    db.dfont0themify.insert( f0= 'sx1250', f1= '(1250)ti-control-eject')
    db.dfont0themify.insert( f0= 'hh1251', f1= '(1251)Text Editor')
    db.dfont0themify.insert( f0= 'sx1252', f1= '(1252)ti-paragraph')
    db.dfont0themify.insert( f0= 'sx1253', f1= '(1253)ti-uppercase')
    db.dfont0themify.insert( f0= 'sx1254', f1= '(1254)ti-underline')
    db.dfont0themify.insert( f0= 'sx1255', f1= '(1255)ti-text')
    db.dfont0themify.insert( f0= 'sx1256', f1= '(1256)ti-Italic')
    db.dfont0themify.insert( f0= 'sx1257', f1= '(1257)ti-smallcap')
    db.dfont0themify.insert( f0= 'sx1258', f1= '(1258)ti-list')
    db.dfont0themify.insert( f0= 'sx1259', f1= '(1259)ti-list-ol')
    db.dfont0themify.insert( f0= 'sx1260', f1= '(1260)ti-align-right')
    db.dfont0themify.insert( f0= 'sx1261', f1= '(1261)ti-align-left')
    db.dfont0themify.insert( f0= 'sx1262', f1= '(1262)ti-align-justify')
    db.dfont0themify.insert( f0= 'sx1263', f1= '(1263)ti-align-center')
    db.dfont0themify.insert( f0= 'sx1264', f1= '(1264)ti-quote-right')
    db.dfont0themify.insert( f0= 'sx1265', f1= '(1265)ti-quote-left')
    db.dfont0themify.insert( f0= 'hh1266', f1= '(1266)Layout Icons')
    db.dfont0themify.insert( f0= 'sx1267', f1= '(1267)ti-layout-width-full')
    db.dfont0themify.insert( f0= 'sx1268', f1= '(1268)ti-layout-width-default')
    db.dfont0themify.insert( f0= 'sx1269', f1= '(1269)ti-layout-width-default-alt')
    db.dfont0themify.insert( f0= 'sx1270', f1= '(1270)ti-layout-tab')
    db.dfont0themify.insert( f0= 'sx1271', f1= '(1271)ti-layout-tab-window')
    db.dfont0themify.insert( f0= 'sx1272', f1= '(1272)ti-layout-tab-v')
    db.dfont0themify.insert( f0= 'sx1273', f1= '(1273)ti-layout-tab-min')
    db.dfont0themify.insert( f0= 'sx1274', f1= '(1274)ti-layout-slider')
    db.dfont0themify.insert( f0= 'sx1275', f1= '(1275)ti-layout-slider-alt')
    db.dfont0themify.insert( f0= 'sx1276', f1= '(1276)ti-layout-sidebar-right')
    db.dfont0themify.insert( f0= 'sx1277', f1= '(1277)ti-layout-sidebar-none')
    db.dfont0themify.insert( f0= 'sx1278', f1= '(1278)ti-layout-sidebar-left')
    db.dfont0themify.insert( f0= 'sx1279', f1= '(1279)ti-layout-placeholder')
    db.dfont0themify.insert( f0= 'sx1280', f1= '(1280)ti-layout-menu')
    db.dfont0themify.insert( f0= 'sx1281', f1= '(1281)ti-layout-menu-v')
    db.dfont0themify.insert( f0= 'sx1282', f1= '(1282)ti-layout-menu-separated')
    db.dfont0themify.insert( f0= 'sx1283', f1= '(1283)ti-layout-menu-full')
    db.dfont0themify.insert( f0= 'sx1284', f1= '(1284)ti-layout-media-right')
    db.dfont0themify.insert( f0= 'sx1285', f1= '(1285)ti-layout-media-right-alt')
    db.dfont0themify.insert( f0= 'sx1286', f1= '(1286)ti-layout-media-overlay')
    db.dfont0themify.insert( f0= 'sx1287', f1= '(1287)ti-layout-media-overlay-alt')
    db.dfont0themify.insert( f0= 'sx1288', f1= '(1288)ti-layout-media-overlay-alt-2')
    db.dfont0themify.insert( f0= 'sx1289', f1= '(1289)ti-layout-media-left')
    db.dfont0themify.insert( f0= 'sx1290', f1= '(1290)ti-layout-media-left-alt')
    db.dfont0themify.insert( f0= 'sx1291', f1= '(1291)ti-layout-media-center')
    db.dfont0themify.insert( f0= 'sx1292', f1= '(1292)ti-layout-media-center-alt')
    db.dfont0themify.insert( f0= 'sx1293', f1= '(1293)ti-layout-list-thumb')
    db.dfont0themify.insert( f0= 'sx1294', f1= '(1294)ti-layout-list-thumb-alt')
    db.dfont0themify.insert( f0= 'sx1295', f1= '(1295)ti-layout-list-post')
    db.dfont0themify.insert( f0= 'sx1296', f1= '(1296)ti-layout-list-large-image')
    db.dfont0themify.insert( f0= 'sx1297', f1= '(1297)ti-layout-line-solid')
    db.dfont0themify.insert( f0= 'sx1298', f1= '(1298)ti-layout-grid4')
    db.dfont0themify.insert( f0= 'sx1299', f1= '(1299)ti-layout-grid3')
    db.dfont0themify.insert( f0= 'sx1300', f1= '(1300)ti-layout-grid2')
    db.dfont0themify.insert( f0= 'sx1301', f1= '(1301)ti-layout-grid2-thumb')
    db.dfont0themify.insert( f0= 'sx1302', f1= '(1302)ti-layout-cta-right')
    db.dfont0themify.insert( f0= 'sx1303', f1= '(1303)ti-layout-cta-left')
    db.dfont0themify.insert( f0= 'sx1304', f1= '(1304)ti-layout-cta-center')
    db.dfont0themify.insert( f0= 'sx1305', f1= '(1305)ti-layout-cta-btn-right')
    db.dfont0themify.insert( f0= 'sx1306', f1= '(1306)ti-layout-cta-btn-left')
    db.dfont0themify.insert( f0= 'sx1307', f1= '(1307)ti-layout-column4')
    db.dfont0themify.insert( f0= 'sx1308', f1= '(1308)ti-layout-column3')
    db.dfont0themify.insert( f0= 'sx1309', f1= '(1309)ti-layout-column2')
    db.dfont0themify.insert( f0= 'sx1310', f1= '(1310)ti-layout-accordion-separated')
    db.dfont0themify.insert( f0= 'sx1311', f1= '(1311)ti-layout-accordion-merged')
    db.dfont0themify.insert( f0= 'sx1312', f1= '(1312)ti-layout-accordion-list')
    db.dfont0themify.insert( f0= 'sx1313', f1= '(1313)ti-widgetized')
    db.dfont0themify.insert( f0= 'sx1314', f1= '(1314)ti-widget')
    db.dfont0themify.insert( f0= 'sx1315', f1= '(1315)ti-widget-alt')
    db.dfont0themify.insert( f0= 'sx1316', f1= '(1316)ti-view-list')
    db.dfont0themify.insert( f0= 'sx1317', f1= '(1317)ti-view-list-alt')
    db.dfont0themify.insert( f0= 'sx1318', f1= '(1318)ti-view-grid')
    db.dfont0themify.insert( f0= 'sx1319', f1= '(1319)ti-upload')
    db.dfont0themify.insert( f0= 'sx1320', f1= '(1320)ti-download')
    db.dfont0themify.insert( f0= 'sx1321', f1= '(1321)ti-loop')
    db.dfont0themify.insert( f0= 'sx1322', f1= '(1322)ti-layout-sidebar-2')
    db.dfont0themify.insert( f0= 'sx1323', f1= '(1323)ti-layout-grid4-alt')
    db.dfont0themify.insert( f0= 'sx1324', f1= '(1324)ti-layout-grid3-alt')
    db.dfont0themify.insert( f0= 'sx1325', f1= '(1325)ti-layout-grid2-alt')
    db.dfont0themify.insert( f0= 'sx1326', f1= '(1326)ti-layout-column4-alt')
    db.dfont0themify.insert( f0= 'sx1327', f1= '(1327)ti-layout-column3-alt')
    db.dfont0themify.insert( f0= 'sx1328', f1= '(1328)ti-layout-column2-alt')
    db.dfont0themify.insert( f0= 'hh1329', f1= '(1329)Brand Icons')
    db.dfont0themify.insert( f0= 'sx1330', f1= '(1330)ti-flickr')
    db.dfont0themify.insert( f0= 'sx1331', f1= '(1331)ti-flickr-alt')
    db.dfont0themify.insert( f0= 'sx1332', f1= '(1332)ti-instagram')
    db.dfont0themify.insert( f0= 'sx1333', f1= '(1333)ti-google')
    db.dfont0themify.insert( f0= 'sx1334', f1= '(1334)ti-github')
    db.dfont0themify.insert( f0= 'sx1335', f1= '(1335)ti-facebook')
    db.dfont0themify.insert( f0= 'sx1336', f1= '(1336)ti-dropbox')
    db.dfont0themify.insert( f0= 'sx1337', f1= '(1337)ti-dropbox-alt')
    db.dfont0themify.insert( f0= 'sx1338', f1= '(1338)ti-dribbble')
    db.dfont0themify.insert( f0= 'sx1339', f1= '(1339)ti-apple')
    db.dfont0themify.insert( f0= 'sx1340', f1= '(1340)ti-android')
    db.dfont0themify.insert( f0= 'sx1341', f1= '(1341)ti-yahoo')
    db.dfont0themify.insert( f0= 'sx1342', f1= '(1342)ti-trello')
    db.dfont0themify.insert( f0= 'sx1343', f1= '(1343)ti-stack-overflow')
    db.dfont0themify.insert( f0= 'sx1344', f1= '(1344)ti-soundcloud')
    db.dfont0themify.insert( f0= 'sx1345', f1= '(1345)ti-sharethis')
    db.dfont0themify.insert( f0= 'sx1346', f1= '(1346)ti-sharethis-alt')
    db.dfont0themify.insert( f0= 'sx1347', f1= '(1347)ti-reddit')
    db.dfont0themify.insert( f0= 'sx1348', f1= '(1348)ti-microsoft')
    db.dfont0themify.insert( f0= 'sx1349', f1= '(1349)ti-microsoft-alt')
    db.dfont0themify.insert( f0= 'sx1350', f1= '(1350)ti-linux')
    db.dfont0themify.insert( f0= 'sx1351', f1= '(1351)ti-jsfiddle')
    db.dfont0themify.insert( f0= 'sx1352', f1= '(1352)ti-joomla')
    db.dfont0themify.insert( f0= 'sx1353', f1= '(1353)ti-html5')
    db.dfont0themify.insert( f0= 'sx1354', f1= '(1354)ti-css3')
    db.dfont0themify.insert( f0= 'sx1355', f1= '(1355)ti-drupal')
    db.dfont0themify.insert( f0= 'sx1356', f1= '(1356)ti-wordpress')
    db.dfont0themify.insert( f0= 'sx1357', f1= '(1357)ti-tumblr')
    db.dfont0themify.insert( f0= 'sx1358', f1= '(1358)ti-tumblr-alt')
    db.dfont0themify.insert( f0= 'sx1359', f1= '(1359)ti-skype')
    db.dfont0themify.insert( f0= 'sx1360', f1= '(1360)ti-youtube')
    db.dfont0themify.insert( f0= 'sx1361', f1= '(1361)ti-vimeo')
    db.dfont0themify.insert( f0= 'sx1362', f1= '(1362)ti-vimeo-alt')
    db.dfont0themify.insert( f0= 'sx1363', f1= '(1363)ti-twitter')
    db.dfont0themify.insert( f0= 'sx1364', f1= '(1364)ti-twitter-alt')
    db.dfont0themify.insert( f0= 'sx1365', f1= '(1365)ti-linkedin')
    db.dfont0themify.insert( f0= 'sx1366', f1= '(1366)ti-pinterest')
    db.dfont0themify.insert( f0= 'sx1367', f1= '(1367)ti-pinterest-alt')
    db.dfont0themify.insert( f0= 'sx1368', f1= '(1368)ti-themify-logo')
    db.dfont0themify.insert( f0= 'sx1369', f1= '(1369)ti-themify-favicon')
    db.dfont0themify.insert( f0= 'sx1370', f1= '(1370)ti-themify-favicon-alt')
    db.commit()
#
