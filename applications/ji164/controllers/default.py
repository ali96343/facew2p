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
def peity():

    qu= db.dpeity.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/peity.html'


    peityform0 = SQLFORM(db.dpeityform0, _class = '', _id= 'idUnk0' )

    peityform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    peityform0.element('input[name=f0]')['_class']='form-control'
    peityform0.element('input[name=f0]')['_id']='id657'
    peityform0.custom.submit['_id'] = 'id659'
    peityform0.custom.submit['_title'] = 'submit peityform0'

    if peityform0.accepts(request,session): 
        response.flash0 = 'submitted peityform0' 
    elif peityform0.errors:
        response.flash0 = '!Errors! peityform0' 
    else: 
        response.flash0 = 'peityform0' 


    return dict( DICT= rows_dict, peityform0= peityform0, )

#@auth.requires_login()
def pdf_viewer():

    qu= db.dpdf0viewer.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/pdf-viewer.html'


    pdf_viewerform0 = SQLFORM(db.dpdf_viewerform0, _class = '', _id= 'idUnk0' )

    pdf_viewerform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    pdf_viewerform0.element('input[name=f0]')['_class']='form-control'
    pdf_viewerform0.element('input[name=f0]')['_id']='id662'
    pdf_viewerform0.custom.submit['_id'] = 'id664'
    pdf_viewerform0.custom.submit['_title'] = 'submit pdf_viewerform0'

    if pdf_viewerform0.accepts(request,session): 
        response.flash0 = 'submitted pdf_viewerform0' 
    elif pdf_viewerform0.errors:
        response.flash0 = '!Errors! pdf_viewerform0' 
    else: 
        response.flash0 = 'pdf_viewerform0' 


    return dict( DICT= rows_dict, pdf_viewerform0= pdf_viewerform0, )

#@auth.requires_login()
def tree_view():

    qu= db.dtree0view.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/tree-view.html'


    tree_viewform0 = SQLFORM(db.dtree_viewform0, _class = '', _id= 'idUnk0' )

    tree_viewform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    tree_viewform0.element('input[name=f0]')['_class']='form-control'
    tree_viewform0.element('input[name=f0]')['_id']='id642'
    tree_viewform0.custom.submit['_id'] = 'id644'
    tree_viewform0.custom.submit['_title'] = 'submit tree_viewform0'

    if tree_viewform0.accepts(request,session): 
        response.flash0 = 'submitted tree_viewform0' 
    elif tree_viewform0.errors:
        response.flash0 = '!Errors! tree_viewform0' 
    else: 
        response.flash0 = 'tree_viewform0' 


    return dict( DICT= rows_dict, tree_viewform0= tree_viewform0, )

#@auth.requires_login()
def google_map():

    qu= db.dgoogle0map.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/google-map.html'


    google_mapform0 = SQLFORM(db.dgoogle_mapform0, _class = '', _id= 'idUnk0' )

    google_mapform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    google_mapform0.element('input[name=f0]')['_class']='form-control'
    google_mapform0.element('input[name=f0]')['_id']='id610'
    google_mapform0.custom.submit['_id'] = 'id612'
    google_mapform0.custom.submit['_title'] = 'submit google_mapform0'

    if google_mapform0.accepts(request,session): 
        response.flash0 = 'submitted google_mapform0' 
    elif google_mapform0.errors:
        response.flash0 = '!Errors! google_mapform0' 
    else: 
        response.flash0 = 'google_mapform0' 


    return dict( DICT= rows_dict, google_mapform0= google_mapform0, )

#@auth.requires_login()
def blog():

    qu= db.dblog.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/blog.html'


    blogform0 = SQLFORM(db.dblogform0, _class = '', _id= 'idUnk0' )

    blogform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    blogform0.element('input[name=f0]')['_class']='form-control'
    blogform0.element('input[name=f0]')['_id']='id201'
    blogform0.custom.submit['_id'] = 'id203'
    blogform0.custom.submit['_title'] = 'submit blogform0'

    if blogform0.accepts(request,session): 
        response.flash0 = 'submitted blogform0' 
    elif blogform0.errors:
        response.flash0 = '!Errors! blogform0' 
    else: 
        response.flash0 = 'blogform0' 


    return dict( DICT= rows_dict, blogform0= blogform0, )

#@auth.requires_login()
def data_maps():

    qu= db.ddata0maps.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/data-maps.html'


    data_mapsform0 = SQLFORM(db.ddata_mapsform0, _class = '', _id= 'idUnk0' )

    data_mapsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    data_mapsform0.element('input[name=f0]')['_class']='form-control'
    data_mapsform0.element('input[name=f0]')['_id']='id99'
    data_mapsform0.custom.submit['_id'] = 'id101'
    data_mapsform0.custom.submit['_title'] = 'submit data_mapsform0'

    if data_mapsform0.accepts(request,session): 
        response.flash0 = 'submitted data_mapsform0' 
    elif data_mapsform0.errors:
        response.flash0 = '!Errors! data_mapsform0' 
    else: 
        response.flash0 = 'data_mapsform0' 


    return dict( DICT= rows_dict, data_mapsform0= data_mapsform0, )

#@auth.requires_login()
def rounded_chart():

    qu= db.drounded0chart.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/rounded-chart.html'


    rounded_chartform0 = SQLFORM(db.drounded_chartform0, _class = '', _id= 'idUnk0' )

    rounded_chartform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    rounded_chartform0.element('input[name=f0]')['_class']='form-control'
    rounded_chartform0.element('input[name=f0]')['_id']='id615'
    rounded_chartform0.custom.submit['_id'] = 'id617'
    rounded_chartform0.custom.submit['_title'] = 'submit rounded_chartform0'

    if rounded_chartform0.accepts(request,session): 
        response.flash0 = 'submitted rounded_chartform0' 
    elif rounded_chartform0.errors:
        response.flash0 = '!Errors! rounded_chartform0' 
    else: 
        response.flash0 = 'rounded_chartform0' 


    return dict( DICT= rows_dict, rounded_chartform0= rounded_chartform0, )

#@auth.requires_login()
def X404():

    qu= db.d404.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/404.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def index_1():

    qu= db.dindex01.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index-1.html'


    index_1form0 = SQLFORM(db.dindex_1form0, _class = '', _id= 'idUnk0' )

    index_1form0.element('input[name=f0]')['_placeholder']='f0 Search...'
    index_1form0.element('input[name=f0]')['_class']='form-control'
    index_1form0.element('input[name=f0]')['_id']='id94'
    index_1form0.custom.submit['_id'] = 'id96'
    index_1form0.custom.submit['_title'] = 'submit index_1form0'

    if index_1form0.accepts(request,session): 
        response.flash0 = 'submitted index_1form0' 
    elif index_1form0.errors:
        response.flash0 = '!Errors! index_1form0' 
    else: 
        response.flash0 = 'index_1form0' 


    return dict( DICT= rows_dict, index_1form0= index_1form0, )

#@auth.requires_login()
def product_edit():

    qu= db.dproduct0edit.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/product-edit.html'


    product_editform0 = SQLFORM(db.dproduct_editform0, _class = '', _id= 'idUnk0' )

    product_editform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    product_editform0.element('input[name=f0]')['_class']='form-control'
    product_editform0.element('input[name=f0]')['_id']='id169'
    product_editform0.custom.submit['_id'] = 'id171'
    product_editform0.custom.submit['_title'] = 'submit product_editform0'

    if product_editform0.accepts(request,session): 
        response.flash0 = 'submitted product_editform0' 
    elif product_editform0.errors:
        response.flash0 = '!Errors! product_editform0' 
    else: 
        response.flash0 = 'product_editform0' 



    product_editform1 = SQLFORM(db.dproduct_editform1, _class = 'classUnk1', _id= 'idUnk1' )

    product_editform1.custom.submit['_class'] = 'unk-class'
    product_editform1.custom.submit['_type'] = 'submit'
    product_editform1.custom.submit['_name'] = 'radio'
    product_editform1.custom.submit['_value'] = 'submit radio'
    product_editform1.custom.submit['_id'] = 'unk-id'
    product_editform1.custom.submit['_title'] = 'submit product_editform1'

    if product_editform1.accepts(request,session): 
        response.flash1 = 'submitted product_editform1' 
    elif product_editform1.errors:
        response.flash1 = '!Errors! product_editform1' 
    else: 
        response.flash1 = 'product_editform1' 



    product_editform2 = SQLFORM(db.dproduct_editform2, _class = 'classUnk2', _id= 'idUnk2' )

    product_editform2.custom.submit['_class'] = 'unk-class'
    product_editform2.custom.submit['_type'] = 'submit'
    product_editform2.custom.submit['_name'] = 'radio'
    product_editform2.custom.submit['_value'] = 'submit radio'
    product_editform2.custom.submit['_id'] = 'unk-id'
    product_editform2.custom.submit['_title'] = 'submit product_editform2'

    if product_editform2.accepts(request,session): 
        response.flash2 = 'submitted product_editform2' 
    elif product_editform2.errors:
        response.flash2 = '!Errors! product_editform2' 
    else: 
        response.flash2 = 'product_editform2' 



    product_editform3 = SQLFORM(db.dproduct_editform3, _class = 'classUnk3', _id= 'idUnk3' )

    product_editform3.custom.submit['_class'] = 'unk-class'
    product_editform3.custom.submit['_type'] = 'submit'
    product_editform3.custom.submit['_name'] = 'radio'
    product_editform3.custom.submit['_value'] = 'submit radio'
    product_editform3.custom.submit['_id'] = 'unk-id'
    product_editform3.custom.submit['_title'] = 'submit product_editform3'

    if product_editform3.accepts(request,session): 
        response.flash3 = 'submitted product_editform3' 
    elif product_editform3.errors:
        response.flash3 = '!Errors! product_editform3' 
    else: 
        response.flash3 = 'product_editform3' 


    return dict( DICT= rows_dict, product_editform0= product_editform0, product_editform1= product_editform1, product_editform2= product_editform2, product_editform3= product_editform3, )

#@auth.requires_login()
def bar_charts():

    qu= db.dbar0charts.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/bar-charts.html'


    bar_chartsform0 = SQLFORM(db.dbar_chartsform0, _class = '', _id= 'idUnk0' )

    bar_chartsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    bar_chartsform0.element('input[name=f0]')['_class']='form-control'
    bar_chartsform0.element('input[name=f0]')['_id']='id724'
    bar_chartsform0.custom.submit['_id'] = 'id726'
    bar_chartsform0.custom.submit['_title'] = 'submit bar_chartsform0'

    if bar_chartsform0.accepts(request,session): 
        response.flash0 = 'submitted bar_chartsform0' 
    elif bar_chartsform0.errors:
        response.flash0 = '!Errors! bar_chartsform0' 
    else: 
        response.flash0 = 'bar_chartsform0' 


    return dict( DICT= rows_dict, bar_chartsform0= bar_chartsform0, )

#@auth.requires_login()
def mailbox_compose():

    qu= db.dmailbox0compose.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/mailbox-compose.html'


    mailbox_composeform0 = SQLFORM(db.dmailbox_composeform0, _class = '', _id= 'idUnk0' )

    mailbox_composeform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    mailbox_composeform0.element('input[name=f0]')['_class']='form-control'
    mailbox_composeform0.element('input[name=f0]')['_id']='id630'
    mailbox_composeform0.custom.submit['_id'] = 'id632'
    mailbox_composeform0.custom.submit['_title'] = 'submit mailbox_composeform0'

    if mailbox_composeform0.accepts(request,session): 
        response.flash0 = 'submitted mailbox_composeform0' 
    elif mailbox_composeform0.errors:
        response.flash0 = '!Errors! mailbox_composeform0' 
    else: 
        response.flash0 = 'mailbox_composeform0' 



    mailbox_composeform1 = SQLFORM(db.dmailbox_composeform1, _class = 'form-horizontal', _id= 'idUnk1' )

    mailbox_composeform1.element('input[name=f0]')['_placeholder']='f0 example@email.com'
    mailbox_composeform1.element('input[name=f0]')['_class']='form-control input-sm'
    mailbox_composeform1.element('input[name=f0]')['_id']='id635'
    mailbox_composeform1.element('input[name=f1]')['_placeholder']='f1 place_639'
    mailbox_composeform1.element('input[name=f1]')['_class']='form-control input-sm'
    mailbox_composeform1.element('input[name=f1]')['_id']='id637'
    mailbox_composeform1.element('input[name=f2]')['_placeholder']='f2 Enter Email subject'
    mailbox_composeform1.element('input[name=f2]')['_class']='form-control input-sm'
    mailbox_composeform1.element('input[name=f2]')['_id']='id640'
    mailbox_composeform1.custom.submit['_type'] = 'submit'
    mailbox_composeform1.custom.submit['_class'] = 'unk-class'
    mailbox_composeform1.custom.submit['_value'] = 'submit input'
    mailbox_composeform1.custom.submit['_id'] = 'unk-id'
    mailbox_composeform1.custom.submit['_title'] = 'submit mailbox_composeform1'

    if mailbox_composeform1.accepts(request,session): 
        response.flash1 = 'submitted mailbox_composeform1' 
    elif mailbox_composeform1.errors:
        response.flash1 = '!Errors! mailbox_composeform1' 
    else: 
        response.flash1 = 'mailbox_composeform1' 


    return dict( DICT= rows_dict, mailbox_composeform0= mailbox_composeform0, mailbox_composeform1= mailbox_composeform1, )

#@auth.requires_login()
def buttons():

    qu= db.dbuttons.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/buttons.html'


    buttonsform0 = SQLFORM(db.dbuttonsform0, _class = '', _id= 'idUnk0' )

    buttonsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    buttonsform0.element('input[name=f0]')['_class']='form-control'
    buttonsform0.element('input[name=f0]')['_id']='id53'
    buttonsform0.custom.submit['_id'] = 'id55'
    buttonsform0.custom.submit['_title'] = 'submit buttonsform0'

    if buttonsform0.accepts(request,session): 
        response.flash0 = 'submitted buttonsform0' 
    elif buttonsform0.errors:
        response.flash0 = '!Errors! buttonsform0' 
    else: 
        response.flash0 = 'buttonsform0' 


    return dict( DICT= rows_dict, buttonsform0= buttonsform0, )

#@auth.requires_login()
def tinymc():

    qu= db.dtinymc.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/tinymc.html'


    tinymcform0 = SQLFORM(db.dtinymcform0, _class = '', _id= 'idUnk0' )

    tinymcform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    tinymcform0.element('input[name=f0]')['_class']='form-control'
    tinymcform0.element('input[name=f0]')['_id']='id719'
    tinymcform0.custom.submit['_id'] = 'id721'
    tinymcform0.custom.submit['_title'] = 'submit tinymcform0'

    if tinymcform0.accepts(request,session): 
        response.flash0 = 'submitted tinymcform0' 
    elif tinymcform0.errors:
        response.flash0 = '!Errors! tinymcform0' 
    else: 
        response.flash0 = 'tinymcform0' 


    return dict( DICT= rows_dict, tinymcform0= tinymcform0, )

#@auth.requires_login()
def line_charts():

    qu= db.dline0charts.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/line-charts.html'


    line_chartsform0 = SQLFORM(db.dline_chartsform0, _class = '', _id= 'idUnk0' )

    line_chartsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    line_chartsform0.element('input[name=f0]')['_class']='form-control'
    line_chartsform0.element('input[name=f0]')['_id']='id559'
    line_chartsform0.custom.submit['_id'] = 'id561'
    line_chartsform0.custom.submit['_title'] = 'submit line_chartsform0'

    if line_chartsform0.accepts(request,session): 
        response.flash0 = 'submitted line_chartsform0' 
    elif line_chartsform0.errors:
        response.flash0 = '!Errors! line_chartsform0' 
    else: 
        response.flash0 = 'line_chartsform0' 


    return dict( DICT= rows_dict, line_chartsform0= line_chartsform0, )

#@auth.requires_login()
def sparkline():

    qu= db.dsparkline.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/sparkline.html'


    sparklineform0 = SQLFORM(db.dsparklineform0, _class = '', _id= 'idUnk0' )

    sparklineform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    sparklineform0.element('input[name=f0]')['_class']='form-control'
    sparklineform0.element('input[name=f0]')['_id']='id652'
    sparklineform0.custom.submit['_id'] = 'id654'
    sparklineform0.custom.submit['_title'] = 'submit sparklineform0'

    if sparklineform0.accepts(request,session): 
        response.flash0 = 'submitted sparklineform0' 
    elif sparklineform0.errors:
        response.flash0 = '!Errors! sparklineform0' 
    else: 
        response.flash0 = 'sparklineform0' 


    return dict( DICT= rows_dict, sparklineform0= sparklineform0, )

#@auth.requires_login()
def password_recovery():

    qu= db.dpassword0recovery.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/password-recovery.html'


    password_recoveryform0 = SQLFORM(db.dpassword_recoveryform0, _class = 'classUnk0', _id= 'loginForm' )

    password_recoveryform0.element('input[name=f0]')['_placeholder']='f0 example@gmail.com'
    password_recoveryform0.element('input[name=f0]')['_id']='username'
    password_recoveryform0.element('input[name=f0]')['_value']='unk_581'
    password_recoveryform0.element('input[name=f0]')['_class']='form-control'
    password_recoveryform0.custom.submit['_type'] = 'submit'
    password_recoveryform0.custom.submit['_class'] = 'btn btn-success btn-block'
    password_recoveryform0.custom.submit['_value'] = 'Reset password'
    password_recoveryform0.custom.submit['_id'] = 'id582'
    password_recoveryform0.custom.submit['_title'] = 'submit password_recoveryform0'

    if password_recoveryform0.accepts(request,session): 
        response.flash0 = 'submitted password_recoveryform0' 
    elif password_recoveryform0.errors:
        response.flash0 = '!Errors! password_recoveryform0' 
    else: 
        response.flash0 = 'password_recoveryform0' 


    return dict( DICT= rows_dict, password_recoveryform0= password_recoveryform0, )

#@auth.requires_login()
def lock():

    qu= db.dlock.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/lock.html'


    lockform0 = SQLFORM(db.dlockform0, _class = 'm-t', _id= 'idUnk0' )

    lockform0.element('input[name=f0]')['_placeholder']='f0 ******'
    lockform0.element('input[name=f0]')['_class']='form-control'
    lockform0.element('input[name=f0]')['_id']='id554'
    lockform0.custom.submit['_type'] = 'submit'
    lockform0.custom.submit['_class'] = 'btn btn-primary block full-width'
    lockform0.custom.submit['_value'] = 'Unlock'
    lockform0.custom.submit['_id'] = 'id556'
    lockform0.custom.submit['_title'] = 'submit lockform0'

    if lockform0.accepts(request,session): 
        response.flash0 = 'submitted lockform0' 
    elif lockform0.errors:
        response.flash0 = '!Errors! lockform0' 
    else: 
        response.flash0 = 'lockform0' 


    return dict( DICT= rows_dict, lockform0= lockform0, )

#@auth.requires_login()
def password_meter():

    qu= db.dpassword0meter.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/password-meter.html'


    password_meterform0 = SQLFORM(db.dpassword_meterform0, _class = '', _id= 'idUnk0' )

    password_meterform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    password_meterform0.element('input[name=f0]')['_class']='form-control'
    password_meterform0.element('input[name=f0]')['_id']='id605'
    password_meterform0.custom.submit['_id'] = 'id607'
    password_meterform0.custom.submit['_title'] = 'submit password_meterform0'

    if password_meterform0.accepts(request,session): 
        response.flash0 = 'submitted password_meterform0' 
    elif password_meterform0.errors:
        response.flash0 = '!Errors! password_meterform0' 
    else: 
        response.flash0 = 'password_meterform0' 


    return dict( DICT= rows_dict, password_meterform0= password_meterform0, )

#@auth.requires_login()
def product_cart():

    qu= db.dproduct0cart.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/product-cart.html'


    product_cartform0 = SQLFORM(db.dproduct_cartform0, _class = '', _id= 'idUnk0' )

    product_cartform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    product_cartform0.element('input[name=f0]')['_class']='form-control'
    product_cartform0.element('input[name=f0]')['_id']='id89'
    product_cartform0.custom.submit['_id'] = 'id91'
    product_cartform0.custom.submit['_title'] = 'submit product_cartform0'

    if product_cartform0.accepts(request,session): 
        response.flash0 = 'submitted product_cartform0' 
    elif product_cartform0.errors:
        response.flash0 = '!Errors! product_cartform0' 
    else: 
        response.flash0 = 'product_cartform0' 


    return dict( DICT= rows_dict, product_cartform0= product_cartform0, )

#@auth.requires_login()
def login():

    qu= db.dlogin.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/login.html'


    loginform0 = SQLFORM(db.dloginform0, _class = 'classUnk0', _id= 'loginForm' )

    loginform0.element('input[name=f0]')['_placeholder']='f0 example@gmail.com'
    loginform0.element('input[name=f0]')['_id']='username'
    loginform0.element('input[name=f0]')['_value']='unk_145'
    loginform0.element('input[name=f0]')['_class']='form-control'
    loginform0.element('input[name=f1]')['_placeholder']='f1 ******'
    loginform0.element('input[name=f1]')['_id']='password'
    loginform0.element('input[name=f1]')['_value']='unk_148'
    loginform0.element('input[name=f1]')['_class']='form-control'
    loginform0.element('input[name=f2]')['_placeholder']='f2 place_152'
    loginform0.element('input[name=f2]')['_class']='i-checks'
    loginform0.element('input[name=f2]')['_id']='id149'
    loginform0.custom.submit['_type'] = 'submit'
    loginform0.custom.submit['_class'] = 'btn btn-success btn-block loginbtn'
    loginform0.custom.submit['_value'] = 'Login'
    loginform0.custom.submit['_id'] = 'id153'
    loginform0.custom.submit['_title'] = 'submit loginform0'
    loginform0.custom.submit['_class'] = 'btn btn-default btn-block'
    loginform0.custom.submit['_id'] = 'id156'
    loginform0.custom.submit['_title'] = 'submit loginform0'

    if loginform0.accepts(request,session): 
        response.flash0 = 'submitted loginform0' 
    elif loginform0.errors:
        response.flash0 = '!Errors! loginform0' 
    else: 
        response.flash0 = 'loginform0' 


    return dict( DICT= rows_dict, loginform0= loginform0, )

#@auth.requires_login()
def product_list():

    qu= db.dproduct0list.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/product-list.html'


    product_listform0 = SQLFORM(db.dproduct_listform0, _class = '', _id= 'idUnk0' )

    product_listform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    product_listform0.element('input[name=f0]')['_class']='form-control'
    product_listform0.element('input[name=f0]')['_id']='id164'
    product_listform0.custom.submit['_id'] = 'id166'
    product_listform0.custom.submit['_title'] = 'submit product_listform0'

    if product_listform0.accepts(request,session): 
        response.flash0 = 'submitted product_listform0' 
    elif product_listform0.errors:
        response.flash0 = '!Errors! product_listform0' 
    else: 
        response.flash0 = 'product_listform0' 


    return dict( DICT= rows_dict, product_listform0= product_listform0, )

#@auth.requires_login()
def multi_upload():

    qu= db.dmulti0upload.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/multi-upload.html'


    multi_uploadform0 = SQLFORM(db.dmulti_uploadform0, _class = '', _id= 'idUnk0' )

    multi_uploadform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    multi_uploadform0.element('input[name=f0]')['_class']='form-control'
    multi_uploadform0.element('input[name=f0]')['_id']='id625'
    multi_uploadform0.custom.submit['_id'] = 'id627'
    multi_uploadform0.custom.submit['_title'] = 'submit multi_uploadform0'

    if multi_uploadform0.accepts(request,session): 
        response.flash0 = 'submitted multi_uploadform0' 
    elif multi_uploadform0.errors:
        response.flash0 = '!Errors! multi_uploadform0' 
    else: 
        response.flash0 = 'multi_uploadform0' 


    return dict( DICT= rows_dict, multi_uploadform0= multi_uploadform0, )

#@auth.requires_login()
def c3():

    qu= db.dc3.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/c3.html'


    c3form0 = SQLFORM(db.dc3form0, _class = '', _id= 'idUnk0' )

    c3form0.element('input[name=f0]')['_placeholder']='f0 Search...'
    c3form0.element('input[name=f0]')['_class']='form-control'
    c3form0.element('input[name=f0]')['_id']='id585'
    c3form0.custom.submit['_id'] = 'id587'
    c3form0.custom.submit['_title'] = 'submit c3form0'

    if c3form0.accepts(request,session): 
        response.flash0 = 'submitted c3form0' 
    elif c3form0.errors:
        response.flash0 = '!Errors! c3form0' 
    else: 
        response.flash0 = 'c3form0' 


    return dict( DICT= rows_dict, c3form0= c3form0, )

#@auth.requires_login()
def static_table():

    qu= db.dstatic0table.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/static-table.html'


    static_tableform0 = SQLFORM(db.dstatic_tableform0, _class = '', _id= 'idUnk0' )

    static_tableform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    static_tableform0.element('input[name=f0]')['_class']='form-control'
    static_tableform0.element('input[name=f0]')['_id']='id590'
    static_tableform0.custom.submit['_id'] = 'id592'
    static_tableform0.custom.submit['_title'] = 'submit static_tableform0'

    if static_tableform0.accepts(request,session): 
        response.flash0 = 'submitted static_tableform0' 
    elif static_tableform0.errors:
        response.flash0 = '!Errors! static_tableform0' 
    else: 
        response.flash0 = 'static_tableform0' 


    return dict( DICT= rows_dict, static_tableform0= static_tableform0, )

#@auth.requires_login()
def advance_form_element():

    qu= db.dadvance0form0element.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/advance-form-element.html'


    advance_form_elementform0 = SQLFORM(db.dadvance_form_elementform0, _class = '', _id= 'idUnk0' )

    advance_form_elementform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    advance_form_elementform0.element('input[name=f0]')['_class']='form-control'
    advance_form_elementform0.element('input[name=f0]')['_id']='id701'
    advance_form_elementform0.custom.submit['_id'] = 'id703'
    advance_form_elementform0.custom.submit['_title'] = 'submit advance_form_elementform0'

    if advance_form_elementform0.accepts(request,session): 
        response.flash0 = 'submitted advance_form_elementform0' 
    elif advance_form_elementform0.errors:
        response.flash0 = '!Errors! advance_form_elementform0' 
    else: 
        response.flash0 = 'advance_form_elementform0' 


    return dict( DICT= rows_dict, advance_form_elementform0= advance_form_elementform0, )

#@auth.requires_login()
def product_detail():

    qu= db.dproduct0detail.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/product-detail.html'


    product_detailform0 = SQLFORM(db.dproduct_detailform0, _class = '', _id= 'idUnk0' )

    product_detailform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    product_detailform0.element('input[name=f0]')['_class']='form-control'
    product_detailform0.element('input[name=f0]')['_id']='id600'
    product_detailform0.custom.submit['_id'] = 'id602'
    product_detailform0.custom.submit['_title'] = 'submit product_detailform0'

    if product_detailform0.accepts(request,session): 
        response.flash0 = 'submitted product_detailform0' 
    elif product_detailform0.errors:
        response.flash0 = '!Errors! product_detailform0' 
    else: 
        response.flash0 = 'product_detailform0' 


    return dict( DICT= rows_dict, product_detailform0= product_detailform0, )

#@auth.requires_login()
def notifications():

    qu= db.dnotifications.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/notifications.html'


    notificationsform0 = SQLFORM(db.dnotificationsform0, _class = '', _id= 'idUnk0' )

    notificationsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    notificationsform0.element('input[name=f0]')['_class']='form-control'
    notificationsform0.element('input[name=f0]')['_id']='id691'
    notificationsform0.custom.submit['_id'] = 'id693'
    notificationsform0.custom.submit['_title'] = 'submit notificationsform0'

    if notificationsform0.accepts(request,session): 
        response.flash0 = 'submitted notificationsform0' 
    elif notificationsform0.errors:
        response.flash0 = '!Errors! notificationsform0' 
    else: 
        response.flash0 = 'notificationsform0' 


    return dict( DICT= rows_dict, notificationsform0= notificationsform0, )

#@auth.requires_login()
def dual_list_box():

    qu= db.ddual0list0box.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/dual-list-box.html'


    dual_list_boxform0 = SQLFORM(db.ddual_list_boxform0, _class = '', _id= 'idUnk0' )

    dual_list_boxform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    dual_list_boxform0.element('input[name=f0]')['_class']='form-control'
    dual_list_boxform0.element('input[name=f0]')['_id']='id711'
    dual_list_boxform0.custom.submit['_id'] = 'id713'
    dual_list_boxform0.custom.submit['_title'] = 'submit dual_list_boxform0'

    if dual_list_boxform0.accepts(request,session): 
        response.flash0 = 'submitted dual_list_boxform0' 
    elif dual_list_boxform0.errors:
        response.flash0 = '!Errors! dual_list_boxform0' 
    else: 
        response.flash0 = 'dual_list_boxform0' 



    dual_list_boxform1 = SQLFORM(db.ddual_list_boxform1, _class = 'wizard-big', _id= 'form' )

    dual_list_boxform1.custom.submit['_type'] = 'submit'
    dual_list_boxform1.custom.submit['_class'] = 'unk-class'
    dual_list_boxform1.custom.submit['_value'] = 'submit select'
    dual_list_boxform1.custom.submit['_id'] = 'unk-id'
    dual_list_boxform1.custom.submit['_title'] = 'submit dual_list_boxform1'

    if dual_list_boxform1.accepts(request,session): 
        response.flash1 = 'submitted dual_list_boxform1' 
    elif dual_list_boxform1.errors:
        response.flash1 = '!Errors! dual_list_boxform1' 
    else: 
        response.flash1 = 'dual_list_boxform1' 


    return dict( DICT= rows_dict, dual_list_boxform0= dual_list_boxform0, dual_list_boxform1= dual_list_boxform1, )

#@auth.requires_login()
def index():

    qu= db.dindex.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index.html'


    indexform0 = SQLFORM(db.dindexform0, _class = '', _id= 'idUnk0' )

    indexform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    indexform0.element('input[name=f0]')['_class']='form-control'
    indexform0.element('input[name=f0]')['_id']='id696'
    indexform0.custom.submit['_id'] = 'id698'
    indexform0.custom.submit['_title'] = 'submit indexform0'

    if indexform0.accepts(request,session): 
        response.flash0 = 'submitted indexform0' 
    elif indexform0.errors:
        response.flash0 = '!Errors! indexform0' 
    else: 
        response.flash0 = 'indexform0' 


    return dict( DICT= rows_dict, indexform0= indexform0, )

#@auth.requires_login()
def accordion():

    qu= db.daccordion.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/accordion.html'


    accordionform0 = SQLFORM(db.daccordionform0, _class = '', _id= 'idUnk0' )

    accordionform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    accordionform0.element('input[name=f0]')['_class']='form-control'
    accordionform0.element('input[name=f0]')['_id']='id84'
    accordionform0.custom.submit['_id'] = 'id86'
    accordionform0.custom.submit['_title'] = 'submit accordionform0'

    if accordionform0.accepts(request,session): 
        response.flash0 = 'submitted accordionform0' 
    elif accordionform0.errors:
        response.flash0 = '!Errors! accordionform0' 
    else: 
        response.flash0 = 'accordionform0' 


    return dict( DICT= rows_dict, accordionform0= accordionform0, )

#@auth.requires_login()
def file_manager():

    qu= db.dfile0manager.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/file-manager.html'


    file_managerform0 = SQLFORM(db.dfile_managerform0, _class = '', _id= 'idUnk0' )

    file_managerform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    file_managerform0.element('input[name=f0]')['_class']='form-control'
    file_managerform0.element('input[name=f0]')['_id']='id706'
    file_managerform0.custom.submit['_id'] = 'id708'
    file_managerform0.custom.submit['_title'] = 'submit file_managerform0'

    if file_managerform0.accepts(request,session): 
        response.flash0 = 'submitted file_managerform0' 
    elif file_managerform0.errors:
        response.flash0 = '!Errors! file_managerform0' 
    else: 
        response.flash0 = 'file_managerform0' 


    return dict( DICT= rows_dict, file_managerform0= file_managerform0, )

#@auth.requires_login()
def preloader():

    qu= db.dpreloader.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/preloader.html'


    preloaderform0 = SQLFORM(db.dpreloaderform0, _class = '', _id= 'idUnk0' )

    preloaderform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    preloaderform0.element('input[name=f0]')['_class']='form-control'
    preloaderform0.element('input[name=f0]')['_id']='id620'
    preloaderform0.custom.submit['_id'] = 'id622'
    preloaderform0.custom.submit['_title'] = 'submit preloaderform0'

    if preloaderform0.accepts(request,session): 
        response.flash0 = 'submitted preloaderform0' 
    elif preloaderform0.errors:
        response.flash0 = '!Errors! preloaderform0' 
    else: 
        response.flash0 = 'preloaderform0' 


    return dict( DICT= rows_dict, preloaderform0= preloaderform0, )

#@auth.requires_login()
def tabs():

    qu= db.dtabs.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/tabs.html'


    tabsform0 = SQLFORM(db.dtabsform0, _class = '', _id= 'idUnk0' )

    tabsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    tabsform0.element('input[name=f0]')['_class']='form-control'
    tabsform0.element('input[name=f0]')['_id']='id595'
    tabsform0.custom.submit['_id'] = 'id597'
    tabsform0.custom.submit['_title'] = 'submit tabsform0'

    if tabsform0.accepts(request,session): 
        response.flash0 = 'submitted tabsform0' 
    elif tabsform0.errors:
        response.flash0 = '!Errors! tabsform0' 
    else: 
        response.flash0 = 'tabsform0' 


    return dict( DICT= rows_dict, tabsform0= tabsform0, )

#@auth.requires_login()
def alerts():

    qu= db.dalerts.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/alerts.html'


    alertsform0 = SQLFORM(db.dalertsform0, _class = '', _id= 'idUnk0' )

    alertsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    alertsform0.element('input[name=f0]')['_class']='form-control'
    alertsform0.element('input[name=f0]')['_id']='id159'
    alertsform0.custom.submit['_id'] = 'id161'
    alertsform0.custom.submit['_title'] = 'submit alertsform0'

    if alertsform0.accepts(request,session): 
        response.flash0 = 'submitted alertsform0' 
    elif alertsform0.errors:
        response.flash0 = '!Errors! alertsform0' 
    else: 
        response.flash0 = 'alertsform0' 


    return dict( DICT= rows_dict, alertsform0= alertsform0, )

#@auth.requires_login()
def index_2():

    qu= db.dindex02.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index-2.html'


    index_2form0 = SQLFORM(db.dindex_2form0, _class = '', _id= 'idUnk0' )

    index_2form0.element('input[name=f0]')['_placeholder']='f0 Search...'
    index_2form0.element('input[name=f0]')['_class']='form-control'
    index_2form0.element('input[name=f0]')['_id']='id74'
    index_2form0.custom.submit['_id'] = 'id76'
    index_2form0.custom.submit['_title'] = 'submit index_2form0'

    if index_2form0.accepts(request,session): 
        response.flash0 = 'submitted index_2form0' 
    elif index_2form0.errors:
        response.flash0 = '!Errors! index_2form0' 
    else: 
        response.flash0 = 'index_2form0' 


    return dict( DICT= rows_dict, index_2form0= index_2form0, )

#@auth.requires_login()
def blog_details():

    qu= db.dblog0details.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/blog-details.html'


    blog_detailsform0 = SQLFORM(db.dblog_detailsform0, _class = '', _id= 'idUnk0' )

    blog_detailsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    blog_detailsform0.element('input[name=f0]')['_class']='form-control'
    blog_detailsform0.element('input[name=f0]')['_id']='id677'
    blog_detailsform0.custom.submit['_id'] = 'id679'
    blog_detailsform0.custom.submit['_title'] = 'submit blog_detailsform0'

    if blog_detailsform0.accepts(request,session): 
        response.flash0 = 'submitted blog_detailsform0' 
    elif blog_detailsform0.errors:
        response.flash0 = '!Errors! blog_detailsform0' 
    else: 
        response.flash0 = 'blog_detailsform0' 



    blog_detailsform1 = SQLFORM(db.dblog_detailsform1, _class = 'classUnk1', _id= 'idUnk1' )

    blog_detailsform1.element('input[name=f0]')['_placeholder']='f0 Name*'
    blog_detailsform1.element('input[name=f0]')['_class']='responsive-mg-b-10'
    blog_detailsform1.element('input[name=f0]')['_id']='id682'
    blog_detailsform1.element('input[name=f1]')['_placeholder']='f1 Email*'
    blog_detailsform1.element('input[name=f1]')['_id']='id684'
    blog_detailsform1.custom.submit['_type'] = 'submit'
    blog_detailsform1.custom.submit['_id'] = 'id686'
    blog_detailsform1.custom.submit['_value'] = 'Send'
    blog_detailsform1.custom.submit['_title'] = 'submit blog_detailsform1'
    blog_detailsform1.element('textarea[name=f2]')['_rows']='10'
    blog_detailsform1.element('textarea[name=f2]')['_placeholder']='f2 Message'
    blog_detailsform1.element('textarea[name=f2]')['_id']='id689'

    if blog_detailsform1.accepts(request,session): 
        response.flash1 = 'submitted blog_detailsform1' 
    elif blog_detailsform1.errors:
        response.flash1 = '!Errors! blog_detailsform1' 
    else: 
        response.flash1 = 'blog_detailsform1' 


    return dict( DICT= rows_dict, blog_detailsform0= blog_detailsform0, blog_detailsform1= blog_detailsform1, )

#@auth.requires_login()
def images_cropper():

    qu= db.dimages0cropper.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/images-cropper.html'


    images_cropperform0 = SQLFORM(db.dimages_cropperform0, _class = '', _id= 'idUnk0' )

    images_cropperform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    images_cropperform0.element('input[name=f0]')['_class']='form-control'
    images_cropperform0.element('input[name=f0]')['_id']='id672'
    images_cropperform0.custom.submit['_id'] = 'id674'
    images_cropperform0.custom.submit['_title'] = 'submit images_cropperform0'

    if images_cropperform0.accepts(request,session): 
        response.flash0 = 'submitted images_cropperform0' 
    elif images_cropperform0.errors:
        response.flash0 = '!Errors! images_cropperform0' 
    else: 
        response.flash0 = 'images_cropperform0' 


    return dict( DICT= rows_dict, images_cropperform0= images_cropperform0, )

#@auth.requires_login()
def x_editable():

    qu= db.dx0editable.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/x-editable.html'


    x_editableform0 = SQLFORM(db.dx_editableform0, _class = '', _id= 'idUnk0' )

    x_editableform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    x_editableform0.element('input[name=f0]')['_class']='form-control'
    x_editableform0.element('input[name=f0]')['_id']='id647'
    x_editableform0.custom.submit['_id'] = 'id649'
    x_editableform0.custom.submit['_title'] = 'submit x_editableform0'

    if x_editableform0.accepts(request,session): 
        response.flash0 = 'submitted x_editableform0' 
    elif x_editableform0.errors:
        response.flash0 = '!Errors! x_editableform0' 
    else: 
        response.flash0 = 'x_editableform0' 


    return dict( DICT= rows_dict, x_editableform0= x_editableform0, )

#@auth.requires_login()
def code_editor():

    qu= db.dcode0editor.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/code-editor.html'


    code_editorform0 = SQLFORM(db.dcode_editorform0, _class = '', _id= 'idUnk0' )

    code_editorform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    code_editorform0.element('input[name=f0]')['_class']='form-control'
    code_editorform0.element('input[name=f0]')['_id']='id569'
    code_editorform0.custom.submit['_id'] = 'id571'
    code_editorform0.custom.submit['_title'] = 'submit code_editorform0'

    if code_editorform0.accepts(request,session): 
        response.flash0 = 'submitted code_editorform0' 
    elif code_editorform0.errors:
        response.flash0 = '!Errors! code_editorform0' 
    else: 
        response.flash0 = 'code_editorform0' 


    return dict( DICT= rows_dict, code_editorform0= code_editorform0, )

#@auth.requires_login()
def data_table():

    qu= db.ddata0table.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/data-table.html'


    data_tableform0 = SQLFORM(db.ddata_tableform0, _class = '', _id= 'idUnk0' )

    data_tableform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    data_tableform0.element('input[name=f0]')['_class']='form-control'
    data_tableform0.element('input[name=f0]')['_id']='id667'
    data_tableform0.custom.submit['_id'] = 'id669'
    data_tableform0.custom.submit['_title'] = 'submit data_tableform0'

    if data_tableform0.accepts(request,session): 
        response.flash0 = 'submitted data_tableform0' 
    elif data_tableform0.errors:
        response.flash0 = '!Errors! data_tableform0' 
    else: 
        response.flash0 = 'data_tableform0' 


    return dict( DICT= rows_dict, data_tableform0= data_tableform0, )

#@auth.requires_login()
def mailbox():

    qu= db.dmailbox.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/mailbox.html'


    mailboxform0 = SQLFORM(db.dmailboxform0, _class = '', _id= 'idUnk0' )

    mailboxform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    mailboxform0.element('input[name=f0]')['_class']='form-control'
    mailboxform0.element('input[name=f0]')['_id']='id104'
    mailboxform0.custom.submit['_id'] = 'id106'
    mailboxform0.custom.submit['_title'] = 'submit mailboxform0'

    if mailboxform0.accepts(request,session): 
        response.flash0 = 'submitted mailboxform0' 
    elif mailboxform0.errors:
        response.flash0 = '!Errors! mailboxform0' 
    else: 
        response.flash0 = 'mailboxform0' 


    return dict( DICT= rows_dict, mailboxform0= mailboxform0, )

#@auth.requires_login()
def basic_form_element():

    qu= db.dbasic0form0element.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/basic-form-element.html'


    basic_form_elementform0 = SQLFORM(db.dbasic_form_elementform0, _class = '', _id= 'idUnk0' )

    basic_form_elementform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    basic_form_elementform0.element('input[name=f0]')['_class']='form-control'
    basic_form_elementform0.element('input[name=f0]')['_id']='id206'
    basic_form_elementform0.custom.submit['_id'] = 'id208'
    basic_form_elementform0.custom.submit['_title'] = 'submit basic_form_elementform0'

    if basic_form_elementform0.accepts(request,session): 
        response.flash0 = 'submitted basic_form_elementform0' 
    elif basic_form_elementform0.errors:
        response.flash0 = '!Errors! basic_form_elementform0' 
    else: 
        response.flash0 = 'basic_form_elementform0' 



    basic_form_elementform1 = SQLFORM(db.dbasic_form_elementform1, _class = 'classUnk1', _id= 'idUnk1' )

    basic_form_elementform1.element('input[name=f0]')['_placeholder']='f0 Enter Email'
    basic_form_elementform1.element('input[name=f0]')['_class']='form-control'
    basic_form_elementform1.element('input[name=f0]')['_id']='id211'
    basic_form_elementform1.element('input[name=f1]')['_placeholder']='f1 password'
    basic_form_elementform1.element('input[name=f1]')['_class']='form-control'
    basic_form_elementform1.element('input[name=f1]')['_id']='id214'
    basic_form_elementform1.element('input[name=f2]')['_placeholder']='f2 place_220'
    basic_form_elementform1.element('input[name=f2]')['_class']='i-checks'
    basic_form_elementform1.element('input[name=f2]')['_id']='id217'
    basic_form_elementform1.custom.submit['_type'] = 'submit'
    basic_form_elementform1.custom.submit['_class'] = 'btn btn-sm btn-primary pull-right login-submit-cs'
    basic_form_elementform1.custom.submit['_value'] = 'Log In'
    basic_form_elementform1.custom.submit['_id'] = 'id221'
    basic_form_elementform1.custom.submit['_title'] = 'submit basic_form_elementform1'

    if basic_form_elementform1.accepts(request,session): 
        response.flash1 = 'submitted basic_form_elementform1' 
    elif basic_form_elementform1.errors:
        response.flash1 = '!Errors! basic_form_elementform1' 
    else: 
        response.flash1 = 'basic_form_elementform1' 



    basic_form_elementform2 = SQLFORM(db.dbasic_form_elementform2, _class = 'classUnk2', _id= 'idUnk2' )

    basic_form_elementform2.element('input[name=f0]')['_placeholder']='f0 Enter Email'
    basic_form_elementform2.element('input[name=f0]')['_class']='form-control'
    basic_form_elementform2.element('input[name=f0]')['_id']='id225'
    basic_form_elementform2.element('input[name=f1]')['_placeholder']='f1 password'
    basic_form_elementform2.element('input[name=f1]')['_class']='form-control'
    basic_form_elementform2.element('input[name=f1]')['_id']='id227'
    basic_form_elementform2.element('input[name=f2]')['_placeholder']='f2 place_232'
    basic_form_elementform2.element('input[name=f2]')['_id']='id229'
    basic_form_elementform2.custom.submit['_type'] = 'submit'
    basic_form_elementform2.custom.submit['_class'] = 'btn btn-sm btn-primary login-submit-cs'
    basic_form_elementform2.custom.submit['_value'] = 'Sign In'
    basic_form_elementform2.custom.submit['_id'] = 'id233'
    basic_form_elementform2.custom.submit['_title'] = 'submit basic_form_elementform2'

    if basic_form_elementform2.accepts(request,session): 
        response.flash2 = 'submitted basic_form_elementform2' 
    elif basic_form_elementform2.errors:
        response.flash2 = '!Errors! basic_form_elementform2' 
    else: 
        response.flash2 = 'basic_form_elementform2' 



    basic_form_elementform3 = SQLFORM(db.dbasic_form_elementform3, _class = 'classUnk3', _id= 'idUnk3' )

    basic_form_elementform3.element('input[name=f0]')['_placeholder']='f0 Enter Email'
    basic_form_elementform3.element('input[name=f0]')['_class']='form-control basic-ele-mg-b-10 responsive-mg-b-10'
    basic_form_elementform3.element('input[name=f0]')['_id']='id236'
    basic_form_elementform3.element('input[name=f1]')['_placeholder']='f1 password'
    basic_form_elementform3.element('input[name=f1]')['_class']='form-control basic-ele-mg-b-10 responsive-mg-b-10'
    basic_form_elementform3.element('input[name=f1]')['_id']='id238'
    basic_form_elementform3.element('input[name=f2]')['_placeholder']='f2 place_243'
    basic_form_elementform3.element('input[name=f2]')['_class']='i-checks'
    basic_form_elementform3.element('input[name=f2]')['_id']='id240'
    basic_form_elementform3.custom.submit['_type'] = 'submit'
    basic_form_elementform3.custom.submit['_class'] = 'btn btn-sm btn-primary login-submit-cs'
    basic_form_elementform3.custom.submit['_value'] = 'Sign In'
    basic_form_elementform3.custom.submit['_id'] = 'id244'
    basic_form_elementform3.custom.submit['_title'] = 'submit basic_form_elementform3'

    if basic_form_elementform3.accepts(request,session): 
        response.flash3 = 'submitted basic_form_elementform3' 
    elif basic_form_elementform3.errors:
        response.flash3 = '!Errors! basic_form_elementform3' 
    else: 
        response.flash3 = 'basic_form_elementform3' 



    basic_form_elementform4 = SQLFORM(db.dbasic_form_elementform4, _class = 'classUnk4', _id= 'idUnk4' )

    basic_form_elementform4.element('input[name=f0]')['_placeholder']='f0 Enter Email'
    basic_form_elementform4.element('input[name=f0]')['_class']='form-control'
    basic_form_elementform4.element('input[name=f0]')['_id']='id247'
    basic_form_elementform4.element('input[name=f1]')['_placeholder']='f1 password'
    basic_form_elementform4.element('input[name=f1]')['_class']='form-control'
    basic_form_elementform4.element('input[name=f1]')['_id']='id249'
    basic_form_elementform4.element('input[name=f2]')['_placeholder']='f2 place_254'
    basic_form_elementform4.element('input[name=f2]')['_class']='i-checks'
    basic_form_elementform4.element('input[name=f2]')['_id']='id251'
    basic_form_elementform4.custom.submit['_type'] = 'submit'
    basic_form_elementform4.custom.submit['_class'] = 'btn btn-sm btn-primary login-submit-cs'
    basic_form_elementform4.custom.submit['_value'] = 'Sign In'
    basic_form_elementform4.custom.submit['_id'] = 'id255'
    basic_form_elementform4.custom.submit['_title'] = 'submit basic_form_elementform4'

    if basic_form_elementform4.accepts(request,session): 
        response.flash4 = 'submitted basic_form_elementform4' 
    elif basic_form_elementform4.errors:
        response.flash4 = '!Errors! basic_form_elementform4' 
    else: 
        response.flash4 = 'basic_form_elementform4' 



    basic_form_elementform5 = SQLFORM(db.dbasic_form_elementform5, _class = 'classUnk5', _id= 'idUnk5' )

    basic_form_elementform5.element('input[name=f0]')['_placeholder']='f0 place_260'
    basic_form_elementform5.element('input[name=f0]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f0]')['_id']='id258'
    basic_form_elementform5.element('input[name=f1]')['_placeholder']='f1 place_263'
    basic_form_elementform5.element('input[name=f1]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f1]')['_id']='id261'
    basic_form_elementform5.element('input[name=f2]')['_placeholder']='f2 place_266'
    basic_form_elementform5.element('input[name=f2]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f2]')['_id']='id264'
    basic_form_elementform5.element('input[name=f3]')['_placeholder']='f3 place_269'
    basic_form_elementform5.element('input[name=f3]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f3]')['_id']='id267'
    basic_form_elementform5.element('input[name=f4]')['_placeholder']='f4 place_272'
    basic_form_elementform5.element('input[name=f4]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f4]')['_id']='id270'
    basic_form_elementform5.element('input[name=f5]')['_placeholder']='f5 place_275'
    basic_form_elementform5.element('input[name=f5]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f5]')['_id']='id273'
    basic_form_elementform5.element('input[name=f6]')['_placeholder']='f6 Placeholder'
    basic_form_elementform5.element('input[name=f6]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f6]')['_id']='id276'
    basic_form_elementform5.element('input[name=f7]')['_placeholder']='f7 Disabled input here...'
    basic_form_elementform5.element('input[name=f7]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f7]')['_id']='id278'
    basic_form_elementform5.element('input[name=f8]')['_placeholder']='f8 place_282'
    basic_form_elementform5.element('input[name=f8]')['_class']='pull-left'
    basic_form_elementform5.element('input[name=f8]')['_id']='id280'
    basic_form_elementform5.element('input[name=f11]')['_placeholder']='f11 place_290'
    basic_form_elementform5.element('input[name=f11]')['_class']='pull-left radio-checked'
    basic_form_elementform5.element('input[name=f11]')['_id']='id287'
    basic_form_elementform5.element('input[name=f12]')['_placeholder']='f12 place_294'
    basic_form_elementform5.element('input[name=f12]')['_class']='pull-left radio-checked'
    basic_form_elementform5.element('input[name=f12]')['_id']='id291'
    basic_form_elementform5.element('input[name=f13]')['_placeholder']='f13 place_298'
    basic_form_elementform5.element('input[name=f13]')['_class']='pull-left radio-checked'
    basic_form_elementform5.element('input[name=f13]')['_id']='id295'
    basic_form_elementform5.element('input[name=f14]')['_placeholder']='f14 place_303'
    basic_form_elementform5.element('input[name=f14]')['_id']='id299'
    basic_form_elementform5.element('input[name=f14]')['_value']='unk_302'
    basic_form_elementform5.element('input[name=f15]')['_placeholder']='f15 place_308'
    basic_form_elementform5.element('input[name=f15]')['_id']='id304'
    basic_form_elementform5.element('input[name=f15]')['_value']='unk_307'
    basic_form_elementform5.element('input[name=f16]')['_placeholder']='f16 place_313'
    basic_form_elementform5.element('input[name=f16]')['_id']='id309'
    basic_form_elementform5.element('input[name=f16]')['_value']='unk_312'
    basic_form_elementform5.element('input[name=f17]')['_placeholder']='f17 place_318'
    basic_form_elementform5.element('input[name=f17]')['_id']='id314'
    basic_form_elementform5.element('input[name=f17]')['_value']='unk_317'
    basic_form_elementform5.element('input[name=f22]')['_placeholder']='f22 place_335'
    basic_form_elementform5.element('input[name=f22]')['_id']='inlineCheckbox1'
    basic_form_elementform5.element('input[name=f22]')['_value']='option1'
    basic_form_elementform5.element('input[name=f23]')['_placeholder']='f23 place_339'
    basic_form_elementform5.element('input[name=f23]')['_id']='inlineCheckbox2'
    basic_form_elementform5.element('input[name=f23]')['_value']='option2'
    basic_form_elementform5.element('input[name=f24]')['_placeholder']='f24 place_343'
    basic_form_elementform5.element('input[name=f24]')['_id']='inlineCheckbox3'
    basic_form_elementform5.element('input[name=f24]')['_value']='option3'
    basic_form_elementform5.element('input[name=f25]')['_placeholder']='f25 place_346'
    basic_form_elementform5.element('input[name=f25]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f25]')['_id']='id344'
    basic_form_elementform5.element('input[name=f26]')['_placeholder']='f26 place_349'
    basic_form_elementform5.element('input[name=f26]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f26]')['_id']='id347'
    basic_form_elementform5.element('input[name=f27]')['_placeholder']='f27 place_352'
    basic_form_elementform5.element('input[name=f27]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f27]')['_id']='id350'
    basic_form_elementform5.element('input[name=f28]')['_placeholder']='f28 .input-lg'
    basic_form_elementform5.element('input[name=f28]')['_class']='form-control input-lg'
    basic_form_elementform5.element('input[name=f28]')['_id']='id353'
    basic_form_elementform5.element('input[name=f29]')['_placeholder']='f29 Default input'
    basic_form_elementform5.element('input[name=f29]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f29]')['_id']='id355'
    basic_form_elementform5.element('input[name=f30]')['_placeholder']='f30 .input-sm'
    basic_form_elementform5.element('input[name=f30]')['_class']='form-control input-sm'
    basic_form_elementform5.element('input[name=f30]')['_id']='id357'
    basic_form_elementform5.element('input[name=f31]')['_placeholder']='f31 .col-md-2'
    basic_form_elementform5.element('input[name=f31]')['_class']='form-control basic-ele-mg-b-10'
    basic_form_elementform5.element('input[name=f31]')['_id']='id359'
    basic_form_elementform5.element('input[name=f32]')['_placeholder']='f32 .col-md-4'
    basic_form_elementform5.element('input[name=f32]')['_class']='form-control basic-ele-mg-b-10'
    basic_form_elementform5.element('input[name=f32]')['_id']='id361'
    basic_form_elementform5.element('input[name=f33]')['_placeholder']='f33 .col-md-6'
    basic_form_elementform5.element('input[name=f33]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f33]')['_id']='id363'
    basic_form_elementform5.element('input[name=f34]')['_placeholder']='f34 Username'
    basic_form_elementform5.element('input[name=f34]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f34]')['_id']='id365'
    basic_form_elementform5.element('input[name=f35]')['_placeholder']='f35 place_369'
    basic_form_elementform5.element('input[name=f35]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f35]')['_id']='id367'
    basic_form_elementform5.element('input[name=f36]')['_placeholder']='f36 place_372'
    basic_form_elementform5.element('input[name=f36]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f36]')['_id']='id370'
    basic_form_elementform5.element('input[name=f37]')['_placeholder']='f37 place_375'
    basic_form_elementform5.element('input[name=f37]')['_id']='id373'
    basic_form_elementform5.element('input[name=f38]')['_placeholder']='f38 place_378'
    basic_form_elementform5.element('input[name=f38]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f38]')['_id']='id376'
    basic_form_elementform5.element('input[name=f40]')['_placeholder']='f40 place_384'
    basic_form_elementform5.element('input[name=f40]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f40]')['_id']='id382'
    basic_form_elementform5.element('input[name=f41]')['_placeholder']='f41 place_387'
    basic_form_elementform5.element('input[name=f41]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f41]')['_id']='id385'
    basic_form_elementform5.element('input[name=f42]')['_placeholder']='f42 .custom-go-button'
    basic_form_elementform5.element('input[name=f42]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f42]')['_id']='id388'
    basic_form_elementform5.element('input[name=f43]')['_placeholder']='f43 place_392'
    basic_form_elementform5.element('input[name=f43]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f43]')['_id']='id390'
    basic_form_elementform5.element('input[name=f44]')['_placeholder']='f44 place_395'
    basic_form_elementform5.element('input[name=f44]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f44]')['_id']='id393'
    basic_form_elementform5.element('input[name=f45]')['_placeholder']='f45 .custom-dropdowns-button'
    basic_form_elementform5.element('input[name=f45]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f45]')['_id']='id396'
    basic_form_elementform5.element('input[name=f46]')['_placeholder']='f46 place_400'
    basic_form_elementform5.element('input[name=f46]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f46]')['_id']='id398'
    basic_form_elementform5.element('input[name=f47]')['_placeholder']='f47 place_403'
    basic_form_elementform5.element('input[name=f47]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f47]')['_id']='id401'
    basic_form_elementform5.element('input[name=f48]')['_placeholder']='f48 .dropdown-segmented'
    basic_form_elementform5.element('input[name=f48]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f48]')['_id']='id404'
    basic_form_elementform5.element('input[name=f49]')['_placeholder']='f49 place_408'
    basic_form_elementform5.element('input[name=f49]')['_class']='form-control'
    basic_form_elementform5.element('input[name=f49]')['_id']='id406'
    basic_form_elementform5.element('input[name=f50]')['_placeholder']='f50 place_411'
    basic_form_elementform5.element('input[name=f50]')['_id']='id409'
    basic_form_elementform5.element('input[name=f51]')['_placeholder']='f51 no file selected'
    basic_form_elementform5.element('input[name=f51]')['_id']='prepend-small-btn'
    basic_form_elementform5.element('input[name=f52]')['_placeholder']='f52 place_416'
    basic_form_elementform5.element('input[name=f52]')['_id']='id414'
    basic_form_elementform5.element('input[name=f53]')['_placeholder']='f53 no file selected'
    basic_form_elementform5.element('input[name=f53]')['_id']='prepend-big-btn'
    basic_form_elementform5.element('input[name=f54]')['_placeholder']='f54 place_422'
    basic_form_elementform5.element('input[name=f54]')['_id']='id420'
    basic_form_elementform5.element('input[name=f55]')['_placeholder']='f55 no file selected'
    basic_form_elementform5.element('input[name=f55]')['_id']='append-small-btn'
    basic_form_elementform5.element('input[name=f56]')['_placeholder']='f56 place_427'
    basic_form_elementform5.element('input[name=f56]')['_id']='id425'
    basic_form_elementform5.element('input[name=f57]')['_placeholder']='f57 no file selected'
    basic_form_elementform5.element('input[name=f57]')['_id']='append-big-btn'
    basic_form_elementform5.custom.submit['_type'] = 'submit'
    basic_form_elementform5.custom.submit['_class'] = 'btn btn-primary'
    basic_form_elementform5.custom.submit['_value'] = 'Go!'
    basic_form_elementform5.custom.submit['_id'] = 'id437'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_type'] = 'submit'
    basic_form_elementform5.custom.submit['_class'] = 'btn btn-primary'
    basic_form_elementform5.custom.submit['_value'] = 'Go!'
    basic_form_elementform5.custom.submit['_id'] = 'id440'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_type'] = 'submit'
    basic_form_elementform5.custom.submit['_class'] = 'btn btn-primary'
    basic_form_elementform5.custom.submit['_value'] = 'Go!'
    basic_form_elementform5.custom.submit['_id'] = 'id443'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_type'] = 'submit'
    basic_form_elementform5.custom.submit['_class'] = 'btn btn-white dropdown-toggle'
    basic_form_elementform5.custom.submit['_value'] = 'Action'
    basic_form_elementform5.custom.submit['_id'] = 'id446'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_type'] = 'submit'
    basic_form_elementform5.custom.submit['_class'] = 'btn btn-white dropdown-toggle'
    basic_form_elementform5.custom.submit['_value'] = 'Action'
    basic_form_elementform5.custom.submit['_id'] = 'id449'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_type'] = 'submit'
    basic_form_elementform5.custom.submit['_class'] = 'btn btn-white dropdown-toggle'
    basic_form_elementform5.custom.submit['_value'] = 'Action'
    basic_form_elementform5.custom.submit['_id'] = 'id452'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_type'] = 'submit'
    basic_form_elementform5.custom.submit['_class'] = 'btn btn-white'
    basic_form_elementform5.custom.submit['_value'] = 'Action'
    basic_form_elementform5.custom.submit['_id'] = 'id455'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_type'] = 'submit'
    basic_form_elementform5.custom.submit['_class'] = 'btn btn-white dropdown-toggle'
    basic_form_elementform5.custom.submit['_value'] = 'unk_460'
    basic_form_elementform5.custom.submit['_id'] = 'id458'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_type'] = 'submit'
    basic_form_elementform5.custom.submit['_class'] = 'btn btn-white'
    basic_form_elementform5.custom.submit['_value'] = 'Action'
    basic_form_elementform5.custom.submit['_id'] = 'id462'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_type'] = 'submit'
    basic_form_elementform5.custom.submit['_class'] = 'btn btn-white dropdown-toggle'
    basic_form_elementform5.custom.submit['_value'] = 'unk_467'
    basic_form_elementform5.custom.submit['_id'] = 'id465'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_type'] = 'submit'
    basic_form_elementform5.custom.submit['_class'] = 'btn btn-white'
    basic_form_elementform5.custom.submit['_value'] = 'Action'
    basic_form_elementform5.custom.submit['_id'] = 'id469'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_type'] = 'submit'
    basic_form_elementform5.custom.submit['_class'] = 'btn btn-white dropdown-toggle'
    basic_form_elementform5.custom.submit['_value'] = 'unk_474'
    basic_form_elementform5.custom.submit['_id'] = 'id472'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_type'] = 'submit'
    basic_form_elementform5.custom.submit['_class'] = 'btn btn-white'
    basic_form_elementform5.custom.submit['_value'] = 'Cancel'
    basic_form_elementform5.custom.submit['_id'] = 'id476'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_type'] = 'submit'
    basic_form_elementform5.custom.submit['_class'] = 'btn btn-sm btn-primary login-submit-cs'
    basic_form_elementform5.custom.submit['_value'] = 'Save Change'
    basic_form_elementform5.custom.submit['_id'] = 'id479'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id482'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id485'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id488'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id491'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id494'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id497'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id500'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id503'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id506'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id509'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id512'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id515'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id518'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id521'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id524'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id527'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id530'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id533'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id536'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id539'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id542'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id545'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id548'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'
    basic_form_elementform5.custom.submit['_id'] = 'id551'
    basic_form_elementform5.custom.submit['_title'] = 'submit basic_form_elementform5'

    if basic_form_elementform5.accepts(request,session): 
        response.flash5 = 'submitted basic_form_elementform5' 
    elif basic_form_elementform5.errors:
        response.flash5 = '!Errors! basic_form_elementform5' 
    else: 
        response.flash5 = 'basic_form_elementform5' 


    return dict( DICT= rows_dict, basic_form_elementform0= basic_form_elementform0, basic_form_elementform1= basic_form_elementform1, basic_form_elementform2= basic_form_elementform2, basic_form_elementform3= basic_form_elementform3, basic_form_elementform4= basic_form_elementform4, basic_form_elementform5= basic_form_elementform5, )

#@auth.requires_login()
def widgets():

    qu= db.dwidgets.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/widgets.html'


    widgetsform0 = SQLFORM(db.dwidgetsform0, _class = '', _id= 'idUnk0' )

    widgetsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    widgetsform0.element('input[name=f0]')['_class']='form-control'
    widgetsform0.element('input[name=f0]')['_id']='id79'
    widgetsform0.custom.submit['_id'] = 'id81'
    widgetsform0.custom.submit['_title'] = 'submit widgetsform0'

    if widgetsform0.accepts(request,session): 
        response.flash0 = 'submitted widgetsform0' 
    elif widgetsform0.errors:
        response.flash0 = '!Errors! widgetsform0' 
    else: 
        response.flash0 = 'widgetsform0' 


    return dict( DICT= rows_dict, widgetsform0= widgetsform0, )

#@auth.requires_login()
def mailbox_view():

    qu= db.dmailbox0view.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/mailbox-view.html'


    mailbox_viewform0 = SQLFORM(db.dmailbox_viewform0, _class = '', _id= 'idUnk0' )

    mailbox_viewform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    mailbox_viewform0.element('input[name=f0]')['_class']='form-control'
    mailbox_viewform0.element('input[name=f0]')['_id']='id729'
    mailbox_viewform0.custom.submit['_id'] = 'id731'
    mailbox_viewform0.custom.submit['_title'] = 'submit mailbox_viewform0'

    if mailbox_viewform0.accepts(request,session): 
        response.flash0 = 'submitted mailbox_viewform0' 
    elif mailbox_viewform0.errors:
        response.flash0 = '!Errors! mailbox_viewform0' 
    else: 
        response.flash0 = 'mailbox_viewform0' 


    return dict( DICT= rows_dict, mailbox_viewform0= mailbox_viewform0, )

#@auth.requires_login()
def area_charts():

    qu= db.darea0charts.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/area-charts.html'


    area_chartsform0 = SQLFORM(db.darea_chartsform0, _class = '', _id= 'idUnk0' )

    area_chartsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    area_chartsform0.element('input[name=f0]')['_class']='form-control'
    area_chartsform0.element('input[name=f0]')['_id']='id138'
    area_chartsform0.custom.submit['_id'] = 'id140'
    area_chartsform0.custom.submit['_title'] = 'submit area_chartsform0'

    if area_chartsform0.accepts(request,session): 
        response.flash0 = 'submitted area_chartsform0' 
    elif area_chartsform0.errors:
        response.flash0 = '!Errors! area_chartsform0' 
    else: 
        response.flash0 = 'area_chartsform0' 


    return dict( DICT= rows_dict, area_chartsform0= area_chartsform0, )

#@auth.requires_login()
def analytics():

    qu= db.danalytics.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/analytics.html'


    analyticsform0 = SQLFORM(db.danalyticsform0, _class = '', _id= 'idUnk0' )

    analyticsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    analyticsform0.element('input[name=f0]')['_class']='form-control'
    analyticsform0.element('input[name=f0]')['_id']='id574'
    analyticsform0.custom.submit['_id'] = 'id576'
    analyticsform0.custom.submit['_title'] = 'submit analyticsform0'

    if analyticsform0.accepts(request,session): 
        response.flash0 = 'submitted analyticsform0' 
    elif analyticsform0.errors:
        response.flash0 = '!Errors! analyticsform0' 
    else: 
        response.flash0 = 'analyticsform0' 


    return dict( DICT= rows_dict, analyticsform0= analyticsform0, )

#@auth.requires_login()
def register():

    qu= db.dregister.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/register.html'


    registerform0 = SQLFORM(db.dregisterform0, _class = 'classUnk0', _id= 'loginForm' )

    registerform0.element('input[name=f0]')['_placeholder']='f0 place_112'
    registerform0.element('input[name=f0]')['_class']='form-control'
    registerform0.element('input[name=f0]')['_id']='id109'
    registerform0.element('input[name=f1]')['_placeholder']='f1 place_116'
    registerform0.element('input[name=f1]')['_class']='form-control'
    registerform0.element('input[name=f1]')['_id']='id113'
    registerform0.element('input[name=f2]')['_placeholder']='f2 place_120'
    registerform0.element('input[name=f2]')['_class']='form-control'
    registerform0.element('input[name=f2]')['_id']='id117'
    registerform0.element('input[name=f3]')['_placeholder']='f3 place_124'
    registerform0.element('input[name=f3]')['_class']='form-control'
    registerform0.element('input[name=f3]')['_id']='id121'
    registerform0.element('input[name=f4]')['_placeholder']='f4 place_128'
    registerform0.element('input[name=f4]')['_class']='form-control'
    registerform0.element('input[name=f4]')['_id']='id125'
    registerform0.element('input[name=f5]')['_placeholder']='f5 place_131'
    registerform0.element('input[name=f5]')['_class']='i-checks'
    registerform0.element('input[name=f5]')['_id']='id129'
    registerform0.custom.submit['_type'] = 'submit'
    registerform0.custom.submit['_class'] = 'btn btn-success loginbtn'
    registerform0.custom.submit['_value'] = 'Register'
    registerform0.custom.submit['_id'] = 'id132'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.custom.submit['_type'] = 'submit'
    registerform0.custom.submit['_class'] = 'btn btn-default'
    registerform0.custom.submit['_value'] = 'Cancel'
    registerform0.custom.submit['_id'] = 'id135'
    registerform0.custom.submit['_title'] = 'submit registerform0'

    if registerform0.accepts(request,session): 
        response.flash0 = 'submitted registerform0' 
    elif registerform0.errors:
        response.flash0 = '!Errors! registerform0' 
    else: 
        response.flash0 = 'registerform0' 


    return dict( DICT= rows_dict, registerform0= registerform0, )

#@auth.requires_login()
def modals():

    qu= db.dmodals.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/modals.html'


    modalsform0 = SQLFORM(db.dmodalsform0, _class = '', _id= 'idUnk0' )

    modalsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    modalsform0.element('input[name=f0]')['_class']='form-control'
    modalsform0.element('input[name=f0]')['_id']='id564'
    modalsform0.custom.submit['_id'] = 'id566'
    modalsform0.custom.submit['_title'] = 'submit modalsform0'

    if modalsform0.accepts(request,session): 
        response.flash0 = 'submitted modalsform0' 
    elif modalsform0.errors:
        response.flash0 = '!Errors! modalsform0' 
    else: 
        response.flash0 = 'modalsform0' 


    return dict( DICT= rows_dict, modalsform0= modalsform0, )

#@auth.requires_login()
def X500():

    qu= db.d500.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/500.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def product_payment():

    qu= db.dproduct0payment.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/product-payment.html'


    product_paymentform0 = SQLFORM(db.dproduct_paymentform0, _class = '', _id= 'idUnk0' )

    product_paymentform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    product_paymentform0.element('input[name=f0]')['_class']='form-control'
    product_paymentform0.element('input[name=f0]')['_id']='id58'
    product_paymentform0.custom.submit['_id'] = 'id60'
    product_paymentform0.custom.submit['_title'] = 'submit product_paymentform0'

    if product_paymentform0.accepts(request,session): 
        response.flash0 = 'submitted product_paymentform0' 
    elif product_paymentform0.errors:
        response.flash0 = '!Errors! product_paymentform0' 
    else: 
        response.flash0 = 'product_paymentform0' 



    product_paymentform1 = SQLFORM(db.dproduct_paymentform1, _class = 'payment-form mg-tb-15', _id= 'idUnk1' )

    product_paymentform1.element('input[name=f0]')['_placeholder']='f0 Card Number'
    product_paymentform1.element('input[name=f0]')['_class']='form-control'
    product_paymentform1.element('input[name=f0]')['_id']='id63'
    product_paymentform1.element('input[name=f1]')['_placeholder']='f1 Full Name'
    product_paymentform1.element('input[name=f1]')['_class']='form-control'
    product_paymentform1.element('input[name=f1]')['_id']='id65'
    product_paymentform1.element('input[name=f2]')['_placeholder']='f2 MM/YY'
    product_paymentform1.element('input[name=f2]')['_class']='form-control'
    product_paymentform1.element('input[name=f2]')['_id']='id67'
    product_paymentform1.element('input[name=f3]')['_placeholder']='f3 CVC'
    product_paymentform1.element('input[name=f3]')['_class']='form-control'
    product_paymentform1.element('input[name=f3]')['_id']='id69'
    product_paymentform1.custom.submit['_class'] = 'btn btn-primary waves-effect waves-light'
    product_paymentform1.custom.submit['_id'] = 'id71'
    product_paymentform1.custom.submit['_title'] = 'submit product_paymentform1'

    if product_paymentform1.accepts(request,session): 
        response.flash1 = 'submitted product_paymentform1' 
    elif product_paymentform1.errors:
        response.flash1 = '!Errors! product_paymentform1' 
    else: 
        response.flash1 = 'product_paymentform1' 


    return dict( DICT= rows_dict, product_paymentform0= product_paymentform0, product_paymentform1= product_paymentform1, )