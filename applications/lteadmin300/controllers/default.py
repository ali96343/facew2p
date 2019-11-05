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


    boxedform0 = SQLFORM(db.dboxedform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    boxedform0.element('input[name=f0]')['_placeholder']='f0 Search'
    boxedform0.element('input[name=f0]')['_id']='id_for425'
    boxedform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    boxedform0.custom.submit['_type'] = 'submit'
    boxedform0.custom.submit['_id'] = 'id_for427'
    boxedform0.custom.submit['_value'] = 'unk_429'
    boxedform0.custom.submit['_class'] = 'btn btn-navbar'
    boxedform0.custom.submit['_title'] = 'submit boxedform0'

    if boxedform0.accepts(request,session): 
        response.flash0 = 'submitted boxedform0' 
    elif boxedform0.errors:
        response.flash0 = '!Errors! boxedform0' 
    else: 
        response.flash0 = 'boxedform0' 


    return dict( DICT= rows_dict, boxedform0= boxedform0, )

#@auth.requires_login()
def projectIIedit():

    qu= db.dproject0edit.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/project_edit.html'


    projectIIeditform0 = SQLFORM(db.dprojectIIeditform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    projectIIeditform0.element('input[name=f0]')['_placeholder']='f0 Search'
    projectIIeditform0.element('input[name=f0]')['_id']='id_for149'
    projectIIeditform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    projectIIeditform0.custom.submit['_type'] = 'submit'
    projectIIeditform0.custom.submit['_id'] = 'id_for151'
    projectIIeditform0.custom.submit['_value'] = 'unk_153'
    projectIIeditform0.custom.submit['_class'] = 'btn btn-navbar'
    projectIIeditform0.custom.submit['_title'] = 'submit projectIIeditform0'

    if projectIIeditform0.accepts(request,session): 
        response.flash0 = 'submitted projectIIeditform0' 
    elif projectIIeditform0.errors:
        response.flash0 = '!Errors! projectIIeditform0' 
    else: 
        response.flash0 = 'projectIIeditform0' 


    return dict( DICT= rows_dict, projectIIeditform0= projectIIeditform0, )

#@auth.requires_login()
def ribbons():

    qu= db.dribbons.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/ribbons.html'


    ribbonsform0 = SQLFORM(db.dribbonsform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    ribbonsform0.element('input[name=f0]')['_placeholder']='f0 Search'
    ribbonsform0.element('input[name=f0]')['_id']='id_for296'
    ribbonsform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    ribbonsform0.custom.submit['_type'] = 'submit'
    ribbonsform0.custom.submit['_id'] = 'id_for298'
    ribbonsform0.custom.submit['_value'] = 'unk_300'
    ribbonsform0.custom.submit['_class'] = 'btn btn-navbar'
    ribbonsform0.custom.submit['_title'] = 'submit ribbonsform0'

    if ribbonsform0.accepts(request,session): 
        response.flash0 = 'submitted ribbonsform0' 
    elif ribbonsform0.errors:
        response.flash0 = '!Errors! ribbonsform0' 
    else: 
        response.flash0 = 'ribbonsform0' 


    return dict( DICT= rows_dict, ribbonsform0= ribbonsform0, )

#@auth.requires_login()
def gallery():

    qu= db.dgallery.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/gallery.html'


    galleryform0 = SQLFORM(db.dgalleryform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    galleryform0.element('input[name=f0]')['_placeholder']='f0 Search'
    galleryform0.element('input[name=f0]')['_id']='id_for272'
    galleryform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    galleryform0.custom.submit['_type'] = 'submit'
    galleryform0.custom.submit['_id'] = 'id_for274'
    galleryform0.custom.submit['_value'] = 'unk_276'
    galleryform0.custom.submit['_class'] = 'btn btn-navbar'
    galleryform0.custom.submit['_title'] = 'submit galleryform0'

    if galleryform0.accepts(request,session): 
        response.flash0 = 'submitted galleryform0' 
    elif galleryform0.errors:
        response.flash0 = '!Errors! galleryform0' 
    else: 
        response.flash0 = 'galleryform0' 


    return dict( DICT= rows_dict, galleryform0= galleryform0, )

#@auth.requires_login()
def index3():

    qu= db.dindex3.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index3.html'


    index3form0 = SQLFORM(db.dindex3form0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    index3form0.element('input[name=f0]')['_placeholder']='f0 Search'
    index3form0.element('input[name=f0]')['_id']='id_for455'
    index3form0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    index3form0.custom.submit['_type'] = 'submit'
    index3form0.custom.submit['_id'] = 'id_for457'
    index3form0.custom.submit['_value'] = 'unk_459'
    index3form0.custom.submit['_class'] = 'btn btn-navbar'
    index3form0.custom.submit['_title'] = 'submit index3form0'

    if index3form0.accepts(request,session): 
        response.flash0 = 'submitted index3form0' 
    elif index3form0.errors:
        response.flash0 = '!Errors! index3form0' 
    else: 
        response.flash0 = 'index3form0' 


    return dict( DICT= rows_dict, index3form0= index3form0, )

#@auth.requires_login()
def inline():

    qu= db.dinline.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/inline.html'


    inlineform0 = SQLFORM(db.dinlineform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    inlineform0.element('input[name=f0]')['_placeholder']='f0 Search'
    inlineform0.element('input[name=f0]')['_id']='id_for371'
    inlineform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    inlineform0.custom.submit['_type'] = 'submit'
    inlineform0.custom.submit['_id'] = 'id_for373'
    inlineform0.custom.submit['_value'] = 'unk_375'
    inlineform0.custom.submit['_class'] = 'btn btn-navbar'
    inlineform0.custom.submit['_title'] = 'submit inlineform0'

    if inlineform0.accepts(request,session): 
        response.flash0 = 'submitted inlineform0' 
    elif inlineform0.errors:
        response.flash0 = '!Errors! inlineform0' 
    else: 
        response.flash0 = 'inlineform0' 


    return dict( DICT= rows_dict, inlineform0= inlineform0, )

#@auth.requires_login()
def advanced():

    qu= db.dadvanced.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/advanced.html'


    advancedform0 = SQLFORM(db.dadvancedform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    advancedform0.element('input[name=f0]')['_placeholder']='f0 Search'
    advancedform0.element('input[name=f0]')['_id']='id_for167'
    advancedform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    advancedform0.custom.submit['_type'] = 'submit'
    advancedform0.custom.submit['_id'] = 'id_for169'
    advancedform0.custom.submit['_value'] = 'unk_171'
    advancedform0.custom.submit['_class'] = 'btn btn-navbar'
    advancedform0.custom.submit['_title'] = 'submit advancedform0'

    if advancedform0.accepts(request,session): 
        response.flash0 = 'submitted advancedform0' 
    elif advancedform0.errors:
        response.flash0 = '!Errors! advancedform0' 
    else: 
        response.flash0 = 'advancedform0' 


    return dict( DICT= rows_dict, advancedform0= advancedform0, )

#@auth.requires_login()
def fixedIIsidebar():

    qu= db.dfixed0sidebar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/fixed-sidebar.html'


    fixedIIsidebarform0 = SQLFORM(db.dfixedIIsidebarform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    fixedIIsidebarform0.element('input[name=f0]')['_placeholder']='f0 Search'
    fixedIIsidebarform0.element('input[name=f0]')['_id']='id_for308'
    fixedIIsidebarform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    fixedIIsidebarform0.custom.submit['_type'] = 'submit'
    fixedIIsidebarform0.custom.submit['_id'] = 'id_for310'
    fixedIIsidebarform0.custom.submit['_value'] = 'unk_312'
    fixedIIsidebarform0.custom.submit['_class'] = 'btn btn-navbar'
    fixedIIsidebarform0.custom.submit['_title'] = 'submit fixedIIsidebarform0'

    if fixedIIsidebarform0.accepts(request,session): 
        response.flash0 = 'submitted fixedIIsidebarform0' 
    elif fixedIIsidebarform0.errors:
        response.flash0 = '!Errors! fixedIIsidebarform0' 
    else: 
        response.flash0 = 'fixedIIsidebarform0' 


    return dict( DICT= rows_dict, fixedIIsidebarform0= fixedIIsidebarform0, )

#@auth.requires_login()
def X404():

    qu= db.d404.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/404.html'


    X404form0 = SQLFORM(db.dX404form0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    X404form0.element('input[name=f0]')['_placeholder']='f0 Search'
    X404form0.element('input[name=f0]')['_id']='id_for222'
    X404form0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    X404form0.custom.submit['_type'] = 'submit'
    X404form0.custom.submit['_id'] = 'id_for224'
    X404form0.custom.submit['_value'] = 'unk_226'
    X404form0.custom.submit['_class'] = 'btn btn-navbar'
    X404form0.custom.submit['_title'] = 'submit X404form0'

    if X404form0.accepts(request,session): 
        response.flash0 = 'submitted X404form0' 
    elif X404form0.errors:
        response.flash0 = '!Errors! X404form0' 
    else: 
        response.flash0 = 'X404form0' 



    X404form1 = SQLFORM(db.dX404form1, _class = 'search-form', _id= 'idUnk1' )

    X404form1.element('input[name=f0]')['_placeholder']='f0 Search'
    X404form1.element('input[name=f0]')['_id']='id_for228'
    X404form1.element('input[name=f0]')['_class']='form-control'

    X404form1.custom.submit['_type'] = 'submit'
    X404form1.custom.submit['_id'] = 'id_for230'
    X404form1.custom.submit['_value'] = 'unk_232'
    X404form1.custom.submit['_class'] = 'btn btn-warning'
    X404form1.custom.submit['_title'] = 'submit X404form1'

    if X404form1.accepts(request,session): 
        response.flash1 = 'submitted X404form1' 
    elif X404form1.errors:
        response.flash1 = '!Errors! X404form1' 
    else: 
        response.flash1 = 'X404form1' 


    return dict( DICT= rows_dict, X404form0= X404form0, X404form1= X404form1, )

#@auth.requires_login()
def collapsedIIsidebar():

    qu= db.dcollapsed0sidebar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/collapsed-sidebar.html'


    collapsedIIsidebarform0 = SQLFORM(db.dcollapsedIIsidebarform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    collapsedIIsidebarform0.element('input[name=f0]')['_placeholder']='f0 Search'
    collapsedIIsidebarform0.element('input[name=f0]')['_id']='id_for161'
    collapsedIIsidebarform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    collapsedIIsidebarform0.custom.submit['_type'] = 'submit'
    collapsedIIsidebarform0.custom.submit['_id'] = 'id_for163'
    collapsedIIsidebarform0.custom.submit['_value'] = 'unk_165'
    collapsedIIsidebarform0.custom.submit['_class'] = 'btn btn-navbar'
    collapsedIIsidebarform0.custom.submit['_title'] = 'submit collapsedIIsidebarform0'

    if collapsedIIsidebarform0.accepts(request,session): 
        response.flash0 = 'submitted collapsedIIsidebarform0' 
    elif collapsedIIsidebarform0.errors:
        response.flash0 = '!Errors! collapsedIIsidebarform0' 
    else: 
        response.flash0 = 'collapsedIIsidebarform0' 


    return dict( DICT= rows_dict, collapsedIIsidebarform0= collapsedIIsidebarform0, )

#@auth.requires_login()
def forgotIIpassword():

    qu= db.dforgot0password.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/forgot-password.html'


    forgotIIpasswordform0 = SQLFORM(db.dforgotIIpasswordform0, _class = 'classUnk0', _id= 'idUnk0' )

    forgotIIpasswordform0.element('input[name=f0]')['_placeholder']='f0 Email'
    forgotIIpasswordform0.element('input[name=f0]')['_id']='id_for349'
    forgotIIpasswordform0.element('input[name=f0]')['_class']='form-control'

    forgotIIpasswordform0.custom.submit['_type'] = 'submit'
    forgotIIpasswordform0.custom.submit['_id'] = 'id_for351'
    forgotIIpasswordform0.custom.submit['_value'] = 'Request new password'
    forgotIIpasswordform0.custom.submit['_class'] = 'btn btn-primary btn-block'
    forgotIIpasswordform0.custom.submit['_title'] = 'submit forgotIIpasswordform0'

    if forgotIIpasswordform0.accepts(request,session): 
        response.flash0 = 'submitted forgotIIpasswordform0' 
    elif forgotIIpasswordform0.errors:
        response.flash0 = '!Errors! forgotIIpasswordform0' 
    else: 
        response.flash0 = 'forgotIIpasswordform0' 


    return dict( DICT= rows_dict, forgotIIpasswordform0= forgotIIpasswordform0, )

#@auth.requires_login()
def starter():

    qu= db.dstarter.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/starter.html'


    starterform0 = SQLFORM(db.dstarterform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    starterform0.element('input[name=f0]')['_placeholder']='f0 Search'
    starterform0.element('input[name=f0]')['_id']='id_for143'
    starterform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    starterform0.custom.submit['_type'] = 'submit'
    starterform0.custom.submit['_id'] = 'id_for145'
    starterform0.custom.submit['_value'] = 'unk_147'
    starterform0.custom.submit['_class'] = 'btn btn-navbar'
    starterform0.custom.submit['_title'] = 'submit starterform0'

    if starterform0.accepts(request,session): 
        response.flash0 = 'submitted starterform0' 
    elif starterform0.errors:
        response.flash0 = '!Errors! starterform0' 
    else: 
        response.flash0 = 'starterform0' 


    return dict( DICT= rows_dict, starterform0= starterform0, )

#@auth.requires_login()
def jsgrid():

    qu= db.djsgrid.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/jsgrid.html'


    jsgridform0 = SQLFORM(db.djsgridform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    jsgridform0.element('input[name=f0]')['_placeholder']='f0 Search'
    jsgridform0.element('input[name=f0]')['_id']='id_for192'
    jsgridform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    jsgridform0.custom.submit['_type'] = 'submit'
    jsgridform0.custom.submit['_id'] = 'id_for194'
    jsgridform0.custom.submit['_value'] = 'unk_196'
    jsgridform0.custom.submit['_class'] = 'btn btn-navbar'
    jsgridform0.custom.submit['_title'] = 'submit jsgridform0'

    if jsgridform0.accepts(request,session): 
        response.flash0 = 'submitted jsgridform0' 
    elif jsgridform0.errors:
        response.flash0 = '!Errors! jsgridform0' 
    else: 
        response.flash0 = 'jsgridform0' 


    return dict( DICT= rows_dict, jsgridform0= jsgridform0, )

#@auth.requires_login()
def index():

    qu= db.dindex.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index.html'


    indexform0 = SQLFORM(db.dindexform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    indexform0.element('input[name=f0]')['_placeholder']='f0 Search'
    indexform0.element('input[name=f0]')['_id']='id_for338'
    indexform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    indexform0.custom.submit['_type'] = 'submit'
    indexform0.custom.submit['_id'] = 'id_for340'
    indexform0.custom.submit['_value'] = 'unk_342'
    indexform0.custom.submit['_class'] = 'btn btn-navbar'
    indexform0.custom.submit['_title'] = 'submit indexform0'

    if indexform0.accepts(request,session): 
        response.flash0 = 'submitted indexform0' 
    elif indexform0.errors:
        response.flash0 = '!Errors! indexform0' 
    else: 
        response.flash0 = 'indexform0' 



    indexform1 = SQLFORM(db.dindexform1, _class = 'classUnk1', _id= 'idUnk1' )

    indexform1.element('input[name=f0]')['_placeholder']='f0 Type Message ...'
    indexform1.element('input[name=f0]')['_id']='id_for344'
    indexform1.element('input[name=f0]')['_class']='form-control'

    indexform1.custom.submit['_type'] = 'submit'
    indexform1.custom.submit['_id'] = 'id_for346'
    indexform1.custom.submit['_value'] = 'Send'
    indexform1.custom.submit['_class'] = 'btn btn-primary'
    indexform1.custom.submit['_title'] = 'submit indexform1'

    if indexform1.accepts(request,session): 
        response.flash1 = 'submitted indexform1' 
    elif indexform1.errors:
        response.flash1 = '!Errors! indexform1' 
    else: 
        response.flash1 = 'indexform1' 


    return dict( DICT= rows_dict, indexform0= indexform0, indexform1= indexform1, )

#@auth.requires_login()
def general():

    qu= db.dgeneral.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/general.html'


    generalform0 = SQLFORM(db.dgeneralform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    generalform0.element('input[name=f0]')['_placeholder']='f0 Search'
    generalform0.element('input[name=f0]')['_id']='id_for278'
    generalform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    generalform0.custom.submit['_type'] = 'submit'
    generalform0.custom.submit['_id'] = 'id_for280'
    generalform0.custom.submit['_value'] = 'unk_282'
    generalform0.custom.submit['_class'] = 'btn btn-navbar'
    generalform0.custom.submit['_title'] = 'submit generalform0'

    if generalform0.accepts(request,session): 
        response.flash0 = 'submitted generalform0' 
    elif generalform0.errors:
        response.flash0 = '!Errors! generalform0' 
    else: 
        response.flash0 = 'generalform0' 


    return dict( DICT= rows_dict, generalform0= generalform0, )

#@auth.requires_login()
def buttons():

    qu= db.dbuttons.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/buttons.html'


    buttonsform0 = SQLFORM(db.dbuttonsform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    buttonsform0.element('input[name=f0]')['_placeholder']='f0 Search'
    buttonsform0.element('input[name=f0]')['_id']='id_for44'
    buttonsform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    buttonsform0.custom.submit['_type'] = 'submit'
    buttonsform0.custom.submit['_id'] = 'id_for46'
    buttonsform0.custom.submit['_value'] = 'unk_48'
    buttonsform0.custom.submit['_class'] = 'btn btn-navbar'
    buttonsform0.custom.submit['_title'] = 'submit buttonsform0'

    if buttonsform0.accepts(request,session): 
        response.flash0 = 'submitted buttonsform0' 
    elif buttonsform0.errors:
        response.flash0 = '!Errors! buttonsform0' 
    else: 
        response.flash0 = 'buttonsform0' 


    return dict( DICT= rows_dict, buttonsform0= buttonsform0, )

#@auth.requires_login()
def readIImail():

    qu= db.dread0mail.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/read-mail.html'


    readIImailform0 = SQLFORM(db.dreadIImailform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    readIImailform0.element('input[name=f0]')['_placeholder']='f0 Search'
    readIImailform0.element('input[name=f0]')['_id']='id_for173'
    readIImailform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    readIImailform0.custom.submit['_type'] = 'submit'
    readIImailform0.custom.submit['_id'] = 'id_for175'
    readIImailform0.custom.submit['_value'] = 'unk_177'
    readIImailform0.custom.submit['_class'] = 'btn btn-navbar'
    readIImailform0.custom.submit['_title'] = 'submit readIImailform0'

    if readIImailform0.accepts(request,session): 
        response.flash0 = 'submitted readIImailform0' 
    elif readIImailform0.errors:
        response.flash0 = '!Errors! readIImailform0' 
    else: 
        response.flash0 = 'readIImailform0' 


    return dict( DICT= rows_dict, readIImailform0= readIImailform0, )

#@auth.requires_login()
def simple():

    qu= db.dsimple.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/simple.html'


    simpleform0 = SQLFORM(db.dsimpleform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    simpleform0.element('input[name=f0]')['_placeholder']='f0 Search'
    simpleform0.element('input[name=f0]')['_id']='id_for137'
    simpleform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    simpleform0.custom.submit['_type'] = 'submit'
    simpleform0.custom.submit['_id'] = 'id_for139'
    simpleform0.custom.submit['_value'] = 'unk_141'
    simpleform0.custom.submit['_class'] = 'btn btn-navbar'
    simpleform0.custom.submit['_title'] = 'submit simpleform0'

    if simpleform0.accepts(request,session): 
        response.flash0 = 'submitted simpleform0' 
    elif simpleform0.errors:
        response.flash0 = '!Errors! simpleform0' 
    else: 
        response.flash0 = 'simpleform0' 


    return dict( DICT= rows_dict, simpleform0= simpleform0, )

#@auth.requires_login()
def data():

    qu= db.ddata.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/data.html'


    dataform0 = SQLFORM(db.ddataform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    dataform0.element('input[name=f0]')['_placeholder']='f0 Search'
    dataform0.element('input[name=f0]')['_id']='id_for216'
    dataform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    dataform0.custom.submit['_type'] = 'submit'
    dataform0.custom.submit['_id'] = 'id_for218'
    dataform0.custom.submit['_value'] = 'unk_220'
    dataform0.custom.submit['_class'] = 'btn btn-navbar'
    dataform0.custom.submit['_title'] = 'submit dataform0'

    if dataform0.accepts(request,session): 
        response.flash0 = 'submitted dataform0' 
    elif dataform0.errors:
        response.flash0 = '!Errors! dataform0' 
    else: 
        response.flash0 = 'dataform0' 


    return dict( DICT= rows_dict, dataform0= dataform0, )

#@auth.requires_login()
def login():

    qu= db.dlogin.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/login.html'


    loginform0 = SQLFORM(db.dloginform0, _class = 'classUnk0', _id= 'idUnk0' )

    loginform0.element('input[name=f0]')['_placeholder']='f0 Email'
    loginform0.element('input[name=f0]')['_id']='id_for121'
    loginform0.element('input[name=f0]')['_class']='form-control'
    loginform0.element('input[name=f1]')['_placeholder']='f1 Password'
    loginform0.element('input[name=f1]')['_id']='id_for123'
    loginform0.element('input[name=f1]')['_class']='form-control'
    loginform0.element('input[name=f2]')['_placeholder']='f2 place_127'
    loginform0.element('input[name=f2]')['_id']='remember'

    loginform0.custom.submit['_type'] = 'submit'
    loginform0.custom.submit['_id'] = 'id_for128'
    loginform0.custom.submit['_value'] = 'Sign In'
    loginform0.custom.submit['_class'] = 'btn btn-primary btn-block'
    loginform0.custom.submit['_title'] = 'submit loginform0'

    if loginform0.accepts(request,session): 
        response.flash0 = 'submitted loginform0' 
    elif loginform0.errors:
        response.flash0 = '!Errors! loginform0' 
    else: 
        response.flash0 = 'loginform0' 


    return dict( DICT= rows_dict, loginform0= loginform0, )

#@auth.requires_login()
def navbar():

    qu= db.dnavbar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/navbar.html'


    navbarform0 = SQLFORM(db.dnavbarform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    navbarform0.element('input[name=f0]')['_placeholder']='f0 Search'
    navbarform0.element('input[name=f0]')['_id']='id_for383'
    navbarform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    navbarform0.custom.submit['_type'] = 'submit'
    navbarform0.custom.submit['_id'] = 'id_for385'
    navbarform0.custom.submit['_value'] = 'unk_387'
    navbarform0.custom.submit['_class'] = 'btn btn-navbar'
    navbarform0.custom.submit['_title'] = 'submit navbarform0'

    if navbarform0.accepts(request,session): 
        response.flash0 = 'submitted navbarform0' 
    elif navbarform0.errors:
        response.flash0 = '!Errors! navbarform0' 
    else: 
        response.flash0 = 'navbarform0' 



    navbarform1 = SQLFORM(db.dnavbarform1, _class = 'form-inline ml-3', _id= 'idUnk1' )

    navbarform1.element('input[name=f0]')['_placeholder']='f0 Search'
    navbarform1.element('input[name=f0]')['_id']='id_for389'
    navbarform1.element('input[name=f0]')['_class']='form-control form-control-navbar'

    navbarform1.custom.submit['_type'] = 'submit'
    navbarform1.custom.submit['_id'] = 'id_for391'
    navbarform1.custom.submit['_value'] = 'unk_393'
    navbarform1.custom.submit['_class'] = 'btn btn-navbar'
    navbarform1.custom.submit['_title'] = 'submit navbarform1'

    if navbarform1.accepts(request,session): 
        response.flash1 = 'submitted navbarform1' 
    elif navbarform1.errors:
        response.flash1 = '!Errors! navbarform1' 
    else: 
        response.flash1 = 'navbarform1' 



    navbarform2 = SQLFORM(db.dnavbarform2, _class = 'form-inline ml-3', _id= 'idUnk2' )

    navbarform2.element('input[name=f0]')['_placeholder']='f0 Search'
    navbarform2.element('input[name=f0]')['_id']='id_for395'
    navbarform2.element('input[name=f0]')['_class']='form-control form-control-navbar'

    navbarform2.custom.submit['_type'] = 'submit'
    navbarform2.custom.submit['_id'] = 'id_for397'
    navbarform2.custom.submit['_value'] = 'unk_399'
    navbarform2.custom.submit['_class'] = 'btn btn-navbar'
    navbarform2.custom.submit['_title'] = 'submit navbarform2'

    if navbarform2.accepts(request,session): 
        response.flash2 = 'submitted navbarform2' 
    elif navbarform2.errors:
        response.flash2 = '!Errors! navbarform2' 
    else: 
        response.flash2 = 'navbarform2' 



    navbarform3 = SQLFORM(db.dnavbarform3, _class = 'form-inline ml-3', _id= 'idUnk3' )

    navbarform3.element('input[name=f0]')['_placeholder']='f0 Search'
    navbarform3.element('input[name=f0]')['_id']='id_for401'
    navbarform3.element('input[name=f0]')['_class']='form-control form-control-navbar'

    navbarform3.custom.submit['_type'] = 'submit'
    navbarform3.custom.submit['_id'] = 'id_for403'
    navbarform3.custom.submit['_value'] = 'unk_405'
    navbarform3.custom.submit['_class'] = 'btn btn-navbar'
    navbarform3.custom.submit['_title'] = 'submit navbarform3'

    if navbarform3.accepts(request,session): 
        response.flash3 = 'submitted navbarform3' 
    elif navbarform3.errors:
        response.flash3 = '!Errors! navbarform3' 
    else: 
        response.flash3 = 'navbarform3' 



    navbarform4 = SQLFORM(db.dnavbarform4, _class = 'form-inline ml-3', _id= 'idUnk4' )

    navbarform4.element('input[name=f0]')['_placeholder']='f0 Search'
    navbarform4.element('input[name=f0]')['_id']='id_for407'
    navbarform4.element('input[name=f0]')['_class']='form-control form-control-navbar'

    navbarform4.custom.submit['_type'] = 'submit'
    navbarform4.custom.submit['_id'] = 'id_for409'
    navbarform4.custom.submit['_value'] = 'unk_411'
    navbarform4.custom.submit['_class'] = 'btn btn-navbar'
    navbarform4.custom.submit['_title'] = 'submit navbarform4'

    if navbarform4.accepts(request,session): 
        response.flash4 = 'submitted navbarform4' 
    elif navbarform4.errors:
        response.flash4 = '!Errors! navbarform4' 
    else: 
        response.flash4 = 'navbarform4' 



    navbarform5 = SQLFORM(db.dnavbarform5, _class = 'form-inline ml-3', _id= 'idUnk5' )

    navbarform5.element('input[name=f0]')['_placeholder']='f0 Search'
    navbarform5.element('input[name=f0]')['_id']='id_for413'
    navbarform5.element('input[name=f0]')['_class']='form-control form-control-navbar'

    navbarform5.custom.submit['_type'] = 'submit'
    navbarform5.custom.submit['_id'] = 'id_for415'
    navbarform5.custom.submit['_value'] = 'unk_417'
    navbarform5.custom.submit['_class'] = 'btn btn-navbar'
    navbarform5.custom.submit['_title'] = 'submit navbarform5'

    if navbarform5.accepts(request,session): 
        response.flash5 = 'submitted navbarform5' 
    elif navbarform5.errors:
        response.flash5 = '!Errors! navbarform5' 
    else: 
        response.flash5 = 'navbarform5' 



    navbarform6 = SQLFORM(db.dnavbarform6, _class = 'form-inline ml-3', _id= 'idUnk6' )

    navbarform6.element('input[name=f0]')['_placeholder']='f0 Search'
    navbarform6.element('input[name=f0]')['_id']='id_for419'
    navbarform6.element('input[name=f0]')['_class']='form-control form-control-navbar'

    navbarform6.custom.submit['_type'] = 'submit'
    navbarform6.custom.submit['_id'] = 'id_for421'
    navbarform6.custom.submit['_value'] = 'unk_423'
    navbarform6.custom.submit['_class'] = 'btn btn-navbar'
    navbarform6.custom.submit['_title'] = 'submit navbarform6'

    if navbarform6.accepts(request,session): 
        response.flash6 = 'submitted navbarform6' 
    elif navbarform6.errors:
        response.flash6 = '!Errors! navbarform6' 
    else: 
        response.flash6 = 'navbarform6' 


    return dict( DICT= rows_dict, navbarform0= navbarform0, navbarform1= navbarform1, navbarform2= navbarform2, navbarform3= navbarform3, navbarform4= navbarform4, navbarform5= navbarform5, navbarform6= navbarform6, )

#@auth.requires_login()
def recoverIIpassword():

    qu= db.drecover0password.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/recover-password.html'


    recoverIIpasswordform0 = SQLFORM(db.drecoverIIpasswordform0, _class = 'classUnk0', _id= 'idUnk0' )

    recoverIIpasswordform0.element('input[name=f0]')['_placeholder']='f0 Password'
    recoverIIpasswordform0.element('input[name=f0]')['_id']='id_for179'
    recoverIIpasswordform0.element('input[name=f0]')['_class']='form-control'
    recoverIIpasswordform0.element('input[name=f1]')['_placeholder']='f1 Confirm Password'
    recoverIIpasswordform0.element('input[name=f1]')['_id']='id_for181'
    recoverIIpasswordform0.element('input[name=f1]')['_class']='form-control'

    recoverIIpasswordform0.custom.submit['_type'] = 'submit'
    recoverIIpasswordform0.custom.submit['_id'] = 'id_for183'
    recoverIIpasswordform0.custom.submit['_value'] = 'Change password'
    recoverIIpasswordform0.custom.submit['_class'] = 'btn btn-primary btn-block'
    recoverIIpasswordform0.custom.submit['_title'] = 'submit recoverIIpasswordform0'

    if recoverIIpasswordform0.accepts(request,session): 
        response.flash0 = 'submitted recoverIIpasswordform0' 
    elif recoverIIpasswordform0.errors:
        response.flash0 = '!Errors! recoverIIpasswordform0' 
    else: 
        response.flash0 = 'recoverIIpasswordform0' 


    return dict( DICT= rows_dict, recoverIIpasswordform0= recoverIIpasswordform0, )

#@auth.requires_login()
def profile():

    qu= db.dprofile.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/profile.html'


    profileform0 = SQLFORM(db.dprofileform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    profileform0.element('input[name=f0]')['_placeholder']='f0 Search'
    profileform0.element('input[name=f0]')['_id']='id_for234'
    profileform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    profileform0.custom.submit['_type'] = 'submit'
    profileform0.custom.submit['_id'] = 'id_for236'
    profileform0.custom.submit['_value'] = 'unk_238'
    profileform0.custom.submit['_class'] = 'btn btn-navbar'
    profileform0.custom.submit['_title'] = 'submit profileform0'

    if profileform0.accepts(request,session): 
        response.flash0 = 'submitted profileform0' 
    elif profileform0.errors:
        response.flash0 = '!Errors! profileform0' 
    else: 
        response.flash0 = 'profileform0' 



    profileform1 = SQLFORM(db.dprofileform1, _class = 'form-horizontal', _id= 'idUnk1' )

    profileform1.element('input[name=f0]')['_placeholder']='f0 Response'
    profileform1.element('input[name=f0]')['_id']='id_for240'
    profileform1.element('input[name=f0]')['_class']='form-control form-control-sm'

    profileform1.custom.submit['_type'] = 'submit'
    profileform1.custom.submit['_id'] = 'id_for242'
    profileform1.custom.submit['_value'] = 'Send'
    profileform1.custom.submit['_class'] = 'btn btn-danger'
    profileform1.custom.submit['_title'] = 'submit profileform1'

    if profileform1.accepts(request,session): 
        response.flash1 = 'submitted profileform1' 
    elif profileform1.errors:
        response.flash1 = '!Errors! profileform1' 
    else: 
        response.flash1 = 'profileform1' 



    profileform2 = SQLFORM(db.dprofileform2, _class = 'form-horizontal', _id= 'idUnk2' )

    profileform2.element('input[name=f0]')['_placeholder']='f0 Name'
    profileform2.element('input[name=f0]')['_id']='inputName'
    profileform2.element('input[name=f0]')['_class']='form-control'
    profileform2.element('input[name=f1]')['_placeholder']='f1 Email'
    profileform2.element('input[name=f1]')['_id']='inputEmail'
    profileform2.element('input[name=f1]')['_class']='form-control'
    profileform2.element('input[name=f2]')['_placeholder']='f2 Name'
    profileform2.element('input[name=f2]')['_id']='inputName2'
    profileform2.element('input[name=f2]')['_class']='form-control'
    profileform2.element('input[name=f3]')['_placeholder']='f3 Skills'
    profileform2.element('input[name=f3]')['_id']='inputSkills'
    profileform2.element('input[name=f3]')['_class']='form-control'
    profileform2.element('input[name=f4]')['_placeholder']='f4 place_256'
    profileform2.element('input[name=f4]')['_id']='id_for253'
    profileform2.element('textarea[name=f5]')['_placeholder']='f5 Experience'
    profileform2.element('textarea[name=f5]')['_id']='inputExperience'
    profileform2.element('textarea[name=f5]')['_class']='form-control'

    profileform2.custom.submit['_type'] = 'submit'
    profileform2.custom.submit['_id'] = 'id_for259'
    profileform2.custom.submit['_value'] = 'Submit'
    profileform2.custom.submit['_class'] = 'btn btn-danger'
    profileform2.custom.submit['_title'] = 'submit profileform2'

    profileform2.custom.submit['_id'] = 'id_for262'
    profileform2.custom.submit['_title'] = 'submit profileform2'

    if profileform2.accepts(request,session): 
        response.flash2 = 'submitted profileform2' 
    elif profileform2.errors:
        response.flash2 = '!Errors! profileform2' 
    else: 
        response.flash2 = 'profileform2' 


    return dict( DICT= rows_dict, profileform0= profileform0, profileform1= profileform1, profileform2= profileform2, )

#@auth.requires_login()
def editors():

    qu= db.deditors.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/editors.html'


    editorsform0 = SQLFORM(db.deditorsform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    editorsform0.element('input[name=f0]')['_placeholder']='f0 Search'
    editorsform0.element('input[name=f0]')['_id']='id_for320'
    editorsform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    editorsform0.custom.submit['_type'] = 'submit'
    editorsform0.custom.submit['_id'] = 'id_for322'
    editorsform0.custom.submit['_value'] = 'unk_324'
    editorsform0.custom.submit['_class'] = 'btn btn-navbar'
    editorsform0.custom.submit['_title'] = 'submit editorsform0'

    if editorsform0.accepts(request,session): 
        response.flash0 = 'submitted editorsform0' 
    elif editorsform0.errors:
        response.flash0 = '!Errors! editorsform0' 
    else: 
        response.flash0 = 'editorsform0' 


    return dict( DICT= rows_dict, editorsform0= editorsform0, )

#@auth.requires_login()
def invoice():

    qu= db.dinvoice.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/invoice.html'


    invoiceform0 = SQLFORM(db.dinvoiceform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    invoiceform0.element('input[name=f0]')['_placeholder']='f0 Search'
    invoiceform0.element('input[name=f0]')['_id']='id_for86'
    invoiceform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    invoiceform0.custom.submit['_type'] = 'submit'
    invoiceform0.custom.submit['_id'] = 'id_for88'
    invoiceform0.custom.submit['_value'] = 'unk_90'
    invoiceform0.custom.submit['_class'] = 'btn btn-navbar'
    invoiceform0.custom.submit['_title'] = 'submit invoiceform0'

    if invoiceform0.accepts(request,session): 
        response.flash0 = 'submitted invoiceform0' 
    elif invoiceform0.errors:
        response.flash0 = '!Errors! invoiceform0' 
    else: 
        response.flash0 = 'invoiceform0' 


    return dict( DICT= rows_dict, invoiceform0= invoiceform0, )

#@auth.requires_login()
def fixedIItopnav():

    qu= db.dfixed0topnav.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/fixed-topnav.html'


    fixedIItopnavform0 = SQLFORM(db.dfixedIItopnavform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    fixedIItopnavform0.element('input[name=f0]')['_placeholder']='f0 Search'
    fixedIItopnavform0.element('input[name=f0]')['_id']='id_for210'
    fixedIItopnavform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    fixedIItopnavform0.custom.submit['_type'] = 'submit'
    fixedIItopnavform0.custom.submit['_id'] = 'id_for212'
    fixedIItopnavform0.custom.submit['_value'] = 'unk_214'
    fixedIItopnavform0.custom.submit['_class'] = 'btn btn-navbar'
    fixedIItopnavform0.custom.submit['_title'] = 'submit fixedIItopnavform0'

    if fixedIItopnavform0.accepts(request,session): 
        response.flash0 = 'submitted fixedIItopnavform0' 
    elif fixedIItopnavform0.errors:
        response.flash0 = '!Errors! fixedIItopnavform0' 
    else: 
        response.flash0 = 'fixedIItopnavform0' 


    return dict( DICT= rows_dict, fixedIItopnavform0= fixedIItopnavform0, )

#@auth.requires_login()
def lockscreen():

    qu= db.dlockscreen.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/lockscreen.html'


    lockscreenform0 = SQLFORM(db.dlockscreenform0, _class = 'lockscreen-credentials', _id= 'idUnk0' )

    lockscreenform0.element('input[name=f0]')['_placeholder']='f0 password'
    lockscreenform0.element('input[name=f0]')['_id']='id_for332'
    lockscreenform0.element('input[name=f0]')['_class']='form-control'

    lockscreenform0.custom.submit['_type'] = 'submit'
    lockscreenform0.custom.submit['_id'] = 'id_for334'
    lockscreenform0.custom.submit['_value'] = 'unk_336'
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


    composeform0 = SQLFORM(db.dcomposeform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    composeform0.element('input[name=f0]')['_placeholder']='f0 Search'
    composeform0.element('input[name=f0]')['_id']='id_for461'
    composeform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    composeform0.custom.submit['_type'] = 'submit'
    composeform0.custom.submit['_id'] = 'id_for463'
    composeform0.custom.submit['_value'] = 'unk_465'
    composeform0.custom.submit['_class'] = 'btn btn-navbar'
    composeform0.custom.submit['_title'] = 'submit composeform0'

    if composeform0.accepts(request,session): 
        response.flash0 = 'submitted composeform0' 
    elif composeform0.errors:
        response.flash0 = '!Errors! composeform0' 
    else: 
        response.flash0 = 'composeform0' 


    return dict( DICT= rows_dict, composeform0= composeform0, )

#@auth.requires_login()
def projectIIdetail():

    qu= db.dproject0detail.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/project_detail.html'


    projectIIdetailform0 = SQLFORM(db.dprojectIIdetailform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    projectIIdetailform0.element('input[name=f0]')['_placeholder']='f0 Search'
    projectIIdetailform0.element('input[name=f0]')['_id']='id_for354'
    projectIIdetailform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    projectIIdetailform0.custom.submit['_type'] = 'submit'
    projectIIdetailform0.custom.submit['_id'] = 'id_for356'
    projectIIdetailform0.custom.submit['_value'] = 'unk_358'
    projectIIdetailform0.custom.submit['_class'] = 'btn btn-navbar'
    projectIIdetailform0.custom.submit['_title'] = 'submit projectIIdetailform0'

    if projectIIdetailform0.accepts(request,session): 
        response.flash0 = 'submitted projectIIdetailform0' 
    elif projectIIdetailform0.errors:
        response.flash0 = '!Errors! projectIIdetailform0' 
    else: 
        response.flash0 = 'projectIIdetailform0' 


    return dict( DICT= rows_dict, projectIIdetailform0= projectIIdetailform0, )

#@auth.requires_login()
def fixedIIfooter():

    qu= db.dfixed0footer.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/fixed-footer.html'


    fixedIIfooterform0 = SQLFORM(db.dfixedIIfooterform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    fixedIIfooterform0.element('input[name=f0]')['_placeholder']='f0 Search'
    fixedIIfooterform0.element('input[name=f0]')['_id']='id_for467'
    fixedIIfooterform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    fixedIIfooterform0.custom.submit['_type'] = 'submit'
    fixedIIfooterform0.custom.submit['_id'] = 'id_for469'
    fixedIIfooterform0.custom.submit['_value'] = 'unk_471'
    fixedIIfooterform0.custom.submit['_class'] = 'btn btn-navbar'
    fixedIIfooterform0.custom.submit['_title'] = 'submit fixedIIfooterform0'

    if fixedIIfooterform0.accepts(request,session): 
        response.flash0 = 'submitted fixedIIfooterform0' 
    elif fixedIIfooterform0.errors:
        response.flash0 = '!Errors! fixedIIfooterform0' 
    else: 
        response.flash0 = 'fixedIIfooterform0' 


    return dict( DICT= rows_dict, fixedIIfooterform0= fixedIIfooterform0, )

#@auth.requires_login()
def blank():

    qu= db.dblank.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/blank.html'


    blankform0 = SQLFORM(db.dblankform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    blankform0.element('input[name=f0]')['_placeholder']='f0 Search'
    blankform0.element('input[name=f0]')['_id']='id_for186'
    blankform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    blankform0.custom.submit['_type'] = 'submit'
    blankform0.custom.submit['_id'] = 'id_for188'
    blankform0.custom.submit['_value'] = 'unk_190'
    blankform0.custom.submit['_class'] = 'btn btn-navbar'
    blankform0.custom.submit['_title'] = 'submit blankform0'

    if blankform0.accepts(request,session): 
        response.flash0 = 'submitted blankform0' 
    elif blankform0.errors:
        response.flash0 = '!Errors! blankform0' 
    else: 
        response.flash0 = 'blankform0' 


    return dict( DICT= rows_dict, blankform0= blankform0, )

#@auth.requires_login()
def icons():

    qu= db.dicons.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/icons.html'


    iconsform0 = SQLFORM(db.diconsform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    iconsform0.element('input[name=f0]')['_placeholder']='f0 Search'
    iconsform0.element('input[name=f0]')['_id']='id_for204'
    iconsform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    iconsform0.custom.submit['_type'] = 'submit'
    iconsform0.custom.submit['_id'] = 'id_for206'
    iconsform0.custom.submit['_value'] = 'unk_208'
    iconsform0.custom.submit['_class'] = 'btn btn-navbar'
    iconsform0.custom.submit['_title'] = 'submit iconsform0'

    if iconsform0.accepts(request,session): 
        response.flash0 = 'submitted iconsform0' 
    elif iconsform0.errors:
        response.flash0 = '!Errors! iconsform0' 
    else: 
        response.flash0 = 'iconsform0' 


    return dict( DICT= rows_dict, iconsform0= iconsform0, )

#@auth.requires_login()
def invoiceIIprint():

    qu= db.dinvoice0print.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/invoice-print.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def legacyIIuserIImenu():

    qu= db.dlegacy0user0menu.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/legacy-user-menu.html'


    legacyIIuserIImenuform0 = SQLFORM(db.dlegacyIIuserIImenuform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    legacyIIuserIImenuform0.element('input[name=f0]')['_placeholder']='f0 Search'
    legacyIIuserIImenuform0.element('input[name=f0]')['_id']='id_for50'
    legacyIIuserIImenuform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    legacyIIuserIImenuform0.custom.submit['_type'] = 'submit'
    legacyIIuserIImenuform0.custom.submit['_id'] = 'id_for52'
    legacyIIuserIImenuform0.custom.submit['_value'] = 'unk_54'
    legacyIIuserIImenuform0.custom.submit['_class'] = 'btn btn-navbar'
    legacyIIuserIImenuform0.custom.submit['_title'] = 'submit legacyIIuserIImenuform0'

    if legacyIIuserIImenuform0.accepts(request,session): 
        response.flash0 = 'submitted legacyIIuserIImenuform0' 
    elif legacyIIuserIImenuform0.errors:
        response.flash0 = '!Errors! legacyIIuserIImenuform0' 
    else: 
        response.flash0 = 'legacyIIuserIImenuform0' 


    return dict( DICT= rows_dict, legacyIIuserIImenuform0= legacyIIuserIImenuform0, )

#@auth.requires_login()
def topIInav():

    qu= db.dtop0nav.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/top-nav.html'


    topIInavform0 = SQLFORM(db.dtopIInavform0, _class = 'form-inline ml-0 ml-md-3', _id= 'idUnk0' )

    topIInavform0.element('input[name=f0]')['_placeholder']='f0 Search'
    topIInavform0.element('input[name=f0]')['_id']='id_for266'
    topIInavform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    topIInavform0.custom.submit['_type'] = 'submit'
    topIInavform0.custom.submit['_id'] = 'id_for268'
    topIInavform0.custom.submit['_value'] = 'unk_270'
    topIInavform0.custom.submit['_class'] = 'btn btn-navbar'
    topIInavform0.custom.submit['_title'] = 'submit topIInavform0'

    if topIInavform0.accepts(request,session): 
        response.flash0 = 'submitted topIInavform0' 
    elif topIInavform0.errors:
        response.flash0 = '!Errors! topIInavform0' 
    else: 
        response.flash0 = 'topIInavform0' 


    return dict( DICT= rows_dict, topIInavform0= topIInavform0, )

#@auth.requires_login()
def contacts():

    qu= db.dcontacts.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/contacts.html'


    contactsform0 = SQLFORM(db.dcontactsform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    contactsform0.element('input[name=f0]')['_placeholder']='f0 Search'
    contactsform0.element('input[name=f0]')['_id']='id_for92'
    contactsform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    contactsform0.custom.submit['_type'] = 'submit'
    contactsform0.custom.submit['_id'] = 'id_for94'
    contactsform0.custom.submit['_value'] = 'unk_96'
    contactsform0.custom.submit['_class'] = 'btn btn-navbar'
    contactsform0.custom.submit['_title'] = 'submit contactsform0'

    if contactsform0.accepts(request,session): 
        response.flash0 = 'submitted contactsform0' 
    elif contactsform0.errors:
        response.flash0 = '!Errors! contactsform0' 
    else: 
        response.flash0 = 'contactsform0' 


    return dict( DICT= rows_dict, contactsform0= contactsform0, )

#@auth.requires_login()
def calendar():

    qu= db.dcalendar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/calendar.html'


    calendarform0 = SQLFORM(db.dcalendarform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    calendarform0.element('input[name=f0]')['_placeholder']='f0 Search'
    calendarform0.element('input[name=f0]')['_id']='id_for449'
    calendarform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    calendarform0.custom.submit['_type'] = 'submit'
    calendarform0.custom.submit['_id'] = 'id_for451'
    calendarform0.custom.submit['_value'] = 'unk_453'
    calendarform0.custom.submit['_class'] = 'btn btn-navbar'
    calendarform0.custom.submit['_title'] = 'submit calendarform0'

    if calendarform0.accepts(request,session): 
        response.flash0 = 'submitted calendarform0' 
    elif calendarform0.errors:
        response.flash0 = '!Errors! calendarform0' 
    else: 
        response.flash0 = 'calendarform0' 


    return dict( DICT= rows_dict, calendarform0= calendarform0, )

#@auth.requires_login()
def mailbox():

    qu= db.dmailbox.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/mailbox.html'


    mailboxform0 = SQLFORM(db.dmailboxform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    mailboxform0.element('input[name=f0]')['_placeholder']='f0 Search'
    mailboxform0.element('input[name=f0]')['_id']='id_for98'
    mailboxform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    mailboxform0.custom.submit['_type'] = 'submit'
    mailboxform0.custom.submit['_id'] = 'id_for100'
    mailboxform0.custom.submit['_value'] = 'unk_102'
    mailboxform0.custom.submit['_class'] = 'btn btn-navbar'
    mailboxform0.custom.submit['_title'] = 'submit mailboxform0'

    if mailboxform0.accepts(request,session): 
        response.flash0 = 'submitted mailboxform0' 
    elif mailboxform0.errors:
        response.flash0 = '!Errors! mailboxform0' 
    else: 
        response.flash0 = 'mailboxform0' 


    return dict( DICT= rows_dict, mailboxform0= mailboxform0, )

#@auth.requires_login()
def pace():

    qu= db.dpace.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/pace.html'


    paceform0 = SQLFORM(db.dpaceform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    paceform0.element('input[name=f0]')['_placeholder']='f0 Search'
    paceform0.element('input[name=f0]')['_id']='id_for284'
    paceform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    paceform0.custom.submit['_type'] = 'submit'
    paceform0.custom.submit['_id'] = 'id_for286'
    paceform0.custom.submit['_value'] = 'unk_288'
    paceform0.custom.submit['_class'] = 'btn btn-navbar'
    paceform0.custom.submit['_title'] = 'submit paceform0'

    if paceform0.accepts(request,session): 
        response.flash0 = 'submitted paceform0' 
    elif paceform0.errors:
        response.flash0 = '!Errors! paceform0' 
    else: 
        response.flash0 = 'paceform0' 


    return dict( DICT= rows_dict, paceform0= paceform0, )

#@auth.requires_login()
def flot():

    qu= db.dflot.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/flot.html'


    flotform0 = SQLFORM(db.dflotform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    flotform0.element('input[name=f0]')['_placeholder']='f0 Search'
    flotform0.element('input[name=f0]')['_id']='id_for198'
    flotform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    flotform0.custom.submit['_type'] = 'submit'
    flotform0.custom.submit['_id'] = 'id_for200'
    flotform0.custom.submit['_value'] = 'unk_202'
    flotform0.custom.submit['_class'] = 'btn btn-navbar'
    flotform0.custom.submit['_title'] = 'submit flotform0'

    if flotform0.accepts(request,session): 
        response.flash0 = 'submitted flotform0' 
    elif flotform0.errors:
        response.flash0 = '!Errors! flotform0' 
    else: 
        response.flash0 = 'flotform0' 


    return dict( DICT= rows_dict, flotform0= flotform0, )

#@auth.requires_login()
def projectIIadd():

    qu= db.dproject0add.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/project_add.html'


    projectIIaddform0 = SQLFORM(db.dprojectIIaddform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    projectIIaddform0.element('input[name=f0]')['_placeholder']='f0 Search'
    projectIIaddform0.element('input[name=f0]')['_id']='id_for131'
    projectIIaddform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    projectIIaddform0.custom.submit['_type'] = 'submit'
    projectIIaddform0.custom.submit['_id'] = 'id_for133'
    projectIIaddform0.custom.submit['_value'] = 'unk_135'
    projectIIaddform0.custom.submit['_class'] = 'btn btn-navbar'
    projectIIaddform0.custom.submit['_title'] = 'submit projectIIaddform0'

    if projectIIaddform0.accepts(request,session): 
        response.flash0 = 'submitted projectIIaddform0' 
    elif projectIIaddform0.errors:
        response.flash0 = '!Errors! projectIIaddform0' 
    else: 
        response.flash0 = 'projectIIaddform0' 


    return dict( DICT= rows_dict, projectIIaddform0= projectIIaddform0, )

#@auth.requires_login()
def chartjs():

    qu= db.dchartjs.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/chartjs.html'


    chartjsform0 = SQLFORM(db.dchartjsform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    chartjsform0.element('input[name=f0]')['_placeholder']='f0 Search'
    chartjsform0.element('input[name=f0]')['_id']='id_for314'
    chartjsform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    chartjsform0.custom.submit['_type'] = 'submit'
    chartjsform0.custom.submit['_id'] = 'id_for316'
    chartjsform0.custom.submit['_value'] = 'unk_318'
    chartjsform0.custom.submit['_class'] = 'btn btn-navbar'
    chartjsform0.custom.submit['_title'] = 'submit chartjsform0'

    if chartjsform0.accepts(request,session): 
        response.flash0 = 'submitted chartjsform0' 
    elif chartjsform0.errors:
        response.flash0 = '!Errors! chartjsform0' 
    else: 
        response.flash0 = 'chartjsform0' 


    return dict( DICT= rows_dict, chartjsform0= chartjsform0, )

#@auth.requires_login()
def widgets():

    qu= db.dwidgets.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/widgets.html'


    widgetsform0 = SQLFORM(db.dwidgetsform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    widgetsform0.element('input[name=f0]')['_placeholder']='f0 Search'
    widgetsform0.element('input[name=f0]')['_id']='id_for56'
    widgetsform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    widgetsform0.custom.submit['_type'] = 'submit'
    widgetsform0.custom.submit['_id'] = 'id_for58'
    widgetsform0.custom.submit['_value'] = 'unk_60'
    widgetsform0.custom.submit['_class'] = 'btn btn-navbar'
    widgetsform0.custom.submit['_title'] = 'submit widgetsform0'

    if widgetsform0.accepts(request,session): 
        response.flash0 = 'submitted widgetsform0' 
    elif widgetsform0.errors:
        response.flash0 = '!Errors! widgetsform0' 
    else: 
        response.flash0 = 'widgetsform0' 



    widgetsform1 = SQLFORM(db.dwidgetsform1, _class = 'classUnk1', _id= 'idUnk1' )

    widgetsform1.element('input[name=f0]')['_placeholder']='f0 Type Message ...'
    widgetsform1.element('input[name=f0]')['_id']='id_for62'
    widgetsform1.element('input[name=f0]')['_class']='form-control'

    widgetsform1.custom.submit['_type'] = 'submit'
    widgetsform1.custom.submit['_id'] = 'id_for64'
    widgetsform1.custom.submit['_value'] = 'Send'
    widgetsform1.custom.submit['_class'] = 'btn btn-primary'
    widgetsform1.custom.submit['_title'] = 'submit widgetsform1'

    if widgetsform1.accepts(request,session): 
        response.flash1 = 'submitted widgetsform1' 
    elif widgetsform1.errors:
        response.flash1 = '!Errors! widgetsform1' 
    else: 
        response.flash1 = 'widgetsform1' 



    widgetsform2 = SQLFORM(db.dwidgetsform2, _class = 'classUnk2', _id= 'idUnk2' )

    widgetsform2.element('input[name=f0]')['_placeholder']='f0 Type Message ...'
    widgetsform2.element('input[name=f0]')['_id']='id_for67'
    widgetsform2.element('input[name=f0]')['_class']='form-control'

    widgetsform2.custom.submit['_type'] = 'submit'
    widgetsform2.custom.submit['_id'] = 'id_for69'
    widgetsform2.custom.submit['_value'] = 'Send'
    widgetsform2.custom.submit['_class'] = 'btn btn-success'
    widgetsform2.custom.submit['_title'] = 'submit widgetsform2'

    if widgetsform2.accepts(request,session): 
        response.flash2 = 'submitted widgetsform2' 
    elif widgetsform2.errors:
        response.flash2 = '!Errors! widgetsform2' 
    else: 
        response.flash2 = 'widgetsform2' 



    widgetsform3 = SQLFORM(db.dwidgetsform3, _class = 'classUnk3', _id= 'idUnk3' )

    widgetsform3.element('input[name=f0]')['_placeholder']='f0 Type Message ...'
    widgetsform3.element('input[name=f0]')['_id']='id_for72'
    widgetsform3.element('input[name=f0]')['_class']='form-control'

    widgetsform3.custom.submit['_type'] = 'submit'
    widgetsform3.custom.submit['_id'] = 'id_for74'
    widgetsform3.custom.submit['_value'] = 'Send'
    widgetsform3.custom.submit['_class'] = 'btn btn-warning'
    widgetsform3.custom.submit['_title'] = 'submit widgetsform3'

    if widgetsform3.accepts(request,session): 
        response.flash3 = 'submitted widgetsform3' 
    elif widgetsform3.errors:
        response.flash3 = '!Errors! widgetsform3' 
    else: 
        response.flash3 = 'widgetsform3' 



    widgetsform4 = SQLFORM(db.dwidgetsform4, _class = 'classUnk4', _id= 'idUnk4' )

    widgetsform4.element('input[name=f0]')['_placeholder']='f0 Type Message ...'
    widgetsform4.element('input[name=f0]')['_id']='id_for77'
    widgetsform4.element('input[name=f0]')['_class']='form-control'

    widgetsform4.custom.submit['_type'] = 'submit'
    widgetsform4.custom.submit['_id'] = 'id_for79'
    widgetsform4.custom.submit['_value'] = 'Send'
    widgetsform4.custom.submit['_class'] = 'btn btn-danger'
    widgetsform4.custom.submit['_title'] = 'submit widgetsform4'

    if widgetsform4.accepts(request,session): 
        response.flash4 = 'submitted widgetsform4' 
    elif widgetsform4.errors:
        response.flash4 = '!Errors! widgetsform4' 
    else: 
        response.flash4 = 'widgetsform4' 



    widgetsform5 = SQLFORM(db.dwidgetsform5, _class = 'classUnk5', _id= 'idUnk5' )

    widgetsform5.element('input[name=f0]')['_placeholder']='f0 Press enter to post comment'
    widgetsform5.element('input[name=f0]')['_id']='id_for82'
    widgetsform5.element('input[name=f0]')['_class']='form-control form-control-sm'

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



    widgetsform6 = SQLFORM(db.dwidgetsform6, _class = 'classUnk6', _id= 'idUnk6' )

    widgetsform6.element('input[name=f0]')['_placeholder']='f0 Press enter to post comment'
    widgetsform6.element('input[name=f0]')['_id']='id_for84'
    widgetsform6.element('input[name=f0]')['_class']='form-control form-control-sm'

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


    return dict( DICT= rows_dict, widgetsform0= widgetsform0, widgetsform1= widgetsform1, widgetsform2= widgetsform2, widgetsform3= widgetsform3, widgetsform4= widgetsform4, widgetsform5= widgetsform5, widgetsform6= widgetsform6, )

#@auth.requires_login()
def projects():

    qu= db.dprojects.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/projects.html'


    projectsform0 = SQLFORM(db.dprojectsform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    projectsform0.element('input[name=f0]')['_placeholder']='f0 Search'
    projectsform0.element('input[name=f0]')['_id']='id_for431'
    projectsform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    projectsform0.custom.submit['_type'] = 'submit'
    projectsform0.custom.submit['_id'] = 'id_for433'
    projectsform0.custom.submit['_value'] = 'unk_435'
    projectsform0.custom.submit['_class'] = 'btn btn-navbar'
    projectsform0.custom.submit['_title'] = 'submit projectsform0'

    if projectsform0.accepts(request,session): 
        response.flash0 = 'submitted projectsform0' 
    elif projectsform0.errors:
        response.flash0 = '!Errors! projectsform0' 
    else: 
        response.flash0 = 'projectsform0' 


    return dict( DICT= rows_dict, projectsform0= projectsform0, )

#@auth.requires_login()
def languageIImenu():

    qu= db.dlanguage0menu.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/language-menu.html'


    languageIImenuform0 = SQLFORM(db.dlanguageIImenuform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    languageIImenuform0.element('input[name=f0]')['_placeholder']='f0 Search'
    languageIImenuform0.element('input[name=f0]')['_id']='id_for290'
    languageIImenuform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    languageIImenuform0.custom.submit['_type'] = 'submit'
    languageIImenuform0.custom.submit['_id'] = 'id_for292'
    languageIImenuform0.custom.submit['_value'] = 'unk_294'
    languageIImenuform0.custom.submit['_class'] = 'btn btn-navbar'
    languageIImenuform0.custom.submit['_title'] = 'submit languageIImenuform0'

    if languageIImenuform0.accepts(request,session): 
        response.flash0 = 'submitted languageIImenuform0' 
    elif languageIImenuform0.errors:
        response.flash0 = '!Errors! languageIImenuform0' 
    else: 
        response.flash0 = 'languageIImenuform0' 


    return dict( DICT= rows_dict, languageIImenuform0= languageIImenuform0, )

#@auth.requires_login()
def sliders():

    qu= db.dsliders.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/sliders.html'


    slidersform0 = SQLFORM(db.dslidersform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    slidersform0.element('input[name=f0]')['_placeholder']='f0 Search'
    slidersform0.element('input[name=f0]')['_id']='id_for302'
    slidersform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    slidersform0.custom.submit['_type'] = 'submit'
    slidersform0.custom.submit['_id'] = 'id_for304'
    slidersform0.custom.submit['_value'] = 'unk_306'
    slidersform0.custom.submit['_class'] = 'btn btn-navbar'
    slidersform0.custom.submit['_title'] = 'submit slidersform0'

    if slidersform0.accepts(request,session): 
        response.flash0 = 'submitted slidersform0' 
    elif slidersform0.errors:
        response.flash0 = '!Errors! slidersform0' 
    else: 
        response.flash0 = 'slidersform0' 


    return dict( DICT= rows_dict, slidersform0= slidersform0, )

#@auth.requires_login()
def register():

    qu= db.dregister.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/register.html'


    registerform0 = SQLFORM(db.dregisterform0, _class = 'classUnk0', _id= 'idUnk0' )

    registerform0.element('input[name=f0]')['_placeholder']='f0 Full name'
    registerform0.element('input[name=f0]')['_id']='id_for104'
    registerform0.element('input[name=f0]')['_class']='form-control'
    registerform0.element('input[name=f1]')['_placeholder']='f1 Email'
    registerform0.element('input[name=f1]')['_id']='id_for106'
    registerform0.element('input[name=f1]')['_class']='form-control'
    registerform0.element('input[name=f2]')['_placeholder']='f2 Password'
    registerform0.element('input[name=f2]')['_id']='id_for108'
    registerform0.element('input[name=f2]')['_class']='form-control'
    registerform0.element('input[name=f3]')['_placeholder']='f3 Retype password'
    registerform0.element('input[name=f3]')['_id']='id_for110'
    registerform0.element('input[name=f3]')['_class']='form-control'
    registerform0.element('input[name=f4]')['_placeholder']='f4 place_114'
    registerform0.element('input[name=f4]')['_id']='agreeTerms'
    registerform0.element('input[name=f4]')['_value']='agree'

    registerform0.custom.submit['_type'] = 'submit'
    registerform0.custom.submit['_id'] = 'id_for115'
    registerform0.custom.submit['_value'] = 'Register'
    registerform0.custom.submit['_class'] = 'btn btn-primary btn-block'
    registerform0.custom.submit['_title'] = 'submit registerform0'

    registerform0.custom.submit['_id'] = 'id_for118'
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


    modalsform0 = SQLFORM(db.dmodalsform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    modalsform0.element('input[name=f0]')['_placeholder']='f0 Search'
    modalsform0.element('input[name=f0]')['_id']='id_for155'
    modalsform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    modalsform0.custom.submit['_type'] = 'submit'
    modalsform0.custom.submit['_id'] = 'id_for157'
    modalsform0.custom.submit['_value'] = 'unk_159'
    modalsform0.custom.submit['_class'] = 'btn btn-navbar'
    modalsform0.custom.submit['_title'] = 'submit modalsform0'

    if modalsform0.accepts(request,session): 
        response.flash0 = 'submitted modalsform0' 
    elif modalsform0.errors:
        response.flash0 = '!Errors! modalsform0' 
    else: 
        response.flash0 = 'modalsform0' 


    return dict( DICT= rows_dict, modalsform0= modalsform0, )

#@auth.requires_login()
def timeline():

    qu= db.dtimeline.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/timeline.html'


    timelineform0 = SQLFORM(db.dtimelineform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    timelineform0.element('input[name=f0]')['_placeholder']='f0 Search'
    timelineform0.element('input[name=f0]')['_id']='id_for326'
    timelineform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    timelineform0.custom.submit['_type'] = 'submit'
    timelineform0.custom.submit['_id'] = 'id_for328'
    timelineform0.custom.submit['_value'] = 'unk_330'
    timelineform0.custom.submit['_class'] = 'btn btn-navbar'
    timelineform0.custom.submit['_title'] = 'submit timelineform0'

    if timelineform0.accepts(request,session): 
        response.flash0 = 'submitted timelineform0' 
    elif timelineform0.errors:
        response.flash0 = '!Errors! timelineform0' 
    else: 
        response.flash0 = 'timelineform0' 


    return dict( DICT= rows_dict, timelineform0= timelineform0, )

#@auth.requires_login()
def index2():

    qu= db.dindex2.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index2.html'


    index2form0 = SQLFORM(db.dindex2form0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    index2form0.element('input[name=f0]')['_placeholder']='f0 Search'
    index2form0.element('input[name=f0]')['_id']='id_for360'
    index2form0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    index2form0.custom.submit['_type'] = 'submit'
    index2form0.custom.submit['_id'] = 'id_for362'
    index2form0.custom.submit['_value'] = 'unk_364'
    index2form0.custom.submit['_class'] = 'btn btn-navbar'
    index2form0.custom.submit['_title'] = 'submit index2form0'

    if index2form0.accepts(request,session): 
        response.flash0 = 'submitted index2form0' 
    elif index2form0.errors:
        response.flash0 = '!Errors! index2form0' 
    else: 
        response.flash0 = 'index2form0' 



    index2form1 = SQLFORM(db.dindex2form1, _class = 'classUnk1', _id= 'idUnk1' )

    index2form1.element('input[name=f0]')['_placeholder']='f0 Type Message ...'
    index2form1.element('input[name=f0]')['_id']='id_for366'
    index2form1.element('input[name=f0]')['_class']='form-control'

    index2form1.custom.submit['_type'] = 'submit'
    index2form1.custom.submit['_id'] = 'id_for368'
    index2form1.custom.submit['_value'] = 'Send'
    index2form1.custom.submit['_class'] = 'btn btn-warning'
    index2form1.custom.submit['_title'] = 'submit index2form1'

    if index2form1.accepts(request,session): 
        response.flash1 = 'submitted index2form1' 
    elif index2form1.errors:
        response.flash1 = '!Errors! index2form1' 
    else: 
        response.flash1 = 'index2form1' 


    return dict( DICT= rows_dict, index2form0= index2form0, index2form1= index2form1, )

#@auth.requires_login()
def eIIcommerce():

    qu= db.de0commerce.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/e_commerce.html'


    eIIcommerceform0 = SQLFORM(db.deIIcommerceform0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    eIIcommerceform0.element('input[name=f0]')['_placeholder']='f0 Search'
    eIIcommerceform0.element('input[name=f0]')['_id']='id_for377'
    eIIcommerceform0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    eIIcommerceform0.custom.submit['_type'] = 'submit'
    eIIcommerceform0.custom.submit['_id'] = 'id_for379'
    eIIcommerceform0.custom.submit['_value'] = 'unk_381'
    eIIcommerceform0.custom.submit['_class'] = 'btn btn-navbar'
    eIIcommerceform0.custom.submit['_title'] = 'submit eIIcommerceform0'

    if eIIcommerceform0.accepts(request,session): 
        response.flash0 = 'submitted eIIcommerceform0' 
    elif eIIcommerceform0.errors:
        response.flash0 = '!Errors! eIIcommerceform0' 
    else: 
        response.flash0 = 'eIIcommerceform0' 


    return dict( DICT= rows_dict, eIIcommerceform0= eIIcommerceform0, )

#@auth.requires_login()
def X500():

    qu= db.d500.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/500.html'


    X500form0 = SQLFORM(db.dX500form0, _class = 'form-inline ml-3', _id= 'idUnk0' )

    X500form0.element('input[name=f0]')['_placeholder']='f0 Search'
    X500form0.element('input[name=f0]')['_id']='id_for437'
    X500form0.element('input[name=f0]')['_class']='form-control form-control-navbar'

    X500form0.custom.submit['_type'] = 'submit'
    X500form0.custom.submit['_id'] = 'id_for439'
    X500form0.custom.submit['_value'] = 'unk_441'
    X500form0.custom.submit['_class'] = 'btn btn-navbar'
    X500form0.custom.submit['_title'] = 'submit X500form0'

    if X500form0.accepts(request,session): 
        response.flash0 = 'submitted X500form0' 
    elif X500form0.errors:
        response.flash0 = '!Errors! X500form0' 
    else: 
        response.flash0 = 'X500form0' 



    X500form1 = SQLFORM(db.dX500form1, _class = 'search-form', _id= 'idUnk1' )

    X500form1.element('input[name=f0]')['_placeholder']='f0 Search'
    X500form1.element('input[name=f0]')['_id']='id_for443'
    X500form1.element('input[name=f0]')['_class']='form-control'

    X500form1.custom.submit['_type'] = 'submit'
    X500form1.custom.submit['_id'] = 'id_for445'
    X500form1.custom.submit['_value'] = 'unk_447'
    X500form1.custom.submit['_class'] = 'btn btn-danger'
    X500form1.custom.submit['_title'] = 'submit X500form1'

    if X500form1.accepts(request,session): 
        response.flash1 = 'submitted X500form1' 
    elif X500form1.errors:
        response.flash1 = '!Errors! X500form1' 
    else: 
        response.flash1 = 'X500form1' 


    return dict( DICT= rows_dict, X500form0= X500form0, X500form1= X500form1, )