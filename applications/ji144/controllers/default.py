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
def ui_switches():

    qu= db.dui0switches.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/ui-switches.html'


    ui_switchesform0 = SQLFORM(db.dui_switchesform0, _class = 'search-form', _id= 'idUnk0' )

    ui_switchesform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    ui_switchesform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    ui_switchesform0.element('input[name=f0]')['_id']='id484'
    ui_switchesform0.custom.submit['_type'] = 'submit'
    ui_switchesform0.custom.submit['_class'] = 'search-close'
    ui_switchesform0.custom.submit['_value'] = 'unk_488'
    ui_switchesform0.custom.submit['_id'] = 'id486'
    ui_switchesform0.custom.submit['_title'] = 'submit ui_switchesform0'

    if ui_switchesform0.accepts(request,session): 
        response.flash0 = 'submitted ui_switchesform0' 
    elif ui_switchesform0.errors:
        response.flash0 = '!Errors! ui_switchesform0' 
    else: 
        response.flash0 = 'ui_switchesform0' 


    return dict( DICT= rows_dict, ui_switchesform0= ui_switchesform0, )

#@auth.requires_login()
def maps_gmap():

    qu= db.dmaps0gmap.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/maps-gmap.html'


    maps_gmapform0 = SQLFORM(db.dmaps_gmapform0, _class = 'search-form', _id= 'idUnk0' )

    maps_gmapform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    maps_gmapform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    maps_gmapform0.element('input[name=f0]')['_id']='id410'
    maps_gmapform0.custom.submit['_type'] = 'submit'
    maps_gmapform0.custom.submit['_class'] = 'search-close'
    maps_gmapform0.custom.submit['_value'] = 'unk_414'
    maps_gmapform0.custom.submit['_id'] = 'id412'
    maps_gmapform0.custom.submit['_title'] = 'submit maps_gmapform0'

    if maps_gmapform0.accepts(request,session): 
        response.flash0 = 'submitted maps_gmapform0' 
    elif maps_gmapform0.errors:
        response.flash0 = '!Errors! maps_gmapform0' 
    else: 
        response.flash0 = 'maps_gmapform0' 


    return dict( DICT= rows_dict, maps_gmapform0= maps_gmapform0, )

#@auth.requires_login()
def ui_progressbar():

    qu= db.dui0progressbar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/ui-progressbar.html'


    ui_progressbarform0 = SQLFORM(db.dui_progressbarform0, _class = 'search-form', _id= 'idUnk0' )

    ui_progressbarform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    ui_progressbarform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    ui_progressbarform0.element('input[name=f0]')['_id']='id385'
    ui_progressbarform0.custom.submit['_type'] = 'submit'
    ui_progressbarform0.custom.submit['_class'] = 'search-close'
    ui_progressbarform0.custom.submit['_value'] = 'unk_389'
    ui_progressbarform0.custom.submit['_id'] = 'id387'
    ui_progressbarform0.custom.submit['_title'] = 'submit ui_progressbarform0'

    if ui_progressbarform0.accepts(request,session): 
        response.flash0 = 'submitted ui_progressbarform0' 
    elif ui_progressbarform0.errors:
        response.flash0 = '!Errors! ui_progressbarform0' 
    else: 
        response.flash0 = 'ui_progressbarform0' 


    return dict( DICT= rows_dict, ui_progressbarform0= ui_progressbarform0, )

#@auth.requires_login()
def font_fontawesome():

    qu= db.dfont0fontawesome.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/font-fontawesome.html'


    font_fontawesomeform0 = SQLFORM(db.dfont_fontawesomeform0, _class = 'search-form', _id= 'idUnk0' )

    font_fontawesomeform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    font_fontawesomeform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    font_fontawesomeform0.element('input[name=f0]')['_id']='id466'
    font_fontawesomeform0.custom.submit['_type'] = 'submit'
    font_fontawesomeform0.custom.submit['_class'] = 'search-close'
    font_fontawesomeform0.custom.submit['_value'] = 'unk_470'
    font_fontawesomeform0.custom.submit['_id'] = 'id468'
    font_fontawesomeform0.custom.submit['_title'] = 'submit font_fontawesomeform0'

    if font_fontawesomeform0.accepts(request,session): 
        response.flash0 = 'submitted font_fontawesomeform0' 
    elif font_fontawesomeform0.errors:
        response.flash0 = '!Errors! font_fontawesomeform0' 
    else: 
        response.flash0 = 'font_fontawesomeform0' 


    return dict( DICT= rows_dict, font_fontawesomeform0= font_fontawesomeform0, )

#@auth.requires_login()
def ui_tabs():

    qu= db.dui0tabs.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/ui-tabs.html'


    ui_tabsform0 = SQLFORM(db.dui_tabsform0, _class = 'search-form', _id= 'idUnk0' )

    ui_tabsform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    ui_tabsform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    ui_tabsform0.element('input[name=f0]')['_id']='id472'
    ui_tabsform0.custom.submit['_type'] = 'submit'
    ui_tabsform0.custom.submit['_class'] = 'search-close'
    ui_tabsform0.custom.submit['_value'] = 'unk_476'
    ui_tabsform0.custom.submit['_id'] = 'id474'
    ui_tabsform0.custom.submit['_title'] = 'submit ui_tabsform0'

    if ui_tabsform0.accepts(request,session): 
        response.flash0 = 'submitted ui_tabsform0' 
    elif ui_tabsform0.errors:
        response.flash0 = '!Errors! ui_tabsform0' 
    else: 
        response.flash0 = 'ui_tabsform0' 


    return dict( DICT= rows_dict, ui_tabsform0= ui_tabsform0, )

#@auth.requires_login()
def page_register():

    qu= db.dpage0register.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/page-register.html'


    page_registerform0 = SQLFORM(db.dpage_registerform0, _class = 'classUnk0', _id= 'idUnk0' )

    page_registerform0.element('input[name=f0]')['_placeholder']='f0 User Name'
    page_registerform0.element('input[name=f0]')['_class']='form-control'
    page_registerform0.element('input[name=f0]')['_id']='id428'
    page_registerform0.element('input[name=f1]')['_placeholder']='f1 Email'
    page_registerform0.element('input[name=f1]')['_class']='form-control'
    page_registerform0.element('input[name=f1]')['_id']='id431'
    page_registerform0.element('input[name=f2]')['_placeholder']='f2 Password'
    page_registerform0.element('input[name=f2]')['_class']='form-control'
    page_registerform0.element('input[name=f2]')['_id']='id434'
    page_registerform0.element('input[name=f3]')['_placeholder']='f3 place_440'
    page_registerform0.element('input[name=f3]')['_id']='id437'
    page_registerform0.custom.submit['_type'] = 'submit'
    page_registerform0.custom.submit['_class'] = 'btn btn-primary btn-flat m-b-30 m-t-30'
    page_registerform0.custom.submit['_value'] = 'Register'
    page_registerform0.custom.submit['_id'] = 'id441'
    page_registerform0.custom.submit['_title'] = 'submit page_registerform0'
    page_registerform0.custom.submit['_type'] = 'submit'
    page_registerform0.custom.submit['_class'] = 'btn social facebook btn-flat btn-addon mb-3'
    page_registerform0.custom.submit['_value'] = 'Register with facebook'
    page_registerform0.custom.submit['_id'] = 'id445'
    page_registerform0.custom.submit['_title'] = 'submit page_registerform0'
    page_registerform0.custom.submit['_type'] = 'submit'
    page_registerform0.custom.submit['_class'] = 'btn social twitter btn-flat btn-addon mt-2'
    page_registerform0.custom.submit['_value'] = 'Register with twitter'
    page_registerform0.custom.submit['_id'] = 'id448'
    page_registerform0.custom.submit['_title'] = 'submit page_registerform0'
    page_registerform0.custom.submit['_id'] = 'id451'
    page_registerform0.custom.submit['_title'] = 'submit page_registerform0'

    if page_registerform0.accepts(request,session): 
        response.flash0 = 'submitted page_registerform0' 
    elif page_registerform0.errors:
        response.flash0 = '!Errors! page_registerform0' 
    else: 
        response.flash0 = 'page_registerform0' 


    return dict( DICT= rows_dict, page_registerform0= page_registerform0, )

#@auth.requires_login()
def charts_peity():

    qu= db.dcharts0peity.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/charts-peity.html'


    charts_peityform0 = SQLFORM(db.dcharts_peityform0, _class = 'search-form', _id= 'idUnk0' )

    charts_peityform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    charts_peityform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    charts_peityform0.element('input[name=f0]')['_id']='id322'
    charts_peityform0.custom.submit['_type'] = 'submit'
    charts_peityform0.custom.submit['_class'] = 'search-close'
    charts_peityform0.custom.submit['_value'] = 'unk_326'
    charts_peityform0.custom.submit['_id'] = 'id324'
    charts_peityform0.custom.submit['_title'] = 'submit charts_peityform0'

    if charts_peityform0.accepts(request,session): 
        response.flash0 = 'submitted charts_peityform0' 
    elif charts_peityform0.errors:
        response.flash0 = '!Errors! charts_peityform0' 
    else: 
        response.flash0 = 'charts_peityform0' 


    return dict( DICT= rows_dict, charts_peityform0= charts_peityform0, )

#@auth.requires_login()
def font_themify():

    qu= db.dfont0themify.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/font-themify.html'


    font_themifyform0 = SQLFORM(db.dfont_themifyform0, _class = 'search-form', _id= 'idUnk0' )

    font_themifyform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    font_themifyform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    font_themifyform0.element('input[name=f0]')['_id']='id398'
    font_themifyform0.custom.submit['_type'] = 'submit'
    font_themifyform0.custom.submit['_class'] = 'search-close'
    font_themifyform0.custom.submit['_value'] = 'unk_402'
    font_themifyform0.custom.submit['_id'] = 'id400'
    font_themifyform0.custom.submit['_title'] = 'submit font_themifyform0'

    if font_themifyform0.accepts(request,session): 
        response.flash0 = 'submitted font_themifyform0' 
    elif font_themifyform0.errors:
        response.flash0 = '!Errors! font_themifyform0' 
    else: 
        response.flash0 = 'font_themifyform0' 


    return dict( DICT= rows_dict, font_themifyform0= font_themifyform0, )

#@auth.requires_login()
def index():

    qu= db.dindex.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index.html'


    indexform0 = SQLFORM(db.dindexform0, _class = 'search-form', _id= 'idUnk0' )

    indexform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    indexform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    indexform0.element('input[name=f0]')['_id']='id460'
    indexform0.custom.submit['_type'] = 'submit'
    indexform0.custom.submit['_class'] = 'search-close'
    indexform0.custom.submit['_value'] = 'unk_464'
    indexform0.custom.submit['_id'] = 'id462'
    indexform0.custom.submit['_title'] = 'submit indexform0'

    if indexform0.accepts(request,session): 
        response.flash0 = 'submitted indexform0' 
    elif indexform0.errors:
        response.flash0 = '!Errors! indexform0' 
    else: 
        response.flash0 = 'indexform0' 


    return dict( DICT= rows_dict, indexform0= indexform0, )

#@auth.requires_login()
def frame():

    qu= db.dframe.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/frame.html'


    frameform0 = SQLFORM(db.dframeform0, _class = 'search-form', _id= 'idUnk0' )

    frameform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    frameform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    frameform0.element('input[name=f0]')['_id']='id346'
    frameform0.custom.submit['_type'] = 'submit'
    frameform0.custom.submit['_class'] = 'search-close'
    frameform0.custom.submit['_value'] = 'unk_350'
    frameform0.custom.submit['_id'] = 'id348'
    frameform0.custom.submit['_title'] = 'submit frameform0'

    if frameform0.accepts(request,session): 
        response.flash0 = 'submitted frameform0' 
    elif frameform0.errors:
        response.flash0 = '!Errors! frameform0' 
    else: 
        response.flash0 = 'frameform0' 


    return dict( DICT= rows_dict, frameform0= frameform0, )

#@auth.requires_login()
def forms_advanced():

    qu= db.dforms0advanced.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/forms-advanced.html'


    forms_advancedform0 = SQLFORM(db.dforms_advancedform0, _class = 'search-form', _id= 'idUnk0' )

    forms_advancedform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    forms_advancedform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    forms_advancedform0.element('input[name=f0]')['_id']='id404'
    forms_advancedform0.custom.submit['_type'] = 'submit'
    forms_advancedform0.custom.submit['_class'] = 'search-close'
    forms_advancedform0.custom.submit['_value'] = 'unk_408'
    forms_advancedform0.custom.submit['_id'] = 'id406'
    forms_advancedform0.custom.submit['_title'] = 'submit forms_advancedform0'

    if forms_advancedform0.accepts(request,session): 
        response.flash0 = 'submitted forms_advancedform0' 
    elif forms_advancedform0.errors:
        response.flash0 = '!Errors! forms_advancedform0' 
    else: 
        response.flash0 = 'forms_advancedform0' 


    return dict( DICT= rows_dict, forms_advancedform0= forms_advancedform0, )

#@auth.requires_login()
def charts_chartjs():

    qu= db.dcharts0chartjs.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/charts-chartjs.html'


    charts_chartjsform0 = SQLFORM(db.dcharts_chartjsform0, _class = 'search-form', _id= 'idUnk0' )

    charts_chartjsform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    charts_chartjsform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    charts_chartjsform0.element('input[name=f0]')['_id']='id340'
    charts_chartjsform0.custom.submit['_type'] = 'submit'
    charts_chartjsform0.custom.submit['_class'] = 'search-close'
    charts_chartjsform0.custom.submit['_value'] = 'unk_344'
    charts_chartjsform0.custom.submit['_id'] = 'id342'
    charts_chartjsform0.custom.submit['_title'] = 'submit charts_chartjsform0'

    if charts_chartjsform0.accepts(request,session): 
        response.flash0 = 'submitted charts_chartjsform0' 
    elif charts_chartjsform0.errors:
        response.flash0 = '!Errors! charts_chartjsform0' 
    else: 
        response.flash0 = 'charts_chartjsform0' 


    return dict( DICT= rows_dict, charts_chartjsform0= charts_chartjsform0, )

#@auth.requires_login()
def maps_vector():

    qu= db.dmaps0vector.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/maps-vector.html'


    maps_vectorform0 = SQLFORM(db.dmaps_vectorform0, _class = 'search-form', _id= 'idUnk0' )

    maps_vectorform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    maps_vectorform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    maps_vectorform0.element('input[name=f0]')['_id']='id310'
    maps_vectorform0.custom.submit['_type'] = 'submit'
    maps_vectorform0.custom.submit['_class'] = 'search-close'
    maps_vectorform0.custom.submit['_value'] = 'unk_314'
    maps_vectorform0.custom.submit['_id'] = 'id312'
    maps_vectorform0.custom.submit['_title'] = 'submit maps_vectorform0'

    if maps_vectorform0.accepts(request,session): 
        response.flash0 = 'submitted maps_vectorform0' 
    elif maps_vectorform0.errors:
        response.flash0 = '!Errors! maps_vectorform0' 
    else: 
        response.flash0 = 'maps_vectorform0' 


    return dict( DICT= rows_dict, maps_vectorform0= maps_vectorform0, )

#@auth.requires_login()
def pages_forget():

    qu= db.dpages0forget.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/pages-forget.html'


    pages_forgetform0 = SQLFORM(db.dpages_forgetform0, _class = 'classUnk0', _id= 'idUnk0' )

    pages_forgetform0.element('input[name=f0]')['_placeholder']='f0 Email'
    pages_forgetform0.element('input[name=f0]')['_class']='form-control'
    pages_forgetform0.element('input[name=f0]')['_id']='id391'
    pages_forgetform0.custom.submit['_type'] = 'submit'
    pages_forgetform0.custom.submit['_class'] = 'btn btn-primary btn-flat m-b-15'
    pages_forgetform0.custom.submit['_value'] = 'Submit'
    pages_forgetform0.custom.submit['_id'] = 'id394'
    pages_forgetform0.custom.submit['_title'] = 'submit pages_forgetform0'

    if pages_forgetform0.accepts(request,session): 
        response.flash0 = 'submitted pages_forgetform0' 
    elif pages_forgetform0.errors:
        response.flash0 = '!Errors! pages_forgetform0' 
    else: 
        response.flash0 = 'pages_forgetform0' 


    return dict( DICT= rows_dict, pages_forgetform0= pages_forgetform0, )

#@auth.requires_login()
def tables_data():

    qu= db.dtables0data.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/tables-data.html'


    tables_dataform0 = SQLFORM(db.dtables_dataform0, _class = 'search-form', _id= 'idUnk0' )

    tables_dataform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    tables_dataform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    tables_dataform0.element('input[name=f0]')['_id']='id454'
    tables_dataform0.custom.submit['_type'] = 'submit'
    tables_dataform0.custom.submit['_class'] = 'search-close'
    tables_dataform0.custom.submit['_value'] = 'unk_458'
    tables_dataform0.custom.submit['_id'] = 'id456'
    tables_dataform0.custom.submit['_title'] = 'submit tables_dataform0'

    if tables_dataform0.accepts(request,session): 
        response.flash0 = 'submitted tables_dataform0' 
    elif tables_dataform0.errors:
        response.flash0 = '!Errors! tables_dataform0' 
    else: 
        response.flash0 = 'tables_dataform0' 


    return dict( DICT= rows_dict, tables_dataform0= tables_dataform0, )

#@auth.requires_login()
def charts_flot():

    qu= db.dcharts0flot.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/charts-flot.html'


    charts_flotform0 = SQLFORM(db.dcharts_flotform0, _class = 'search-form', _id= 'idUnk0' )

    charts_flotform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    charts_flotform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    charts_flotform0.element('input[name=f0]')['_id']='id304'
    charts_flotform0.custom.submit['_type'] = 'submit'
    charts_flotform0.custom.submit['_class'] = 'search-close'
    charts_flotform0.custom.submit['_value'] = 'unk_308'
    charts_flotform0.custom.submit['_id'] = 'id306'
    charts_flotform0.custom.submit['_title'] = 'submit charts_flotform0'

    if charts_flotform0.accepts(request,session): 
        response.flash0 = 'submitted charts_flotform0' 
    elif charts_flotform0.errors:
        response.flash0 = '!Errors! charts_flotform0' 
    else: 
        response.flash0 = 'charts_flotform0' 


    return dict( DICT= rows_dict, charts_flotform0= charts_flotform0, )

#@auth.requires_login()
def ui_badges():

    qu= db.dui0badges.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/ui-badges.html'


    ui_badgesform0 = SQLFORM(db.dui_badgesform0, _class = 'search-form', _id= 'idUnk0' )

    ui_badgesform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    ui_badgesform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    ui_badgesform0.element('input[name=f0]')['_id']='id416'
    ui_badgesform0.custom.submit['_type'] = 'submit'
    ui_badgesform0.custom.submit['_class'] = 'search-close'
    ui_badgesform0.custom.submit['_value'] = 'unk_420'
    ui_badgesform0.custom.submit['_id'] = 'id418'
    ui_badgesform0.custom.submit['_title'] = 'submit ui_badgesform0'

    if ui_badgesform0.accepts(request,session): 
        response.flash0 = 'submitted ui_badgesform0' 
    elif ui_badgesform0.errors:
        response.flash0 = '!Errors! ui_badgesform0' 
    else: 
        response.flash0 = 'ui_badgesform0' 


    return dict( DICT= rows_dict, ui_badgesform0= ui_badgesform0, )

#@auth.requires_login()
def ui_modals():

    qu= db.dui0modals.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/ui-modals.html'


    ui_modalsform0 = SQLFORM(db.dui_modalsform0, _class = 'search-form', _id= 'idUnk0' )

    ui_modalsform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    ui_modalsform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    ui_modalsform0.element('input[name=f0]')['_id']='id316'
    ui_modalsform0.custom.submit['_type'] = 'submit'
    ui_modalsform0.custom.submit['_class'] = 'search-close'
    ui_modalsform0.custom.submit['_value'] = 'unk_320'
    ui_modalsform0.custom.submit['_id'] = 'id318'
    ui_modalsform0.custom.submit['_title'] = 'submit ui_modalsform0'

    if ui_modalsform0.accepts(request,session): 
        response.flash0 = 'submitted ui_modalsform0' 
    elif ui_modalsform0.errors:
        response.flash0 = '!Errors! ui_modalsform0' 
    else: 
        response.flash0 = 'ui_modalsform0' 


    return dict( DICT= rows_dict, ui_modalsform0= ui_modalsform0, )

#@auth.requires_login()
def ui_buttons():

    qu= db.dui0buttons.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/ui-buttons.html'


    ui_buttonsform0 = SQLFORM(db.dui_buttonsform0, _class = 'search-form', _id= 'idUnk0' )

    ui_buttonsform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    ui_buttonsform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    ui_buttonsform0.element('input[name=f0]')['_id']='id334'
    ui_buttonsform0.custom.submit['_type'] = 'submit'
    ui_buttonsform0.custom.submit['_class'] = 'search-close'
    ui_buttonsform0.custom.submit['_value'] = 'unk_338'
    ui_buttonsform0.custom.submit['_id'] = 'id336'
    ui_buttonsform0.custom.submit['_title'] = 'submit ui_buttonsform0'

    if ui_buttonsform0.accepts(request,session): 
        response.flash0 = 'submitted ui_buttonsform0' 
    elif ui_buttonsform0.errors:
        response.flash0 = '!Errors! ui_buttonsform0' 
    else: 
        response.flash0 = 'ui_buttonsform0' 


    return dict( DICT= rows_dict, ui_buttonsform0= ui_buttonsform0, )

#@auth.requires_login()
def forms_basic():

    qu= db.dforms0basic.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/forms-basic.html'


    forms_basicform0 = SQLFORM(db.dforms_basicform0, _class = 'search-form', _id= 'idUnk0' )

    forms_basicform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    forms_basicform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    forms_basicform0.element('input[name=f0]')['_id']='id17'
    forms_basicform0.custom.submit['_type'] = 'submit'
    forms_basicform0.custom.submit['_class'] = 'search-close'
    forms_basicform0.custom.submit['_value'] = 'unk_21'
    forms_basicform0.custom.submit['_id'] = 'id19'
    forms_basicform0.custom.submit['_title'] = 'submit forms_basicform0'

    if forms_basicform0.accepts(request,session): 
        response.flash0 = 'submitted forms_basicform0' 
    elif forms_basicform0.errors:
        response.flash0 = '!Errors! forms_basicform0' 
    else: 
        response.flash0 = 'forms_basicform0' 



    forms_basicform1 = SQLFORM(db.dforms_basicform1, _class = 'classUnk1', _id= 'idUnk1' )

    forms_basicform1.element('input[name=f0]')['_placeholder']='f0 place_25'
    forms_basicform1.element('input[name=f0]')['_id']='cc-pament'
    forms_basicform1.element('input[name=f0]')['_value']='100.00'
    forms_basicform1.element('input[name=f0]')['_class']='form-control'
    forms_basicform1.element('input[name=f1]')['_placeholder']='f1 place_28'
    forms_basicform1.element('input[name=f1]')['_id']='cc-name'
    forms_basicform1.element('input[name=f1]')['_class']='form-control cc-name valid'
    forms_basicform1.element('input[name=f2]')['_placeholder']='f2 place_32'
    forms_basicform1.element('input[name=f2]')['_id']='cc-number'
    forms_basicform1.element('input[name=f2]')['_value']='unk_31'
    forms_basicform1.element('input[name=f2]')['_class']='form-control cc-number identified visa'
    forms_basicform1.element('input[name=f3]')['_placeholder']='f3 MM / YY'
    forms_basicform1.element('input[name=f3]')['_id']='cc-exp'
    forms_basicform1.element('input[name=f3]')['_value']='unk_35'
    forms_basicform1.element('input[name=f3]')['_class']='form-control cc-exp'
    forms_basicform1.element('input[name=f4]')['_placeholder']='f4 place_39'
    forms_basicform1.element('input[name=f4]')['_id']='x_card_code'
    forms_basicform1.element('input[name=f4]')['_value']='unk_38'
    forms_basicform1.element('input[name=f4]')['_class']='form-control cc-cvc'
    forms_basicform1.custom.submit['_type'] = 'submit'
    forms_basicform1.custom.submit['_id'] = 'payment-button'
    forms_basicform1.custom.submit['_value'] = 'Pay $100.00 Sending'
    forms_basicform1.custom.submit['_class'] = 'btn btn-lg btn-info btn-block'
    forms_basicform1.custom.submit['_title'] = 'submit forms_basicform1'

    if forms_basicform1.accepts(request,session): 
        response.flash1 = 'submitted forms_basicform1' 
    elif forms_basicform1.errors:
        response.flash1 = '!Errors! forms_basicform1' 
    else: 
        response.flash1 = 'forms_basicform1' 



    forms_basicform2 = SQLFORM(db.dforms_basicform2, _class = 'form-horizontal', _id= 'idUnk2' )

    forms_basicform2.element('input[name=f0]')['_placeholder']='f0 Text'
    forms_basicform2.element('input[name=f0]')['_id']='text-input'
    forms_basicform2.element('input[name=f0]')['_class']='form-control'
    forms_basicform2.element('input[name=f1]')['_placeholder']='f1 Enter Email'
    forms_basicform2.element('input[name=f1]')['_id']='email-input'
    forms_basicform2.element('input[name=f1]')['_class']='form-control'
    forms_basicform2.element('input[name=f2]')['_placeholder']='f2 Password'
    forms_basicform2.element('input[name=f2]')['_id']='password-input'
    forms_basicform2.element('input[name=f2]')['_class']='form-control'
    forms_basicform2.element('input[name=f3]')['_placeholder']='f3 Disabled'
    forms_basicform2.element('input[name=f3]')['_id']='disabled-input'
    forms_basicform2.element('input[name=f3]')['_class']='form-control'
    forms_basicform2.element('input[name=f10]')['_placeholder']='f10 place_65'
    forms_basicform2.element('input[name=f10]')['_id']='checkbox1'
    forms_basicform2.element('input[name=f10]')['_value']='option1'
    forms_basicform2.element('input[name=f10]')['_class']='form-check-input'
    forms_basicform2.element('input[name=f11]')['_placeholder']='f11 place_68'
    forms_basicform2.element('input[name=f11]')['_id']='checkbox2'
    forms_basicform2.element('input[name=f11]')['_value']='option2'
    forms_basicform2.element('input[name=f11]')['_class']='form-check-input'
    forms_basicform2.element('input[name=f12]')['_placeholder']='f12 place_71'
    forms_basicform2.element('input[name=f12]')['_id']='checkbox3'
    forms_basicform2.element('input[name=f12]')['_value']='option3'
    forms_basicform2.element('input[name=f12]')['_class']='form-check-input'
    forms_basicform2.element('input[name=f13]')['_placeholder']='f13 place_74'
    forms_basicform2.element('input[name=f13]')['_id']='inline-checkbox1'
    forms_basicform2.element('input[name=f13]')['_value']='option1'
    forms_basicform2.element('input[name=f13]')['_class']='form-check-input'
    forms_basicform2.element('input[name=f14]')['_placeholder']='f14 place_77'
    forms_basicform2.element('input[name=f14]')['_id']='inline-checkbox2'
    forms_basicform2.element('input[name=f14]')['_value']='option2'
    forms_basicform2.element('input[name=f14]')['_class']='form-check-input'
    forms_basicform2.element('input[name=f15]')['_placeholder']='f15 place_80'
    forms_basicform2.element('input[name=f15]')['_id']='inline-checkbox3'
    forms_basicform2.element('input[name=f15]')['_value']='option3'
    forms_basicform2.element('input[name=f15]')['_class']='form-check-input'
    forms_basicform2.element('input[name=f16]')['_placeholder']='f16 place_83'
    forms_basicform2.element('input[name=f16]')['_id']='file-input'
    forms_basicform2.element('input[name=f16]')['_class']='form-control-file'
    forms_basicform2.element('input[name=f17]')['_placeholder']='f17 place_86'
    forms_basicform2.element('input[name=f17]')['_id']='file-multiple-input'
    forms_basicform2.element('input[name=f17]')['_class']='form-control-file'
    forms_basicform2.element('textarea[name=f18]')['_rows']='9'
    forms_basicform2.element('textarea[name=f18]')['_placeholder']='f18 Content...'
    forms_basicform2.element('textarea[name=f18]')['_id']='textarea-input'
    forms_basicform2.element('textarea[name=f18]')['_class']='form-control'
    forms_basicform2.custom.submit['_type'] = 'submit'
    forms_basicform2.custom.submit['_id'] = 'unk-id'
    forms_basicform2.custom.submit['_value'] = 'submit input'
    forms_basicform2.custom.submit['_class'] = 'unk-class'
    forms_basicform2.custom.submit['_title'] = 'submit forms_basicform2'

    if forms_basicform2.accepts(request,session): 
        response.flash2 = 'submitted forms_basicform2' 
    elif forms_basicform2.errors:
        response.flash2 = '!Errors! forms_basicform2' 
    else: 
        response.flash2 = 'forms_basicform2' 



    forms_basicform3 = SQLFORM(db.dforms_basicform3, _class = 'form-inline', _id= 'idUnk3' )

    forms_basicform3.element('input[name=f0]')['_placeholder']='f0 Jane Doe'
    forms_basicform3.element('input[name=f0]')['_id']='exampleInputName2'
    forms_basicform3.element('input[name=f0]')['_class']='form-control'
    forms_basicform3.element('input[name=f1]')['_placeholder']='f1 jane.doe@example.com'
    forms_basicform3.element('input[name=f1]')['_id']='exampleInputEmail2'
    forms_basicform3.element('input[name=f1]')['_class']='form-control'
    forms_basicform3.custom.submit['_type'] = 'submit'
    forms_basicform3.custom.submit['_id'] = 'unk-id'
    forms_basicform3.custom.submit['_value'] = 'submit input'
    forms_basicform3.custom.submit['_class'] = 'unk-class'
    forms_basicform3.custom.submit['_title'] = 'submit forms_basicform3'

    if forms_basicform3.accepts(request,session): 
        response.flash3 = 'submitted forms_basicform3' 
    elif forms_basicform3.errors:
        response.flash3 = '!Errors! forms_basicform3' 
    else: 
        response.flash3 = 'forms_basicform3' 



    forms_basicform4 = SQLFORM(db.dforms_basicform4, _class = 'form-horizontal', _id= 'idUnk4' )

    forms_basicform4.element('input[name=f0]')['_placeholder']='f0 Enter Email...'
    forms_basicform4.element('input[name=f0]')['_id']='hf-email'
    forms_basicform4.element('input[name=f0]')['_class']='form-control'
    forms_basicform4.element('input[name=f1]')['_placeholder']='f1 Enter Password...'
    forms_basicform4.element('input[name=f1]')['_id']='hf-password'
    forms_basicform4.element('input[name=f1]')['_class']='form-control'
    forms_basicform4.custom.submit['_type'] = 'submit'
    forms_basicform4.custom.submit['_id'] = 'unk-id'
    forms_basicform4.custom.submit['_value'] = 'submit input'
    forms_basicform4.custom.submit['_class'] = 'unk-class'
    forms_basicform4.custom.submit['_title'] = 'submit forms_basicform4'

    if forms_basicform4.accepts(request,session): 
        response.flash4 = 'submitted forms_basicform4' 
    elif forms_basicform4.errors:
        response.flash4 = '!Errors! forms_basicform4' 
    else: 
        response.flash4 = 'forms_basicform4' 



    forms_basicform5 = SQLFORM(db.dforms_basicform5, _class = '', _id= 'idUnk5' )

    forms_basicform5.element('input[name=f0]')['_placeholder']='f0 Enter Email..'
    forms_basicform5.element('input[name=f0]')['_id']='nf-email'
    forms_basicform5.element('input[name=f0]')['_class']='form-control'
    forms_basicform5.element('input[name=f1]')['_placeholder']='f1 Enter Password..'
    forms_basicform5.element('input[name=f1]')['_id']='nf-password'
    forms_basicform5.element('input[name=f1]')['_class']='form-control'
    forms_basicform5.custom.submit['_type'] = 'submit'
    forms_basicform5.custom.submit['_id'] = 'unk-id'
    forms_basicform5.custom.submit['_value'] = 'submit input'
    forms_basicform5.custom.submit['_class'] = 'unk-class'
    forms_basicform5.custom.submit['_title'] = 'submit forms_basicform5'

    if forms_basicform5.accepts(request,session): 
        response.flash5 = 'submitted forms_basicform5' 
    elif forms_basicform5.errors:
        response.flash5 = '!Errors! forms_basicform5' 
    else: 
        response.flash5 = 'forms_basicform5' 



    forms_basicform6 = SQLFORM(db.dforms_basicform6, _class = 'form-horizontal', _id= 'idUnk6' )

    forms_basicform6.element('input[name=f0]')['_placeholder']='f0 .col-sm-3'
    forms_basicform6.element('input[name=f0]')['_class']='form-control'
    forms_basicform6.element('input[name=f0]')['_id']='id116'
    forms_basicform6.element('input[name=f1]')['_placeholder']='f1 .col-sm-4'
    forms_basicform6.element('input[name=f1]')['_class']='form-control'
    forms_basicform6.element('input[name=f1]')['_id']='id118'
    forms_basicform6.element('input[name=f2]')['_placeholder']='f2 .col-sm-5'
    forms_basicform6.element('input[name=f2]')['_class']='form-control'
    forms_basicform6.element('input[name=f2]')['_id']='id120'
    forms_basicform6.element('input[name=f3]')['_placeholder']='f3 .col-sm-6'
    forms_basicform6.element('input[name=f3]')['_class']='form-control'
    forms_basicform6.element('input[name=f3]')['_id']='id122'
    forms_basicform6.element('input[name=f4]')['_placeholder']='f4 .col-sm-7'
    forms_basicform6.element('input[name=f4]')['_class']='form-control'
    forms_basicform6.element('input[name=f4]')['_id']='id124'
    forms_basicform6.element('input[name=f5]')['_placeholder']='f5 .col-sm-8'
    forms_basicform6.element('input[name=f5]')['_class']='form-control'
    forms_basicform6.element('input[name=f5]')['_id']='id126'
    forms_basicform6.element('input[name=f6]')['_placeholder']='f6 .col-sm-9'
    forms_basicform6.element('input[name=f6]')['_class']='form-control'
    forms_basicform6.element('input[name=f6]')['_id']='id128'
    forms_basicform6.element('input[name=f7]')['_placeholder']='f7 .col-sm-10'
    forms_basicform6.element('input[name=f7]')['_class']='form-control'
    forms_basicform6.element('input[name=f7]')['_id']='id130'
    forms_basicform6.element('input[name=f8]')['_placeholder']='f8 .col-sm-11'
    forms_basicform6.element('input[name=f8]')['_class']='form-control'
    forms_basicform6.element('input[name=f8]')['_id']='id132'
    forms_basicform6.element('input[name=f9]')['_placeholder']='f9 .col-sm-12'
    forms_basicform6.element('input[name=f9]')['_class']='form-control'
    forms_basicform6.element('input[name=f9]')['_id']='id134'
    forms_basicform6.custom.submit['_type'] = 'submit'
    forms_basicform6.custom.submit['_class'] = 'unk-class'
    forms_basicform6.custom.submit['_value'] = 'submit input'
    forms_basicform6.custom.submit['_id'] = 'unk-id'
    forms_basicform6.custom.submit['_title'] = 'submit forms_basicform6'

    if forms_basicform6.accepts(request,session): 
        response.flash6 = 'submitted forms_basicform6' 
    elif forms_basicform6.errors:
        response.flash6 = '!Errors! forms_basicform6' 
    else: 
        response.flash6 = 'forms_basicform6' 



    forms_basicform7 = SQLFORM(db.dforms_basicform7, _class = 'form-horizontal', _id= 'idUnk7' )

    forms_basicform7.element('input[name=f0]')['_placeholder']='f0 .form-control-sm'
    forms_basicform7.element('input[name=f0]')['_id']='input-small'
    forms_basicform7.element('input[name=f0]')['_class']='input-sm form-control-sm form-control'
    forms_basicform7.element('input[name=f1]')['_placeholder']='f1 Normal'
    forms_basicform7.element('input[name=f1]')['_id']='input-normal'
    forms_basicform7.element('input[name=f1]')['_class']='form-control'
    forms_basicform7.element('input[name=f2]')['_placeholder']='f2 .form-control-lg'
    forms_basicform7.element('input[name=f2]')['_id']='input-large'
    forms_basicform7.element('input[name=f2]')['_class']='input-lg form-control-lg form-control'
    forms_basicform7.custom.submit['_type'] = 'submit'
    forms_basicform7.custom.submit['_id'] = 'unk-id'
    forms_basicform7.custom.submit['_value'] = 'submit input'
    forms_basicform7.custom.submit['_class'] = 'unk-class'
    forms_basicform7.custom.submit['_title'] = 'submit forms_basicform7'

    if forms_basicform7.accepts(request,session): 
        response.flash7 = 'submitted forms_basicform7' 
    elif forms_basicform7.errors:
        response.flash7 = '!Errors! forms_basicform7' 
    else: 
        response.flash7 = 'forms_basicform7' 



    forms_basicform8 = SQLFORM(db.dforms_basicform8, _class = 'form-horizontal', _id= 'idUnk8' )

    forms_basicform8.element('input[name=f0]')['_placeholder']='f0 Username'
    forms_basicform8.element('input[name=f0]')['_id']='input1-group1'
    forms_basicform8.element('input[name=f0]')['_class']='form-control'
    forms_basicform8.element('input[name=f1]')['_placeholder']='f1 Email'
    forms_basicform8.element('input[name=f1]')['_id']='input2-group1'
    forms_basicform8.element('input[name=f1]')['_class']='form-control'
    forms_basicform8.element('input[name=f2]')['_placeholder']='f2 ..'
    forms_basicform8.element('input[name=f2]')['_id']='input3-group1'
    forms_basicform8.element('input[name=f2]')['_class']='form-control'
    forms_basicform8.custom.submit['_type'] = 'submit'
    forms_basicform8.custom.submit['_id'] = 'unk-id'
    forms_basicform8.custom.submit['_value'] = 'submit input'
    forms_basicform8.custom.submit['_class'] = 'unk-class'
    forms_basicform8.custom.submit['_title'] = 'submit forms_basicform8'

    if forms_basicform8.accepts(request,session): 
        response.flash8 = 'submitted forms_basicform8' 
    elif forms_basicform8.errors:
        response.flash8 = '!Errors! forms_basicform8' 
    else: 
        response.flash8 = 'forms_basicform8' 



    forms_basicform9 = SQLFORM(db.dforms_basicform9, _class = 'form-horizontal', _id= 'idUnk9' )

    forms_basicform9.element('input[name=f0]')['_placeholder']='f0 Username'
    forms_basicform9.element('input[name=f0]')['_id']='input1-group2'
    forms_basicform9.element('input[name=f0]')['_class']='form-control'
    forms_basicform9.element('input[name=f1]')['_placeholder']='f1 Email'
    forms_basicform9.element('input[name=f1]')['_id']='input2-group2'
    forms_basicform9.element('input[name=f1]')['_class']='form-control'
    forms_basicform9.element('input[name=f2]')['_placeholder']='f2 Search'
    forms_basicform9.element('input[name=f2]')['_id']='input3-group2'
    forms_basicform9.element('input[name=f2]')['_class']='form-control'
    forms_basicform9.custom.submit['_type'] = 'submit'
    forms_basicform9.custom.submit['_class'] = 'btn btn-primary'
    forms_basicform9.custom.submit['_value'] = 'Search'
    forms_basicform9.custom.submit['_id'] = 'id154'
    forms_basicform9.custom.submit['_title'] = 'submit forms_basicform9'
    forms_basicform9.custom.submit['_type'] = 'submit'
    forms_basicform9.custom.submit['_class'] = 'btn btn-primary'
    forms_basicform9.custom.submit['_value'] = 'Submit'
    forms_basicform9.custom.submit['_id'] = 'id157'
    forms_basicform9.custom.submit['_title'] = 'submit forms_basicform9'
    forms_basicform9.custom.submit['_type'] = 'submit'
    forms_basicform9.custom.submit['_class'] = 'btn btn-primary'
    forms_basicform9.custom.submit['_value'] = 'unk_162'
    forms_basicform9.custom.submit['_id'] = 'id160'
    forms_basicform9.custom.submit['_title'] = 'submit forms_basicform9'
    forms_basicform9.custom.submit['_type'] = 'submit'
    forms_basicform9.custom.submit['_class'] = 'btn btn-primary'
    forms_basicform9.custom.submit['_value'] = 'unk_166'
    forms_basicform9.custom.submit['_id'] = 'id164'
    forms_basicform9.custom.submit['_title'] = 'submit forms_basicform9'

    if forms_basicform9.accepts(request,session): 
        response.flash9 = 'submitted forms_basicform9' 
    elif forms_basicform9.errors:
        response.flash9 = '!Errors! forms_basicform9' 
    else: 
        response.flash9 = 'forms_basicform9' 



    forms_basicform10 = SQLFORM(db.dforms_basicform10, _class = 'form-horizontal', _id= 'idUnk10' )

    forms_basicform10.element('input[name=f0]')['_placeholder']='f0 Username'
    forms_basicform10.element('input[name=f0]')['_id']='input1-group3'
    forms_basicform10.element('input[name=f0]')['_class']='form-control'
    forms_basicform10.element('input[name=f1]')['_placeholder']='f1 Email'
    forms_basicform10.element('input[name=f1]')['_id']='input2-group3'
    forms_basicform10.element('input[name=f1]')['_class']='form-control'
    forms_basicform10.element('input[name=f2]')['_placeholder']='f2 ..'
    forms_basicform10.element('input[name=f2]')['_id']='input3-group3'
    forms_basicform10.element('input[name=f2]')['_class']='form-control'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-toggle btn btn-primary'
    forms_basicform10.custom.submit['_value'] = 'Dropdown'
    forms_basicform10.custom.submit['_id'] = 'id174'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Action'
    forms_basicform10.custom.submit['_id'] = 'id177'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Another Action'
    forms_basicform10.custom.submit['_id'] = 'id180'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Something else here'
    forms_basicform10.custom.submit['_id'] = 'id183'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Separated link'
    forms_basicform10.custom.submit['_id'] = 'id186'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-toggle btn btn-primary'
    forms_basicform10.custom.submit['_value'] = 'Dropdown'
    forms_basicform10.custom.submit['_id'] = 'id189'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Action'
    forms_basicform10.custom.submit['_id'] = 'id192'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Another Action'
    forms_basicform10.custom.submit['_id'] = 'id195'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Something else here'
    forms_basicform10.custom.submit['_id'] = 'id198'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Separated link'
    forms_basicform10.custom.submit['_id'] = 'id201'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-toggle btn btn-primary'
    forms_basicform10.custom.submit['_value'] = 'Action'
    forms_basicform10.custom.submit['_id'] = 'id204'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Action'
    forms_basicform10.custom.submit['_id'] = 'id207'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Another Action'
    forms_basicform10.custom.submit['_id'] = 'id210'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Something else here'
    forms_basicform10.custom.submit['_id'] = 'id213'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Separated link'
    forms_basicform10.custom.submit['_id'] = 'id216'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-toggle btn btn-primary'
    forms_basicform10.custom.submit['_value'] = 'Dropdown'
    forms_basicform10.custom.submit['_id'] = 'id219'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Action'
    forms_basicform10.custom.submit['_id'] = 'id222'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Another Action'
    forms_basicform10.custom.submit['_id'] = 'id225'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Something else here'
    forms_basicform10.custom.submit['_id'] = 'id228'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'
    forms_basicform10.custom.submit['_type'] = 'submit'
    forms_basicform10.custom.submit['_class'] = 'dropdown-item'
    forms_basicform10.custom.submit['_value'] = 'Separated link'
    forms_basicform10.custom.submit['_id'] = 'id231'
    forms_basicform10.custom.submit['_title'] = 'submit forms_basicform10'

    if forms_basicform10.accepts(request,session): 
        response.flash10 = 'submitted forms_basicform10' 
    elif forms_basicform10.errors:
        response.flash10 = '!Errors! forms_basicform10' 
    else: 
        response.flash10 = 'forms_basicform10' 



    forms_basicform11 = SQLFORM(db.dforms_basicform11, _class = 'form-horizontal', _id= 'idUnk11' )

    forms_basicform11.element('input[name=f0]')['_placeholder']='f0 .col-md-8'
    forms_basicform11.element('input[name=f0]')['_class']='form-control'
    forms_basicform11.element('input[name=f0]')['_id']='id234'
    forms_basicform11.element('input[name=f1]')['_placeholder']='f1 .col-md-4'
    forms_basicform11.element('input[name=f1]')['_class']='form-control'
    forms_basicform11.element('input[name=f1]')['_id']='id236'
    forms_basicform11.element('input[name=f2]')['_placeholder']='f2 .col-md-7'
    forms_basicform11.element('input[name=f2]')['_class']='form-control'
    forms_basicform11.element('input[name=f2]')['_id']='id238'
    forms_basicform11.element('input[name=f3]')['_placeholder']='f3 .col-md-5'
    forms_basicform11.element('input[name=f3]')['_class']='form-control'
    forms_basicform11.element('input[name=f3]')['_id']='id240'
    forms_basicform11.element('input[name=f4]')['_placeholder']='f4 .col-md-6'
    forms_basicform11.element('input[name=f4]')['_class']='form-control'
    forms_basicform11.element('input[name=f4]')['_id']='id242'
    forms_basicform11.element('input[name=f5]')['_placeholder']='f5 .col-md-6'
    forms_basicform11.element('input[name=f5]')['_class']='form-control'
    forms_basicform11.element('input[name=f5]')['_id']='id244'
    forms_basicform11.element('input[name=f6]')['_placeholder']='f6 .col-md-5'
    forms_basicform11.element('input[name=f6]')['_class']='form-control'
    forms_basicform11.element('input[name=f6]')['_id']='id246'
    forms_basicform11.element('input[name=f7]')['_placeholder']='f7 .col-md-7'
    forms_basicform11.element('input[name=f7]')['_class']='form-control'
    forms_basicform11.element('input[name=f7]')['_id']='id248'
    forms_basicform11.element('input[name=f8]')['_placeholder']='f8 .col-md-4'
    forms_basicform11.element('input[name=f8]')['_class']='form-control'
    forms_basicform11.element('input[name=f8]')['_id']='id250'
    forms_basicform11.element('input[name=f9]')['_placeholder']='f9 .col-md-8'
    forms_basicform11.element('input[name=f9]')['_class']='form-control'
    forms_basicform11.element('input[name=f9]')['_id']='id252'
    forms_basicform11.custom.submit['_type'] = 'submit'
    forms_basicform11.custom.submit['_class'] = 'unk-class'
    forms_basicform11.custom.submit['_value'] = 'submit input'
    forms_basicform11.custom.submit['_id'] = 'unk-id'
    forms_basicform11.custom.submit['_title'] = 'submit forms_basicform11'

    if forms_basicform11.accepts(request,session): 
        response.flash11 = 'submitted forms_basicform11' 
    elif forms_basicform11.errors:
        response.flash11 = '!Errors! forms_basicform11' 
    else: 
        response.flash11 = 'forms_basicform11' 



    forms_basicform12 = SQLFORM(db.dforms_basicform12, _class = 'form-horizontal', _id= 'idUnk12' )

    forms_basicform12.element('input[name=f0]')['_placeholder']='f0 .col-4'
    forms_basicform12.element('input[name=f0]')['_class']='form-control'
    forms_basicform12.element('input[name=f0]')['_id']='id254'
    forms_basicform12.element('input[name=f1]')['_placeholder']='f1 .col-8'
    forms_basicform12.element('input[name=f1]')['_class']='form-control'
    forms_basicform12.element('input[name=f1]')['_id']='id256'
    forms_basicform12.element('input[name=f2]')['_placeholder']='f2 .col-5'
    forms_basicform12.element('input[name=f2]')['_class']='form-control'
    forms_basicform12.element('input[name=f2]')['_id']='id258'
    forms_basicform12.element('input[name=f3]')['_placeholder']='f3 .col-7'
    forms_basicform12.element('input[name=f3]')['_class']='form-control'
    forms_basicform12.element('input[name=f3]')['_id']='id260'
    forms_basicform12.element('input[name=f4]')['_placeholder']='f4 .col-6'
    forms_basicform12.element('input[name=f4]')['_class']='form-control'
    forms_basicform12.element('input[name=f4]')['_id']='id262'
    forms_basicform12.element('input[name=f5]')['_placeholder']='f5 .col-6'
    forms_basicform12.element('input[name=f5]')['_class']='form-control'
    forms_basicform12.element('input[name=f5]')['_id']='id264'
    forms_basicform12.element('input[name=f6]')['_placeholder']='f6 .col-5'
    forms_basicform12.element('input[name=f6]')['_class']='form-control'
    forms_basicform12.element('input[name=f6]')['_id']='id266'
    forms_basicform12.element('input[name=f7]')['_placeholder']='f7 .col-5'
    forms_basicform12.element('input[name=f7]')['_class']='form-control'
    forms_basicform12.element('input[name=f7]')['_id']='id268'
    forms_basicform12.element('input[name=f8]')['_placeholder']='f8 .col-8'
    forms_basicform12.element('input[name=f8]')['_class']='form-control'
    forms_basicform12.element('input[name=f8]')['_id']='id270'
    forms_basicform12.element('input[name=f9]')['_placeholder']='f9 .col-4'
    forms_basicform12.element('input[name=f9]')['_class']='form-control'
    forms_basicform12.element('input[name=f9]')['_id']='id272'
    forms_basicform12.custom.submit['_type'] = 'submit'
    forms_basicform12.custom.submit['_class'] = 'unk-class'
    forms_basicform12.custom.submit['_value'] = 'submit input'
    forms_basicform12.custom.submit['_id'] = 'unk-id'
    forms_basicform12.custom.submit['_title'] = 'submit forms_basicform12'

    if forms_basicform12.accepts(request,session): 
        response.flash12 = 'submitted forms_basicform12' 
    elif forms_basicform12.errors:
        response.flash12 = '!Errors! forms_basicform12' 
    else: 
        response.flash12 = 'forms_basicform12' 



    forms_basicform13 = SQLFORM(db.dforms_basicform13, _class = '', _id= 'idUnk13' )

    forms_basicform13.element('input[name=f0]')['_placeholder']='f0 place_276'
    forms_basicform13.element('input[name=f0]')['_id']='username3'
    forms_basicform13.element('input[name=f0]')['_class']='form-control'
    forms_basicform13.element('input[name=f1]')['_placeholder']='f1 place_279'
    forms_basicform13.element('input[name=f1]')['_id']='email3'
    forms_basicform13.element('input[name=f1]')['_class']='form-control'
    forms_basicform13.element('input[name=f2]')['_placeholder']='f2 place_282'
    forms_basicform13.element('input[name=f2]')['_id']='password3'
    forms_basicform13.element('input[name=f2]')['_class']='form-control'
    forms_basicform13.custom.submit['_type'] = 'submit'
    forms_basicform13.custom.submit['_class'] = 'btn btn-primary btn-sm'
    forms_basicform13.custom.submit['_value'] = 'Submit'
    forms_basicform13.custom.submit['_id'] = 'id283'
    forms_basicform13.custom.submit['_title'] = 'submit forms_basicform13'

    if forms_basicform13.accepts(request,session): 
        response.flash13 = 'submitted forms_basicform13' 
    elif forms_basicform13.errors:
        response.flash13 = '!Errors! forms_basicform13' 
    else: 
        response.flash13 = 'forms_basicform13' 



    forms_basicform14 = SQLFORM(db.dforms_basicform14, _class = '', _id= 'idUnk14' )

    forms_basicform14.element('input[name=f0]')['_placeholder']='f0 Username'
    forms_basicform14.element('input[name=f0]')['_id']='username2'
    forms_basicform14.element('input[name=f0]')['_class']='form-control'
    forms_basicform14.element('input[name=f1]')['_placeholder']='f1 Email'
    forms_basicform14.element('input[name=f1]')['_id']='email2'
    forms_basicform14.element('input[name=f1]')['_class']='form-control'
    forms_basicform14.element('input[name=f2]')['_placeholder']='f2 Password'
    forms_basicform14.element('input[name=f2]')['_id']='password2'
    forms_basicform14.element('input[name=f2]')['_class']='form-control'
    forms_basicform14.custom.submit['_type'] = 'submit'
    forms_basicform14.custom.submit['_class'] = 'btn btn-secondary btn-sm'
    forms_basicform14.custom.submit['_value'] = 'Submit'
    forms_basicform14.custom.submit['_id'] = 'id292'
    forms_basicform14.custom.submit['_title'] = 'submit forms_basicform14'

    if forms_basicform14.accepts(request,session): 
        response.flash14 = 'submitted forms_basicform14' 
    elif forms_basicform14.errors:
        response.flash14 = '!Errors! forms_basicform14' 
    else: 
        response.flash14 = 'forms_basicform14' 



    forms_basicform15 = SQLFORM(db.dforms_basicform15, _class = '', _id= 'idUnk15' )

    forms_basicform15.element('input[name=f0]')['_placeholder']='f0 Username'
    forms_basicform15.element('input[name=f0]')['_id']='username'
    forms_basicform15.element('input[name=f0]')['_class']='form-control'
    forms_basicform15.element('input[name=f1]')['_placeholder']='f1 Email'
    forms_basicform15.element('input[name=f1]')['_id']='email'
    forms_basicform15.element('input[name=f1]')['_class']='form-control'
    forms_basicform15.element('input[name=f2]')['_placeholder']='f2 Password'
    forms_basicform15.element('input[name=f2]')['_id']='password'
    forms_basicform15.element('input[name=f2]')['_class']='form-control'
    forms_basicform15.custom.submit['_type'] = 'submit'
    forms_basicform15.custom.submit['_class'] = 'btn btn-success btn-sm'
    forms_basicform15.custom.submit['_value'] = 'Submit'
    forms_basicform15.custom.submit['_id'] = 'id301'
    forms_basicform15.custom.submit['_title'] = 'submit forms_basicform15'

    if forms_basicform15.accepts(request,session): 
        response.flash15 = 'submitted forms_basicform15' 
    elif forms_basicform15.errors:
        response.flash15 = '!Errors! forms_basicform15' 
    else: 
        response.flash15 = 'forms_basicform15' 


    return dict( DICT= rows_dict, forms_basicform0= forms_basicform0, forms_basicform1= forms_basicform1, forms_basicform2= forms_basicform2, forms_basicform3= forms_basicform3, forms_basicform4= forms_basicform4, forms_basicform5= forms_basicform5, forms_basicform6= forms_basicform6, forms_basicform7= forms_basicform7, forms_basicform8= forms_basicform8, forms_basicform9= forms_basicform9, forms_basicform10= forms_basicform10, forms_basicform11= forms_basicform11, forms_basicform12= forms_basicform12, forms_basicform13= forms_basicform13, forms_basicform14= forms_basicform14, forms_basicform15= forms_basicform15, )

#@auth.requires_login()
def ui_grids():

    qu= db.dui0grids.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/ui-grids.html'


    ui_gridsform0 = SQLFORM(db.dui_gridsform0, _class = 'search-form', _id= 'idUnk0' )

    ui_gridsform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    ui_gridsform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    ui_gridsform0.element('input[name=f0]')['_id']='id478'
    ui_gridsform0.custom.submit['_type'] = 'submit'
    ui_gridsform0.custom.submit['_class'] = 'search-close'
    ui_gridsform0.custom.submit['_value'] = 'unk_482'
    ui_gridsform0.custom.submit['_id'] = 'id480'
    ui_gridsform0.custom.submit['_title'] = 'submit ui_gridsform0'

    if ui_gridsform0.accepts(request,session): 
        response.flash0 = 'submitted ui_gridsform0' 
    elif ui_gridsform0.errors:
        response.flash0 = '!Errors! ui_gridsform0' 
    else: 
        response.flash0 = 'ui_gridsform0' 


    return dict( DICT= rows_dict, ui_gridsform0= ui_gridsform0, )

#@auth.requires_login()
def ui_social_buttons():

    qu= db.dui0social0buttons.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/ui-social-buttons.html'


    ui_social_buttonsform0 = SQLFORM(db.dui_social_buttonsform0, _class = 'search-form', _id= 'idUnk0' )

    ui_social_buttonsform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    ui_social_buttonsform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    ui_social_buttonsform0.element('input[name=f0]')['_id']='id5'
    ui_social_buttonsform0.custom.submit['_type'] = 'submit'
    ui_social_buttonsform0.custom.submit['_class'] = 'search-close'
    ui_social_buttonsform0.custom.submit['_value'] = 'unk_9'
    ui_social_buttonsform0.custom.submit['_id'] = 'id7'
    ui_social_buttonsform0.custom.submit['_title'] = 'submit ui_social_buttonsform0'

    if ui_social_buttonsform0.accepts(request,session): 
        response.flash0 = 'submitted ui_social_buttonsform0' 
    elif ui_social_buttonsform0.errors:
        response.flash0 = '!Errors! ui_social_buttonsform0' 
    else: 
        response.flash0 = 'ui_social_buttonsform0' 


    return dict( DICT= rows_dict, ui_social_buttonsform0= ui_social_buttonsform0, )

#@auth.requires_login()
def ui_typgraphy():

    qu= db.dui0typgraphy.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/ui-typgraphy.html'


    ui_typgraphyform0 = SQLFORM(db.dui_typgraphyform0, _class = 'search-form', _id= 'idUnk0' )

    ui_typgraphyform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    ui_typgraphyform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    ui_typgraphyform0.element('input[name=f0]')['_id']='id328'
    ui_typgraphyform0.custom.submit['_type'] = 'submit'
    ui_typgraphyform0.custom.submit['_class'] = 'search-close'
    ui_typgraphyform0.custom.submit['_value'] = 'unk_332'
    ui_typgraphyform0.custom.submit['_id'] = 'id330'
    ui_typgraphyform0.custom.submit['_title'] = 'submit ui_typgraphyform0'

    if ui_typgraphyform0.accepts(request,session): 
        response.flash0 = 'submitted ui_typgraphyform0' 
    elif ui_typgraphyform0.errors:
        response.flash0 = '!Errors! ui_typgraphyform0' 
    else: 
        response.flash0 = 'ui_typgraphyform0' 


    return dict( DICT= rows_dict, ui_typgraphyform0= ui_typgraphyform0, )

#@auth.requires_login()
def widgets():

    qu= db.dwidgets.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/widgets.html'


    widgetsform0 = SQLFORM(db.dwidgetsform0, _class = 'search-form', _id= 'idUnk0' )

    widgetsform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    widgetsform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    widgetsform0.element('input[name=f0]')['_id']='id11'
    widgetsform0.custom.submit['_type'] = 'submit'
    widgetsform0.custom.submit['_class'] = 'search-close'
    widgetsform0.custom.submit['_value'] = 'unk_15'
    widgetsform0.custom.submit['_id'] = 'id13'
    widgetsform0.custom.submit['_title'] = 'submit widgetsform0'

    if widgetsform0.accepts(request,session): 
        response.flash0 = 'submitted widgetsform0' 
    elif widgetsform0.errors:
        response.flash0 = '!Errors! widgetsform0' 
    else: 
        response.flash0 = 'widgetsform0' 


    return dict( DICT= rows_dict, widgetsform0= widgetsform0, )

#@auth.requires_login()
def tables_basic():

    qu= db.dtables0basic.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/tables-basic.html'


    tables_basicform0 = SQLFORM(db.dtables_basicform0, _class = 'search-form', _id= 'idUnk0' )

    tables_basicform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    tables_basicform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    tables_basicform0.element('input[name=f0]')['_id']='id352'
    tables_basicform0.custom.submit['_type'] = 'submit'
    tables_basicform0.custom.submit['_class'] = 'search-close'
    tables_basicform0.custom.submit['_value'] = 'unk_356'
    tables_basicform0.custom.submit['_id'] = 'id354'
    tables_basicform0.custom.submit['_title'] = 'submit tables_basicform0'

    if tables_basicform0.accepts(request,session): 
        response.flash0 = 'submitted tables_basicform0' 
    elif tables_basicform0.errors:
        response.flash0 = '!Errors! tables_basicform0' 
    else: 
        response.flash0 = 'tables_basicform0' 


    return dict( DICT= rows_dict, tables_basicform0= tables_basicform0, )

#@auth.requires_login()
def ui_alerts():

    qu= db.dui0alerts.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/ui-alerts.html'


    ui_alertsform0 = SQLFORM(db.dui_alertsform0, _class = 'search-form', _id= 'idUnk0' )

    ui_alertsform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    ui_alertsform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    ui_alertsform0.element('input[name=f0]')['_id']='id490'
    ui_alertsform0.custom.submit['_type'] = 'submit'
    ui_alertsform0.custom.submit['_class'] = 'search-close'
    ui_alertsform0.custom.submit['_value'] = 'unk_494'
    ui_alertsform0.custom.submit['_id'] = 'id492'
    ui_alertsform0.custom.submit['_title'] = 'submit ui_alertsform0'

    if ui_alertsform0.accepts(request,session): 
        response.flash0 = 'submitted ui_alertsform0' 
    elif ui_alertsform0.errors:
        response.flash0 = '!Errors! ui_alertsform0' 
    else: 
        response.flash0 = 'ui_alertsform0' 


    return dict( DICT= rows_dict, ui_alertsform0= ui_alertsform0, )

#@auth.requires_login()
def page_login():

    qu= db.dpage0login.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/page-login.html'


    page_loginform0 = SQLFORM(db.dpage_loginform0, _class = 'classUnk0', _id= 'idUnk0' )

    page_loginform0.element('input[name=f0]')['_placeholder']='f0 Email'
    page_loginform0.element('input[name=f0]')['_class']='form-control'
    page_loginform0.element('input[name=f0]')['_id']='id358'
    page_loginform0.element('input[name=f1]')['_placeholder']='f1 Password'
    page_loginform0.element('input[name=f1]')['_class']='form-control'
    page_loginform0.element('input[name=f1]')['_id']='id361'
    page_loginform0.element('input[name=f2]')['_placeholder']='f2 place_367'
    page_loginform0.element('input[name=f2]')['_id']='id364'
    page_loginform0.custom.submit['_type'] = 'submit'
    page_loginform0.custom.submit['_class'] = 'btn btn-success btn-flat m-b-30 m-t-30'
    page_loginform0.custom.submit['_value'] = 'Sign in'
    page_loginform0.custom.submit['_id'] = 'id368'
    page_loginform0.custom.submit['_title'] = 'submit page_loginform0'
    page_loginform0.custom.submit['_type'] = 'submit'
    page_loginform0.custom.submit['_class'] = 'btn social facebook btn-flat btn-addon mb-3'
    page_loginform0.custom.submit['_value'] = 'Sign in with facebook'
    page_loginform0.custom.submit['_id'] = 'id372'
    page_loginform0.custom.submit['_title'] = 'submit page_loginform0'
    page_loginform0.custom.submit['_type'] = 'submit'
    page_loginform0.custom.submit['_class'] = 'btn social twitter btn-flat btn-addon mt-2'
    page_loginform0.custom.submit['_value'] = 'Sign in with twitter'
    page_loginform0.custom.submit['_id'] = 'id375'
    page_loginform0.custom.submit['_title'] = 'submit page_loginform0'
    page_loginform0.custom.submit['_id'] = 'id378'
    page_loginform0.custom.submit['_title'] = 'submit page_loginform0'
    page_loginform0.custom.submit['_id'] = 'id382'
    page_loginform0.custom.submit['_title'] = 'submit page_loginform0'

    if page_loginform0.accepts(request,session): 
        response.flash0 = 'submitted page_loginform0' 
    elif page_loginform0.errors:
        response.flash0 = '!Errors! page_loginform0' 
    else: 
        response.flash0 = 'page_loginform0' 


    return dict( DICT= rows_dict, page_loginform0= page_loginform0, )

#@auth.requires_login()
def ui_cards():

    qu= db.dui0cards.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/ui-cards.html'


    ui_cardsform0 = SQLFORM(db.dui_cardsform0, _class = 'search-form', _id= 'idUnk0' )

    ui_cardsform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    ui_cardsform0.element('input[name=f0]')['_class']='form-control mr-sm-2'
    ui_cardsform0.element('input[name=f0]')['_id']='id422'
    ui_cardsform0.custom.submit['_type'] = 'submit'
    ui_cardsform0.custom.submit['_class'] = 'search-close'
    ui_cardsform0.custom.submit['_value'] = 'unk_426'
    ui_cardsform0.custom.submit['_id'] = 'id424'
    ui_cardsform0.custom.submit['_title'] = 'submit ui_cardsform0'

    if ui_cardsform0.accepts(request,session): 
        response.flash0 = 'submitted ui_cardsform0' 
    elif ui_cardsform0.errors:
        response.flash0 = '!Errors! ui_cardsform0' 
    else: 
        response.flash0 = 'ui_cardsform0' 


    return dict( DICT= rows_dict, ui_cardsform0= ui_cardsform0, )