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
def boxed():

    qu= db.dboxed.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/boxed.html'


    boxedform0 = SQLFORM(db.dboxedform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #boxedform0 = SQLFORM(db.dboxedform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    boxedform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    boxedform0.element('input[name=f0]')['_id']='id_for908'
    boxedform0.element('input[name=f0]')['_class']='form-control'

    boxedform0.custom.submit['_type'] = 'submit'
    boxedform0.custom.submit['_id'] = 'search-btn'
    boxedform0.custom.submit['_value'] = 'unk_912'
    boxedform0.custom.submit['_class'] = 'btn btn-flat'
    boxedform0.custom.submit['_title'] = 'submit boxedform0'

    if boxedform0.accepts(request,session): 
        response.flash0 = 'submitted boxedform0' 
    elif boxedform0.errors:
        response.flash0 = '!Errors! boxedform0' 
    else: 
        response.flash0 = 'boxedform0' 



    boxedform1 = SQLFORM(db.dboxedform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #boxedform1 = SQLFORM(db.dboxedform1,  _class = 'classUnk1', _id= 'idUnk1' )

    boxedform1.element('input[name=f0]')['_placeholder']='f0 place_917'
    boxedform1.element('input[name=f0]')['_id']='id_for914'
    boxedform1.element('input[name=f0]')['_class']='pull-right'
    boxedform1.element('input[name=f1]')['_placeholder']='f1 place_921'
    boxedform1.element('input[name=f1]')['_id']='id_for918'
    boxedform1.element('input[name=f1]')['_class']='pull-right'
    boxedform1.element('input[name=f2]')['_placeholder']='f2 place_925'
    boxedform1.element('input[name=f2]')['_id']='id_for922'
    boxedform1.element('input[name=f2]')['_class']='pull-right'
    boxedform1.element('input[name=f3]')['_placeholder']='f3 place_929'
    boxedform1.element('input[name=f3]')['_id']='id_for926'
    boxedform1.element('input[name=f3]')['_class']='pull-right'
    boxedform1.element('input[name=f4]')['_placeholder']='f4 place_933'
    boxedform1.element('input[name=f4]')['_id']='id_for930'
    boxedform1.element('input[name=f4]')['_class']='pull-right'

    boxedform1.custom.submit['_id'] = 'id_for934'
    boxedform1.custom.submit['_class'] = 'text-red pull-right'
    boxedform1.custom.submit['_title'] = 'submit boxedform1'

    if boxedform1.accepts(request,session): 
        response.flash1 = 'submitted boxedform1' 
    elif boxedform1.errors:
        response.flash1 = '!Errors! boxedform1' 
    else: 
        response.flash1 = 'boxedform1' 


    return dict( DICT= rows_dict, boxedform0= boxedform0, boxedform1= boxedform1, )

#@auth.requires_login()
def fixed():

    qu= db.dfixed.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/fixed.html'


    fixedform0 = SQLFORM(db.dfixedform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #fixedform0 = SQLFORM(db.dfixedform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    fixedform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    fixedform0.element('input[name=f0]')['_id']='id_for747'
    fixedform0.element('input[name=f0]')['_class']='form-control'

    fixedform0.custom.submit['_type'] = 'submit'
    fixedform0.custom.submit['_id'] = 'search-btn'
    fixedform0.custom.submit['_value'] = 'unk_751'
    fixedform0.custom.submit['_class'] = 'btn btn-flat'
    fixedform0.custom.submit['_title'] = 'submit fixedform0'

    if fixedform0.accepts(request,session): 
        response.flash0 = 'submitted fixedform0' 
    elif fixedform0.errors:
        response.flash0 = '!Errors! fixedform0' 
    else: 
        response.flash0 = 'fixedform0' 



    fixedform1 = SQLFORM(db.dfixedform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #fixedform1 = SQLFORM(db.dfixedform1,  _class = 'classUnk1', _id= 'idUnk1' )

    fixedform1.element('input[name=f0]')['_placeholder']='f0 place_756'
    fixedform1.element('input[name=f0]')['_id']='id_for753'
    fixedform1.element('input[name=f0]')['_class']='pull-right'
    fixedform1.element('input[name=f1]')['_placeholder']='f1 place_760'
    fixedform1.element('input[name=f1]')['_id']='id_for757'
    fixedform1.element('input[name=f1]')['_class']='pull-right'
    fixedform1.element('input[name=f2]')['_placeholder']='f2 place_764'
    fixedform1.element('input[name=f2]')['_id']='id_for761'
    fixedform1.element('input[name=f2]')['_class']='pull-right'
    fixedform1.element('input[name=f3]')['_placeholder']='f3 place_768'
    fixedform1.element('input[name=f3]')['_id']='id_for765'
    fixedform1.element('input[name=f3]')['_class']='pull-right'
    fixedform1.element('input[name=f4]')['_placeholder']='f4 place_772'
    fixedform1.element('input[name=f4]')['_id']='id_for769'
    fixedform1.element('input[name=f4]')['_class']='pull-right'

    fixedform1.custom.submit['_id'] = 'id_for773'
    fixedform1.custom.submit['_class'] = 'text-red pull-right'
    fixedform1.custom.submit['_title'] = 'submit fixedform1'

    if fixedform1.accepts(request,session): 
        response.flash1 = 'submitted fixedform1' 
    elif fixedform1.errors:
        response.flash1 = '!Errors! fixedform1' 
    else: 
        response.flash1 = 'fixedform1' 


    return dict( DICT= rows_dict, fixedform0= fixedform0, fixedform1= fixedform1, )

#@auth.requires_login()
def advanced():

    qu= db.dadvanced.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/advanced.html'


    advancedform0 = SQLFORM(db.dadvancedform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #advancedform0 = SQLFORM(db.dadvancedform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    advancedform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    advancedform0.element('input[name=f0]')['_id']='id_for282'
    advancedform0.element('input[name=f0]')['_class']='form-control'

    advancedform0.custom.submit['_type'] = 'submit'
    advancedform0.custom.submit['_id'] = 'search-btn'
    advancedform0.custom.submit['_value'] = 'unk_286'
    advancedform0.custom.submit['_class'] = 'btn btn-flat'
    advancedform0.custom.submit['_title'] = 'submit advancedform0'

    if advancedform0.accepts(request,session): 
        response.flash0 = 'submitted advancedform0' 
    elif advancedform0.errors:
        response.flash0 = '!Errors! advancedform0' 
    else: 
        response.flash0 = 'advancedform0' 



    advancedform1 = SQLFORM(db.dadvancedform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #advancedform1 = SQLFORM(db.dadvancedform1,  _class = 'classUnk1', _id= 'idUnk1' )

    advancedform1.element('input[name=f0]')['_placeholder']='f0 place_291'
    advancedform1.element('input[name=f0]')['_id']='id_for288'
    advancedform1.element('input[name=f0]')['_class']='pull-right'
    advancedform1.element('input[name=f1]')['_placeholder']='f1 place_295'
    advancedform1.element('input[name=f1]')['_id']='id_for292'
    advancedform1.element('input[name=f1]')['_class']='pull-right'
    advancedform1.element('input[name=f2]')['_placeholder']='f2 place_299'
    advancedform1.element('input[name=f2]')['_id']='id_for296'
    advancedform1.element('input[name=f2]')['_class']='pull-right'
    advancedform1.element('input[name=f3]')['_placeholder']='f3 place_303'
    advancedform1.element('input[name=f3]')['_id']='id_for300'
    advancedform1.element('input[name=f3]')['_class']='pull-right'
    advancedform1.element('input[name=f4]')['_placeholder']='f4 place_307'
    advancedform1.element('input[name=f4]')['_id']='id_for304'
    advancedform1.element('input[name=f4]')['_class']='pull-right'

    advancedform1.custom.submit['_id'] = 'id_for308'
    advancedform1.custom.submit['_class'] = 'text-red pull-right'
    advancedform1.custom.submit['_title'] = 'submit advancedform1'

    if advancedform1.accepts(request,session): 
        response.flash1 = 'submitted advancedform1' 
    elif advancedform1.errors:
        response.flash1 = '!Errors! advancedform1' 
    else: 
        response.flash1 = 'advancedform1' 


    return dict( DICT= rows_dict, advancedform0= advancedform0, advancedform1= advancedform1, )

#@auth.requires_login()
def X404():

    qu= db.d404.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/404.html'


    X404form0 = SQLFORM(db.dX404form0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #X404form0 = SQLFORM(db.dX404form0,  _class = 'sidebar-form', _id= 'idUnk0' )

    X404form0.element('input[name=f0]')['_placeholder']='f0 Search...'
    X404form0.element('input[name=f0]')['_id']='id_for462'
    X404form0.element('input[name=f0]')['_class']='form-control'

    X404form0.custom.submit['_type'] = 'submit'
    X404form0.custom.submit['_id'] = 'search-btn'
    X404form0.custom.submit['_value'] = 'unk_466'
    X404form0.custom.submit['_class'] = 'btn btn-flat'
    X404form0.custom.submit['_title'] = 'submit X404form0'

    if X404form0.accepts(request,session): 
        response.flash0 = 'submitted X404form0' 
    elif X404form0.errors:
        response.flash0 = '!Errors! X404form0' 
    else: 
        response.flash0 = 'X404form0' 



    X404form1 = SQLFORM(db.dX404form1, formstyle= 'divs', _class = 'search-form', _id= 'idUnk1' )
    #X404form1 = SQLFORM(db.dX404form1,  _class = 'search-form', _id= 'idUnk1' )

    X404form1.element('input[name=f0]')['_placeholder']='f0 Search'
    X404form1.element('input[name=f0]')['_id']='id_for468'
    X404form1.element('input[name=f0]')['_class']='form-control'

    X404form1.custom.submit['_type'] = 'submit'
    X404form1.custom.submit['_id'] = 'id_for470'
    X404form1.custom.submit['_value'] = 'unk_472'
    X404form1.custom.submit['_class'] = 'btn btn-warning btn-flat'
    X404form1.custom.submit['_title'] = 'submit X404form1'

    if X404form1.accepts(request,session): 
        response.flash1 = 'submitted X404form1' 
    elif X404form1.errors:
        response.flash1 = '!Errors! X404form1' 
    else: 
        response.flash1 = 'X404form1' 



    X404form2 = SQLFORM(db.dX404form2, formstyle= 'divs', _class = 'classUnk2', _id= 'idUnk2' )
    #X404form2 = SQLFORM(db.dX404form2,  _class = 'classUnk2', _id= 'idUnk2' )

    X404form2.element('input[name=f0]')['_placeholder']='f0 place_477'
    X404form2.element('input[name=f0]')['_id']='id_for474'
    X404form2.element('input[name=f0]')['_class']='pull-right'
    X404form2.element('input[name=f1]')['_placeholder']='f1 place_481'
    X404form2.element('input[name=f1]')['_id']='id_for478'
    X404form2.element('input[name=f1]')['_class']='pull-right'
    X404form2.element('input[name=f2]')['_placeholder']='f2 place_485'
    X404form2.element('input[name=f2]')['_id']='id_for482'
    X404form2.element('input[name=f2]')['_class']='pull-right'
    X404form2.element('input[name=f3]')['_placeholder']='f3 place_489'
    X404form2.element('input[name=f3]')['_id']='id_for486'
    X404form2.element('input[name=f3]')['_class']='pull-right'
    X404form2.element('input[name=f4]')['_placeholder']='f4 place_493'
    X404form2.element('input[name=f4]')['_id']='id_for490'
    X404form2.element('input[name=f4]')['_class']='pull-right'

    X404form2.custom.submit['_id'] = 'id_for494'
    X404form2.custom.submit['_class'] = 'text-red pull-right'
    X404form2.custom.submit['_title'] = 'submit X404form2'

    if X404form2.accepts(request,session): 
        response.flash2 = 'submitted X404form2' 
    elif X404form2.errors:
        response.flash2 = '!Errors! X404form2' 
    else: 
        response.flash2 = 'X404form2' 


    return dict( DICT= rows_dict, X404form0= X404form0, X404form1= X404form1, X404form2= X404form2, )

#@auth.requires_login()
def collapsedIIsidebar():

    qu= db.dcollapsed0sidebar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/collapsed-sidebar.html'


    collapsedIIsidebarform0 = SQLFORM(db.dcollapsedIIsidebarform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #collapsedIIsidebarform0 = SQLFORM(db.dcollapsedIIsidebarform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    collapsedIIsidebarform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    collapsedIIsidebarform0.element('input[name=f0]')['_id']='id_for252'
    collapsedIIsidebarform0.element('input[name=f0]')['_class']='form-control'

    collapsedIIsidebarform0.custom.submit['_type'] = 'submit'
    collapsedIIsidebarform0.custom.submit['_id'] = 'search-btn'
    collapsedIIsidebarform0.custom.submit['_value'] = 'unk_256'
    collapsedIIsidebarform0.custom.submit['_class'] = 'btn btn-flat'
    collapsedIIsidebarform0.custom.submit['_title'] = 'submit collapsedIIsidebarform0'

    if collapsedIIsidebarform0.accepts(request,session): 
        response.flash0 = 'submitted collapsedIIsidebarform0' 
    elif collapsedIIsidebarform0.errors:
        response.flash0 = '!Errors! collapsedIIsidebarform0' 
    else: 
        response.flash0 = 'collapsedIIsidebarform0' 



    collapsedIIsidebarform1 = SQLFORM(db.dcollapsedIIsidebarform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #collapsedIIsidebarform1 = SQLFORM(db.dcollapsedIIsidebarform1,  _class = 'classUnk1', _id= 'idUnk1' )

    collapsedIIsidebarform1.element('input[name=f0]')['_placeholder']='f0 place_261'
    collapsedIIsidebarform1.element('input[name=f0]')['_id']='id_for258'
    collapsedIIsidebarform1.element('input[name=f0]')['_class']='pull-right'
    collapsedIIsidebarform1.element('input[name=f1]')['_placeholder']='f1 place_265'
    collapsedIIsidebarform1.element('input[name=f1]')['_id']='id_for262'
    collapsedIIsidebarform1.element('input[name=f1]')['_class']='pull-right'
    collapsedIIsidebarform1.element('input[name=f2]')['_placeholder']='f2 place_269'
    collapsedIIsidebarform1.element('input[name=f2]')['_id']='id_for266'
    collapsedIIsidebarform1.element('input[name=f2]')['_class']='pull-right'
    collapsedIIsidebarform1.element('input[name=f3]')['_placeholder']='f3 place_273'
    collapsedIIsidebarform1.element('input[name=f3]')['_id']='id_for270'
    collapsedIIsidebarform1.element('input[name=f3]')['_class']='pull-right'
    collapsedIIsidebarform1.element('input[name=f4]')['_placeholder']='f4 place_277'
    collapsedIIsidebarform1.element('input[name=f4]')['_id']='id_for274'
    collapsedIIsidebarform1.element('input[name=f4]')['_class']='pull-right'

    collapsedIIsidebarform1.custom.submit['_id'] = 'id_for278'
    collapsedIIsidebarform1.custom.submit['_class'] = 'text-red pull-right'
    collapsedIIsidebarform1.custom.submit['_title'] = 'submit collapsedIIsidebarform1'

    if collapsedIIsidebarform1.accepts(request,session): 
        response.flash1 = 'submitted collapsedIIsidebarform1' 
    elif collapsedIIsidebarform1.errors:
        response.flash1 = '!Errors! collapsedIIsidebarform1' 
    else: 
        response.flash1 = 'collapsedIIsidebarform1' 


    return dict( DICT= rows_dict, collapsedIIsidebarform0= collapsedIIsidebarform0, collapsedIIsidebarform1= collapsedIIsidebarform1, )

#@auth.requires_login()
def starter():

    qu= db.dstarter.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/starter.html'


    starterform0 = SQLFORM(db.dstarterform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #starterform0 = SQLFORM(db.dstarterform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    starterform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    starterform0.element('input[name=f0]')['_id']='id_for212'
    starterform0.element('input[name=f0]')['_class']='form-control'

    starterform0.custom.submit['_type'] = 'submit'
    starterform0.custom.submit['_id'] = 'search-btn'
    starterform0.custom.submit['_value'] = 'unk_216'
    starterform0.custom.submit['_class'] = 'btn btn-flat'
    starterform0.custom.submit['_title'] = 'submit starterform0'

    if starterform0.accepts(request,session): 
        response.flash0 = 'submitted starterform0' 
    elif starterform0.errors:
        response.flash0 = '!Errors! starterform0' 
    else: 
        response.flash0 = 'starterform0' 



    starterform1 = SQLFORM(db.dstarterform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #starterform1 = SQLFORM(db.dstarterform1,  _class = 'classUnk1', _id= 'idUnk1' )

    starterform1.element('input[name=f0]')['_placeholder']='f0 place_221'
    starterform1.element('input[name=f0]')['_id']='id_for218'
    starterform1.element('input[name=f0]')['_class']='pull-right'

    starterform1.custom.submit['_type'] = 'submit'
    starterform1.custom.submit['_id'] = 'unk-id'
    starterform1.custom.submit['_value'] = 'submit checkbox'
    starterform1.custom.submit['_class'] = 'unk-class'
    starterform1.custom.submit['_title'] = 'submit starterform1'

    if starterform1.accepts(request,session): 
        response.flash1 = 'submitted starterform1' 
    elif starterform1.errors:
        response.flash1 = '!Errors! starterform1' 
    else: 
        response.flash1 = 'starterform1' 


    return dict( DICT= rows_dict, starterform0= starterform0, starterform1= starterform1, )

#@auth.requires_login()
def index():

    qu= db.dindex.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index.html'


    indexform0 = SQLFORM(db.dindexform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #indexform0 = SQLFORM(db.dindexform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    indexform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    indexform0.element('input[name=f0]')['_id']='id_for807'
    indexform0.element('input[name=f0]')['_class']='form-control'

    indexform0.custom.submit['_type'] = 'submit'
    indexform0.custom.submit['_id'] = 'search-btn'
    indexform0.custom.submit['_value'] = 'unk_811'
    indexform0.custom.submit['_class'] = 'btn btn-flat'
    indexform0.custom.submit['_title'] = 'submit indexform0'

    if indexform0.accepts(request,session): 
        response.flash0 = 'submitted indexform0' 
    elif indexform0.errors:
        response.flash0 = '!Errors! indexform0' 
    else: 
        response.flash0 = 'indexform0' 



    indexform1 = SQLFORM(db.dindexform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #indexform1 = SQLFORM(db.dindexform1,  _class = 'classUnk1', _id= 'idUnk1' )

    indexform1.element('input[name=f0]')['_placeholder']='f0 Email to:'
    indexform1.element('input[name=f0]')['_id']='id_for813'
    indexform1.element('input[name=f0]')['_class']='form-control'
    indexform1.element('input[name=f1]')['_placeholder']='f1 Subject'
    indexform1.element('input[name=f1]')['_id']='id_for815'
    indexform1.element('input[name=f1]')['_class']='form-control'
    indexform1.element('textarea[name=f2]')['_placeholder']='f2 Message'
    indexform1.element('textarea[name=f2]')['_id']='id_for817'
    indexform1.element('textarea[name=f2]')['_class']='textarea'

    indexform1.custom.submit['_type'] = 'submit'
    indexform1.custom.submit['_id'] = 'unk-id'
    indexform1.custom.submit['_value'] = 'submit input'
    indexform1.custom.submit['_class'] = 'unk-class'
    indexform1.custom.submit['_title'] = 'submit indexform1'

    if indexform1.accepts(request,session): 
        response.flash1 = 'submitted indexform1' 
    elif indexform1.errors:
        response.flash1 = '!Errors! indexform1' 
    else: 
        response.flash1 = 'indexform1' 



    indexform2 = SQLFORM(db.dindexform2, formstyle= 'divs', _class = 'classUnk2', _id= 'idUnk2' )
    #indexform2 = SQLFORM(db.dindexform2,  _class = 'classUnk2', _id= 'idUnk2' )

    indexform2.element('input[name=f0]')['_placeholder']='f0 place_822'
    indexform2.element('input[name=f0]')['_id']='id_for819'
    indexform2.element('input[name=f0]')['_class']='pull-right'
    indexform2.element('input[name=f1]')['_placeholder']='f1 place_826'
    indexform2.element('input[name=f1]')['_id']='id_for823'
    indexform2.element('input[name=f1]')['_class']='pull-right'
    indexform2.element('input[name=f2]')['_placeholder']='f2 place_830'
    indexform2.element('input[name=f2]')['_id']='id_for827'
    indexform2.element('input[name=f2]')['_class']='pull-right'
    indexform2.element('input[name=f3]')['_placeholder']='f3 place_834'
    indexform2.element('input[name=f3]')['_id']='id_for831'
    indexform2.element('input[name=f3]')['_class']='pull-right'
    indexform2.element('input[name=f4]')['_placeholder']='f4 place_838'
    indexform2.element('input[name=f4]')['_id']='id_for835'
    indexform2.element('input[name=f4]')['_class']='pull-right'

    indexform2.custom.submit['_id'] = 'id_for839'
    indexform2.custom.submit['_class'] = 'text-red pull-right'
    indexform2.custom.submit['_title'] = 'submit indexform2'

    if indexform2.accepts(request,session): 
        response.flash2 = 'submitted indexform2' 
    elif indexform2.errors:
        response.flash2 = '!Errors! indexform2' 
    else: 
        response.flash2 = 'indexform2' 


    return dict( DICT= rows_dict, indexform0= indexform0, indexform1= indexform1, indexform2= indexform2, )

#@auth.requires_login()
def general():

    qu= db.dgeneral.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/general.html'


    generalform0 = SQLFORM(db.dgeneralform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #generalform0 = SQLFORM(db.dgeneralform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    generalform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    generalform0.element('input[name=f0]')['_id']='id_for556'
    generalform0.element('input[name=f0]')['_class']='form-control'

    generalform0.custom.submit['_type'] = 'submit'
    generalform0.custom.submit['_id'] = 'search-btn'
    generalform0.custom.submit['_value'] = 'unk_560'
    generalform0.custom.submit['_class'] = 'btn btn-flat'
    generalform0.custom.submit['_title'] = 'submit generalform0'

    if generalform0.accepts(request,session): 
        response.flash0 = 'submitted generalform0' 
    elif generalform0.errors:
        response.flash0 = '!Errors! generalform0' 
    else: 
        response.flash0 = 'generalform0' 



    generalform1 = SQLFORM(db.dgeneralform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #generalform1 = SQLFORM(db.dgeneralform1,  _class = 'classUnk1', _id= 'idUnk1' )

    generalform1.element('input[name=f0]')['_placeholder']='f0 place_565'
    generalform1.element('input[name=f0]')['_id']='id_for562'
    generalform1.element('input[name=f0]')['_class']='pull-right'
    generalform1.element('input[name=f1]')['_placeholder']='f1 place_569'
    generalform1.element('input[name=f1]')['_id']='id_for566'
    generalform1.element('input[name=f1]')['_class']='pull-right'
    generalform1.element('input[name=f2]')['_placeholder']='f2 place_573'
    generalform1.element('input[name=f2]')['_id']='id_for570'
    generalform1.element('input[name=f2]')['_class']='pull-right'
    generalform1.element('input[name=f3]')['_placeholder']='f3 place_577'
    generalform1.element('input[name=f3]')['_id']='id_for574'
    generalform1.element('input[name=f3]')['_class']='pull-right'
    generalform1.element('input[name=f4]')['_placeholder']='f4 place_581'
    generalform1.element('input[name=f4]')['_id']='id_for578'
    generalform1.element('input[name=f4]')['_class']='pull-right'

    generalform1.custom.submit['_id'] = 'id_for582'
    generalform1.custom.submit['_class'] = 'text-red pull-right'
    generalform1.custom.submit['_title'] = 'submit generalform1'

    if generalform1.accepts(request,session): 
        response.flash1 = 'submitted generalform1' 
    elif generalform1.errors:
        response.flash1 = '!Errors! generalform1' 
    else: 
        response.flash1 = 'generalform1' 


    return dict( DICT= rows_dict, generalform0= generalform0, generalform1= generalform1, )

#@auth.requires_login()
def buttons():

    qu= db.dbuttons.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/buttons.html'


    buttonsform0 = SQLFORM(db.dbuttonsform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #buttonsform0 = SQLFORM(db.dbuttonsform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    buttonsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    buttonsform0.element('input[name=f0]')['_id']='id_for0'
    buttonsform0.element('input[name=f0]')['_class']='form-control'

    buttonsform0.custom.submit['_type'] = 'submit'
    buttonsform0.custom.submit['_id'] = 'search-btn'
    buttonsform0.custom.submit['_value'] = 'unk_4'
    buttonsform0.custom.submit['_class'] = 'btn btn-flat'
    buttonsform0.custom.submit['_title'] = 'submit buttonsform0'

    if buttonsform0.accepts(request,session): 
        response.flash0 = 'submitted buttonsform0' 
    elif buttonsform0.errors:
        response.flash0 = '!Errors! buttonsform0' 
    else: 
        response.flash0 = 'buttonsform0' 



    buttonsform1 = SQLFORM(db.dbuttonsform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #buttonsform1 = SQLFORM(db.dbuttonsform1,  _class = 'classUnk1', _id= 'idUnk1' )

    buttonsform1.element('input[name=f0]')['_placeholder']='f0 place_9'
    buttonsform1.element('input[name=f0]')['_id']='id_for6'
    buttonsform1.element('input[name=f0]')['_class']='pull-right'
    buttonsform1.element('input[name=f1]')['_placeholder']='f1 place_13'
    buttonsform1.element('input[name=f1]')['_id']='id_for10'
    buttonsform1.element('input[name=f1]')['_class']='pull-right'
    buttonsform1.element('input[name=f2]')['_placeholder']='f2 place_17'
    buttonsform1.element('input[name=f2]')['_id']='id_for14'
    buttonsform1.element('input[name=f2]')['_class']='pull-right'
    buttonsform1.element('input[name=f3]')['_placeholder']='f3 place_21'
    buttonsform1.element('input[name=f3]')['_id']='id_for18'
    buttonsform1.element('input[name=f3]')['_class']='pull-right'
    buttonsform1.element('input[name=f4]')['_placeholder']='f4 place_25'
    buttonsform1.element('input[name=f4]')['_id']='id_for22'
    buttonsform1.element('input[name=f4]')['_class']='pull-right'

    buttonsform1.custom.submit['_id'] = 'id_for26'
    buttonsform1.custom.submit['_class'] = 'text-red pull-right'
    buttonsform1.custom.submit['_title'] = 'submit buttonsform1'

    if buttonsform1.accepts(request,session): 
        response.flash1 = 'submitted buttonsform1' 
    elif buttonsform1.errors:
        response.flash1 = '!Errors! buttonsform1' 
    else: 
        response.flash1 = 'buttonsform1' 


    return dict( DICT= rows_dict, buttonsform0= buttonsform0, buttonsform1= buttonsform1, )

#@auth.requires_login()
def readIImail():

    qu= db.dread0mail.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/read-mail.html'


    readIImailform0 = SQLFORM(db.dreadIImailform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #readIImailform0 = SQLFORM(db.dreadIImailform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    readIImailform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    readIImailform0.element('input[name=f0]')['_id']='id_for312'
    readIImailform0.element('input[name=f0]')['_class']='form-control'

    readIImailform0.custom.submit['_type'] = 'submit'
    readIImailform0.custom.submit['_id'] = 'search-btn'
    readIImailform0.custom.submit['_value'] = 'unk_316'
    readIImailform0.custom.submit['_class'] = 'btn btn-flat'
    readIImailform0.custom.submit['_title'] = 'submit readIImailform0'

    if readIImailform0.accepts(request,session): 
        response.flash0 = 'submitted readIImailform0' 
    elif readIImailform0.errors:
        response.flash0 = '!Errors! readIImailform0' 
    else: 
        response.flash0 = 'readIImailform0' 



    readIImailform1 = SQLFORM(db.dreadIImailform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #readIImailform1 = SQLFORM(db.dreadIImailform1,  _class = 'classUnk1', _id= 'idUnk1' )

    readIImailform1.element('input[name=f0]')['_placeholder']='f0 place_321'
    readIImailform1.element('input[name=f0]')['_id']='id_for318'
    readIImailform1.element('input[name=f0]')['_class']='pull-right'
    readIImailform1.element('input[name=f1]')['_placeholder']='f1 place_325'
    readIImailform1.element('input[name=f1]')['_id']='id_for322'
    readIImailform1.element('input[name=f1]')['_class']='pull-right'
    readIImailform1.element('input[name=f2]')['_placeholder']='f2 place_329'
    readIImailform1.element('input[name=f2]')['_id']='id_for326'
    readIImailform1.element('input[name=f2]')['_class']='pull-right'
    readIImailform1.element('input[name=f3]')['_placeholder']='f3 place_333'
    readIImailform1.element('input[name=f3]')['_id']='id_for330'
    readIImailform1.element('input[name=f3]')['_class']='pull-right'
    readIImailform1.element('input[name=f4]')['_placeholder']='f4 place_337'
    readIImailform1.element('input[name=f4]')['_id']='id_for334'
    readIImailform1.element('input[name=f4]')['_class']='pull-right'

    readIImailform1.custom.submit['_id'] = 'id_for338'
    readIImailform1.custom.submit['_class'] = 'text-red pull-right'
    readIImailform1.custom.submit['_title'] = 'submit readIImailform1'

    if readIImailform1.accepts(request,session): 
        response.flash1 = 'submitted readIImailform1' 
    elif readIImailform1.errors:
        response.flash1 = '!Errors! readIImailform1' 
    else: 
        response.flash1 = 'readIImailform1' 


    return dict( DICT= rows_dict, readIImailform0= readIImailform0, readIImailform1= readIImailform1, )

#@auth.requires_login()
def simple():

    qu= db.dsimple.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/simple.html'


    simpleform0 = SQLFORM(db.dsimpleform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #simpleform0 = SQLFORM(db.dsimpleform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    simpleform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    simpleform0.element('input[name=f0]')['_id']='id_for182'
    simpleform0.element('input[name=f0]')['_class']='form-control'

    simpleform0.custom.submit['_type'] = 'submit'
    simpleform0.custom.submit['_id'] = 'search-btn'
    simpleform0.custom.submit['_value'] = 'unk_186'
    simpleform0.custom.submit['_class'] = 'btn btn-flat'
    simpleform0.custom.submit['_title'] = 'submit simpleform0'

    if simpleform0.accepts(request,session): 
        response.flash0 = 'submitted simpleform0' 
    elif simpleform0.errors:
        response.flash0 = '!Errors! simpleform0' 
    else: 
        response.flash0 = 'simpleform0' 



    simpleform1 = SQLFORM(db.dsimpleform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #simpleform1 = SQLFORM(db.dsimpleform1,  _class = 'classUnk1', _id= 'idUnk1' )

    simpleform1.element('input[name=f0]')['_placeholder']='f0 place_191'
    simpleform1.element('input[name=f0]')['_id']='id_for188'
    simpleform1.element('input[name=f0]')['_class']='pull-right'
    simpleform1.element('input[name=f1]')['_placeholder']='f1 place_195'
    simpleform1.element('input[name=f1]')['_id']='id_for192'
    simpleform1.element('input[name=f1]')['_class']='pull-right'
    simpleform1.element('input[name=f2]')['_placeholder']='f2 place_199'
    simpleform1.element('input[name=f2]')['_id']='id_for196'
    simpleform1.element('input[name=f2]')['_class']='pull-right'
    simpleform1.element('input[name=f3]')['_placeholder']='f3 place_203'
    simpleform1.element('input[name=f3]')['_id']='id_for200'
    simpleform1.element('input[name=f3]')['_class']='pull-right'
    simpleform1.element('input[name=f4]')['_placeholder']='f4 place_207'
    simpleform1.element('input[name=f4]')['_id']='id_for204'
    simpleform1.element('input[name=f4]')['_class']='pull-right'

    simpleform1.custom.submit['_id'] = 'id_for208'
    simpleform1.custom.submit['_class'] = 'text-red pull-right'
    simpleform1.custom.submit['_title'] = 'submit simpleform1'

    if simpleform1.accepts(request,session): 
        response.flash1 = 'submitted simpleform1' 
    elif simpleform1.errors:
        response.flash1 = '!Errors! simpleform1' 
    else: 
        response.flash1 = 'simpleform1' 


    return dict( DICT= rows_dict, simpleform0= simpleform0, simpleform1= simpleform1, )

#@auth.requires_login()
def data():

    qu= db.ddata.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/data.html'


    dataform0 = SQLFORM(db.ddataform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #dataform0 = SQLFORM(db.ddataform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    dataform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    dataform0.element('input[name=f0]')['_id']='id_for432'
    dataform0.element('input[name=f0]')['_class']='form-control'

    dataform0.custom.submit['_type'] = 'submit'
    dataform0.custom.submit['_id'] = 'search-btn'
    dataform0.custom.submit['_value'] = 'unk_436'
    dataform0.custom.submit['_class'] = 'btn btn-flat'
    dataform0.custom.submit['_title'] = 'submit dataform0'

    if dataform0.accepts(request,session): 
        response.flash0 = 'submitted dataform0' 
    elif dataform0.errors:
        response.flash0 = '!Errors! dataform0' 
    else: 
        response.flash0 = 'dataform0' 



    dataform1 = SQLFORM(db.ddataform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #dataform1 = SQLFORM(db.ddataform1,  _class = 'classUnk1', _id= 'idUnk1' )

    dataform1.element('input[name=f0]')['_placeholder']='f0 place_441'
    dataform1.element('input[name=f0]')['_id']='id_for438'
    dataform1.element('input[name=f0]')['_class']='pull-right'
    dataform1.element('input[name=f1]')['_placeholder']='f1 place_445'
    dataform1.element('input[name=f1]')['_id']='id_for442'
    dataform1.element('input[name=f1]')['_class']='pull-right'
    dataform1.element('input[name=f2]')['_placeholder']='f2 place_449'
    dataform1.element('input[name=f2]')['_id']='id_for446'
    dataform1.element('input[name=f2]')['_class']='pull-right'
    dataform1.element('input[name=f3]')['_placeholder']='f3 place_453'
    dataform1.element('input[name=f3]')['_id']='id_for450'
    dataform1.element('input[name=f3]')['_class']='pull-right'
    dataform1.element('input[name=f4]')['_placeholder']='f4 place_457'
    dataform1.element('input[name=f4]')['_id']='id_for454'
    dataform1.element('input[name=f4]')['_class']='pull-right'

    dataform1.custom.submit['_id'] = 'id_for458'
    dataform1.custom.submit['_class'] = 'text-red pull-right'
    dataform1.custom.submit['_title'] = 'submit dataform1'

    if dataform1.accepts(request,session): 
        response.flash1 = 'submitted dataform1' 
    elif dataform1.errors:
        response.flash1 = '!Errors! dataform1' 
    else: 
        response.flash1 = 'dataform1' 


    return dict( DICT= rows_dict, dataform0= dataform0, dataform1= dataform1, )

#@auth.requires_login()
def inline():

    qu= db.dinline.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/inline.html'


    inlineform0 = SQLFORM(db.dinlineform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #inlineform0 = SQLFORM(db.dinlineform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    inlineform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    inlineform0.element('input[name=f0]')['_id']='id_for878'
    inlineform0.element('input[name=f0]')['_class']='form-control'

    inlineform0.custom.submit['_type'] = 'submit'
    inlineform0.custom.submit['_id'] = 'search-btn'
    inlineform0.custom.submit['_value'] = 'unk_882'
    inlineform0.custom.submit['_class'] = 'btn btn-flat'
    inlineform0.custom.submit['_title'] = 'submit inlineform0'

    if inlineform0.accepts(request,session): 
        response.flash0 = 'submitted inlineform0' 
    elif inlineform0.errors:
        response.flash0 = '!Errors! inlineform0' 
    else: 
        response.flash0 = 'inlineform0' 



    inlineform1 = SQLFORM(db.dinlineform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #inlineform1 = SQLFORM(db.dinlineform1,  _class = 'classUnk1', _id= 'idUnk1' )

    inlineform1.element('input[name=f0]')['_placeholder']='f0 place_887'
    inlineform1.element('input[name=f0]')['_id']='id_for884'
    inlineform1.element('input[name=f0]')['_class']='pull-right'
    inlineform1.element('input[name=f1]')['_placeholder']='f1 place_891'
    inlineform1.element('input[name=f1]')['_id']='id_for888'
    inlineform1.element('input[name=f1]')['_class']='pull-right'
    inlineform1.element('input[name=f2]')['_placeholder']='f2 place_895'
    inlineform1.element('input[name=f2]')['_id']='id_for892'
    inlineform1.element('input[name=f2]')['_class']='pull-right'
    inlineform1.element('input[name=f3]')['_placeholder']='f3 place_899'
    inlineform1.element('input[name=f3]')['_id']='id_for896'
    inlineform1.element('input[name=f3]')['_class']='pull-right'
    inlineform1.element('input[name=f4]')['_placeholder']='f4 place_903'
    inlineform1.element('input[name=f4]')['_id']='id_for900'
    inlineform1.element('input[name=f4]')['_class']='pull-right'

    inlineform1.custom.submit['_id'] = 'id_for904'
    inlineform1.custom.submit['_class'] = 'text-red pull-right'
    inlineform1.custom.submit['_title'] = 'submit inlineform1'

    if inlineform1.accepts(request,session): 
        response.flash1 = 'submitted inlineform1' 
    elif inlineform1.errors:
        response.flash1 = '!Errors! inlineform1' 
    else: 
        response.flash1 = 'inlineform1' 


    return dict( DICT= rows_dict, inlineform0= inlineform0, inlineform1= inlineform1, )

#@auth.requires_login()
def login():

    qu= db.dlogin.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/login.html'


    loginform0 = SQLFORM(db.dloginform0, formstyle= 'divs', _class = 'classUnk0', _id= 'idUnk0' )
    #loginform0 = SQLFORM(db.dloginform0,  _class = 'classUnk0', _id= 'idUnk0' )

    loginform0.element('input[name=f0]')['_placeholder']='f0 Email'
    loginform0.element('input[name=f0]')['_id']='id_for168'
    loginform0.element('input[name=f0]')['_class']='form-control'
    loginform0.element('input[name=f1]')['_placeholder']='f1 Password'
    loginform0.element('input[name=f1]')['_id']='id_for171'
    loginform0.element('input[name=f1]')['_class']='form-control'
    loginform0.element('input[name=f2]')['_placeholder']='f2 place_177'
    loginform0.element('input[name=f2]')['_id']='id_for174'

    loginform0.custom.submit['_type'] = 'submit'
    loginform0.custom.submit['_id'] = 'id_for178'
    loginform0.custom.submit['_value'] = 'Sign In'
    loginform0.custom.submit['_class'] = 'btn btn-primary btn-block btn-flat'
    loginform0.custom.submit['_title'] = 'submit loginform0'

    if loginform0.accepts(request,session): 
        response.flash0 = 'submitted loginform0' 
    elif loginform0.errors:
        response.flash0 = '!Errors! loginform0' 
    else: 
        response.flash0 = 'loginform0' 


    return dict( DICT= rows_dict, loginform0= loginform0, )

#@auth.requires_login()
def profile():

    qu= db.dprofile.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/profile.html'


    profileform0 = SQLFORM(db.dprofileform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #profileform0 = SQLFORM(db.dprofileform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    profileform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    profileform0.element('input[name=f0]')['_id']='id_for498'
    profileform0.element('input[name=f0]')['_class']='form-control'

    profileform0.custom.submit['_type'] = 'submit'
    profileform0.custom.submit['_id'] = 'search-btn'
    profileform0.custom.submit['_value'] = 'unk_502'
    profileform0.custom.submit['_class'] = 'btn btn-flat'
    profileform0.custom.submit['_title'] = 'submit profileform0'

    if profileform0.accepts(request,session): 
        response.flash0 = 'submitted profileform0' 
    elif profileform0.errors:
        response.flash0 = '!Errors! profileform0' 
    else: 
        response.flash0 = 'profileform0' 



    profileform1 = SQLFORM(db.dprofileform1, formstyle= 'divs', _class = 'form-horizontal', _id= 'idUnk1' )
    #profileform1 = SQLFORM(db.dprofileform1,  _class = 'form-horizontal', _id= 'idUnk1' )

    profileform1.element('input[name=f0]')['_placeholder']='f0 Response'
    profileform1.element('input[name=f0]')['_id']='id_for504'
    profileform1.element('input[name=f0]')['_class']='form-control input-sm'

    profileform1.custom.submit['_type'] = 'submit'
    profileform1.custom.submit['_id'] = 'id_for506'
    profileform1.custom.submit['_value'] = 'Send'
    profileform1.custom.submit['_class'] = 'btn btn-danger pull-right btn-block btn-sm'
    profileform1.custom.submit['_title'] = 'submit profileform1'

    if profileform1.accepts(request,session): 
        response.flash1 = 'submitted profileform1' 
    elif profileform1.errors:
        response.flash1 = '!Errors! profileform1' 
    else: 
        response.flash1 = 'profileform1' 



    profileform2 = SQLFORM(db.dprofileform2, formstyle= 'divs', _class = 'form-horizontal', _id= 'idUnk2' )
    #profileform2 = SQLFORM(db.dprofileform2,  _class = 'form-horizontal', _id= 'idUnk2' )

    profileform2.element('input[name=f0]')['_placeholder']='f0 Name'
    profileform2.element('input[name=f0]')['_id']='inputName'
    profileform2.element('input[name=f0]')['_class']='form-control'
    profileform2.element('input[name=f1]')['_placeholder']='f1 Email'
    profileform2.element('input[name=f1]')['_id']='inputEmail'
    profileform2.element('input[name=f1]')['_class']='form-control'
    profileform2.element('input[name=f2]')['_placeholder']='f2 Name'
    profileform2.element('input[name=f2]')['_id']='inputName'
    profileform2.element('input[name=f2]')['_class']='form-control'
    profileform2.element('input[name=f3]')['_placeholder']='f3 Skills'
    profileform2.element('input[name=f3]')['_id']='inputSkills'
    profileform2.element('input[name=f3]')['_class']='form-control'
    profileform2.element('input[name=f4]')['_placeholder']='f4 place_520'
    profileform2.element('input[name=f4]')['_id']='id_for517'
    profileform2.element('textarea[name=f5]')['_placeholder']='f5 Experience'
    profileform2.element('textarea[name=f5]')['_id']='inputExperience'
    profileform2.element('textarea[name=f5]')['_class']='form-control'

    profileform2.custom.submit['_type'] = 'submit'
    profileform2.custom.submit['_id'] = 'id_for523'
    profileform2.custom.submit['_value'] = 'Submit'
    profileform2.custom.submit['_class'] = 'btn btn-danger'
    profileform2.custom.submit['_title'] = 'submit profileform2'

    profileform2.custom.submit['_id'] = 'id_for526'
    profileform2.custom.submit['_title'] = 'submit profileform2'

    if profileform2.accepts(request,session): 
        response.flash2 = 'submitted profileform2' 
    elif profileform2.errors:
        response.flash2 = '!Errors! profileform2' 
    else: 
        response.flash2 = 'profileform2' 



    profileform3 = SQLFORM(db.dprofileform3, formstyle= 'divs', _class = 'classUnk3', _id= 'idUnk3' )
    #profileform3 = SQLFORM(db.dprofileform3,  _class = 'classUnk3', _id= 'idUnk3' )

    profileform3.element('input[name=f0]')['_placeholder']='f0 place_533'
    profileform3.element('input[name=f0]')['_id']='id_for530'
    profileform3.element('input[name=f0]')['_class']='pull-right'
    profileform3.element('input[name=f1]')['_placeholder']='f1 place_537'
    profileform3.element('input[name=f1]')['_id']='id_for534'
    profileform3.element('input[name=f1]')['_class']='pull-right'
    profileform3.element('input[name=f2]')['_placeholder']='f2 place_541'
    profileform3.element('input[name=f2]')['_id']='id_for538'
    profileform3.element('input[name=f2]')['_class']='pull-right'
    profileform3.element('input[name=f3]')['_placeholder']='f3 place_545'
    profileform3.element('input[name=f3]')['_id']='id_for542'
    profileform3.element('input[name=f3]')['_class']='pull-right'
    profileform3.element('input[name=f4]')['_placeholder']='f4 place_549'
    profileform3.element('input[name=f4]')['_id']='id_for546'
    profileform3.element('input[name=f4]')['_class']='pull-right'

    profileform3.custom.submit['_id'] = 'id_for550'
    profileform3.custom.submit['_class'] = 'text-red pull-right'
    profileform3.custom.submit['_title'] = 'submit profileform3'

    if profileform3.accepts(request,session): 
        response.flash3 = 'submitted profileform3' 
    elif profileform3.errors:
        response.flash3 = '!Errors! profileform3' 
    else: 
        response.flash3 = 'profileform3' 


    return dict( DICT= rows_dict, profileform0= profileform0, profileform1= profileform1, profileform2= profileform2, profileform3= profileform3, )

#@auth.requires_login()
def editors():

    qu= db.deditors.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/editors.html'


    editorsform0 = SQLFORM(db.deditorsform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #editorsform0 = SQLFORM(db.deditorsform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    editorsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    editorsform0.element('input[name=f0]')['_id']='id_for676'
    editorsform0.element('input[name=f0]')['_class']='form-control'

    editorsform0.custom.submit['_type'] = 'submit'
    editorsform0.custom.submit['_id'] = 'search-btn'
    editorsform0.custom.submit['_value'] = 'unk_680'
    editorsform0.custom.submit['_class'] = 'btn btn-flat'
    editorsform0.custom.submit['_title'] = 'submit editorsform0'

    if editorsform0.accepts(request,session): 
        response.flash0 = 'submitted editorsform0' 
    elif editorsform0.errors:
        response.flash0 = '!Errors! editorsform0' 
    else: 
        response.flash0 = 'editorsform0' 



    editorsform1 = SQLFORM(db.deditorsform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #editorsform1 = SQLFORM(db.deditorsform1,  _class = 'classUnk1', _id= 'idUnk1' )

    editorsform1.element('textarea[name=f0]')['_rows']='10'
    editorsform1.element('textarea[name=f0]')['_placeholder']='f0 place_684'
    editorsform1.element('textarea[name=f0]')['_id']='editor1'

    editorsform1.custom.submit['_rows'] = '10'
    editorsform1.custom.submit['_value'] = 'submit textarea'
    editorsform1.custom.submit['_class'] = 'unk-class'
    editorsform1.custom.submit['_type'] = 'submit'
    editorsform1.custom.submit['_id'] = 'unk-id'
    editorsform1.custom.submit['_title'] = 'submit editorsform1'

    if editorsform1.accepts(request,session): 
        response.flash1 = 'submitted editorsform1' 
    elif editorsform1.errors:
        response.flash1 = '!Errors! editorsform1' 
    else: 
        response.flash1 = 'editorsform1' 



    editorsform2 = SQLFORM(db.deditorsform2, formstyle= 'divs', _class = 'classUnk2', _id= 'idUnk2' )
    #editorsform2 = SQLFORM(db.deditorsform2,  _class = 'classUnk2', _id= 'idUnk2' )

    editorsform2.element('textarea[name=f0]')['_placeholder']='f0 Place some text here'
    editorsform2.element('textarea[name=f0]')['_id']='id_for685'
    editorsform2.element('textarea[name=f0]')['_class']='textarea'

    editorsform2.custom.submit['_type'] = 'submit'
    editorsform2.custom.submit['_id'] = 'unk-id'
    editorsform2.custom.submit['_value'] = 'submit textarea'
    editorsform2.custom.submit['_class'] = 'unk-class'
    editorsform2.custom.submit['_title'] = 'submit editorsform2'

    if editorsform2.accepts(request,session): 
        response.flash2 = 'submitted editorsform2' 
    elif editorsform2.errors:
        response.flash2 = '!Errors! editorsform2' 
    else: 
        response.flash2 = 'editorsform2' 



    editorsform3 = SQLFORM(db.deditorsform3, formstyle= 'divs', _class = 'classUnk3', _id= 'idUnk3' )
    #editorsform3 = SQLFORM(db.deditorsform3,  _class = 'classUnk3', _id= 'idUnk3' )

    editorsform3.element('input[name=f0]')['_placeholder']='f0 place_690'
    editorsform3.element('input[name=f0]')['_id']='id_for687'
    editorsform3.element('input[name=f0]')['_class']='pull-right'
    editorsform3.element('input[name=f1]')['_placeholder']='f1 place_694'
    editorsform3.element('input[name=f1]')['_id']='id_for691'
    editorsform3.element('input[name=f1]')['_class']='pull-right'
    editorsform3.element('input[name=f2]')['_placeholder']='f2 place_698'
    editorsform3.element('input[name=f2]')['_id']='id_for695'
    editorsform3.element('input[name=f2]')['_class']='pull-right'
    editorsform3.element('input[name=f3]')['_placeholder']='f3 place_702'
    editorsform3.element('input[name=f3]')['_id']='id_for699'
    editorsform3.element('input[name=f3]')['_class']='pull-right'
    editorsform3.element('input[name=f4]')['_placeholder']='f4 place_706'
    editorsform3.element('input[name=f4]')['_id']='id_for703'
    editorsform3.element('input[name=f4]')['_class']='pull-right'

    editorsform3.custom.submit['_id'] = 'id_for707'
    editorsform3.custom.submit['_class'] = 'text-red pull-right'
    editorsform3.custom.submit['_title'] = 'submit editorsform3'

    if editorsform3.accepts(request,session): 
        response.flash3 = 'submitted editorsform3' 
    elif editorsform3.errors:
        response.flash3 = '!Errors! editorsform3' 
    else: 
        response.flash3 = 'editorsform3' 


    return dict( DICT= rows_dict, editorsform0= editorsform0, editorsform1= editorsform1, editorsform2= editorsform2, editorsform3= editorsform3, )

#@auth.requires_login()
def invoice():

    qu= db.dinvoice.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/invoice.html'


    invoiceform0 = SQLFORM(db.dinvoiceform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #invoiceform0 = SQLFORM(db.dinvoiceform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    invoiceform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    invoiceform0.element('input[name=f0]')['_id']='id_for84'
    invoiceform0.element('input[name=f0]')['_class']='form-control'

    invoiceform0.custom.submit['_type'] = 'submit'
    invoiceform0.custom.submit['_id'] = 'search-btn'
    invoiceform0.custom.submit['_value'] = 'unk_88'
    invoiceform0.custom.submit['_class'] = 'btn btn-flat'
    invoiceform0.custom.submit['_title'] = 'submit invoiceform0'

    if invoiceform0.accepts(request,session): 
        response.flash0 = 'submitted invoiceform0' 
    elif invoiceform0.errors:
        response.flash0 = '!Errors! invoiceform0' 
    else: 
        response.flash0 = 'invoiceform0' 



    invoiceform1 = SQLFORM(db.dinvoiceform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #invoiceform1 = SQLFORM(db.dinvoiceform1,  _class = 'classUnk1', _id= 'idUnk1' )

    invoiceform1.element('input[name=f0]')['_placeholder']='f0 place_93'
    invoiceform1.element('input[name=f0]')['_id']='id_for90'
    invoiceform1.element('input[name=f0]')['_class']='pull-right'
    invoiceform1.element('input[name=f1]')['_placeholder']='f1 place_97'
    invoiceform1.element('input[name=f1]')['_id']='id_for94'
    invoiceform1.element('input[name=f1]')['_class']='pull-right'
    invoiceform1.element('input[name=f2]')['_placeholder']='f2 place_101'
    invoiceform1.element('input[name=f2]')['_id']='id_for98'
    invoiceform1.element('input[name=f2]')['_class']='pull-right'
    invoiceform1.element('input[name=f3]')['_placeholder']='f3 place_105'
    invoiceform1.element('input[name=f3]')['_id']='id_for102'
    invoiceform1.element('input[name=f3]')['_class']='pull-right'
    invoiceform1.element('input[name=f4]')['_placeholder']='f4 place_109'
    invoiceform1.element('input[name=f4]')['_id']='id_for106'
    invoiceform1.element('input[name=f4]')['_class']='pull-right'

    invoiceform1.custom.submit['_id'] = 'id_for110'
    invoiceform1.custom.submit['_class'] = 'text-red pull-right'
    invoiceform1.custom.submit['_title'] = 'submit invoiceform1'

    if invoiceform1.accepts(request,session): 
        response.flash1 = 'submitted invoiceform1' 
    elif invoiceform1.errors:
        response.flash1 = '!Errors! invoiceform1' 
    else: 
        response.flash1 = 'invoiceform1' 


    return dict( DICT= rows_dict, invoiceform0= invoiceform0, invoiceform1= invoiceform1, )

#@auth.requires_login()
def lockscreen():

    qu= db.dlockscreen.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/lockscreen.html'


    lockscreenform0 = SQLFORM(db.dlockscreenform0, formstyle= 'divs', _class = 'lockscreen-credentials', _id= 'idUnk0' )
    #lockscreenform0 = SQLFORM(db.dlockscreenform0,  _class = 'lockscreen-credentials', _id= 'idUnk0' )

    lockscreenform0.element('input[name=f0]')['_placeholder']='f0 password'
    lockscreenform0.element('input[name=f0]')['_id']='id_for741'
    lockscreenform0.element('input[name=f0]')['_class']='form-control'

    lockscreenform0.custom.submit['_type'] = 'submit'
    lockscreenform0.custom.submit['_id'] = 'id_for743'
    lockscreenform0.custom.submit['_value'] = 'unk_745'
    lockscreenform0.custom.submit['_class'] = 'btn'
    lockscreenform0.custom.submit['_title'] = 'submit lockscreenform0'

    if lockscreenform0.accepts(request,session): 
        response.flash0 = 'submitted lockscreenform0' 
    elif lockscreenform0.errors:
        response.flash0 = '!Errors! lockscreenform0' 
    else: 
        response.flash0 = 'lockscreenform0' 


    return dict( DICT= rows_dict, lockscreenform0= lockscreenform0, )

#@auth.requires_login()
def compose():

    qu= db.dcompose.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/compose.html'


    composeform0 = SQLFORM(db.dcomposeform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #composeform0 = SQLFORM(db.dcomposeform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    composeform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    composeform0.element('input[name=f0]')['_id']='id_for1004'
    composeform0.element('input[name=f0]')['_class']='form-control'

    composeform0.custom.submit['_type'] = 'submit'
    composeform0.custom.submit['_id'] = 'search-btn'
    composeform0.custom.submit['_value'] = 'unk_1008'
    composeform0.custom.submit['_class'] = 'btn btn-flat'
    composeform0.custom.submit['_title'] = 'submit composeform0'

    if composeform0.accepts(request,session): 
        response.flash0 = 'submitted composeform0' 
    elif composeform0.errors:
        response.flash0 = '!Errors! composeform0' 
    else: 
        response.flash0 = 'composeform0' 



    composeform1 = SQLFORM(db.dcomposeform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #composeform1 = SQLFORM(db.dcomposeform1,  _class = 'classUnk1', _id= 'idUnk1' )

    composeform1.element('input[name=f0]')['_placeholder']='f0 place_1013'
    composeform1.element('input[name=f0]')['_id']='id_for1010'
    composeform1.element('input[name=f0]')['_class']='pull-right'
    composeform1.element('input[name=f1]')['_placeholder']='f1 place_1017'
    composeform1.element('input[name=f1]')['_id']='id_for1014'
    composeform1.element('input[name=f1]')['_class']='pull-right'
    composeform1.element('input[name=f2]')['_placeholder']='f2 place_1021'
    composeform1.element('input[name=f2]')['_id']='id_for1018'
    composeform1.element('input[name=f2]')['_class']='pull-right'
    composeform1.element('input[name=f3]')['_placeholder']='f3 place_1025'
    composeform1.element('input[name=f3]')['_id']='id_for1022'
    composeform1.element('input[name=f3]')['_class']='pull-right'
    composeform1.element('input[name=f4]')['_placeholder']='f4 place_1029'
    composeform1.element('input[name=f4]')['_id']='id_for1026'
    composeform1.element('input[name=f4]')['_class']='pull-right'

    composeform1.custom.submit['_id'] = 'id_for1030'
    composeform1.custom.submit['_class'] = 'text-red pull-right'
    composeform1.custom.submit['_title'] = 'submit composeform1'

    if composeform1.accepts(request,session): 
        response.flash1 = 'submitted composeform1' 
    elif composeform1.errors:
        response.flash1 = '!Errors! composeform1' 
    else: 
        response.flash1 = 'composeform1' 


    return dict( DICT= rows_dict, composeform0= composeform0, composeform1= composeform1, )

#@auth.requires_login()
def blank():

    qu= db.dblank.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/blank.html'


    blankform0 = SQLFORM(db.dblankform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #blankform0 = SQLFORM(db.dblankform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    blankform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    blankform0.element('input[name=f0]')['_id']='id_for342'
    blankform0.element('input[name=f0]')['_class']='form-control'

    blankform0.custom.submit['_type'] = 'submit'
    blankform0.custom.submit['_id'] = 'search-btn'
    blankform0.custom.submit['_value'] = 'unk_346'
    blankform0.custom.submit['_class'] = 'btn btn-flat'
    blankform0.custom.submit['_title'] = 'submit blankform0'

    if blankform0.accepts(request,session): 
        response.flash0 = 'submitted blankform0' 
    elif blankform0.errors:
        response.flash0 = '!Errors! blankform0' 
    else: 
        response.flash0 = 'blankform0' 



    blankform1 = SQLFORM(db.dblankform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #blankform1 = SQLFORM(db.dblankform1,  _class = 'classUnk1', _id= 'idUnk1' )

    blankform1.element('input[name=f0]')['_placeholder']='f0 place_351'
    blankform1.element('input[name=f0]')['_id']='id_for348'
    blankform1.element('input[name=f0]')['_class']='pull-right'
    blankform1.element('input[name=f1]')['_placeholder']='f1 place_355'
    blankform1.element('input[name=f1]')['_id']='id_for352'
    blankform1.element('input[name=f1]')['_class']='pull-right'
    blankform1.element('input[name=f2]')['_placeholder']='f2 place_359'
    blankform1.element('input[name=f2]')['_id']='id_for356'
    blankform1.element('input[name=f2]')['_class']='pull-right'
    blankform1.element('input[name=f3]')['_placeholder']='f3 place_363'
    blankform1.element('input[name=f3]')['_id']='id_for360'
    blankform1.element('input[name=f3]')['_class']='pull-right'
    blankform1.element('input[name=f4]')['_placeholder']='f4 place_367'
    blankform1.element('input[name=f4]')['_id']='id_for364'
    blankform1.element('input[name=f4]')['_class']='pull-right'

    blankform1.custom.submit['_id'] = 'id_for368'
    blankform1.custom.submit['_class'] = 'text-red pull-right'
    blankform1.custom.submit['_title'] = 'submit blankform1'

    if blankform1.accepts(request,session): 
        response.flash1 = 'submitted blankform1' 
    elif blankform1.errors:
        response.flash1 = '!Errors! blankform1' 
    else: 
        response.flash1 = 'blankform1' 


    return dict( DICT= rows_dict, blankform0= blankform0, blankform1= blankform1, )

#@auth.requires_login()
def morris():

    qu= db.dmorris.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/morris.html'


    morrisform0 = SQLFORM(db.dmorrisform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #morrisform0 = SQLFORM(db.dmorrisform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    morrisform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    morrisform0.element('input[name=f0]')['_id']='id_for777'
    morrisform0.element('input[name=f0]')['_class']='form-control'

    morrisform0.custom.submit['_type'] = 'submit'
    morrisform0.custom.submit['_id'] = 'search-btn'
    morrisform0.custom.submit['_value'] = 'unk_781'
    morrisform0.custom.submit['_class'] = 'btn btn-flat'
    morrisform0.custom.submit['_title'] = 'submit morrisform0'

    if morrisform0.accepts(request,session): 
        response.flash0 = 'submitted morrisform0' 
    elif morrisform0.errors:
        response.flash0 = '!Errors! morrisform0' 
    else: 
        response.flash0 = 'morrisform0' 



    morrisform1 = SQLFORM(db.dmorrisform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #morrisform1 = SQLFORM(db.dmorrisform1,  _class = 'classUnk1', _id= 'idUnk1' )

    morrisform1.element('input[name=f0]')['_placeholder']='f0 place_786'
    morrisform1.element('input[name=f0]')['_id']='id_for783'
    morrisform1.element('input[name=f0]')['_class']='pull-right'
    morrisform1.element('input[name=f1]')['_placeholder']='f1 place_790'
    morrisform1.element('input[name=f1]')['_id']='id_for787'
    morrisform1.element('input[name=f1]')['_class']='pull-right'
    morrisform1.element('input[name=f2]')['_placeholder']='f2 place_794'
    morrisform1.element('input[name=f2]')['_id']='id_for791'
    morrisform1.element('input[name=f2]')['_class']='pull-right'
    morrisform1.element('input[name=f3]')['_placeholder']='f3 place_798'
    morrisform1.element('input[name=f3]')['_id']='id_for795'
    morrisform1.element('input[name=f3]')['_class']='pull-right'
    morrisform1.element('input[name=f4]')['_placeholder']='f4 place_802'
    morrisform1.element('input[name=f4]')['_id']='id_for799'
    morrisform1.element('input[name=f4]')['_class']='pull-right'

    morrisform1.custom.submit['_id'] = 'id_for803'
    morrisform1.custom.submit['_class'] = 'text-red pull-right'
    morrisform1.custom.submit['_title'] = 'submit morrisform1'

    if morrisform1.accepts(request,session): 
        response.flash1 = 'submitted morrisform1' 
    elif morrisform1.errors:
        response.flash1 = '!Errors! morrisform1' 
    else: 
        response.flash1 = 'morrisform1' 


    return dict( DICT= rows_dict, morrisform0= morrisform0, morrisform1= morrisform1, )

#@auth.requires_login()
def icons():

    qu= db.dicons.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/icons.html'


    iconsform0 = SQLFORM(db.diconsform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #iconsform0 = SQLFORM(db.diconsform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    iconsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    iconsform0.element('input[name=f0]')['_id']='id_for402'
    iconsform0.element('input[name=f0]')['_class']='form-control'

    iconsform0.custom.submit['_type'] = 'submit'
    iconsform0.custom.submit['_id'] = 'search-btn'
    iconsform0.custom.submit['_value'] = 'unk_406'
    iconsform0.custom.submit['_class'] = 'btn btn-flat'
    iconsform0.custom.submit['_title'] = 'submit iconsform0'

    if iconsform0.accepts(request,session): 
        response.flash0 = 'submitted iconsform0' 
    elif iconsform0.errors:
        response.flash0 = '!Errors! iconsform0' 
    else: 
        response.flash0 = 'iconsform0' 



    iconsform1 = SQLFORM(db.diconsform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #iconsform1 = SQLFORM(db.diconsform1,  _class = 'classUnk1', _id= 'idUnk1' )

    iconsform1.element('input[name=f0]')['_placeholder']='f0 place_411'
    iconsform1.element('input[name=f0]')['_id']='id_for408'
    iconsform1.element('input[name=f0]')['_class']='pull-right'
    iconsform1.element('input[name=f1]')['_placeholder']='f1 place_415'
    iconsform1.element('input[name=f1]')['_id']='id_for412'
    iconsform1.element('input[name=f1]')['_class']='pull-right'
    iconsform1.element('input[name=f2]')['_placeholder']='f2 place_419'
    iconsform1.element('input[name=f2]')['_id']='id_for416'
    iconsform1.element('input[name=f2]')['_class']='pull-right'
    iconsform1.element('input[name=f3]')['_placeholder']='f3 place_423'
    iconsform1.element('input[name=f3]')['_id']='id_for420'
    iconsform1.element('input[name=f3]')['_class']='pull-right'
    iconsform1.element('input[name=f4]')['_placeholder']='f4 place_427'
    iconsform1.element('input[name=f4]')['_id']='id_for424'
    iconsform1.element('input[name=f4]')['_class']='pull-right'

    iconsform1.custom.submit['_id'] = 'id_for428'
    iconsform1.custom.submit['_class'] = 'text-red pull-right'
    iconsform1.custom.submit['_title'] = 'submit iconsform1'

    if iconsform1.accepts(request,session): 
        response.flash1 = 'submitted iconsform1' 
    elif iconsform1.errors:
        response.flash1 = '!Errors! iconsform1' 
    else: 
        response.flash1 = 'iconsform1' 


    return dict( DICT= rows_dict, iconsform0= iconsform0, iconsform1= iconsform1, )

#@auth.requires_login()
def invoiceIIprint():

    qu= db.dinvoice0print.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/invoice-print.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def topIInav():

    qu= db.dtop0nav.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/top-nav.html'


    topIInavform0 = SQLFORM(db.dtopIInavform0, formstyle= 'divs', _class = 'navbar-form navbar-left', _id= 'idUnk0' )
    #topIInavform0 = SQLFORM(db.dtopIInavform0,  _class = 'navbar-form navbar-left', _id= 'idUnk0' )

    topIInavform0.element('input[name=f0]')['_placeholder']='f0 Search'
    topIInavform0.element('input[name=f0]')['_id']='navbar-search-input'
    topIInavform0.element('input[name=f0]')['_class']='form-control'

    topIInavform0.custom.submit['_type'] = 'submit'
    topIInavform0.custom.submit['_id'] = 'unk-id'
    topIInavform0.custom.submit['_value'] = 'submit input'
    topIInavform0.custom.submit['_class'] = 'unk-class'
    topIInavform0.custom.submit['_title'] = 'submit topIInavform0'

    if topIInavform0.accepts(request,session): 
        response.flash0 = 'submitted topIInavform0' 
    elif topIInavform0.errors:
        response.flash0 = '!Errors! topIInavform0' 
    else: 
        response.flash0 = 'topIInavform0' 


    return dict( DICT= rows_dict, topIInavform0= topIInavform0, )

#@auth.requires_login()
def timeline():

    qu= db.dtimeline.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/timeline.html'


    timelineform0 = SQLFORM(db.dtimelineform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #timelineform0 = SQLFORM(db.dtimelineform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    timelineform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    timelineform0.element('input[name=f0]')['_id']='id_for711'
    timelineform0.element('input[name=f0]')['_class']='form-control'

    timelineform0.custom.submit['_type'] = 'submit'
    timelineform0.custom.submit['_id'] = 'search-btn'
    timelineform0.custom.submit['_value'] = 'unk_715'
    timelineform0.custom.submit['_class'] = 'btn btn-flat'
    timelineform0.custom.submit['_title'] = 'submit timelineform0'

    if timelineform0.accepts(request,session): 
        response.flash0 = 'submitted timelineform0' 
    elif timelineform0.errors:
        response.flash0 = '!Errors! timelineform0' 
    else: 
        response.flash0 = 'timelineform0' 



    timelineform1 = SQLFORM(db.dtimelineform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #timelineform1 = SQLFORM(db.dtimelineform1,  _class = 'classUnk1', _id= 'idUnk1' )

    timelineform1.element('input[name=f0]')['_placeholder']='f0 place_720'
    timelineform1.element('input[name=f0]')['_id']='id_for717'
    timelineform1.element('input[name=f0]')['_class']='pull-right'
    timelineform1.element('input[name=f1]')['_placeholder']='f1 place_724'
    timelineform1.element('input[name=f1]')['_id']='id_for721'
    timelineform1.element('input[name=f1]')['_class']='pull-right'
    timelineform1.element('input[name=f2]')['_placeholder']='f2 place_728'
    timelineform1.element('input[name=f2]')['_id']='id_for725'
    timelineform1.element('input[name=f2]')['_class']='pull-right'
    timelineform1.element('input[name=f3]')['_placeholder']='f3 place_732'
    timelineform1.element('input[name=f3]')['_id']='id_for729'
    timelineform1.element('input[name=f3]')['_class']='pull-right'
    timelineform1.element('input[name=f4]')['_placeholder']='f4 place_736'
    timelineform1.element('input[name=f4]')['_id']='id_for733'
    timelineform1.element('input[name=f4]')['_class']='pull-right'

    timelineform1.custom.submit['_id'] = 'id_for737'
    timelineform1.custom.submit['_class'] = 'text-red pull-right'
    timelineform1.custom.submit['_title'] = 'submit timelineform1'

    if timelineform1.accepts(request,session): 
        response.flash1 = 'submitted timelineform1' 
    elif timelineform1.errors:
        response.flash1 = '!Errors! timelineform1' 
    else: 
        response.flash1 = 'timelineform1' 


    return dict( DICT= rows_dict, timelineform0= timelineform0, timelineform1= timelineform1, )

#@auth.requires_login()
def mailbox():

    qu= db.dmailbox.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/mailbox.html'


    mailboxform0 = SQLFORM(db.dmailboxform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #mailboxform0 = SQLFORM(db.dmailboxform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    mailboxform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    mailboxform0.element('input[name=f0]')['_id']='id_for114'
    mailboxform0.element('input[name=f0]')['_class']='form-control'

    mailboxform0.custom.submit['_type'] = 'submit'
    mailboxform0.custom.submit['_id'] = 'search-btn'
    mailboxform0.custom.submit['_value'] = 'unk_118'
    mailboxform0.custom.submit['_class'] = 'btn btn-flat'
    mailboxform0.custom.submit['_title'] = 'submit mailboxform0'

    if mailboxform0.accepts(request,session): 
        response.flash0 = 'submitted mailboxform0' 
    elif mailboxform0.errors:
        response.flash0 = '!Errors! mailboxform0' 
    else: 
        response.flash0 = 'mailboxform0' 



    mailboxform1 = SQLFORM(db.dmailboxform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #mailboxform1 = SQLFORM(db.dmailboxform1,  _class = 'classUnk1', _id= 'idUnk1' )

    mailboxform1.element('input[name=f0]')['_placeholder']='f0 place_123'
    mailboxform1.element('input[name=f0]')['_id']='id_for120'
    mailboxform1.element('input[name=f0]')['_class']='pull-right'
    mailboxform1.element('input[name=f1]')['_placeholder']='f1 place_127'
    mailboxform1.element('input[name=f1]')['_id']='id_for124'
    mailboxform1.element('input[name=f1]')['_class']='pull-right'
    mailboxform1.element('input[name=f2]')['_placeholder']='f2 place_131'
    mailboxform1.element('input[name=f2]')['_id']='id_for128'
    mailboxform1.element('input[name=f2]')['_class']='pull-right'
    mailboxform1.element('input[name=f3]')['_placeholder']='f3 place_135'
    mailboxform1.element('input[name=f3]')['_id']='id_for132'
    mailboxform1.element('input[name=f3]')['_class']='pull-right'
    mailboxform1.element('input[name=f4]')['_placeholder']='f4 place_139'
    mailboxform1.element('input[name=f4]')['_id']='id_for136'
    mailboxform1.element('input[name=f4]')['_class']='pull-right'

    mailboxform1.custom.submit['_id'] = 'id_for140'
    mailboxform1.custom.submit['_class'] = 'text-red pull-right'
    mailboxform1.custom.submit['_title'] = 'submit mailboxform1'

    if mailboxform1.accepts(request,session): 
        response.flash1 = 'submitted mailboxform1' 
    elif mailboxform1.errors:
        response.flash1 = '!Errors! mailboxform1' 
    else: 
        response.flash1 = 'mailboxform1' 


    return dict( DICT= rows_dict, mailboxform0= mailboxform0, mailboxform1= mailboxform1, )

#@auth.requires_login()
def pace():

    qu= db.dpace.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/pace.html'


    paceform0 = SQLFORM(db.dpaceform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #paceform0 = SQLFORM(db.dpaceform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    paceform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    paceform0.element('input[name=f0]')['_id']='id_for586'
    paceform0.element('input[name=f0]')['_class']='form-control'

    paceform0.custom.submit['_type'] = 'submit'
    paceform0.custom.submit['_id'] = 'search-btn'
    paceform0.custom.submit['_value'] = 'unk_590'
    paceform0.custom.submit['_class'] = 'btn btn-flat'
    paceform0.custom.submit['_title'] = 'submit paceform0'

    if paceform0.accepts(request,session): 
        response.flash0 = 'submitted paceform0' 
    elif paceform0.errors:
        response.flash0 = '!Errors! paceform0' 
    else: 
        response.flash0 = 'paceform0' 



    paceform1 = SQLFORM(db.dpaceform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #paceform1 = SQLFORM(db.dpaceform1,  _class = 'classUnk1', _id= 'idUnk1' )

    paceform1.element('input[name=f0]')['_placeholder']='f0 place_595'
    paceform1.element('input[name=f0]')['_id']='id_for592'
    paceform1.element('input[name=f0]')['_class']='pull-right'
    paceform1.element('input[name=f1]')['_placeholder']='f1 place_599'
    paceform1.element('input[name=f1]')['_id']='id_for596'
    paceform1.element('input[name=f1]')['_class']='pull-right'
    paceform1.element('input[name=f2]')['_placeholder']='f2 place_603'
    paceform1.element('input[name=f2]')['_id']='id_for600'
    paceform1.element('input[name=f2]')['_class']='pull-right'
    paceform1.element('input[name=f3]')['_placeholder']='f3 place_607'
    paceform1.element('input[name=f3]')['_id']='id_for604'
    paceform1.element('input[name=f3]')['_class']='pull-right'
    paceform1.element('input[name=f4]')['_placeholder']='f4 place_611'
    paceform1.element('input[name=f4]')['_id']='id_for608'
    paceform1.element('input[name=f4]')['_class']='pull-right'

    paceform1.custom.submit['_id'] = 'id_for612'
    paceform1.custom.submit['_class'] = 'text-red pull-right'
    paceform1.custom.submit['_title'] = 'submit paceform1'

    if paceform1.accepts(request,session): 
        response.flash1 = 'submitted paceform1' 
    elif paceform1.errors:
        response.flash1 = '!Errors! paceform1' 
    else: 
        response.flash1 = 'paceform1' 


    return dict( DICT= rows_dict, paceform0= paceform0, paceform1= paceform1, )

#@auth.requires_login()
def flot():

    qu= db.dflot.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/flot.html'


    flotform0 = SQLFORM(db.dflotform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #flotform0 = SQLFORM(db.dflotform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    flotform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    flotform0.element('input[name=f0]')['_id']='id_for372'
    flotform0.element('input[name=f0]')['_class']='form-control'

    flotform0.custom.submit['_type'] = 'submit'
    flotform0.custom.submit['_id'] = 'search-btn'
    flotform0.custom.submit['_value'] = 'unk_376'
    flotform0.custom.submit['_class'] = 'btn btn-flat'
    flotform0.custom.submit['_title'] = 'submit flotform0'

    if flotform0.accepts(request,session): 
        response.flash0 = 'submitted flotform0' 
    elif flotform0.errors:
        response.flash0 = '!Errors! flotform0' 
    else: 
        response.flash0 = 'flotform0' 



    flotform1 = SQLFORM(db.dflotform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #flotform1 = SQLFORM(db.dflotform1,  _class = 'classUnk1', _id= 'idUnk1' )

    flotform1.element('input[name=f0]')['_placeholder']='f0 place_381'
    flotform1.element('input[name=f0]')['_id']='id_for378'
    flotform1.element('input[name=f0]')['_class']='pull-right'
    flotform1.element('input[name=f1]')['_placeholder']='f1 place_385'
    flotform1.element('input[name=f1]')['_id']='id_for382'
    flotform1.element('input[name=f1]')['_class']='pull-right'
    flotform1.element('input[name=f2]')['_placeholder']='f2 place_389'
    flotform1.element('input[name=f2]')['_id']='id_for386'
    flotform1.element('input[name=f2]')['_class']='pull-right'
    flotform1.element('input[name=f3]')['_placeholder']='f3 place_393'
    flotform1.element('input[name=f3]')['_id']='id_for390'
    flotform1.element('input[name=f3]')['_class']='pull-right'
    flotform1.element('input[name=f4]')['_placeholder']='f4 place_397'
    flotform1.element('input[name=f4]')['_id']='id_for394'
    flotform1.element('input[name=f4]')['_class']='pull-right'

    flotform1.custom.submit['_id'] = 'id_for398'
    flotform1.custom.submit['_class'] = 'text-red pull-right'
    flotform1.custom.submit['_title'] = 'submit flotform1'

    if flotform1.accepts(request,session): 
        response.flash1 = 'submitted flotform1' 
    elif flotform1.errors:
        response.flash1 = '!Errors! flotform1' 
    else: 
        response.flash1 = 'flotform1' 


    return dict( DICT= rows_dict, flotform0= flotform0, flotform1= flotform1, )

#@auth.requires_login()
def chartjs():

    qu= db.dchartjs.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/chartjs.html'


    chartjsform0 = SQLFORM(db.dchartjsform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #chartjsform0 = SQLFORM(db.dchartjsform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    chartjsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    chartjsform0.element('input[name=f0]')['_id']='id_for646'
    chartjsform0.element('input[name=f0]')['_class']='form-control'

    chartjsform0.custom.submit['_type'] = 'submit'
    chartjsform0.custom.submit['_id'] = 'search-btn'
    chartjsform0.custom.submit['_value'] = 'unk_650'
    chartjsform0.custom.submit['_class'] = 'btn btn-flat'
    chartjsform0.custom.submit['_title'] = 'submit chartjsform0'

    if chartjsform0.accepts(request,session): 
        response.flash0 = 'submitted chartjsform0' 
    elif chartjsform0.errors:
        response.flash0 = '!Errors! chartjsform0' 
    else: 
        response.flash0 = 'chartjsform0' 



    chartjsform1 = SQLFORM(db.dchartjsform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #chartjsform1 = SQLFORM(db.dchartjsform1,  _class = 'classUnk1', _id= 'idUnk1' )

    chartjsform1.element('input[name=f0]')['_placeholder']='f0 place_655'
    chartjsform1.element('input[name=f0]')['_id']='id_for652'
    chartjsform1.element('input[name=f0]')['_class']='pull-right'
    chartjsform1.element('input[name=f1]')['_placeholder']='f1 place_659'
    chartjsform1.element('input[name=f1]')['_id']='id_for656'
    chartjsform1.element('input[name=f1]')['_class']='pull-right'
    chartjsform1.element('input[name=f2]')['_placeholder']='f2 place_663'
    chartjsform1.element('input[name=f2]')['_id']='id_for660'
    chartjsform1.element('input[name=f2]')['_class']='pull-right'
    chartjsform1.element('input[name=f3]')['_placeholder']='f3 place_667'
    chartjsform1.element('input[name=f3]')['_id']='id_for664'
    chartjsform1.element('input[name=f3]')['_class']='pull-right'
    chartjsform1.element('input[name=f4]')['_placeholder']='f4 place_671'
    chartjsform1.element('input[name=f4]')['_id']='id_for668'
    chartjsform1.element('input[name=f4]')['_class']='pull-right'

    chartjsform1.custom.submit['_id'] = 'id_for672'
    chartjsform1.custom.submit['_class'] = 'text-red pull-right'
    chartjsform1.custom.submit['_title'] = 'submit chartjsform1'

    if chartjsform1.accepts(request,session): 
        response.flash1 = 'submitted chartjsform1' 
    elif chartjsform1.errors:
        response.flash1 = '!Errors! chartjsform1' 
    else: 
        response.flash1 = 'chartjsform1' 


    return dict( DICT= rows_dict, chartjsform0= chartjsform0, chartjsform1= chartjsform1, )

#@auth.requires_login()
def widgets():

    qu= db.dwidgets.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/widgets.html'


    widgetsform0 = SQLFORM(db.dwidgetsform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #widgetsform0 = SQLFORM(db.dwidgetsform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    widgetsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    widgetsform0.element('input[name=f0]')['_id']='id_for30'
    widgetsform0.element('input[name=f0]')['_class']='form-control'

    widgetsform0.custom.submit['_type'] = 'submit'
    widgetsform0.custom.submit['_id'] = 'search-btn'
    widgetsform0.custom.submit['_value'] = 'unk_34'
    widgetsform0.custom.submit['_class'] = 'btn btn-flat'
    widgetsform0.custom.submit['_title'] = 'submit widgetsform0'

    if widgetsform0.accepts(request,session): 
        response.flash0 = 'submitted widgetsform0' 
    elif widgetsform0.errors:
        response.flash0 = '!Errors! widgetsform0' 
    else: 
        response.flash0 = 'widgetsform0' 



    widgetsform1 = SQLFORM(db.dwidgetsform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #widgetsform1 = SQLFORM(db.dwidgetsform1,  _class = 'classUnk1', _id= 'idUnk1' )

    widgetsform1.element('input[name=f0]')['_placeholder']='f0 Type Message ...'
    widgetsform1.element('input[name=f0]')['_id']='id_for36'
    widgetsform1.element('input[name=f0]')['_class']='form-control'

    widgetsform1.custom.submit['_type'] = 'submit'
    widgetsform1.custom.submit['_id'] = 'id_for38'
    widgetsform1.custom.submit['_value'] = 'Send'
    widgetsform1.custom.submit['_class'] = 'btn btn-primary btn-flat'
    widgetsform1.custom.submit['_title'] = 'submit widgetsform1'

    if widgetsform1.accepts(request,session): 
        response.flash1 = 'submitted widgetsform1' 
    elif widgetsform1.errors:
        response.flash1 = '!Errors! widgetsform1' 
    else: 
        response.flash1 = 'widgetsform1' 



    widgetsform2 = SQLFORM(db.dwidgetsform2, formstyle= 'divs', _class = 'classUnk2', _id= 'idUnk2' )
    #widgetsform2 = SQLFORM(db.dwidgetsform2,  _class = 'classUnk2', _id= 'idUnk2' )

    widgetsform2.element('input[name=f0]')['_placeholder']='f0 Type Message ...'
    widgetsform2.element('input[name=f0]')['_id']='id_for41'
    widgetsform2.element('input[name=f0]')['_class']='form-control'

    widgetsform2.custom.submit['_type'] = 'submit'
    widgetsform2.custom.submit['_id'] = 'id_for43'
    widgetsform2.custom.submit['_value'] = 'Send'
    widgetsform2.custom.submit['_class'] = 'btn btn-success btn-flat'
    widgetsform2.custom.submit['_title'] = 'submit widgetsform2'

    if widgetsform2.accepts(request,session): 
        response.flash2 = 'submitted widgetsform2' 
    elif widgetsform2.errors:
        response.flash2 = '!Errors! widgetsform2' 
    else: 
        response.flash2 = 'widgetsform2' 



    widgetsform3 = SQLFORM(db.dwidgetsform3, formstyle= 'divs', _class = 'classUnk3', _id= 'idUnk3' )
    #widgetsform3 = SQLFORM(db.dwidgetsform3,  _class = 'classUnk3', _id= 'idUnk3' )

    widgetsform3.element('input[name=f0]')['_placeholder']='f0 Type Message ...'
    widgetsform3.element('input[name=f0]')['_id']='id_for46'
    widgetsform3.element('input[name=f0]')['_class']='form-control'

    widgetsform3.custom.submit['_type'] = 'submit'
    widgetsform3.custom.submit['_id'] = 'id_for48'
    widgetsform3.custom.submit['_value'] = 'Send'
    widgetsform3.custom.submit['_class'] = 'btn btn-warning btn-flat'
    widgetsform3.custom.submit['_title'] = 'submit widgetsform3'

    if widgetsform3.accepts(request,session): 
        response.flash3 = 'submitted widgetsform3' 
    elif widgetsform3.errors:
        response.flash3 = '!Errors! widgetsform3' 
    else: 
        response.flash3 = 'widgetsform3' 



    widgetsform4 = SQLFORM(db.dwidgetsform4, formstyle= 'divs', _class = 'classUnk4', _id= 'idUnk4' )
    #widgetsform4 = SQLFORM(db.dwidgetsform4,  _class = 'classUnk4', _id= 'idUnk4' )

    widgetsform4.element('input[name=f0]')['_placeholder']='f0 Type Message ...'
    widgetsform4.element('input[name=f0]')['_id']='id_for51'
    widgetsform4.element('input[name=f0]')['_class']='form-control'

    widgetsform4.custom.submit['_type'] = 'submit'
    widgetsform4.custom.submit['_id'] = 'id_for53'
    widgetsform4.custom.submit['_value'] = 'Send'
    widgetsform4.custom.submit['_class'] = 'btn btn-danger btn-flat'
    widgetsform4.custom.submit['_title'] = 'submit widgetsform4'

    if widgetsform4.accepts(request,session): 
        response.flash4 = 'submitted widgetsform4' 
    elif widgetsform4.errors:
        response.flash4 = '!Errors! widgetsform4' 
    else: 
        response.flash4 = 'widgetsform4' 



    widgetsform5 = SQLFORM(db.dwidgetsform5, formstyle= 'divs', _class = 'classUnk5', _id= 'idUnk5' )
    #widgetsform5 = SQLFORM(db.dwidgetsform5,  _class = 'classUnk5', _id= 'idUnk5' )

    widgetsform5.element('input[name=f0]')['_placeholder']='f0 Press enter to post comment'
    widgetsform5.element('input[name=f0]')['_id']='id_for56'
    widgetsform5.element('input[name=f0]')['_class']='form-control input-sm'

    widgetsform5.custom.submit['_type'] = 'submit'
    widgetsform5.custom.submit['_id'] = 'unk-id'
    widgetsform5.custom.submit['_value'] = 'submit input'
    widgetsform5.custom.submit['_class'] = 'unk-class'
    widgetsform5.custom.submit['_title'] = 'submit widgetsform5'

    if widgetsform5.accepts(request,session): 
        response.flash5 = 'submitted widgetsform5' 
    elif widgetsform5.errors:
        response.flash5 = '!Errors! widgetsform5' 
    else: 
        response.flash5 = 'widgetsform5' 



    widgetsform6 = SQLFORM(db.dwidgetsform6, formstyle= 'divs', _class = 'classUnk6', _id= 'idUnk6' )
    #widgetsform6 = SQLFORM(db.dwidgetsform6,  _class = 'classUnk6', _id= 'idUnk6' )

    widgetsform6.element('input[name=f0]')['_placeholder']='f0 Press enter to post comment'
    widgetsform6.element('input[name=f0]')['_id']='id_for58'
    widgetsform6.element('input[name=f0]')['_class']='form-control input-sm'

    widgetsform6.custom.submit['_type'] = 'submit'
    widgetsform6.custom.submit['_id'] = 'unk-id'
    widgetsform6.custom.submit['_value'] = 'submit input'
    widgetsform6.custom.submit['_class'] = 'unk-class'
    widgetsform6.custom.submit['_title'] = 'submit widgetsform6'

    if widgetsform6.accepts(request,session): 
        response.flash6 = 'submitted widgetsform6' 
    elif widgetsform6.errors:
        response.flash6 = '!Errors! widgetsform6' 
    else: 
        response.flash6 = 'widgetsform6' 



    widgetsform7 = SQLFORM(db.dwidgetsform7, formstyle= 'divs', _class = 'classUnk7', _id= 'idUnk7' )
    #widgetsform7 = SQLFORM(db.dwidgetsform7,  _class = 'classUnk7', _id= 'idUnk7' )

    widgetsform7.element('input[name=f0]')['_placeholder']='f0 place_63'
    widgetsform7.element('input[name=f0]')['_id']='id_for60'
    widgetsform7.element('input[name=f0]')['_class']='pull-right'
    widgetsform7.element('input[name=f1]')['_placeholder']='f1 place_67'
    widgetsform7.element('input[name=f1]')['_id']='id_for64'
    widgetsform7.element('input[name=f1]')['_class']='pull-right'
    widgetsform7.element('input[name=f2]')['_placeholder']='f2 place_71'
    widgetsform7.element('input[name=f2]')['_id']='id_for68'
    widgetsform7.element('input[name=f2]')['_class']='pull-right'
    widgetsform7.element('input[name=f3]')['_placeholder']='f3 place_75'
    widgetsform7.element('input[name=f3]')['_id']='id_for72'
    widgetsform7.element('input[name=f3]')['_class']='pull-right'
    widgetsform7.element('input[name=f4]')['_placeholder']='f4 place_79'
    widgetsform7.element('input[name=f4]')['_id']='id_for76'
    widgetsform7.element('input[name=f4]')['_class']='pull-right'

    widgetsform7.custom.submit['_id'] = 'id_for80'
    widgetsform7.custom.submit['_class'] = 'text-red pull-right'
    widgetsform7.custom.submit['_title'] = 'submit widgetsform7'

    if widgetsform7.accepts(request,session): 
        response.flash7 = 'submitted widgetsform7' 
    elif widgetsform7.errors:
        response.flash7 = '!Errors! widgetsform7' 
    else: 
        response.flash7 = 'widgetsform7' 


    return dict( DICT= rows_dict, widgetsform0= widgetsform0, widgetsform1= widgetsform1, widgetsform2= widgetsform2, widgetsform3= widgetsform3, widgetsform4= widgetsform4, widgetsform5= widgetsform5, widgetsform6= widgetsform6, widgetsform7= widgetsform7, )

#@auth.requires_login()
def sliders():

    qu= db.dsliders.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/sliders.html'


    slidersform0 = SQLFORM(db.dslidersform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #slidersform0 = SQLFORM(db.dslidersform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    slidersform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    slidersform0.element('input[name=f0]')['_id']='id_for616'
    slidersform0.element('input[name=f0]')['_class']='form-control'

    slidersform0.custom.submit['_type'] = 'submit'
    slidersform0.custom.submit['_id'] = 'search-btn'
    slidersform0.custom.submit['_value'] = 'unk_620'
    slidersform0.custom.submit['_class'] = 'btn btn-flat'
    slidersform0.custom.submit['_title'] = 'submit slidersform0'

    if slidersform0.accepts(request,session): 
        response.flash0 = 'submitted slidersform0' 
    elif slidersform0.errors:
        response.flash0 = '!Errors! slidersform0' 
    else: 
        response.flash0 = 'slidersform0' 



    slidersform1 = SQLFORM(db.dslidersform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #slidersform1 = SQLFORM(db.dslidersform1,  _class = 'classUnk1', _id= 'idUnk1' )

    slidersform1.element('input[name=f0]')['_placeholder']='f0 place_625'
    slidersform1.element('input[name=f0]')['_id']='id_for622'
    slidersform1.element('input[name=f0]')['_class']='pull-right'
    slidersform1.element('input[name=f1]')['_placeholder']='f1 place_629'
    slidersform1.element('input[name=f1]')['_id']='id_for626'
    slidersform1.element('input[name=f1]')['_class']='pull-right'
    slidersform1.element('input[name=f2]')['_placeholder']='f2 place_633'
    slidersform1.element('input[name=f2]')['_id']='id_for630'
    slidersform1.element('input[name=f2]')['_class']='pull-right'
    slidersform1.element('input[name=f3]')['_placeholder']='f3 place_637'
    slidersform1.element('input[name=f3]')['_id']='id_for634'
    slidersform1.element('input[name=f3]')['_class']='pull-right'
    slidersform1.element('input[name=f4]')['_placeholder']='f4 place_641'
    slidersform1.element('input[name=f4]')['_id']='id_for638'
    slidersform1.element('input[name=f4]')['_class']='pull-right'

    slidersform1.custom.submit['_id'] = 'id_for642'
    slidersform1.custom.submit['_class'] = 'text-red pull-right'
    slidersform1.custom.submit['_title'] = 'submit slidersform1'

    if slidersform1.accepts(request,session): 
        response.flash1 = 'submitted slidersform1' 
    elif slidersform1.errors:
        response.flash1 = '!Errors! slidersform1' 
    else: 
        response.flash1 = 'slidersform1' 


    return dict( DICT= rows_dict, slidersform0= slidersform0, slidersform1= slidersform1, )

#@auth.requires_login()
def register():

    qu= db.dregister.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/register.html'


    registerform0 = SQLFORM(db.dregisterform0, formstyle= 'divs', _class = 'classUnk0', _id= 'idUnk0' )
    #registerform0 = SQLFORM(db.dregisterform0,  _class = 'classUnk0', _id= 'idUnk0' )

    registerform0.element('input[name=f0]')['_placeholder']='f0 Full name'
    registerform0.element('input[name=f0]')['_id']='id_for144'
    registerform0.element('input[name=f0]')['_class']='form-control'
    registerform0.element('input[name=f1]')['_placeholder']='f1 Email'
    registerform0.element('input[name=f1]')['_id']='id_for147'
    registerform0.element('input[name=f1]')['_class']='form-control'
    registerform0.element('input[name=f2]')['_placeholder']='f2 Password'
    registerform0.element('input[name=f2]')['_id']='id_for150'
    registerform0.element('input[name=f2]')['_class']='form-control'
    registerform0.element('input[name=f3]')['_placeholder']='f3 Retype password'
    registerform0.element('input[name=f3]')['_id']='id_for153'
    registerform0.element('input[name=f3]')['_class']='form-control'
    registerform0.element('input[name=f4]')['_placeholder']='f4 place_159'
    registerform0.element('input[name=f4]')['_id']='id_for156'

    registerform0.custom.submit['_type'] = 'submit'
    registerform0.custom.submit['_id'] = 'id_for160'
    registerform0.custom.submit['_value'] = 'Register'
    registerform0.custom.submit['_class'] = 'btn btn-primary btn-block btn-flat'
    registerform0.custom.submit['_title'] = 'submit registerform0'

    registerform0.custom.submit['_id'] = 'id_for164'
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


    modalsform0 = SQLFORM(db.dmodalsform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #modalsform0 = SQLFORM(db.dmodalsform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    modalsform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    modalsform0.element('input[name=f0]')['_id']='id_for222'
    modalsform0.element('input[name=f0]')['_class']='form-control'

    modalsform0.custom.submit['_type'] = 'submit'
    modalsform0.custom.submit['_id'] = 'search-btn'
    modalsform0.custom.submit['_value'] = 'unk_226'
    modalsform0.custom.submit['_class'] = 'btn btn-flat'
    modalsform0.custom.submit['_title'] = 'submit modalsform0'

    if modalsform0.accepts(request,session): 
        response.flash0 = 'submitted modalsform0' 
    elif modalsform0.errors:
        response.flash0 = '!Errors! modalsform0' 
    else: 
        response.flash0 = 'modalsform0' 



    modalsform1 = SQLFORM(db.dmodalsform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #modalsform1 = SQLFORM(db.dmodalsform1,  _class = 'classUnk1', _id= 'idUnk1' )

    modalsform1.element('input[name=f0]')['_placeholder']='f0 place_231'
    modalsform1.element('input[name=f0]')['_id']='id_for228'
    modalsform1.element('input[name=f0]')['_class']='pull-right'
    modalsform1.element('input[name=f1]')['_placeholder']='f1 place_235'
    modalsform1.element('input[name=f1]')['_id']='id_for232'
    modalsform1.element('input[name=f1]')['_class']='pull-right'
    modalsform1.element('input[name=f2]')['_placeholder']='f2 place_239'
    modalsform1.element('input[name=f2]')['_id']='id_for236'
    modalsform1.element('input[name=f2]')['_class']='pull-right'
    modalsform1.element('input[name=f3]')['_placeholder']='f3 place_243'
    modalsform1.element('input[name=f3]')['_id']='id_for240'
    modalsform1.element('input[name=f3]')['_class']='pull-right'
    modalsform1.element('input[name=f4]')['_placeholder']='f4 place_247'
    modalsform1.element('input[name=f4]')['_id']='id_for244'
    modalsform1.element('input[name=f4]')['_class']='pull-right'

    modalsform1.custom.submit['_id'] = 'id_for248'
    modalsform1.custom.submit['_class'] = 'text-red pull-right'
    modalsform1.custom.submit['_title'] = 'submit modalsform1'

    if modalsform1.accepts(request,session): 
        response.flash1 = 'submitted modalsform1' 
    elif modalsform1.errors:
        response.flash1 = '!Errors! modalsform1' 
    else: 
        response.flash1 = 'modalsform1' 


    return dict( DICT= rows_dict, modalsform0= modalsform0, modalsform1= modalsform1, )

#@auth.requires_login()
def calendar():

    qu= db.dcalendar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/calendar.html'


    calendarform0 = SQLFORM(db.dcalendarform0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #calendarform0 = SQLFORM(db.dcalendarform0,  _class = 'sidebar-form', _id= 'idUnk0' )

    calendarform0.element('input[name=f0]')['_placeholder']='f0 Search...'
    calendarform0.element('input[name=f0]')['_id']='id_for974'
    calendarform0.element('input[name=f0]')['_class']='form-control'

    calendarform0.custom.submit['_type'] = 'submit'
    calendarform0.custom.submit['_id'] = 'search-btn'
    calendarform0.custom.submit['_value'] = 'unk_978'
    calendarform0.custom.submit['_class'] = 'btn btn-flat'
    calendarform0.custom.submit['_title'] = 'submit calendarform0'

    if calendarform0.accepts(request,session): 
        response.flash0 = 'submitted calendarform0' 
    elif calendarform0.errors:
        response.flash0 = '!Errors! calendarform0' 
    else: 
        response.flash0 = 'calendarform0' 



    calendarform1 = SQLFORM(db.dcalendarform1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #calendarform1 = SQLFORM(db.dcalendarform1,  _class = 'classUnk1', _id= 'idUnk1' )

    calendarform1.element('input[name=f0]')['_placeholder']='f0 place_983'
    calendarform1.element('input[name=f0]')['_id']='id_for980'
    calendarform1.element('input[name=f0]')['_class']='pull-right'
    calendarform1.element('input[name=f1]')['_placeholder']='f1 place_987'
    calendarform1.element('input[name=f1]')['_id']='id_for984'
    calendarform1.element('input[name=f1]')['_class']='pull-right'
    calendarform1.element('input[name=f2]')['_placeholder']='f2 place_991'
    calendarform1.element('input[name=f2]')['_id']='id_for988'
    calendarform1.element('input[name=f2]')['_class']='pull-right'
    calendarform1.element('input[name=f3]')['_placeholder']='f3 place_995'
    calendarform1.element('input[name=f3]')['_id']='id_for992'
    calendarform1.element('input[name=f3]')['_class']='pull-right'
    calendarform1.element('input[name=f4]')['_placeholder']='f4 place_999'
    calendarform1.element('input[name=f4]')['_id']='id_for996'
    calendarform1.element('input[name=f4]')['_class']='pull-right'

    calendarform1.custom.submit['_id'] = 'id_for1000'
    calendarform1.custom.submit['_class'] = 'text-red pull-right'
    calendarform1.custom.submit['_title'] = 'submit calendarform1'

    if calendarform1.accepts(request,session): 
        response.flash1 = 'submitted calendarform1' 
    elif calendarform1.errors:
        response.flash1 = '!Errors! calendarform1' 
    else: 
        response.flash1 = 'calendarform1' 


    return dict( DICT= rows_dict, calendarform0= calendarform0, calendarform1= calendarform1, )

#@auth.requires_login()
def index2():

    qu= db.dindex2.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index2.html'


    index2form0 = SQLFORM(db.dindex2form0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #index2form0 = SQLFORM(db.dindex2form0,  _class = 'sidebar-form', _id= 'idUnk0' )

    index2form0.element('input[name=f0]')['_placeholder']='f0 Search...'
    index2form0.element('input[name=f0]')['_id']='id_for843'
    index2form0.element('input[name=f0]')['_class']='form-control'

    index2form0.custom.submit['_type'] = 'submit'
    index2form0.custom.submit['_id'] = 'search-btn'
    index2form0.custom.submit['_value'] = 'unk_847'
    index2form0.custom.submit['_class'] = 'btn btn-flat'
    index2form0.custom.submit['_title'] = 'submit index2form0'

    if index2form0.accepts(request,session): 
        response.flash0 = 'submitted index2form0' 
    elif index2form0.errors:
        response.flash0 = '!Errors! index2form0' 
    else: 
        response.flash0 = 'index2form0' 



    index2form1 = SQLFORM(db.dindex2form1, formstyle= 'divs', _class = 'classUnk1', _id= 'idUnk1' )
    #index2form1 = SQLFORM(db.dindex2form1,  _class = 'classUnk1', _id= 'idUnk1' )

    index2form1.element('input[name=f0]')['_placeholder']='f0 Type Message ...'
    index2form1.element('input[name=f0]')['_id']='id_for849'
    index2form1.element('input[name=f0]')['_class']='form-control'

    index2form1.custom.submit['_type'] = 'submit'
    index2form1.custom.submit['_id'] = 'id_for851'
    index2form1.custom.submit['_value'] = 'Send'
    index2form1.custom.submit['_class'] = 'btn btn-warning btn-flat'
    index2form1.custom.submit['_title'] = 'submit index2form1'

    if index2form1.accepts(request,session): 
        response.flash1 = 'submitted index2form1' 
    elif index2form1.errors:
        response.flash1 = '!Errors! index2form1' 
    else: 
        response.flash1 = 'index2form1' 



    index2form2 = SQLFORM(db.dindex2form2, formstyle= 'divs', _class = 'classUnk2', _id= 'idUnk2' )
    #index2form2 = SQLFORM(db.dindex2form2,  _class = 'classUnk2', _id= 'idUnk2' )

    index2form2.element('input[name=f0]')['_placeholder']='f0 place_857'
    index2form2.element('input[name=f0]')['_id']='id_for854'
    index2form2.element('input[name=f0]')['_class']='pull-right'
    index2form2.element('input[name=f1]')['_placeholder']='f1 place_861'
    index2form2.element('input[name=f1]')['_id']='id_for858'
    index2form2.element('input[name=f1]')['_class']='pull-right'
    index2form2.element('input[name=f2]')['_placeholder']='f2 place_865'
    index2form2.element('input[name=f2]')['_id']='id_for862'
    index2form2.element('input[name=f2]')['_class']='pull-right'
    index2form2.element('input[name=f3]')['_placeholder']='f3 place_869'
    index2form2.element('input[name=f3]')['_id']='id_for866'
    index2form2.element('input[name=f3]')['_class']='pull-right'
    index2form2.element('input[name=f4]')['_placeholder']='f4 place_873'
    index2form2.element('input[name=f4]')['_id']='id_for870'
    index2form2.element('input[name=f4]')['_class']='pull-right'

    index2form2.custom.submit['_id'] = 'id_for874'
    index2form2.custom.submit['_class'] = 'text-red pull-right'
    index2form2.custom.submit['_title'] = 'submit index2form2'

    if index2form2.accepts(request,session): 
        response.flash2 = 'submitted index2form2' 
    elif index2form2.errors:
        response.flash2 = '!Errors! index2form2' 
    else: 
        response.flash2 = 'index2form2' 


    return dict( DICT= rows_dict, index2form0= index2form0, index2form1= index2form1, index2form2= index2form2, )

#@auth.requires_login()
def X500():

    qu= db.d500.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/500.html'


    X500form0 = SQLFORM(db.dX500form0, formstyle= 'divs', _class = 'sidebar-form', _id= 'idUnk0' )
    #X500form0 = SQLFORM(db.dX500form0,  _class = 'sidebar-form', _id= 'idUnk0' )

    X500form0.element('input[name=f0]')['_placeholder']='f0 Search...'
    X500form0.element('input[name=f0]')['_id']='id_for938'
    X500form0.element('input[name=f0]')['_class']='form-control'

    X500form0.custom.submit['_type'] = 'submit'
    X500form0.custom.submit['_id'] = 'search-btn'
    X500form0.custom.submit['_value'] = 'unk_942'
    X500form0.custom.submit['_class'] = 'btn btn-flat'
    X500form0.custom.submit['_title'] = 'submit X500form0'

    if X500form0.accepts(request,session): 
        response.flash0 = 'submitted X500form0' 
    elif X500form0.errors:
        response.flash0 = '!Errors! X500form0' 
    else: 
        response.flash0 = 'X500form0' 



    X500form1 = SQLFORM(db.dX500form1, formstyle= 'divs', _class = 'search-form', _id= 'idUnk1' )
    #X500form1 = SQLFORM(db.dX500form1,  _class = 'search-form', _id= 'idUnk1' )

    X500form1.element('input[name=f0]')['_placeholder']='f0 Search'
    X500form1.element('input[name=f0]')['_id']='id_for944'
    X500form1.element('input[name=f0]')['_class']='form-control'

    X500form1.custom.submit['_type'] = 'submit'
    X500form1.custom.submit['_id'] = 'id_for946'
    X500form1.custom.submit['_value'] = 'unk_948'
    X500form1.custom.submit['_class'] = 'btn btn-danger btn-flat'
    X500form1.custom.submit['_title'] = 'submit X500form1'

    if X500form1.accepts(request,session): 
        response.flash1 = 'submitted X500form1' 
    elif X500form1.errors:
        response.flash1 = '!Errors! X500form1' 
    else: 
        response.flash1 = 'X500form1' 



    X500form2 = SQLFORM(db.dX500form2, formstyle= 'divs', _class = 'classUnk2', _id= 'idUnk2' )
    #X500form2 = SQLFORM(db.dX500form2,  _class = 'classUnk2', _id= 'idUnk2' )

    X500form2.element('input[name=f0]')['_placeholder']='f0 place_953'
    X500form2.element('input[name=f0]')['_id']='id_for950'
    X500form2.element('input[name=f0]')['_class']='pull-right'
    X500form2.element('input[name=f1]')['_placeholder']='f1 place_957'
    X500form2.element('input[name=f1]')['_id']='id_for954'
    X500form2.element('input[name=f1]')['_class']='pull-right'
    X500form2.element('input[name=f2]')['_placeholder']='f2 place_961'
    X500form2.element('input[name=f2]')['_id']='id_for958'
    X500form2.element('input[name=f2]')['_class']='pull-right'
    X500form2.element('input[name=f3]')['_placeholder']='f3 place_965'
    X500form2.element('input[name=f3]')['_id']='id_for962'
    X500form2.element('input[name=f3]')['_class']='pull-right'
    X500form2.element('input[name=f4]')['_placeholder']='f4 place_969'
    X500form2.element('input[name=f4]')['_id']='id_for966'
    X500form2.element('input[name=f4]')['_class']='pull-right'

    X500form2.custom.submit['_id'] = 'id_for970'
    X500form2.custom.submit['_class'] = 'text-red pull-right'
    X500form2.custom.submit['_title'] = 'submit X500form2'

    if X500form2.accepts(request,session): 
        response.flash2 = 'submitted X500form2' 
    elif X500form2.errors:
        response.flash2 = '!Errors! X500form2' 
    else: 
        response.flash2 = 'X500form2' 


    return dict( DICT= rows_dict, X500form0= X500form0, X500form1= X500form1, X500form2= X500form2, )