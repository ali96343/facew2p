#
# table for controller: forms_advanced
#

from gluon.contrib.populate import populate

db.define_table('dforms0advanced', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dforms0advanced.id ).count():
    db.dforms0advanced.insert( f0= 'hc1766', f1= '(1766)UI elements')
    db.dforms0advanced.insert( f0= 'aa1768', f1= '(1768)Buttons')
    db.dforms0advanced.insert( f0= 'aa1770', f1= '(1770)Badges')
    db.dforms0advanced.insert( f0= 'aa1772', f1= '(1772)Tabs')
    db.dforms0advanced.insert( f0= 'aa1774', f1= '(1774)Social Buttons')
    db.dforms0advanced.insert( f0= 'aa1776', f1= '(1776)Cards')
    db.dforms0advanced.insert( f0= 'aa1778', f1= '(1778)Alerts')
    db.dforms0advanced.insert( f0= 'aa1780', f1= '(1780)Progress Bars')
    db.dforms0advanced.insert( f0= 'aa1782', f1= '(1782)Modals')
    db.dforms0advanced.insert( f0= 'aa1784', f1= '(1784)Switches')
    db.dforms0advanced.insert( f0= 'aa1786', f1= '(1786)Grids')
    db.dforms0advanced.insert( f0= 'aa1788', f1= '(1788)Typography')
    db.dforms0advanced.insert( f0= 'aa1790', f1= '(1790)Basic Table')
    db.dforms0advanced.insert( f0= 'aa1792', f1= '(1792)Data Table')
    db.dforms0advanced.insert( f0= 'aa1794', f1= '(1794)Basic Form')
    db.dforms0advanced.insert( f0= 'aa1796', f1= '(1796)Advanced Form')
    db.dforms0advanced.insert( f0= 'hc1797', f1= '(1797)Icons')
    db.dforms0advanced.insert( f0= 'aa1799', f1= '(1799)Font Awesome')
    db.dforms0advanced.insert( f0= 'aa1801', f1= '(1801)Themefy Icons')
    db.dforms0advanced.insert( f0= 'aa1804', f1= '(1804)Chart JS')
    db.dforms0advanced.insert( f0= 'aa1806', f1= '(1806)Flot Chart')
    db.dforms0advanced.insert( f0= 'aa1808', f1= '(1808)Peity Chart')
    db.dforms0advanced.insert( f0= 'aa1810', f1= '(1810)Google Maps')
    db.dforms0advanced.insert( f0= 'aa1812', f1= '(1812)Vector Maps')
    db.dforms0advanced.insert( f0= 'hc1813', f1= '(1813)Extras')
    db.dforms0advanced.insert( f0= 'aa1815', f1= '(1815)Login')
    db.dforms0advanced.insert( f0= 'aa1817', f1= '(1817)Register')
    db.dforms0advanced.insert( f0= 'aa1819', f1= '(1819)Forget Pass')
    db.dforms0advanced.insert( f0= 'pb1820', f1= '(1820)Search ...')
    db.dforms0advanced.insert( f0= 'pc1821', f1= '(1821)You have 3 Notification')
    db.dforms0advanced.insert( f0= 'pc1822', f1= '(1822)You have 4 Mails')
    db.dforms0advanced.insert( f0= 'sx1824', f1= '(1824)Jonathan Smith')
    db.dforms0advanced.insert( f0= 'sx1825', f1= '(1825)Just now')
    db.dforms0advanced.insert( f0= 'pa1826', f1= '(1826)Hello, this is an example msg')
    db.dforms0advanced.insert( f0= 'sx1828', f1= '(1828)Jack Sanders')
    db.dforms0advanced.insert( f0= 'sx1829', f1= '(1829)5 minutes ago')
    db.dforms0advanced.insert( f0= 'pa1830', f1= '(1830)Lorem ipsum dolor sit amet, consectetur')
    db.dforms0advanced.insert( f0= 'sx1832', f1= '(1832)Cheryl Wheeler')
    db.dforms0advanced.insert( f0= 'sx1833', f1= '(1833)10 minutes ago')
    db.dforms0advanced.insert( f0= 'pa1834', f1= '(1834)Hello, this is an example msg')
    db.dforms0advanced.insert( f0= 'sx1836', f1= '(1836)Rachel Santos')
    db.dforms0advanced.insert( f0= 'sx1837', f1= '(1837)15 minutes ago')
    db.dforms0advanced.insert( f0= 'pa1838', f1= '(1838)Lorem ipsum dolor sit amet, consectetur')
    db.dforms0advanced.insert( f0= 'sx1840', f1= '(1840)13')
    db.dforms0advanced.insert( f0= 'hh1841', f1= '(1841)Dashboard')
    db.dforms0advanced.insert( f0= 'aa1842', f1= '(1842)Dashboard')
    db.dforms0advanced.insert( f0= 'aa1843', f1= '(1843)Forms')
    db.dforms0advanced.insert( f0= 'lb1844', f1= '(1844)Advanced')
    db.dforms0advanced.insert( f0= 'sp1845', f1= '(1845)Masked Input')
    db.dforms0advanced.insert( f0= 'si1846', f1= '(1846)Small Text Mask')
    db.dforms0advanced.insert( f0= 'pb1852', f1= '(1852)Choose a Country...')
    db.dforms0advanced.insert( f0= 'pb1853', f1= '(1853)Choose a country...')
    db.dforms0advanced.insert( f0= 'pb1854', f1= '(1854)Your Favorite Football Team')
    db.commit()
#
