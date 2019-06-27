#
# table for controller: email
#

from gluon.contrib.populate import populate

db.define_table('demail', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.demail.id ).count():
    db.demail.insert( f0= 'sx2519', f1= '(2519)Toggle sidebar')
    db.demail.insert( f0= 'sx2521', f1= '(2521)Software Update')
    db.demail.insert( f0= 'sx2522', f1= '(2522)65%')
    db.demail.insert( f0= 'sx2523', f1= '(2523)Hardware Upgrade')
    db.demail.insert( f0= 'sx2524', f1= '(2524)35%')
    db.demail.insert( f0= 'sx2525', f1= '(2525)Unit Testing')
    db.demail.insert( f0= 'sx2526', f1= '(2526)15%')
    db.demail.insert( f0= 'sx2527', f1= '(2527)Bug Fixes')
    db.demail.insert( f0= 'sx2528', f1= '(2528)90%')
    db.demail.insert( f0= 'sx2529', f1= '(2529)+12')
    db.demail.insert( f0= 'sx2530', f1= '(2530)+8')
    db.demail.insert( f0= 'sx2531', f1= '(2531)+11')
    db.demail.insert( f0= 'sx2533', f1= '(2533)Alex:')
    db.demail.insert( f0= 'sp2534', f1= '(2534)a moment ago')
    db.demail.insert( f0= 'sx2536', f1= '(2536)Susan:')
    db.demail.insert( f0= 'sp2537', f1= '(2537)20 minutes ago')
    db.demail.insert( f0= 'sx2539', f1= '(2539)Bob:')
    db.demail.insert( f0= 'sp2540', f1= '(2540)3:15 pm')
    db.demail.insert( f0= 'sx2542', f1= '(2542)Kate:')
    db.demail.insert( f0= 'sp2543', f1= '(2543)1:33 pm')
    db.demail.insert( f0= 'sx2545', f1= '(2545)Fred:')
    db.demail.insert( f0= 'sp2546', f1= '(2546)10:09 am')
    db.demail.insert( f0= 'ic2549', f1= '(2549)Welcome,')
    db.demail.insert( f0= 'sx2552', f1= '(2552)Dashboard')
    db.demail.insert( f0= 'sx2566', f1= '(2566)Tables')
    db.demail.insert( f0= 'sx2569', f1= '(2569)Forms')
    db.demail.insert( f0= 'sx2576', f1= '(2576)Widgets')
    db.demail.insert( f0= 'sx2579', f1= '(2579)Gallery')
    db.demail.insert( f0= 'sx2580', f1= '(2580)More Pages')
    db.demail.insert( f0= 'aa2594', f1= '(2594)Home')
    db.demail.insert( f0= 'aa2595', f1= '(2595)More Pages')
    db.demail.insert( f0= 'lb2596', f1= '(2596)Email Templates')
    db.demail.insert( f0= 'pb2597', f1= '(2597)Search ...')
    db.demail.insert( f0= 'bb2598', f1= '(2598).container')
    db.demail.insert( f0= 'sx2607', f1= '(2607)Ace')
    db.commit()
#
