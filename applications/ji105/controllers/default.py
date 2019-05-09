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
def form_components():

    qu= db.dform0components.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/form-components.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def animations():

    qu= db.danimations.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/animations.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def login_register():

    qu= db.dlogin0register.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/login-register.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def index_3():

    qu= db.dindex03.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index-3.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def compose_email():

    qu= db.dcompose0email.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/compose-email.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def X404():

    qu= db.d404.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/404.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def index():

    qu= db.dindex.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def buttons():

    qu= db.dbuttons.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/buttons.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def line_charts():

    qu= db.dline0charts.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/line-charts.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def popovers():

    qu= db.dpopovers.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/popovers.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def color():

    qu= db.dcolor.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/color.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def notification():

    qu= db.dnotification.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/notification.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def invoice():

    qu= db.dinvoice.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/invoice.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def tabs():

    qu= db.dtabs.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/tabs.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def normal_table():

    qu= db.dnormal0table.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/normal-table.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def accordion():

    qu= db.daccordion.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/accordion.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def bar_charts():

    qu= db.dbar0charts.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/bar-charts.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def data_map():

    qu= db.ddata0map.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/data-map.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def dialog():

    qu= db.ddialog.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/dialog.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def alert():

    qu= db.dalert.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/alert.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def contact():

    qu= db.dcontact.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/contact.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def typography():

    qu= db.dtypography.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/typography.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def wizard():

    qu= db.dwizard.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/wizard.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def google_map():

    qu= db.dgoogle0map.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/google-map.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def index_2():

    qu= db.dindex02.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index-2.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def index_4():

    qu= db.dindex04.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/index-4.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def view_email():

    qu= db.dview0email.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/view-email.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def code_editor():

    qu= db.dcode0editor.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/code-editor.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def data_table():

    qu= db.ddata0table.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/data-table.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def tooltips():

    qu= db.dtooltips.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/tooltips.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def form_examples():

    qu= db.dform0examples.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/form-examples.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def flot_charts():

    qu= db.dflot0charts.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/flot-charts.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def widgets():

    qu= db.dwidgets.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/widgets.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def form_elements():

    qu= db.dform0elements.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/form-elements.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def area_charts():

    qu= db.darea0charts.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/area-charts.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def analytics():

    qu= db.danalytics.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/analytics.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def modals():

    qu= db.dmodals.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/modals.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def inbox():

    qu= db.dinbox.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/inbox.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def image_cropper():

    qu= db.dimage0cropper.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/image-cropper.html'

    return dict( DICT= rows_dict, )

#@auth.requires_login()
def dropdown():

    qu= db.ddropdown.id > 0
    rows= db(qu).select()
    rows_dict = { r.f0 : r.f1 for r in rows }
    response.view = 'default/dropdown.html'

    return dict( DICT= rows_dict, )