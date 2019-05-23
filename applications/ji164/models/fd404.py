#
# table for controller: X404
#

from gluon.contrib.populate import populate

db.define_table('d404', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.d404.id ).count():
    db.d404.insert( f0= 'sp19374', f1= '(19374)outdated')
    db.d404.insert( f0= 'pc19375', f1= '(19375)to improve your experience.')
    db.d404.insert( f0= 'aa19376', f1= '(19376)upgrade your browser')
    db.d404.insert( f0= 'aa19378', f1= '(19378)Back to Dashboard')
    db.d404.insert( f0= 'sx19379', f1= '(19379)404')
    db.d404.insert( f0= 'hh19380', f1= '(19380)ERROR')
    db.d404.insert( f0= 'pa19381', f1= '(19381)Sorry, but the page you are looking for has note been found. Try checking the URL for error, then hit the refresh button on your browser or try found something else in our app.')
    db.d404.insert( f0= 'aa19382', f1= '(19382)Report Problem')
    db.d404.insert( f0= 'pc19383', f1= '(19383)All rights reserved.')
    db.d404.insert( f0= 'pf19384', f1= '(19384)Copyright  2018')
    db.commit()
#
