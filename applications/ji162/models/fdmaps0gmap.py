#
# table for controller: maps_gmap
#

from gluon.contrib.populate import populate

db.define_table('dmaps0gmap', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dmaps0gmap.id ).count():
    db.dmaps0gmap.insert( f0= 'hc2221', f1= '(2221)UI elements')
    db.dmaps0gmap.insert( f0= 'aa2223', f1= '(2223)Buttons')
    db.dmaps0gmap.insert( f0= 'aa2225', f1= '(2225)Badges')
    db.dmaps0gmap.insert( f0= 'aa2227', f1= '(2227)Tabs')
    db.dmaps0gmap.insert( f0= 'aa2229', f1= '(2229)Social Buttons')
    db.dmaps0gmap.insert( f0= 'aa2231', f1= '(2231)Cards')
    db.dmaps0gmap.insert( f0= 'aa2233', f1= '(2233)Alerts')
    db.dmaps0gmap.insert( f0= 'aa2235', f1= '(2235)Progress Bars')
    db.dmaps0gmap.insert( f0= 'aa2237', f1= '(2237)Modals')
    db.dmaps0gmap.insert( f0= 'aa2239', f1= '(2239)Switches')
    db.dmaps0gmap.insert( f0= 'aa2241', f1= '(2241)Grids')
    db.dmaps0gmap.insert( f0= 'aa2243', f1= '(2243)Typography')
    db.dmaps0gmap.insert( f0= 'aa2245', f1= '(2245)Basic Table')
    db.dmaps0gmap.insert( f0= 'aa2247', f1= '(2247)Data Table')
    db.dmaps0gmap.insert( f0= 'aa2249', f1= '(2249)Basic Form')
    db.dmaps0gmap.insert( f0= 'aa2251', f1= '(2251)Advanced Form')
    db.dmaps0gmap.insert( f0= 'hc2252', f1= '(2252)Icons')
    db.dmaps0gmap.insert( f0= 'aa2254', f1= '(2254)Font Awesome')
    db.dmaps0gmap.insert( f0= 'aa2256', f1= '(2256)Themefy Icons')
    db.dmaps0gmap.insert( f0= 'aa2259', f1= '(2259)Chart JS')
    db.dmaps0gmap.insert( f0= 'aa2261', f1= '(2261)Flot Chart')
    db.dmaps0gmap.insert( f0= 'aa2263', f1= '(2263)Peity Chart')
    db.dmaps0gmap.insert( f0= 'aa2265', f1= '(2265)Google Maps')
    db.dmaps0gmap.insert( f0= 'aa2267', f1= '(2267)Vector Maps')
    db.dmaps0gmap.insert( f0= 'hc2268', f1= '(2268)Extras')
    db.dmaps0gmap.insert( f0= 'aa2270', f1= '(2270)Login')
    db.dmaps0gmap.insert( f0= 'aa2272', f1= '(2272)Register')
    db.dmaps0gmap.insert( f0= 'aa2274', f1= '(2274)Forget Pass')
    db.dmaps0gmap.insert( f0= 'pb2275', f1= '(2275)Search ...')
    db.dmaps0gmap.insert( f0= 'pc2276', f1= '(2276)You have 3 Notification')
    db.dmaps0gmap.insert( f0= 'pc2277', f1= '(2277)You have 4 Mails')
    db.dmaps0gmap.insert( f0= 'sx2279', f1= '(2279)Jonathan Smith')
    db.dmaps0gmap.insert( f0= 'sx2280', f1= '(2280)Just now')
    db.dmaps0gmap.insert( f0= 'pa2281', f1= '(2281)Hello, this is an example msg')
    db.dmaps0gmap.insert( f0= 'sx2283', f1= '(2283)Jack Sanders')
    db.dmaps0gmap.insert( f0= 'sx2284', f1= '(2284)5 minutes ago')
    db.dmaps0gmap.insert( f0= 'pa2285', f1= '(2285)Lorem ipsum dolor sit amet, consectetur')
    db.dmaps0gmap.insert( f0= 'sx2287', f1= '(2287)Cheryl Wheeler')
    db.dmaps0gmap.insert( f0= 'sx2288', f1= '(2288)10 minutes ago')
    db.dmaps0gmap.insert( f0= 'pa2289', f1= '(2289)Hello, this is an example msg')
    db.dmaps0gmap.insert( f0= 'sx2291', f1= '(2291)Rachel Santos')
    db.dmaps0gmap.insert( f0= 'sx2292', f1= '(2292)15 minutes ago')
    db.dmaps0gmap.insert( f0= 'pa2293', f1= '(2293)Lorem ipsum dolor sit amet, consectetur')
    db.dmaps0gmap.insert( f0= 'sx2295', f1= '(2295)13')
    db.dmaps0gmap.insert( f0= 'hh2296', f1= '(2296)Dashboard')
    db.dmaps0gmap.insert( f0= 'aa2297', f1= '(2297)Dashboard')
    db.dmaps0gmap.insert( f0= 'aa2298', f1= '(2298)Map')
    db.dmaps0gmap.insert( f0= 'lb2299', f1= '(2299)Gmap')
    db.dmaps0gmap.insert( f0= 'hh2300', f1= '(2300)Basic Map')
    db.dmaps0gmap.insert( f0= 'hh2301', f1= '(2301)Fusion Tables layers')
    db.dmaps0gmap.insert( f0= 'hh2302', f1= '(2302)Geometry overlays')
    db.dmaps0gmap.insert( f0= 'hh2303', f1= '(2303)Elevation locations')
    db.dmaps0gmap.insert( f0= 'hh2304', f1= '(2304)Geolocation')
    db.dmaps0gmap.insert( f0= 'hh2305', f1= '(2305)KML layers')
    db.dmaps0gmap.insert( f0= 'hh2306', f1= '(2306)Layers')
    db.dmaps0gmap.insert( f0= 'hh2307', f1= '(2307)Map events')
    db.commit()
#
