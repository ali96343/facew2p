#
# table for controller: countdown
#

from gluon.contrib.populate import populate

db.define_table('dcountdown', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcountdown.id ).count():
    db.dcountdown.insert( f0= 'sx2994', f1= '(2994)UC')
    db.dcountdown.insert( f0= 'sx2995', f1= '(2995)U')
    db.dcountdown.insert( f0= 'hh2996', f1= '(2996)Our Site')
    db.dcountdown.insert( f0= 'si2997', f1= '(2997)We are done with the backend just front end to go. The site will launch in:')
    db.dcountdown.insert( f0= 'di2998', f1= '(2998)DAYS')
    db.dcountdown.insert( f0= 'di2999', f1= '(2999)HOURS')
    db.dcountdown.insert( f0= 'di3000', f1= '(3000)MINUTES')
    db.dcountdown.insert( f0= 'di3001', f1= '(3001)SECOND')
    db.dcountdown.insert( f0= 'pb3002', f1= '(3002)Enter your email to subscribe')
    db.dcountdown.insert( f0= 'bu3003', f1= '(3003)Submit')
    db.dcountdown.insert( f0= 'bu3004', f1= '(3004)Cancel')
    db.dcountdown.insert( f0= 'pb3005', f1= '(3005)Enter yor name')
    db.dcountdown.insert( f0= 'pb3006', f1= '(3006)Enter your e-mail')
    db.dcountdown.insert( f0= 'pb3007', f1= '(3007)Enter your subject')
    db.dcountdown.insert( f0= 'pb3008', f1= '(3008)Enter your message')
    db.dcountdown.insert( f0= 'bu3009', f1= '(3009)Submit')
    db.dcountdown.insert( f0= 'bu3010', f1= '(3010)Cancel')
    db.dcountdown.insert( f0= 'hh3011', f1= '(3011)Contact info')
    db.dcountdown.insert( f0= 'ma3013', f1= '(3013)mail@domain.com')
    db.commit()
#
