#
# table for controller: tables
#

from gluon.contrib.populate import populate

db.define_table('dtables', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtables.id ).count():
    db.dtables.insert( f0= 'sx2217', f1= '(2217)Toggle sidebar')
    db.dtables.insert( f0= 'sx2219', f1= '(2219)Software Update')
    db.dtables.insert( f0= 'sx2220', f1= '(2220)65%')
    db.dtables.insert( f0= 'sx2221', f1= '(2221)Hardware Upgrade')
    db.dtables.insert( f0= 'sx2222', f1= '(2222)35%')
    db.dtables.insert( f0= 'sx2223', f1= '(2223)Unit Testing')
    db.dtables.insert( f0= 'sx2224', f1= '(2224)15%')
    db.dtables.insert( f0= 'sx2225', f1= '(2225)Bug Fixes')
    db.dtables.insert( f0= 'sx2226', f1= '(2226)90%')
    db.dtables.insert( f0= 'sx2227', f1= '(2227)+12')
    db.dtables.insert( f0= 'sx2228', f1= '(2228)+8')
    db.dtables.insert( f0= 'sx2229', f1= '(2229)+11')
    db.dtables.insert( f0= 'sx2231', f1= '(2231)Alex:')
    db.dtables.insert( f0= 'sp2232', f1= '(2232)a moment ago')
    db.dtables.insert( f0= 'sx2234', f1= '(2234)Susan:')
    db.dtables.insert( f0= 'sp2235', f1= '(2235)20 minutes ago')
    db.dtables.insert( f0= 'sx2237', f1= '(2237)Bob:')
    db.dtables.insert( f0= 'sp2238', f1= '(2238)3:15 pm')
    db.dtables.insert( f0= 'sx2240', f1= '(2240)Kate:')
    db.dtables.insert( f0= 'sp2241', f1= '(2241)1:33 pm')
    db.dtables.insert( f0= 'sx2243', f1= '(2243)Fred:')
    db.dtables.insert( f0= 'sp2244', f1= '(2244)10:09 am')
    db.dtables.insert( f0= 'ic2247', f1= '(2247)Welcome,')
    db.dtables.insert( f0= 'sx2250', f1= '(2250)Dashboard')
    db.dtables.insert( f0= 'sx2264', f1= '(2264)Tables')
    db.dtables.insert( f0= 'sx2267', f1= '(2267)Forms')
    db.dtables.insert( f0= 'sx2274', f1= '(2274)Widgets')
    db.dtables.insert( f0= 'sx2277', f1= '(2277)Gallery')
    db.dtables.insert( f0= 'sx2278', f1= '(2278)More Pages')
    db.dtables.insert( f0= 'aa2292', f1= '(2292)Home')
    db.dtables.insert( f0= 'aa2293', f1= '(2293)Tables')
    db.dtables.insert( f0= 'pb2294', f1= '(2294)Search ...')
    db.dtables.insert( f0= 'bb2295', f1= '(2295).container')
    db.dtables.insert( f0= 'sx2296', f1= '(2296)Details')
    db.dtables.insert( f0= 'aa2297', f1= '(2297)ace.com')
    db.dtables.insert( f0= 'sx2298', f1= '(2298)Expiring')
    db.dtables.insert( f0= 'sx2300', f1= '(2300)Alex M. Doe')
    db.dtables.insert( f0= 'di2301', f1= '(2301)Username')
    db.dtables.insert( f0= 'sp2302', f1= '(2302)alexdoe')
    db.dtables.insert( f0= 'di2303', f1= '(2303)Location')
    db.dtables.insert( f0= 'sp2304', f1= '(2304)Netherlands, Amsterdam')
    db.dtables.insert( f0= 'di2305', f1= '(2305)Age')
    db.dtables.insert( f0= 'sp2306', f1= '(2306)38')
    db.dtables.insert( f0= 'di2307', f1= '(2307)Joined')
    db.dtables.insert( f0= 'sp2308', f1= '(2308)2010/06/20')
    db.dtables.insert( f0= 'di2309', f1= '(2309)Last Online')
    db.dtables.insert( f0= 'sp2310', f1= '(2310)3 hours ago')
    db.dtables.insert( f0= 'di2311', f1= '(2311)About Me')
    db.dtables.insert( f0= 'sp2312', f1= '(2312)Bio')
    db.dtables.insert( f0= 'hd2313', f1= '(2313)Send a message to Alex')
    db.dtables.insert( f0= 'pb2314', f1= '(2314)Type something')
    db.dtables.insert( f0= 'sx2315', f1= '(2315)Email me a copy')
    db.dtables.insert( f0= 'sx2316', f1= '(2316)Details')
    db.dtables.insert( f0= 'aa2317', f1= '(2317)base.com')
    db.dtables.insert( f0= 'sx2318', f1= '(2318)Registered')
    db.dtables.insert( f0= 'sx2320', f1= '(2320)Alex M. Doe')
    db.dtables.insert( f0= 'di2321', f1= '(2321)Username')
    db.dtables.insert( f0= 'sp2322', f1= '(2322)alexdoe')
    db.dtables.insert( f0= 'di2323', f1= '(2323)Location')
    db.dtables.insert( f0= 'sp2324', f1= '(2324)Netherlands, Amsterdam')
    db.dtables.insert( f0= 'di2325', f1= '(2325)Age')
    db.dtables.insert( f0= 'sp2326', f1= '(2326)38')
    db.dtables.insert( f0= 'di2327', f1= '(2327)Joined')
    db.dtables.insert( f0= 'sp2328', f1= '(2328)2010/06/20')
    db.dtables.insert( f0= 'di2329', f1= '(2329)Last Online')
    db.dtables.insert( f0= 'sp2330', f1= '(2330)3 hours ago')
    db.dtables.insert( f0= 'di2331', f1= '(2331)About Me')
    db.dtables.insert( f0= 'sp2332', f1= '(2332)Bio')
    db.dtables.insert( f0= 'hd2333', f1= '(2333)Send a message to Alex')
    db.dtables.insert( f0= 'pb2334', f1= '(2334)Type something')
    db.dtables.insert( f0= 'sx2335', f1= '(2335)Email me a copy')
    db.dtables.insert( f0= 'sx2336', f1= '(2336)Details')
    db.dtables.insert( f0= 'aa2337', f1= '(2337)max.com')
    db.dtables.insert( f0= 'sx2338', f1= '(2338)Expiring')
    db.dtables.insert( f0= 'sx2340', f1= '(2340)Alex M. Doe')
    db.dtables.insert( f0= 'di2341', f1= '(2341)Username')
    db.dtables.insert( f0= 'sp2342', f1= '(2342)alexdoe')
    db.dtables.insert( f0= 'di2343', f1= '(2343)Location')
    db.dtables.insert( f0= 'sp2344', f1= '(2344)Netherlands, Amsterdam')
    db.dtables.insert( f0= 'di2345', f1= '(2345)Age')
    db.dtables.insert( f0= 'sp2346', f1= '(2346)38')
    db.dtables.insert( f0= 'di2347', f1= '(2347)Joined')
    db.dtables.insert( f0= 'sp2348', f1= '(2348)2010/06/20')
    db.dtables.insert( f0= 'di2349', f1= '(2349)Last Online')
    db.dtables.insert( f0= 'sp2350', f1= '(2350)3 hours ago')
    db.dtables.insert( f0= 'di2351', f1= '(2351)About Me')
    db.dtables.insert( f0= 'sp2352', f1= '(2352)Bio')
    db.dtables.insert( f0= 'hd2353', f1= '(2353)Send a message to Alex')
    db.dtables.insert( f0= 'pb2354', f1= '(2354)Type something')
    db.dtables.insert( f0= 'sx2355', f1= '(2355)Email me a copy')
    db.dtables.insert( f0= 'sx2356', f1= '(2356)Details')
    db.dtables.insert( f0= 'aa2357', f1= '(2357)best.com')
    db.dtables.insert( f0= 'sx2358', f1= '(2358)Flagged')
    db.dtables.insert( f0= 'sx2360', f1= '(2360)Alex M. Doe')
    db.dtables.insert( f0= 'di2361', f1= '(2361)Username')
    db.dtables.insert( f0= 'sp2362', f1= '(2362)alexdoe')
    db.dtables.insert( f0= 'di2363', f1= '(2363)Location')
    db.dtables.insert( f0= 'sp2364', f1= '(2364)Netherlands, Amsterdam')
    db.dtables.insert( f0= 'di2365', f1= '(2365)Age')
    db.dtables.insert( f0= 'sp2366', f1= '(2366)38')
    db.dtables.insert( f0= 'di2367', f1= '(2367)Joined')
    db.dtables.insert( f0= 'sp2368', f1= '(2368)2010/06/20')
    db.dtables.insert( f0= 'di2369', f1= '(2369)Last Online')
    db.dtables.insert( f0= 'sp2370', f1= '(2370)3 hours ago')
    db.dtables.insert( f0= 'di2371', f1= '(2371)About Me')
    db.dtables.insert( f0= 'sp2372', f1= '(2372)Bio')
    db.dtables.insert( f0= 'hd2373', f1= '(2373)Send a message to Alex')
    db.dtables.insert( f0= 'pb2374', f1= '(2374)Type something')
    db.dtables.insert( f0= 'sx2375', f1= '(2375)Email me a copy')
    db.dtables.insert( f0= 'sx2376', f1= '(2376)Details')
    db.dtables.insert( f0= 'aa2377', f1= '(2377)pro.com')
    db.dtables.insert( f0= 'sx2378', f1= '(2378)Registered')
    db.dtables.insert( f0= 'sx2380', f1= '(2380)Alex M. Doe')
    db.dtables.insert( f0= 'di2381', f1= '(2381)Username')
    db.dtables.insert( f0= 'sp2382', f1= '(2382)alexdoe')
    db.dtables.insert( f0= 'di2383', f1= '(2383)Location')
    db.dtables.insert( f0= 'sp2384', f1= '(2384)Netherlands, Amsterdam')
    db.dtables.insert( f0= 'di2385', f1= '(2385)Age')
    db.dtables.insert( f0= 'sp2386', f1= '(2386)38')
    db.dtables.insert( f0= 'di2387', f1= '(2387)Joined')
    db.dtables.insert( f0= 'sp2388', f1= '(2388)2010/06/20')
    db.dtables.insert( f0= 'di2389', f1= '(2389)Last Online')
    db.dtables.insert( f0= 'sp2390', f1= '(2390)3 hours ago')
    db.dtables.insert( f0= 'di2391', f1= '(2391)About Me')
    db.dtables.insert( f0= 'sp2392', f1= '(2392)Bio')
    db.dtables.insert( f0= 'hd2393', f1= '(2393)Send a message to Alex')
    db.dtables.insert( f0= 'pb2394', f1= '(2394)Type something')
    db.dtables.insert( f0= 'sx2395', f1= '(2395)Email me a copy')
    db.dtables.insert( f0= 'aa2396', f1= '(2396)Table Inside a Modal Box')
    db.dtables.insert( f0= 'hc2397', f1= '(2397)jQuery dataTables')
    db.dtables.insert( f0= 'aa2398', f1= '(2398)app.com')
    db.dtables.insert( f0= 'sx2399', f1= '(2399)Expiring')
    db.dtables.insert( f0= 'aa2400', f1= '(2400)base.com')
    db.dtables.insert( f0= 'sx2401', f1= '(2401)Registered')
    db.dtables.insert( f0= 'aa2402', f1= '(2402)max.com')
    db.dtables.insert( f0= 'sx2403', f1= '(2403)Expiring')
    db.dtables.insert( f0= 'aa2404', f1= '(2404)best.com')
    db.dtables.insert( f0= 'sx2405', f1= '(2405)Flagged')
    db.dtables.insert( f0= 'aa2406', f1= '(2406)pro.com')
    db.dtables.insert( f0= 'sx2407', f1= '(2407)Registered')
    db.dtables.insert( f0= 'aa2408', f1= '(2408)team.com')
    db.dtables.insert( f0= 'sx2409', f1= '(2409)Flagged')
    db.dtables.insert( f0= 'aa2410', f1= '(2410)up.com')
    db.dtables.insert( f0= 'sx2411', f1= '(2411)Sold')
    db.dtables.insert( f0= 'aa2412', f1= '(2412)view.com')
    db.dtables.insert( f0= 'sx2413', f1= '(2413)Registered')
    db.dtables.insert( f0= 'aa2414', f1= '(2414)nice.com')
    db.dtables.insert( f0= 'sx2415', f1= '(2415)Sold')
    db.dtables.insert( f0= 'aa2416', f1= '(2416)fine.com')
    db.dtables.insert( f0= 'sx2417', f1= '(2417)Expiring')
    db.dtables.insert( f0= 'aa2418', f1= '(2418)good.com')
    db.dtables.insert( f0= 'sx2419', f1= '(2419)Flagged')
    db.dtables.insert( f0= 'aa2420', f1= '(2420)great.com')
    db.dtables.insert( f0= 'sx2421', f1= '(2421)Registered')
    db.dtables.insert( f0= 'aa2422', f1= '(2422)shine.com')
    db.dtables.insert( f0= 'sx2423', f1= '(2423)Flagged')
    db.dtables.insert( f0= 'aa2424', f1= '(2424)rise.com')
    db.dtables.insert( f0= 'sx2425', f1= '(2425)Sold')
    db.dtables.insert( f0= 'aa2426', f1= '(2426)above.com')
    db.dtables.insert( f0= 'sx2427', f1= '(2427)Expiring')
    db.dtables.insert( f0= 'aa2428', f1= '(2428)share.com')
    db.dtables.insert( f0= 'sx2429', f1= '(2429)Sold')
    db.dtables.insert( f0= 'aa2430', f1= '(2430)fair.com')
    db.dtables.insert( f0= 'sx2431', f1= '(2431)Flagged')
    db.dtables.insert( f0= 'aa2432', f1= '(2432)year.com')
    db.dtables.insert( f0= 'sx2433', f1= '(2433)Expiring')
    db.dtables.insert( f0= 'aa2434', f1= '(2434)day.com')
    db.dtables.insert( f0= 'sx2435', f1= '(2435)Sold')
    db.dtables.insert( f0= 'aa2436', f1= '(2436)light.com')
    db.dtables.insert( f0= 'sx2437', f1= '(2437)Registered')
    db.dtables.insert( f0= 'aa2438', f1= '(2438)sight.com')
    db.dtables.insert( f0= 'sx2439', f1= '(2439)Flagged')
    db.dtables.insert( f0= 'aa2440', f1= '(2440)right.com')
    db.dtables.insert( f0= 'sx2441', f1= '(2441)Expiring')
    db.dtables.insert( f0= 'aa2442', f1= '(2442)once.com')
    db.dtables.insert( f0= 'sx2443', f1= '(2443)Sold')
    db.dtables.insert( f0= 'sx2444', f1= '(2444)&times;')
    db.dtables.insert( f0= 'aa2445', f1= '(2445)ace.com')
    db.dtables.insert( f0= 'aa2446', f1= '(2446)base.com')
    db.dtables.insert( f0= 'aa2447', f1= '(2447)max.com')
    db.dtables.insert( f0= 'aa2448', f1= '(2448)best.com')
    db.dtables.insert( f0= 'aa2449', f1= '(2449)pro.com')
    db.dtables.insert( f0= 'sx2450', f1= '(2450)Ace')
    db.dtables.insert( f0= 'sx2465', f1= '(2465)Show/hide columns')
    db.dtables.insert( f0= 'sx2466', f1= '(2466)Copy to clipboard')
    db.dtables.insert( f0= 'sx2467', f1= '(2467)Export to CSV')
    db.dtables.insert( f0= 'sx2468', f1= '(2468)Export to Excel')
    db.dtables.insert( f0= 'sx2469', f1= '(2469)Export to PDF')
    db.dtables.insert( f0= 'sx2470', f1= '(2470)Print')
    db.commit()
#
