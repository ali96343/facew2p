#
# table for controller: charts_chartjs
#

from gluon.contrib.populate import populate

db.define_table('dcharts0chartjs', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcharts0chartjs.id ).count():
    db.dcharts0chartjs.insert( f0= 'hc1876', f1= '(1876)UI elements')
    db.dcharts0chartjs.insert( f0= 'aa1878', f1= '(1878)Buttons')
    db.dcharts0chartjs.insert( f0= 'aa1880', f1= '(1880)Badges')
    db.dcharts0chartjs.insert( f0= 'aa1882', f1= '(1882)Tabs')
    db.dcharts0chartjs.insert( f0= 'aa1884', f1= '(1884)Social Buttons')
    db.dcharts0chartjs.insert( f0= 'aa1886', f1= '(1886)Cards')
    db.dcharts0chartjs.insert( f0= 'aa1888', f1= '(1888)Alerts')
    db.dcharts0chartjs.insert( f0= 'aa1890', f1= '(1890)Progress Bars')
    db.dcharts0chartjs.insert( f0= 'aa1892', f1= '(1892)Modals')
    db.dcharts0chartjs.insert( f0= 'aa1894', f1= '(1894)Switches')
    db.dcharts0chartjs.insert( f0= 'aa1896', f1= '(1896)Grids')
    db.dcharts0chartjs.insert( f0= 'aa1898', f1= '(1898)Typography')
    db.dcharts0chartjs.insert( f0= 'aa1900', f1= '(1900)Basic Table')
    db.dcharts0chartjs.insert( f0= 'aa1902', f1= '(1902)Data Table')
    db.dcharts0chartjs.insert( f0= 'aa1904', f1= '(1904)Basic Form')
    db.dcharts0chartjs.insert( f0= 'aa1906', f1= '(1906)Advanced Form')
    db.dcharts0chartjs.insert( f0= 'hc1907', f1= '(1907)Icons')
    db.dcharts0chartjs.insert( f0= 'aa1909', f1= '(1909)Font Awesome')
    db.dcharts0chartjs.insert( f0= 'aa1911', f1= '(1911)Themefy Icons')
    db.dcharts0chartjs.insert( f0= 'aa1914', f1= '(1914)Chart JS')
    db.dcharts0chartjs.insert( f0= 'aa1916', f1= '(1916)Flot Chart')
    db.dcharts0chartjs.insert( f0= 'aa1918', f1= '(1918)Peity Chart')
    db.dcharts0chartjs.insert( f0= 'aa1920', f1= '(1920)Google Maps')
    db.dcharts0chartjs.insert( f0= 'aa1922', f1= '(1922)Vector Maps')
    db.dcharts0chartjs.insert( f0= 'hc1923', f1= '(1923)Extras')
    db.dcharts0chartjs.insert( f0= 'aa1925', f1= '(1925)Login')
    db.dcharts0chartjs.insert( f0= 'aa1927', f1= '(1927)Register')
    db.dcharts0chartjs.insert( f0= 'aa1929', f1= '(1929)Forget Pass')
    db.dcharts0chartjs.insert( f0= 'pb1930', f1= '(1930)Search ...')
    db.dcharts0chartjs.insert( f0= 'pc1931', f1= '(1931)You have 3 Notification')
    db.dcharts0chartjs.insert( f0= 'pc1932', f1= '(1932)You have 4 Mails')
    db.dcharts0chartjs.insert( f0= 'sx1934', f1= '(1934)Jonathan Smith')
    db.dcharts0chartjs.insert( f0= 'sx1935', f1= '(1935)Just now')
    db.dcharts0chartjs.insert( f0= 'pa1936', f1= '(1936)Hello, this is an example msg')
    db.dcharts0chartjs.insert( f0= 'sx1938', f1= '(1938)Jack Sanders')
    db.dcharts0chartjs.insert( f0= 'sx1939', f1= '(1939)5 minutes ago')
    db.dcharts0chartjs.insert( f0= 'pa1940', f1= '(1940)Lorem ipsum dolor sit amet, consectetur')
    db.dcharts0chartjs.insert( f0= 'sx1942', f1= '(1942)Cheryl Wheeler')
    db.dcharts0chartjs.insert( f0= 'sx1943', f1= '(1943)10 minutes ago')
    db.dcharts0chartjs.insert( f0= 'pa1944', f1= '(1944)Hello, this is an example msg')
    db.dcharts0chartjs.insert( f0= 'sx1946', f1= '(1946)Rachel Santos')
    db.dcharts0chartjs.insert( f0= 'sx1947', f1= '(1947)15 minutes ago')
    db.dcharts0chartjs.insert( f0= 'pa1948', f1= '(1948)Lorem ipsum dolor sit amet, consectetur')
    db.dcharts0chartjs.insert( f0= 'sx1950', f1= '(1950)13')
    db.dcharts0chartjs.insert( f0= 'hh1951', f1= '(1951)Dashboard')
    db.dcharts0chartjs.insert( f0= 'aa1952', f1= '(1952)Dashboard')
    db.dcharts0chartjs.insert( f0= 'aa1953', f1= '(1953)Charts')
    db.dcharts0chartjs.insert( f0= 'lb1954', f1= '(1954)Chartjs')
    db.dcharts0chartjs.insert( f0= 'hd1955', f1= '(1955)Yearly Sales')
    db.dcharts0chartjs.insert( f0= 'hd1956', f1= '(1956)Team Commits')
    db.dcharts0chartjs.insert( f0= 'hd1957', f1= '(1957)Bar chart')
    db.dcharts0chartjs.insert( f0= 'hd1958', f1= '(1958)Rader chart')
    db.dcharts0chartjs.insert( f0= 'hd1959', f1= '(1959)Line Chart')
    db.dcharts0chartjs.insert( f0= 'hd1960', f1= '(1960)Doughut Chart')
    db.dcharts0chartjs.insert( f0= 'hd1961', f1= '(1961)Pie Chart')
    db.dcharts0chartjs.insert( f0= 'hd1962', f1= '(1962)Polar Chart')
    db.dcharts0chartjs.insert( f0= 'hd1963', f1= '(1963)Single Bar Chart')
    db.commit()
#
