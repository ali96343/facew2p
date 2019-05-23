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


    indexform0 = SQLFORM(db.dindexform0, _class = 'd-none d-md-inline-block form-inline ml-auto mr-0 mr-md-3 my-2 my-md-0', _id= 'idUnk0' )

    indexform0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    indexform0.element('input[name=f0]')['_class']='form-control'
    indexform0.element('input[name=f0]')['_id']='id48'
    indexform0.custom.submit['_type'] = 'submit'
    indexform0.custom.submit['_class'] = 'btn btn-primary'
    indexform0.custom.submit['_value'] = 'unk_52'
    indexform0.custom.submit['_id'] = 'id50'
    indexform0.custom.submit['_title'] = 'submit indexform0'

    if indexform0.accepts(request,session): 
        response.flash0 = 'submitted indexform0' 
    elif indexform0.errors:
        response.flash0 = '!Errors! indexform0' 
    else: 
        response.flash0 = 'indexform0' 


    return dict( DICT= rows_dict, indexform0= indexform0, )

#@auth.requires_login()
def blank():

    qu= db.dblank.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/blank.html'


    blankform0 = SQLFORM(db.dblankform0, _class = 'd-none d-md-inline-block form-inline ml-auto mr-0 mr-md-3 my-2 my-md-0', _id= 'idUnk0' )

    blankform0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    blankform0.element('input[name=f0]')['_class']='form-control'
    blankform0.element('input[name=f0]')['_id']='id30'
    blankform0.custom.submit['_type'] = 'submit'
    blankform0.custom.submit['_class'] = 'btn btn-primary'
    blankform0.custom.submit['_value'] = 'unk_34'
    blankform0.custom.submit['_id'] = 'id32'
    blankform0.custom.submit['_title'] = 'submit blankform0'

    if blankform0.accepts(request,session): 
        response.flash0 = 'submitted blankform0' 
    elif blankform0.errors:
        response.flash0 = '!Errors! blankform0' 
    else: 
        response.flash0 = 'blankform0' 


    return dict( DICT= rows_dict, blankform0= blankform0, )

#@auth.requires_login()
def login():

    qu= db.dlogin.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/login.html'


    loginform0 = SQLFORM(db.dloginform0, _class = 'classUnk0', _id= 'idUnk0' )

    loginform0.element('input[name=f0]')['_placeholder']='f0 Email address'
    loginform0.element('input[name=f0]')['_id']='inputEmail'
    loginform0.element('input[name=f0]')['_class']='form-control'
    loginform0.element('input[name=f1]')['_placeholder']='f1 Password'
    loginform0.element('input[name=f1]')['_id']='inputPassword'
    loginform0.element('input[name=f1]')['_class']='form-control'
    loginform0.element('input[name=f2]')['_placeholder']='f2 place_26'
    loginform0.element('input[name=f2]')['_id']='id23'
    loginform0.element('input[name=f2]')['_value']='remember-me'
    loginform0.custom.submit['_class'] = 'btn btn-primary btn-block'
    loginform0.custom.submit['_id'] = 'id27'
    loginform0.custom.submit['_title'] = 'submit loginform0'

    if loginform0.accepts(request,session): 
        response.flash0 = 'submitted loginform0' 
    elif loginform0.errors:
        response.flash0 = '!Errors! loginform0' 
    else: 
        response.flash0 = 'loginform0' 


    return dict( DICT= rows_dict, loginform0= loginform0, )

#@auth.requires_login()
def register():

    qu= db.dregister.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/register.html'


    registerform0 = SQLFORM(db.dregisterform0, _class = 'classUnk0', _id= 'idUnk0' )

    registerform0.element('input[name=f0]')['_placeholder']='f0 First name'
    registerform0.element('input[name=f0]')['_id']='firstName'
    registerform0.element('input[name=f0]')['_class']='form-control'
    registerform0.element('input[name=f1]')['_placeholder']='f1 Last name'
    registerform0.element('input[name=f1]')['_id']='lastName'
    registerform0.element('input[name=f1]')['_class']='form-control'
    registerform0.element('input[name=f2]')['_placeholder']='f2 Email address'
    registerform0.element('input[name=f2]')['_id']='inputEmail'
    registerform0.element('input[name=f2]')['_class']='form-control'
    registerform0.element('input[name=f3]')['_placeholder']='f3 Password'
    registerform0.element('input[name=f3]')['_id']='inputPassword'
    registerform0.element('input[name=f3]')['_class']='form-control'
    registerform0.element('input[name=f4]')['_placeholder']='f4 Confirm password'
    registerform0.element('input[name=f4]')['_id']='confirmPassword'
    registerform0.element('input[name=f4]')['_class']='form-control'
    registerform0.custom.submit['_class'] = 'btn btn-primary btn-block'
    registerform0.custom.submit['_id'] = 'id10'
    registerform0.custom.submit['_title'] = 'submit registerform0'

    if registerform0.accepts(request,session): 
        response.flash0 = 'submitted registerform0' 
    elif registerform0.errors:
        response.flash0 = '!Errors! registerform0' 
    else: 
        response.flash0 = 'registerform0' 


    return dict( DICT= rows_dict, registerform0= registerform0, )

#@auth.requires_login()
def tables():

    qu= db.dtables.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/tables.html'


    tablesform0 = SQLFORM(db.dtablesform0, _class = 'd-none d-md-inline-block form-inline ml-auto mr-0 mr-md-3 my-2 my-md-0', _id= 'idUnk0' )

    tablesform0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    tablesform0.element('input[name=f0]')['_class']='form-control'
    tablesform0.element('input[name=f0]')['_id']='id13'
    tablesform0.custom.submit['_type'] = 'submit'
    tablesform0.custom.submit['_class'] = 'btn btn-primary'
    tablesform0.custom.submit['_value'] = 'unk_17'
    tablesform0.custom.submit['_id'] = 'id15'
    tablesform0.custom.submit['_title'] = 'submit tablesform0'

    if tablesform0.accepts(request,session): 
        response.flash0 = 'submitted tablesform0' 
    elif tablesform0.errors:
        response.flash0 = '!Errors! tablesform0' 
    else: 
        response.flash0 = 'tablesform0' 


    return dict( DICT= rows_dict, tablesform0= tablesform0, )

#@auth.requires_login()
def X404():

    qu= db.d404.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/404.html'


    X404form0 = SQLFORM(db.dX404form0, _class = 'd-none d-md-inline-block form-inline ml-auto mr-0 mr-md-3 my-2 my-md-0', _id= 'idUnk0' )

    X404form0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    X404form0.element('input[name=f0]')['_class']='form-control'
    X404form0.element('input[name=f0]')['_id']='id36'
    X404form0.custom.submit['_type'] = 'submit'
    X404form0.custom.submit['_class'] = 'btn btn-primary'
    X404form0.custom.submit['_value'] = 'unk_40'
    X404form0.custom.submit['_id'] = 'id38'
    X404form0.custom.submit['_title'] = 'submit X404form0'

    if X404form0.accepts(request,session): 
        response.flash0 = 'submitted X404form0' 
    elif X404form0.errors:
        response.flash0 = '!Errors! X404form0' 
    else: 
        response.flash0 = 'X404form0' 


    return dict( DICT= rows_dict, X404form0= X404form0, )

#@auth.requires_login()
def charts():

    qu= db.dcharts.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/charts.html'


    chartsform0 = SQLFORM(db.dchartsform0, _class = 'd-none d-md-inline-block form-inline ml-auto mr-0 mr-md-3 my-2 my-md-0', _id= 'idUnk0' )

    chartsform0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    chartsform0.element('input[name=f0]')['_class']='form-control'
    chartsform0.element('input[name=f0]')['_id']='id42'
    chartsform0.custom.submit['_type'] = 'submit'
    chartsform0.custom.submit['_class'] = 'btn btn-primary'
    chartsform0.custom.submit['_value'] = 'unk_46'
    chartsform0.custom.submit['_id'] = 'id44'
    chartsform0.custom.submit['_title'] = 'submit chartsform0'

    if chartsform0.accepts(request,session): 
        response.flash0 = 'submitted chartsform0' 
    elif chartsform0.errors:
        response.flash0 = '!Errors! chartsform0' 
    else: 
        response.flash0 = 'chartsform0' 


    return dict( DICT= rows_dict, chartsform0= chartsform0, )

#@auth.requires_login()
def forgot_password():

    qu= db.dforgot0password.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/forgot-password.html'


    forgot_passwordform0 = SQLFORM(db.dforgot_passwordform0, _class = 'classUnk0', _id= 'idUnk0' )

    forgot_passwordform0.element('input[name=f0]')['_placeholder']='f0 Enter email address'
    forgot_passwordform0.element('input[name=f0]')['_id']='inputEmail'
    forgot_passwordform0.element('input[name=f0]')['_class']='form-control'
    forgot_passwordform0.custom.submit['_class'] = 'btn btn-primary btn-block'
    forgot_passwordform0.custom.submit['_id'] = 'id56'
    forgot_passwordform0.custom.submit['_title'] = 'submit forgot_passwordform0'

    if forgot_passwordform0.accepts(request,session): 
        response.flash0 = 'submitted forgot_passwordform0' 
    elif forgot_passwordform0.errors:
        response.flash0 = '!Errors! forgot_passwordform0' 
    else: 
        response.flash0 = 'forgot_passwordform0' 


    return dict( DICT= rows_dict, forgot_passwordform0= forgot_passwordform0, )