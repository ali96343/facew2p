#
# table for controller: emailIInewsletter
#

from gluon.contrib.populate import populate

db.define_table('demail0newsletter', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.demail0newsletter.id ).count():
    db.demail0newsletter.insert( f0= 'aa5113', f1= '(5113)Click here to see them')
    db.demail0newsletter.insert( f0= 'bb5125', f1= '(5125)Nullam massa sapien')
    db.demail0newsletter.insert( f0= 'bb5130', f1= '(5130)Convallis eget')
    db.demail0newsletter.insert( f0= 'ix5134', f1= '(5134)Integer eget odio est, eget malesuada lorem:')
    db.demail0newsletter.insert( f0= 'sx5144', f1= '(5144)Wednesday')
    db.demail0newsletter.insert( f0= 'bb5146', f1= '(5146)Convallis eget nisi mauris a sagittis dui')
    db.demail0newsletter.insert( f0= 'sx5149', f1= '(5149)Monday')
    db.demail0newsletter.insert( f0= 'bb5151', f1= '(5151)Pellentesque sem dolor, fringilla et pharetra vitae')
    db.demail0newsletter.insert( f0= 'aa5155', f1= '(5155)Twitter')
    db.demail0newsletter.insert( f0= 'aa5156', f1= '(5156)Facebook')
    db.demail0newsletter.insert( f0= 'aa5157', f1= '(5157)Google+')
    db.demail0newsletter.insert( f0= 'ma5159', f1= '(5159)hseldon@trantor.com')
    db.demail0newsletter.insert( f0= 'di5162', f1= '(5162)&copy; 2014 by Ace Company')
    db.demail0newsletter.insert( f0= 'aa5164', f1= '(5164)Terms')
    db.demail0newsletter.insert( f0= 'aa5165', f1= '(5165)Privacy')
    db.demail0newsletter.insert( f0= 'aa5166', f1= '(5166)Unsubscribe')
    db.commit()
#
