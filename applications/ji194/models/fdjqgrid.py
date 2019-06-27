#
# table for controller: jqgrid
#

from gluon.contrib.populate import populate

db.define_table('djqgrid', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.djqgrid.id ).count():
    db.djqgrid.insert( f0= 'sx2089', f1= '(2089)Toggle sidebar')
    db.djqgrid.insert( f0= 'sx2091', f1= '(2091)Software Update')
    db.djqgrid.insert( f0= 'sx2092', f1= '(2092)65%')
    db.djqgrid.insert( f0= 'sx2093', f1= '(2093)Hardware Upgrade')
    db.djqgrid.insert( f0= 'sx2094', f1= '(2094)35%')
    db.djqgrid.insert( f0= 'sx2095', f1= '(2095)Unit Testing')
    db.djqgrid.insert( f0= 'sx2096', f1= '(2096)15%')
    db.djqgrid.insert( f0= 'sx2097', f1= '(2097)Bug Fixes')
    db.djqgrid.insert( f0= 'sx2098', f1= '(2098)90%')
    db.djqgrid.insert( f0= 'sx2099', f1= '(2099)+12')
    db.djqgrid.insert( f0= 'sx2100', f1= '(2100)+8')
    db.djqgrid.insert( f0= 'sx2101', f1= '(2101)+11')
    db.djqgrid.insert( f0= 'sx2103', f1= '(2103)Alex:')
    db.djqgrid.insert( f0= 'sp2104', f1= '(2104)a moment ago')
    db.djqgrid.insert( f0= 'sx2106', f1= '(2106)Susan:')
    db.djqgrid.insert( f0= 'sp2107', f1= '(2107)20 minutes ago')
    db.djqgrid.insert( f0= 'sx2109', f1= '(2109)Bob:')
    db.djqgrid.insert( f0= 'sp2110', f1= '(2110)3:15 pm')
    db.djqgrid.insert( f0= 'sx2112', f1= '(2112)Kate:')
    db.djqgrid.insert( f0= 'sp2113', f1= '(2113)1:33 pm')
    db.djqgrid.insert( f0= 'sx2115', f1= '(2115)Fred:')
    db.djqgrid.insert( f0= 'sp2116', f1= '(2116)10:09 am')
    db.djqgrid.insert( f0= 'ic2119', f1= '(2119)Welcome,')
    db.djqgrid.insert( f0= 'sx2122', f1= '(2122)Dashboard')
    db.djqgrid.insert( f0= 'sx2136', f1= '(2136)Tables')
    db.djqgrid.insert( f0= 'sx2139', f1= '(2139)Forms')
    db.djqgrid.insert( f0= 'sx2146', f1= '(2146)Widgets')
    db.djqgrid.insert( f0= 'sx2149', f1= '(2149)Gallery')
    db.djqgrid.insert( f0= 'sx2150', f1= '(2150)More Pages')
    db.djqgrid.insert( f0= 'aa2164', f1= '(2164)Home')
    db.djqgrid.insert( f0= 'aa2165', f1= '(2165)Tables')
    db.djqgrid.insert( f0= 'lb2166', f1= '(2166)jqGrid plugin')
    db.djqgrid.insert( f0= 'pb2167', f1= '(2167)Search ...')
    db.djqgrid.insert( f0= 'bb2168', f1= '(2168).container')
    db.djqgrid.insert( f0= 'sx2169', f1= '(2169)Ace')
    db.commit()
#
