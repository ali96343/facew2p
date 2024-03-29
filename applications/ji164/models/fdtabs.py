#
# table for controller: tabs
#

from gluon.contrib.populate import populate

db.define_table('dtabs', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtabs.id ).count():
    db.dtabs.insert( f0= 'sp1689', f1= '(1689)outdated')
    db.dtabs.insert( f0= 'pc1690', f1= '(1690)to improve your experience.')
    db.dtabs.insert( f0= 'aa1691', f1= '(1691)upgrade your browser')
    db.dtabs.insert( f0= 'sx1696', f1= '(1696)Ecommerce')
    db.dtabs.insert( f0= 'sx1698', f1= '(1698)Dashboard v.1')
    db.dtabs.insert( f0= 'sx1700', f1= '(1700)Dashboard v.2')
    db.dtabs.insert( f0= 'sx1702', f1= '(1702)Dashboard v.3')
    db.dtabs.insert( f0= 'sx1704', f1= '(1704)Product List')
    db.dtabs.insert( f0= 'sx1706', f1= '(1706)Product Edit')
    db.dtabs.insert( f0= 'sx1708', f1= '(1708)Product Detail')
    db.dtabs.insert( f0= 'sx1710', f1= '(1710)Product Cart')
    db.dtabs.insert( f0= 'sx1712', f1= '(1712)Product Payment')
    db.dtabs.insert( f0= 'sx1714', f1= '(1714)Analytics')
    db.dtabs.insert( f0= 'sx1716', f1= '(1716)Widgets')
    db.dtabs.insert( f0= 'sx1718', f1= '(1718)Mailbox')
    db.dtabs.insert( f0= 'sx1720', f1= '(1720)Inbox')
    db.dtabs.insert( f0= 'sx1722', f1= '(1722)View Mail')
    db.dtabs.insert( f0= 'sx1724', f1= '(1724)Compose Mail')
    db.dtabs.insert( f0= 'sx1726', f1= '(1726)Interface')
    db.dtabs.insert( f0= 'sx1728', f1= '(1728)Google Map')
    db.dtabs.insert( f0= 'sx1730', f1= '(1730)Data Maps')
    db.dtabs.insert( f0= 'sx1732', f1= '(1732)Pdf Viewer')
    db.dtabs.insert( f0= 'sx1734', f1= '(1734)X-Editable')
    db.dtabs.insert( f0= 'sx1736', f1= '(1736)Code Editor')
    db.dtabs.insert( f0= 'sx1738', f1= '(1738)Tree View')
    db.dtabs.insert( f0= 'sx1740', f1= '(1740)Preloader')
    db.dtabs.insert( f0= 'sx1742', f1= '(1742)Images Cropper')
    db.dtabs.insert( f0= 'sx1744', f1= '(1744)Miscellaneous')
    db.dtabs.insert( f0= 'sx1746', f1= '(1746)File Manager')
    db.dtabs.insert( f0= 'sx1748', f1= '(1748)Blog')
    db.dtabs.insert( f0= 'sx1750', f1= '(1750)Blog Details')
    db.dtabs.insert( f0= 'sx1752', f1= '(1752)404 Page')
    db.dtabs.insert( f0= 'sx1754', f1= '(1754)500 Page')
    db.dtabs.insert( f0= 'sx1756', f1= '(1756)Charts')
    db.dtabs.insert( f0= 'sx1758', f1= '(1758)Bar Charts')
    db.dtabs.insert( f0= 'sx1760', f1= '(1760)Line Charts')
    db.dtabs.insert( f0= 'sx1762', f1= '(1762)Area Charts')
    db.dtabs.insert( f0= 'sx1764', f1= '(1764)Rounded Charts')
    db.dtabs.insert( f0= 'sx1766', f1= '(1766)C3 Charts')
    db.dtabs.insert( f0= 'sx1768', f1= '(1768)Sparkline Charts')
    db.dtabs.insert( f0= 'sx1770', f1= '(1770)Peity Charts')
    db.dtabs.insert( f0= 'sx1772', f1= '(1772)Data Tables')
    db.dtabs.insert( f0= 'sx1774', f1= '(1774)Static Table')
    db.dtabs.insert( f0= 'sx1776', f1= '(1776)Data Table')
    db.dtabs.insert( f0= 'sx1778', f1= '(1778)Forms Elements')
    db.dtabs.insert( f0= 'sx1780', f1= '(1780)Bc Form Elements')
    db.dtabs.insert( f0= 'sx1782', f1= '(1782)Ad Form Elements')
    db.dtabs.insert( f0= 'sx1784', f1= '(1784)Password Meter')
    db.dtabs.insert( f0= 'sx1786', f1= '(1786)Multi Upload')
    db.dtabs.insert( f0= 'sx1788', f1= '(1788)Text Editor')
    db.dtabs.insert( f0= 'sx1790', f1= '(1790)Dual List Box')
    db.dtabs.insert( f0= 'sx1792', f1= '(1792)App views')
    db.dtabs.insert( f0= 'sx1794', f1= '(1794)Notifications')
    db.dtabs.insert( f0= 'sx1796', f1= '(1796)Alerts')
    db.dtabs.insert( f0= 'sx1798', f1= '(1798)Modals')
    db.dtabs.insert( f0= 'sx1800', f1= '(1800)Buttons')
    db.dtabs.insert( f0= 'sx1802', f1= '(1802)Tabs')
    db.dtabs.insert( f0= 'sx1804', f1= '(1804)Accordion')
    db.dtabs.insert( f0= 'sx1805', f1= '(1805)Pages')
    db.dtabs.insert( f0= 'sx1807', f1= '(1807)Login')
    db.dtabs.insert( f0= 'sx1809', f1= '(1809)Register')
    db.dtabs.insert( f0= 'sx1811', f1= '(1811)Lock')
    db.dtabs.insert( f0= 'sx1813', f1= '(1813)Password Recovery')
    db.dtabs.insert( f0= 'sx1814', f1= '(1814)Landing Page')
    db.dtabs.insert( f0= 'aa1817', f1= '(1817)Home')
    db.dtabs.insert( f0= 'aa1818', f1= '(1818)About')
    db.dtabs.insert( f0= 'aa1819', f1= '(1819)Services')
    db.dtabs.insert( f0= 'aa1820', f1= '(1820)Support')
    db.dtabs.insert( f0= 'hh1821', f1= '(1821)Message')
    db.dtabs.insert( f0= 'sx1823', f1= '(1823)16 Sept')
    db.dtabs.insert( f0= 'hh1824', f1= '(1824)Advanda Cro')
    db.dtabs.insert( f0= 'pa1825', f1= '(1825)Please done this project as soon possible.')
    db.dtabs.insert( f0= 'sx1827', f1= '(1827)16 Sept')
    db.dtabs.insert( f0= 'hh1828', f1= '(1828)Sulaiman din')
    db.dtabs.insert( f0= 'pa1829', f1= '(1829)Please done this project as soon possible.')
    db.dtabs.insert( f0= 'sx1831', f1= '(1831)16 Sept')
    db.dtabs.insert( f0= 'hh1832', f1= '(1832)Victor Jara')
    db.dtabs.insert( f0= 'pa1833', f1= '(1833)Please done this project as soon possible.')
    db.dtabs.insert( f0= 'sx1835', f1= '(1835)16 Sept')
    db.dtabs.insert( f0= 'hh1836', f1= '(1836)Victor Jara')
    db.dtabs.insert( f0= 'pa1837', f1= '(1837)Please done this project as soon possible.')
    db.dtabs.insert( f0= 'aa1838', f1= '(1838)View All Messages')
    db.dtabs.insert( f0= 'hh1839', f1= '(1839)Notifications')
    db.dtabs.insert( f0= 'sx1840', f1= '(1840)16 Sept')
    db.dtabs.insert( f0= 'hh1841', f1= '(1841)Advanda Cro')
    db.dtabs.insert( f0= 'pa1842', f1= '(1842)Please done this project as soon possible.')
    db.dtabs.insert( f0= 'sx1843', f1= '(1843)16 Sept')
    db.dtabs.insert( f0= 'hh1844', f1= '(1844)Sulaiman din')
    db.dtabs.insert( f0= 'pa1845', f1= '(1845)Please done this project as soon possible.')
    db.dtabs.insert( f0= 'sx1846', f1= '(1846)16 Sept')
    db.dtabs.insert( f0= 'hh1847', f1= '(1847)Victor Jara')
    db.dtabs.insert( f0= 'pa1848', f1= '(1848)Please done this project as soon possible.')
    db.dtabs.insert( f0= 'sx1849', f1= '(1849)16 Sept')
    db.dtabs.insert( f0= 'hh1850', f1= '(1850)Victor Jara')
    db.dtabs.insert( f0= 'pa1851', f1= '(1851)Please done this project as soon possible.')
    db.dtabs.insert( f0= 'aa1852', f1= '(1852)View All Notification')
    db.dtabs.insert( f0= 'sx1853', f1= '(1853)Advanda Cro')
    db.dtabs.insert( f0= 'aa1857', f1= '(1857)News')
    db.dtabs.insert( f0= 'aa1858', f1= '(1858)Activity')
    db.dtabs.insert( f0= 'aa1859', f1= '(1859)Settings')
    db.dtabs.insert( f0= 'pa1860', f1= '(1860)You have 10 New News.')
    db.dtabs.insert( f0= 'pa1862', f1= '(1862)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtabs.insert( f0= 'sp1863', f1= '(1863)Yesterday 2:45 pm')
    db.dtabs.insert( f0= 'pa1865', f1= '(1865)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtabs.insert( f0= 'sp1866', f1= '(1866)Yesterday 2:45 pm')
    db.dtabs.insert( f0= 'pa1868', f1= '(1868)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtabs.insert( f0= 'sp1869', f1= '(1869)Yesterday 2:45 pm')
    db.dtabs.insert( f0= 'pa1871', f1= '(1871)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtabs.insert( f0= 'sp1872', f1= '(1872)Yesterday 2:45 pm')
    db.dtabs.insert( f0= 'pa1874', f1= '(1874)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtabs.insert( f0= 'sp1875', f1= '(1875)Yesterday 2:45 pm')
    db.dtabs.insert( f0= 'pa1877', f1= '(1877)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtabs.insert( f0= 'sp1878', f1= '(1878)Yesterday 2:45 pm')
    db.dtabs.insert( f0= 'pa1880', f1= '(1880)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtabs.insert( f0= 'sp1881', f1= '(1881)Yesterday 2:45 pm')
    db.dtabs.insert( f0= 'pa1883', f1= '(1883)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtabs.insert( f0= 'sp1884', f1= '(1884)Yesterday 2:45 pm')
    db.dtabs.insert( f0= 'pa1886', f1= '(1886)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtabs.insert( f0= 'sp1887', f1= '(1887)Yesterday 2:45 pm')
    db.dtabs.insert( f0= 'pa1889', f1= '(1889)The point of using Lorem Ipsum is that it has a more-or-less normal.')
    db.dtabs.insert( f0= 'sp1890', f1= '(1890)Yesterday 2:45 pm')
    db.dtabs.insert( f0= 'pa1891', f1= '(1891)You have 20 Recent Activity.')
    db.dtabs.insert( f0= 'hh1892', f1= '(1892)New User Registered')
    db.dtabs.insert( f0= 'pa1893', f1= '(1893)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtabs.insert( f0= 'sx1894', f1= '(1894)1 hours ago')
    db.dtabs.insert( f0= 'hh1895', f1= '(1895)New Order Received')
    db.dtabs.insert( f0= 'pa1896', f1= '(1896)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtabs.insert( f0= 'sx1897', f1= '(1897)2 hours ago')
    db.dtabs.insert( f0= 'hh1898', f1= '(1898)New Order Received')
    db.dtabs.insert( f0= 'pa1899', f1= '(1899)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtabs.insert( f0= 'sx1900', f1= '(1900)3 hours ago')
    db.dtabs.insert( f0= 'hh1901', f1= '(1901)New Order Received')
    db.dtabs.insert( f0= 'pa1902', f1= '(1902)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtabs.insert( f0= 'sx1903', f1= '(1903)4 hours ago')
    db.dtabs.insert( f0= 'hh1904', f1= '(1904)New User Registered')
    db.dtabs.insert( f0= 'pa1905', f1= '(1905)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtabs.insert( f0= 'sx1906', f1= '(1906)5 hours ago')
    db.dtabs.insert( f0= 'hh1907', f1= '(1907)New Order')
    db.dtabs.insert( f0= 'pa1908', f1= '(1908)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtabs.insert( f0= 'sx1909', f1= '(1909)6 hours ago')
    db.dtabs.insert( f0= 'hh1910', f1= '(1910)New User')
    db.dtabs.insert( f0= 'pa1911', f1= '(1911)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtabs.insert( f0= 'sx1912', f1= '(1912)7 hours ago')
    db.dtabs.insert( f0= 'hh1913', f1= '(1913)New Order')
    db.dtabs.insert( f0= 'pa1914', f1= '(1914)The point of using Lorem Ipsum is that it has a more or less normal.')
    db.dtabs.insert( f0= 'sx1915', f1= '(1915)9 hours ago')
    db.dtabs.insert( f0= 'pa1916', f1= '(1916)You have 20 Settings. 5 not completed.')
    db.dtabs.insert( f0= 'hh1917', f1= '(1917)Show notifications')
    db.dtabs.insert( f0= 'hh1918', f1= '(1918)Disable Chat')
    db.dtabs.insert( f0= 'hh1919', f1= '(1919)Enable history')
    db.dtabs.insert( f0= 'hh1920', f1= '(1920)Show charts')
    db.dtabs.insert( f0= 'hh1921', f1= '(1921)Update everyday')
    db.dtabs.insert( f0= 'hh1922', f1= '(1922)Global search')
    db.dtabs.insert( f0= 'hh1923', f1= '(1923)Offline users')
    db.dtabs.insert( f0= 'aa1925', f1= '(1925)Dashboard v.1')
    db.dtabs.insert( f0= 'aa1927', f1= '(1927)Dashboard v.2')
    db.dtabs.insert( f0= 'aa1929', f1= '(1929)Dashboard v.3')
    db.dtabs.insert( f0= 'aa1931', f1= '(1931)Product List')
    db.dtabs.insert( f0= 'aa1933', f1= '(1933)Product Edit')
    db.dtabs.insert( f0= 'aa1935', f1= '(1935)Product Detail')
    db.dtabs.insert( f0= 'aa1937', f1= '(1937)Product Cart')
    db.dtabs.insert( f0= 'aa1939', f1= '(1939)Product Payment')
    db.dtabs.insert( f0= 'aa1941', f1= '(1941)Analytics')
    db.dtabs.insert( f0= 'aa1943', f1= '(1943)Widgets')
    db.dtabs.insert( f0= 'aa1945', f1= '(1945)Inbox')
    db.dtabs.insert( f0= 'aa1947', f1= '(1947)View Mail')
    db.dtabs.insert( f0= 'aa1949', f1= '(1949)Compose Mail')
    db.dtabs.insert( f0= 'aa1951', f1= '(1951)File Manager')
    db.dtabs.insert( f0= 'aa1953', f1= '(1953)Contacts Client')
    db.dtabs.insert( f0= 'aa1955', f1= '(1955)Project')
    db.dtabs.insert( f0= 'aa1957', f1= '(1957)Project Details')
    db.dtabs.insert( f0= 'aa1959', f1= '(1959)Blog')
    db.dtabs.insert( f0= 'aa1961', f1= '(1961)Blog Details')
    db.dtabs.insert( f0= 'aa1963', f1= '(1963)404 Page')
    db.dtabs.insert( f0= 'aa1965', f1= '(1965)500 Page')
    db.dtabs.insert( f0= 'aa1967', f1= '(1967)Google Map')
    db.dtabs.insert( f0= 'aa1969', f1= '(1969)Data Maps')
    db.dtabs.insert( f0= 'aa1971', f1= '(1971)Pdf Viewer')
    db.dtabs.insert( f0= 'aa1973', f1= '(1973)X-Editable')
    db.dtabs.insert( f0= 'aa1975', f1= '(1975)Code Editor')
    db.dtabs.insert( f0= 'aa1977', f1= '(1977)Tree View')
    db.dtabs.insert( f0= 'aa1979', f1= '(1979)Preloader')
    db.dtabs.insert( f0= 'aa1981', f1= '(1981)Images Cropper')
    db.dtabs.insert( f0= 'aa1983', f1= '(1983)Bar Charts')
    db.dtabs.insert( f0= 'aa1985', f1= '(1985)Line Charts')
    db.dtabs.insert( f0= 'aa1987', f1= '(1987)Area Charts')
    db.dtabs.insert( f0= 'aa1989', f1= '(1989)Rounded Charts')
    db.dtabs.insert( f0= 'aa1991', f1= '(1991)C3 Charts')
    db.dtabs.insert( f0= 'aa1993', f1= '(1993)Sparkline Charts')
    db.dtabs.insert( f0= 'aa1995', f1= '(1995)Peity Charts')
    db.dtabs.insert( f0= 'aa1997', f1= '(1997)Static Table')
    db.dtabs.insert( f0= 'aa1999', f1= '(1999)Data Table')
    db.dtabs.insert( f0= 'aa2001', f1= '(2001)Basic Form Elements')
    db.dtabs.insert( f0= 'aa2003', f1= '(2003)Advanced Form Elements')
    db.dtabs.insert( f0= 'aa2005', f1= '(2005)Password Meter')
    db.dtabs.insert( f0= 'aa2007', f1= '(2007)Multi Upload')
    db.dtabs.insert( f0= 'aa2009', f1= '(2009)Text Editor')
    db.dtabs.insert( f0= 'aa2011', f1= '(2011)Dual List Box')
    db.dtabs.insert( f0= 'aa2013', f1= '(2013)Basic Form Elements')
    db.dtabs.insert( f0= 'aa2015', f1= '(2015)Advanced Form Elements')
    db.dtabs.insert( f0= 'aa2017', f1= '(2017)Password Meter')
    db.dtabs.insert( f0= 'aa2019', f1= '(2019)Multi Upload')
    db.dtabs.insert( f0= 'aa2021', f1= '(2021)Text Editor')
    db.dtabs.insert( f0= 'aa2023', f1= '(2023)Dual List Box')
    db.dtabs.insert( f0= 'aa2025', f1= '(2025)Login')
    db.dtabs.insert( f0= 'aa2027', f1= '(2027)Register')
    db.dtabs.insert( f0= 'aa2029', f1= '(2029)Lock')
    db.dtabs.insert( f0= 'aa2031', f1= '(2031)Password Recovery')
    db.dtabs.insert( f0= 'pb2032', f1= '(2032)Search...')
    db.dtabs.insert( f0= 'aa2033', f1= '(2033)Home')
    db.dtabs.insert( f0= 'sx2034', f1= '(2034)Tabs')
    db.dtabs.insert( f0= 'hh2035', f1= '(2035)Custom Animate Tab Bootstrap')
    db.dtabs.insert( f0= 'pa2036', f1= '(2036)Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s.')
    db.dtabs.insert( f0= 'pa2037', f1= '(2037)when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.')
    db.dtabs.insert( f0= 'pa2038', f1= '(2038)It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')
    db.dtabs.insert( f0= 'pa2039', f1= '(2039)Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s.')
    db.dtabs.insert( f0= 'pa2040', f1= '(2040)when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.')
    db.dtabs.insert( f0= 'pa2041', f1= '(2041)Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s.')
    db.dtabs.insert( f0= 'pa2042', f1= '(2042)when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries.')
    db.dtabs.insert( f0= 'pa2043', f1= '(2043)the leap into electronic typesetting, remaining essentially unchanged.')
    db.dtabs.insert( f0= 'pa2044', f1= '(2044)Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s.')
    db.dtabs.insert( f0= 'pa2045', f1= '(2045)when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.')
    db.dtabs.insert( f0= 'pa2046', f1= '(2046)It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')
    db.dtabs.insert( f0= 'pa2047', f1= '(2047)Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s.')
    db.dtabs.insert( f0= 'pa2048', f1= '(2048)when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.')
    db.dtabs.insert( f0= 'pa2049', f1= '(2049)Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s.')
    db.dtabs.insert( f0= 'pa2050', f1= '(2050)when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries.')
    db.dtabs.insert( f0= 'pa2051', f1= '(2051)the leap into electronic typesetting, remaining essentially unchanged.')
    db.dtabs.insert( f0= 'pc2052', f1= '(2052)All rights reserved.')
    db.dtabs.insert( f0= 'pf2053', f1= '(2053)Copyright &copy; 2018')
    db.commit()
#
