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
def blog():

    qu= db.dblog.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/blog.html'


    blogform0 = SQLFORM(db.dblogform0, _class = 'classUnk0', _id= 'idUnk0' )

    blogform0.element('input[name=f0]')['_placeholder']='f0 What are you looking for?'
    blogform0.custom.submit['_title'] = 'submit blogform0'
    blogform0.element('input[name=f0]')['_id']='search'
    blogform0.custom.submit['_title'] = 'submit blogform0'
    blogform0.custom.submit['_type'] = 'submit'
    blogform0.custom.submit['_class'] = 'submit'
    blogform0.custom.submit['_value'] = 'unk_0'

    if blogform0.accepts(request,session): 
        response.flash0 = 'submitted blogform0' 
    elif blogform0.errors:
        response.flash0 = '!Errors! blogform0' 
    else: 
        response.flash0 = 'blogform0' 



    blogform1 = SQLFORM(db.dblogform1, _class = 'search-form', _id= 'idUnk1' )

    blogform1.element('input[name=f0]')['_placeholder']='f0 What are you looking for?'
    blogform1.custom.submit['_title'] = 'submit blogform1'
    blogform1.custom.submit['_type'] = 'submit'
    blogform1.custom.submit['_class'] = 'submit'
    blogform1.custom.submit['_value'] = 'unk_2'

    if blogform1.accepts(request,session): 
        response.flash1 = 'submitted blogform1' 
    elif blogform1.errors:
        response.flash1 = '!Errors! blogform1' 
    else: 
        response.flash1 = 'blogform1' 


    return dict( DICT= rows_dict, blogform0= blogform0, blogform1= blogform1, )

#@auth.requires_login()
def index():

    qu= db.dindex.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index.html'


    indexform0 = SQLFORM(db.dindexform0, _class = 'classUnk0', _id= 'idUnk0' )

    indexform0.element('input[name=f0]')['_placeholder']='f0 What are you looking for?'
    indexform0.custom.submit['_title'] = 'submit indexform0'
    indexform0.element('input[name=f0]')['_id']='search'
    indexform0.custom.submit['_title'] = 'submit indexform0'
    indexform0.custom.submit['_type'] = 'submit'
    indexform0.custom.submit['_class'] = 'submit'
    indexform0.custom.submit['_value'] = 'unk_9'

    if indexform0.accepts(request,session): 
        response.flash0 = 'submitted indexform0' 
    elif indexform0.errors:
        response.flash0 = '!Errors! indexform0' 
    else: 
        response.flash0 = 'indexform0' 



    indexform1 = SQLFORM(db.dindexform1, _class = 'classUnk1', _id= 'idUnk1' )

    indexform1.element('input[name=f0]')['_placeholder']='f0 Type your email address'
    indexform1.custom.submit['_title'] = 'submit indexform1'
    indexform1.element('input[name=f0]')['_id']='email'
    indexform1.custom.submit['_title'] = 'submit indexform1'
    indexform1.custom.submit['_type'] = 'submit'
    indexform1.custom.submit['_class'] = 'submit'
    indexform1.custom.submit['_value'] = 'Subscribe'

    if indexform1.accepts(request,session): 
        response.flash1 = 'submitted indexform1' 
    elif indexform1.errors:
        response.flash1 = '!Errors! indexform1' 
    else: 
        response.flash1 = 'indexform1' 


    return dict( DICT= rows_dict, indexform0= indexform0, indexform1= indexform1, )

#@auth.requires_login()
def post():

    qu= db.dpost.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/post.html'


    postform0 = SQLFORM(db.dpostform0, _class = 'classUnk0', _id= 'idUnk0' )

    postform0.element('input[name=f0]')['_placeholder']='f0 What are you looking for?'
    postform0.custom.submit['_title'] = 'submit postform0'
    postform0.element('input[name=f0]')['_id']='search'
    postform0.custom.submit['_title'] = 'submit postform0'
    postform0.custom.submit['_type'] = 'submit'
    postform0.custom.submit['_class'] = 'submit'
    postform0.custom.submit['_value'] = 'unk_4'

    if postform0.accepts(request,session): 
        response.flash0 = 'submitted postform0' 
    elif postform0.errors:
        response.flash0 = '!Errors! postform0' 
    else: 
        response.flash0 = 'postform0' 



    postform1 = SQLFORM(db.dpostform1, _class = 'commenting-form', _id= 'idUnk1' )

    postform1.element('input[name=f0]')['_placeholder']='f0 Name'
    postform1.custom.submit['_title'] = 'submit postform1'
    postform1.element('input[name=f0]')['_id']='username'
    postform1.custom.submit['_title'] = 'submit postform1'
    postform1.element('input[name=f0]')['_class']='form-control'
    postform1.custom.submit['_title'] = 'submit postform1'
    postform1.element('input[name=f1]')['_placeholder']='f1 Email Address (will not be published)'
    postform1.custom.submit['_title'] = 'submit postform1'
    postform1.element('input[name=f1]')['_id']='useremail'
    postform1.custom.submit['_title'] = 'submit postform1'
    postform1.element('input[name=f1]')['_class']='form-control'
    postform1.custom.submit['_title'] = 'submit postform1'
    postform1.element('textarea[name=f2]')['_placeholder']='f2 Type your comment'
    postform1.custom.submit['_title'] = 'submit postform1'
    postform1.element('textarea[name=f2]')['_id']='usercomment'
    postform1.custom.submit['_title'] = 'submit postform1'
    postform1.element('textarea[name=f2]')['_class']='form-control'
    postform1.custom.submit['_title'] = 'submit postform1'
    postform1.custom.submit['_type'] = 'submit'
    postform1.custom.submit['_class'] = 'btn btn-secondary'
    postform1.custom.submit['_value'] = 'Submit Comment'

    if postform1.accepts(request,session): 
        response.flash1 = 'submitted postform1' 
    elif postform1.errors:
        response.flash1 = '!Errors! postform1' 
    else: 
        response.flash1 = 'postform1' 



    postform2 = SQLFORM(db.dpostform2, _class = 'search-form', _id= 'idUnk2' )

    postform2.element('input[name=f0]')['_placeholder']='f0 What are you looking for?'
    postform2.custom.submit['_title'] = 'submit postform2'
    postform2.custom.submit['_type'] = 'submit'
    postform2.custom.submit['_class'] = 'submit'
    postform2.custom.submit['_value'] = 'unk_7'

    if postform2.accepts(request,session): 
        response.flash2 = 'submitted postform2' 
    elif postform2.errors:
        response.flash2 = '!Errors! postform2' 
    else: 
        response.flash2 = 'postform2' 


    return dict( DICT= rows_dict, postform0= postform0, postform1= postform1, postform2= postform2, )