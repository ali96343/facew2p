#
# table for controller: typography
#

from gluon.contrib.populate import populate

db.define_table('dtypography', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtypography.id ).count():
    db.dtypography.insert( f0= 'sx940', f1= '(940)Toggle navigation')
    db.dtypography.insert( f0= 'sx943', f1= '(943)5')
    db.dtypography.insert( f0= 'sx944', f1= '(944)4')
    db.dtypography.insert( f0= 'aa947', f1= '(947)Dashboard')
    db.dtypography.insert( f0= 'aa949', f1= '(949)Tables')
    db.dtypography.insert( f0= 'aa951', f1= '(951)General')
    db.dtypography.insert( f0= 'aa953', f1= '(953)Validation')
    db.dtypography.insert( f0= 'aa955', f1= '(955)WYSIWYG')
    db.dtypography.insert( f0= 'aa957', f1= '(957)Wizard &amp; File Upload')
    db.dtypography.insert( f0= 'pb958', f1= '(958)Live Search ...')
    db.dtypography.insert( f0= 'sx960', f1= '(960)16')
    db.dtypography.insert( f0= 'he961', f1= '(961)Archie')
    db.dtypography.insert( f0= 'aa962', f1= '(962)Administrator')
    db.dtypography.insert( f0= 'ba963', f1= '(963)Last Access :')
    db.dtypography.insert( f0= 'lb964', f1= '(964)Menu')
    db.dtypography.insert( f0= 'sx966', f1= '(966)&nbsp;Dashboard')
    db.dtypography.insert( f0= 'sx967', f1= '(967)Layouts')
    db.dtypography.insert( f0= 'sx986', f1= '(986)Components')
    db.dtypography.insert( f0= 'sx998', f1= '(998)Tables')
    db.dtypography.insert( f0= 'aa1013', f1= '(1013)Level 2')
    db.dtypography.insert( f0= 'aa1014', f1= '(1014)Level 2')
    db.dtypography.insert( f0= 'aa1015', f1= '(1015)Level 3')
    db.dtypography.insert( f0= 'aa1016', f1= '(1016)Level 3')
    db.dtypography.insert( f0= 'aa1017', f1= '(1017)Level 4')
    db.dtypography.insert( f0= 'aa1018', f1= '(1018)Level 4')
    db.dtypography.insert( f0= 'aa1019', f1= '(1019)Level 5')
    db.dtypography.insert( f0= 'aa1020', f1= '(1020)Level 5')
    db.dtypography.insert( f0= 'aa1021', f1= '(1021)Level 5')
    db.dtypography.insert( f0= 'aa1022', f1= '(1022)Level 4')
    db.dtypography.insert( f0= 'aa1023', f1= '(1023)Level 2')
    db.dtypography.insert( f0= 'aa1024', f1= '(1024)Level 1')
    db.dtypography.insert( f0= 'aa1025', f1= '(1025)Level 2')
    db.dtypography.insert( f0= 'aa1026', f1= '(1026)Level 2')
    db.dtypography.insert( f0= 'aa1027', f1= '(1027)Level 2')
    db.dtypography.insert( f0= 'hh1028', f1= '(1028)Heading')
    db.dtypography.insert( f0= 'ha1029', f1= '(1029)Heading 1')
    db.dtypography.insert( f0= 'hb1030', f1= '(1030)Heading 2')
    db.dtypography.insert( f0= 'hc1031', f1= '(1031)Heading 3')
    db.dtypography.insert( f0= 'hd1032', f1= '(1032)Heading 4')
    db.dtypography.insert( f0= 'he1033', f1= '(1033)Heading 5')
    db.dtypography.insert( f0= 'hf1034', f1= '(1034)Heading 6')
    db.dtypography.insert( f0= 'hh1035', f1= '(1035)Paragraph')
    db.dtypography.insert( f0= 'pa1036', f1= '(1036)Default paragraph')
    db.dtypography.insert( f0= 'pc1037', f1= '(1037)lead paragraph')
    db.dtypography.insert( f0= 'pc1038', f1= '(1038)Muted paragraph')
    db.dtypography.insert( f0= 'pc1039', f1= '(1039)warning paragraph')
    db.dtypography.insert( f0= 'pc1040', f1= '(1040)primary paragraph')
    db.dtypography.insert( f0= 'pc1041', f1= '(1041)info paragraph')
    db.dtypography.insert( f0= 'pc1042', f1= '(1042)success paragraph')
    db.dtypography.insert( f0= 'pc1043', f1= '(1043)danger paragraph')
    db.dtypography.insert( f0= 'hh1044', f1= '(1044)Blockquotes')
    db.dtypography.insert( f0= 'si1045', f1= '(1045)Sed fringilla pellentesque consequat.')
    db.dtypography.insert( f0= 'hh1046', f1= '(1046)List')
    db.dtypography.insert( f0= 'hh1047', f1= '(1047)Unordered')
    db.dtypography.insert( f0= 'la1048', f1= '(1048)Lorem ipsum dolor sit amet')
    db.dtypography.insert( f0= 'lb1049', f1= '(1049)Consectetur adipiscing elit')
    db.dtypography.insert( f0= 'lb1050', f1= '(1050)Integer molestie lorem at massa')
    db.dtypography.insert( f0= 'lb1051', f1= '(1051)Facilisis in pretium nisl aliquet')
    db.dtypography.insert( f0= 'la1052', f1= '(1052)Phasellus iaculis neque')
    db.dtypography.insert( f0= 'lb1053', f1= '(1053)Purus sodales ultricies')
    db.dtypography.insert( f0= 'la1054', f1= '(1054)Vestibulum laoreet porttitor sem')
    db.dtypography.insert( f0= 'la1055', f1= '(1055)Ac tristique libero volutpat at')
    db.dtypography.insert( f0= 'la1056', f1= '(1056)Faucibus porta lacus fringilla vel')
    db.dtypography.insert( f0= 'la1057', f1= '(1057)Aenean sit amet erat nunc')
    db.dtypography.insert( f0= 'la1058', f1= '(1058)Eget porttitor lorem')
    db.dtypography.insert( f0= 'hh1059', f1= '(1059)Ordered')
    db.dtypography.insert( f0= 'la1060', f1= '(1060)Lorem ipsum dolor sit amet')
    db.dtypography.insert( f0= 'la1061', f1= '(1061)Consectetur adipiscing elit')
    db.dtypography.insert( f0= 'la1062', f1= '(1062)Integer molestie lorem at massa')
    db.dtypography.insert( f0= 'la1063', f1= '(1063)Facilisis in pretium nisl aliquet')
    db.dtypography.insert( f0= 'la1064', f1= '(1064)Phasellus iaculis neque')
    db.dtypography.insert( f0= 'la1065', f1= '(1065)Purus sodales ultricies')
    db.dtypography.insert( f0= 'la1066', f1= '(1066)Vestibulum laoreet porttitor sem')
    db.dtypography.insert( f0= 'la1067', f1= '(1067)Ac tristique libero volutpat at')
    db.dtypography.insert( f0= 'la1068', f1= '(1068)Faucibus porta lacus fringilla vel')
    db.dtypography.insert( f0= 'la1069', f1= '(1069)Aenean sit amet erat nunc')
    db.dtypography.insert( f0= 'la1070', f1= '(1070)Eget porttitor lorem')
    db.dtypography.insert( f0= 'si1071', f1= '(1071)10px padding')
    db.dtypography.insert( f0= 'si1072', f1= '(1072)No padding')
    db.dtypography.insert( f0= 'hh1073', f1= '(1073)Label')
    db.dtypography.insert( f0= 'sx1074', f1= '(1074)label')
    db.dtypography.insert( f0= 'sx1075', f1= '(1075)Default')
    db.dtypography.insert( f0= 'sx1076', f1= '(1076)Success')
    db.dtypography.insert( f0= 'sx1077', f1= '(1077)Warning')
    db.dtypography.insert( f0= 'sx1078', f1= '(1078)Danger')
    db.dtypography.insert( f0= 'sx1079', f1= '(1079)Info')
    db.dtypography.insert( f0= 'hh1080', f1= '(1080)Badge')
    db.dtypography.insert( f0= 'sx1081', f1= '(1081)badge')
    db.dtypography.insert( f0= 'sx1082', f1= '(1082)1')
    db.dtypography.insert( f0= 'bu1083', f1= '(1083)&times;')
    db.dtypography.insert( f0= 'sp1084', f1= '(1084)Warning!')
    db.dtypography.insert( f0= 'sx1085', f1= '(1085)1,4,4,7,5,9,10')
    db.dtypography.insert( f0= 'sx1086', f1= '(1086)Loading..')
    db.dtypography.insert( f0= 'sx1087', f1= '(1087)Loading..')
    db.dtypography.insert( f0= 'sx1088', f1= '(1088)1,3,4,5,3,5')
    db.dtypography.insert( f0= 'bu1089', f1= '(1089)Default')
    db.dtypography.insert( f0= 'bu1090', f1= '(1090)Primary')
    db.dtypography.insert( f0= 'bu1091', f1= '(1091)Info')
    db.dtypography.insert( f0= 'bu1092', f1= '(1092)Success')
    db.dtypography.insert( f0= 'bu1093', f1= '(1093)Danger')
    db.dtypography.insert( f0= 'bu1094', f1= '(1094)Warning')
    db.dtypography.insert( f0= 'bu1095', f1= '(1095)Inverse')
    db.dtypography.insert( f0= 'bu1096', f1= '(1096)btn-metis-1')
    db.dtypography.insert( f0= 'bu1097', f1= '(1097)btn-metis-2')
    db.dtypography.insert( f0= 'bu1098', f1= '(1098)btn-metis-3')
    db.dtypography.insert( f0= 'bu1099', f1= '(1099)btn-metis-4')
    db.dtypography.insert( f0= 'bu1100', f1= '(1100)btn-metis-5')
    db.dtypography.insert( f0= 'bu1101', f1= '(1101)btn-metis-6')
    db.dtypography.insert( f0= 'si1102', f1= '(1102)20%')
    db.dtypography.insert( f0= 'sp1103', f1= '(1103)Default')
    db.dtypography.insert( f0= 'si1104', f1= '(1104)40%')
    db.dtypography.insert( f0= 'sp1105', f1= '(1105)Success')
    db.dtypography.insert( f0= 'si1106', f1= '(1106)60%')
    db.dtypography.insert( f0= 'sp1107', f1= '(1107)warning')
    db.dtypography.insert( f0= 'si1108', f1= '(1108)80%')
    db.dtypography.insert( f0= 'sp1109', f1= '(1109)Danger')
    db.dtypography.insert( f0= 'pa1110', f1= '(1110)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dtypography.insert( f0= 'bu1111', f1= '(1111)&times;')
    db.dtypography.insert( f0= 'hd1112', f1= '(1112)Modal title')
    db.dtypography.insert( f0= 'bu1113', f1= '(1113)Close')
    db.commit()
#
