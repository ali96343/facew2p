#
# table for controller: emailIInavbar
#

from gluon.contrib.populate import populate

db.define_table('demail0navbar', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.demail0navbar.id ).count():
    db.demail0navbar.insert( f0= 'aa2812', f1= '(2812)Click it!')
    db.demail0navbar.insert( f0= 'sx2818', f1= '(2818)Sub-head or something')
    db.demail0navbar.insert( f0= 'aa2820', f1= '(2820)Just a Plain Link')
    db.demail0navbar.insert( f0= 'aa2821', f1= '(2821)Just a Plain Link')
    db.demail0navbar.insert( f0= 'aa2822', f1= '(2822)Just a Plain Link')
    db.demail0navbar.insert( f0= 'aa2823', f1= '(2823)Just a Plain Link')
    db.demail0navbar.insert( f0= 'aa2824', f1= '(2824)Just a Plain Link')
    db.demail0navbar.insert( f0= 'aa2825', f1= '(2825)Just a Plain Link')
    db.demail0navbar.insert( f0= 'sx2828', f1= '(2828)408.341.0600')
    db.demail0navbar.insert( f0= 'sx2829', f1= '(2829)hseldon@trantor.com')
    db.demail0navbar.insert( f0= 'di2832', f1= '(2832)&copy; 2014 by Ace Company')
    db.demail0navbar.insert( f0= 'aa2834', f1= '(2834)Terms')
    db.demail0navbar.insert( f0= 'aa2835', f1= '(2835)Privacy')
    db.demail0navbar.insert( f0= 'aa2836', f1= '(2836)Unsubscribe')
    db.commit()
#
