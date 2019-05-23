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
    db.dcountdown.insert( f0= 'sx2889', f1= '(2889)UC')
    db.dcountdown.insert( f0= 'hh2890', f1= '(2890)Our Site')
    db.dcountdown.insert( f0= 'si2891', f1= '(2891)We are done with the backend just front end to go. The site will launch in:')
    db.dcountdown.insert( f0= 'di2892', f1= '(2892)DAYS')
    db.dcountdown.insert( f0= 'di2893', f1= '(2893)HOURS')
    db.dcountdown.insert( f0= 'di2894', f1= '(2894)MINUTES')
    db.dcountdown.insert( f0= 'di2895', f1= '(2895)SECOND')
    db.dcountdown.insert( f0= 'pb2896', f1= '(2896)Enter your email to subscribe')
    db.dcountdown.insert( f0= 'bu2897', f1= '(2897)Submit')
    db.dcountdown.insert( f0= 'bu2898', f1= '(2898)Cancel')
    db.dcountdown.insert( f0= 'pb2899', f1= '(2899)Enter yor name')
    db.dcountdown.insert( f0= 'pb2900', f1= '(2900)Enter your e-mail')
    db.dcountdown.insert( f0= 'pb2901', f1= '(2901)Enter your subject')
    db.dcountdown.insert( f0= 'pb2902', f1= '(2902)Enter your message')
    db.dcountdown.insert( f0= 'bu2903', f1= '(2903)Submit')
    db.dcountdown.insert( f0= 'bu2904', f1= '(2904)Cancel')
    db.dcountdown.insert( f0= 'hh2905', f1= '(2905)Contact info')
    db.dcountdown.insert( f0= 'ma2907', f1= '(2907)mail@domain.com')
    db.commit()
#
