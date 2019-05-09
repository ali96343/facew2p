

@auth.requires_login()
def mygrid(tnm):
   return SQLFORM.grid(db[tnm], deletable= False, user_signature=False,  buttons_placement = 'left', showbuttontext=False, csv=False )
# 

@auth.requires_login()
def search_site():
    import os
    form = SQLFORM.factory(
       Field('search', label='search for unique text ( or number label) from screen', requires=IS_NOT_EMPTY(),  ),
       Field('replace', 'text', label='replace with new text', requires=IS_NOT_EMPTY(), length= 1000, ),
       )
    if form.process( keepvalues = True  ).accepted: 
        search  = form.vars.search
        replace  = form.vars.replace
        replace=replace.strip()
        for table in db.tables():
             if any (['auth_' in table, 'form' in table,  not 'f1' in db[table].fields]) :
                     continue
             qu= db[table].f1.contains(search)
             rows = db(qu).select()
             if rows:
               if len(rows) == 1:
                 row = db(qu).select().first()
                 if row:
                    #session.flash = 'found!! %s' % row.f1
                    savef1= row.f1
                    db(db[table].id == row.id).update( f1= replace, f2= savef1  )
                    response.flash = 'replaced, found == 1!'
                    break
               else:
                    response.flash = 'do not replaced, found > 1!'
                    break
    elif form.errors:
        response.flash = 'Please correct the error(s).'
    else: 
        response.flash = 'Insert data please - no fields can be empty.' 
    return form


#https://stackoverflow.com/questions/37806801/can-not-post-data-via-ajax-to-web2py-rest-api-possible-cors-issue/37859336
#url_name='https://sun.minfindnr.ru/ji15/default/api/t0_tables.json'
#url_name='https://sun.minfindnr.ru/ji15/default/api/patterns.json'

@auth.requires_login()
@request.restful()
def api():
    from gluon.serializers import json
    response.view = 'generic.' + request.extension
    def GET(*args,**vars):
         patterns = 'auto'
         parser = db.parse_as_rest(patterns,args,vars)
         if parser.status == 200:
            return dict(content=parser.response)
         else:
            raise HTTP(parser.status,parser.error)
    def POST(table_name,**vars):
        #return db[table_name].validate_and_insert(**vars)
        #data = gluon.contrib.simplejson.loads(request.body.read())
        return json(db[table_name].validate_and_insert(**vars))
        return dict()
    def PUT(table_name,record_id,**vars):
        return db(db[table_name]._id==record_id).update(**vars)
    def DELETE(table_name,record_id):
        return db(db[table_name]._id==record_id).delete()
    def OPTIONS(*args,**vars):
        print ( 'OPTION called') 
        return True
    return dict(GET=GET,POST=POST,PUT=PUT,DELETE=DELETE,OPTIONS=OPTIONS)


@auth.requires_login()
def index():
    response.view = 'myadd/index.html'
    return dict(form=search_site())



@auth.requires_login()
def index_2():
    db.dindex02.f0.writable = True
    response.view = 'myadd/index-2.html'
    return dict(grid= mygrid('dindex02'))
#


@auth.requires_login()
def animations():
    db.danimations.f0.writable = True
    response.view = 'myadd/animations.html'
    return dict(grid= mygrid('danimations'))
#


@auth.requires_login()
def tabs():
    db.dtabs.f0.writable = True
    response.view = 'myadd/tabs.html'
    return dict(grid= mygrid('dtabs'))
#


@auth.requires_login()
def accordion():
    db.daccordion.f0.writable = True
    response.view = 'myadd/accordion.html'
    return dict(grid= mygrid('daccordion'))
#


@auth.requires_login()
def modals():
    db.dmodals.f0.writable = True
    response.view = 'myadd/modals.html'
    return dict(grid= mygrid('dmodals'))
#


@auth.requires_login()
def code_editor():
    db.dcode0editor.f0.writable = True
    response.view = 'myadd/code-editor.html'
    return dict(grid= mygrid('dcode0editor'))
#


@auth.requires_login()
def login_register():
    db.dlogin0register.f0.writable = True
    response.view = 'myadd/login-register.html'
    return dict(grid= mygrid('dlogin0register'))
#


@auth.requires_login()
def typography():
    db.dtypography.f0.writable = True
    response.view = 'myadd/typography.html'
    return dict(grid= mygrid('dtypography'))
#


@auth.requires_login()
def invoice():
    db.dinvoice.f0.writable = True
    response.view = 'myadd/invoice.html'
    return dict(grid= mygrid('dinvoice'))
#


@auth.requires_login()
def view_email():
    db.dview0email.f0.writable = True
    response.view = 'myadd/view-email.html'
    return dict(grid= mygrid('dview0email'))
#


@auth.requires_login()
def form_components():
    db.dform0components.f0.writable = True
    response.view = 'myadd/form-components.html'
    return dict(grid= mygrid('dform0components'))
#


@auth.requires_login()
def flot_charts():
    db.dflot0charts.f0.writable = True
    response.view = 'myadd/flot-charts.html'
    return dict(grid= mygrid('dflot0charts'))
#


@auth.requires_login()
def buttons():
    db.dbuttons.f0.writable = True
    response.view = 'myadd/buttons.html'
    return dict(grid= mygrid('dbuttons'))
#


@auth.requires_login()
def analytics():
    db.danalytics.f0.writable = True
    response.view = 'myadd/analytics.html'
    return dict(grid= mygrid('danalytics'))
#


@auth.requires_login()
def dialog():
    db.ddialog.f0.writable = True
    response.view = 'myadd/dialog.html'
    return dict(grid= mygrid('ddialog'))
#


@auth.requires_login()
def wizard():
    db.dwizard.f0.writable = True
    response.view = 'myadd/wizard.html'
    return dict(grid= mygrid('dwizard'))
#


@auth.requires_login()
def bar_charts():
    db.dbar0charts.f0.writable = True
    response.view = 'myadd/bar-charts.html'
    return dict(grid= mygrid('dbar0charts'))
#


@auth.requires_login()
def notification():
    db.dnotification.f0.writable = True
    response.view = 'myadd/notification.html'
    return dict(grid= mygrid('dnotification'))
#


@auth.requires_login()
def dropdown():
    db.ddropdown.f0.writable = True
    response.view = 'myadd/dropdown.html'
    return dict(grid= mygrid('ddropdown'))
#


@auth.requires_login()
def area_charts():
    db.darea0charts.f0.writable = True
    response.view = 'myadd/area-charts.html'
    return dict(grid= mygrid('darea0charts'))
#


@auth.requires_login()
def index_4():
    db.dindex04.f0.writable = True
    response.view = 'myadd/index-4.html'
    return dict(grid= mygrid('dindex04'))
#


@auth.requires_login()
def form_elements():
    db.dform0elements.f0.writable = True
    response.view = 'myadd/form-elements.html'
    return dict(grid= mygrid('dform0elements'))
#


@auth.requires_login()
def alert():
    db.dalert.f0.writable = True
    response.view = 'myadd/alert.html'
    return dict(grid= mygrid('dalert'))
#


@auth.requires_login()
def line_charts():
    db.dline0charts.f0.writable = True
    response.view = 'myadd/line-charts.html'
    return dict(grid= mygrid('dline0charts'))
#


@auth.requires_login()
def contact():
    db.dcontact.f0.writable = True
    response.view = 'myadd/contact.html'
    return dict(grid= mygrid('dcontact'))
#


@auth.requires_login()
def popovers():
    db.dpopovers.f0.writable = True
    response.view = 'myadd/popovers.html'
    return dict(grid= mygrid('dpopovers'))
#


@auth.requires_login()
def normal_table():
    db.dnormal0table.f0.writable = True
    response.view = 'myadd/normal-table.html'
    return dict(grid= mygrid('dnormal0table'))
#


@auth.requires_login()
def form_examples():
    db.dform0examples.f0.writable = True
    response.view = 'myadd/form-examples.html'
    return dict(grid= mygrid('dform0examples'))
#


@auth.requires_login()
def index_3():
    db.dindex03.f0.writable = True
    response.view = 'myadd/index-3.html'
    return dict(grid= mygrid('dindex03'))
#


@auth.requires_login()
def color():
    db.dcolor.f0.writable = True
    response.view = 'myadd/color.html'
    return dict(grid= mygrid('dcolor'))
#


@auth.requires_login()
def widgets():
    db.dwidgets.f0.writable = True
    response.view = 'myadd/widgets.html'
    return dict(grid= mygrid('dwidgets'))
#


@auth.requires_login()
def table_index1():
    db.dindex.f0.writable = True
    response.view = 'myadd/table_index1.html'
    return dict(grid= mygrid('dindex'))
#


@auth.requires_login()
def data_map():
    db.ddata0map.f0.writable = True
    response.view = 'myadd/data-map.html'
    return dict(grid= mygrid('ddata0map'))
#


@auth.requires_login()
def compose_email():
    db.dcompose0email.f0.writable = True
    response.view = 'myadd/compose-email.html'
    return dict(grid= mygrid('dcompose0email'))
#


@auth.requires_login()
def inbox():
    db.dinbox.f0.writable = True
    response.view = 'myadd/inbox.html'
    return dict(grid= mygrid('dinbox'))
#


@auth.requires_login()
def google_map():
    db.dgoogle0map.f0.writable = True
    response.view = 'myadd/google-map.html'
    return dict(grid= mygrid('dgoogle0map'))
#


@auth.requires_login()
def tooltips():
    db.dtooltips.f0.writable = True
    response.view = 'myadd/tooltips.html'
    return dict(grid= mygrid('dtooltips'))
#


@auth.requires_login()
def data_table():
    db.ddata0table.f0.writable = True
    response.view = 'myadd/data-table.html'
    return dict(grid= mygrid('ddata0table'))
#


@auth.requires_login()
def X404():
    db.d404.f0.writable = True
    response.view = 'myadd/404.html'
    return dict(grid= mygrid('d404'))
#


@auth.requires_login()
def image_cropper():
    db.dimage0cropper.f0.writable = True
    response.view = 'myadd/image-cropper.html'
    return dict(grid= mygrid('dimage0cropper'))
#


@auth.requires_login()
def auth_eventctrl():
    response.view = 'myadd/auth_eventctrl.html'
    return dict(grid= mygrid('auth_event'))
#


@auth.requires_login()
def auth_userctrl():
    response.view = 'myadd/auth_userctrl.html'
    return dict(grid= mygrid('auth_user'))
#


@auth.requires_login()
def auth_groupctrl():
    response.view = 'myadd/auth_groupctrl.html'
    return dict(grid= mygrid('auth_group'))
#


@auth.requires_login()
def auth_membershipctrl():
    response.view = 'myadd/auth_membershipctrl.html'
    return dict(grid= mygrid('auth_membership'))
#


@auth.requires_login()
def index03table0ctrl():
    response.view = 'myadd/index03table0ctrl.html'
    return dict(grid= mygrid('index03table0'))
#


@auth.requires_login()
def indextable0ctrl():
    response.view = 'myadd/indextable0ctrl.html'
    return dict(grid= mygrid('indextable0'))
#


@auth.requires_login()
def invoicetable0ctrl():
    response.view = 'myadd/invoicetable0ctrl.html'
    return dict(grid= mygrid('invoicetable0'))
#


@auth.requires_login()
def normal0tabletable0ctrl():
    response.view = 'myadd/normal0tabletable0ctrl.html'
    return dict(grid= mygrid('normal0tabletable0'))
#


@auth.requires_login()
def normal0tabletable1ctrl():
    response.view = 'myadd/normal0tabletable1ctrl.html'
    return dict(grid= mygrid('normal0tabletable1'))
#


@auth.requires_login()
def normal0tabletable2ctrl():
    response.view = 'myadd/normal0tabletable2ctrl.html'
    return dict(grid= mygrid('normal0tabletable2'))
#


@auth.requires_login()
def normal0tabletable3ctrl():
    response.view = 'myadd/normal0tabletable3ctrl.html'
    return dict(grid= mygrid('normal0tabletable3'))
#


@auth.requires_login()
def normal0tabletable4ctrl():
    response.view = 'myadd/normal0tabletable4ctrl.html'
    return dict(grid= mygrid('normal0tabletable4'))
#


@auth.requires_login()
def normal0tabletable5ctrl():
    response.view = 'myadd/normal0tabletable5ctrl.html'
    return dict(grid= mygrid('normal0tabletable5'))
#


@auth.requires_login()
def index02table0ctrl():
    response.view = 'myadd/index02table0ctrl.html'
    return dict(grid= mygrid('index02table0'))
#


@auth.requires_login()
def index04table0ctrl():
    response.view = 'myadd/index04table0ctrl.html'
    return dict(grid= mygrid('index04table0'))
#


@auth.requires_login()
def data0tabletable0ctrl():
    response.view = 'myadd/data0tabletable0ctrl.html'
    return dict(grid= mygrid('data0tabletable0'))
#


@auth.requires_login()
def analyticstable0ctrl():
    response.view = 'myadd/analyticstable0ctrl.html'
    return dict(grid= mygrid('analyticstable0'))
#


@auth.requires_login()
def analyticstable1ctrl():
    response.view = 'myadd/analyticstable1ctrl.html'
    return dict(grid= mygrid('analyticstable1'))
#


@auth.requires_login()
def analyticstable2ctrl():
    response.view = 'myadd/analyticstable2ctrl.html'
    return dict(grid= mygrid('analyticstable2'))
#
