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


    indexform0 = SQLFORM(db.dindexform0, _class = 'd-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search', _id= 'idUnk0' )

    indexform0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    indexform0.custom.submit['_title'] = 'submit indexform0'
    indexform0.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    indexform0.custom.submit['_title'] = 'submit indexform0'
    indexform0.custom.submit['_type'] = 'submit'
    indexform0.custom.submit['_class'] = 'btn btn-primary'
    indexform0.custom.submit['_value'] = 'unk_47'

    if indexform0.accepts(request,session): 
        response.flash0 = 'submitted indexform0' 
    elif indexform0.errors:
        response.flash0 = '!Errors! indexform0' 
    else: 
        response.flash0 = 'indexform0' 



    indexform1 = SQLFORM(db.dindexform1, _class = 'form-inline mr-auto w-100 navbar-search', _id= 'idUnk1' )

    indexform1.element('input[name=f0]')['_placeholder']='f0 Search for...'
    indexform1.custom.submit['_title'] = 'submit indexform1'
    indexform1.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    indexform1.custom.submit['_title'] = 'submit indexform1'
    indexform1.custom.submit['_type'] = 'submit'
    indexform1.custom.submit['_class'] = 'btn btn-primary'
    indexform1.custom.submit['_value'] = 'unk_49'

    if indexform1.accepts(request,session): 
        response.flash1 = 'submitted indexform1' 
    elif indexform1.errors:
        response.flash1 = '!Errors! indexform1' 
    else: 
        response.flash1 = 'indexform1' 


    return dict( DICT= rows_dict, indexform0= indexform0, indexform1= indexform1, )

#@auth.requires_login()
def blank():

    qu= db.dblank.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/blank.html'


    blankform0 = SQLFORM(db.dblankform0, _class = 'd-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search', _id= 'idUnk0' )

    blankform0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    blankform0.custom.submit['_title'] = 'submit blankform0'
    blankform0.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    blankform0.custom.submit['_title'] = 'submit blankform0'
    blankform0.custom.submit['_type'] = 'submit'
    blankform0.custom.submit['_class'] = 'btn btn-primary'
    blankform0.custom.submit['_value'] = 'unk_23'

    if blankform0.accepts(request,session): 
        response.flash0 = 'submitted blankform0' 
    elif blankform0.errors:
        response.flash0 = '!Errors! blankform0' 
    else: 
        response.flash0 = 'blankform0' 



    blankform1 = SQLFORM(db.dblankform1, _class = 'form-inline mr-auto w-100 navbar-search', _id= 'idUnk1' )

    blankform1.element('input[name=f0]')['_placeholder']='f0 Search for...'
    blankform1.custom.submit['_title'] = 'submit blankform1'
    blankform1.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    blankform1.custom.submit['_title'] = 'submit blankform1'
    blankform1.custom.submit['_type'] = 'submit'
    blankform1.custom.submit['_class'] = 'btn btn-primary'
    blankform1.custom.submit['_value'] = 'unk_25'

    if blankform1.accepts(request,session): 
        response.flash1 = 'submitted blankform1' 
    elif blankform1.errors:
        response.flash1 = '!Errors! blankform1' 
    else: 
        response.flash1 = 'blankform1' 


    return dict( DICT= rows_dict, blankform0= blankform0, blankform1= blankform1, )

#@auth.requires_login()
def buttons():

    qu= db.dbuttons.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/buttons.html'


    buttonsform0 = SQLFORM(db.dbuttonsform0, _class = 'd-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search', _id= 'idUnk0' )

    buttonsform0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    buttonsform0.custom.submit['_title'] = 'submit buttonsform0'
    buttonsform0.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    buttonsform0.custom.submit['_title'] = 'submit buttonsform0'
    buttonsform0.custom.submit['_type'] = 'submit'
    buttonsform0.custom.submit['_class'] = 'btn btn-primary'
    buttonsform0.custom.submit['_value'] = 'unk_0'

    if buttonsform0.accepts(request,session): 
        response.flash0 = 'submitted buttonsform0' 
    elif buttonsform0.errors:
        response.flash0 = '!Errors! buttonsform0' 
    else: 
        response.flash0 = 'buttonsform0' 



    buttonsform1 = SQLFORM(db.dbuttonsform1, _class = 'form-inline mr-auto w-100 navbar-search', _id= 'idUnk1' )

    buttonsform1.element('input[name=f0]')['_placeholder']='f0 Search for...'
    buttonsform1.custom.submit['_title'] = 'submit buttonsform1'
    buttonsform1.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    buttonsform1.custom.submit['_title'] = 'submit buttonsform1'
    buttonsform1.custom.submit['_type'] = 'submit'
    buttonsform1.custom.submit['_class'] = 'btn btn-primary'
    buttonsform1.custom.submit['_value'] = 'unk_2'

    if buttonsform1.accepts(request,session): 
        response.flash1 = 'submitted buttonsform1' 
    elif buttonsform1.errors:
        response.flash1 = '!Errors! buttonsform1' 
    else: 
        response.flash1 = 'buttonsform1' 


    return dict( DICT= rows_dict, buttonsform0= buttonsform0, buttonsform1= buttonsform1, )

#@auth.requires_login()
def charts():

    qu= db.dcharts.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/charts.html'


    chartsform0 = SQLFORM(db.dchartsform0, _class = 'd-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search', _id= 'idUnk0' )

    chartsform0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    chartsform0.custom.submit['_title'] = 'submit chartsform0'
    chartsform0.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    chartsform0.custom.submit['_title'] = 'submit chartsform0'
    chartsform0.custom.submit['_type'] = 'submit'
    chartsform0.custom.submit['_class'] = 'btn btn-primary'
    chartsform0.custom.submit['_value'] = 'unk_35'

    if chartsform0.accepts(request,session): 
        response.flash0 = 'submitted chartsform0' 
    elif chartsform0.errors:
        response.flash0 = '!Errors! chartsform0' 
    else: 
        response.flash0 = 'chartsform0' 



    chartsform1 = SQLFORM(db.dchartsform1, _class = 'form-inline mr-auto w-100 navbar-search', _id= 'idUnk1' )

    chartsform1.element('input[name=f0]')['_placeholder']='f0 Search for...'
    chartsform1.custom.submit['_title'] = 'submit chartsform1'
    chartsform1.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    chartsform1.custom.submit['_title'] = 'submit chartsform1'
    chartsform1.custom.submit['_type'] = 'submit'
    chartsform1.custom.submit['_class'] = 'btn btn-primary'
    chartsform1.custom.submit['_value'] = 'unk_37'

    if chartsform1.accepts(request,session): 
        response.flash1 = 'submitted chartsform1' 
    elif chartsform1.errors:
        response.flash1 = '!Errors! chartsform1' 
    else: 
        response.flash1 = 'chartsform1' 


    return dict( DICT= rows_dict, chartsform0= chartsform0, chartsform1= chartsform1, )

#@auth.requires_login()
def utilities_other():

    qu= db.dutilities0other.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/utilities-other.html'


    utilities_otherform0 = SQLFORM(db.dutilities_otherform0, _class = 'd-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search', _id= 'idUnk0' )

    utilities_otherform0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    utilities_otherform0.custom.submit['_title'] = 'submit utilities_otherform0'
    utilities_otherform0.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    utilities_otherform0.custom.submit['_title'] = 'submit utilities_otherform0'
    utilities_otherform0.custom.submit['_type'] = 'submit'
    utilities_otherform0.custom.submit['_class'] = 'btn btn-primary'
    utilities_otherform0.custom.submit['_value'] = 'unk_39'

    if utilities_otherform0.accepts(request,session): 
        response.flash0 = 'submitted utilities_otherform0' 
    elif utilities_otherform0.errors:
        response.flash0 = '!Errors! utilities_otherform0' 
    else: 
        response.flash0 = 'utilities_otherform0' 



    utilities_otherform1 = SQLFORM(db.dutilities_otherform1, _class = 'form-inline mr-auto w-100 navbar-search', _id= 'idUnk1' )

    utilities_otherform1.element('input[name=f0]')['_placeholder']='f0 Search for...'
    utilities_otherform1.custom.submit['_title'] = 'submit utilities_otherform1'
    utilities_otherform1.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    utilities_otherform1.custom.submit['_title'] = 'submit utilities_otherform1'
    utilities_otherform1.custom.submit['_type'] = 'submit'
    utilities_otherform1.custom.submit['_class'] = 'btn btn-primary'
    utilities_otherform1.custom.submit['_value'] = 'unk_41'

    if utilities_otherform1.accepts(request,session): 
        response.flash1 = 'submitted utilities_otherform1' 
    elif utilities_otherform1.errors:
        response.flash1 = '!Errors! utilities_otherform1' 
    else: 
        response.flash1 = 'utilities_otherform1' 


    return dict( DICT= rows_dict, utilities_otherform0= utilities_otherform0, utilities_otherform1= utilities_otherform1, )

#@auth.requires_login()
def utilities_animation():

    qu= db.dutilities0animation.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/utilities-animation.html'


    utilities_animationform0 = SQLFORM(db.dutilities_animationform0, _class = 'd-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search', _id= 'idUnk0' )

    utilities_animationform0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    utilities_animationform0.custom.submit['_title'] = 'submit utilities_animationform0'
    utilities_animationform0.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    utilities_animationform0.custom.submit['_title'] = 'submit utilities_animationform0'
    utilities_animationform0.custom.submit['_type'] = 'submit'
    utilities_animationform0.custom.submit['_class'] = 'btn btn-primary'
    utilities_animationform0.custom.submit['_value'] = 'unk_27'

    if utilities_animationform0.accepts(request,session): 
        response.flash0 = 'submitted utilities_animationform0' 
    elif utilities_animationform0.errors:
        response.flash0 = '!Errors! utilities_animationform0' 
    else: 
        response.flash0 = 'utilities_animationform0' 



    utilities_animationform1 = SQLFORM(db.dutilities_animationform1, _class = 'form-inline mr-auto w-100 navbar-search', _id= 'idUnk1' )

    utilities_animationform1.element('input[name=f0]')['_placeholder']='f0 Search for...'
    utilities_animationform1.custom.submit['_title'] = 'submit utilities_animationform1'
    utilities_animationform1.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    utilities_animationform1.custom.submit['_title'] = 'submit utilities_animationform1'
    utilities_animationform1.custom.submit['_type'] = 'submit'
    utilities_animationform1.custom.submit['_class'] = 'btn btn-primary'
    utilities_animationform1.custom.submit['_value'] = 'unk_29'

    if utilities_animationform1.accepts(request,session): 
        response.flash1 = 'submitted utilities_animationform1' 
    elif utilities_animationform1.errors:
        response.flash1 = '!Errors! utilities_animationform1' 
    else: 
        response.flash1 = 'utilities_animationform1' 


    return dict( DICT= rows_dict, utilities_animationform0= utilities_animationform0, utilities_animationform1= utilities_animationform1, )

#@auth.requires_login()
def utilities_border():

    qu= db.dutilities0border.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/utilities-border.html'


    utilities_borderform0 = SQLFORM(db.dutilities_borderform0, _class = 'd-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search', _id= 'idUnk0' )

    utilities_borderform0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    utilities_borderform0.custom.submit['_title'] = 'submit utilities_borderform0'
    utilities_borderform0.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    utilities_borderform0.custom.submit['_title'] = 'submit utilities_borderform0'
    utilities_borderform0.custom.submit['_type'] = 'submit'
    utilities_borderform0.custom.submit['_class'] = 'btn btn-primary'
    utilities_borderform0.custom.submit['_value'] = 'unk_8'

    if utilities_borderform0.accepts(request,session): 
        response.flash0 = 'submitted utilities_borderform0' 
    elif utilities_borderform0.errors:
        response.flash0 = '!Errors! utilities_borderform0' 
    else: 
        response.flash0 = 'utilities_borderform0' 



    utilities_borderform1 = SQLFORM(db.dutilities_borderform1, _class = 'form-inline mr-auto w-100 navbar-search', _id= 'idUnk1' )

    utilities_borderform1.element('input[name=f0]')['_placeholder']='f0 Search for...'
    utilities_borderform1.custom.submit['_title'] = 'submit utilities_borderform1'
    utilities_borderform1.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    utilities_borderform1.custom.submit['_title'] = 'submit utilities_borderform1'
    utilities_borderform1.custom.submit['_type'] = 'submit'
    utilities_borderform1.custom.submit['_class'] = 'btn btn-primary'
    utilities_borderform1.custom.submit['_value'] = 'unk_10'

    if utilities_borderform1.accepts(request,session): 
        response.flash1 = 'submitted utilities_borderform1' 
    elif utilities_borderform1.errors:
        response.flash1 = '!Errors! utilities_borderform1' 
    else: 
        response.flash1 = 'utilities_borderform1' 


    return dict( DICT= rows_dict, utilities_borderform0= utilities_borderform0, utilities_borderform1= utilities_borderform1, )

#@auth.requires_login()
def login():

    qu= db.dlogin.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/login.html'


    loginform0 = SQLFORM(db.dloginform0, _class = 'user', _id= 'idUnk0' )

    loginform0.element('input[name=f0]')['_placeholder']='f0 Enter Email Address...'
    loginform0.custom.submit['_title'] = 'submit loginform0'
    loginform0.element('input[name=f0]')['_id']='exampleInputEmail'
    loginform0.custom.submit['_title'] = 'submit loginform0'
    loginform0.element('input[name=f0]')['_class']='form-control form-control-user'
    loginform0.custom.submit['_title'] = 'submit loginform0'
    loginform0.element('input[name=f1]')['_placeholder']='f1 Password'
    loginform0.custom.submit['_title'] = 'submit loginform0'
    loginform0.element('input[name=f1]')['_id']='exampleInputPassword'
    loginform0.custom.submit['_title'] = 'submit loginform0'
    loginform0.element('input[name=f1]')['_class']='form-control form-control-user'
    loginform0.custom.submit['_title'] = 'submit loginform0'
    loginform0.element('input[name=f2]')['_placeholder']='f2 place_19'
    loginform0.custom.submit['_title'] = 'submit loginform0'
    loginform0.element('input[name=f2]')['_id']='customCheck'
    loginform0.custom.submit['_title'] = 'submit loginform0'
    loginform0.element('input[name=f2]')['_class']='custom-control-input'
    loginform0.custom.submit['_title'] = 'submit loginform0'
    loginform0.custom.submit['_class'] = 'btn btn-primary btn-user btn-block'
    loginform0.custom.submit['_class'] = 'btn btn-google btn-user btn-block'
    loginform0.custom.submit['_class'] = 'btn btn-facebook btn-user btn-block'

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


    registerform0 = SQLFORM(db.dregisterform0, _class = 'user', _id= 'idUnk0' )

    registerform0.element('input[name=f0]')['_placeholder']='f0 First Name'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.element('input[name=f0]')['_id']='exampleFirstName'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.element('input[name=f0]')['_class']='form-control form-control-user'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.element('input[name=f1]')['_placeholder']='f1 Last Name'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.element('input[name=f1]')['_id']='exampleLastName'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.element('input[name=f1]')['_class']='form-control form-control-user'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.element('input[name=f2]')['_placeholder']='f2 Email Address'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.element('input[name=f2]')['_id']='exampleInputEmail'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.element('input[name=f2]')['_class']='form-control form-control-user'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.element('input[name=f3]')['_placeholder']='f3 Password'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.element('input[name=f3]')['_id']='exampleInputPassword'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.element('input[name=f3]')['_class']='form-control form-control-user'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.element('input[name=f4]')['_placeholder']='f4 Repeat Password'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.element('input[name=f4]')['_id']='exampleRepeatPassword'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.element('input[name=f4]')['_class']='form-control form-control-user'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.custom.submit['_class'] = 'btn btn-primary btn-user btn-block'
    registerform0.custom.submit['_class'] = 'btn btn-google btn-user btn-block'
    registerform0.custom.submit['_class'] = 'btn btn-facebook btn-user btn-block'

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


    tablesform0 = SQLFORM(db.dtablesform0, _class = 'd-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search', _id= 'idUnk0' )

    tablesform0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    tablesform0.custom.submit['_title'] = 'submit tablesform0'
    tablesform0.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    tablesform0.custom.submit['_title'] = 'submit tablesform0'
    tablesform0.custom.submit['_type'] = 'submit'
    tablesform0.custom.submit['_class'] = 'btn btn-primary'
    tablesform0.custom.submit['_value'] = 'unk_15'

    if tablesform0.accepts(request,session): 
        response.flash0 = 'submitted tablesform0' 
    elif tablesform0.errors:
        response.flash0 = '!Errors! tablesform0' 
    else: 
        response.flash0 = 'tablesform0' 



    tablesform1 = SQLFORM(db.dtablesform1, _class = 'form-inline mr-auto w-100 navbar-search', _id= 'idUnk1' )

    tablesform1.element('input[name=f0]')['_placeholder']='f0 Search for...'
    tablesform1.custom.submit['_title'] = 'submit tablesform1'
    tablesform1.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    tablesform1.custom.submit['_title'] = 'submit tablesform1'
    tablesform1.custom.submit['_type'] = 'submit'
    tablesform1.custom.submit['_class'] = 'btn btn-primary'
    tablesform1.custom.submit['_value'] = 'unk_17'

    if tablesform1.accepts(request,session): 
        response.flash1 = 'submitted tablesform1' 
    elif tablesform1.errors:
        response.flash1 = '!Errors! tablesform1' 
    else: 
        response.flash1 = 'tablesform1' 


    return dict( DICT= rows_dict, tablesform0= tablesform0, tablesform1= tablesform1, )

#@auth.requires_login()
def X404():

    qu= db.d404.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/404.html'


    X404form0 = SQLFORM(db.dX404form0, _class = 'd-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search', _id= 'idUnk0' )

    X404form0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    X404form0.custom.submit['_title'] = 'submit X404form0'
    X404form0.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    X404form0.custom.submit['_title'] = 'submit X404form0'
    X404form0.custom.submit['_type'] = 'submit'
    X404form0.custom.submit['_class'] = 'btn btn-primary'
    X404form0.custom.submit['_value'] = 'unk_31'

    if X404form0.accepts(request,session): 
        response.flash0 = 'submitted X404form0' 
    elif X404form0.errors:
        response.flash0 = '!Errors! X404form0' 
    else: 
        response.flash0 = 'X404form0' 



    X404form1 = SQLFORM(db.dX404form1, _class = 'form-inline mr-auto w-100 navbar-search', _id= 'idUnk1' )

    X404form1.element('input[name=f0]')['_placeholder']='f0 Search for...'
    X404form1.custom.submit['_title'] = 'submit X404form1'
    X404form1.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    X404form1.custom.submit['_title'] = 'submit X404form1'
    X404form1.custom.submit['_type'] = 'submit'
    X404form1.custom.submit['_class'] = 'btn btn-primary'
    X404form1.custom.submit['_value'] = 'unk_33'

    if X404form1.accepts(request,session): 
        response.flash1 = 'submitted X404form1' 
    elif X404form1.errors:
        response.flash1 = '!Errors! X404form1' 
    else: 
        response.flash1 = 'X404form1' 


    return dict( DICT= rows_dict, X404form0= X404form0, X404form1= X404form1, )

#@auth.requires_login()
def utilities_color():

    qu= db.dutilities0color.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/utilities-color.html'


    utilities_colorform0 = SQLFORM(db.dutilities_colorform0, _class = 'd-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search', _id= 'idUnk0' )

    utilities_colorform0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    utilities_colorform0.custom.submit['_title'] = 'submit utilities_colorform0'
    utilities_colorform0.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    utilities_colorform0.custom.submit['_title'] = 'submit utilities_colorform0'
    utilities_colorform0.custom.submit['_type'] = 'submit'
    utilities_colorform0.custom.submit['_class'] = 'btn btn-primary'
    utilities_colorform0.custom.submit['_value'] = 'unk_4'

    if utilities_colorform0.accepts(request,session): 
        response.flash0 = 'submitted utilities_colorform0' 
    elif utilities_colorform0.errors:
        response.flash0 = '!Errors! utilities_colorform0' 
    else: 
        response.flash0 = 'utilities_colorform0' 



    utilities_colorform1 = SQLFORM(db.dutilities_colorform1, _class = 'form-inline mr-auto w-100 navbar-search', _id= 'idUnk1' )

    utilities_colorform1.element('input[name=f0]')['_placeholder']='f0 Search for...'
    utilities_colorform1.custom.submit['_title'] = 'submit utilities_colorform1'
    utilities_colorform1.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    utilities_colorform1.custom.submit['_title'] = 'submit utilities_colorform1'
    utilities_colorform1.custom.submit['_type'] = 'submit'
    utilities_colorform1.custom.submit['_class'] = 'btn btn-primary'
    utilities_colorform1.custom.submit['_value'] = 'unk_6'

    if utilities_colorform1.accepts(request,session): 
        response.flash1 = 'submitted utilities_colorform1' 
    elif utilities_colorform1.errors:
        response.flash1 = '!Errors! utilities_colorform1' 
    else: 
        response.flash1 = 'utilities_colorform1' 


    return dict( DICT= rows_dict, utilities_colorform0= utilities_colorform0, utilities_colorform1= utilities_colorform1, )

#@auth.requires_login()
def forgot_password():

    qu= db.dforgot0password.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/forgot-password.html'


    forgot_passwordform0 = SQLFORM(db.dforgot_passwordform0, _class = 'user', _id= 'idUnk0' )

    forgot_passwordform0.element('input[name=f0]')['_placeholder']='f0 Enter Email Address...'
    forgot_passwordform0.custom.submit['_title'] = 'submit forgot_passwordform0'
    forgot_passwordform0.element('input[name=f0]')['_id']='exampleInputEmail'
    forgot_passwordform0.custom.submit['_title'] = 'submit forgot_passwordform0'
    forgot_passwordform0.element('input[name=f0]')['_class']='form-control form-control-user'
    forgot_passwordform0.custom.submit['_title'] = 'submit forgot_passwordform0'
    forgot_passwordform0.custom.submit['_class'] = 'btn btn-primary btn-user btn-block'

    if forgot_passwordform0.accepts(request,session): 
        response.flash0 = 'submitted forgot_passwordform0' 
    elif forgot_passwordform0.errors:
        response.flash0 = '!Errors! forgot_passwordform0' 
    else: 
        response.flash0 = 'forgot_passwordform0' 


    return dict( DICT= rows_dict, forgot_passwordform0= forgot_passwordform0, )

#@auth.requires_login()
def cards():

    qu= db.dcards.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/cards.html'


    cardsform0 = SQLFORM(db.dcardsform0, _class = 'd-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search', _id= 'idUnk0' )

    cardsform0.element('input[name=f0]')['_placeholder']='f0 Search for...'
    cardsform0.custom.submit['_title'] = 'submit cardsform0'
    cardsform0.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    cardsform0.custom.submit['_title'] = 'submit cardsform0'
    cardsform0.custom.submit['_type'] = 'submit'
    cardsform0.custom.submit['_class'] = 'btn btn-primary'
    cardsform0.custom.submit['_value'] = 'unk_43'

    if cardsform0.accepts(request,session): 
        response.flash0 = 'submitted cardsform0' 
    elif cardsform0.errors:
        response.flash0 = '!Errors! cardsform0' 
    else: 
        response.flash0 = 'cardsform0' 



    cardsform1 = SQLFORM(db.dcardsform1, _class = 'form-inline mr-auto w-100 navbar-search', _id= 'idUnk1' )

    cardsform1.element('input[name=f0]')['_placeholder']='f0 Search for...'
    cardsform1.custom.submit['_title'] = 'submit cardsform1'
    cardsform1.element('input[name=f0]')['_class']='form-control bg-light border-0 small'
    cardsform1.custom.submit['_title'] = 'submit cardsform1'
    cardsform1.custom.submit['_type'] = 'submit'
    cardsform1.custom.submit['_class'] = 'btn btn-primary'
    cardsform1.custom.submit['_value'] = 'unk_45'

    if cardsform1.accepts(request,session): 
        response.flash1 = 'submitted cardsform1' 
    elif cardsform1.errors:
        response.flash1 = '!Errors! cardsform1' 
    else: 
        response.flash1 = 'cardsform1' 


    return dict( DICT= rows_dict, cardsform0= cardsform0, cardsform1= cardsform1, )