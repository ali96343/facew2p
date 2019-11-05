#
# table for controller: starter
#

from gluon.contrib.populate import populate

db.define_table('dstarter', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dstarter.id ).count():
    db.dstarter.insert( f0= 'bb5910', f1= '(5910)A')
    db.dstarter.insert( f0= 'sx5911', f1= '(5911)LT')
    db.dstarter.insert( f0= 'bb5912', f1= '(5912)Admin')
    db.dstarter.insert( f0= 'sx5913', f1= '(5913)LTE')
    db.dstarter.insert( f0= 'sx5914', f1= '(5914)Toggle navigation')
    db.dstarter.insert( f0= 'sx5915', f1= '(5915)4')
    db.dstarter.insert( f0= 'lb5916', f1= '(5916)You have 4 messages')
    db.dstarter.insert( f0= 'ib5918', f1= '(5918)5 mins')
    db.dstarter.insert( f0= 'pa5919', f1= '(5919)Why not buy a new awesome theme?')
    db.dstarter.insert( f0= 'aa5920', f1= '(5920)See All Messages')
    db.dstarter.insert( f0= 'lb5921', f1= '(5921)You have 10 notifications')
    db.dstarter.insert( f0= 'aa5922', f1= '(5922)View all')
    db.dstarter.insert( f0= 'sx5923', f1= '(5923)9')
    db.dstarter.insert( f0= 'lb5924', f1= '(5924)You have 9 tasks')
    db.dstarter.insert( f0= 'sx5925', f1= '(5925)20% Complete')
    db.dstarter.insert( f0= 'aa5926', f1= '(5926)View all tasks')
    db.dstarter.insert( f0= 'sx5928', f1= '(5928)Alexander Pierce')
    db.dstarter.insert( f0= 'ic5930', f1= '(5930)Member since Nov. 2012')
    db.dstarter.insert( f0= 'aa5931', f1= '(5931)Followers')
    db.dstarter.insert( f0= 'aa5932', f1= '(5932)Sales')
    db.dstarter.insert( f0= 'aa5933', f1= '(5933)Friends')
    db.dstarter.insert( f0= 'aa5934', f1= '(5934)Profile')
    db.dstarter.insert( f0= 'aa5935', f1= '(5935)Sign out')
    db.dstarter.insert( f0= 'pa5937', f1= '(5937)Alexander Pierce')
    db.dstarter.insert( f0= 'ia5938', f1= '(5938)Online')
    db.dstarter.insert( f0= 'pb5939', f1= '(5939)Search...')
    db.dstarter.insert( f0= 'lb5940', f1= '(5940)HEADER')
    db.dstarter.insert( f0= 'sp5941', f1= '(5941)Link')
    db.dstarter.insert( f0= 'sp5942', f1= '(5942)Another Link')
    db.dstarter.insert( f0= 'sp5943', f1= '(5943)Multilevel')
    db.dstarter.insert( f0= 'aa5944', f1= '(5944)Link in level 2')
    db.dstarter.insert( f0= 'aa5945', f1= '(5945)Link in level 2')
    db.dstarter.insert( f0= 'ic5946', f1= '(5946)Optional description')
    db.dstarter.insert( f0= 'ia5947', f1= '(5947)Level')
    db.dstarter.insert( f0= 'lb5948', f1= '(5948)Here')
    db.dstarter.insert( f0= 'aa5949', f1= '(5949)Company')
    db.dstarter.insert( f0= 'hc5950', f1= '(5950)Recent Activity')
    db.dstarter.insert( f0= 'hd5951', f1= '(5951)Langdon s Birthday')
    db.dstarter.insert( f0= 'pa5952', f1= '(5952)Will be 23 on April 24th')
    db.dstarter.insert( f0= 'hc5953', f1= '(5953)Tasks Progress')
    db.dstarter.insert( f0= 'di5954', f1= '(5954)Stats Tab Content')
    db.dstarter.insert( f0= 'hc5955', f1= '(5955)General Settings')
    db.commit()
#
