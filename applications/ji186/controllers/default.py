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
def typo():

    qu= db.dtypo.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/typo.html'


    typoform0 = SQLFORM(db.dtypoform0, _class = 'form-header', _id= 'idUnk0' )

    typoform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    typoform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    typoform0.element('input[name=f0]')['_id']='id397'
    typoform0.custom.submit['_type'] = 'submit'
    typoform0.custom.submit['_class'] = 'au-btn--submit'
    typoform0.custom.submit['_value'] = 'unk_401'
    typoform0.custom.submit['_id'] = 'id399'
    typoform0.custom.submit['_title'] = 'submit typoform0'

    if typoform0.accepts(request,session): 
        response.flash0 = 'submitted typoform0' 
    elif typoform0.errors:
        response.flash0 = '!Errors! typoform0' 
    else: 
        response.flash0 = 'typoform0' 


    return dict( DICT= rows_dict, typoform0= typoform0, )

#@auth.requires_login()
def tab():

    qu= db.dtab.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/tab.html'


    tabform0 = SQLFORM(db.dtabform0, _class = 'form-header', _id= 'idUnk0' )

    tabform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    tabform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    tabform0.element('input[name=f0]')['_id']='id434'
    tabform0.custom.submit['_type'] = 'submit'
    tabform0.custom.submit['_class'] = 'au-btn--submit'
    tabform0.custom.submit['_value'] = 'unk_438'
    tabform0.custom.submit['_id'] = 'id436'
    tabform0.custom.submit['_title'] = 'submit tabform0'

    if tabform0.accepts(request,session): 
        response.flash0 = 'submitted tabform0' 
    elif tabform0.errors:
        response.flash0 = '!Errors! tabform0' 
    else: 
        response.flash0 = 'tabform0' 


    return dict( DICT= rows_dict, tabform0= tabform0, )

#@auth.requires_login()
def progress_bar():

    qu= db.dprogress0bar.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/progress-bar.html'


    progress_barform0 = SQLFORM(db.dprogress_barform0, _class = 'form-header', _id= 'idUnk0' )

    progress_barform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    progress_barform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    progress_barform0.element('input[name=f0]')['_id']='id379'
    progress_barform0.custom.submit['_type'] = 'submit'
    progress_barform0.custom.submit['_class'] = 'au-btn--submit'
    progress_barform0.custom.submit['_value'] = 'unk_383'
    progress_barform0.custom.submit['_id'] = 'id381'
    progress_barform0.custom.submit['_title'] = 'submit progress_barform0'

    if progress_barform0.accepts(request,session): 
        response.flash0 = 'submitted progress_barform0' 
    elif progress_barform0.errors:
        response.flash0 = '!Errors! progress_barform0' 
    else: 
        response.flash0 = 'progress_barform0' 


    return dict( DICT= rows_dict, progress_barform0= progress_barform0, )

#@auth.requires_login()
def index3():

    qu= db.dindex3.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index3.html'


    index3form0 = SQLFORM(db.dindex3form0, _class = 'au-form-icon--sm', _id= 'idUnk0' )

    index3form0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    index3form0.element('input[name=f0]')['_class']='au-input--w300 au-input--style2'
    index3form0.element('input[name=f0]')['_id']='id478'
    index3form0.custom.submit['_type'] = 'submit'
    index3form0.custom.submit['_class'] = 'au-btn--submit2'
    index3form0.custom.submit['_value'] = 'unk_482'
    index3form0.custom.submit['_id'] = 'id480'
    index3form0.custom.submit['_title'] = 'submit index3form0'

    if index3form0.accepts(request,session): 
        response.flash0 = 'submitted index3form0' 
    elif index3form0.errors:
        response.flash0 = '!Errors! index3form0' 
    else: 
        response.flash0 = 'index3form0' 


    return dict( DICT= rows_dict, index3form0= index3form0, )

#@auth.requires_login()
def modal():

    qu= db.dmodal.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/modal.html'


    modalform0 = SQLFORM(db.dmodalform0, _class = 'form-header', _id= 'idUnk0' )

    modalform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    modalform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    modalform0.element('input[name=f0]')['_id']='id421'
    modalform0.custom.submit['_type'] = 'submit'
    modalform0.custom.submit['_class'] = 'au-btn--submit'
    modalform0.custom.submit['_value'] = 'unk_425'
    modalform0.custom.submit['_id'] = 'id423'
    modalform0.custom.submit['_title'] = 'submit modalform0'

    if modalform0.accepts(request,session): 
        response.flash0 = 'submitted modalform0' 
    elif modalform0.errors:
        response.flash0 = '!Errors! modalform0' 
    else: 
        response.flash0 = 'modalform0' 


    return dict( DICT= rows_dict, modalform0= modalform0, )

#@auth.requires_login()
def forget_pass():

    qu= db.dforget0pass.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/forget-pass.html'


    forget_passform0 = SQLFORM(db.dforget_passform0, _class = 'classUnk0', _id= 'idUnk0' )

    forget_passform0.element('input[name=f0]')['_placeholder']='f0 Email'
    forget_passform0.element('input[name=f0]')['_class']='au-input au-input--full'
    forget_passform0.element('input[name=f0]')['_id']='id427'
    forget_passform0.custom.submit['_type'] = 'submit'
    forget_passform0.custom.submit['_class'] = 'au-btn au-btn--block au-btn--green m-b-20'
    forget_passform0.custom.submit['_value'] = 'submit'
    forget_passform0.custom.submit['_id'] = 'id430'
    forget_passform0.custom.submit['_title'] = 'submit forget_passform0'

    if forget_passform0.accepts(request,session): 
        response.flash0 = 'submitted forget_passform0' 
    elif forget_passform0.errors:
        response.flash0 = '!Errors! forget_passform0' 
    else: 
        response.flash0 = 'forget_passform0' 


    return dict( DICT= rows_dict, forget_passform0= forget_passform0, )

#@auth.requires_login()
def index():

    qu= db.dindex.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index.html'


    indexform0 = SQLFORM(db.dindexform0, _class = 'form-header', _id= 'idUnk0' )

    indexform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    indexform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    indexform0.element('input[name=f0]')['_id']='id458'
    indexform0.custom.submit['_type'] = 'submit'
    indexform0.custom.submit['_class'] = 'au-btn--submit'
    indexform0.custom.submit['_value'] = 'unk_462'
    indexform0.custom.submit['_id'] = 'id460'
    indexform0.custom.submit['_title'] = 'submit indexform0'

    if indexform0.accepts(request,session): 
        response.flash0 = 'submitted indexform0' 
    elif indexform0.errors:
        response.flash0 = '!Errors! indexform0' 
    else: 
        response.flash0 = 'indexform0' 



    indexform1 = SQLFORM(db.dindexform1, _class = 'au-form-icon', _id= 'idUnk1' )

    indexform1.element('input[name=f0]')['_placeholder']='f0 Type a message'
    indexform1.element('input[name=f0]')['_class']='au-input au-input--full au-input--h65'
    indexform1.element('input[name=f0]')['_id']='id464'
    indexform1.custom.submit['_type'] = 'submit'
    indexform1.custom.submit['_class'] = 'au-input-icon'
    indexform1.custom.submit['_value'] = 'unk_468'
    indexform1.custom.submit['_id'] = 'id466'
    indexform1.custom.submit['_title'] = 'submit indexform1'

    if indexform1.accepts(request,session): 
        response.flash1 = 'submitted indexform1' 
    elif indexform1.errors:
        response.flash1 = '!Errors! indexform1' 
    else: 
        response.flash1 = 'indexform1' 


    return dict( DICT= rows_dict, indexform0= indexform0, indexform1= indexform1, )

#@auth.requires_login()
def button():

    qu= db.dbutton.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/button.html'


    buttonform0 = SQLFORM(db.dbuttonform0, _class = 'form-header', _id= 'idUnk0' )

    buttonform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    buttonform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    buttonform0.element('input[name=f0]')['_id']='id80'
    buttonform0.custom.submit['_type'] = 'submit'
    buttonform0.custom.submit['_class'] = 'au-btn--submit'
    buttonform0.custom.submit['_value'] = 'unk_84'
    buttonform0.custom.submit['_id'] = 'id82'
    buttonform0.custom.submit['_title'] = 'submit buttonform0'

    if buttonform0.accepts(request,session): 
        response.flash0 = 'submitted buttonform0' 
    elif buttonform0.errors:
        response.flash0 = '!Errors! buttonform0' 
    else: 
        response.flash0 = 'buttonform0' 


    return dict( DICT= rows_dict, buttonform0= buttonform0, )

#@auth.requires_login()
def table():

    qu= db.dtable.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/table.html'


    tableform0 = SQLFORM(db.dtableform0, _class = 'form-header', _id= 'idUnk0' )

    tableform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    tableform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    tableform0.element('input[name=f0]')['_id']='id68'
    tableform0.custom.submit['_type'] = 'submit'
    tableform0.custom.submit['_class'] = 'au-btn--submit'
    tableform0.custom.submit['_value'] = 'unk_72'
    tableform0.custom.submit['_id'] = 'id70'
    tableform0.custom.submit['_title'] = 'submit tableform0'

    if tableform0.accepts(request,session): 
        response.flash0 = 'submitted tableform0' 
    elif tableform0.errors:
        response.flash0 = '!Errors! tableform0' 
    else: 
        response.flash0 = 'tableform0' 


    return dict( DICT= rows_dict, tableform0= tableform0, )

#@auth.requires_login()
def login():

    qu= db.dlogin.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/login.html'


    loginform0 = SQLFORM(db.dloginform0, _class = 'classUnk0', _id= 'idUnk0' )

    loginform0.element('input[name=f0]')['_placeholder']='f0 Email'
    loginform0.element('input[name=f0]')['_class']='au-input au-input--full'
    loginform0.element('input[name=f0]')['_id']='id44'
    loginform0.element('input[name=f1]')['_placeholder']='f1 Password'
    loginform0.element('input[name=f1]')['_class']='au-input au-input--full'
    loginform0.element('input[name=f1]')['_id']='id47'
    loginform0.element('input[name=f2]')['_placeholder']='f2 place_53'
    loginform0.element('input[name=f2]')['_id']='id50'
    loginform0.custom.submit['_type'] = 'submit'
    loginform0.custom.submit['_class'] = 'au-btn au-btn--block au-btn--green m-b-20'
    loginform0.custom.submit['_value'] = 'sign in'
    loginform0.custom.submit['_id'] = 'id54'
    loginform0.custom.submit['_title'] = 'submit loginform0'
    loginform0.custom.submit['_type'] = 'submit'
    loginform0.custom.submit['_class'] = 'au-btn au-btn--block au-btn--blue m-b-20'
    loginform0.custom.submit['_value'] = 'sign in with facebook'
    loginform0.custom.submit['_id'] = 'id58'
    loginform0.custom.submit['_title'] = 'submit loginform0'
    loginform0.custom.submit['_type'] = 'submit'
    loginform0.custom.submit['_class'] = 'au-btn au-btn--block au-btn--blue2'
    loginform0.custom.submit['_value'] = 'sign in with twitter'
    loginform0.custom.submit['_id'] = 'id61'
    loginform0.custom.submit['_title'] = 'submit loginform0'
    loginform0.custom.submit['_id'] = 'id64'
    loginform0.custom.submit['_title'] = 'submit loginform0'

    if loginform0.accepts(request,session): 
        response.flash0 = 'submitted loginform0' 
    elif loginform0.errors:
        response.flash0 = '!Errors! loginform0' 
    else: 
        response.flash0 = 'loginform0' 


    return dict( DICT= rows_dict, loginform0= loginform0, )

#@auth.requires_login()
def index4():

    qu= db.dindex4.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index4.html'


    index4form0 = SQLFORM(db.dindex4form0, _class = 'form-header form-header2', _id= 'idUnk0' )

    index4form0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    index4form0.element('input[name=f0]')['_class']='au-input au-input--w435'
    index4form0.element('input[name=f0]')['_id']='id385'
    index4form0.custom.submit['_type'] = 'submit'
    index4form0.custom.submit['_class'] = 'au-btn--submit'
    index4form0.custom.submit['_value'] = 'unk_389'
    index4form0.custom.submit['_id'] = 'id387'
    index4form0.custom.submit['_title'] = 'submit index4form0'

    if index4form0.accepts(request,session): 
        response.flash0 = 'submitted index4form0' 
    elif index4form0.errors:
        response.flash0 = '!Errors! index4form0' 
    else: 
        response.flash0 = 'index4form0' 



    index4form1 = SQLFORM(db.dindex4form1, _class = 'au-form-icon', _id= 'idUnk1' )

    index4form1.element('input[name=f0]')['_placeholder']='f0 Type a message'
    index4form1.element('input[name=f0]')['_class']='au-input au-input--full au-input--h65'
    index4form1.element('input[name=f0]')['_id']='id391'
    index4form1.custom.submit['_type'] = 'submit'
    index4form1.custom.submit['_class'] = 'au-input-icon'
    index4form1.custom.submit['_value'] = 'unk_395'
    index4form1.custom.submit['_id'] = 'id393'
    index4form1.custom.submit['_title'] = 'submit index4form1'

    if index4form1.accepts(request,session): 
        response.flash1 = 'submitted index4form1' 
    elif index4form1.errors:
        response.flash1 = '!Errors! index4form1' 
    else: 
        response.flash1 = 'index4form1' 


    return dict( DICT= rows_dict, index4form0= index4form0, index4form1= index4form1, )

#@auth.requires_login()
def grid():

    qu= db.dgrid.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/grid.html'


    gridform0 = SQLFORM(db.dgridform0, _class = 'form-header', _id= 'idUnk0' )

    gridform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    gridform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    gridform0.element('input[name=f0]')['_id']='id440'
    gridform0.custom.submit['_type'] = 'submit'
    gridform0.custom.submit['_class'] = 'au-btn--submit'
    gridform0.custom.submit['_value'] = 'unk_444'
    gridform0.custom.submit['_id'] = 'id442'
    gridform0.custom.submit['_title'] = 'submit gridform0'

    if gridform0.accepts(request,session): 
        response.flash0 = 'submitted gridform0' 
    elif gridform0.errors:
        response.flash0 = '!Errors! gridform0' 
    else: 
        response.flash0 = 'gridform0' 


    return dict( DICT= rows_dict, gridform0= gridform0, )

#@auth.requires_login()
def card():

    qu= db.dcard.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/card.html'


    cardform0 = SQLFORM(db.dcardform0, _class = 'form-header', _id= 'idUnk0' )

    cardform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    cardform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    cardform0.element('input[name=f0]')['_id']='id74'
    cardform0.custom.submit['_type'] = 'submit'
    cardform0.custom.submit['_class'] = 'au-btn--submit'
    cardform0.custom.submit['_value'] = 'unk_78'
    cardform0.custom.submit['_id'] = 'id76'
    cardform0.custom.submit['_title'] = 'submit cardform0'

    if cardform0.accepts(request,session): 
        response.flash0 = 'submitted cardform0' 
    elif cardform0.errors:
        response.flash0 = '!Errors! cardform0' 
    else: 
        response.flash0 = 'cardform0' 


    return dict( DICT= rows_dict, cardform0= cardform0, )

#@auth.requires_login()
def alert():

    qu= db.dalert.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/alert.html'


    alertform0 = SQLFORM(db.dalertform0, _class = 'form-header', _id= 'idUnk0' )

    alertform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    alertform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    alertform0.element('input[name=f0]')['_id']='id373'
    alertform0.custom.submit['_type'] = 'submit'
    alertform0.custom.submit['_class'] = 'au-btn--submit'
    alertform0.custom.submit['_value'] = 'unk_377'
    alertform0.custom.submit['_id'] = 'id375'
    alertform0.custom.submit['_title'] = 'submit alertform0'

    if alertform0.accepts(request,session): 
        response.flash0 = 'submitted alertform0' 
    elif alertform0.errors:
        response.flash0 = '!Errors! alertform0' 
    else: 
        response.flash0 = 'alertform0' 


    return dict( DICT= rows_dict, alertform0= alertform0, )

#@auth.requires_login()
def switch():

    qu= db.dswitch.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/switch.html'


    switchform0 = SQLFORM(db.dswitchform0, _class = 'form-header', _id= 'idUnk0' )

    switchform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    switchform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    switchform0.element('input[name=f0]')['_id']='id470'
    switchform0.custom.submit['_type'] = 'submit'
    switchform0.custom.submit['_class'] = 'au-btn--submit'
    switchform0.custom.submit['_value'] = 'unk_474'
    switchform0.custom.submit['_id'] = 'id472'
    switchform0.custom.submit['_title'] = 'submit switchform0'

    if switchform0.accepts(request,session): 
        response.flash0 = 'submitted switchform0' 
    elif switchform0.errors:
        response.flash0 = '!Errors! switchform0' 
    else: 
        response.flash0 = 'switchform0' 


    return dict( DICT= rows_dict, switchform0= switchform0, )

#@auth.requires_login()
def fontawesome():

    qu= db.dfontawesome.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/fontawesome.html'


    fontawesomeform0 = SQLFORM(db.dfontawesomeform0, _class = 'form-header', _id= 'idUnk0' )

    fontawesomeform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    fontawesomeform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    fontawesomeform0.element('input[name=f0]')['_id']='id452'
    fontawesomeform0.custom.submit['_type'] = 'submit'
    fontawesomeform0.custom.submit['_class'] = 'au-btn--submit'
    fontawesomeform0.custom.submit['_value'] = 'unk_456'
    fontawesomeform0.custom.submit['_id'] = 'id454'
    fontawesomeform0.custom.submit['_title'] = 'submit fontawesomeform0'

    if fontawesomeform0.accepts(request,session): 
        response.flash0 = 'submitted fontawesomeform0' 
    elif fontawesomeform0.errors:
        response.flash0 = '!Errors! fontawesomeform0' 
    else: 
        response.flash0 = 'fontawesomeform0' 


    return dict( DICT= rows_dict, fontawesomeform0= fontawesomeform0, )

#@auth.requires_login()
def badge():

    qu= db.dbadge.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/badge.html'


    badgeform0 = SQLFORM(db.dbadgeform0, _class = 'form-header', _id= 'idUnk0' )

    badgeform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    badgeform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    badgeform0.element('input[name=f0]')['_id']='id15'
    badgeform0.custom.submit['_type'] = 'submit'
    badgeform0.custom.submit['_class'] = 'au-btn--submit'
    badgeform0.custom.submit['_value'] = 'unk_19'
    badgeform0.custom.submit['_id'] = 'id17'
    badgeform0.custom.submit['_title'] = 'submit badgeform0'

    if badgeform0.accepts(request,session): 
        response.flash0 = 'submitted badgeform0' 
    elif badgeform0.errors:
        response.flash0 = '!Errors! badgeform0' 
    else: 
        response.flash0 = 'badgeform0' 


    return dict( DICT= rows_dict, badgeform0= badgeform0, )

#@auth.requires_login()
def map():

    qu= db.dmap.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/map.html'


    mapform0 = SQLFORM(db.dmapform0, _class = 'form-header', _id= 'idUnk0' )

    mapform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    mapform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    mapform0.element('input[name=f0]')['_id']='id446'
    mapform0.custom.submit['_type'] = 'submit'
    mapform0.custom.submit['_class'] = 'au-btn--submit'
    mapform0.custom.submit['_value'] = 'unk_450'
    mapform0.custom.submit['_id'] = 'id448'
    mapform0.custom.submit['_title'] = 'submit mapform0'

    if mapform0.accepts(request,session): 
        response.flash0 = 'submitted mapform0' 
    elif mapform0.errors:
        response.flash0 = '!Errors! mapform0' 
    else: 
        response.flash0 = 'mapform0' 


    return dict( DICT= rows_dict, mapform0= mapform0, )

#@auth.requires_login()
def form():

    qu= db.dform.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/form.html'


    formform0 = SQLFORM(db.dformform0, _class = 'form-header', _id= 'idUnk0' )

    formform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    formform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    formform0.element('input[name=f0]')['_id']='id86'
    formform0.custom.submit['_type'] = 'submit'
    formform0.custom.submit['_class'] = 'au-btn--submit'
    formform0.custom.submit['_value'] = 'unk_90'
    formform0.custom.submit['_id'] = 'id88'
    formform0.custom.submit['_title'] = 'submit formform0'

    if formform0.accepts(request,session): 
        response.flash0 = 'submitted formform0' 
    elif formform0.errors:
        response.flash0 = '!Errors! formform0' 
    else: 
        response.flash0 = 'formform0' 



    formform1 = SQLFORM(db.dformform1, _class = 'classUnk1', _id= 'idUnk1' )

    formform1.element('input[name=f0]')['_placeholder']='f0 place_94'
    formform1.element('input[name=f0]')['_id']='cc-pament'
    formform1.element('input[name=f0]')['_value']='100.00'
    formform1.element('input[name=f0]')['_class']='form-control'
    formform1.element('input[name=f1]')['_placeholder']='f1 place_97'
    formform1.element('input[name=f1]')['_id']='cc-name'
    formform1.element('input[name=f1]')['_class']='form-control cc-name valid'
    formform1.element('input[name=f2]')['_placeholder']='f2 place_101'
    formform1.element('input[name=f2]')['_id']='cc-number'
    formform1.element('input[name=f2]')['_value']='unk_100'
    formform1.element('input[name=f2]')['_class']='form-control cc-number identified visa'
    formform1.element('input[name=f3]')['_placeholder']='f3 MM / YY'
    formform1.element('input[name=f3]')['_id']='cc-exp'
    formform1.element('input[name=f3]')['_value']='unk_104'
    formform1.element('input[name=f3]')['_class']='form-control cc-exp'
    formform1.element('input[name=f4]')['_placeholder']='f4 place_108'
    formform1.element('input[name=f4]')['_id']='x_card_code'
    formform1.element('input[name=f4]')['_value']='unk_107'
    formform1.element('input[name=f4]')['_class']='form-control cc-cvc'
    formform1.custom.submit['_type'] = 'submit'
    formform1.custom.submit['_id'] = 'payment-button'
    formform1.custom.submit['_value'] = 'Pay $100.00 Sending'
    formform1.custom.submit['_class'] = 'btn btn-lg btn-info btn-block'
    formform1.custom.submit['_title'] = 'submit formform1'

    if formform1.accepts(request,session): 
        response.flash1 = 'submitted formform1' 
    elif formform1.errors:
        response.flash1 = '!Errors! formform1' 
    else: 
        response.flash1 = 'formform1' 



    formform2 = SQLFORM(db.dformform2, _class = 'form-horizontal', _id= 'idUnk2' )

    formform2.element('input[name=f0]')['_placeholder']='f0 Text'
    formform2.element('input[name=f0]')['_id']='text-input'
    formform2.element('input[name=f0]')['_class']='form-control'
    formform2.element('input[name=f1]')['_placeholder']='f1 Enter Email'
    formform2.element('input[name=f1]')['_id']='email-input'
    formform2.element('input[name=f1]')['_class']='form-control'
    formform2.element('input[name=f2]')['_placeholder']='f2 Password'
    formform2.element('input[name=f2]')['_id']='password-input'
    formform2.element('input[name=f2]')['_class']='form-control'
    formform2.element('input[name=f3]')['_placeholder']='f3 Disabled'
    formform2.element('input[name=f3]')['_id']='disabled-input'
    formform2.element('input[name=f3]')['_class']='form-control'
    formform2.element('input[name=f10]')['_placeholder']='f10 place_134'
    formform2.element('input[name=f10]')['_id']='checkbox1'
    formform2.element('input[name=f10]')['_value']='option1'
    formform2.element('input[name=f10]')['_class']='form-check-input'
    formform2.element('input[name=f11]')['_placeholder']='f11 place_137'
    formform2.element('input[name=f11]')['_id']='checkbox2'
    formform2.element('input[name=f11]')['_value']='option2'
    formform2.element('input[name=f11]')['_class']='form-check-input'
    formform2.element('input[name=f12]')['_placeholder']='f12 place_140'
    formform2.element('input[name=f12]')['_id']='checkbox3'
    formform2.element('input[name=f12]')['_value']='option3'
    formform2.element('input[name=f12]')['_class']='form-check-input'
    formform2.element('input[name=f13]')['_placeholder']='f13 place_143'
    formform2.element('input[name=f13]')['_id']='inline-checkbox1'
    formform2.element('input[name=f13]')['_value']='option1'
    formform2.element('input[name=f13]')['_class']='form-check-input'
    formform2.element('input[name=f14]')['_placeholder']='f14 place_146'
    formform2.element('input[name=f14]')['_id']='inline-checkbox2'
    formform2.element('input[name=f14]')['_value']='option2'
    formform2.element('input[name=f14]')['_class']='form-check-input'
    formform2.element('input[name=f15]')['_placeholder']='f15 place_149'
    formform2.element('input[name=f15]')['_id']='inline-checkbox3'
    formform2.element('input[name=f15]')['_value']='option3'
    formform2.element('input[name=f15]')['_class']='form-check-input'
    formform2.element('input[name=f16]')['_placeholder']='f16 place_152'
    formform2.element('input[name=f16]')['_id']='file-input'
    formform2.element('input[name=f16]')['_class']='form-control-file'
    formform2.element('input[name=f17]')['_placeholder']='f17 place_155'
    formform2.element('input[name=f17]')['_id']='file-multiple-input'
    formform2.element('input[name=f17]')['_class']='form-control-file'
    formform2.element('textarea[name=f18]')['_rows']='9'
    formform2.element('textarea[name=f18]')['_placeholder']='f18 Content...'
    formform2.element('textarea[name=f18]')['_id']='textarea-input'
    formform2.element('textarea[name=f18]')['_class']='form-control'
    formform2.custom.submit['_type'] = 'submit'
    formform2.custom.submit['_id'] = 'unk-id'
    formform2.custom.submit['_value'] = 'submit input'
    formform2.custom.submit['_class'] = 'unk-class'
    formform2.custom.submit['_title'] = 'submit formform2'

    if formform2.accepts(request,session): 
        response.flash2 = 'submitted formform2' 
    elif formform2.errors:
        response.flash2 = '!Errors! formform2' 
    else: 
        response.flash2 = 'formform2' 



    formform3 = SQLFORM(db.dformform3, _class = 'form-inline', _id= 'idUnk3' )

    formform3.element('input[name=f0]')['_placeholder']='f0 Jane Doe'
    formform3.element('input[name=f0]')['_id']='exampleInputName2'
    formform3.element('input[name=f0]')['_class']='form-control'
    formform3.element('input[name=f1]')['_placeholder']='f1 jane.doe@example.com'
    formform3.element('input[name=f1]')['_id']='exampleInputEmail2'
    formform3.element('input[name=f1]')['_class']='form-control'
    formform3.custom.submit['_type'] = 'submit'
    formform3.custom.submit['_id'] = 'unk-id'
    formform3.custom.submit['_value'] = 'submit input'
    formform3.custom.submit['_class'] = 'unk-class'
    formform3.custom.submit['_title'] = 'submit formform3'

    if formform3.accepts(request,session): 
        response.flash3 = 'submitted formform3' 
    elif formform3.errors:
        response.flash3 = '!Errors! formform3' 
    else: 
        response.flash3 = 'formform3' 



    formform4 = SQLFORM(db.dformform4, _class = 'form-horizontal', _id= 'idUnk4' )

    formform4.element('input[name=f0]')['_placeholder']='f0 Enter Email...'
    formform4.element('input[name=f0]')['_id']='hf-email'
    formform4.element('input[name=f0]')['_class']='form-control'
    formform4.element('input[name=f1]')['_placeholder']='f1 Enter Password...'
    formform4.element('input[name=f1]')['_id']='hf-password'
    formform4.element('input[name=f1]')['_class']='form-control'
    formform4.custom.submit['_type'] = 'submit'
    formform4.custom.submit['_id'] = 'unk-id'
    formform4.custom.submit['_value'] = 'submit input'
    formform4.custom.submit['_class'] = 'unk-class'
    formform4.custom.submit['_title'] = 'submit formform4'

    if formform4.accepts(request,session): 
        response.flash4 = 'submitted formform4' 
    elif formform4.errors:
        response.flash4 = '!Errors! formform4' 
    else: 
        response.flash4 = 'formform4' 



    formform5 = SQLFORM(db.dformform5, _class = '', _id= 'idUnk5' )

    formform5.element('input[name=f0]')['_placeholder']='f0 Enter Email..'
    formform5.element('input[name=f0]')['_id']='nf-email'
    formform5.element('input[name=f0]')['_class']='form-control'
    formform5.element('input[name=f1]')['_placeholder']='f1 Enter Password..'
    formform5.element('input[name=f1]')['_id']='nf-password'
    formform5.element('input[name=f1]')['_class']='form-control'
    formform5.custom.submit['_type'] = 'submit'
    formform5.custom.submit['_id'] = 'unk-id'
    formform5.custom.submit['_value'] = 'submit input'
    formform5.custom.submit['_class'] = 'unk-class'
    formform5.custom.submit['_title'] = 'submit formform5'

    if formform5.accepts(request,session): 
        response.flash5 = 'submitted formform5' 
    elif formform5.errors:
        response.flash5 = '!Errors! formform5' 
    else: 
        response.flash5 = 'formform5' 



    formform6 = SQLFORM(db.dformform6, _class = 'form-horizontal', _id= 'idUnk6' )

    formform6.element('input[name=f0]')['_placeholder']='f0 .col-sm-3'
    formform6.element('input[name=f0]')['_class']='form-control'
    formform6.element('input[name=f0]')['_id']='id185'
    formform6.element('input[name=f1]')['_placeholder']='f1 .col-sm-4'
    formform6.element('input[name=f1]')['_class']='form-control'
    formform6.element('input[name=f1]')['_id']='id187'
    formform6.element('input[name=f2]')['_placeholder']='f2 .col-sm-5'
    formform6.element('input[name=f2]')['_class']='form-control'
    formform6.element('input[name=f2]')['_id']='id189'
    formform6.element('input[name=f3]')['_placeholder']='f3 .col-sm-6'
    formform6.element('input[name=f3]')['_class']='form-control'
    formform6.element('input[name=f3]')['_id']='id191'
    formform6.element('input[name=f4]')['_placeholder']='f4 .col-sm-7'
    formform6.element('input[name=f4]')['_class']='form-control'
    formform6.element('input[name=f4]')['_id']='id193'
    formform6.element('input[name=f5]')['_placeholder']='f5 .col-sm-8'
    formform6.element('input[name=f5]')['_class']='form-control'
    formform6.element('input[name=f5]')['_id']='id195'
    formform6.element('input[name=f6]')['_placeholder']='f6 .col-sm-9'
    formform6.element('input[name=f6]')['_class']='form-control'
    formform6.element('input[name=f6]')['_id']='id197'
    formform6.element('input[name=f7]')['_placeholder']='f7 .col-sm-10'
    formform6.element('input[name=f7]')['_class']='form-control'
    formform6.element('input[name=f7]')['_id']='id199'
    formform6.element('input[name=f8]')['_placeholder']='f8 .col-sm-11'
    formform6.element('input[name=f8]')['_class']='form-control'
    formform6.element('input[name=f8]')['_id']='id201'
    formform6.element('input[name=f9]')['_placeholder']='f9 .col-sm-12'
    formform6.element('input[name=f9]')['_class']='form-control'
    formform6.element('input[name=f9]')['_id']='id203'
    formform6.custom.submit['_type'] = 'submit'
    formform6.custom.submit['_class'] = 'unk-class'
    formform6.custom.submit['_value'] = 'submit input'
    formform6.custom.submit['_id'] = 'unk-id'
    formform6.custom.submit['_title'] = 'submit formform6'

    if formform6.accepts(request,session): 
        response.flash6 = 'submitted formform6' 
    elif formform6.errors:
        response.flash6 = '!Errors! formform6' 
    else: 
        response.flash6 = 'formform6' 



    formform7 = SQLFORM(db.dformform7, _class = 'form-horizontal', _id= 'idUnk7' )

    formform7.element('input[name=f0]')['_placeholder']='f0 .form-control-sm'
    formform7.element('input[name=f0]')['_id']='input-small'
    formform7.element('input[name=f0]')['_class']='input-sm form-control-sm form-control'
    formform7.element('input[name=f1]')['_placeholder']='f1 Normal'
    formform7.element('input[name=f1]')['_id']='input-normal'
    formform7.element('input[name=f1]')['_class']='form-control'
    formform7.element('input[name=f2]')['_placeholder']='f2 .form-control-lg'
    formform7.element('input[name=f2]')['_id']='input-large'
    formform7.element('input[name=f2]')['_class']='input-lg form-control-lg form-control'
    formform7.custom.submit['_type'] = 'submit'
    formform7.custom.submit['_id'] = 'unk-id'
    formform7.custom.submit['_value'] = 'submit input'
    formform7.custom.submit['_class'] = 'unk-class'
    formform7.custom.submit['_title'] = 'submit formform7'

    if formform7.accepts(request,session): 
        response.flash7 = 'submitted formform7' 
    elif formform7.errors:
        response.flash7 = '!Errors! formform7' 
    else: 
        response.flash7 = 'formform7' 



    formform8 = SQLFORM(db.dformform8, _class = 'form-horizontal', _id= 'idUnk8' )

    formform8.element('input[name=f0]')['_placeholder']='f0 Username'
    formform8.element('input[name=f0]')['_id']='input1-group1'
    formform8.element('input[name=f0]')['_class']='form-control'
    formform8.element('input[name=f1]')['_placeholder']='f1 Email'
    formform8.element('input[name=f1]')['_id']='input2-group1'
    formform8.element('input[name=f1]')['_class']='form-control'
    formform8.element('input[name=f2]')['_placeholder']='f2 ..'
    formform8.element('input[name=f2]')['_id']='input3-group1'
    formform8.element('input[name=f2]')['_class']='form-control'
    formform8.custom.submit['_type'] = 'submit'
    formform8.custom.submit['_id'] = 'unk-id'
    formform8.custom.submit['_value'] = 'submit input'
    formform8.custom.submit['_class'] = 'unk-class'
    formform8.custom.submit['_title'] = 'submit formform8'

    if formform8.accepts(request,session): 
        response.flash8 = 'submitted formform8' 
    elif formform8.errors:
        response.flash8 = '!Errors! formform8' 
    else: 
        response.flash8 = 'formform8' 



    formform9 = SQLFORM(db.dformform9, _class = 'form-horizontal', _id= 'idUnk9' )

    formform9.element('input[name=f0]')['_placeholder']='f0 Username'
    formform9.element('input[name=f0]')['_id']='input1-group2'
    formform9.element('input[name=f0]')['_class']='form-control'
    formform9.element('input[name=f1]')['_placeholder']='f1 Email'
    formform9.element('input[name=f1]')['_id']='input2-group2'
    formform9.element('input[name=f1]')['_class']='form-control'
    formform9.element('input[name=f2]')['_placeholder']='f2 Search'
    formform9.element('input[name=f2]')['_id']='input3-group2'
    formform9.element('input[name=f2]')['_class']='form-control'
    formform9.custom.submit['_type'] = 'submit'
    formform9.custom.submit['_class'] = 'btn btn-primary'
    formform9.custom.submit['_value'] = 'Search'
    formform9.custom.submit['_id'] = 'id223'
    formform9.custom.submit['_title'] = 'submit formform9'
    formform9.custom.submit['_type'] = 'submit'
    formform9.custom.submit['_class'] = 'btn btn-primary'
    formform9.custom.submit['_value'] = 'Submit'
    formform9.custom.submit['_id'] = 'id226'
    formform9.custom.submit['_title'] = 'submit formform9'
    formform9.custom.submit['_type'] = 'submit'
    formform9.custom.submit['_class'] = 'btn btn-primary'
    formform9.custom.submit['_value'] = 'unk_231'
    formform9.custom.submit['_id'] = 'id229'
    formform9.custom.submit['_title'] = 'submit formform9'
    formform9.custom.submit['_type'] = 'submit'
    formform9.custom.submit['_class'] = 'btn btn-primary'
    formform9.custom.submit['_value'] = 'unk_235'
    formform9.custom.submit['_id'] = 'id233'
    formform9.custom.submit['_title'] = 'submit formform9'

    if formform9.accepts(request,session): 
        response.flash9 = 'submitted formform9' 
    elif formform9.errors:
        response.flash9 = '!Errors! formform9' 
    else: 
        response.flash9 = 'formform9' 



    formform10 = SQLFORM(db.dformform10, _class = 'form-horizontal', _id= 'idUnk10' )

    formform10.element('input[name=f0]')['_placeholder']='f0 Username'
    formform10.element('input[name=f0]')['_id']='input1-group3'
    formform10.element('input[name=f0]')['_class']='form-control'
    formform10.element('input[name=f1]')['_placeholder']='f1 Email'
    formform10.element('input[name=f1]')['_id']='input2-group3'
    formform10.element('input[name=f1]')['_class']='form-control'
    formform10.element('input[name=f2]')['_placeholder']='f2 ..'
    formform10.element('input[name=f2]')['_id']='input3-group3'
    formform10.element('input[name=f2]')['_class']='form-control'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-toggle btn btn-primary'
    formform10.custom.submit['_value'] = 'Dropdown'
    formform10.custom.submit['_id'] = 'id243'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Action'
    formform10.custom.submit['_id'] = 'id246'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Another Action'
    formform10.custom.submit['_id'] = 'id249'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Something else here'
    formform10.custom.submit['_id'] = 'id252'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Separated link'
    formform10.custom.submit['_id'] = 'id255'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-toggle btn btn-primary'
    formform10.custom.submit['_value'] = 'Dropdown'
    formform10.custom.submit['_id'] = 'id258'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Action'
    formform10.custom.submit['_id'] = 'id261'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Another Action'
    formform10.custom.submit['_id'] = 'id264'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Something else here'
    formform10.custom.submit['_id'] = 'id267'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Separated link'
    formform10.custom.submit['_id'] = 'id270'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-toggle btn btn-primary'
    formform10.custom.submit['_value'] = 'Action'
    formform10.custom.submit['_id'] = 'id273'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Action'
    formform10.custom.submit['_id'] = 'id276'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Another Action'
    formform10.custom.submit['_id'] = 'id279'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Something else here'
    formform10.custom.submit['_id'] = 'id282'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Separated link'
    formform10.custom.submit['_id'] = 'id285'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-toggle btn btn-primary'
    formform10.custom.submit['_value'] = 'Dropdown'
    formform10.custom.submit['_id'] = 'id288'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Action'
    formform10.custom.submit['_id'] = 'id291'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Another Action'
    formform10.custom.submit['_id'] = 'id294'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Something else here'
    formform10.custom.submit['_id'] = 'id297'
    formform10.custom.submit['_title'] = 'submit formform10'
    formform10.custom.submit['_type'] = 'submit'
    formform10.custom.submit['_class'] = 'dropdown-item'
    formform10.custom.submit['_value'] = 'Separated link'
    formform10.custom.submit['_id'] = 'id300'
    formform10.custom.submit['_title'] = 'submit formform10'

    if formform10.accepts(request,session): 
        response.flash10 = 'submitted formform10' 
    elif formform10.errors:
        response.flash10 = '!Errors! formform10' 
    else: 
        response.flash10 = 'formform10' 



    formform11 = SQLFORM(db.dformform11, _class = 'form-horizontal', _id= 'idUnk11' )

    formform11.element('input[name=f0]')['_placeholder']='f0 .col-md-8'
    formform11.element('input[name=f0]')['_class']='form-control'
    formform11.element('input[name=f0]')['_id']='id303'
    formform11.element('input[name=f1]')['_placeholder']='f1 .col-md-4'
    formform11.element('input[name=f1]')['_class']='form-control'
    formform11.element('input[name=f1]')['_id']='id305'
    formform11.element('input[name=f2]')['_placeholder']='f2 .col-md-7'
    formform11.element('input[name=f2]')['_class']='form-control'
    formform11.element('input[name=f2]')['_id']='id307'
    formform11.element('input[name=f3]')['_placeholder']='f3 .col-md-5'
    formform11.element('input[name=f3]')['_class']='form-control'
    formform11.element('input[name=f3]')['_id']='id309'
    formform11.element('input[name=f4]')['_placeholder']='f4 .col-md-6'
    formform11.element('input[name=f4]')['_class']='form-control'
    formform11.element('input[name=f4]')['_id']='id311'
    formform11.element('input[name=f5]')['_placeholder']='f5 .col-md-6'
    formform11.element('input[name=f5]')['_class']='form-control'
    formform11.element('input[name=f5]')['_id']='id313'
    formform11.element('input[name=f6]')['_placeholder']='f6 .col-md-5'
    formform11.element('input[name=f6]')['_class']='form-control'
    formform11.element('input[name=f6]')['_id']='id315'
    formform11.element('input[name=f7]')['_placeholder']='f7 .col-md-7'
    formform11.element('input[name=f7]')['_class']='form-control'
    formform11.element('input[name=f7]')['_id']='id317'
    formform11.element('input[name=f8]')['_placeholder']='f8 .col-md-4'
    formform11.element('input[name=f8]')['_class']='form-control'
    formform11.element('input[name=f8]')['_id']='id319'
    formform11.element('input[name=f9]')['_placeholder']='f9 .col-md-8'
    formform11.element('input[name=f9]')['_class']='form-control'
    formform11.element('input[name=f9]')['_id']='id321'
    formform11.custom.submit['_type'] = 'submit'
    formform11.custom.submit['_class'] = 'unk-class'
    formform11.custom.submit['_value'] = 'submit input'
    formform11.custom.submit['_id'] = 'unk-id'
    formform11.custom.submit['_title'] = 'submit formform11'

    if formform11.accepts(request,session): 
        response.flash11 = 'submitted formform11' 
    elif formform11.errors:
        response.flash11 = '!Errors! formform11' 
    else: 
        response.flash11 = 'formform11' 



    formform12 = SQLFORM(db.dformform12, _class = 'form-horizontal', _id= 'idUnk12' )

    formform12.element('input[name=f0]')['_placeholder']='f0 .col-4'
    formform12.element('input[name=f0]')['_class']='form-control'
    formform12.element('input[name=f0]')['_id']='id323'
    formform12.element('input[name=f1]')['_placeholder']='f1 .col-8'
    formform12.element('input[name=f1]')['_class']='form-control'
    formform12.element('input[name=f1]')['_id']='id325'
    formform12.element('input[name=f2]')['_placeholder']='f2 .col-5'
    formform12.element('input[name=f2]')['_class']='form-control'
    formform12.element('input[name=f2]')['_id']='id327'
    formform12.element('input[name=f3]')['_placeholder']='f3 .col-7'
    formform12.element('input[name=f3]')['_class']='form-control'
    formform12.element('input[name=f3]')['_id']='id329'
    formform12.element('input[name=f4]')['_placeholder']='f4 .col-6'
    formform12.element('input[name=f4]')['_class']='form-control'
    formform12.element('input[name=f4]')['_id']='id331'
    formform12.element('input[name=f5]')['_placeholder']='f5 .col-6'
    formform12.element('input[name=f5]')['_class']='form-control'
    formform12.element('input[name=f5]')['_id']='id333'
    formform12.element('input[name=f6]')['_placeholder']='f6 .col-5'
    formform12.element('input[name=f6]')['_class']='form-control'
    formform12.element('input[name=f6]')['_id']='id335'
    formform12.element('input[name=f7]')['_placeholder']='f7 .col-5'
    formform12.element('input[name=f7]')['_class']='form-control'
    formform12.element('input[name=f7]')['_id']='id337'
    formform12.element('input[name=f8]')['_placeholder']='f8 .col-8'
    formform12.element('input[name=f8]')['_class']='form-control'
    formform12.element('input[name=f8]')['_id']='id339'
    formform12.element('input[name=f9]')['_placeholder']='f9 .col-4'
    formform12.element('input[name=f9]')['_class']='form-control'
    formform12.element('input[name=f9]')['_id']='id341'
    formform12.custom.submit['_type'] = 'submit'
    formform12.custom.submit['_class'] = 'unk-class'
    formform12.custom.submit['_value'] = 'submit input'
    formform12.custom.submit['_id'] = 'unk-id'
    formform12.custom.submit['_title'] = 'submit formform12'

    if formform12.accepts(request,session): 
        response.flash12 = 'submitted formform12' 
    elif formform12.errors:
        response.flash12 = '!Errors! formform12' 
    else: 
        response.flash12 = 'formform12' 



    formform13 = SQLFORM(db.dformform13, _class = '', _id= 'idUnk13' )

    formform13.element('input[name=f0]')['_placeholder']='f0 place_345'
    formform13.element('input[name=f0]')['_id']='username3'
    formform13.element('input[name=f0]')['_class']='form-control'
    formform13.element('input[name=f1]')['_placeholder']='f1 place_348'
    formform13.element('input[name=f1]')['_id']='email3'
    formform13.element('input[name=f1]')['_class']='form-control'
    formform13.element('input[name=f2]')['_placeholder']='f2 place_351'
    formform13.element('input[name=f2]')['_id']='password3'
    formform13.element('input[name=f2]')['_class']='form-control'
    formform13.custom.submit['_type'] = 'submit'
    formform13.custom.submit['_class'] = 'btn btn-primary btn-sm'
    formform13.custom.submit['_value'] = 'Submit'
    formform13.custom.submit['_id'] = 'id352'
    formform13.custom.submit['_title'] = 'submit formform13'

    if formform13.accepts(request,session): 
        response.flash13 = 'submitted formform13' 
    elif formform13.errors:
        response.flash13 = '!Errors! formform13' 
    else: 
        response.flash13 = 'formform13' 



    formform14 = SQLFORM(db.dformform14, _class = '', _id= 'idUnk14' )

    formform14.element('input[name=f0]')['_placeholder']='f0 Username'
    formform14.element('input[name=f0]')['_id']='username2'
    formform14.element('input[name=f0]')['_class']='form-control'
    formform14.element('input[name=f1]')['_placeholder']='f1 Email'
    formform14.element('input[name=f1]')['_id']='email2'
    formform14.element('input[name=f1]')['_class']='form-control'
    formform14.element('input[name=f2]')['_placeholder']='f2 Password'
    formform14.element('input[name=f2]')['_id']='password2'
    formform14.element('input[name=f2]')['_class']='form-control'
    formform14.custom.submit['_type'] = 'submit'
    formform14.custom.submit['_class'] = 'btn btn-secondary btn-sm'
    formform14.custom.submit['_value'] = 'Submit'
    formform14.custom.submit['_id'] = 'id361'
    formform14.custom.submit['_title'] = 'submit formform14'

    if formform14.accepts(request,session): 
        response.flash14 = 'submitted formform14' 
    elif formform14.errors:
        response.flash14 = '!Errors! formform14' 
    else: 
        response.flash14 = 'formform14' 



    formform15 = SQLFORM(db.dformform15, _class = '', _id= 'idUnk15' )

    formform15.element('input[name=f0]')['_placeholder']='f0 Username'
    formform15.element('input[name=f0]')['_id']='username'
    formform15.element('input[name=f0]')['_class']='form-control'
    formform15.element('input[name=f1]')['_placeholder']='f1 Email'
    formform15.element('input[name=f1]')['_id']='email'
    formform15.element('input[name=f1]')['_class']='form-control'
    formform15.element('input[name=f2]')['_placeholder']='f2 Password'
    formform15.element('input[name=f2]')['_id']='password'
    formform15.element('input[name=f2]')['_class']='form-control'
    formform15.custom.submit['_type'] = 'submit'
    formform15.custom.submit['_class'] = 'btn btn-success btn-sm'
    formform15.custom.submit['_value'] = 'Submit'
    formform15.custom.submit['_id'] = 'id370'
    formform15.custom.submit['_title'] = 'submit formform15'

    if formform15.accepts(request,session): 
        response.flash15 = 'submitted formform15' 
    elif formform15.errors:
        response.flash15 = '!Errors! formform15' 
    else: 
        response.flash15 = 'formform15' 


    return dict( DICT= rows_dict, formform0= formform0, formform1= formform1, formform2= formform2, formform3= formform3, formform4= formform4, formform5= formform5, formform6= formform6, formform7= formform7, formform8= formform8, formform9= formform9, formform10= formform10, formform11= formform11, formform12= formform12, formform13= formform13, formform14= formform14, formform15= formform15, )

#@auth.requires_login()
def register():

    qu= db.dregister.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/register.html'


    registerform0 = SQLFORM(db.dregisterform0, _class = 'classUnk0', _id= 'idUnk0' )

    registerform0.element('input[name=f0]')['_placeholder']='f0 Username'
    registerform0.element('input[name=f0]')['_class']='au-input au-input--full'
    registerform0.element('input[name=f0]')['_id']='id21'
    registerform0.element('input[name=f1]')['_placeholder']='f1 Email'
    registerform0.element('input[name=f1]')['_class']='au-input au-input--full'
    registerform0.element('input[name=f1]')['_id']='id24'
    registerform0.element('input[name=f2]')['_placeholder']='f2 Password'
    registerform0.element('input[name=f2]')['_class']='au-input au-input--full'
    registerform0.element('input[name=f2]')['_id']='id27'
    registerform0.element('input[name=f3]')['_placeholder']='f3 place_33'
    registerform0.element('input[name=f3]')['_id']='id30'
    registerform0.custom.submit['_type'] = 'submit'
    registerform0.custom.submit['_class'] = 'au-btn au-btn--block au-btn--green m-b-20'
    registerform0.custom.submit['_value'] = 'register'
    registerform0.custom.submit['_id'] = 'id34'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.custom.submit['_type'] = 'submit'
    registerform0.custom.submit['_class'] = 'au-btn au-btn--block au-btn--blue m-b-20'
    registerform0.custom.submit['_value'] = 'register with facebook'
    registerform0.custom.submit['_id'] = 'id38'
    registerform0.custom.submit['_title'] = 'submit registerform0'
    registerform0.custom.submit['_type'] = 'submit'
    registerform0.custom.submit['_class'] = 'au-btn au-btn--block au-btn--blue2'
    registerform0.custom.submit['_value'] = 'register with twitter'
    registerform0.custom.submit['_id'] = 'id41'
    registerform0.custom.submit['_title'] = 'submit registerform0'

    if registerform0.accepts(request,session): 
        response.flash0 = 'submitted registerform0' 
    elif registerform0.errors:
        response.flash0 = '!Errors! registerform0' 
    else: 
        response.flash0 = 'registerform0' 


    return dict( DICT= rows_dict, registerform0= registerform0, )

#@auth.requires_login()
def inbox():

    qu= db.dinbox.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/inbox.html'


    inboxform0 = SQLFORM(db.dinboxform0, _class = 'form-header', _id= 'idUnk0' )

    inboxform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    inboxform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    inboxform0.element('input[name=f0]')['_id']='id403'
    inboxform0.custom.submit['_type'] = 'submit'
    inboxform0.custom.submit['_class'] = 'au-btn--submit'
    inboxform0.custom.submit['_value'] = 'unk_407'
    inboxform0.custom.submit['_id'] = 'id405'
    inboxform0.custom.submit['_title'] = 'submit inboxform0'

    if inboxform0.accepts(request,session): 
        response.flash0 = 'submitted inboxform0' 
    elif inboxform0.errors:
        response.flash0 = '!Errors! inboxform0' 
    else: 
        response.flash0 = 'inboxform0' 



    inboxform1 = SQLFORM(db.dinboxform1, _class = 'au-form-icon', _id= 'idUnk1' )

    inboxform1.element('input[name=f0]')['_placeholder']='f0 Type a message'
    inboxform1.element('input[name=f0]')['_class']='au-input au-input--full au-input--h65'
    inboxform1.element('input[name=f0]')['_id']='id409'
    inboxform1.custom.submit['_type'] = 'submit'
    inboxform1.custom.submit['_class'] = 'au-input-icon'
    inboxform1.custom.submit['_value'] = 'unk_413'
    inboxform1.custom.submit['_id'] = 'id411'
    inboxform1.custom.submit['_title'] = 'submit inboxform1'

    if inboxform1.accepts(request,session): 
        response.flash1 = 'submitted inboxform1' 
    elif inboxform1.errors:
        response.flash1 = '!Errors! inboxform1' 
    else: 
        response.flash1 = 'inboxform1' 



    inboxform2 = SQLFORM(db.dinboxform2, _class = 'au-form-icon', _id= 'idUnk2' )

    inboxform2.element('input[name=f0]')['_placeholder']='f0 Type a message'
    inboxform2.element('input[name=f0]')['_class']='au-input au-input--full au-input--h65'
    inboxform2.element('input[name=f0]')['_id']='id415'
    inboxform2.custom.submit['_type'] = 'submit'
    inboxform2.custom.submit['_class'] = 'au-input-icon'
    inboxform2.custom.submit['_value'] = 'unk_419'
    inboxform2.custom.submit['_id'] = 'id417'
    inboxform2.custom.submit['_title'] = 'submit inboxform2'

    if inboxform2.accepts(request,session): 
        response.flash2 = 'submitted inboxform2' 
    elif inboxform2.errors:
        response.flash2 = '!Errors! inboxform2' 
    else: 
        response.flash2 = 'inboxform2' 


    return dict( DICT= rows_dict, inboxform0= inboxform0, inboxform1= inboxform1, inboxform2= inboxform2, )

#@auth.requires_login()
def index2():

    qu= db.dindex2.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index2.html'


    index2form0 = SQLFORM(db.dindex2form0, _class = 'classUnk0', _id= 'idUnk0' )

    index2form0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    index2form0.element('input[name=f0]')['_class']='au-input au-input--full au-input--h65'
    index2form0.element('input[name=f0]')['_id']='id476'
    index2form0.custom.submit['_type'] = 'submit'
    index2form0.custom.submit['_class'] = 'unk-class'
    index2form0.custom.submit['_value'] = 'submit input'
    index2form0.custom.submit['_id'] = 'unk-id'
    index2form0.custom.submit['_title'] = 'submit index2form0'

    if index2form0.accepts(request,session): 
        response.flash0 = 'submitted index2form0' 
    elif index2form0.errors:
        response.flash0 = '!Errors! index2form0' 
    else: 
        response.flash0 = 'index2form0' 


    return dict( DICT= rows_dict, index2form0= index2form0, )

#@auth.requires_login()
def chart():

    qu= db.dchart.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/chart.html'


    chartform0 = SQLFORM(db.dchartform0, _class = 'form-header', _id= 'idUnk0' )

    chartform0.element('input[name=f0]')['_placeholder']='f0 Search for datas & reports...'
    chartform0.element('input[name=f0]')['_class']='au-input au-input--xl'
    chartform0.element('input[name=f0]')['_id']='id484'
    chartform0.custom.submit['_type'] = 'submit'
    chartform0.custom.submit['_class'] = 'au-btn--submit'
    chartform0.custom.submit['_value'] = 'unk_488'
    chartform0.custom.submit['_id'] = 'id486'
    chartform0.custom.submit['_title'] = 'submit chartform0'

    if chartform0.accepts(request,session): 
        response.flash0 = 'submitted chartform0' 
    elif chartform0.errors:
        response.flash0 = '!Errors! chartform0' 
    else: 
        response.flash0 = 'chartform0' 


    return dict( DICT= rows_dict, chartform0= chartform0, )