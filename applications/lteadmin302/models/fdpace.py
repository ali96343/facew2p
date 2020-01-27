#
# table for controller: pace
#

from gluon.contrib.populate import populate

db.define_table('dpace', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dpace.id ).count():
    db.dpace.insert( f0= 'aa2159', f1= '(2159)Home')
    db.dpace.insert( f0= 'aa2160', f1= '(2160)Contact')
    db.dpace.insert( f0= 'pb2161', f1= '(2161)Search')
    db.dpace.insert( f0= 'sx2162', f1= '(2162)3')
    db.dpace.insert( f0= 'pc2164', f1= '(2164)Call me whenever you can...')
    db.dpace.insert( f0= 'pc2165', f1= '(2165)4 Hours Ago')
    db.dpace.insert( f0= 'pc2167', f1= '(2167)I got your message bro')
    db.dpace.insert( f0= 'pc2168', f1= '(2168)4 Hours Ago')
    db.dpace.insert( f0= 'pc2170', f1= '(2170)The subject goes here')
    db.dpace.insert( f0= 'pc2171', f1= '(2171)4 Hours Ago')
    db.dpace.insert( f0= 'aa2172', f1= '(2172)See All Messages')
    db.dpace.insert( f0= 'sx2173', f1= '(2173)15 Notifications')
    db.dpace.insert( f0= 'sx2174', f1= '(2174)3 mins')
    db.dpace.insert( f0= 'sx2175', f1= '(2175)12 hours')
    db.dpace.insert( f0= 'sx2176', f1= '(2176)2 days')
    db.dpace.insert( f0= 'aa2177', f1= '(2177)See All Notifications')
    db.dpace.insert( f0= 'sx2180', f1= '(2180)AdminLTE 3')
    db.dpace.insert( f0= 'aa2182', f1= '(2182)Alexander Pierce')
    db.dpace.insert( f0= 'pa2184', f1= '(2184)Dashboard v1')
    db.dpace.insert( f0= 'pa2186', f1= '(2186)Dashboard v2')
    db.dpace.insert( f0= 'pa2188', f1= '(2188)Dashboard v3')
    db.dpace.insert( f0= 'sx2190', f1= '(2190)New')
    db.dpace.insert( f0= 'sx2191', f1= '(2191)6')
    db.dpace.insert( f0= 'pa2193', f1= '(2193)Top Navigation')
    db.dpace.insert( f0= 'pa2195', f1= '(2195)Top Navigation + Sidebar')
    db.dpace.insert( f0= 'pa2197', f1= '(2197)Boxed')
    db.dpace.insert( f0= 'pa2199', f1= '(2199)Fixed Sidebar')
    db.dpace.insert( f0= 'pa2201', f1= '(2201)Fixed Navbar')
    db.dpace.insert( f0= 'pa2203', f1= '(2203)Fixed Footer')
    db.dpace.insert( f0= 'pa2205', f1= '(2205)Collapsed Sidebar')
    db.dpace.insert( f0= 'pa2207', f1= '(2207)ChartJS')
    db.dpace.insert( f0= 'pa2209', f1= '(2209)Flot')
    db.dpace.insert( f0= 'pa2211', f1= '(2211)Inline')
    db.dpace.insert( f0= 'pa2213', f1= '(2213)General')
    db.dpace.insert( f0= 'pa2215', f1= '(2215)Icons')
    db.dpace.insert( f0= 'pa2217', f1= '(2217)Buttons')
    db.dpace.insert( f0= 'pa2219', f1= '(2219)Sliders')
    db.dpace.insert( f0= 'pa2221', f1= '(2221)Modals & Alerts')
    db.dpace.insert( f0= 'pa2223', f1= '(2223)Navbar & Tabs')
    db.dpace.insert( f0= 'pa2225', f1= '(2225)Timeline')
    db.dpace.insert( f0= 'pa2227', f1= '(2227)Ribbons')
    db.dpace.insert( f0= 'pa2229', f1= '(2229)General Elements')
    db.dpace.insert( f0= 'pa2231', f1= '(2231)Advanced Elements')
    db.dpace.insert( f0= 'pa2233', f1= '(2233)Editors')
    db.dpace.insert( f0= 'pa2235', f1= '(2235)Validation')
    db.dpace.insert( f0= 'pa2237', f1= '(2237)Simple Tables')
    db.dpace.insert( f0= 'pa2239', f1= '(2239)DataTables')
    db.dpace.insert( f0= 'pa2241', f1= '(2241)jsGrid')
    db.dpace.insert( f0= 'lb2242', f1= '(2242)EXAMPLES')
    db.dpace.insert( f0= 'sx2244', f1= '(2244)2')
    db.dpace.insert( f0= 'pa2247', f1= '(2247)Inbox')
    db.dpace.insert( f0= 'pa2249', f1= '(2249)Compose')
    db.dpace.insert( f0= 'pa2251', f1= '(2251)Read')
    db.dpace.insert( f0= 'pa2253', f1= '(2253)Invoice')
    db.dpace.insert( f0= 'pa2255', f1= '(2255)Profile')
    db.dpace.insert( f0= 'pa2257', f1= '(2257)E-commerce')
    db.dpace.insert( f0= 'pa2259', f1= '(2259)Projects')
    db.dpace.insert( f0= 'pa2261', f1= '(2261)Project Add')
    db.dpace.insert( f0= 'pa2263', f1= '(2263)Project Edit')
    db.dpace.insert( f0= 'pa2265', f1= '(2265)Project Detail')
    db.dpace.insert( f0= 'pa2267', f1= '(2267)Contacts')
    db.dpace.insert( f0= 'pa2269', f1= '(2269)Login')
    db.dpace.insert( f0= 'pa2271', f1= '(2271)Register')
    db.dpace.insert( f0= 'pa2273', f1= '(2273)Forgot Password')
    db.dpace.insert( f0= 'pa2275', f1= '(2275)Recover Password')
    db.dpace.insert( f0= 'pa2277', f1= '(2277)Lockscreen')
    db.dpace.insert( f0= 'pa2279', f1= '(2279)Legacy User Menu')
    db.dpace.insert( f0= 'pa2281', f1= '(2281)Language Menu')
    db.dpace.insert( f0= 'pa2283', f1= '(2283)Error 404')
    db.dpace.insert( f0= 'pa2285', f1= '(2285)Error 500')
    db.dpace.insert( f0= 'pa2287', f1= '(2287)Pace')
    db.dpace.insert( f0= 'pa2289', f1= '(2289)Blank Page')
    db.dpace.insert( f0= 'pa2291', f1= '(2291)Starter Page')
    db.dpace.insert( f0= 'lb2292', f1= '(2292)MISCELLANEOUS')
    db.dpace.insert( f0= 'pa2293', f1= '(2293)Documentation')
    db.dpace.insert( f0= 'lb2294', f1= '(2294)MULTI LEVEL EXAMPLE')
    db.dpace.insert( f0= 'pa2295', f1= '(2295)Level 1')
    db.dpace.insert( f0= 'pa2296', f1= '(2296)Level 2')
    db.dpace.insert( f0= 'pa2297', f1= '(2297)Level 3')
    db.dpace.insert( f0= 'pa2298', f1= '(2298)Level 3')
    db.dpace.insert( f0= 'pa2299', f1= '(2299)Level 3')
    db.dpace.insert( f0= 'pa2300', f1= '(2300)Level 2')
    db.dpace.insert( f0= 'pa2301', f1= '(2301)Level 1')
    db.dpace.insert( f0= 'lb2302', f1= '(2302)LABELS')
    db.dpace.insert( f0= 'pc2303', f1= '(2303)Important')
    db.dpace.insert( f0= 'pa2304', f1= '(2304)Warning')
    db.dpace.insert( f0= 'pa2305', f1= '(2305)Informational')
    db.dpace.insert( f0= 'hh2306', f1= '(2306)Pace')
    db.dpace.insert( f0= 'aa2307', f1= '(2307)Home')
    db.dpace.insert( f0= 'lb2308', f1= '(2308)Pace')
    db.dpace.insert( f0= 'hc2309', f1= '(2309)Title')
    db.dpace.insert( f0= 'bb2310', f1= '(2310)Version')
    db.dpace.insert( f0= 'aa2311', f1= '(2311)AdminLTE.io')
    db.commit()
#
