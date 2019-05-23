#
# table for controller: charts_flot
#

from gluon.contrib.populate import populate

db.define_table('dcharts0flot', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcharts0flot.id ).count():
    db.dcharts0flot.insert( f0= 'hc1986', f1= '(1986)UI elements')
    db.dcharts0flot.insert( f0= 'aa1988', f1= '(1988)Buttons')
    db.dcharts0flot.insert( f0= 'aa1990', f1= '(1990)Badges')
    db.dcharts0flot.insert( f0= 'aa1992', f1= '(1992)Tabs')
    db.dcharts0flot.insert( f0= 'aa1994', f1= '(1994)Social Buttons')
    db.dcharts0flot.insert( f0= 'aa1996', f1= '(1996)Cards')
    db.dcharts0flot.insert( f0= 'aa1998', f1= '(1998)Alerts')
    db.dcharts0flot.insert( f0= 'aa2000', f1= '(2000)Progress Bars')
    db.dcharts0flot.insert( f0= 'aa2002', f1= '(2002)Modals')
    db.dcharts0flot.insert( f0= 'aa2004', f1= '(2004)Switches')
    db.dcharts0flot.insert( f0= 'aa2006', f1= '(2006)Grids')
    db.dcharts0flot.insert( f0= 'aa2008', f1= '(2008)Typography')
    db.dcharts0flot.insert( f0= 'aa2010', f1= '(2010)Basic Table')
    db.dcharts0flot.insert( f0= 'aa2012', f1= '(2012)Data Table')
    db.dcharts0flot.insert( f0= 'aa2014', f1= '(2014)Basic Form')
    db.dcharts0flot.insert( f0= 'aa2016', f1= '(2016)Advanced Form')
    db.dcharts0flot.insert( f0= 'hc2017', f1= '(2017)Icons')
    db.dcharts0flot.insert( f0= 'aa2019', f1= '(2019)Font Awesome')
    db.dcharts0flot.insert( f0= 'aa2021', f1= '(2021)Themefy Icons')
    db.dcharts0flot.insert( f0= 'aa2024', f1= '(2024)Chart JS')
    db.dcharts0flot.insert( f0= 'aa2026', f1= '(2026)Flot Chart')
    db.dcharts0flot.insert( f0= 'aa2028', f1= '(2028)Peity Chart')
    db.dcharts0flot.insert( f0= 'aa2030', f1= '(2030)Google Maps')
    db.dcharts0flot.insert( f0= 'aa2032', f1= '(2032)Vector Maps')
    db.dcharts0flot.insert( f0= 'hc2033', f1= '(2033)Extras')
    db.dcharts0flot.insert( f0= 'aa2035', f1= '(2035)Login')
    db.dcharts0flot.insert( f0= 'aa2037', f1= '(2037)Register')
    db.dcharts0flot.insert( f0= 'aa2039', f1= '(2039)Forget Pass')
    db.dcharts0flot.insert( f0= 'pb2040', f1= '(2040)Search ...')
    db.dcharts0flot.insert( f0= 'pc2041', f1= '(2041)You have 3 Notification')
    db.dcharts0flot.insert( f0= 'pc2042', f1= '(2042)You have 4 Mails')
    db.dcharts0flot.insert( f0= 'sx2044', f1= '(2044)Jonathan Smith')
    db.dcharts0flot.insert( f0= 'sx2045', f1= '(2045)Just now')
    db.dcharts0flot.insert( f0= 'pa2046', f1= '(2046)Hello, this is an example msg')
    db.dcharts0flot.insert( f0= 'sx2048', f1= '(2048)Jack Sanders')
    db.dcharts0flot.insert( f0= 'sx2049', f1= '(2049)5 minutes ago')
    db.dcharts0flot.insert( f0= 'pa2050', f1= '(2050)Lorem ipsum dolor sit amet, consectetur')
    db.dcharts0flot.insert( f0= 'sx2052', f1= '(2052)Cheryl Wheeler')
    db.dcharts0flot.insert( f0= 'sx2053', f1= '(2053)10 minutes ago')
    db.dcharts0flot.insert( f0= 'pa2054', f1= '(2054)Hello, this is an example msg')
    db.dcharts0flot.insert( f0= 'sx2056', f1= '(2056)Rachel Santos')
    db.dcharts0flot.insert( f0= 'sx2057', f1= '(2057)15 minutes ago')
    db.dcharts0flot.insert( f0= 'pa2058', f1= '(2058)Lorem ipsum dolor sit amet, consectetur')
    db.dcharts0flot.insert( f0= 'sx2060', f1= '(2060)13')
    db.dcharts0flot.insert( f0= 'hh2061', f1= '(2061)Dashboard')
    db.dcharts0flot.insert( f0= 'aa2062', f1= '(2062)Dashboard')
    db.dcharts0flot.insert( f0= 'aa2063', f1= '(2063)Charts')
    db.dcharts0flot.insert( f0= 'lb2064', f1= '(2064)Float Chart')
    db.dcharts0flot.insert( f0= 'hd2065', f1= '(2065)Real Chart')
    db.dcharts0flot.insert( f0= 'hd2066', f1= '(2066)Line Chart')
    db.dcharts0flot.insert( f0= 'hd2067', f1= '(2067)Pie Chart')
    db.dcharts0flot.insert( f0= 'hd2068', f1= '(2068)Line Chart')
    db.dcharts0flot.insert( f0= 'hd2069', f1= '(2069)Bar Chart')
    db.dcharts0flot.insert( f0= 'hd2070', f1= '(2070)Bar Chart')
    db.commit()
#
