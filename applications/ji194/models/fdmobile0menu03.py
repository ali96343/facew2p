#
# table for controller: mobileIImenuII3
#

from gluon.contrib.populate import populate

db.define_table('dmobile0menu03', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dmobile0menu03.id ).count():
    db.dmobile0menu03.insert( f0= 'sx4894', f1= '(4894)Toggle user menu')
    db.dmobile0menu03.insert( f0= 'sx4896', f1= '(4896)Toggle sidebar')
    db.dmobile0menu03.insert( f0= 'sx4897', f1= '(4897)Software Update')
    db.dmobile0menu03.insert( f0= 'sx4898', f1= '(4898)65%')
    db.dmobile0menu03.insert( f0= 'sx4899', f1= '(4899)Hardware Upgrade')
    db.dmobile0menu03.insert( f0= 'sx4900', f1= '(4900)35%')
    db.dmobile0menu03.insert( f0= 'sx4901', f1= '(4901)Unit Testing')
    db.dmobile0menu03.insert( f0= 'sx4902', f1= '(4902)15%')
    db.dmobile0menu03.insert( f0= 'sx4903', f1= '(4903)Bug Fixes')
    db.dmobile0menu03.insert( f0= 'sx4904', f1= '(4904)90%')
    db.dmobile0menu03.insert( f0= 'sx4906', f1= '(4906)Alex:')
    db.dmobile0menu03.insert( f0= 'sp4907', f1= '(4907)a moment ago')
    db.dmobile0menu03.insert( f0= 'sx4909', f1= '(4909)Susan:')
    db.dmobile0menu03.insert( f0= 'sp4910', f1= '(4910)20 minutes ago')
    db.dmobile0menu03.insert( f0= 'sx4912', f1= '(4912)Bob:')
    db.dmobile0menu03.insert( f0= 'sp4913', f1= '(4913)3:15 pm')
    db.dmobile0menu03.insert( f0= 'sx4915', f1= '(4915)Kate:')
    db.dmobile0menu03.insert( f0= 'sp4916', f1= '(4916)1:33 pm')
    db.dmobile0menu03.insert( f0= 'sx4918', f1= '(4918)Fred:')
    db.dmobile0menu03.insert( f0= 'sp4919', f1= '(4919)10:09 am')
    db.dmobile0menu03.insert( f0= 'ic4922', f1= '(4922)Welcome,')
    db.dmobile0menu03.insert( f0= 'sx4925', f1= '(4925)Dashboard')
    db.dmobile0menu03.insert( f0= 'sx4939', f1= '(4939)Tables')
    db.dmobile0menu03.insert( f0= 'sx4942', f1= '(4942)Forms')
    db.dmobile0menu03.insert( f0= 'sx4949', f1= '(4949)Widgets')
    db.dmobile0menu03.insert( f0= 'sx4952', f1= '(4952)Gallery')
    db.dmobile0menu03.insert( f0= 'sx4953', f1= '(4953)More Pages')
    db.dmobile0menu03.insert( f0= 'aa4967', f1= '(4967)Home')
    db.dmobile0menu03.insert( f0= 'aa4968', f1= '(4968)Layouts')
    db.dmobile0menu03.insert( f0= 'lb4969', f1= '(4969)Mobile Menu 3')
    db.dmobile0menu03.insert( f0= 'pb4970', f1= '(4970)Search ...')
    db.dmobile0menu03.insert( f0= 'bb4971', f1= '(4971).container')
    db.dmobile0menu03.insert( f0= 'hh4972', f1= '(4972)Collapsible Responsive(mobile) Menu')
    db.dmobile0menu03.insert( f0= 'sx4973', f1= '(4973)mobile menu')
    db.dmobile0menu03.insert( f0= 'sx4974', f1= '(4974)992px')
    db.dmobile0menu03.insert( f0= 'sx4975', f1= '(4975)992px')
    db.dmobile0menu03.insert( f0= 'sx4976', f1= '(4976)Ace')
    db.commit()
#
