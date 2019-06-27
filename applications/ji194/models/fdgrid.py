#
# table for controller: grid
#

from gluon.contrib.populate import populate

db.define_table('dgrid', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dgrid.id ).count():
    db.dgrid.insert( f0= 'sx729', f1= '(729)Toggle sidebar')
    db.dgrid.insert( f0= 'sx731', f1= '(731)Software Update')
    db.dgrid.insert( f0= 'sx732', f1= '(732)65%')
    db.dgrid.insert( f0= 'sx733', f1= '(733)Hardware Upgrade')
    db.dgrid.insert( f0= 'sx734', f1= '(734)35%')
    db.dgrid.insert( f0= 'sx735', f1= '(735)Unit Testing')
    db.dgrid.insert( f0= 'sx736', f1= '(736)15%')
    db.dgrid.insert( f0= 'sx737', f1= '(737)Bug Fixes')
    db.dgrid.insert( f0= 'sx738', f1= '(738)90%')
    db.dgrid.insert( f0= 'sx739', f1= '(739)+12')
    db.dgrid.insert( f0= 'sx740', f1= '(740)+8')
    db.dgrid.insert( f0= 'sx741', f1= '(741)+11')
    db.dgrid.insert( f0= 'sx743', f1= '(743)Alex:')
    db.dgrid.insert( f0= 'sp744', f1= '(744)a moment ago')
    db.dgrid.insert( f0= 'sx746', f1= '(746)Susan:')
    db.dgrid.insert( f0= 'sp747', f1= '(747)20 minutes ago')
    db.dgrid.insert( f0= 'sx749', f1= '(749)Bob:')
    db.dgrid.insert( f0= 'sp750', f1= '(750)3:15 pm')
    db.dgrid.insert( f0= 'sx752', f1= '(752)Kate:')
    db.dgrid.insert( f0= 'sp753', f1= '(753)1:33 pm')
    db.dgrid.insert( f0= 'sx755', f1= '(755)Fred:')
    db.dgrid.insert( f0= 'sp756', f1= '(756)10:09 am')
    db.dgrid.insert( f0= 'ic759', f1= '(759)Welcome,')
    db.dgrid.insert( f0= 'sx762', f1= '(762)Dashboard')
    db.dgrid.insert( f0= 'sx776', f1= '(776)Tables')
    db.dgrid.insert( f0= 'sx779', f1= '(779)Forms')
    db.dgrid.insert( f0= 'sx786', f1= '(786)Widgets')
    db.dgrid.insert( f0= 'sx789', f1= '(789)Gallery')
    db.dgrid.insert( f0= 'sx790', f1= '(790)More Pages')
    db.dgrid.insert( f0= 'aa804', f1= '(804)Home')
    db.dgrid.insert( f0= 'aa805', f1= '(805)Other Pages')
    db.dgrid.insert( f0= 'lb806', f1= '(806)Grid')
    db.dgrid.insert( f0= 'pb807', f1= '(807)Search ...')
    db.dgrid.insert( f0= 'bb808', f1= '(808).container')
    db.dgrid.insert( f0= 'sp809', f1= '(809).col-xs-12')
    db.dgrid.insert( f0= 'sp810', f1= '(810).col-xs-1')
    db.dgrid.insert( f0= 'sp811', f1= '(811).col-xs-11')
    db.dgrid.insert( f0= 'sp812', f1= '(812).col-xs-6.col-sm-2')
    db.dgrid.insert( f0= 'sp813', f1= '(813).col-xs-6.col-sm-10')
    db.dgrid.insert( f0= 'sp814', f1= '(814).col-xs-4')
    db.dgrid.insert( f0= 'sp815', f1= '(815).col-xs-8')
    db.dgrid.insert( f0= 'sp816', f1= '(816).col-xs-5')
    db.dgrid.insert( f0= 'sp817', f1= '(817).col-xs-7')
    db.dgrid.insert( f0= 'sp818', f1= '(818).col-xs-7')
    db.dgrid.insert( f0= 'sp819', f1= '(819).col-xs-5')
    db.dgrid.insert( f0= 'sp820', f1= '(820).col-xs-8')
    db.dgrid.insert( f0= 'sp821', f1= '(821).col-xs-4')
    db.dgrid.insert( f0= 'sp822', f1= '(822).col-xs-9')
    db.dgrid.insert( f0= 'sp823', f1= '(823).col-xs-3')
    db.dgrid.insert( f0= 'sp824', f1= '(824).col-xs-10')
    db.dgrid.insert( f0= 'sp825', f1= '(825).col-xs-2')
    db.dgrid.insert( f0= 'sp826', f1= '(826).col-xs-11')
    db.dgrid.insert( f0= 'sp827', f1= '(827).col-xs-1')
    db.dgrid.insert( f0= 'sp828', f1= '(828).col-xs-12')
    db.dgrid.insert( f0= 'sx829', f1= '(829)Ace')
    db.commit()
#
