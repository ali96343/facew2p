#
# table for controller: twoIImenuII1
#

from gluon.contrib.populate import populate

db.define_table('dtwo0menu01', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtwo0menu01.id ).count():
    db.dtwo0menu01.insert( f0= 'sx13', f1= '(13)Toggle sidebar')
    db.dtwo0menu01.insert( f0= 'sx15', f1= '(15)Toggle user menu')
    db.dtwo0menu01.insert( f0= 'sx17', f1= '(17)Software Update')
    db.dtwo0menu01.insert( f0= 'sx18', f1= '(18)65%')
    db.dtwo0menu01.insert( f0= 'sx19', f1= '(19)Hardware Upgrade')
    db.dtwo0menu01.insert( f0= 'sx20', f1= '(20)35%')
    db.dtwo0menu01.insert( f0= 'sx21', f1= '(21)Unit Testing')
    db.dtwo0menu01.insert( f0= 'sx22', f1= '(22)15%')
    db.dtwo0menu01.insert( f0= 'sx23', f1= '(23)Bug Fixes')
    db.dtwo0menu01.insert( f0= 'sx24', f1= '(24)90%')
    db.dtwo0menu01.insert( f0= 'sx26', f1= '(26)Alex:')
    db.dtwo0menu01.insert( f0= 'sp27', f1= '(27)a moment ago')
    db.dtwo0menu01.insert( f0= 'sx29', f1= '(29)Susan:')
    db.dtwo0menu01.insert( f0= 'sp30', f1= '(30)20 minutes ago')
    db.dtwo0menu01.insert( f0= 'sx32', f1= '(32)Bob:')
    db.dtwo0menu01.insert( f0= 'sp33', f1= '(33)3:15 pm')
    db.dtwo0menu01.insert( f0= 'sx35', f1= '(35)Kate:')
    db.dtwo0menu01.insert( f0= 'sp36', f1= '(36)1:33 pm')
    db.dtwo0menu01.insert( f0= 'sx38', f1= '(38)Fred:')
    db.dtwo0menu01.insert( f0= 'sp39', f1= '(39)10:09 am')
    db.dtwo0menu01.insert( f0= 'ic42', f1= '(42)Welcome,')
    db.dtwo0menu01.insert( f0= 'sx45', f1= '(45)Dashboard')
    db.dtwo0menu01.insert( f0= 'sx59', f1= '(59)Tables')
    db.dtwo0menu01.insert( f0= 'sx62', f1= '(62)Forms')
    db.dtwo0menu01.insert( f0= 'sx69', f1= '(69)Widgets')
    db.dtwo0menu01.insert( f0= 'sx72', f1= '(72)Gallery')
    db.dtwo0menu01.insert( f0= 'sx73', f1= '(73)More Pages')
    db.dtwo0menu01.insert( f0= 'bb87', f1= '(87).container')
    db.dtwo0menu01.insert( f0= 'hh88', f1= '(88)Two menu')
    db.dtwo0menu01.insert( f0= 'sx89', f1= '(89)Toggle sidebar')
    db.dtwo0menu01.insert( f0= 'sx90', f1= '(90)Dashboard')
    db.dtwo0menu01.insert( f0= 'sx91', f1= '(91)Widgets')
    db.dtwo0menu01.insert( f0= 'sx92', f1= '(92)Gallery')
    db.dtwo0menu01.insert( f0= 'sx93', f1= '(93)More Pages')
    db.dtwo0menu01.insert( f0= 'sx94', f1= '(94)Ace')
    db.commit()
#
