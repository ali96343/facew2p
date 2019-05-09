#
# table for controller: fixed_menu
#

from gluon.contrib.populate import populate

db.define_table('dfixed0menu', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dfixed0menu.id ).count():
    db.dfixed0menu.insert( f0= 'sx1690', f1= '(1690)Toggle navigation')
    db.dfixed0menu.insert( f0= 'sx1693', f1= '(1693)5')
    db.dfixed0menu.insert( f0= 'sx1694', f1= '(1694)4')
    db.dfixed0menu.insert( f0= 'aa1697', f1= '(1697)Dashboard')
    db.dfixed0menu.insert( f0= 'aa1699', f1= '(1699)Tables')
    db.dfixed0menu.insert( f0= 'aa1701', f1= '(1701)General')
    db.dfixed0menu.insert( f0= 'aa1703', f1= '(1703)Validation')
    db.dfixed0menu.insert( f0= 'aa1705', f1= '(1705)WYSIWYG')
    db.dfixed0menu.insert( f0= 'aa1707', f1= '(1707)Wizard &amp; File Upload')
    db.dfixed0menu.insert( f0= 'pb1708', f1= '(1708)Live Search ...')
    db.dfixed0menu.insert( f0= 'sx1710', f1= '(1710)16')
    db.dfixed0menu.insert( f0= 'he1711', f1= '(1711)Archie')
    db.dfixed0menu.insert( f0= 'aa1712', f1= '(1712)Administrator')
    db.dfixed0menu.insert( f0= 'ba1713', f1= '(1713)Last Access :')
    db.dfixed0menu.insert( f0= 'lb1714', f1= '(1714)Menu')
    db.dfixed0menu.insert( f0= 'sx1716', f1= '(1716)&nbsp;Dashboard')
    db.dfixed0menu.insert( f0= 'sx1717', f1= '(1717)Layouts')
    db.dfixed0menu.insert( f0= 'sx1736', f1= '(1736)Components')
    db.dfixed0menu.insert( f0= 'sx1748', f1= '(1748)Tables')
    db.dfixed0menu.insert( f0= 'aa1763', f1= '(1763)Level 2')
    db.dfixed0menu.insert( f0= 'aa1764', f1= '(1764)Level 2')
    db.dfixed0menu.insert( f0= 'aa1765', f1= '(1765)Level 3')
    db.dfixed0menu.insert( f0= 'aa1766', f1= '(1766)Level 3')
    db.dfixed0menu.insert( f0= 'aa1767', f1= '(1767)Level 4')
    db.dfixed0menu.insert( f0= 'aa1768', f1= '(1768)Level 4')
    db.dfixed0menu.insert( f0= 'aa1769', f1= '(1769)Level 5')
    db.dfixed0menu.insert( f0= 'aa1770', f1= '(1770)Level 5')
    db.dfixed0menu.insert( f0= 'aa1771', f1= '(1771)Level 5')
    db.dfixed0menu.insert( f0= 'aa1772', f1= '(1772)Level 4')
    db.dfixed0menu.insert( f0= 'aa1773', f1= '(1773)Level 2')
    db.dfixed0menu.insert( f0= 'aa1774', f1= '(1774)Level 1')
    db.dfixed0menu.insert( f0= 'aa1775', f1= '(1775)Level 2')
    db.dfixed0menu.insert( f0= 'aa1776', f1= '(1776)Level 2')
    db.dfixed0menu.insert( f0= 'aa1777', f1= '(1777)Level 2')
    db.dfixed0menu.insert( f0= 'hh1778', f1= '(1778)Code')
    db.dfixed0menu.insert( f0= 'bu1779', f1= '(1779)&times;')
    db.dfixed0menu.insert( f0= 'sp1780', f1= '(1780)Warning!')
    db.dfixed0menu.insert( f0= 'sx1781', f1= '(1781)1,4,4,7,5,9,10')
    db.dfixed0menu.insert( f0= 'sx1782', f1= '(1782)Loading..')
    db.dfixed0menu.insert( f0= 'sx1783', f1= '(1783)Loading..')
    db.dfixed0menu.insert( f0= 'sx1784', f1= '(1784)1,3,4,5,3,5')
    db.dfixed0menu.insert( f0= 'bu1785', f1= '(1785)Default')
    db.dfixed0menu.insert( f0= 'bu1786', f1= '(1786)Primary')
    db.dfixed0menu.insert( f0= 'bu1787', f1= '(1787)Info')
    db.dfixed0menu.insert( f0= 'bu1788', f1= '(1788)Success')
    db.dfixed0menu.insert( f0= 'bu1789', f1= '(1789)Danger')
    db.dfixed0menu.insert( f0= 'bu1790', f1= '(1790)Warning')
    db.dfixed0menu.insert( f0= 'bu1791', f1= '(1791)Inverse')
    db.dfixed0menu.insert( f0= 'bu1792', f1= '(1792)btn-metis-1')
    db.dfixed0menu.insert( f0= 'bu1793', f1= '(1793)btn-metis-2')
    db.dfixed0menu.insert( f0= 'bu1794', f1= '(1794)btn-metis-3')
    db.dfixed0menu.insert( f0= 'bu1795', f1= '(1795)btn-metis-4')
    db.dfixed0menu.insert( f0= 'bu1796', f1= '(1796)btn-metis-5')
    db.dfixed0menu.insert( f0= 'bu1797', f1= '(1797)btn-metis-6')
    db.dfixed0menu.insert( f0= 'si1798', f1= '(1798)20%')
    db.dfixed0menu.insert( f0= 'sp1799', f1= '(1799)Default')
    db.dfixed0menu.insert( f0= 'si1800', f1= '(1800)40%')
    db.dfixed0menu.insert( f0= 'sp1801', f1= '(1801)Success')
    db.dfixed0menu.insert( f0= 'si1802', f1= '(1802)60%')
    db.dfixed0menu.insert( f0= 'sp1803', f1= '(1803)warning')
    db.dfixed0menu.insert( f0= 'si1804', f1= '(1804)80%')
    db.dfixed0menu.insert( f0= 'sp1805', f1= '(1805)Danger')
    db.dfixed0menu.insert( f0= 'pa1806', f1= '(1806)2017 &copy; Metis Bootstrap Admin Template v2.4.2')
    db.dfixed0menu.insert( f0= 'bu1807', f1= '(1807)&times;')
    db.dfixed0menu.insert( f0= 'hd1808', f1= '(1808)Modal title')
    db.dfixed0menu.insert( f0= 'bu1809', f1= '(1809)Close')
    db.commit()
#
