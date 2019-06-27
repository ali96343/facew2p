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
def emailIInavbar():

    qu= db.demail0navbar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/email-navbar.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def wysiwyg():

    qu= db.dwysiwyg.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/wysiwyg.html'


    wysiwygform0 = SQLFORM(db.dwysiwygform0, _class = 'form-search', _id= 'idUnk0' )

    wysiwygform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    wysiwygform0.element('input[name=f0]')['_id']='nav-search-input'
    wysiwygform0.element('input[name=f0]')['_class']='nav-search-input'

    wysiwygform0.custom.submit['_type'] = 'submit'
    wysiwygform0.custom.submit['_id'] = 'unk-id'
    wysiwygform0.custom.submit['_value'] = 'submit input'
    wysiwygform0.custom.submit['_class'] = 'unk-class'
    wysiwygform0.custom.submit['_title'] = 'submit wysiwygform0'

    if wysiwygform0.accepts(request,session): 
        response.flash0 = 'submitted wysiwygform0' 
    elif wysiwygform0.errors:
        response.flash0 = '!Errors! wysiwygform0' 
    else: 
        response.flash0 = 'wysiwygform0' 


    return dict( DICT= rows_dict, wysiwygform0= wysiwygform0, )

#@auth.requires_login()
def widgets():

    qu= db.dwidgets.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/widgets.html'


    widgetsform0 = SQLFORM(db.dwidgetsform0, _class = 'form-search', _id= 'idUnk0' )

    widgetsform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    widgetsform0.element('input[name=f0]')['_id']='nav-search-input'
    widgetsform0.element('input[name=f0]')['_class']='nav-search-input'

    widgetsform0.custom.submit['_type'] = 'submit'
    widgetsform0.custom.submit['_id'] = 'unk-id'
    widgetsform0.custom.submit['_value'] = 'submit input'
    widgetsform0.custom.submit['_class'] = 'unk-class'
    widgetsform0.custom.submit['_title'] = 'submit widgetsform0'

    if widgetsform0.accepts(request,session): 
        response.flash0 = 'submitted widgetsform0' 
    elif widgetsform0.errors:
        response.flash0 = '!Errors! widgetsform0' 
    else: 
        response.flash0 = 'widgetsform0' 


    return dict( DICT= rows_dict, widgetsform0= widgetsform0, )

#@auth.requires_login()
def email():

    qu= db.demail.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/email.html'


    emailform0 = SQLFORM(db.demailform0, _class = 'form-search', _id= 'idUnk0' )

    emailform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    emailform0.element('input[name=f0]')['_id']='nav-search-input'
    emailform0.element('input[name=f0]')['_class']='nav-search-input'

    emailform0.custom.submit['_type'] = 'submit'
    emailform0.custom.submit['_id'] = 'unk-id'
    emailform0.custom.submit['_value'] = 'submit input'
    emailform0.custom.submit['_class'] = 'unk-class'
    emailform0.custom.submit['_title'] = 'submit emailform0'

    if emailform0.accepts(request,session): 
        response.flash0 = 'submitted emailform0' 
    elif emailform0.errors:
        response.flash0 = '!Errors! emailform0' 
    else: 
        response.flash0 = 'emailform0' 


    return dict( DICT= rows_dict, emailform0= emailform0, )

#@auth.requires_login()
def mobileIImenuII2():

    qu= db.dmobile0menu02.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/mobile-menu-2.html'


    mobileIImenuII2form0 = SQLFORM(db.dmobileIImenuII2form0, _class = 'form-search', _id= 'idUnk0' )

    mobileIImenuII2form0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    mobileIImenuII2form0.element('input[name=f0]')['_id']='nav-search-input'
    mobileIImenuII2form0.element('input[name=f0]')['_class']='nav-search-input'

    mobileIImenuII2form0.custom.submit['_type'] = 'submit'
    mobileIImenuII2form0.custom.submit['_id'] = 'unk-id'
    mobileIImenuII2form0.custom.submit['_value'] = 'submit input'
    mobileIImenuII2form0.custom.submit['_class'] = 'unk-class'
    mobileIImenuII2form0.custom.submit['_title'] = 'submit mobileIImenuII2form0'

    if mobileIImenuII2form0.accepts(request,session): 
        response.flash0 = 'submitted mobileIImenuII2form0' 
    elif mobileIImenuII2form0.errors:
        response.flash0 = '!Errors! mobileIImenuII2form0' 
    else: 
        response.flash0 = 'mobileIImenuII2form0' 


    return dict( DICT= rows_dict, mobileIImenuII2form0= mobileIImenuII2form0, )

#@auth.requires_login()
def treeview():

    qu= db.dtreeview.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/treeview.html'


    treeviewform0 = SQLFORM(db.dtreeviewform0, _class = 'form-search', _id= 'idUnk0' )

    treeviewform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    treeviewform0.element('input[name=f0]')['_id']='nav-search-input'
    treeviewform0.element('input[name=f0]')['_class']='nav-search-input'

    treeviewform0.custom.submit['_type'] = 'submit'
    treeviewform0.custom.submit['_id'] = 'unk-id'
    treeviewform0.custom.submit['_value'] = 'submit input'
    treeviewform0.custom.submit['_class'] = 'unk-class'
    treeviewform0.custom.submit['_title'] = 'submit treeviewform0'

    if treeviewform0.accepts(request,session): 
        response.flash0 = 'submitted treeviewform0' 
    elif treeviewform0.errors:
        response.flash0 = '!Errors! treeviewform0' 
    else: 
        response.flash0 = 'treeviewform0' 


    return dict( DICT= rows_dict, treeviewform0= treeviewform0, )

#@auth.requires_login()
def tables():

    qu= db.dtables.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/tables.html'


    tablesform0 = SQLFORM(db.dtablesform0, _class = 'form-search', _id= 'idUnk0' )

    tablesform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    tablesform0.element('input[name=f0]')['_id']='nav-search-input'
    tablesform0.element('input[name=f0]')['_class']='nav-search-input'

    tablesform0.custom.submit['_type'] = 'submit'
    tablesform0.custom.submit['_id'] = 'unk-id'
    tablesform0.custom.submit['_value'] = 'submit input'
    tablesform0.custom.submit['_class'] = 'unk-class'
    tablesform0.custom.submit['_title'] = 'submit tablesform0'

    if tablesform0.accepts(request,session): 
        response.flash0 = 'submitted tablesform0' 
    elif tablesform0.errors:
        response.flash0 = '!Errors! tablesform0' 
    else: 
        response.flash0 = 'tablesform0' 



    tablesform1 = SQLFORM(db.dtablesform1, _class = 'classUnk1', _id= 'idUnk1' )

    tablesform1.element('input[name=f0]')['_placeholder']='f0 place_130'
    tablesform1.element('input[name=f0]')['_id']='id_for127'
    tablesform1.element('input[name=f0]')['_class']='ace'
    tablesform1.element('textarea[name=f1]')['_placeholder']='f1 Type something'
    tablesform1.element('textarea[name=f1]')['_id']='id_for131'
    tablesform1.element('textarea[name=f1]')['_class']='width-100'

    tablesform1.custom.submit['_type'] = 'submit'
    tablesform1.custom.submit['_id'] = 'id_for134'
    tablesform1.custom.submit['_value'] = 'Submit'
    tablesform1.custom.submit['_class'] = 'pull-right btn btn-sm btn-primary btn-white btn-round'
    tablesform1.custom.submit['_title'] = 'submit tablesform1'

    if tablesform1.accepts(request,session): 
        response.flash1 = 'submitted tablesform1' 
    elif tablesform1.errors:
        response.flash1 = '!Errors! tablesform1' 
    else: 
        response.flash1 = 'tablesform1' 



    tablesform2 = SQLFORM(db.dtablesform2, _class = 'classUnk2', _id= 'idUnk2' )

    tablesform2.element('input[name=f0]')['_placeholder']='f0 place_141'
    tablesform2.element('input[name=f0]')['_id']='id_for138'
    tablesform2.element('input[name=f0]')['_class']='ace'
    tablesform2.element('textarea[name=f1]')['_placeholder']='f1 Type something'
    tablesform2.element('textarea[name=f1]')['_id']='id_for142'
    tablesform2.element('textarea[name=f1]')['_class']='width-100'

    tablesform2.custom.submit['_type'] = 'submit'
    tablesform2.custom.submit['_id'] = 'id_for145'
    tablesform2.custom.submit['_value'] = 'Submit'
    tablesform2.custom.submit['_class'] = 'pull-right btn btn-sm btn-primary btn-white btn-round'
    tablesform2.custom.submit['_title'] = 'submit tablesform2'

    if tablesform2.accepts(request,session): 
        response.flash2 = 'submitted tablesform2' 
    elif tablesform2.errors:
        response.flash2 = '!Errors! tablesform2' 
    else: 
        response.flash2 = 'tablesform2' 



    tablesform3 = SQLFORM(db.dtablesform3, _class = 'classUnk3', _id= 'idUnk3' )

    tablesform3.element('input[name=f0]')['_placeholder']='f0 place_152'
    tablesform3.element('input[name=f0]')['_id']='id_for149'
    tablesform3.element('input[name=f0]')['_class']='ace'
    tablesform3.element('textarea[name=f1]')['_placeholder']='f1 Type something'
    tablesform3.element('textarea[name=f1]')['_id']='id_for153'
    tablesform3.element('textarea[name=f1]')['_class']='width-100'

    tablesform3.custom.submit['_type'] = 'submit'
    tablesform3.custom.submit['_id'] = 'id_for156'
    tablesform3.custom.submit['_value'] = 'Submit'
    tablesform3.custom.submit['_class'] = 'pull-right btn btn-sm btn-primary btn-white btn-round'
    tablesform3.custom.submit['_title'] = 'submit tablesform3'

    if tablesform3.accepts(request,session): 
        response.flash3 = 'submitted tablesform3' 
    elif tablesform3.errors:
        response.flash3 = '!Errors! tablesform3' 
    else: 
        response.flash3 = 'tablesform3' 



    tablesform4 = SQLFORM(db.dtablesform4, _class = 'classUnk4', _id= 'idUnk4' )

    tablesform4.element('input[name=f0]')['_placeholder']='f0 place_163'
    tablesform4.element('input[name=f0]')['_id']='id_for160'
    tablesform4.element('input[name=f0]')['_class']='ace'
    tablesform4.element('textarea[name=f1]')['_placeholder']='f1 Type something'
    tablesform4.element('textarea[name=f1]')['_id']='id_for164'
    tablesform4.element('textarea[name=f1]')['_class']='width-100'

    tablesform4.custom.submit['_type'] = 'submit'
    tablesform4.custom.submit['_id'] = 'id_for167'
    tablesform4.custom.submit['_value'] = 'Submit'
    tablesform4.custom.submit['_class'] = 'pull-right btn btn-sm btn-primary btn-white btn-round'
    tablesform4.custom.submit['_title'] = 'submit tablesform4'

    if tablesform4.accepts(request,session): 
        response.flash4 = 'submitted tablesform4' 
    elif tablesform4.errors:
        response.flash4 = '!Errors! tablesform4' 
    else: 
        response.flash4 = 'tablesform4' 



    tablesform5 = SQLFORM(db.dtablesform5, _class = 'classUnk5', _id= 'idUnk5' )

    tablesform5.element('input[name=f0]')['_placeholder']='f0 place_174'
    tablesform5.element('input[name=f0]')['_id']='id_for171'
    tablesform5.element('input[name=f0]')['_class']='ace'
    tablesform5.element('textarea[name=f1]')['_placeholder']='f1 Type something'
    tablesform5.element('textarea[name=f1]')['_id']='id_for175'
    tablesform5.element('textarea[name=f1]')['_class']='width-100'

    tablesform5.custom.submit['_type'] = 'submit'
    tablesform5.custom.submit['_id'] = 'id_for178'
    tablesform5.custom.submit['_value'] = 'Submit'
    tablesform5.custom.submit['_class'] = 'pull-right btn btn-sm btn-primary btn-white btn-round'
    tablesform5.custom.submit['_title'] = 'submit tablesform5'

    if tablesform5.accepts(request,session): 
        response.flash5 = 'submitted tablesform5' 
    elif tablesform5.errors:
        response.flash5 = '!Errors! tablesform5' 
    else: 
        response.flash5 = 'tablesform5' 


    return dict( DICT= rows_dict, tablesform0= tablesform0, tablesform1= tablesform1, tablesform2= tablesform2, tablesform3= tablesform3, tablesform4= tablesform4, tablesform5= tablesform5, )

#@auth.requires_login()
def errorII500():

    qu= db.derror0500.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/error-500.html'


    errorII500form0 = SQLFORM(db.derrorII500form0, _class = 'form-search', _id= 'idUnk0' )

    errorII500form0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    errorII500form0.element('input[name=f0]')['_id']='nav-search-input'
    errorII500form0.element('input[name=f0]')['_class']='nav-search-input'

    errorII500form0.custom.submit['_type'] = 'submit'
    errorII500form0.custom.submit['_id'] = 'unk-id'
    errorII500form0.custom.submit['_value'] = 'submit input'
    errorII500form0.custom.submit['_class'] = 'unk-class'
    errorII500form0.custom.submit['_title'] = 'submit errorII500form0'

    if errorII500form0.accepts(request,session): 
        response.flash0 = 'submitted errorII500form0' 
    elif errorII500form0.errors:
        response.flash0 = '!Errors! errorII500form0' 
    else: 
        response.flash0 = 'errorII500form0' 


    return dict( DICT= rows_dict, errorII500form0= errorII500form0, )

#@auth.requires_login()
def index():

    qu= db.dindex.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index.html'


    indexform0 = SQLFORM(db.dindexform0, _class = 'form-search', _id= 'idUnk0' )

    indexform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    indexform0.element('input[name=f0]')['_id']='nav-search-input'
    indexform0.element('input[name=f0]')['_class']='nav-search-input'

    indexform0.custom.submit['_type'] = 'submit'
    indexform0.custom.submit['_id'] = 'unk-id'
    indexform0.custom.submit['_value'] = 'submit input'
    indexform0.custom.submit['_class'] = 'unk-class'
    indexform0.custom.submit['_title'] = 'submit indexform0'

    if indexform0.accepts(request,session): 
        response.flash0 = 'submitted indexform0' 
    elif indexform0.errors:
        response.flash0 = '!Errors! indexform0' 
    else: 
        response.flash0 = 'indexform0' 



    indexform1 = SQLFORM(db.dindexform1, _class = 'classUnk1', _id= 'idUnk1' )

    indexform1.element('input[name=f0]')['_placeholder']='f0 Type your message here ...'
    indexform1.element('input[name=f0]')['_id']='id_for785'
    indexform1.element('input[name=f0]')['_class']='form-control'

    indexform1.custom.submit['_type'] = 'submit'
    indexform1.custom.submit['_id'] = 'id_for787'
    indexform1.custom.submit['_value'] = 'Send'
    indexform1.custom.submit['_class'] = 'btn btn-sm btn-info no-radius'
    indexform1.custom.submit['_title'] = 'submit indexform1'

    if indexform1.accepts(request,session): 
        response.flash1 = 'submitted indexform1' 
    elif indexform1.errors:
        response.flash1 = '!Errors! indexform1' 
    else: 
        response.flash1 = 'indexform1' 


    return dict( DICT= rows_dict, indexform0= indexform0, indexform1= indexform1, )

#@auth.requires_login()
def formIIelementsII2():

    qu= db.dform0elements02.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/form-elements-2.html'


    formIIelementsII2form0 = SQLFORM(db.dformIIelementsII2form0, _class = 'form-search', _id= 'idUnk0' )

    formIIelementsII2form0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    formIIelementsII2form0.element('input[name=f0]')['_id']='nav-search-input'
    formIIelementsII2form0.element('input[name=f0]')['_class']='nav-search-input'

    formIIelementsII2form0.custom.submit['_type'] = 'submit'
    formIIelementsII2form0.custom.submit['_id'] = 'unk-id'
    formIIelementsII2form0.custom.submit['_value'] = 'submit input'
    formIIelementsII2form0.custom.submit['_class'] = 'unk-class'
    formIIelementsII2form0.custom.submit['_title'] = 'submit formIIelementsII2form0'

    if formIIelementsII2form0.accepts(request,session): 
        response.flash0 = 'submitted formIIelementsII2form0' 
    elif formIIelementsII2form0.errors:
        response.flash0 = '!Errors! formIIelementsII2form0' 
    else: 
        response.flash0 = 'formIIelementsII2form0' 



    formIIelementsII2form1 = SQLFORM(db.dformIIelementsII2form1, _class = 'form-horizontal', _id= 'idUnk1' )

    formIIelementsII2form1.element('input[name=f0]')['_placeholder']='f0 States of USA'
    formIIelementsII2form1.element('input[name=f0]')['_id']='id_for754'
    formIIelementsII2form1.element('input[name=f0]')['_class']='typeahead scrollable'

    formIIelementsII2form1.custom.submit['_type'] = 'submit'
    formIIelementsII2form1.custom.submit['_id'] = 'unk-id'
    formIIelementsII2form1.custom.submit['_value'] = 'submit input'
    formIIelementsII2form1.custom.submit['_class'] = 'unk-class'
    formIIelementsII2form1.custom.submit['_title'] = 'submit formIIelementsII2form1'

    if formIIelementsII2form1.accepts(request,session): 
        response.flash1 = 'submitted formIIelementsII2form1' 
    elif formIIelementsII2form1.errors:
        response.flash1 = '!Errors! formIIelementsII2form1' 
    else: 
        response.flash1 = 'formIIelementsII2form1' 


    return dict( DICT= rows_dict, formIIelementsII2form0= formIIelementsII2form0, formIIelementsII2form1= formIIelementsII2form1, )

#@auth.requires_login()
def buttons():

    qu= db.dbuttons.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/buttons.html'


    buttonsform0 = SQLFORM(db.dbuttonsform0, _class = 'form-search', _id= 'idUnk0' )

    buttonsform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    buttonsform0.element('input[name=f0]')['_id']='nav-search-input'
    buttonsform0.element('input[name=f0]')['_class']='nav-search-input'

    buttonsform0.custom.submit['_type'] = 'submit'
    buttonsform0.custom.submit['_id'] = 'unk-id'
    buttonsform0.custom.submit['_value'] = 'submit input'
    buttonsform0.custom.submit['_class'] = 'unk-class'
    buttonsform0.custom.submit['_title'] = 'submit buttonsform0'

    if buttonsform0.accepts(request,session): 
        response.flash0 = 'submitted buttonsform0' 
    elif buttonsform0.errors:
        response.flash0 = '!Errors! buttonsform0' 
    else: 
        response.flash0 = 'buttonsform0' 


    return dict( DICT= rows_dict, buttonsform0= buttonsform0, )

#@auth.requires_login()
def gallery():

    qu= db.dgallery.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/gallery.html'


    galleryform0 = SQLFORM(db.dgalleryform0, _class = 'form-search', _id= 'idUnk0' )

    galleryform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    galleryform0.element('input[name=f0]')['_id']='nav-search-input'
    galleryform0.element('input[name=f0]')['_class']='nav-search-input'

    galleryform0.custom.submit['_type'] = 'submit'
    galleryform0.custom.submit['_id'] = 'unk-id'
    galleryform0.custom.submit['_value'] = 'submit input'
    galleryform0.custom.submit['_class'] = 'unk-class'
    galleryform0.custom.submit['_title'] = 'submit galleryform0'

    if galleryform0.accepts(request,session): 
        response.flash0 = 'submitted galleryform0' 
    elif galleryform0.errors:
        response.flash0 = '!Errors! galleryform0' 
    else: 
        response.flash0 = 'galleryform0' 


    return dict( DICT= rows_dict, galleryform0= galleryform0, )

#@auth.requires_login()
def mobileIImenuII3():

    qu= db.dmobile0menu03.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/mobile-menu-3.html'


    mobileIImenuII3form0 = SQLFORM(db.dmobileIImenuII3form0, _class = 'form-search', _id= 'idUnk0' )

    mobileIImenuII3form0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    mobileIImenuII3form0.element('input[name=f0]')['_id']='nav-search-input'
    mobileIImenuII3form0.element('input[name=f0]')['_class']='nav-search-input'

    mobileIImenuII3form0.custom.submit['_type'] = 'submit'
    mobileIImenuII3form0.custom.submit['_id'] = 'unk-id'
    mobileIImenuII3form0.custom.submit['_value'] = 'submit input'
    mobileIImenuII3form0.custom.submit['_class'] = 'unk-class'
    mobileIImenuII3form0.custom.submit['_title'] = 'submit mobileIImenuII3form0'

    if mobileIImenuII3form0.accepts(request,session): 
        response.flash0 = 'submitted mobileIImenuII3form0' 
    elif mobileIImenuII3form0.errors:
        response.flash0 = '!Errors! mobileIImenuII3form0' 
    else: 
        response.flash0 = 'mobileIImenuII3form0' 


    return dict( DICT= rows_dict, mobileIImenuII3form0= mobileIImenuII3form0, )

#@auth.requires_login()
def emailIIcontrast():

    qu= db.demail0contrast.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/email-contrast.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def calendar():

    qu= db.dcalendar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/calendar.html'


    calendarform0 = SQLFORM(db.dcalendarform0, _class = 'form-search', _id= 'idUnk0' )

    calendarform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    calendarform0.element('input[name=f0]')['_id']='nav-search-input'
    calendarform0.element('input[name=f0]')['_class']='nav-search-input'

    calendarform0.custom.submit['_type'] = 'submit'
    calendarform0.custom.submit['_id'] = 'unk-id'
    calendarform0.custom.submit['_value'] = 'submit input'
    calendarform0.custom.submit['_class'] = 'unk-class'
    calendarform0.custom.submit['_title'] = 'submit calendarform0'

    if calendarform0.accepts(request,session): 
        response.flash0 = 'submitted calendarform0' 
    elif calendarform0.errors:
        response.flash0 = '!Errors! calendarform0' 
    else: 
        response.flash0 = 'calendarform0' 


    return dict( DICT= rows_dict, calendarform0= calendarform0, )

#@auth.requires_login()
def login():

    qu= db.dlogin.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/login.html'


    loginform0 = SQLFORM(db.dloginform0, _class = 'classUnk0', _id= 'idUnk0' )

    loginform0.element('input[name=f0]')['_placeholder']='f0 Username'
    loginform0.element('input[name=f0]')['_id']='id_for184'
    loginform0.element('input[name=f0]')['_class']='form-control'
    loginform0.element('input[name=f1]')['_placeholder']='f1 Password'
    loginform0.element('input[name=f1]')['_id']='id_for186'
    loginform0.element('input[name=f1]')['_class']='form-control'
    loginform0.element('input[name=f2]')['_placeholder']='f2 place_191'
    loginform0.element('input[name=f2]')['_id']='id_for188'
    loginform0.element('input[name=f2]')['_class']='ace'

    loginform0.custom.submit['_type'] = 'submit'
    loginform0.custom.submit['_id'] = 'id_for192'
    loginform0.custom.submit['_value'] = 'Login'
    loginform0.custom.submit['_class'] = 'width-35 pull-right btn btn-sm btn-primary'
    loginform0.custom.submit['_title'] = 'submit loginform0'

    if loginform0.accepts(request,session): 
        response.flash0 = 'submitted loginform0' 
    elif loginform0.errors:
        response.flash0 = '!Errors! loginform0' 
    else: 
        response.flash0 = 'loginform0' 



    loginform1 = SQLFORM(db.dloginform1, _class = 'classUnk1', _id= 'idUnk1' )

    loginform1.element('input[name=f0]')['_placeholder']='f0 Email'
    loginform1.element('input[name=f0]')['_id']='id_for196'
    loginform1.element('input[name=f0]')['_class']='form-control'

    loginform1.custom.submit['_type'] = 'submit'
    loginform1.custom.submit['_id'] = 'id_for198'
    loginform1.custom.submit['_value'] = 'Send Me!'
    loginform1.custom.submit['_class'] = 'width-35 pull-right btn btn-sm btn-danger'
    loginform1.custom.submit['_title'] = 'submit loginform1'

    if loginform1.accepts(request,session): 
        response.flash1 = 'submitted loginform1' 
    elif loginform1.errors:
        response.flash1 = '!Errors! loginform1' 
    else: 
        response.flash1 = 'loginform1' 



    loginform2 = SQLFORM(db.dloginform2, _class = 'classUnk2', _id= 'idUnk2' )

    loginform2.element('input[name=f0]')['_placeholder']='f0 Email'
    loginform2.element('input[name=f0]')['_id']='id_for203'
    loginform2.element('input[name=f0]')['_class']='form-control'
    loginform2.element('input[name=f1]')['_placeholder']='f1 Username'
    loginform2.element('input[name=f1]')['_id']='id_for205'
    loginform2.element('input[name=f1]')['_class']='form-control'
    loginform2.element('input[name=f2]')['_placeholder']='f2 Password'
    loginform2.element('input[name=f2]')['_id']='id_for207'
    loginform2.element('input[name=f2]')['_class']='form-control'
    loginform2.element('input[name=f3]')['_placeholder']='f3 Repeat password'
    loginform2.element('input[name=f3]')['_id']='id_for209'
    loginform2.element('input[name=f3]')['_class']='form-control'
    loginform2.element('input[name=f4]')['_placeholder']='f4 place_215'
    loginform2.element('input[name=f4]')['_id']='id_for211'
    loginform2.element('input[name=f4]')['_class']='ace'

    loginform2.custom.submit['_type'] = 'submit'
    loginform2.custom.submit['_id'] = 'id_for216'
    loginform2.custom.submit['_value'] = 'Reset'
    loginform2.custom.submit['_class'] = 'width-30 pull-left btn btn-sm'
    loginform2.custom.submit['_title'] = 'submit loginform2'

    loginform2.custom.submit['_type'] = 'submit'
    loginform2.custom.submit['_id'] = 'id_for221'
    loginform2.custom.submit['_value'] = 'Register'
    loginform2.custom.submit['_class'] = 'width-65 pull-right btn btn-sm btn-success'
    loginform2.custom.submit['_title'] = 'submit loginform2'

    loginform2.custom.submit['_id'] = 'id_for226'
    loginform2.custom.submit['_title'] = 'submit loginform2'

    if loginform2.accepts(request,session): 
        response.flash2 = 'submitted loginform2' 
    elif loginform2.errors:
        response.flash2 = '!Errors! loginform2' 
    else: 
        response.flash2 = 'loginform2' 


    return dict( DICT= rows_dict, loginform0= loginform0, loginform1= loginform1, loginform2= loginform2, )

#@auth.requires_login()
def profile():

    qu= db.dprofile.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/profile.html'


    profileform0 = SQLFORM(db.dprofileform0, _class = 'form-search', _id= 'idUnk0' )

    profileform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    profileform0.element('input[name=f0]')['_id']='nav-search-input'
    profileform0.element('input[name=f0]')['_class']='nav-search-input'

    profileform0.custom.submit['_type'] = 'submit'
    profileform0.custom.submit['_id'] = 'unk-id'
    profileform0.custom.submit['_value'] = 'submit input'
    profileform0.custom.submit['_class'] = 'unk-class'
    profileform0.custom.submit['_title'] = 'submit profileform0'

    if profileform0.accepts(request,session): 
        response.flash0 = 'submitted profileform0' 
    elif profileform0.errors:
        response.flash0 = '!Errors! profileform0' 
    else: 
        response.flash0 = 'profileform0' 



    profileform1 = SQLFORM(db.dprofileform1, _class = 'form-horizontal', _id= 'idUnk1' )

    profileform1.element('input[name=f0]')['_placeholder']='f0 place_671'
    profileform1.element('input[name=f0]')['_id']='id_for669'
    profileform1.element('input[name=f1]')['_placeholder']='f1 Username'
    profileform1.element('input[name=f1]')['_id']='form-field-username'
    profileform1.element('input[name=f1]')['_value']='alexdoe'
    profileform1.element('input[name=f1]')['_class']='col-xs-12 col-sm-10'
    profileform1.element('input[name=f2]')['_placeholder']='f2 First Name'
    profileform1.element('input[name=f2]')['_id']='form-field-first'
    profileform1.element('input[name=f2]')['_value']='Alex'
    profileform1.element('input[name=f2]')['_class']='input-small'
    profileform1.element('input[name=f3]')['_placeholder']='f3 Last Name'
    profileform1.element('input[name=f3]')['_id']='form-field-last'
    profileform1.element('input[name=f3]')['_value']='Doe'
    profileform1.element('input[name=f3]')['_class']='input-small'
    profileform1.element('input[name=f4]')['_placeholder']='f4 dd-mm-yyyy'
    profileform1.element('input[name=f4]')['_id']='form-field-date'
    profileform1.element('input[name=f4]')['_class']='input-medium date-picker'
    profileform1.element('input[name=f5]')['_placeholder']='f5 place_688'
    profileform1.element('input[name=f5]')['_id']='form-field-email'
    profileform1.element('input[name=f5]')['_value']='alexdoe@gmail.com'
    profileform1.element('input[name=f6]')['_placeholder']='f6 place_691'
    profileform1.element('input[name=f6]')['_id']='form-field-website'
    profileform1.element('input[name=f6]')['_value']='http://www.alexdoe.com/'
    profileform1.element('input[name=f7]')['_placeholder']='f7 place_694'
    profileform1.element('input[name=f7]')['_id']='form-field-phone'
    profileform1.element('input[name=f7]')['_class']='input-medium input-mask-phone'
    profileform1.element('input[name=f8]')['_placeholder']='f8 place_697'
    profileform1.element('input[name=f8]')['_id']='form-field-facebook'
    profileform1.element('input[name=f8]')['_value']='facebook_alexdoe'
    profileform1.element('input[name=f9]')['_placeholder']='f9 place_700'
    profileform1.element('input[name=f9]')['_id']='form-field-twitter'
    profileform1.element('input[name=f9]')['_value']='twitter_alexdoe'
    profileform1.element('input[name=f10]')['_placeholder']='f10 place_703'
    profileform1.element('input[name=f10]')['_id']='form-field-gplus'
    profileform1.element('input[name=f10]')['_value']='google_alexdoe'
    profileform1.element('input[name=f11]')['_placeholder']='f11 place_707'
    profileform1.element('input[name=f11]')['_id']='id_for704'
    profileform1.element('input[name=f11]')['_class']='ace'
    profileform1.element('input[name=f12]')['_placeholder']='f12 place_711'
    profileform1.element('input[name=f12]')['_id']='id_for708'
    profileform1.element('input[name=f12]')['_class']='ace'
    profileform1.element('input[name=f13]')['_placeholder']='f13 place_715'
    profileform1.element('input[name=f13]')['_id']='id_for712'
    profileform1.element('input[name=f13]')['_class']='ace'
    profileform1.element('input[name=f14]')['_placeholder']='f14 place_719'
    profileform1.element('input[name=f14]')['_id']='id_for716'
    profileform1.element('input[name=f14]')['_class']='input-mini'
    profileform1.element('input[name=f15]')['_placeholder']='f15 place_722'
    profileform1.element('input[name=f15]')['_id']='form-field-pass1'
    profileform1.element('input[name=f16]')['_placeholder']='f16 place_725'
    profileform1.element('input[name=f16]')['_id']='form-field-pass2'
    profileform1.element('textarea[name=f17]')['_placeholder']='f17 place_728'
    profileform1.element('textarea[name=f17]')['_id']='form-field-comment'

    profileform1.custom.submit['_type'] = 'submit'
    profileform1.custom.submit['_id'] = 'id_for729'
    profileform1.custom.submit['_value'] = 'Save'
    profileform1.custom.submit['_class'] = 'btn btn-info'
    profileform1.custom.submit['_title'] = 'submit profileform1'

    profileform1.custom.submit['_type'] = 'submit'
    profileform1.custom.submit['_id'] = 'id_for732'
    profileform1.custom.submit['_value'] = 'Reset'
    profileform1.custom.submit['_class'] = 'btn'
    profileform1.custom.submit['_title'] = 'submit profileform1'

    profileform1.custom.submit['_id'] = 'id_for735'
    profileform1.custom.submit['_title'] = 'submit profileform1'

    profileform1.custom.submit['_id'] = 'id_for738'
    profileform1.custom.submit['_title'] = 'submit profileform1'

    profileform1.custom.submit['_id'] = 'id_for741'
    profileform1.custom.submit['_title'] = 'submit profileform1'

    if profileform1.accepts(request,session): 
        response.flash1 = 'submitted profileform1' 
    elif profileform1.errors:
        response.flash1 = '!Errors! profileform1' 
    else: 
        response.flash1 = 'profileform1' 


    return dict( DICT= rows_dict, profileform0= profileform0, profileform1= profileform1, )

#@auth.requires_login()
def invoice():

    qu= db.dinvoice.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/invoice.html'


    invoiceform0 = SQLFORM(db.dinvoiceform0, _class = 'form-search', _id= 'idUnk0' )

    invoiceform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    invoiceform0.element('input[name=f0]')['_id']='nav-search-input'
    invoiceform0.element('input[name=f0]')['_class']='nav-search-input'

    invoiceform0.custom.submit['_type'] = 'submit'
    invoiceform0.custom.submit['_id'] = 'unk-id'
    invoiceform0.custom.submit['_value'] = 'submit input'
    invoiceform0.custom.submit['_class'] = 'unk-class'
    invoiceform0.custom.submit['_title'] = 'submit invoiceform0'

    if invoiceform0.accepts(request,session): 
        response.flash0 = 'submitted invoiceform0' 
    elif invoiceform0.errors:
        response.flash0 = '!Errors! invoiceform0' 
    else: 
        response.flash0 = 'invoiceform0' 


    return dict( DICT= rows_dict, invoiceform0= invoiceform0, )

#@auth.requires_login()
def mobileIImenuII1():

    qu= db.dmobile0menu01.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/mobile-menu-1.html'


    mobileIImenuII1form0 = SQLFORM(db.dmobileIImenuII1form0, _class = 'form-search', _id= 'idUnk0' )

    mobileIImenuII1form0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    mobileIImenuII1form0.element('input[name=f0]')['_id']='nav-search-input'
    mobileIImenuII1form0.element('input[name=f0]')['_class']='nav-search-input'

    mobileIImenuII1form0.custom.submit['_type'] = 'submit'
    mobileIImenuII1form0.custom.submit['_id'] = 'unk-id'
    mobileIImenuII1form0.custom.submit['_value'] = 'submit input'
    mobileIImenuII1form0.custom.submit['_class'] = 'unk-class'
    mobileIImenuII1form0.custom.submit['_title'] = 'submit mobileIImenuII1form0'

    if mobileIImenuII1form0.accepts(request,session): 
        response.flash0 = 'submitted mobileIImenuII1form0' 
    elif mobileIImenuII1form0.errors:
        response.flash0 = '!Errors! mobileIImenuII1form0' 
    else: 
        response.flash0 = 'mobileIImenuII1form0' 


    return dict( DICT= rows_dict, mobileIImenuII1form0= mobileIImenuII1form0, )

#@auth.requires_login()
def emailIInewsletter():

    qu= db.demail0newsletter.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/email-newsletter.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def errorII404():

    qu= db.derror0404.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/error-404.html'


    errorII404form0 = SQLFORM(db.derrorII404form0, _class = 'form-search', _id= 'idUnk0' )

    errorII404form0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    errorII404form0.element('input[name=f0]')['_id']='nav-search-input'
    errorII404form0.element('input[name=f0]')['_class']='nav-search-input'

    errorII404form0.custom.submit['_type'] = 'submit'
    errorII404form0.custom.submit['_id'] = 'unk-id'
    errorII404form0.custom.submit['_value'] = 'submit input'
    errorII404form0.custom.submit['_class'] = 'unk-class'
    errorII404form0.custom.submit['_title'] = 'submit errorII404form0'

    if errorII404form0.accepts(request,session): 
        response.flash0 = 'submitted errorII404form0' 
    elif errorII404form0.errors:
        response.flash0 = '!Errors! errorII404form0' 
    else: 
        response.flash0 = 'errorII404form0' 



    errorII404form1 = SQLFORM(db.derrorII404form1, _class = 'form-search', _id= 'idUnk1' )

    errorII404form1.element('input[name=f0]')['_placeholder']='f0 Give it a search...'
    errorII404form1.element('input[name=f0]')['_id']='id_for774'
    errorII404form1.element('input[name=f0]')['_class']='search-query'

    errorII404form1.custom.submit['_type'] = 'submit'
    errorII404form1.custom.submit['_id'] = 'id_for776'
    errorII404form1.custom.submit['_value'] = 'Go!'
    errorII404form1.custom.submit['_class'] = 'btn btn-sm'
    errorII404form1.custom.submit['_title'] = 'submit errorII404form1'

    if errorII404form1.accepts(request,session): 
        response.flash1 = 'submitted errorII404form1' 
    elif errorII404form1.errors:
        response.flash1 = '!Errors! errorII404form1' 
    else: 
        response.flash1 = 'errorII404form1' 


    return dict( DICT= rows_dict, errorII404form0= errorII404form0, errorII404form1= errorII404form1, )

#@auth.requires_login()
def twoIImenuII2():

    qu= db.dtwo0menu02.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/two-menu-2.html'


    twoIImenuII2form0 = SQLFORM(db.dtwoIImenuII2form0, _class = 'navbar-form navbar-left form-search', _id= 'idUnk0' )

    twoIImenuII2form0.element('input[name=f0]')['_placeholder']='f0 search'
    twoIImenuII2form0.element('input[name=f0]')['_id']='id_for570'

    twoIImenuII2form0.custom.submit['_type'] = 'submit'
    twoIImenuII2form0.custom.submit['_id'] = 'id_for572'
    twoIImenuII2form0.custom.submit['_value'] = 'unk_574'
    twoIImenuII2form0.custom.submit['_class'] = 'btn btn-mini btn-info2'
    twoIImenuII2form0.custom.submit['_title'] = 'submit twoIImenuII2form0'

    if twoIImenuII2form0.accepts(request,session): 
        response.flash0 = 'submitted twoIImenuII2form0' 
    elif twoIImenuII2form0.errors:
        response.flash0 = '!Errors! twoIImenuII2form0' 
    else: 
        response.flash0 = 'twoIImenuII2form0' 


    return dict( DICT= rows_dict, twoIImenuII2form0= twoIImenuII2form0, )

#@auth.requires_login()
def elements():

    qu= db.delements.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/elements.html'


    elementsform0 = SQLFORM(db.delementsform0, _class = 'form-search', _id= 'idUnk0' )

    elementsform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    elementsform0.element('input[name=f0]')['_id']='nav-search-input'
    elementsform0.element('input[name=f0]')['_class']='nav-search-input'

    elementsform0.custom.submit['_type'] = 'submit'
    elementsform0.custom.submit['_id'] = 'unk-id'
    elementsform0.custom.submit['_value'] = 'submit input'
    elementsform0.custom.submit['_class'] = 'unk-class'
    elementsform0.custom.submit['_title'] = 'submit elementsform0'

    if elementsform0.accepts(request,session): 
        response.flash0 = 'submitted elementsform0' 
    elif elementsform0.errors:
        response.flash0 = '!Errors! elementsform0' 
    else: 
        response.flash0 = 'elementsform0' 



    elementsform1 = SQLFORM(db.delementsform1, _class = 'form-horizontal', _id= 'spinner-opts' )

    elementsform1.element('input[name=f0]')['_placeholder']='f0 place_96'
    elementsform1.element('input[name=f0]')['_id']='id_for93'
    elementsform1.element('input[name=f0]')['_value']='12'
    elementsform1.element('input[name=f0]')['_class']='hidden'
    elementsform1.element('input[name=f1]')['_placeholder']='f1 place_100'
    elementsform1.element('input[name=f1]')['_id']='id_for97'
    elementsform1.element('input[name=f1]')['_value']='7'
    elementsform1.element('input[name=f1]')['_class']='hidden'
    elementsform1.element('input[name=f2]')['_placeholder']='f2 place_104'
    elementsform1.element('input[name=f2]')['_id']='id_for101'
    elementsform1.element('input[name=f2]')['_value']='4'
    elementsform1.element('input[name=f2]')['_class']='hidden'
    elementsform1.element('input[name=f3]')['_placeholder']='f3 place_108'
    elementsform1.element('input[name=f3]')['_id']='id_for105'
    elementsform1.element('input[name=f3]')['_value']='10'
    elementsform1.element('input[name=f3]')['_class']='hidden'
    elementsform1.element('input[name=f4]')['_placeholder']='f4 place_112'
    elementsform1.element('input[name=f4]')['_id']='id_for109'
    elementsform1.element('input[name=f4]')['_value']='1'
    elementsform1.element('input[name=f4]')['_class']='hidden'
    elementsform1.element('input[name=f5]')['_placeholder']='f5 place_116'
    elementsform1.element('input[name=f5]')['_id']='id_for113'
    elementsform1.element('input[name=f5]')['_value']='0'
    elementsform1.element('input[name=f5]')['_class']='hidden'
    elementsform1.element('input[name=f6]')['_placeholder']='f6 place_120'
    elementsform1.element('input[name=f6]')['_id']='id_for117'
    elementsform1.element('input[name=f6]')['_value']='60'
    elementsform1.element('input[name=f6]')['_class']='hidden'
    elementsform1.element('input[name=f7]')['_placeholder']='f7 place_124'
    elementsform1.element('input[name=f7]')['_id']='id_for121'
    elementsform1.element('input[name=f7]')['_value']='1'
    elementsform1.element('input[name=f7]')['_class']='hidden'

    elementsform1.custom.submit['_type'] = 'submit'
    elementsform1.custom.submit['_id'] = 'unk-id'
    elementsform1.custom.submit['_value'] = 'submit input'
    elementsform1.custom.submit['_class'] = 'unk-class'
    elementsform1.custom.submit['_title'] = 'submit elementsform1'

    if elementsform1.accepts(request,session): 
        response.flash1 = 'submitted elementsform1' 
    elif elementsform1.errors:
        response.flash1 = '!Errors! elementsform1' 
    else: 
        response.flash1 = 'elementsform1' 


    return dict( DICT= rows_dict, elementsform0= elementsform0, elementsform1= elementsform1, )

#@auth.requires_login()
def timeline():

    qu= db.dtimeline.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/timeline.html'


    timelineform0 = SQLFORM(db.dtimelineform0, _class = 'form-search', _id= 'idUnk0' )

    timelineform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    timelineform0.element('input[name=f0]')['_id']='nav-search-input'
    timelineform0.element('input[name=f0]')['_class']='nav-search-input'

    timelineform0.custom.submit['_type'] = 'submit'
    timelineform0.custom.submit['_id'] = 'unk-id'
    timelineform0.custom.submit['_value'] = 'submit input'
    timelineform0.custom.submit['_class'] = 'unk-class'
    timelineform0.custom.submit['_title'] = 'submit timelineform0'

    if timelineform0.accepts(request,session): 
        response.flash0 = 'submitted timelineform0' 
    elif timelineform0.errors:
        response.flash0 = '!Errors! timelineform0' 
    else: 
        response.flash0 = 'timelineform0' 


    return dict( DICT= rows_dict, timelineform0= timelineform0, )

#@auth.requires_login()
def blank():

    qu= db.dblank.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/blank.html'


    blankform0 = SQLFORM(db.dblankform0, _class = 'form-search', _id= 'idUnk0' )

    blankform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    blankform0.element('input[name=f0]')['_id']='nav-search-input'
    blankform0.element('input[name=f0]')['_class']='nav-search-input'

    blankform0.custom.submit['_type'] = 'submit'
    blankform0.custom.submit['_id'] = 'unk-id'
    blankform0.custom.submit['_value'] = 'submit input'
    blankform0.custom.submit['_class'] = 'unk-class'
    blankform0.custom.submit['_title'] = 'submit blankform0'

    if blankform0.accepts(request,session): 
        response.flash0 = 'submitted blankform0' 
    elif blankform0.errors:
        response.flash0 = '!Errors! blankform0' 
    else: 
        response.flash0 = 'blankform0' 


    return dict( DICT= rows_dict, blankform0= blankform0, )

#@auth.requires_login()
def contentIIslider():

    qu= db.dcontent0slider.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/content-slider.html'


    contentIIsliderform0 = SQLFORM(db.dcontentIIsliderform0, _class = 'form-search', _id= 'idUnk0' )

    contentIIsliderform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    contentIIsliderform0.element('input[name=f0]')['_id']='nav-search-input'
    contentIIsliderform0.element('input[name=f0]')['_class']='nav-search-input'

    contentIIsliderform0.custom.submit['_type'] = 'submit'
    contentIIsliderform0.custom.submit['_id'] = 'unk-id'
    contentIIsliderform0.custom.submit['_value'] = 'submit input'
    contentIIsliderform0.custom.submit['_class'] = 'unk-class'
    contentIIsliderform0.custom.submit['_title'] = 'submit contentIIsliderform0'

    if contentIIsliderform0.accepts(request,session): 
        response.flash0 = 'submitted contentIIsliderform0' 
    elif contentIIsliderform0.errors:
        response.flash0 = '!Errors! contentIIsliderform0' 
    else: 
        response.flash0 = 'contentIIsliderform0' 


    return dict( DICT= rows_dict, contentIIsliderform0= contentIIsliderform0, )

#@auth.requires_login()
def typography():

    qu= db.dtypography.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/typography.html'


    typographyform0 = SQLFORM(db.dtypographyform0, _class = 'form-search', _id= 'idUnk0' )

    typographyform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    typographyform0.element('input[name=f0]')['_id']='nav-search-input'
    typographyform0.element('input[name=f0]')['_class']='nav-search-input'

    typographyform0.custom.submit['_type'] = 'submit'
    typographyform0.custom.submit['_id'] = 'unk-id'
    typographyform0.custom.submit['_value'] = 'submit input'
    typographyform0.custom.submit['_class'] = 'unk-class'
    typographyform0.custom.submit['_title'] = 'submit typographyform0'

    if typographyform0.accepts(request,session): 
        response.flash0 = 'submitted typographyform0' 
    elif typographyform0.errors:
        response.flash0 = '!Errors! typographyform0' 
    else: 
        response.flash0 = 'typographyform0' 


    return dict( DICT= rows_dict, typographyform0= typographyform0, )

#@auth.requires_login()
def topIImenu():

    qu= db.dtop0menu.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/top-menu.html'


    topIImenuform0 = SQLFORM(db.dtopIImenuform0, _class = 'navbar-form navbar-left form-search', _id= 'idUnk0' )

    topIImenuform0.element('input[name=f0]')['_placeholder']='f0 search'
    topIImenuform0.element('input[name=f0]')['_id']='id_for547'

    topIImenuform0.custom.submit['_type'] = 'submit'
    topIImenuform0.custom.submit['_id'] = 'id_for549'
    topIImenuform0.custom.submit['_value'] = 'unk_551'
    topIImenuform0.custom.submit['_class'] = 'btn btn-mini btn-info2'
    topIImenuform0.custom.submit['_title'] = 'submit topIImenuform0'

    if topIImenuform0.accepts(request,session): 
        response.flash0 = 'submitted topIImenuform0' 
    elif topIImenuform0.errors:
        response.flash0 = '!Errors! topIImenuform0' 
    else: 
        response.flash0 = 'topIImenuform0' 


    return dict( DICT= rows_dict, topIImenuform0= topIImenuform0, )

#@auth.requires_login()
def emailIIconfirmation():

    qu= db.demail0confirmation.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/email-confirmation.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def formIIelements():

    qu= db.dform0elements.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/form-elements.html'


    formIIelementsform0 = SQLFORM(db.dformIIelementsform0, _class = 'form-search', _id= 'idUnk0' )

    formIIelementsform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    formIIelementsform0.element('input[name=f0]')['_id']='nav-search-input'
    formIIelementsform0.element('input[name=f0]')['_class']='nav-search-input'

    formIIelementsform0.custom.submit['_type'] = 'submit'
    formIIelementsform0.custom.submit['_id'] = 'unk-id'
    formIIelementsform0.custom.submit['_value'] = 'submit input'
    formIIelementsform0.custom.submit['_class'] = 'unk-class'
    formIIelementsform0.custom.submit['_title'] = 'submit formIIelementsform0'

    if formIIelementsform0.accepts(request,session): 
        response.flash0 = 'submitted formIIelementsform0' 
    elif formIIelementsform0.errors:
        response.flash0 = '!Errors! formIIelementsform0' 
    else: 
        response.flash0 = 'formIIelementsform0' 



    formIIelementsform1 = SQLFORM(db.dformIIelementsform1, _class = 'form-horizontal', _id= 'idUnk1' )

    formIIelementsform1.element('input[name=f0]')['_placeholder']='f0 Username'
    formIIelementsform1.element('input[name=f0]')['_id']='form-field-1'
    formIIelementsform1.element('input[name=f0]')['_class']='col-xs-10 col-sm-5'
    formIIelementsform1.element('input[name=f1]')['_placeholder']='f1 Text Field'
    formIIelementsform1.element('input[name=f1]')['_id']='form-field-1-1'
    formIIelementsform1.element('input[name=f1]')['_class']='form-control'
    formIIelementsform1.element('input[name=f2]')['_placeholder']='f2 Password'
    formIIelementsform1.element('input[name=f2]')['_id']='form-field-2'
    formIIelementsform1.element('input[name=f2]')['_class']='col-xs-10 col-sm-5'
    formIIelementsform1.element('input[name=f3]')['_placeholder']='f3 place_240'
    formIIelementsform1.element('input[name=f3]')['_id']='form-input-readonly'
    formIIelementsform1.element('input[name=f3]')['_value']='This text field is readonly!'
    formIIelementsform1.element('input[name=f3]')['_class']='col-xs-10 col-sm-5'
    formIIelementsform1.element('input[name=f4]')['_placeholder']='f4 place_244'
    formIIelementsform1.element('input[name=f4]')['_id']='id-disable-check'
    formIIelementsform1.element('input[name=f4]')['_class']='ace'
    formIIelementsform1.element('input[name=f5]')['_placeholder']='f5 .input-sm'
    formIIelementsform1.element('input[name=f5]')['_id']='form-field-4'
    formIIelementsform1.element('input[name=f5]')['_class']='input-sm'
    formIIelementsform1.element('input[name=f6]')['_placeholder']='f6 .col-xs-1'
    formIIelementsform1.element('input[name=f6]')['_id']='form-field-5'
    formIIelementsform1.element('input[name=f6]')['_class']='col-xs-1'
    formIIelementsform1.element('input[name=f7]')['_placeholder']='f7 place_251'
    formIIelementsform1.element('input[name=f7]')['_id']='form-field-icon-1'
    formIIelementsform1.element('input[name=f8]')['_placeholder']='f8 place_254'
    formIIelementsform1.element('input[name=f8]')['_id']='form-field-icon-2'
    formIIelementsform1.element('input[name=f9]')['_placeholder']='f9 Tooltip on hover'
    formIIelementsform1.element('input[name=f9]')['_id']='form-field-6'
    formIIelementsform1.element('input[name=f10]')['_placeholder']='f10 Enter tags ...'
    formIIelementsform1.element('input[name=f10]')['_id']='form-field-tags'
    formIIelementsform1.element('input[name=f10]')['_value']='Tag Input Control'
    formIIelementsform1.element('input[name=f11]')['_placeholder']='f11 place_261'
    formIIelementsform1.element('input[name=f11]')['_id']='form-field-mask-1'
    formIIelementsform1.element('input[name=f11]')['_class']='form-control input-mask-date'
    formIIelementsform1.element('input[name=f12]')['_placeholder']='f12 place_264'
    formIIelementsform1.element('input[name=f12]')['_id']='form-field-mask-2'
    formIIelementsform1.element('input[name=f12]')['_class']='form-control input-mask-phone'
    formIIelementsform1.element('input[name=f13]')['_placeholder']='f13 place_267'
    formIIelementsform1.element('input[name=f13]')['_id']='form-field-mask-3'
    formIIelementsform1.element('input[name=f13]')['_class']='form-control input-mask-product'
    formIIelementsform1.element('input[name=f14]')['_placeholder']='f14 place_270'
    formIIelementsform1.element('input[name=f14]')['_id']='form-field-mask-4'
    formIIelementsform1.element('input[name=f14]')['_class']='input-medium input-mask-eyescript'
    formIIelementsform1.element('input[name=f15]')['_placeholder']='f15 place_280'
    formIIelementsform1.element('input[name=f15]')['_id']='id_for277'
    formIIelementsform1.element('input[name=f15]')['_class']='ace'
    formIIelementsform1.element('input[name=f16]')['_placeholder']='f16 place_284'
    formIIelementsform1.element('input[name=f16]')['_id']='id_for281'
    formIIelementsform1.element('input[name=f16]')['_class']='ace'
    formIIelementsform1.element('input[name=f17]')['_placeholder']='f17 place_288'
    formIIelementsform1.element('input[name=f17]')['_id']='id_for285'
    formIIelementsform1.element('input[name=f17]')['_class']='ace ace-checkbox-2'
    formIIelementsform1.element('input[name=f18]')['_placeholder']='f18 place_292'
    formIIelementsform1.element('input[name=f18]')['_id']='id_for289'
    formIIelementsform1.element('input[name=f18]')['_class']='ace'
    formIIelementsform1.element('input[name=f19]')['_placeholder']='f19 place_296'
    formIIelementsform1.element('input[name=f19]')['_id']='id_for293'
    formIIelementsform1.element('input[name=f19]')['_class']='ace input-lg'
    formIIelementsform1.element('input[name=f20]')['_placeholder']='f20 place_316'
    formIIelementsform1.element('input[name=f20]')['_id']='id_for312'
    formIIelementsform1.element('input[name=f20]')['_class']='ace ace-switch'
    formIIelementsform1.element('input[name=f21]')['_placeholder']='f21 place_321'
    formIIelementsform1.element('input[name=f21]')['_id']='id_for317'
    formIIelementsform1.element('input[name=f21]')['_class']='ace ace-switch ace-switch-2'
    formIIelementsform1.element('input[name=f22]')['_placeholder']='f22 place_326'
    formIIelementsform1.element('input[name=f22]')['_id']='id_for322'
    formIIelementsform1.element('input[name=f22]')['_class']='ace ace-switch ace-switch-3'
    formIIelementsform1.element('input[name=f23]')['_placeholder']='f23 place_331'
    formIIelementsform1.element('input[name=f23]')['_id']='id_for327'
    formIIelementsform1.element('input[name=f23]')['_class']='ace ace-switch'
    formIIelementsform1.element('input[name=f24]')['_placeholder']='f24 place_336'
    formIIelementsform1.element('input[name=f24]')['_id']='id_for332'
    formIIelementsform1.element('input[name=f24]')['_class']='ace ace-switch ace-switch-4'
    formIIelementsform1.element('input[name=f25]')['_placeholder']='f25 place_341'
    formIIelementsform1.element('input[name=f25]')['_id']='id_for337'
    formIIelementsform1.element('input[name=f25]')['_class']='ace ace-switch ace-switch-5'
    formIIelementsform1.element('input[name=f26]')['_placeholder']='f26 place_346'
    formIIelementsform1.element('input[name=f26]')['_id']='id_for342'
    formIIelementsform1.element('input[name=f26]')['_class']='ace ace-switch ace-switch-6'
    formIIelementsform1.element('input[name=f27]')['_placeholder']='f27 place_351'
    formIIelementsform1.element('input[name=f27]')['_id']='id_for347'
    formIIelementsform1.element('input[name=f27]')['_class']='ace ace-switch ace-switch-7'
    formIIelementsform1.element('input[name=f28]')['_placeholder']='f28 place_356'
    formIIelementsform1.element('input[name=f28]')['_id']='id_for352'
    formIIelementsform1.element('input[name=f28]')['_class']='ace ace-switch btn-rotate'
    formIIelementsform1.element('input[name=f29]')['_placeholder']='f29 place_361'
    formIIelementsform1.element('input[name=f29]')['_id']='id_for357'
    formIIelementsform1.element('input[name=f29]')['_class']='ace ace-switch ace-switch-4 btn-rotate'
    formIIelementsform1.element('input[name=f30]')['_placeholder']='f30 place_366'
    formIIelementsform1.element('input[name=f30]')['_id']='id_for362'
    formIIelementsform1.element('input[name=f30]')['_class']='ace ace-switch ace-switch-4 btn-empty'
    formIIelementsform1.element('input[name=f31]')['_placeholder']='f31 place_371'
    formIIelementsform1.element('input[name=f31]')['_id']='id_for367'
    formIIelementsform1.element('input[name=f31]')['_class']='ace ace-switch ace-switch-4 btn-flat'
    formIIelementsform1.element('input[name=f32]')['_placeholder']='f32 place_374'
    formIIelementsform1.element('input[name=f32]')['_id']='id-input-file-2'
    formIIelementsform1.element('input[name=f33]')['_placeholder']='f33 place_377'
    formIIelementsform1.element('input[name=f33]')['_id']='id-input-file-3'
    formIIelementsform1.element('input[name=f34]')['_placeholder']='f34 place_381'
    formIIelementsform1.element('input[name=f34]')['_id']='id-file-format'
    formIIelementsform1.element('input[name=f34]')['_class']='ace'
    formIIelementsform1.element('input[name=f35]')['_placeholder']='f35 place_384'
    formIIelementsform1.element('input[name=f35]')['_id']='spinner1'
    formIIelementsform1.element('input[name=f36]')['_placeholder']='f36 place_387'
    formIIelementsform1.element('input[name=f36]')['_id']='spinner2'
    formIIelementsform1.element('input[name=f36]')['_class']='input-sm'
    formIIelementsform1.element('input[name=f37]')['_placeholder']='f37 place_390'
    formIIelementsform1.element('input[name=f37]')['_id']='spinner3'
    formIIelementsform1.element('input[name=f38]')['_placeholder']='f38 place_393'
    formIIelementsform1.element('input[name=f38]')['_id']='spinner4'
    formIIelementsform1.element('input[name=f38]')['_class']='input-lg'
    formIIelementsform1.element('input[name=f39]')['_placeholder']='f39 place_396'
    formIIelementsform1.element('input[name=f39]')['_id']='id-date-picker-1'
    formIIelementsform1.element('input[name=f39]')['_class']='form-control date-picker'
    formIIelementsform1.element('input[name=f40]')['_placeholder']='f40 place_399'
    formIIelementsform1.element('input[name=f40]')['_id']='id_for397'
    formIIelementsform1.element('input[name=f40]')['_class']='input-sm form-control'
    formIIelementsform1.element('input[name=f41]')['_placeholder']='f41 place_402'
    formIIelementsform1.element('input[name=f41]')['_id']='id_for400'
    formIIelementsform1.element('input[name=f41]')['_class']='input-sm form-control'
    formIIelementsform1.element('input[name=f42]')['_placeholder']='f42 place_405'
    formIIelementsform1.element('input[name=f42]')['_id']='id-date-range-picker-1'
    formIIelementsform1.element('input[name=f42]')['_class']='form-control'
    formIIelementsform1.element('input[name=f43]')['_placeholder']='f43 place_408'
    formIIelementsform1.element('input[name=f43]')['_id']='timepicker1'
    formIIelementsform1.element('input[name=f43]')['_class']='form-control'
    formIIelementsform1.element('input[name=f44]')['_placeholder']='f44 place_411'
    formIIelementsform1.element('input[name=f44]')['_id']='date-timepicker1'
    formIIelementsform1.element('input[name=f44]')['_class']='form-control'
    formIIelementsform1.element('input[name=f45]')['_placeholder']='f45 place_414'
    formIIelementsform1.element('input[name=f45]')['_id']='colorpicker1'
    formIIelementsform1.element('input[name=f45]')['_class']='input-small'
    formIIelementsform1.element('input[name=f46]')['_placeholder']='f46 place_417'
    formIIelementsform1.element('input[name=f46]')['_id']='id_for415'
    formIIelementsform1.element('input[name=f46]')['_value']='15'
    formIIelementsform1.element('input[name=f46]')['_class']='input-small knob'
    formIIelementsform1.element('input[name=f47]')['_placeholder']='f47 place_420'
    formIIelementsform1.element('input[name=f47]')['_id']='id_for418'
    formIIelementsform1.element('input[name=f47]')['_value']='41'
    formIIelementsform1.element('input[name=f47]')['_class']='input-small knob'
    formIIelementsform1.element('input[name=f48]')['_placeholder']='f48 place_423'
    formIIelementsform1.element('input[name=f48]')['_id']='id_for421'
    formIIelementsform1.element('input[name=f48]')['_value']='1'
    formIIelementsform1.element('input[name=f48]')['_class']='input-small knob'
    formIIelementsform1.element('textarea[name=f49]')['_placeholder']='f49 Default Text'
    formIIelementsform1.element('textarea[name=f49]')['_id']='form-field-8'
    formIIelementsform1.element('textarea[name=f49]')['_class']='form-control'
    formIIelementsform1.element('textarea[name=f50]')['_placeholder']='f50 place_428'
    formIIelementsform1.element('textarea[name=f50]')['_id']='form-field-9'
    formIIelementsform1.element('textarea[name=f50]')['_class']='form-control limited'
    formIIelementsform1.element('textarea[name=f51]')['_placeholder']='f51 place_431'
    formIIelementsform1.element('textarea[name=f51]')['_id']='form-field-11'
    formIIelementsform1.element('textarea[name=f51]')['_class']='autosize-transition form-control'

    formIIelementsform1.custom.submit['_type'] = 'submit'
    formIIelementsform1.custom.submit['_id'] = 'id_for450'
    formIIelementsform1.custom.submit['_value'] = 'Submit'
    formIIelementsform1.custom.submit['_class'] = 'btn btn-info'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_type'] = 'submit'
    formIIelementsform1.custom.submit['_id'] = 'id_for453'
    formIIelementsform1.custom.submit['_value'] = 'Reset'
    formIIelementsform1.custom.submit['_class'] = 'btn'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_type'] = 'submit'
    formIIelementsform1.custom.submit['_id'] = 'id_for456'
    formIIelementsform1.custom.submit['_value'] = 'Go!'
    formIIelementsform1.custom.submit['_class'] = 'btn btn-sm btn-default'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for459'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for462'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for465'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for468'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for471'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for474'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for477'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for480'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for483'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for486'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for489'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for492'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for495'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for498'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for501'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    formIIelementsform1.custom.submit['_id'] = 'id_for504'
    formIIelementsform1.custom.submit['_title'] = 'submit formIIelementsform1'

    if formIIelementsform1.accepts(request,session): 
        response.flash1 = 'submitted formIIelementsform1' 
    elif formIIelementsform1.errors:
        response.flash1 = '!Errors! formIIelementsform1' 
    else: 
        response.flash1 = 'formIIelementsform1' 



    formIIelementsform2 = SQLFORM(db.dformIIelementsform2, _class = 'classUnk2', _id= 'idUnk2' )

    formIIelementsform2.element('input[name=f0]')['_placeholder']='f0 Type something'
    formIIelementsform2.element('input[name=f0]')['_id']='id_for507'
    formIIelementsform2.element('input[name=f1]')['_placeholder']='f1 place_513'
    formIIelementsform2.element('input[name=f1]')['_id']='id_for510'
    formIIelementsform2.element('input[name=f1]')['_class']='ace'

    formIIelementsform2.custom.submit['_type'] = 'submit'
    formIIelementsform2.custom.submit['_id'] = 'id_for514'
    formIIelementsform2.custom.submit['_value'] = 'Submit'
    formIIelementsform2.custom.submit['_class'] = 'btn btn-sm btn-success'
    formIIelementsform2.custom.submit['_title'] = 'submit formIIelementsform2'

    if formIIelementsform2.accepts(request,session): 
        response.flash2 = 'submitted formIIelementsform2' 
    elif formIIelementsform2.errors:
        response.flash2 = '!Errors! formIIelementsform2' 
    else: 
        response.flash2 = 'formIIelementsform2' 



    formIIelementsform3 = SQLFORM(db.dformIIelementsform3, _class = 'form-inline', _id= 'idUnk3' )

    formIIelementsform3.element('input[name=f0]')['_placeholder']='f0 Username'
    formIIelementsform3.element('input[name=f0]')['_id']='id_for518'
    formIIelementsform3.element('input[name=f0]')['_class']='input-small'
    formIIelementsform3.element('input[name=f1]')['_placeholder']='f1 Password'
    formIIelementsform3.element('input[name=f1]')['_id']='id_for521'
    formIIelementsform3.element('input[name=f1]')['_class']='input-small'
    formIIelementsform3.element('input[name=f2]')['_placeholder']='f2 place_527'
    formIIelementsform3.element('input[name=f2]')['_id']='id_for524'
    formIIelementsform3.element('input[name=f2]')['_class']='ace'

    formIIelementsform3.custom.submit['_type'] = 'submit'
    formIIelementsform3.custom.submit['_id'] = 'id_for528'
    formIIelementsform3.custom.submit['_value'] = 'Login'
    formIIelementsform3.custom.submit['_class'] = 'btn btn-info btn-sm'
    formIIelementsform3.custom.submit['_title'] = 'submit formIIelementsform3'

    if formIIelementsform3.accepts(request,session): 
        response.flash3 = 'submitted formIIelementsform3' 
    elif formIIelementsform3.errors:
        response.flash3 = '!Errors! formIIelementsform3' 
    else: 
        response.flash3 = 'formIIelementsform3' 



    formIIelementsform4 = SQLFORM(db.dformIIelementsform4, _class = 'form-search', _id= 'idUnk4' )

    formIIelementsform4.element('input[name=f0]')['_placeholder']='f0 Type your query'
    formIIelementsform4.element('input[name=f0]')['_id']='id_for532'
    formIIelementsform4.element('input[name=f0]')['_class']='form-control search-query'
    formIIelementsform4.element('input[name=f1]')['_placeholder']='f1 Type your query'
    formIIelementsform4.element('input[name=f1]')['_id']='id_for534'
    formIIelementsform4.element('input[name=f1]')['_class']='form-control search-query'
    formIIelementsform4.element('input[name=f2]')['_placeholder']='f2 Type your query'
    formIIelementsform4.element('input[name=f2]')['_id']='id_for536'
    formIIelementsform4.element('input[name=f2]')['_class']='form-control search-query'

    formIIelementsform4.custom.submit['_type'] = 'submit'
    formIIelementsform4.custom.submit['_id'] = 'id_for538'
    formIIelementsform4.custom.submit['_value'] = 'Search'
    formIIelementsform4.custom.submit['_class'] = 'btn btn-purple btn-sm'
    formIIelementsform4.custom.submit['_title'] = 'submit formIIelementsform4'

    formIIelementsform4.custom.submit['_type'] = 'submit'
    formIIelementsform4.custom.submit['_id'] = 'id_for541'
    formIIelementsform4.custom.submit['_value'] = 'Search'
    formIIelementsform4.custom.submit['_class'] = 'btn btn-default btn-lg'
    formIIelementsform4.custom.submit['_title'] = 'submit formIIelementsform4'

    formIIelementsform4.custom.submit['_type'] = 'submit'
    formIIelementsform4.custom.submit['_id'] = 'id_for544'
    formIIelementsform4.custom.submit['_value'] = 'Search'
    formIIelementsform4.custom.submit['_class'] = 'btn btn-inverse btn-white'
    formIIelementsform4.custom.submit['_title'] = 'submit formIIelementsform4'

    if formIIelementsform4.accepts(request,session): 
        response.flash4 = 'submitted formIIelementsform4' 
    elif formIIelementsform4.errors:
        response.flash4 = '!Errors! formIIelementsform4' 
    else: 
        response.flash4 = 'formIIelementsform4' 


    return dict( DICT= rows_dict, formIIelementsform0= formIIelementsform0, formIIelementsform1= formIIelementsform1, formIIelementsform2= formIIelementsform2, formIIelementsform3= formIIelementsform3, formIIelementsform4= formIIelementsform4, )

#@auth.requires_login()
def jqgrid():

    qu= db.djqgrid.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/jqgrid.html'


    jqgridform0 = SQLFORM(db.djqgridform0, _class = 'form-search', _id= 'idUnk0' )

    jqgridform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    jqgridform0.element('input[name=f0]')['_id']='nav-search-input'
    jqgridform0.element('input[name=f0]')['_class']='nav-search-input'

    jqgridform0.custom.submit['_type'] = 'submit'
    jqgridform0.custom.submit['_id'] = 'unk-id'
    jqgridform0.custom.submit['_value'] = 'submit input'
    jqgridform0.custom.submit['_class'] = 'unk-class'
    jqgridform0.custom.submit['_title'] = 'submit jqgridform0'

    if jqgridform0.accepts(request,session): 
        response.flash0 = 'submitted jqgridform0' 
    elif jqgridform0.errors:
        response.flash0 = '!Errors! jqgridform0' 
    else: 
        response.flash0 = 'jqgridform0' 


    return dict( DICT= rows_dict, jqgridform0= jqgridform0, )

#@auth.requires_login()
def nestableIIlist():

    qu= db.dnestable0list.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/nestable-list.html'


    nestableIIlistform0 = SQLFORM(db.dnestableIIlistform0, _class = 'form-search', _id= 'idUnk0' )

    nestableIIlistform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    nestableIIlistform0.element('input[name=f0]')['_id']='nav-search-input'
    nestableIIlistform0.element('input[name=f0]')['_class']='nav-search-input'

    nestableIIlistform0.custom.submit['_type'] = 'submit'
    nestableIIlistform0.custom.submit['_id'] = 'unk-id'
    nestableIIlistform0.custom.submit['_value'] = 'submit input'
    nestableIIlistform0.custom.submit['_class'] = 'unk-class'
    nestableIIlistform0.custom.submit['_title'] = 'submit nestableIIlistform0'

    if nestableIIlistform0.accepts(request,session): 
        response.flash0 = 'submitted nestableIIlistform0' 
    elif nestableIIlistform0.errors:
        response.flash0 = '!Errors! nestableIIlistform0' 
    else: 
        response.flash0 = 'nestableIIlistform0' 


    return dict( DICT= rows_dict, nestableIIlistform0= nestableIIlistform0, )

#@auth.requires_login()
def jqueryIIui():

    qu= db.djquery0ui.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/jquery-ui.html'


    jqueryIIuiform0 = SQLFORM(db.djqueryIIuiform0, _class = 'form-search', _id= 'idUnk0' )

    jqueryIIuiform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    jqueryIIuiform0.element('input[name=f0]')['_id']='nav-search-input'
    jqueryIIuiform0.element('input[name=f0]')['_class']='nav-search-input'

    jqueryIIuiform0.custom.submit['_type'] = 'submit'
    jqueryIIuiform0.custom.submit['_id'] = 'unk-id'
    jqueryIIuiform0.custom.submit['_value'] = 'submit input'
    jqueryIIuiform0.custom.submit['_class'] = 'unk-class'
    jqueryIIuiform0.custom.submit['_title'] = 'submit jqueryIIuiform0'

    if jqueryIIuiform0.accepts(request,session): 
        response.flash0 = 'submitted jqueryIIuiform0' 
    elif jqueryIIuiform0.errors:
        response.flash0 = '!Errors! jqueryIIuiform0' 
    else: 
        response.flash0 = 'jqueryIIuiform0' 


    return dict( DICT= rows_dict, jqueryIIuiform0= jqueryIIuiform0, )

#@auth.requires_login()
def inbox():

    qu= db.dinbox.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/inbox.html'


    inboxform0 = SQLFORM(db.dinboxform0, _class = 'form-search', _id= 'idUnk0' )

    inboxform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    inboxform0.element('input[name=f0]')['_id']='nav-search-input'
    inboxform0.element('input[name=f0]')['_class']='nav-search-input'

    inboxform0.custom.submit['_type'] = 'submit'
    inboxform0.custom.submit['_id'] = 'unk-id'
    inboxform0.custom.submit['_value'] = 'submit input'
    inboxform0.custom.submit['_class'] = 'unk-class'
    inboxform0.custom.submit['_title'] = 'submit inboxform0'

    if inboxform0.accepts(request,session): 
        response.flash0 = 'submitted inboxform0' 
    elif inboxform0.errors:
        response.flash0 = '!Errors! inboxform0' 
    else: 
        response.flash0 = 'inboxform0' 



    inboxform1 = SQLFORM(db.dinboxform1, _class = 'form-search', _id= 'idUnk1' )

    inboxform1.element('input[name=f0]')['_placeholder']='f0 Search inbox ...'
    inboxform1.element('input[name=f0]')['_id']='id_for655'
    inboxform1.element('input[name=f0]')['_class']='input-small nav-search-input'

    inboxform1.custom.submit['_type'] = 'submit'
    inboxform1.custom.submit['_id'] = 'unk-id'
    inboxform1.custom.submit['_value'] = 'submit input'
    inboxform1.custom.submit['_class'] = 'unk-class'
    inboxform1.custom.submit['_title'] = 'submit inboxform1'

    if inboxform1.accepts(request,session): 
        response.flash1 = 'submitted inboxform1' 
    elif inboxform1.errors:
        response.flash1 = '!Errors! inboxform1' 
    else: 
        response.flash1 = 'inboxform1' 



    inboxform2 = SQLFORM(db.dinboxform2, _class = 'hide form-horizontal message-form col-xs-12', _id= 'id-message-form' )

    inboxform2.element('input[name=f0]')['_placeholder']='f0 Recipient(s)'
    inboxform2.element('input[name=f0]')['_id']='form-field-recipient'
    inboxform2.element('input[name=f0]')['_value']='alex@doe.com'
    inboxform2.element('input[name=f1]')['_placeholder']='f1 Subject'
    inboxform2.element('input[name=f1]')['_id']='form-field-subject'
    inboxform2.element('input[name=f1]')['_class']='col-xs-12'
    inboxform2.element('input[name=f2]')['_placeholder']='f2 place_663'
    inboxform2.element('input[name=f2]')['_id']='id_for661'

    inboxform2.custom.submit['_type'] = 'submit'
    inboxform2.custom.submit['_id'] = 'id-add-attachment'
    inboxform2.custom.submit['_value'] = 'Add Attachment'
    inboxform2.custom.submit['_class'] = 'btn btn-sm btn-danger'
    inboxform2.custom.submit['_title'] = 'submit inboxform2'

    if inboxform2.accepts(request,session): 
        response.flash2 = 'submitted inboxform2' 
    elif inboxform2.errors:
        response.flash2 = '!Errors! inboxform2' 
    else: 
        response.flash2 = 'inboxform2' 


    return dict( DICT= rows_dict, inboxform0= inboxform0, inboxform1= inboxform1, inboxform2= inboxform2, )

#@auth.requires_login()
def formIIwizard():

    qu= db.dform0wizard.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/form-wizard.html'


    formIIwizardform0 = SQLFORM(db.dformIIwizardform0, _class = 'form-search', _id= 'idUnk0' )

    formIIwizardform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    formIIwizardform0.element('input[name=f0]')['_id']='nav-search-input'
    formIIwizardform0.element('input[name=f0]')['_class']='nav-search-input'

    formIIwizardform0.custom.submit['_type'] = 'submit'
    formIIwizardform0.custom.submit['_id'] = 'unk-id'
    formIIwizardform0.custom.submit['_value'] = 'submit input'
    formIIwizardform0.custom.submit['_class'] = 'unk-class'
    formIIwizardform0.custom.submit['_title'] = 'submit formIIwizardform0'

    if formIIwizardform0.accepts(request,session): 
        response.flash0 = 'submitted formIIwizardform0' 
    elif formIIwizardform0.errors:
        response.flash0 = '!Errors! formIIwizardform0' 
    else: 
        response.flash0 = 'formIIwizardform0' 



    formIIwizardform1 = SQLFORM(db.dformIIwizardform1, _class = 'form-horizontal', _id= 'sample-form' )

    formIIwizardform1.element('input[name=f0]')['_placeholder']='f0 place_588'
    formIIwizardform1.element('input[name=f0]')['_id']='inputWarning'
    formIIwizardform1.element('input[name=f0]')['_class']='width-100'
    formIIwizardform1.element('input[name=f1]')['_placeholder']='f1 place_591'
    formIIwizardform1.element('input[name=f1]')['_id']='inputError'
    formIIwizardform1.element('input[name=f1]')['_class']='width-100'
    formIIwizardform1.element('input[name=f2]')['_placeholder']='f2 place_594'
    formIIwizardform1.element('input[name=f2]')['_id']='inputSuccess'
    formIIwizardform1.element('input[name=f2]')['_class']='width-100'
    formIIwizardform1.element('input[name=f3]')['_placeholder']='f3 place_597'
    formIIwizardform1.element('input[name=f3]')['_id']='inputInfo'
    formIIwizardform1.element('input[name=f3]')['_class']='width-100'
    formIIwizardform1.element('input[name=f4]')['_placeholder']='f4 place_600'
    formIIwizardform1.element('input[name=f4]')['_id']='inputError2'
    formIIwizardform1.element('input[name=f4]')['_class']='width-100'

    formIIwizardform1.custom.submit['_type'] = 'submit'
    formIIwizardform1.custom.submit['_id'] = 'unk-id'
    formIIwizardform1.custom.submit['_value'] = 'submit input'
    formIIwizardform1.custom.submit['_class'] = 'unk-class'
    formIIwizardform1.custom.submit['_title'] = 'submit formIIwizardform1'

    if formIIwizardform1.accepts(request,session): 
        response.flash1 = 'submitted formIIwizardform1' 
    elif formIIwizardform1.errors:
        response.flash1 = '!Errors! formIIwizardform1' 
    else: 
        response.flash1 = 'formIIwizardform1' 



    formIIwizardform2 = SQLFORM(db.dformIIwizardform2, _class = 'form-horizontal hide', _id= 'validation-form' )

    formIIwizardform2.element('input[name=f0]')['_placeholder']='f0 place_603'
    formIIwizardform2.element('input[name=f0]')['_id']='email'
    formIIwizardform2.element('input[name=f0]')['_class']='col-xs-12 col-sm-6'
    formIIwizardform2.element('input[name=f1]')['_placeholder']='f1 place_606'
    formIIwizardform2.element('input[name=f1]')['_id']='password'
    formIIwizardform2.element('input[name=f1]')['_class']='col-xs-12 col-sm-4'
    formIIwizardform2.element('input[name=f2]')['_placeholder']='f2 place_609'
    formIIwizardform2.element('input[name=f2]')['_id']='password2'
    formIIwizardform2.element('input[name=f2]')['_class']='col-xs-12 col-sm-4'
    formIIwizardform2.element('input[name=f3]')['_placeholder']='f3 place_612'
    formIIwizardform2.element('input[name=f3]')['_id']='name'
    formIIwizardform2.element('input[name=f3]')['_class']='col-xs-12 col-sm-5'
    formIIwizardform2.element('input[name=f4]')['_placeholder']='f4 place_615'
    formIIwizardform2.element('input[name=f4]')['_id']='phone'
    formIIwizardform2.element('input[name=f5]')['_placeholder']='f5 place_618'
    formIIwizardform2.element('input[name=f5]')['_id']='url'
    formIIwizardform2.element('input[name=f5]')['_class']='col-xs-12 col-sm-8'
    formIIwizardform2.element('input[name=f6]')['_placeholder']='f6 place_622'
    formIIwizardform2.element('input[name=f6]')['_id']='id_for619'
    formIIwizardform2.element('input[name=f6]')['_value']='1'
    formIIwizardform2.element('input[name=f6]')['_class']='ace'
    formIIwizardform2.element('input[name=f7]')['_placeholder']='f7 place_626'
    formIIwizardform2.element('input[name=f7]')['_id']='id_for623'
    formIIwizardform2.element('input[name=f7]')['_value']='2'
    formIIwizardform2.element('input[name=f7]')['_class']='ace'
    formIIwizardform2.element('input[name=f9]')['_placeholder']='f9 place_636'
    formIIwizardform2.element('input[name=f9]')['_id']='agree'
    formIIwizardform2.element('input[name=f9]')['_class']='ace'
    formIIwizardform2.element('textarea[name=f10]')['_placeholder']='f10 place_639'
    formIIwizardform2.element('textarea[name=f10]')['_id']='comment'
    formIIwizardform2.element('textarea[name=f10]')['_class']='input-xlarge'

    formIIwizardform2.custom.submit['_type'] = 'submit'
    formIIwizardform2.custom.submit['_id'] = 'unk-id'
    formIIwizardform2.custom.submit['_value'] = 'submit input'
    formIIwizardform2.custom.submit['_class'] = 'unk-class'
    formIIwizardform2.custom.submit['_title'] = 'submit formIIwizardform2'

    if formIIwizardform2.accepts(request,session): 
        response.flash2 = 'submitted formIIwizardform2' 
    elif formIIwizardform2.errors:
        response.flash2 = '!Errors! formIIwizardform2' 
    else: 
        response.flash2 = 'formIIwizardform2' 


    return dict( DICT= rows_dict, formIIwizardform0= formIIwizardform0, formIIwizardform1= formIIwizardform1, formIIwizardform2= formIIwizardform2, )

#@auth.requires_login()
def dropzone():

    qu= db.ddropzone.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/dropzone.html'


    dropzoneform0 = SQLFORM(db.ddropzoneform0, _class = 'form-search', _id= 'idUnk0' )

    dropzoneform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    dropzoneform0.element('input[name=f0]')['_id']='nav-search-input'
    dropzoneform0.element('input[name=f0]')['_class']='nav-search-input'

    dropzoneform0.custom.submit['_type'] = 'submit'
    dropzoneform0.custom.submit['_id'] = 'unk-id'
    dropzoneform0.custom.submit['_value'] = 'submit input'
    dropzoneform0.custom.submit['_class'] = 'unk-class'
    dropzoneform0.custom.submit['_title'] = 'submit dropzoneform0'

    if dropzoneform0.accepts(request,session): 
        response.flash0 = 'submitted dropzoneform0' 
    elif dropzoneform0.errors:
        response.flash0 = '!Errors! dropzoneform0' 
    else: 
        response.flash0 = 'dropzoneform0' 



    dropzoneform1 = SQLFORM(db.ddropzoneform1, _class = 'dropzone well', _id= 'dropzone' )

    dropzoneform1.element('input[name=f0]')['_placeholder']='f0 place_798'
    dropzoneform1.element('input[name=f0]')['_id']='id_for796'

    dropzoneform1.custom.submit['_type'] = 'submit'
    dropzoneform1.custom.submit['_id'] = 'unk-id'
    dropzoneform1.custom.submit['_value'] = 'submit input'
    dropzoneform1.custom.submit['_class'] = 'unk-class'
    dropzoneform1.custom.submit['_title'] = 'submit dropzoneform1'

    if dropzoneform1.accepts(request,session): 
        response.flash1 = 'submitted dropzoneform1' 
    elif dropzoneform1.errors:
        response.flash1 = '!Errors! dropzoneform1' 
    else: 
        response.flash1 = 'dropzoneform1' 


    return dict( DICT= rows_dict, dropzoneform0= dropzoneform0, dropzoneform1= dropzoneform1, )

#@auth.requires_login()
def twoIImenuII1():

    qu= db.dtwo0menu01.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/two-menu-1.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def grid():

    qu= db.dgrid.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/grid.html'


    gridform0 = SQLFORM(db.dgridform0, _class = 'form-search', _id= 'idUnk0' )

    gridform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    gridform0.element('input[name=f0]')['_id']='nav-search-input'
    gridform0.element('input[name=f0]')['_class']='nav-search-input'

    gridform0.custom.submit['_type'] = 'submit'
    gridform0.custom.submit['_id'] = 'unk-id'
    gridform0.custom.submit['_value'] = 'submit input'
    gridform0.custom.submit['_class'] = 'unk-class'
    gridform0.custom.submit['_title'] = 'submit gridform0'

    if gridform0.accepts(request,session): 
        response.flash0 = 'submitted gridform0' 
    elif gridform0.errors:
        response.flash0 = '!Errors! gridform0' 
    else: 
        response.flash0 = 'gridform0' 


    return dict( DICT= rows_dict, gridform0= gridform0, )

#@auth.requires_login()
def pricing():

    qu= db.dpricing.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/pricing.html'


    pricingform0 = SQLFORM(db.dpricingform0, _class = 'form-search', _id= 'idUnk0' )

    pricingform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    pricingform0.element('input[name=f0]')['_id']='nav-search-input'
    pricingform0.element('input[name=f0]')['_class']='nav-search-input'

    pricingform0.custom.submit['_type'] = 'submit'
    pricingform0.custom.submit['_id'] = 'unk-id'
    pricingform0.custom.submit['_value'] = 'submit input'
    pricingform0.custom.submit['_class'] = 'unk-class'
    pricingform0.custom.submit['_title'] = 'submit pricingform0'

    if pricingform0.accepts(request,session): 
        response.flash0 = 'submitted pricingform0' 
    elif pricingform0.errors:
        response.flash0 = '!Errors! pricingform0' 
    else: 
        response.flash0 = 'pricingform0' 


    return dict( DICT= rows_dict, pricingform0= pricingform0, )

#@auth.requires_login()
def search():

    qu= db.dsearch.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/search.html'


    searchform0 = SQLFORM(db.dsearchform0, _class = 'form-search', _id= 'idUnk0' )

    searchform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    searchform0.element('input[name=f0]')['_id']='nav-search-input'
    searchform0.element('input[name=f0]')['_class']='nav-search-input'

    searchform0.custom.submit['_type'] = 'submit'
    searchform0.custom.submit['_id'] = 'unk-id'
    searchform0.custom.submit['_value'] = 'submit input'
    searchform0.custom.submit['_class'] = 'unk-class'
    searchform0.custom.submit['_title'] = 'submit searchform0'

    if searchform0.accepts(request,session): 
        response.flash0 = 'submitted searchform0' 
    elif searchform0.errors:
        response.flash0 = '!Errors! searchform0' 
    else: 
        response.flash0 = 'searchform0' 



    searchform1 = SQLFORM(db.dsearchform1, _class = 'classUnk1', _id= 'idUnk1' )

    searchform1.element('input[name=f0]')['_placeholder']='f0 Look within results'
    searchform1.element('input[name=f0]')['_id']='id_for557'
    searchform1.element('input[name=f0]')['_class']='form-control'

    searchform1.custom.submit['_type'] = 'submit'
    searchform1.custom.submit['_id'] = 'id_for559'
    searchform1.custom.submit['_value'] = 'unk_561'
    searchform1.custom.submit['_class'] = 'btn btn-default no-border btn-sm'
    searchform1.custom.submit['_title'] = 'submit searchform1'

    if searchform1.accepts(request,session): 
        response.flash1 = 'submitted searchform1' 
    elif searchform1.errors:
        response.flash1 = '!Errors! searchform1' 
    else: 
        response.flash1 = 'searchform1' 



    searchform2 = SQLFORM(db.dsearchform2, _class = 'classUnk2', _id= 'idUnk2' )

    searchform2.element('input[name=f0]')['_placeholder']='f0 place_565'
    searchform2.element('input[name=f0]')['_id']='id_for563'
    searchform2.element('input[name=f0]')['_value']='Hello World'
    searchform2.element('input[name=f0]')['_class']='form-control'

    searchform2.custom.submit['_type'] = 'submit'
    searchform2.custom.submit['_id'] = 'id_for566'
    searchform2.custom.submit['_value'] = 'unk_568'
    searchform2.custom.submit['_class'] = 'btn btn-primary btn-sm'
    searchform2.custom.submit['_title'] = 'submit searchform2'

    if searchform2.accepts(request,session): 
        response.flash2 = 'submitted searchform2' 
    elif searchform2.errors:
        response.flash2 = '!Errors! searchform2' 
    else: 
        response.flash2 = 'searchform2' 


    return dict( DICT= rows_dict, searchform0= searchform0, searchform1= searchform1, searchform2= searchform2, )

#@auth.requires_login()
def faq():

    qu= db.dfaq.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/faq.html'


    faqform0 = SQLFORM(db.dfaqform0, _class = 'form-search', _id= 'idUnk0' )

    faqform0.element('input[name=f0]')['_placeholder']='f0 Search ...'
    faqform0.element('input[name=f0]')['_id']='nav-search-input'
    faqform0.element('input[name=f0]')['_class']='nav-search-input'

    faqform0.custom.submit['_type'] = 'submit'
    faqform0.custom.submit['_id'] = 'unk-id'
    faqform0.custom.submit['_value'] = 'submit input'
    faqform0.custom.submit['_class'] = 'unk-class'
    faqform0.custom.submit['_title'] = 'submit faqform0'

    if faqform0.accepts(request,session): 
        response.flash0 = 'submitted faqform0' 
    elif faqform0.errors:
        response.flash0 = '!Errors! faqform0' 
    else: 
        response.flash0 = 'faqform0' 


    return dict( DICT= rows_dict, faqform0= faqform0, )