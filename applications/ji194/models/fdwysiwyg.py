#
# table for controller: wysiwyg
#

from gluon.contrib.populate import populate

db.define_table('dwysiwyg', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dwysiwyg.id ).count():
    db.dwysiwyg.insert( f0= 'sx4997', f1= '(4997)Toggle sidebar')
    db.dwysiwyg.insert( f0= 'sx4999', f1= '(4999)Software Update')
    db.dwysiwyg.insert( f0= 'sx5000', f1= '(5000)65%')
    db.dwysiwyg.insert( f0= 'sx5001', f1= '(5001)Hardware Upgrade')
    db.dwysiwyg.insert( f0= 'sx5002', f1= '(5002)35%')
    db.dwysiwyg.insert( f0= 'sx5003', f1= '(5003)Unit Testing')
    db.dwysiwyg.insert( f0= 'sx5004', f1= '(5004)15%')
    db.dwysiwyg.insert( f0= 'sx5005', f1= '(5005)Bug Fixes')
    db.dwysiwyg.insert( f0= 'sx5006', f1= '(5006)90%')
    db.dwysiwyg.insert( f0= 'sx5007', f1= '(5007)+12')
    db.dwysiwyg.insert( f0= 'sx5008', f1= '(5008)+8')
    db.dwysiwyg.insert( f0= 'sx5009', f1= '(5009)+11')
    db.dwysiwyg.insert( f0= 'sx5011', f1= '(5011)Alex:')
    db.dwysiwyg.insert( f0= 'sp5012', f1= '(5012)a moment ago')
    db.dwysiwyg.insert( f0= 'sx5014', f1= '(5014)Susan:')
    db.dwysiwyg.insert( f0= 'sp5015', f1= '(5015)20 minutes ago')
    db.dwysiwyg.insert( f0= 'sx5017', f1= '(5017)Bob:')
    db.dwysiwyg.insert( f0= 'sp5018', f1= '(5018)3:15 pm')
    db.dwysiwyg.insert( f0= 'sx5020', f1= '(5020)Kate:')
    db.dwysiwyg.insert( f0= 'sp5021', f1= '(5021)1:33 pm')
    db.dwysiwyg.insert( f0= 'sx5023', f1= '(5023)Fred:')
    db.dwysiwyg.insert( f0= 'sp5024', f1= '(5024)10:09 am')
    db.dwysiwyg.insert( f0= 'ic5027', f1= '(5027)Welcome,')
    db.dwysiwyg.insert( f0= 'sx5030', f1= '(5030)Dashboard')
    db.dwysiwyg.insert( f0= 'sx5044', f1= '(5044)Tables')
    db.dwysiwyg.insert( f0= 'sx5047', f1= '(5047)Forms')
    db.dwysiwyg.insert( f0= 'sx5054', f1= '(5054)Widgets')
    db.dwysiwyg.insert( f0= 'sx5057', f1= '(5057)Gallery')
    db.dwysiwyg.insert( f0= 'sx5058', f1= '(5058)More Pages')
    db.dwysiwyg.insert( f0= 'aa5072', f1= '(5072)Home')
    db.dwysiwyg.insert( f0= 'aa5073', f1= '(5073)Forms')
    db.dwysiwyg.insert( f0= 'pb5074', f1= '(5074)Search ...')
    db.dwysiwyg.insert( f0= 'bb5075', f1= '(5075).container')
    db.dwysiwyg.insert( f0= 'hd5076', f1= '(5076)Inside Widget')
    db.dwysiwyg.insert( f0= 'di5077', f1= '(5077)unk_0')
    db.dwysiwyg.insert( f0= 'hd5078', f1= '(5078)Markdown Editor')
    db.dwysiwyg.insert( f0= 'di5079', f1= '(5079)unk_1')
    db.dwysiwyg.insert( f0= 'sx5080', f1= '(5080)Ace')
    db.dwysiwyg.insert( f0= 'bu5094', f1= '(5094)&times;')
    db.dwysiwyg.insert( f0= 'sp5095', f1= '(5095)File upload error')
    db.commit()
#
