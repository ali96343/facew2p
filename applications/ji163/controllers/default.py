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
def bgimage():

    qu= db.dbgimage.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/bgimage.html'


    bgimageform0 = SQLFORM(db.dbgimageform0, _class = 'main-search', _id= 'idUnk0' )

    bgimageform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    bgimageform0.element('input[name=f0]')['_class']='form-control'
    bgimageform0.element('input[name=f0]')['_id']='id84'
    bgimageform0.custom.submit['_type'] = 'submit'
    bgimageform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    bgimageform0.custom.submit['_value'] = 'unk_88'
    bgimageform0.custom.submit['_id'] = 'id86'
    bgimageform0.custom.submit['_title'] = 'submit bgimageform0'

    if bgimageform0.accepts(request,session): 
        response.flash0 = 'submitted bgimageform0' 
    elif bgimageform0.errors:
        response.flash0 = '!Errors! bgimageform0' 
    else: 
        response.flash0 = 'bgimageform0' 


    return dict( DICT= rows_dict, bgimageform0= bgimageform0, )

#@auth.requires_login()
def boxed():

    qu= db.dboxed.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/boxed.html'


    boxedform0 = SQLFORM(db.dboxedform0, _class = 'main-search', _id= 'idUnk0' )

    boxedform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    boxedform0.element('input[name=f0]')['_class']='form-control'
    boxedform0.element('input[name=f0]')['_id']='id667'
    boxedform0.custom.submit['_type'] = 'submit'
    boxedform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    boxedform0.custom.submit['_value'] = 'unk_671'
    boxedform0.custom.submit['_id'] = 'id669'
    boxedform0.custom.submit['_title'] = 'submit boxedform0'

    if boxedform0.accepts(request,session): 
        response.flash0 = 'submitted boxedform0' 
    elif boxedform0.errors:
        response.flash0 = '!Errors! boxedform0' 
    else: 
        response.flash0 = 'boxedform0' 


    return dict( DICT= rows_dict, boxedform0= boxedform0, )

#@auth.requires_login()
def button():

    qu= db.dbutton.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/button.html'


    buttonform0 = SQLFORM(db.dbuttonform0, _class = 'main-search', _id= 'idUnk0' )

    buttonform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    buttonform0.element('input[name=f0]')['_class']='form-control'
    buttonform0.element('input[name=f0]')['_id']='id78'
    buttonform0.custom.submit['_type'] = 'submit'
    buttonform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    buttonform0.custom.submit['_value'] = 'unk_82'
    buttonform0.custom.submit['_id'] = 'id80'
    buttonform0.custom.submit['_title'] = 'submit buttonform0'

    if buttonform0.accepts(request,session): 
        response.flash0 = 'submitted buttonform0' 
    elif buttonform0.errors:
        response.flash0 = '!Errors! buttonform0' 
    else: 
        response.flash0 = 'buttonform0' 


    return dict( DICT= rows_dict, buttonform0= buttonform0, )

#@auth.requires_login()
def fixed_header_fixed_mini_sidebar():

    qu= db.dfixed0header0fixed0mini0sidebar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/fixed-header-fixed-mini-sidebar.html'


    fixed_header_fixed_mini_sidebarform0 = SQLFORM(db.dfixed_header_fixed_mini_sidebarform0, _class = 'main-search', _id= 'idUnk0' )

    fixed_header_fixed_mini_sidebarform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    fixed_header_fixed_mini_sidebarform0.element('input[name=f0]')['_class']='form-control'
    fixed_header_fixed_mini_sidebarform0.element('input[name=f0]')['_id']='id633'
    fixed_header_fixed_mini_sidebarform0.custom.submit['_type'] = 'submit'
    fixed_header_fixed_mini_sidebarform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    fixed_header_fixed_mini_sidebarform0.custom.submit['_value'] = 'unk_637'
    fixed_header_fixed_mini_sidebarform0.custom.submit['_id'] = 'id635'
    fixed_header_fixed_mini_sidebarform0.custom.submit['_title'] = 'submit fixed_header_fixed_mini_sidebarform0'

    if fixed_header_fixed_mini_sidebarform0.accepts(request,session): 
        response.flash0 = 'submitted fixed_header_fixed_mini_sidebarform0' 
    elif fixed_header_fixed_mini_sidebarform0.errors:
        response.flash0 = '!Errors! fixed_header_fixed_mini_sidebarform0' 
    else: 
        response.flash0 = 'fixed_header_fixed_mini_sidebarform0' 


    return dict( DICT= rows_dict, fixed_header_fixed_mini_sidebarform0= fixed_header_fixed_mini_sidebarform0, )

#@auth.requires_login()
def X404():

    qu= db.d404.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/404.html'


    X404form0 = SQLFORM(db.dX404form0, _class = 'classUnk0', _id= 'idUnk0' )

    X404form0.element('input[name=f0]')['_placeholder']='f0 search ...'
    X404form0.element('input[name=f0]')['_class']='form-control'
    X404form0.element('input[name=f0]')['_id']='id465'
    X404form0.custom.submit['_type'] = 'submit'
    X404form0.custom.submit['_class'] = 'btn btn-default'
    X404form0.custom.submit['_value'] = 'unk_469'
    X404form0.custom.submit['_id'] = 'id467'
    X404form0.custom.submit['_title'] = 'submit X404form0'

    if X404form0.accepts(request,session): 
        response.flash0 = 'submitted X404form0' 
    elif X404form0.errors:
        response.flash0 = '!Errors! X404form0' 
    else: 
        response.flash0 = 'X404form0' 


    return dict( DICT= rows_dict, X404form0= X404form0, )

#@auth.requires_login()
def no_left_sidebar_main_search():

    qu= db.dno0left0sidebar0main0search.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/no-left-sidebar-main-search.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def dashboard():

    qu= db.ddashboard.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/dashboard.html'


    dashboardform0 = SQLFORM(db.ddashboardform0, _class = 'main-search', _id= 'idUnk0' )

    dashboardform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    dashboardform0.element('input[name=f0]')['_class']='form-control'
    dashboardform0.element('input[name=f0]')['_id']='id18'
    dashboardform0.custom.submit['_type'] = 'submit'
    dashboardform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    dashboardform0.custom.submit['_value'] = 'unk_22'
    dashboardform0.custom.submit['_id'] = 'id20'
    dashboardform0.custom.submit['_title'] = 'submit dashboardform0'

    if dashboardform0.accepts(request,session): 
        response.flash0 = 'submitted dashboardform0' 
    elif dashboardform0.errors:
        response.flash0 = '!Errors! dashboardform0' 
    else: 
        response.flash0 = 'dashboardform0' 


    return dict( DICT= rows_dict, dashboardform0= dashboardform0, )

#@auth.requires_login()
def no_right_sidebar():

    qu= db.dno0right0sidebar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/no-right-sidebar.html'


    no_right_sidebarform0 = SQLFORM(db.dno_right_sidebarform0, _class = 'main-search', _id= 'idUnk0' )

    no_right_sidebarform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    no_right_sidebarform0.element('input[name=f0]')['_class']='form-control'
    no_right_sidebarform0.element('input[name=f0]')['_id']='id24'
    no_right_sidebarform0.custom.submit['_type'] = 'submit'
    no_right_sidebarform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    no_right_sidebarform0.custom.submit['_value'] = 'unk_28'
    no_right_sidebarform0.custom.submit['_id'] = 'id26'
    no_right_sidebarform0.custom.submit['_title'] = 'submit no_right_sidebarform0'

    if no_right_sidebarform0.accepts(request,session): 
        response.flash0 = 'submitted no_right_sidebarform0' 
    elif no_right_sidebarform0.errors:
        response.flash0 = '!Errors! no_right_sidebarform0' 
    else: 
        response.flash0 = 'no_right_sidebarform0' 


    return dict( DICT= rows_dict, no_right_sidebarform0= no_right_sidebarform0, )

#@auth.requires_login()
def form_general():

    qu= db.dform0general.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/form-general.html'


    form_generalform0 = SQLFORM(db.dform_generalform0, _class = 'main-search', _id= 'idUnk0' )

    form_generalform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    form_generalform0.element('input[name=f0]')['_class']='form-control'
    form_generalform0.element('input[name=f0]')['_id']='id138'
    form_generalform0.custom.submit['_type'] = 'submit'
    form_generalform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    form_generalform0.custom.submit['_value'] = 'unk_142'
    form_generalform0.custom.submit['_id'] = 'id140'
    form_generalform0.custom.submit['_title'] = 'submit form_generalform0'

    if form_generalform0.accepts(request,session): 
        response.flash0 = 'submitted form_generalform0' 
    elif form_generalform0.errors:
        response.flash0 = '!Errors! form_generalform0' 
    else: 
        response.flash0 = 'form_generalform0' 



    form_generalform1 = SQLFORM(db.dform_generalform1, _class = 'form-horizontal', _id= 'idUnk1' )

    form_generalform1.element('input[name=f0]')['_placeholder']='f0 Email'
    form_generalform1.element('input[name=f0]')['_id']='text1'
    form_generalform1.element('input[name=f0]')['_class']='form-control'
    form_generalform1.element('input[name=f1]')['_placeholder']='f1 place_148'
    form_generalform1.element('input[name=f1]')['_id']='pass1'
    form_generalform1.element('input[name=f1]')['_class']='form-control'
    form_generalform1.element('input[name=f2]')['_placeholder']='f2 place_151'
    form_generalform1.element('input[name=f2]')['_class']='form-control'
    form_generalform1.element('input[name=f2]')['_value']='read only'
    form_generalform1.element('input[name=f2]')['_id']='id149'
    form_generalform1.element('input[name=f3]')['_placeholder']='f3 place_154'
    form_generalform1.element('input[name=f3]')['_class']='form-control'
    form_generalform1.element('input[name=f3]')['_value']='disabled'
    form_generalform1.element('input[name=f3]')['_id']='id152'
    form_generalform1.element('input[name=f4]')['_placeholder']='f4 placeholder text'
    form_generalform1.element('input[name=f4]')['_id']='text2'
    form_generalform1.element('input[name=f4]')['_class']='form-control'
    form_generalform1.element('input[name=f5]')['_placeholder']='f5 place_159'
    form_generalform1.element('input[name=f5]')['_id']='tags'
    form_generalform1.element('input[name=f5]')['_value']='foo,bar,baz'
    form_generalform1.element('input[name=f5]')['_class']='form-control'
    form_generalform1.element('textarea[name=f6]')['_placeholder']='f6 place_162'
    form_generalform1.element('textarea[name=f6]')['_id']='limiter'
    form_generalform1.element('textarea[name=f6]')['_class']='form-control'
    form_generalform1.element('textarea[name=f7]')['_placeholder']='f7 place_165'
    form_generalform1.element('textarea[name=f7]')['_id']='text4'
    form_generalform1.element('textarea[name=f7]')['_class']='form-control'
    form_generalform1.element('textarea[name=f8]')['_placeholder']='f8 place_168'
    form_generalform1.element('textarea[name=f8]')['_id']='autosize'
    form_generalform1.element('textarea[name=f8]')['_class']='form-control'
    form_generalform1.custom.submit['_type'] = 'submit'
    form_generalform1.custom.submit['_id'] = 'unk-id'
    form_generalform1.custom.submit['_value'] = 'submit input'
    form_generalform1.custom.submit['_class'] = 'unk-class'
    form_generalform1.custom.submit['_title'] = 'submit form_generalform1'

    if form_generalform1.accepts(request,session): 
        response.flash1 = 'submitted form_generalform1' 
    elif form_generalform1.errors:
        response.flash1 = '!Errors! form_generalform1' 
    else: 
        response.flash1 = 'form_generalform1' 



    form_generalform2 = SQLFORM(db.dform_generalform2, _class = 'form-horizontal', _id= 'idUnk2' )

    form_generalform2.element('input[name=f0]')['_placeholder']='f0 place_171'
    form_generalform2.element('input[name=f0]')['_class']='form-control'
    form_generalform2.element('input[name=f0]')['_value']='6'
    form_generalform2.element('input[name=f0]')['_id']='id169'
    form_generalform2.element('input[name=f1]')['_placeholder']='f1 place_174'
    form_generalform2.element('input[name=f1]')['_class']='form-control'
    form_generalform2.element('input[name=f1]')['_value']='2.8'
    form_generalform2.element('input[name=f1]')['_id']='id172'
    form_generalform2.element('input[name=f2]')['_placeholder']='f2 place_177'
    form_generalform2.element('input[name=f2]')['_class']='form-control'
    form_generalform2.element('input[name=f2]')['_value']='16'
    form_generalform2.element('input[name=f2]')['_id']='id175'
    form_generalform2.custom.submit['_type'] = 'submit'
    form_generalform2.custom.submit['_class'] = 'unk-class'
    form_generalform2.custom.submit['_value'] = 'submit input'
    form_generalform2.custom.submit['_id'] = 'unk-id'
    form_generalform2.custom.submit['_title'] = 'submit form_generalform2'

    if form_generalform2.accepts(request,session): 
        response.flash2 = 'submitted form_generalform2' 
    elif form_generalform2.errors:
        response.flash2 = '!Errors! form_generalform2' 
    else: 
        response.flash2 = 'form_generalform2' 



    form_generalform3 = SQLFORM(db.dform_generalform3, _class = 'form-horizontal', _id= 'idUnk3' )

    form_generalform3.element('input[name=f0]')['_placeholder']='f0 place_227'
    form_generalform3.element('input[name=f0]')['_class']='uniform'
    form_generalform3.element('input[name=f0]')['_value']='option1'
    form_generalform3.element('input[name=f0]')['_id']='id224'
    form_generalform3.element('input[name=f1]')['_placeholder']='f1 place_231'
    form_generalform3.element('input[name=f1]')['_class']='uniform'
    form_generalform3.element('input[name=f1]')['_value']='option2'
    form_generalform3.element('input[name=f1]')['_id']='id228'
    form_generalform3.element('input[name=f2]')['_placeholder']='f2 place_235'
    form_generalform3.element('input[name=f2]')['_class']='uniform'
    form_generalform3.element('input[name=f2]')['_value']='option3'
    form_generalform3.element('input[name=f2]')['_id']='id232'
    form_generalform3.element('input[name=f3]')['_placeholder']='f3 place_239'
    form_generalform3.element('input[name=f3]')['_class']='uniform'
    form_generalform3.element('input[name=f3]')['_value']='option2'
    form_generalform3.element('input[name=f3]')['_id']='id236'
    form_generalform3.element('input[name=f8]')['_placeholder']='f8 place_254'
    form_generalform3.element('input[name=f8]')['_class']='make-switch'
    form_generalform3.element('input[name=f8]')['_id']='id252'
    form_generalform3.element('input[name=f9]')['_placeholder']='f9 place_257'
    form_generalform3.element('input[name=f9]')['_class']='make-switch'
    form_generalform3.element('input[name=f9]')['_id']='id255'
    form_generalform3.element('input[name=f10]')['_placeholder']='f10 place_260'
    form_generalform3.element('input[name=f10]')['_class']='make-switch'
    form_generalform3.element('input[name=f10]')['_id']='id258'
    form_generalform3.element('input[name=f11]')['_placeholder']='f11 place_263'
    form_generalform3.element('input[name=f11]')['_class']='make-switch'
    form_generalform3.element('input[name=f11]')['_id']='id261'
    form_generalform3.element('input[name=f12]')['_placeholder']='f12 place_266'
    form_generalform3.element('input[name=f12]')['_class']='make-switch'
    form_generalform3.element('input[name=f12]')['_id']='id264'
    form_generalform3.element('input[name=f13]')['_placeholder']='f13 place_269'
    form_generalform3.element('input[name=f13]')['_class']='make-switch'
    form_generalform3.element('input[name=f13]')['_id']='id267'
    form_generalform3.element('input[name=f14]')['_placeholder']='f14 place_272'
    form_generalform3.element('input[name=f14]')['_class']='make-switch'
    form_generalform3.element('input[name=f14]')['_id']='id270'
    form_generalform3.element('input[name=f15]')['_placeholder']='f15 place_275'
    form_generalform3.element('input[name=f15]')['_class']='make-switch'
    form_generalform3.element('input[name=f15]')['_id']='id273'
    form_generalform3.element('input[name=f16]')['_placeholder']='f16 place_278'
    form_generalform3.element('input[name=f16]')['_class']='make-switch'
    form_generalform3.element('input[name=f16]')['_id']='id276'
    form_generalform3.element('input[name=f17]')['_placeholder']='f17 place_281'
    form_generalform3.element('input[name=f17]')['_class']='make-switch'
    form_generalform3.element('input[name=f17]')['_id']='id279'
    form_generalform3.element('input[name=f18]')['_placeholder']='f18 place_284'
    form_generalform3.element('input[name=f18]')['_class']='make-switch'
    form_generalform3.element('input[name=f18]')['_id']='id282'
    form_generalform3.element('input[name=f19]')['_placeholder']='f19 place_287'
    form_generalform3.element('input[name=f19]')['_class']='make-switch'
    form_generalform3.element('input[name=f19]')['_id']='id285'
    form_generalform3.element('input[name=f20]')['_placeholder']='f20 place_290'
    form_generalform3.element('input[name=f20]')['_class']='make-switch'
    form_generalform3.element('input[name=f20]')['_id']='id288'
    form_generalform3.custom.submit['_type'] = 'submit'
    form_generalform3.custom.submit['_class'] = 'unk-class'
    form_generalform3.custom.submit['_value'] = 'submit checkbox'
    form_generalform3.custom.submit['_id'] = 'unk-id'
    form_generalform3.custom.submit['_title'] = 'submit form_generalform3'

    if form_generalform3.accepts(request,session): 
        response.flash3 = 'submitted form_generalform3' 
    elif form_generalform3.errors:
        response.flash3 = '!Errors! form_generalform3' 
    else: 
        response.flash3 = 'form_generalform3' 



    form_generalform4 = SQLFORM(db.dform_generalform4, _class = 'form-inline', _id= 'validVal' )

    form_generalform4.element('input[name=f0]')['_placeholder']='f0 place_293'
    form_generalform4.element('input[name=f0]')['_class']='form-control autotab'
    form_generalform4.element('input[name=f0]')['_id']='id291'
    form_generalform4.element('input[name=f1]')['_placeholder']='f1 place_296'
    form_generalform4.element('input[name=f1]')['_class']='form-control autotab'
    form_generalform4.element('input[name=f1]')['_id']='id294'
    form_generalform4.element('input[name=f2]')['_placeholder']='f2 place_299'
    form_generalform4.element('input[name=f2]')['_class']='form-control'
    form_generalform4.element('input[name=f2]')['_id']='id297'
    form_generalform4.custom.submit['_type'] = 'submit'
    form_generalform4.custom.submit['_class'] = 'unk-class'
    form_generalform4.custom.submit['_value'] = 'submit input'
    form_generalform4.custom.submit['_id'] = 'unk-id'
    form_generalform4.custom.submit['_title'] = 'submit form_generalform4'

    if form_generalform4.accepts(request,session): 
        response.flash4 = 'submitted form_generalform4' 
    elif form_generalform4.errors:
        response.flash4 = '!Errors! form_generalform4' 
    else: 
        response.flash4 = 'form_generalform4' 



    form_generalform5 = SQLFORM(db.dform_generalform5, _class = 'form-horizontal', _id= 'idUnk5' )

    form_generalform5.element('input[name=f0]')['_placeholder']='f0 place_308'
    form_generalform5.element('input[name=f0]')['_class']='form-control'
    form_generalform5.element('input[name=f0]')['_id']='id306'
    form_generalform5.element('input[name=f1]')['_placeholder']='f1 place_311'
    form_generalform5.element('input[name=f1]')['_class']='form-control'
    form_generalform5.element('input[name=f1]')['_id']='id309'
    form_generalform5.element('input[name=f2]')['_placeholder']='f2 place_314'
    form_generalform5.element('input[name=f2]')['_class']='form-control'
    form_generalform5.element('input[name=f2]')['_id']='id312'
    form_generalform5.element('input[name=f3]')['_placeholder']='f3 place_317'
    form_generalform5.element('input[name=f3]')['_class']='form-control'
    form_generalform5.element('input[name=f3]')['_id']='id315'
    form_generalform5.element('input[name=f4]')['_placeholder']='f4 place_320'
    form_generalform5.element('input[name=f4]')['_class']='form-control'
    form_generalform5.element('input[name=f4]')['_id']='id318'
    form_generalform5.custom.submit['_type'] = 'submit'
    form_generalform5.custom.submit['_class'] = 'unk-class'
    form_generalform5.custom.submit['_value'] = 'submit input'
    form_generalform5.custom.submit['_id'] = 'unk-id'
    form_generalform5.custom.submit['_title'] = 'submit form_generalform5'

    if form_generalform5.accepts(request,session): 
        response.flash5 = 'submitted form_generalform5' 
    elif form_generalform5.errors:
        response.flash5 = '!Errors! form_generalform5' 
    else: 
        response.flash5 = 'form_generalform5' 



    form_generalform6 = SQLFORM(db.dform_generalform6, _class = 'form-horizontal', _id= 'idUnk6' )

    form_generalform6.element('input[name=f0]')['_placeholder']='f0 place_323'
    form_generalform6.element('input[name=f0]')['_id']='cp1'
    form_generalform6.element('input[name=f0]')['_value']='#8fff00'
    form_generalform6.element('input[name=f0]')['_class']='form-control'
    form_generalform6.element('input[name=f1]')['_placeholder']='f1 place_326'
    form_generalform6.element('input[name=f1]')['_id']='cp2'
    form_generalform6.element('input[name=f1]')['_value']='rgb(0,194,255,0.78)'
    form_generalform6.element('input[name=f1]')['_class']='form-control'
    form_generalform6.element('input[name=f2]')['_placeholder']='f2 place_329'
    form_generalform6.element('input[name=f2]')['_id']='cp3'
    form_generalform6.element('input[name=f2]')['_class']='form-control'
    form_generalform6.custom.submit['_id'] = 'cp4'
    form_generalform6.custom.submit['_class'] = 'btn btn-danger'
    form_generalform6.custom.submit['_title'] = 'submit form_generalform6'

    if form_generalform6.accepts(request,session): 
        response.flash6 = 'submitted form_generalform6' 
    elif form_generalform6.errors:
        response.flash6 = '!Errors! form_generalform6' 
    else: 
        response.flash6 = 'form_generalform6' 



    form_generalform7 = SQLFORM(db.dform_generalform7, _class = 'form-horizontal', _id= 'idUnk7' )

    form_generalform7.element('input[name=f0]')['_placeholder']='f0 place_335'
    form_generalform7.element('input[name=f0]')['_id']='dp1'
    form_generalform7.element('input[name=f0]')['_value']='02-16-2012'
    form_generalform7.element('input[name=f0]')['_class']='form-control'
    form_generalform7.element('input[name=f1]')['_placeholder']='f1 place_338'
    form_generalform7.element('input[name=f1]')['_id']='dp2'
    form_generalform7.element('input[name=f1]')['_value']='02/16/12'
    form_generalform7.element('input[name=f1]')['_class']='form-control'
    form_generalform7.element('input[name=f2]')['_placeholder']='f2 place_341'
    form_generalform7.element('input[name=f2]')['_class']='form-control'
    form_generalform7.element('input[name=f2]')['_value']='12-02-2012'
    form_generalform7.element('input[name=f2]')['_id']='id339'
    form_generalform7.element('input[name=f3]')['_placeholder']='f3 place_344'
    form_generalform7.element('input[name=f3]')['_class']='form-control'
    form_generalform7.element('input[name=f3]')['_value']='12-02-2012'
    form_generalform7.element('input[name=f3]')['_id']='id342'
    form_generalform7.element('input[name=f4]')['_placeholder']='f4 place_347'
    form_generalform7.element('input[name=f4]')['_class']='form-control'
    form_generalform7.element('input[name=f4]')['_value']='12-02-2012'
    form_generalform7.element('input[name=f4]')['_id']='id345'
    form_generalform7.custom.submit['_type'] = 'submit'
    form_generalform7.custom.submit['_id'] = 'unk-id'
    form_generalform7.custom.submit['_value'] = 'submit input'
    form_generalform7.custom.submit['_class'] = 'unk-class'
    form_generalform7.custom.submit['_title'] = 'submit form_generalform7'

    if form_generalform7.accepts(request,session): 
        response.flash7 = 'submitted form_generalform7' 
    elif form_generalform7.errors:
        response.flash7 = '!Errors! form_generalform7' 
    else: 
        response.flash7 = 'form_generalform7' 



    form_generalform8 = SQLFORM(db.dform_generalform8, _class = 'form-horizontal', _id= 'idUnk8' )

    form_generalform8.element('input[name=f0]')['_placeholder']='f0 place_350'
    form_generalform8.element('input[name=f0]')['_id']='reservation'
    form_generalform8.element('input[name=f0]')['_class']='form-control'
    form_generalform8.element('input[name=f1]')['_placeholder']='f1 place_353'
    form_generalform8.element('input[name=f1]')['_id']='reportrange'
    form_generalform8.element('input[name=f1]')['_value']='02-16-2012'
    form_generalform8.element('input[name=f1]')['_class']='form-control'
    form_generalform8.custom.submit['_type'] = 'submit'
    form_generalform8.custom.submit['_id'] = 'unk-id'
    form_generalform8.custom.submit['_value'] = 'submit input'
    form_generalform8.custom.submit['_class'] = 'unk-class'
    form_generalform8.custom.submit['_title'] = 'submit form_generalform8'

    if form_generalform8.accepts(request,session): 
        response.flash8 = 'submitted form_generalform8' 
    elif form_generalform8.errors:
        response.flash8 = '!Errors! form_generalform8' 
    else: 
        response.flash8 = 'form_generalform8' 



    form_generalform9 = SQLFORM(db.dform_generalform9, _class = 'form-horizontal', _id= 'idUnk9' )

    form_generalform9.element('input[name=f0]')['_placeholder']='f0 place_356'
    form_generalform9.element('input[name=f0]')['_class']='form-control'
    form_generalform9.element('input[name=f0]')['_id']='id354'
    form_generalform9.custom.submit['_type'] = 'submit'
    form_generalform9.custom.submit['_class'] = 'unk-class'
    form_generalform9.custom.submit['_value'] = 'submit input'
    form_generalform9.custom.submit['_id'] = 'unk-id'
    form_generalform9.custom.submit['_title'] = 'submit form_generalform9'

    if form_generalform9.accepts(request,session): 
        response.flash9 = 'submitted form_generalform9' 
    elif form_generalform9.errors:
        response.flash9 = '!Errors! form_generalform9' 
    else: 
        response.flash9 = 'form_generalform9' 



    form_generalform10 = SQLFORM(db.dform_generalform10, _class = '', _id= 'idUnk10' )

    form_generalform10.element('input[name=f0]')['_placeholder']='f0 .col-lg-1'
    form_generalform10.element('input[name=f0]')['_class']='form-control'
    form_generalform10.element('input[name=f0]')['_id']='id357'
    form_generalform10.element('input[name=f1]')['_placeholder']='f1 .col-lg-11'
    form_generalform10.element('input[name=f1]')['_class']='form-control'
    form_generalform10.element('input[name=f1]')['_id']='id359'
    form_generalform10.element('input[name=f2]')['_placeholder']='f2 .col-lg-2'
    form_generalform10.element('input[name=f2]')['_class']='form-control'
    form_generalform10.element('input[name=f2]')['_id']='id361'
    form_generalform10.element('input[name=f3]')['_placeholder']='f3 .col-lg-10'
    form_generalform10.element('input[name=f3]')['_class']='form-control'
    form_generalform10.element('input[name=f3]')['_id']='id363'
    form_generalform10.element('input[name=f4]')['_placeholder']='f4 .col-lg-3'
    form_generalform10.element('input[name=f4]')['_class']='form-control'
    form_generalform10.element('input[name=f4]')['_id']='id365'
    form_generalform10.element('input[name=f5]')['_placeholder']='f5 .col-lg-9'
    form_generalform10.element('input[name=f5]')['_class']='form-control'
    form_generalform10.element('input[name=f5]')['_id']='id367'
    form_generalform10.element('input[name=f6]')['_placeholder']='f6 .col-lg-4'
    form_generalform10.element('input[name=f6]')['_class']='form-control'
    form_generalform10.element('input[name=f6]')['_id']='id369'
    form_generalform10.element('input[name=f7]')['_placeholder']='f7 .col-lg-8'
    form_generalform10.element('input[name=f7]')['_class']='form-control'
    form_generalform10.element('input[name=f7]')['_id']='id371'
    form_generalform10.element('input[name=f8]')['_placeholder']='f8 .col-lg-5'
    form_generalform10.element('input[name=f8]')['_class']='form-control'
    form_generalform10.element('input[name=f8]')['_id']='id373'
    form_generalform10.element('input[name=f9]')['_placeholder']='f9 .col-lg-7'
    form_generalform10.element('input[name=f9]')['_class']='form-control'
    form_generalform10.element('input[name=f9]')['_id']='id375'
    form_generalform10.element('input[name=f10]')['_placeholder']='f10 .col-lg-6'
    form_generalform10.element('input[name=f10]')['_class']='form-control'
    form_generalform10.element('input[name=f10]')['_id']='id377'
    form_generalform10.element('input[name=f11]')['_placeholder']='f11 .col-lg-6'
    form_generalform10.element('input[name=f11]')['_class']='form-control'
    form_generalform10.element('input[name=f11]')['_id']='id379'
    form_generalform10.element('input[name=f12]')['_placeholder']='f12 .col-lg-4'
    form_generalform10.element('input[name=f12]')['_class']='form-control'
    form_generalform10.element('input[name=f12]')['_id']='id381'
    form_generalform10.element('input[name=f13]')['_placeholder']='f13 .col-lg-4'
    form_generalform10.element('input[name=f13]')['_class']='form-control'
    form_generalform10.element('input[name=f13]')['_id']='id383'
    form_generalform10.element('input[name=f14]')['_placeholder']='f14 .col-lg-4'
    form_generalform10.element('input[name=f14]')['_class']='form-control'
    form_generalform10.element('input[name=f14]')['_id']='id385'
    form_generalform10.element('input[name=f15]')['_placeholder']='f15 .col-lg-3'
    form_generalform10.element('input[name=f15]')['_class']='form-control'
    form_generalform10.element('input[name=f15]')['_id']='id387'
    form_generalform10.element('input[name=f16]')['_placeholder']='f16 .col-lg-4'
    form_generalform10.element('input[name=f16]')['_class']='form-control'
    form_generalform10.element('input[name=f16]')['_id']='id389'
    form_generalform10.element('input[name=f17]')['_placeholder']='f17 .col-lg-5'
    form_generalform10.element('input[name=f17]')['_class']='form-control'
    form_generalform10.element('input[name=f17]')['_id']='id391'
    form_generalform10.custom.submit['_type'] = 'submit'
    form_generalform10.custom.submit['_class'] = 'unk-class'
    form_generalform10.custom.submit['_value'] = 'submit input'
    form_generalform10.custom.submit['_id'] = 'unk-id'
    form_generalform10.custom.submit['_title'] = 'submit form_generalform10'

    if form_generalform10.accepts(request,session): 
        response.flash10 = 'submitted form_generalform10' 
    elif form_generalform10.errors:
        response.flash10 = '!Errors! form_generalform10' 
    else: 
        response.flash10 = 'form_generalform10' 


    return dict( DICT= rows_dict, form_generalform0= form_generalform0, form_generalform1= form_generalform1, form_generalform2= form_generalform2, form_generalform3= form_generalform3, form_generalform4= form_generalform4, form_generalform5= form_generalform5, form_generalform6= form_generalform6, form_generalform7= form_generalform7, form_generalform8= form_generalform8, form_generalform9= form_generalform9, form_generalform10= form_generalform10, )

#@auth.requires_login()
def no_header():

    qu= db.dno0header.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/no-header.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def index():

    qu= db.dindex.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index.html'


    indexform0 = SQLFORM(db.dindexform0, _class = 'main-search', _id= 'idUnk0' )

    indexform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    indexform0.element('input[name=f0]')['_class']='form-control'
    indexform0.element('input[name=f0]')['_id']='id627'
    indexform0.custom.submit['_type'] = 'submit'
    indexform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    indexform0.custom.submit['_value'] = 'unk_631'
    indexform0.custom.submit['_id'] = 'id629'
    indexform0.custom.submit['_title'] = 'submit indexform0'

    if indexform0.accepts(request,session): 
        response.flash0 = 'submitted indexform0' 
    elif indexform0.errors:
        response.flash0 = '!Errors! indexform0' 
    else: 
        response.flash0 = 'indexform0' 


    return dict( DICT= rows_dict, indexform0= indexform0, )

#@auth.requires_login()
def X503():

    qu= db.d503.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/503.html'


    X503form0 = SQLFORM(db.dX503form0, _class = 'classUnk0', _id= 'idUnk0' )

    X503form0.element('input[name=f0]')['_placeholder']='f0 search ...'
    X503form0.element('input[name=f0]')['_class']='form-control'
    X503form0.element('input[name=f0]')['_id']='id405'
    X503form0.custom.submit['_type'] = 'submit'
    X503form0.custom.submit['_class'] = 'btn btn-default'
    X503form0.custom.submit['_value'] = 'unk_409'
    X503form0.custom.submit['_id'] = 'id407'
    X503form0.custom.submit['_title'] = 'submit X503form0'

    if X503form0.accepts(request,session): 
        response.flash0 = 'submitted X503form0' 
    elif X503form0.errors:
        response.flash0 = '!Errors! X503form0' 
    else: 
        response.flash0 = 'X503form0' 


    return dict( DICT= rows_dict, X503form0= X503form0, )

#@auth.requires_login()
def no_main_search():

    qu= db.dno0main0search.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/no-main-search.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def maps():

    qu= db.dmaps.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/maps.html'


    mapsform0 = SQLFORM(db.dmapsform0, _class = 'main-search', _id= 'idUnk0' )

    mapsform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    mapsform0.element('input[name=f0]')['_class']='form-control'
    mapsform0.element('input[name=f0]')['_id']='id598'
    mapsform0.custom.submit['_type'] = 'submit'
    mapsform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    mapsform0.custom.submit['_value'] = 'unk_602'
    mapsform0.custom.submit['_id'] = 'id600'
    mapsform0.custom.submit['_title'] = 'submit mapsform0'

    if mapsform0.accepts(request,session): 
        response.flash0 = 'submitted mapsform0' 
    elif mapsform0.errors:
        response.flash0 = '!Errors! mapsform0' 
    else: 
        response.flash0 = 'mapsform0' 



    mapsform1 = SQLFORM(db.dmapsform1, _class = 'form-search', _id= 'geocoding_form' )

    mapsform1.element('input[name=f0]')['_placeholder']='f0 search ..'
    mapsform1.element('input[name=f0]')['_id']='address'
    mapsform1.element('input[name=f0]')['_class']='form-control input-sm'
    mapsform1.custom.submit['_type'] = 'submit'
    mapsform1.custom.submit['_class'] = 'btn btn-default btn-sm'
    mapsform1.custom.submit['_value'] = 'Search'
    mapsform1.custom.submit['_id'] = 'id606'
    mapsform1.custom.submit['_title'] = 'submit mapsform1'

    if mapsform1.accepts(request,session): 
        response.flash1 = 'submitted mapsform1' 
    elif mapsform1.errors:
        response.flash1 = '!Errors! mapsform1' 
    else: 
        response.flash1 = 'mapsform1' 


    return dict( DICT= rows_dict, mapsform0= mapsform0, mapsform1= mapsform1, )

#@auth.requires_login()
def table():

    qu= db.dtable.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/table.html'


    tableform0 = SQLFORM(db.dtableform0, _class = 'main-search', _id= 'idUnk0' )

    tableform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    tableform0.element('input[name=f0]')['_class']='form-control'
    tableform0.element('input[name=f0]')['_id']='id60'
    tableform0.custom.submit['_type'] = 'submit'
    tableform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    tableform0.custom.submit['_value'] = 'unk_64'
    tableform0.custom.submit['_id'] = 'id62'
    tableform0.custom.submit['_title'] = 'submit tableform0'

    if tableform0.accepts(request,session): 
        response.flash0 = 'submitted tableform0' 
    elif tableform0.errors:
        response.flash0 = '!Errors! tableform0' 
    else: 
        response.flash0 = 'tableform0' 


    return dict( DICT= rows_dict, tableform0= tableform0, )

#@auth.requires_login()
def no_header_sidebar():

    qu= db.dno0header0sidebar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/no-header-sidebar.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def fixed_header():

    qu= db.dfixed0header.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/fixed-header.html'


    fixed_headerform0 = SQLFORM(db.dfixed_headerform0, _class = 'main-search', _id= 'idUnk0' )

    fixed_headerform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    fixed_headerform0.element('input[name=f0]')['_class']='form-control'
    fixed_headerform0.element('input[name=f0]')['_id']='id132'
    fixed_headerform0.custom.submit['_type'] = 'submit'
    fixed_headerform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    fixed_headerform0.custom.submit['_value'] = 'unk_136'
    fixed_headerform0.custom.submit['_id'] = 'id134'
    fixed_headerform0.custom.submit['_title'] = 'submit fixed_headerform0'

    if fixed_headerform0.accepts(request,session): 
        response.flash0 = 'submitted fixed_headerform0' 
    elif fixed_headerform0.errors:
        response.flash0 = '!Errors! fixed_headerform0' 
    else: 
        response.flash0 = 'fixed_headerform0' 


    return dict( DICT= rows_dict, fixed_headerform0= fixed_headerform0, )

#@auth.requires_login()
def login():

    qu= db.dlogin.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/login.html'


    loginform0 = SQLFORM(db.dloginform0, _class = 'classUnk0', _id= 'idUnk0' )

    loginform0.element('input[name=f0]')['_placeholder']='f0 Username'
    loginform0.element('input[name=f0]')['_class']='form-control top'
    loginform0.element('input[name=f0]')['_id']='id30'
    loginform0.element('input[name=f1]')['_placeholder']='f1 Password'
    loginform0.element('input[name=f1]')['_class']='form-control bottom'
    loginform0.element('input[name=f1]')['_id']='id33'
    loginform0.element('input[name=f2]')['_placeholder']='f2 place_39'
    loginform0.element('input[name=f2]')['_id']='id36'
    loginform0.custom.submit['_type'] = 'submit'
    loginform0.custom.submit['_class'] = 'btn btn-lg btn-primary btn-block'
    loginform0.custom.submit['_value'] = 'Sign in'
    loginform0.custom.submit['_id'] = 'id40'
    loginform0.custom.submit['_title'] = 'submit loginform0'

    if loginform0.accepts(request,session): 
        response.flash0 = 'submitted loginform0' 
    elif loginform0.errors:
        response.flash0 = '!Errors! loginform0' 
    else: 
        response.flash0 = 'loginform0' 



    loginform1 = SQLFORM(db.dloginform1, _class = 'classUnk1', _id= 'idUnk1' )

    loginform1.element('input[name=f0]')['_placeholder']='f0 mail@domain.com'
    loginform1.element('input[name=f0]')['_class']='form-control'
    loginform1.element('input[name=f0]')['_id']='id44'
    loginform1.custom.submit['_type'] = 'submit'
    loginform1.custom.submit['_class'] = 'btn btn-lg btn-danger btn-block'
    loginform1.custom.submit['_value'] = 'Recover Password'
    loginform1.custom.submit['_id'] = 'id46'
    loginform1.custom.submit['_title'] = 'submit loginform1'

    if loginform1.accepts(request,session): 
        response.flash1 = 'submitted loginform1' 
    elif loginform1.errors:
        response.flash1 = '!Errors! loginform1' 
    else: 
        response.flash1 = 'loginform1' 



    loginform2 = SQLFORM(db.dloginform2, _class = 'classUnk2', _id= 'idUnk2' )

    loginform2.element('input[name=f0]')['_placeholder']='f0 username'
    loginform2.element('input[name=f0]')['_class']='form-control top'
    loginform2.element('input[name=f0]')['_id']='id49'
    loginform2.element('input[name=f1]')['_placeholder']='f1 mail@domain.com'
    loginform2.element('input[name=f1]')['_class']='form-control middle'
    loginform2.element('input[name=f1]')['_id']='id51'
    loginform2.element('input[name=f2]')['_placeholder']='f2 password'
    loginform2.element('input[name=f2]')['_class']='form-control middle'
    loginform2.element('input[name=f2]')['_id']='id53'
    loginform2.element('input[name=f3]')['_placeholder']='f3 re-password'
    loginform2.element('input[name=f3]')['_class']='form-control bottom'
    loginform2.element('input[name=f3]')['_id']='id55'
    loginform2.custom.submit['_type'] = 'submit'
    loginform2.custom.submit['_class'] = 'btn btn-lg btn-success btn-block'
    loginform2.custom.submit['_value'] = 'Register'
    loginform2.custom.submit['_id'] = 'id57'
    loginform2.custom.submit['_title'] = 'submit loginform2'

    if loginform2.accepts(request,session): 
        response.flash2 = 'submitted loginform2' 
    elif loginform2.errors:
        response.flash2 = '!Errors! loginform2' 
    else: 
        response.flash2 = 'loginform2' 


    return dict( DICT= rows_dict, loginform0= loginform0, loginform1= loginform1, loginform2= loginform2, )

#@auth.requires_login()
def chart():

    qu= db.dchart.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/chart.html'


    chartform0 = SQLFORM(db.dchartform0, _class = 'main-search', _id= 'idUnk0' )

    chartform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    chartform0.element('input[name=f0]')['_class']='form-control'
    chartform0.element('input[name=f0]')['_id']='id691'
    chartform0.custom.submit['_type'] = 'submit'
    chartform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    chartform0.custom.submit['_value'] = 'unk_695'
    chartform0.custom.submit['_id'] = 'id693'
    chartform0.custom.submit['_title'] = 'submit chartform0'

    if chartform0.accepts(request,session): 
        response.flash0 = 'submitted chartform0' 
    elif chartform0.errors:
        response.flash0 = '!Errors! chartform0' 
    else: 
        response.flash0 = 'chartform0' 


    return dict( DICT= rows_dict, chartform0= chartform0, )

#@auth.requires_login()
def grid():

    qu= db.dgrid.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/grid.html'


    gridform0 = SQLFORM(db.dgridform0, _class = 'main-search', _id= 'idUnk0' )

    gridform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    gridform0.element('input[name=f0]')['_class']='form-control'
    gridform0.element('input[name=f0]')['_id']='id615'
    gridform0.custom.submit['_type'] = 'submit'
    gridform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    gridform0.custom.submit['_value'] = 'unk_619'
    gridform0.custom.submit['_id'] = 'id617'
    gridform0.custom.submit['_title'] = 'submit gridform0'

    if gridform0.accepts(request,session): 
        response.flash0 = 'submitted gridform0' 
    elif gridform0.errors:
        response.flash0 = '!Errors! gridform0' 
    else: 
        response.flash0 = 'gridform0' 


    return dict( DICT= rows_dict, gridform0= gridform0, )

#@auth.requires_login()
def icon():

    qu= db.dicon.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/icon.html'


    iconform0 = SQLFORM(db.diconform0, _class = 'main-search', _id= 'idUnk0' )

    iconform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    iconform0.element('input[name=f0]')['_class']='form-control'
    iconform0.element('input[name=f0]')['_id']='id697'
    iconform0.custom.submit['_type'] = 'submit'
    iconform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    iconform0.custom.submit['_value'] = 'unk_701'
    iconform0.custom.submit['_id'] = 'id699'
    iconform0.custom.submit['_title'] = 'submit iconform0'

    if iconform0.accepts(request,session): 
        response.flash0 = 'submitted iconform0' 
    elif iconform0.errors:
        response.flash0 = '!Errors! iconform0' 
    else: 
        response.flash0 = 'iconform0' 


    return dict( DICT= rows_dict, iconform0= iconform0, )

#@auth.requires_login()
def X403():

    qu= db.d403.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/403.html'


    X403form0 = SQLFORM(db.dX403form0, _class = 'classUnk0', _id= 'idUnk0' )

    X403form0.element('input[name=f0]')['_placeholder']='f0 search ...'
    X403form0.element('input[name=f0]')['_class']='form-control'
    X403form0.element('input[name=f0]')['_id']='id72'
    X403form0.custom.submit['_type'] = 'submit'
    X403form0.custom.submit['_class'] = 'btn btn-default'
    X403form0.custom.submit['_value'] = 'unk_76'
    X403form0.custom.submit['_id'] = 'id74'
    X403form0.custom.submit['_title'] = 'submit X403form0'

    if X403form0.accepts(request,session): 
        response.flash0 = 'submitted X403form0' 
    elif X403form0.errors:
        response.flash0 = '!Errors! X403form0' 
    else: 
        response.flash0 = 'X403form0' 


    return dict( DICT= rows_dict, X403form0= X403form0, )

#@auth.requires_login()
def fixed_header_menu():

    qu= db.dfixed0header0menu.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/fixed-header-menu.html'


    fixed_header_menuform0 = SQLFORM(db.dfixed_header_menuform0, _class = 'main-search', _id= 'idUnk0' )

    fixed_header_menuform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    fixed_header_menuform0.element('input[name=f0]')['_class']='form-control'
    fixed_header_menuform0.element('input[name=f0]')['_id']='id108'
    fixed_header_menuform0.custom.submit['_type'] = 'submit'
    fixed_header_menuform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    fixed_header_menuform0.custom.submit['_value'] = 'unk_112'
    fixed_header_menuform0.custom.submit['_id'] = 'id110'
    fixed_header_menuform0.custom.submit['_title'] = 'submit fixed_header_menuform0'

    if fixed_header_menuform0.accepts(request,session): 
        response.flash0 = 'submitted fixed_header_menuform0' 
    elif fixed_header_menuform0.errors:
        response.flash0 = '!Errors! fixed_header_menuform0' 
    else: 
        response.flash0 = 'fixed_header_menuform0' 


    return dict( DICT= rows_dict, fixed_header_menuform0= fixed_header_menuform0, )

#@auth.requires_login()
def fixed_header_mini_sidebar():

    qu= db.dfixed0header0mini0sidebar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/fixed-header-mini-sidebar.html'


    fixed_header_mini_sidebarform0 = SQLFORM(db.dfixed_header_mini_sidebarform0, _class = 'main-search', _id= 'idUnk0' )

    fixed_header_mini_sidebarform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    fixed_header_mini_sidebarform0.element('input[name=f0]')['_class']='form-control'
    fixed_header_mini_sidebarform0.element('input[name=f0]')['_id']='id661'
    fixed_header_mini_sidebarform0.custom.submit['_type'] = 'submit'
    fixed_header_mini_sidebarform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    fixed_header_mini_sidebarform0.custom.submit['_value'] = 'unk_665'
    fixed_header_mini_sidebarform0.custom.submit['_id'] = 'id663'
    fixed_header_mini_sidebarform0.custom.submit['_title'] = 'submit fixed_header_mini_sidebarform0'

    if fixed_header_mini_sidebarform0.accepts(request,session): 
        response.flash0 = 'submitted fixed_header_mini_sidebarform0' 
    elif fixed_header_mini_sidebarform0.errors:
        response.flash0 = '!Errors! fixed_header_mini_sidebarform0' 
    else: 
        response.flash0 = 'fixed_header_mini_sidebarform0' 


    return dict( DICT= rows_dict, fixed_header_mini_sidebarform0= fixed_header_mini_sidebarform0, )

#@auth.requires_login()
def panel():

    qu= db.dpanel.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/panel.html'


    panelform0 = SQLFORM(db.dpanelform0, _class = 'main-search', _id= 'idUnk0' )

    panelform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    panelform0.element('input[name=f0]')['_class']='form-control'
    panelform0.element('input[name=f0]')['_id']='id453'
    panelform0.custom.submit['_type'] = 'submit'
    panelform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    panelform0.custom.submit['_value'] = 'unk_457'
    panelform0.custom.submit['_id'] = 'id455'
    panelform0.custom.submit['_title'] = 'submit panelform0'

    if panelform0.accepts(request,session): 
        response.flash0 = 'submitted panelform0' 
    elif panelform0.errors:
        response.flash0 = '!Errors! panelform0' 
    else: 
        response.flash0 = 'panelform0' 


    return dict( DICT= rows_dict, panelform0= panelform0, )

#@auth.requires_login()
def fixed_menu_boxed():

    qu= db.dfixed0menu0boxed.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/fixed-menu-boxed.html'


    fixed_menu_boxedform0 = SQLFORM(db.dfixed_menu_boxedform0, _class = 'main-search', _id= 'idUnk0' )

    fixed_menu_boxedform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    fixed_menu_boxedform0.element('input[name=f0]')['_class']='form-control'
    fixed_menu_boxedform0.element('input[name=f0]')['_id']='id586'
    fixed_menu_boxedform0.custom.submit['_type'] = 'submit'
    fixed_menu_boxedform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    fixed_menu_boxedform0.custom.submit['_value'] = 'unk_590'
    fixed_menu_boxedform0.custom.submit['_id'] = 'id588'
    fixed_menu_boxedform0.custom.submit['_title'] = 'submit fixed_menu_boxedform0'

    if fixed_menu_boxedform0.accepts(request,session): 
        response.flash0 = 'submitted fixed_menu_boxedform0' 
    elif fixed_menu_boxedform0.errors:
        response.flash0 = '!Errors! fixed_menu_boxedform0' 
    else: 
        response.flash0 = 'fixed_menu_boxedform0' 


    return dict( DICT= rows_dict, fixed_menu_boxedform0= fixed_menu_boxedform0, )

#@auth.requires_login()
def fixed_mini_sidebar():

    qu= db.dfixed0mini0sidebar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/fixed-mini-sidebar.html'


    fixed_mini_sidebarform0 = SQLFORM(db.dfixed_mini_sidebarform0, _class = 'main-search', _id= 'idUnk0' )

    fixed_mini_sidebarform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    fixed_mini_sidebarform0.element('input[name=f0]')['_class']='form-control'
    fixed_mini_sidebarform0.element('input[name=f0]')['_id']='id609'
    fixed_mini_sidebarform0.custom.submit['_type'] = 'submit'
    fixed_mini_sidebarform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    fixed_mini_sidebarform0.custom.submit['_value'] = 'unk_613'
    fixed_mini_sidebarform0.custom.submit['_id'] = 'id611'
    fixed_mini_sidebarform0.custom.submit['_title'] = 'submit fixed_mini_sidebarform0'

    if fixed_mini_sidebarform0.accepts(request,session): 
        response.flash0 = 'submitted fixed_mini_sidebarform0' 
    elif fixed_mini_sidebarform0.errors:
        response.flash0 = '!Errors! fixed_mini_sidebarform0' 
    else: 
        response.flash0 = 'fixed_mini_sidebarform0' 


    return dict( DICT= rows_dict, fixed_mini_sidebarform0= fixed_mini_sidebarform0, )

#@auth.requires_login()
def no_left_sidebar():

    qu= db.dno0left0sidebar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/no-left-sidebar.html'


    no_left_sidebarform0 = SQLFORM(db.dno_left_sidebarform0, _class = 'main-search', _id= 'idUnk0' )

    no_left_sidebarform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    no_left_sidebarform0.element('input[name=f0]')['_class']='form-control'
    no_left_sidebarform0.element('input[name=f0]')['_id']='id66'
    no_left_sidebarform0.custom.submit['_type'] = 'submit'
    no_left_sidebarform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    no_left_sidebarform0.custom.submit['_value'] = 'unk_70'
    no_left_sidebarform0.custom.submit['_id'] = 'id68'
    no_left_sidebarform0.custom.submit['_title'] = 'submit no_left_sidebarform0'

    if no_left_sidebarform0.accepts(request,session): 
        response.flash0 = 'submitted no_left_sidebarform0' 
    elif no_left_sidebarform0.errors:
        response.flash0 = '!Errors! no_left_sidebarform0' 
    else: 
        response.flash0 = 'no_left_sidebarform0' 


    return dict( DICT= rows_dict, no_left_sidebarform0= no_left_sidebarform0, )

#@auth.requires_login()
def X405():

    qu= db.d405.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/405.html'


    X405form0 = SQLFORM(db.dX405form0, _class = 'classUnk0', _id= 'idUnk0' )

    X405form0.element('input[name=f0]')['_placeholder']='f0 search ...'
    X405form0.element('input[name=f0]')['_class']='form-control'
    X405form0.element('input[name=f0]')['_id']='id592'
    X405form0.custom.submit['_type'] = 'submit'
    X405form0.custom.submit['_class'] = 'btn btn-default'
    X405form0.custom.submit['_value'] = 'unk_596'
    X405form0.custom.submit['_id'] = 'id594'
    X405form0.custom.submit['_title'] = 'submit X405form0'

    if X405form0.accepts(request,session): 
        response.flash0 = 'submitted X405form0' 
    elif X405form0.errors:
        response.flash0 = '!Errors! X405form0' 
    else: 
        response.flash0 = 'X405form0' 


    return dict( DICT= rows_dict, X405form0= X405form0, )

#@auth.requires_login()
def fixed_header_boxed():

    qu= db.dfixed0header0boxed.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/fixed-header-boxed.html'


    fixed_header_boxedform0 = SQLFORM(db.dfixed_header_boxedform0, _class = 'main-search', _id= 'idUnk0' )

    fixed_header_boxedform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    fixed_header_boxedform0.element('input[name=f0]')['_class']='form-control'
    fixed_header_boxedform0.element('input[name=f0]')['_id']='id679'
    fixed_header_boxedform0.custom.submit['_type'] = 'submit'
    fixed_header_boxedform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    fixed_header_boxedform0.custom.submit['_value'] = 'unk_683'
    fixed_header_boxedform0.custom.submit['_id'] = 'id681'
    fixed_header_boxedform0.custom.submit['_title'] = 'submit fixed_header_boxedform0'

    if fixed_header_boxedform0.accepts(request,session): 
        response.flash0 = 'submitted fixed_header_boxedform0' 
    elif fixed_header_boxedform0.errors:
        response.flash0 = '!Errors! fixed_header_boxedform0' 
    else: 
        response.flash0 = 'fixed_header_boxedform0' 


    return dict( DICT= rows_dict, fixed_header_boxedform0= fixed_header_boxedform0, )

#@auth.requires_login()
def typography():

    qu= db.dtypography.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/typography.html'


    typographyform0 = SQLFORM(db.dtypographyform0, _class = 'main-search', _id= 'idUnk0' )

    typographyform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    typographyform0.element('input[name=f0]')['_class']='form-control'
    typographyform0.element('input[name=f0]')['_id']='id393'
    typographyform0.custom.submit['_type'] = 'submit'
    typographyform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    typographyform0.custom.submit['_value'] = 'unk_397'
    typographyform0.custom.submit['_id'] = 'id395'
    typographyform0.custom.submit['_title'] = 'submit typographyform0'

    if typographyform0.accepts(request,session): 
        response.flash0 = 'submitted typographyform0' 
    elif typographyform0.errors:
        response.flash0 = '!Errors! typographyform0' 
    else: 
        response.flash0 = 'typographyform0' 


    return dict( DICT= rows_dict, typographyform0= typographyform0, )

#@auth.requires_login()
def sm():

    qu= db.dsm.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/sm.html'


    smform0 = SQLFORM(db.dsmform0, _class = 'main-search', _id= 'idUnk0' )

    smform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    smform0.element('input[name=f0]')['_class']='form-control'
    smform0.element('input[name=f0]')['_id']='id411'
    smform0.custom.submit['_type'] = 'submit'
    smform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    smform0.custom.submit['_value'] = 'unk_415'
    smform0.custom.submit['_id'] = 'id413'
    smform0.custom.submit['_title'] = 'submit smform0'

    if smform0.accepts(request,session): 
        response.flash0 = 'submitted smform0' 
    elif smform0.errors:
        response.flash0 = '!Errors! smform0' 
    else: 
        response.flash0 = 'smform0' 


    return dict( DICT= rows_dict, smform0= smform0, )

#@auth.requires_login()
def progress():

    qu= db.dprogress.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/progress.html'


    progressform0 = SQLFORM(db.dprogressform0, _class = 'main-search', _id= 'idUnk0' )

    progressform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    progressform0.element('input[name=f0]')['_class']='form-control'
    progressform0.element('input[name=f0]')['_id']='id399'
    progressform0.custom.submit['_type'] = 'submit'
    progressform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    progressform0.custom.submit['_value'] = 'unk_403'
    progressform0.custom.submit['_id'] = 'id401'
    progressform0.custom.submit['_title'] = 'submit progressform0'

    if progressform0.accepts(request,session): 
        response.flash0 = 'submitted progressform0' 
    elif progressform0.errors:
        response.flash0 = '!Errors! progressform0' 
    else: 
        response.flash0 = 'progressform0' 


    return dict( DICT= rows_dict, progressform0= progressform0, )

#@auth.requires_login()
def alterne():

    qu= db.dalterne.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/alterne.html'


    alterneform0 = SQLFORM(db.dalterneform0, _class = 'main-search', _id= 'idUnk0' )

    alterneform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    alterneform0.element('input[name=f0]')['_class']='form-control'
    alterneform0.element('input[name=f0]')['_id']='id621'
    alterneform0.custom.submit['_type'] = 'submit'
    alterneform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    alterneform0.custom.submit['_value'] = 'unk_625'
    alterneform0.custom.submit['_id'] = 'id623'
    alterneform0.custom.submit['_title'] = 'submit alterneform0'

    if alterneform0.accepts(request,session): 
        response.flash0 = 'submitted alterneform0' 
    elif alterneform0.errors:
        response.flash0 = '!Errors! alterneform0' 
    else: 
        response.flash0 = 'alterneform0' 


    return dict( DICT= rows_dict, alterneform0= alterneform0, )

#@auth.requires_login()
def offline():

    qu= db.doffline.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/offline.html'


    offlineform0 = SQLFORM(db.dofflineform0, _class = 'classUnk0', _id= 'idUnk0' )

    offlineform0.element('input[name=f0]')['_placeholder']='f0 search ...'
    offlineform0.element('input[name=f0]')['_class']='form-control'
    offlineform0.element('input[name=f0]')['_id']='id0'
    offlineform0.custom.submit['_type'] = 'submit'
    offlineform0.custom.submit['_class'] = 'btn btn-default'
    offlineform0.custom.submit['_value'] = 'unk_4'
    offlineform0.custom.submit['_id'] = 'id2'
    offlineform0.custom.submit['_title'] = 'submit offlineform0'

    if offlineform0.accepts(request,session): 
        response.flash0 = 'submitted offlineform0' 
    elif offlineform0.errors:
        response.flash0 = '!Errors! offlineform0' 
    else: 
        response.flash0 = 'offlineform0' 


    return dict( DICT= rows_dict, offlineform0= offlineform0, )

#@auth.requires_login()
def blank():

    qu= db.dblank.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/blank.html'


    blankform0 = SQLFORM(db.dblankform0, _class = 'main-search', _id= 'idUnk0' )

    blankform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    blankform0.element('input[name=f0]')['_class']='form-control'
    blankform0.element('input[name=f0]')['_id']='id102'
    blankform0.custom.submit['_type'] = 'submit'
    blankform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    blankform0.custom.submit['_value'] = 'unk_106'
    blankform0.custom.submit['_id'] = 'id104'
    blankform0.custom.submit['_title'] = 'submit blankform0'

    if blankform0.accepts(request,session): 
        response.flash0 = 'submitted blankform0' 
    elif blankform0.errors:
        response.flash0 = '!Errors! blankform0' 
    else: 
        response.flash0 = 'blankform0' 


    return dict( DICT= rows_dict, blankform0= blankform0, )

#@auth.requires_login()
def countdown():

    qu= db.dcountdown.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/countdown.html'


    countdownform0 = SQLFORM(db.dcountdownform0, _class = 'classUnk0', _id= 'emailForm' )

    countdownform0.element('input[name=f0]')['_placeholder']='f0 Enter your email to subscribe'
    countdownform0.element('input[name=f0]')['_id']='email1'
    countdownform0.element('input[name=f0]')['_class']='form-control'
    countdownform0.custom.submit['_type'] = 'submit'
    countdownform0.custom.submit['_class'] = 'btn btn-warning btn-block'
    countdownform0.custom.submit['_value'] = 'Submit'
    countdownform0.custom.submit['_id'] = 'id641'
    countdownform0.custom.submit['_title'] = 'submit countdownform0'
    countdownform0.custom.submit['_type'] = 'submit'
    countdownform0.custom.submit['_class'] = 'btn btn-block btn-default'
    countdownform0.custom.submit['_value'] = 'Cancel'
    countdownform0.custom.submit['_id'] = 'id644'
    countdownform0.custom.submit['_title'] = 'submit countdownform0'

    if countdownform0.accepts(request,session): 
        response.flash0 = 'submitted countdownform0' 
    elif countdownform0.errors:
        response.flash0 = '!Errors! countdownform0' 
    else: 
        response.flash0 = 'countdownform0' 



    countdownform1 = SQLFORM(db.dcountdownform1, _class = 'classUnk1', _id= 'messageForm' )

    countdownform1.element('input[name=f0]')['_placeholder']='f0 Enter yor name'
    countdownform1.element('input[name=f0]')['_id']='name'
    countdownform1.element('input[name=f0]')['_class']='form-control'
    countdownform1.element('input[name=f1]')['_placeholder']='f1 Enter your e-mail'
    countdownform1.element('input[name=f1]')['_id']='email'
    countdownform1.element('input[name=f1]')['_class']='form-control'
    countdownform1.element('input[name=f2]')['_placeholder']='f2 Enter your subject'
    countdownform1.element('input[name=f2]')['_id']='subject'
    countdownform1.element('input[name=f2]')['_class']='form-control'
    countdownform1.element('textarea[name=f3]')['_placeholder']='f3 Enter your message'
    countdownform1.element('textarea[name=f3]')['_id']='message'
    countdownform1.element('textarea[name=f3]')['_class']='form-control'
    countdownform1.custom.submit['_type'] = 'submit'
    countdownform1.custom.submit['_class'] = 'btn btn-warning btn-block'
    countdownform1.custom.submit['_value'] = 'Submit'
    countdownform1.custom.submit['_id'] = 'id655'
    countdownform1.custom.submit['_title'] = 'submit countdownform1'
    countdownform1.custom.submit['_type'] = 'submit'
    countdownform1.custom.submit['_class'] = 'btn btn-block btn-default'
    countdownform1.custom.submit['_value'] = 'Cancel'
    countdownform1.custom.submit['_id'] = 'id658'
    countdownform1.custom.submit['_title'] = 'submit countdownform1'

    if countdownform1.accepts(request,session): 
        response.flash1 = 'submitted countdownform1' 
    elif countdownform1.errors:
        response.flash1 = '!Errors! countdownform1' 
    else: 
        response.flash1 = 'countdownform1' 


    return dict( DICT= rows_dict, countdownform0= countdownform0, countdownform1= countdownform1, )

#@auth.requires_login()
def form_wysiwyg():

    qu= db.dform0wysiwyg.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/form-wysiwyg.html'


    form_wysiwygform0 = SQLFORM(db.dform_wysiwygform0, _class = 'main-search', _id= 'idUnk0' )

    form_wysiwygform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    form_wysiwygform0.element('input[name=f0]')['_class']='form-control'
    form_wysiwygform0.element('input[name=f0]')['_id']='id114'
    form_wysiwygform0.custom.submit['_type'] = 'submit'
    form_wysiwygform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    form_wysiwygform0.custom.submit['_value'] = 'unk_118'
    form_wysiwygform0.custom.submit['_id'] = 'id116'
    form_wysiwygform0.custom.submit['_title'] = 'submit form_wysiwygform0'

    if form_wysiwygform0.accepts(request,session): 
        response.flash0 = 'submitted form_wysiwygform0' 
    elif form_wysiwygform0.errors:
        response.flash0 = '!Errors! form_wysiwygform0' 
    else: 
        response.flash0 = 'form_wysiwygform0' 



    form_wysiwygform1 = SQLFORM(db.dform_wysiwygform1, _class = 'classUnk1', _id= 'idUnk1' )

    form_wysiwygform1.custom.submit['_type'] = 'submit'
    form_wysiwygform1.custom.submit['_class'] = 'btn btn-primary'
    form_wysiwygform1.custom.submit['_value'] = 'Submit'
    form_wysiwygform1.custom.submit['_id'] = 'id120'
    form_wysiwygform1.custom.submit['_title'] = 'submit form_wysiwygform1'
    form_wysiwygform1.element('textarea[name=f0]')['_rows']='10'
    form_wysiwygform1.element('textarea[name=f0]')['_placeholder']='f0 place_125'
    form_wysiwygform1.element('textarea[name=f0]')['_id']='wysihtml5'
    form_wysiwygform1.element('textarea[name=f0]')['_class']='form-control'

    if form_wysiwygform1.accepts(request,session): 
        response.flash1 = 'submitted form_wysiwygform1' 
    elif form_wysiwygform1.errors:
        response.flash1 = '!Errors! form_wysiwygform1' 
    else: 
        response.flash1 = 'form_wysiwygform1' 



    form_wysiwygform2 = SQLFORM(db.dform_wysiwygform2, _class = 'classUnk2', _id= 'idUnk2' )

    form_wysiwygform2.custom.submit['_type'] = 'submit'
    form_wysiwygform2.custom.submit['_class'] = 'btn btn-primary'
    form_wysiwygform2.custom.submit['_value'] = 'Submit'
    form_wysiwygform2.custom.submit['_id'] = 'id126'
    form_wysiwygform2.custom.submit['_title'] = 'submit form_wysiwygform2'
    form_wysiwygform2.element('textarea[name=f0]')['_placeholder']='f0 place_131'
    form_wysiwygform2.element('textarea[name=f0]')['_id']='ckeditor'
    form_wysiwygform2.element('textarea[name=f0]')['_class']='ckeditor'

    if form_wysiwygform2.accepts(request,session): 
        response.flash2 = 'submitted form_wysiwygform2' 
    elif form_wysiwygform2.errors:
        response.flash2 = '!Errors! form_wysiwygform2' 
    else: 
        response.flash2 = 'form_wysiwygform2' 


    return dict( DICT= rows_dict, form_wysiwygform0= form_wysiwygform0, form_wysiwygform1= form_wysiwygform1, form_wysiwygform2= form_wysiwygform2, )

#@auth.requires_login()
def pricing():

    qu= db.dpricing.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/pricing.html'


    pricingform0 = SQLFORM(db.dpricingform0, _class = 'main-search', _id= 'idUnk0' )

    pricingform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    pricingform0.element('input[name=f0]')['_class']='form-control'
    pricingform0.element('input[name=f0]')['_id']='id459'
    pricingform0.custom.submit['_type'] = 'submit'
    pricingform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    pricingform0.custom.submit['_value'] = 'unk_463'
    pricingform0.custom.submit['_id'] = 'id461'
    pricingform0.custom.submit['_title'] = 'submit pricingform0'

    if pricingform0.accepts(request,session): 
        response.flash0 = 'submitted pricingform0' 
    elif pricingform0.errors:
        response.flash0 = '!Errors! pricingform0' 
    else: 
        response.flash0 = 'pricingform0' 


    return dict( DICT= rows_dict, pricingform0= pricingform0, )

#@auth.requires_login()
def bgcolor():

    qu= db.dbgcolor.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/bgcolor.html'


    bgcolorform0 = SQLFORM(db.dbgcolorform0, _class = 'main-search', _id= 'idUnk0' )

    bgcolorform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    bgcolorform0.element('input[name=f0]')['_class']='form-control'
    bgcolorform0.element('input[name=f0]')['_id']='id90'
    bgcolorform0.custom.submit['_type'] = 'submit'
    bgcolorform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    bgcolorform0.custom.submit['_value'] = 'unk_94'
    bgcolorform0.custom.submit['_id'] = 'id92'
    bgcolorform0.custom.submit['_title'] = 'submit bgcolorform0'

    if bgcolorform0.accepts(request,session): 
        response.flash0 = 'submitted bgcolorform0' 
    elif bgcolorform0.errors:
        response.flash0 = '!Errors! bgcolorform0' 
    else: 
        response.flash0 = 'bgcolorform0' 


    return dict( DICT= rows_dict, bgcolorform0= bgcolorform0, )

#@auth.requires_login()
def calendar():

    qu= db.dcalendar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/calendar.html'


    calendarform0 = SQLFORM(db.dcalendarform0, _class = 'main-search', _id= 'idUnk0' )

    calendarform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    calendarform0.element('input[name=f0]')['_class']='form-control'
    calendarform0.element('input[name=f0]')['_id']='id685'
    calendarform0.custom.submit['_type'] = 'submit'
    calendarform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    calendarform0.custom.submit['_value'] = 'unk_689'
    calendarform0.custom.submit['_id'] = 'id687'
    calendarform0.custom.submit['_title'] = 'submit calendarform0'

    if calendarform0.accepts(request,session): 
        response.flash0 = 'submitted calendarform0' 
    elif calendarform0.errors:
        response.flash0 = '!Errors! calendarform0' 
    else: 
        response.flash0 = 'calendarform0' 


    return dict( DICT= rows_dict, calendarform0= calendarform0, )

#@auth.requires_login()
def no_left_right_sidebar():

    qu= db.dno0left0right0sidebar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/no-left-right-sidebar.html'


    no_left_right_sidebarform0 = SQLFORM(db.dno_left_right_sidebarform0, _class = 'main-search', _id= 'idUnk0' )

    no_left_right_sidebarform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    no_left_right_sidebarform0.element('input[name=f0]')['_class']='form-control'
    no_left_right_sidebarform0.element('input[name=f0]')['_id']='id96'
    no_left_right_sidebarform0.custom.submit['_type'] = 'submit'
    no_left_right_sidebarform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    no_left_right_sidebarform0.custom.submit['_value'] = 'unk_100'
    no_left_right_sidebarform0.custom.submit['_id'] = 'id98'
    no_left_right_sidebarform0.custom.submit['_title'] = 'submit no_left_right_sidebarform0'

    if no_left_right_sidebarform0.accepts(request,session): 
        response.flash0 = 'submitted no_left_right_sidebarform0' 
    elif no_left_right_sidebarform0.errors:
        response.flash0 = '!Errors! no_left_right_sidebarform0' 
    else: 
        response.flash0 = 'no_left_right_sidebarform0' 


    return dict( DICT= rows_dict, no_left_right_sidebarform0= no_left_right_sidebarform0, )

#@auth.requires_login()
def form_wizard():

    qu= db.dform0wizard.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/form-wizard.html'


    form_wizardform0 = SQLFORM(db.dform_wizardform0, _class = 'main-search', _id= 'idUnk0' )

    form_wizardform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    form_wizardform0.element('input[name=f0]')['_class']='form-control'
    form_wizardform0.element('input[name=f0]')['_id']='id417'
    form_wizardform0.custom.submit['_type'] = 'submit'
    form_wizardform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    form_wizardform0.custom.submit['_value'] = 'unk_421'
    form_wizardform0.custom.submit['_id'] = 'id419'
    form_wizardform0.custom.submit['_title'] = 'submit form_wizardform0'

    if form_wizardform0.accepts(request,session): 
        response.flash0 = 'submitted form_wizardform0' 
    elif form_wizardform0.errors:
        response.flash0 = '!Errors! form_wizardform0' 
    else: 
        response.flash0 = 'form_wizardform0' 



    form_wizardform1 = SQLFORM(db.dform_wizardform1, _class = 'form-horizontal', _id= 'idUnk1' )

    form_wizardform1.element('input[name=f0]')['_placeholder']='f0 place_425'
    form_wizardform1.element('input[name=f0]')['_id']='id423'
    form_wizardform1.element('input[name=f1]')['_placeholder']='f1 place_428'
    form_wizardform1.element('input[name=f1]')['_id']='fileUpload'
    form_wizardform1.element('input[name=f2]')['_placeholder']='f2 place_431'
    form_wizardform1.element('input[name=f2]')['_id']='id429'
    form_wizardform1.element('input[name=f3]')['_placeholder']='f3 place_434'
    form_wizardform1.element('input[name=f3]')['_id']='id432'
    form_wizardform1.element('input[name=f4]')['_placeholder']='f4 place_437'
    form_wizardform1.element('input[name=f4]')['_id']='id435'
    form_wizardform1.element('input[name=f5]')['_placeholder']='f5 place_440'
    form_wizardform1.element('input[name=f5]')['_id']='id438'
    form_wizardform1.custom.submit['_class'] = 'input-group-addon btn btn-default fileinput-exists'
    form_wizardform1.custom.submit['_id'] = 'id441'
    form_wizardform1.custom.submit['_title'] = 'submit form_wizardform1'
    form_wizardform1.custom.submit['_class'] = 'close fileinput-exists'
    form_wizardform1.custom.submit['_id'] = 'id444'
    form_wizardform1.custom.submit['_title'] = 'submit form_wizardform1'
    form_wizardform1.custom.submit['_class'] = 'btn btn-default fileinput-exists'
    form_wizardform1.custom.submit['_id'] = 'id447'
    form_wizardform1.custom.submit['_title'] = 'submit form_wizardform1'
    form_wizardform1.custom.submit['_class'] = 'btn btn-default fileinput-exists'
    form_wizardform1.custom.submit['_id'] = 'id450'
    form_wizardform1.custom.submit['_title'] = 'submit form_wizardform1'

    if form_wizardform1.accepts(request,session): 
        response.flash1 = 'submitted form_wizardform1' 
    elif form_wizardform1.errors:
        response.flash1 = '!Errors! form_wizardform1' 
    else: 
        response.flash1 = 'form_wizardform1' 


    return dict( DICT= rows_dict, form_wizardform0= form_wizardform0, form_wizardform1= form_wizardform1, )

#@auth.requires_login()
def fixed_menu():

    qu= db.dfixed0menu.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/fixed-menu.html'


    fixed_menuform0 = SQLFORM(db.dfixed_menuform0, _class = 'main-search', _id= 'idUnk0' )

    fixed_menuform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    fixed_menuform0.element('input[name=f0]')['_class']='form-control'
    fixed_menuform0.element('input[name=f0]')['_id']='id6'
    fixed_menuform0.custom.submit['_type'] = 'submit'
    fixed_menuform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    fixed_menuform0.custom.submit['_value'] = 'unk_10'
    fixed_menuform0.custom.submit['_id'] = 'id8'
    fixed_menuform0.custom.submit['_title'] = 'submit fixed_menuform0'

    if fixed_menuform0.accepts(request,session): 
        response.flash0 = 'submitted fixed_menuform0' 
    elif fixed_menuform0.errors:
        response.flash0 = '!Errors! fixed_menuform0' 
    else: 
        response.flash0 = 'fixed_menuform0' 


    return dict( DICT= rows_dict, fixed_menuform0= fixed_menuform0, )

#@auth.requires_login()
def fxhmoxed():

    qu= db.dfxhmoxed.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/fxhmoxed.html'


    fxhmoxedform0 = SQLFORM(db.dfxhmoxedform0, _class = 'main-search', _id= 'idUnk0' )

    fxhmoxedform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    fxhmoxedform0.element('input[name=f0]')['_class']='form-control'
    fxhmoxedform0.element('input[name=f0]')['_id']='id12'
    fxhmoxedform0.custom.submit['_type'] = 'submit'
    fxhmoxedform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    fxhmoxedform0.custom.submit['_value'] = 'unk_16'
    fxhmoxedform0.custom.submit['_id'] = 'id14'
    fxhmoxedform0.custom.submit['_title'] = 'submit fxhmoxedform0'

    if fxhmoxedform0.accepts(request,session): 
        response.flash0 = 'submitted fxhmoxedform0' 
    elif fxhmoxedform0.errors:
        response.flash0 = '!Errors! fxhmoxedform0' 
    else: 
        response.flash0 = 'fxhmoxedform0' 


    return dict( DICT= rows_dict, fxhmoxedform0= fxhmoxedform0, )

#@auth.requires_login()
def X500():

    qu= db.d500.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/500.html'


    X500form0 = SQLFORM(db.dX500form0, _class = 'classUnk0', _id= 'idUnk0' )

    X500form0.element('input[name=f0]')['_placeholder']='f0 search ...'
    X500form0.element('input[name=f0]')['_class']='form-control'
    X500form0.element('input[name=f0]')['_id']='id673'
    X500form0.custom.submit['_type'] = 'submit'
    X500form0.custom.submit['_class'] = 'btn btn-default'
    X500form0.custom.submit['_value'] = 'unk_677'
    X500form0.custom.submit['_id'] = 'id675'
    X500form0.custom.submit['_title'] = 'submit X500form0'

    if X500form0.accepts(request,session): 
        response.flash0 = 'submitted X500form0' 
    elif X500form0.errors:
        response.flash0 = '!Errors! X500form0' 
    else: 
        response.flash0 = 'X500form0' 


    return dict( DICT= rows_dict, X500form0= X500form0, )

#@auth.requires_login()
def form_validation():

    qu= db.dform0validation.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/form-validation.html'


    form_validationform0 = SQLFORM(db.dform_validationform0, _class = 'main-search', _id= 'idUnk0' )

    form_validationform0.element('input[name=f0]')['_placeholder']='f0 Live Search ...'
    form_validationform0.element('input[name=f0]')['_class']='form-control'
    form_validationform0.element('input[name=f0]')['_id']='id471'
    form_validationform0.custom.submit['_type'] = 'submit'
    form_validationform0.custom.submit['_class'] = 'btn btn-primary btn-sm text-muted'
    form_validationform0.custom.submit['_value'] = 'unk_475'
    form_validationform0.custom.submit['_id'] = 'id473'
    form_validationform0.custom.submit['_title'] = 'submit form_validationform0'

    if form_validationform0.accepts(request,session): 
        response.flash0 = 'submitted form_validationform0' 
    elif form_validationform0.errors:
        response.flash0 = '!Errors! form_validationform0' 
    else: 
        response.flash0 = 'form_validationform0' 



    form_validationform1 = SQLFORM(db.dform_validationform1, _class = 'form-horizontal', _id= 'popup-validation' )

    form_validationform1.element('input[name=f0]')['_placeholder']='f0 place_479'
    form_validationform1.element('input[name=f0]')['_id']='req'
    form_validationform1.element('input[name=f0]')['_class']='validate[required] form-control'
    form_validationform1.element('input[name=f1]')['_placeholder']='f1 place_482'
    form_validationform1.element('input[name=f1]')['_id']='url1'
    form_validationform1.element('input[name=f1]')['_value']='http://'
    form_validationform1.element('input[name=f1]')['_class']='validate[required,custom[url]] form-control'
    form_validationform1.element('input[name=f2]')['_placeholder']='f2 place_485'
    form_validationform1.element('input[name=f2]')['_id']='email1'
    form_validationform1.element('input[name=f2]')['_class']='validate[required,custom[email]] form-control'
    form_validationform1.element('input[name=f3]')['_placeholder']='f3 place_488'
    form_validationform1.element('input[name=f3]')['_id']='pass1'
    form_validationform1.element('input[name=f3]')['_class']='validate[required] form-control'
    form_validationform1.element('input[name=f4]')['_placeholder']='f4 place_491'
    form_validationform1.element('input[name=f4]')['_id']='pass2'
    form_validationform1.element('input[name=f4]')['_class']='validate[required,equals[pass1]] form-control'
    form_validationform1.element('input[name=f5]')['_placeholder']='f5 place_495'
    form_validationform1.element('input[name=f5]')['_id']='minsize1'
    form_validationform1.element('input[name=f5]')['_value']='unk_494'
    form_validationform1.element('input[name=f5]')['_class']='validate[required,minSize[6]] form-control'
    form_validationform1.element('input[name=f6]')['_placeholder']='f6 place_498'
    form_validationform1.element('input[name=f6]')['_id']='maxsize1'
    form_validationform1.element('input[name=f6]')['_value']='0123456789'
    form_validationform1.element('input[name=f6]')['_class']='validate[optional,maxSize[6]] form-control'
    form_validationform1.element('input[name=f7]')['_placeholder']='f7 place_501'
    form_validationform1.element('input[name=f7]')['_id']='number2'
    form_validationform1.element('input[name=f7]')['_value']='-33.87a'
    form_validationform1.element('input[name=f7]')['_class']='validate[required,custom[number]] form-control'
    form_validationform1.element('input[name=f8]')['_placeholder']='f8 place_504'
    form_validationform1.element('input[name=f8]')['_id']='ip'
    form_validationform1.element('input[name=f8]')['_value']='192.168.3.'
    form_validationform1.element('input[name=f8]')['_class']='validate[required,custom[ipv4]] form-control'
    form_validationform1.element('input[name=f9]')['_placeholder']='f9 place_507'
    form_validationform1.element('input[name=f9]')['_id']='date3'
    form_validationform1.element('input[name=f9]')['_value']='201-12-01'
    form_validationform1.element('input[name=f9]')['_class']='validate[required,custom[date]] form-control'
    form_validationform1.element('input[name=f10]')['_placeholder']='f10 place_510'
    form_validationform1.element('input[name=f10]')['_id']='past'
    form_validationform1.element('input[name=f10]')['_value']='2012/12/16'
    form_validationform1.element('input[name=f10]')['_class']='validate[custom[date],past[2012/09/13]] form-control'
    form_validationform1.custom.submit['_type'] = 'submit'
    form_validationform1.custom.submit['_class'] = 'btn btn-primary'
    form_validationform1.custom.submit['_value'] = 'Validate'
    form_validationform1.custom.submit['_id'] = 'id511'
    form_validationform1.custom.submit['_title'] = 'submit form_validationform1'

    if form_validationform1.accepts(request,session): 
        response.flash1 = 'submitted form_validationform1' 
    elif form_validationform1.errors:
        response.flash1 = '!Errors! form_validationform1' 
    else: 
        response.flash1 = 'form_validationform1' 



    form_validationform2 = SQLFORM(db.dform_validationform2, _class = 'form-horizontal', _id= 'block-validate' )

    form_validationform2.element('input[name=f0]')['_placeholder']='f0 place_522'
    form_validationform2.element('input[name=f0]')['_id']='required2'
    form_validationform2.element('input[name=f0]')['_class']='form-control'
    form_validationform2.element('input[name=f1]')['_placeholder']='f1 place_525'
    form_validationform2.element('input[name=f1]')['_id']='email2'
    form_validationform2.element('input[name=f1]')['_class']='form-control'
    form_validationform2.element('input[name=f2]')['_placeholder']='f2 place_528'
    form_validationform2.element('input[name=f2]')['_id']='password2'
    form_validationform2.element('input[name=f2]')['_class']='form-control'
    form_validationform2.element('input[name=f3]')['_placeholder']='f3 place_531'
    form_validationform2.element('input[name=f3]')['_id']='confirm_password2'
    form_validationform2.element('input[name=f3]')['_class']='form-control'
    form_validationform2.element('input[name=f4]')['_placeholder']='f4 place_534'
    form_validationform2.element('input[name=f4]')['_id']='date2'
    form_validationform2.element('input[name=f4]')['_class']='form-control'
    form_validationform2.element('input[name=f5]')['_placeholder']='f5 place_537'
    form_validationform2.element('input[name=f5]')['_id']='url2'
    form_validationform2.element('input[name=f5]')['_class']='form-control'
    form_validationform2.element('input[name=f6]')['_placeholder']='f6 place_540'
    form_validationform2.element('input[name=f6]')['_id']='digits'
    form_validationform2.element('input[name=f6]')['_class']='form-control'
    form_validationform2.element('input[name=f7]')['_placeholder']='f7 place_543'
    form_validationform2.element('input[name=f7]')['_id']='range'
    form_validationform2.element('input[name=f7]')['_class']='form-control'
    form_validationform2.element('input[name=f8]')['_placeholder']='f8 place_546'
    form_validationform2.element('input[name=f8]')['_id']='agree2'
    form_validationform2.element('input[name=f8]')['_class']='form-control'
    form_validationform2.custom.submit['_type'] = 'submit'
    form_validationform2.custom.submit['_class'] = 'btn btn-primary'
    form_validationform2.custom.submit['_value'] = 'Validate'
    form_validationform2.custom.submit['_id'] = 'id547'
    form_validationform2.custom.submit['_title'] = 'submit form_validationform2'

    if form_validationform2.accepts(request,session): 
        response.flash2 = 'submitted form_validationform2' 
    elif form_validationform2.errors:
        response.flash2 = '!Errors! form_validationform2' 
    else: 
        response.flash2 = 'form_validationform2' 



    form_validationform3 = SQLFORM(db.dform_validationform3, _class = 'form-horizontal', _id= 'inline-validate' )

    form_validationform3.element('input[name=f0]')['_placeholder']='f0 place_552'
    form_validationform3.element('input[name=f0]')['_id']='required'
    form_validationform3.element('input[name=f0]')['_class']='form-control col-lg-6'
    form_validationform3.element('input[name=f1]')['_placeholder']='f1 place_555'
    form_validationform3.element('input[name=f1]')['_id']='email'
    form_validationform3.element('input[name=f1]')['_class']='form-control col-lg-6'
    form_validationform3.element('input[name=f2]')['_placeholder']='f2 place_558'
    form_validationform3.element('input[name=f2]')['_id']='password'
    form_validationform3.element('input[name=f2]')['_class']='form-control col-lg-6'
    form_validationform3.element('input[name=f3]')['_placeholder']='f3 place_561'
    form_validationform3.element('input[name=f3]')['_id']='confirm_password'
    form_validationform3.element('input[name=f3]')['_class']='form-control col-lg-6'
    form_validationform3.element('input[name=f4]')['_placeholder']='f4 place_564'
    form_validationform3.element('input[name=f4]')['_id']='date'
    form_validationform3.element('input[name=f4]')['_class']='form-control col-lg-6'
    form_validationform3.element('input[name=f5]')['_placeholder']='f5 place_567'
    form_validationform3.element('input[name=f5]')['_id']='url'
    form_validationform3.element('input[name=f5]')['_class']='form-control col-lg-6'
    form_validationform3.element('input[name=f6]')['_placeholder']='f6 place_570'
    form_validationform3.element('input[name=f6]')['_id']='agree'
    form_validationform3.element('input[name=f6]')['_class']='form-control col-lg-6'
    form_validationform3.element('input[name=f7]')['_placeholder']='f7 place_573'
    form_validationform3.element('input[name=f7]')['_id']='minsize'
    form_validationform3.element('input[name=f7]')['_class']='form-control col-lg-6'
    form_validationform3.element('input[name=f8]')['_placeholder']='f8 place_576'
    form_validationform3.element('input[name=f8]')['_id']='maxsize'
    form_validationform3.element('input[name=f8]')['_class']='form-control col-lg-6'
    form_validationform3.element('input[name=f9]')['_placeholder']='f9 place_579'
    form_validationform3.element('input[name=f9]')['_id']='minNum'
    form_validationform3.element('input[name=f9]')['_class']='form-control col-lg-6'
    form_validationform3.element('input[name=f10]')['_placeholder']='f10 place_582'
    form_validationform3.element('input[name=f10]')['_id']='maxNum'
    form_validationform3.element('input[name=f10]')['_class']='form-control col-lg-6'
    form_validationform3.custom.submit['_type'] = 'submit'
    form_validationform3.custom.submit['_class'] = 'btn btn-primary'
    form_validationform3.custom.submit['_value'] = 'Validate'
    form_validationform3.custom.submit['_id'] = 'id583'
    form_validationform3.custom.submit['_title'] = 'submit form_validationform3'

    if form_validationform3.accepts(request,session): 
        response.flash3 = 'submitted form_validationform3' 
    elif form_validationform3.errors:
        response.flash3 = '!Errors! form_validationform3' 
    else: 
        response.flash3 = 'form_validationform3' 


    return dict( DICT= rows_dict, form_validationform0= form_validationform0, form_validationform1= form_validationform1, form_validationform2= form_validationform2, form_validationform3= form_validationform3, )