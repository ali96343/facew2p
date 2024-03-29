#
# table for controller: formIIwizard
#

from gluon.contrib.populate import populate

db.define_table('dform0wizard', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dform0wizard.id ).count():
    db.dform0wizard.insert( f0= 'sx1765', f1= '(1765)Toggle sidebar')
    db.dform0wizard.insert( f0= 'sx1767', f1= '(1767)Software Update')
    db.dform0wizard.insert( f0= 'sx1768', f1= '(1768)65%')
    db.dform0wizard.insert( f0= 'sx1769', f1= '(1769)Hardware Upgrade')
    db.dform0wizard.insert( f0= 'sx1770', f1= '(1770)35%')
    db.dform0wizard.insert( f0= 'sx1771', f1= '(1771)Unit Testing')
    db.dform0wizard.insert( f0= 'sx1772', f1= '(1772)15%')
    db.dform0wizard.insert( f0= 'sx1773', f1= '(1773)Bug Fixes')
    db.dform0wizard.insert( f0= 'sx1774', f1= '(1774)90%')
    db.dform0wizard.insert( f0= 'sx1775', f1= '(1775)+12')
    db.dform0wizard.insert( f0= 'sx1776', f1= '(1776)+8')
    db.dform0wizard.insert( f0= 'sx1777', f1= '(1777)+11')
    db.dform0wizard.insert( f0= 'sx1779', f1= '(1779)Alex:')
    db.dform0wizard.insert( f0= 'sp1780', f1= '(1780)a moment ago')
    db.dform0wizard.insert( f0= 'sx1782', f1= '(1782)Susan:')
    db.dform0wizard.insert( f0= 'sp1783', f1= '(1783)20 minutes ago')
    db.dform0wizard.insert( f0= 'sx1785', f1= '(1785)Bob:')
    db.dform0wizard.insert( f0= 'sp1786', f1= '(1786)3:15 pm')
    db.dform0wizard.insert( f0= 'sx1788', f1= '(1788)Kate:')
    db.dform0wizard.insert( f0= 'sp1789', f1= '(1789)1:33 pm')
    db.dform0wizard.insert( f0= 'sx1791', f1= '(1791)Fred:')
    db.dform0wizard.insert( f0= 'sp1792', f1= '(1792)10:09 am')
    db.dform0wizard.insert( f0= 'ic1795', f1= '(1795)Welcome,')
    db.dform0wizard.insert( f0= 'sx1798', f1= '(1798)Dashboard')
    db.dform0wizard.insert( f0= 'sx1812', f1= '(1812)Tables')
    db.dform0wizard.insert( f0= 'sx1815', f1= '(1815)Forms')
    db.dform0wizard.insert( f0= 'sx1822', f1= '(1822)Widgets')
    db.dform0wizard.insert( f0= 'sx1825', f1= '(1825)Gallery')
    db.dform0wizard.insert( f0= 'sx1826', f1= '(1826)More Pages')
    db.dform0wizard.insert( f0= 'aa1840', f1= '(1840)Home')
    db.dform0wizard.insert( f0= 'aa1841', f1= '(1841)Forms')
    db.dform0wizard.insert( f0= 'pb1842', f1= '(1842)Search ...')
    db.dform0wizard.insert( f0= 'bb1843', f1= '(1843).container')
    db.dform0wizard.insert( f0= 'aa1844', f1= '(1844)Wizard Inside a Modal Box')
    db.dform0wizard.insert( f0= 'hd1845', f1= '(1845)New Item Wizard')
    db.dform0wizard.insert( f0= 'bb1846', f1= '(1846)Validation')
    db.dform0wizard.insert( f0= 'sx1847', f1= '(1847)Validation states')
    db.dform0wizard.insert( f0= 'sx1848', f1= '(1848)Alerts')
    db.dform0wizard.insert( f0= 'sx1849', f1= '(1849)Payment Info')
    db.dform0wizard.insert( f0= 'sx1850', f1= '(1850)Other Info')
    db.dform0wizard.insert( f0= 'hc1851', f1= '(1851)Enter the following information')
    db.dform0wizard.insert( f0= 'di1852', f1= '(1852)Warning tip help!')
    db.dform0wizard.insert( f0= 'di1853', f1= '(1853)Error tip help!')
    db.dform0wizard.insert( f0= 'di1854', f1= '(1854)Success tip help!')
    db.dform0wizard.insert( f0= 'di1855', f1= '(1855)Info tip help!')
    db.dform0wizard.insert( f0= 'di1856', f1= '(1856)Error tip help!')
    db.dform0wizard.insert( f0= 'sx1857', f1= '(1857)Latest news and announcements')
    db.dform0wizard.insert( f0= 'sx1858', f1= '(1858)Product offers and discounts')
    db.dform0wizard.insert( f0= 'sx1859', f1= '(1859)Male')
    db.dform0wizard.insert( f0= 'sx1860', f1= '(1860)Female')
    db.dform0wizard.insert( f0= 'pb1861', f1= '(1861)Click to Choose...')
    db.dform0wizard.insert( f0= 'sx1862', f1= '(1862)I accept the policy')
    db.dform0wizard.insert( f0= 'sp1863', f1= '(1863)Warning!')
    db.dform0wizard.insert( f0= 'sp1864', f1= '(1864)Heads up!')
    db.dform0wizard.insert( f0= 'hc1865', f1= '(1865)This is step 3')
    db.dform0wizard.insert( f0= 'hc1866', f1= '(1866)Congrats!')
    db.dform0wizard.insert( f0= 'sx1867', f1= '(1867)Validation states')
    db.dform0wizard.insert( f0= 'sx1868', f1= '(1868)Alerts')
    db.dform0wizard.insert( f0= 'sx1869', f1= '(1869)Payment Info')
    db.dform0wizard.insert( f0= 'sx1870', f1= '(1870)Other Info')
    db.dform0wizard.insert( f0= 'hd1871', f1= '(1871)Step 1')
    db.dform0wizard.insert( f0= 'hd1872', f1= '(1872)Step 2')
    db.dform0wizard.insert( f0= 'hd1873', f1= '(1873)Step 3')
    db.dform0wizard.insert( f0= 'hd1874', f1= '(1874)Step 4')
    db.dform0wizard.insert( f0= 'sx1875', f1= '(1875)Ace')
    db.commit()
#
