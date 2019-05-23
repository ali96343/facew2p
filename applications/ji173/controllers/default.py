# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()




#@auth.requires_login()
def index():

    qu= db.dindex.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def review():

    qu= db.dreview.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/review.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def categories():

    qu= db.dcategories.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/categories.html'


    categoriesform0 = SQLFORM(db.dcategoriesform0, _class = 'search-widget', _id= 'idUnk0' )

    categoriesform0.element('input[name=f0]')['_placeholder']='f0 Search'
    categoriesform0.element('input[name=f0]')['_id']='id20'
    categoriesform0.custom.submit['_type'] = 'submit'
    categoriesform0.custom.submit['_id'] = 'id22'
    categoriesform0.custom.submit['_value'] = 'unk_24'
    categoriesform0.custom.submit['_title'] = 'submit categoriesform0'

    if categoriesform0.accepts(request,session): 
        response.flash0 = 'submitted categoriesform0' 
    elif categoriesform0.errors:
        response.flash0 = '!Errors! categoriesform0' 
    else: 
        response.flash0 = 'categoriesform0' 


    return dict( DICT= rows_dict, categoriesform0= categoriesform0, )

#@auth.requires_login()
def contact():

    qu= db.dcontact.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/contact.html'


    contactform0 = SQLFORM(db.dcontactform0, _class = 'comment-form', _id= 'idUnk0' )

    contactform0.element('input[name=f0]')['_placeholder']='f0 Name'
    contactform0.element('input[name=f0]')['_id']='id26'
    contactform0.element('input[name=f1]')['_placeholder']='f1 Email'
    contactform0.element('input[name=f1]')['_id']='id28'
    contactform0.element('input[name=f2]')['_placeholder']='f2 Subject'
    contactform0.element('input[name=f2]')['_id']='id30'
    contactform0.element('textarea[name=f3]')['_placeholder']='f3 Message'
    contactform0.element('textarea[name=f3]')['_id']='id32'
    contactform0.custom.submit['_type'] = 'submit'
    contactform0.custom.submit['_class'] = 'site-btn btn-sm'
    contactform0.custom.submit['_value'] = 'Send'
    contactform0.custom.submit['_id'] = 'id34'
    contactform0.custom.submit['_title'] = 'submit contactform0'

    if contactform0.accepts(request,session): 
        response.flash0 = 'submitted contactform0' 
    elif contactform0.errors:
        response.flash0 = '!Errors! contactform0' 
    else: 
        response.flash0 = 'contactform0' 


    return dict( DICT= rows_dict, contactform0= contactform0, )

#@auth.requires_login()
def single_blog():

    qu= db.dsingle0blog.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/single-blog.html'


    single_blogform0 = SQLFORM(db.dsingle_blogform0, _class = 'comment-form', _id= 'idUnk0' )

    single_blogform0.element('input[name=f0]')['_placeholder']='f0 Name'
    single_blogform0.element('input[name=f0]')['_id']='id0'
    single_blogform0.element('input[name=f1]')['_placeholder']='f1 Email'
    single_blogform0.element('input[name=f1]')['_id']='id2'
    single_blogform0.element('input[name=f2]')['_placeholder']='f2 Subject'
    single_blogform0.element('input[name=f2]')['_id']='id4'
    single_blogform0.element('textarea[name=f3]')['_placeholder']='f3 Message'
    single_blogform0.element('textarea[name=f3]')['_id']='id6'
    single_blogform0.custom.submit['_type'] = 'submit'
    single_blogform0.custom.submit['_class'] = 'site-btn btn-sm'
    single_blogform0.custom.submit['_value'] = 'Send'
    single_blogform0.custom.submit['_id'] = 'id8'
    single_blogform0.custom.submit['_title'] = 'submit single_blogform0'

    if single_blogform0.accepts(request,session): 
        response.flash0 = 'submitted single_blogform0' 
    elif single_blogform0.errors:
        response.flash0 = '!Errors! single_blogform0' 
    else: 
        response.flash0 = 'single_blogform0' 



    single_blogform1 = SQLFORM(db.dsingle_blogform1, _class = 'search-widget', _id= 'idUnk1' )

    single_blogform1.element('input[name=f0]')['_placeholder']='f0 Search'
    single_blogform1.element('input[name=f0]')['_id']='id11'
    single_blogform1.custom.submit['_type'] = 'submit'
    single_blogform1.custom.submit['_id'] = 'id13'
    single_blogform1.custom.submit['_value'] = 'unk_15'
    single_blogform1.custom.submit['_title'] = 'submit single_blogform1'

    if single_blogform1.accepts(request,session): 
        response.flash1 = 'submitted single_blogform1' 
    elif single_blogform1.errors:
        response.flash1 = '!Errors! single_blogform1' 
    else: 
        response.flash1 = 'single_blogform1' 


    return dict( DICT= rows_dict, single_blogform0= single_blogform0, single_blogform1= single_blogform1, )

#@auth.requires_login()
def community():

    qu= db.dcommunity.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/community.html'


    communityform0 = SQLFORM(db.dcommunityform0, _class = 'community-filter', _id= 'idUnk0' )

    communityform0.custom.submit['_type'] = 'submit'
    communityform0.custom.submit['_id'] = 'unk-id'
    communityform0.custom.submit['_value'] = 'submit select'
    communityform0.custom.submit['_class'] = 'unk-class'
    communityform0.custom.submit['_title'] = 'submit communityform0'

    if communityform0.accepts(request,session): 
        response.flash0 = 'submitted communityform0' 
    elif communityform0.errors:
        response.flash0 = '!Errors! communityform0' 
    else: 
        response.flash0 = 'communityform0' 


    return dict( DICT= rows_dict, communityform0= communityform0, )