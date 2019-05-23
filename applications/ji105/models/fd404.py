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
    db.d404.insert( f0= 'sp12098', f1= '(12098)outdated')
    db.d404.insert( f0= 'pc12099', f1= '(12099)to improve your experience.')
    db.d404.insert( f0= 'aa12100', f1= '(12100)upgrade your browser')
    db.d404.insert( f0= 'sx12101', f1= '(12101)404')
    db.d404.insert( f0= 'hh12102', f1= '(12102)ERROR')
    db.d404.insert( f0= 'pa12103', f1= '(12103)Sorry, but the page you are looking for has note been found. Try checking the URL for an error, then hit the refresh button on your browser or try found something else in our app.')
    db.d404.insert( f0= 'aa12105', f1= '(12105)Dashboard')
    db.d404.insert( f0= 'aa12106', f1= '(12106)Report Problem')
    db.commit()
#
