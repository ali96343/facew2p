

@auth.requires_login()
def mygrid(tnm):
   return SQLFORM.grid(db[tnm], deletable= False, user_signature=False,  buttons_placement = 'left', showbuttontext=False, csv=False )
# 

@auth.requires_login()
def search_site():
    import os
    form = SQLFORM.factory(
       Field('search', label='search for unique text ( or number label) from screen', requires=IS_NOT_EMPTY(),  ),
       Field('replace', 'text', label='replace with new text', requires=IS_NOT_EMPTY(), length= 1000, ),
       )
    if form.process( keepvalues = True  ).accepted: 
        search  = form.vars.search
        replace  = form.vars.replace
        replace=replace.strip()
        for table in db.tables():
             if any (['auth_' in table, 'form' in table,  not 'f1' in db[table].fields]) :
                     continue
             qu= db[table].f1.contains(search)
             rows = db(qu).select()
             if rows:
               if len(rows) == 1:
                 row = db(qu).select().first()
                 if row:
                    #session.flash = 'found!! %s' % row.f1
                    savef1= row.f1
                    db(db[table].id == row.id).update( f1= replace, f2= savef1  )
                    response.flash = 'replaced, found == 1!'
                    break
               else:
                    response.flash = 'do not replaced, found > 1!'
                    break
    elif form.errors:
        response.flash = 'Please correct the error(s).'
    else: 
        response.flash = 'Insert data please - no fields can be empty.' 
    return form


#https://stackoverflow.com/questions/37806801/can-not-post-data-via-ajax-to-web2py-rest-api-possible-cors-issue/37859336
#url_name='https://sun.minfindnr.ru/ji15/default/api/t0_tables.json'
#url_name='https://sun.minfindnr.ru/ji15/default/api/patterns.json'

@auth.requires_login()
@request.restful()
def api():
    from gluon.serializers import json
    response.view = 'generic.' + request.extension
    def GET(*args,**vars):
         patterns = 'auto'
         parser = db.parse_as_rest(patterns,args,vars)
         if parser.status == 200:
            return dict(content=parser.response)
         else:
            raise HTTP(parser.status,parser.error)
    def POST(table_name,**vars):
        #return db[table_name].validate_and_insert(**vars)
        #data = gluon.contrib.simplejson.loads(request.body.read())
        return json(db[table_name].validate_and_insert(**vars))
        return dict()
    def PUT(table_name,record_id,**vars):
        return db(db[table_name]._id==record_id).update(**vars)
    def DELETE(table_name,record_id):
        return db(db[table_name]._id==record_id).delete()
    def OPTIONS(*args,**vars):
        print ( 'OPTION called') 
        return True
    return dict(GET=GET,POST=POST,PUT=PUT,DELETE=DELETE,OPTIONS=OPTIONS)


@auth.requires_login()
def index():
    response.view = 'myadd/index.html'
    return dict(form=search_site())



@auth.requires_login()
def review():
    db.dreview.f0.writable = True
    response.view = 'myadd/review.html'
    return dict(grid= mygrid('dreview'))
#


@auth.requires_login()
def single_blog():
    db.dsingle0blog.f0.writable = True
    response.view = 'myadd/single-blog.html'
    return dict(grid= mygrid('dsingle0blog'))
#


@auth.requires_login()
def contact():
    db.dcontact.f0.writable = True
    response.view = 'myadd/contact.html'
    return dict(grid= mygrid('dcontact'))
#


@auth.requires_login()
def categories():
    db.dcategories.f0.writable = True
    response.view = 'myadd/categories.html'
    return dict(grid= mygrid('dcategories'))
#


@auth.requires_login()
def table_index1():
    db.dindex.f0.writable = True
    response.view = 'myadd/table_index1.html'
    return dict(grid= mygrid('dindex'))
#


@auth.requires_login()
def community():
    db.dcommunity.f0.writable = True
    response.view = 'myadd/community.html'
    return dict(grid= mygrid('dcommunity'))
#


@auth.requires_login()
def auth_eventctrl():
    response.view = 'myadd/auth_eventctrl.html'
    return dict(grid= mygrid('auth_event'))
#


@auth.requires_login()
def auth_userctrl():
    response.view = 'myadd/auth_userctrl.html'
    return dict(grid= mygrid('auth_user'))
#


@auth.requires_login()
def auth_groupctrl():
    response.view = 'myadd/auth_groupctrl.html'
    return dict(grid= mygrid('auth_group'))
#


@auth.requires_login()
def auth_membershipctrl():
    response.view = 'myadd/auth_membershipctrl.html'
    return dict(grid= mygrid('auth_membership'))
#


@auth.requires_login()
def dcategoriesform0ctrl():
    response.view = 'myadd/dcategoriesform0ctrl.html'
    return dict(grid= mygrid('dcategoriesform0'))
#


@auth.requires_login()
def dcontactform0ctrl():
    response.view = 'myadd/dcontactform0ctrl.html'
    return dict(grid= mygrid('dcontactform0'))
#


@auth.requires_login()
def dsingle_blogform0ctrl():
    response.view = 'myadd/dsingle_blogform0ctrl.html'
    return dict(grid= mygrid('dsingle_blogform0'))
#


@auth.requires_login()
def dsingle_blogform1ctrl():
    response.view = 'myadd/dsingle_blogform1ctrl.html'
    return dict(grid= mygrid('dsingle_blogform1'))
#


@auth.requires_login()
def dcommunityform0ctrl():
    response.view = 'myadd/dcommunityform0ctrl.html'
    return dict(grid= mygrid('dcommunityform0'))
#
