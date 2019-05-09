

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
def rounded_chart():
    db.drounded0chart.f0.writable = True
    response.view = 'myadd/rounded-chart.html'
    return dict(grid= mygrid('drounded0chart'))
#


@auth.requires_login()
def product_detail():
    db.dproduct0detail.f0.writable = True
    response.view = 'myadd/product-detail.html'
    return dict(grid= mygrid('dproduct0detail'))
#


@auth.requires_login()
def dual_list_box():
    db.ddual0list0box.f0.writable = True
    response.view = 'myadd/dual-list-box.html'
    return dict(grid= mygrid('ddual0list0box'))
#


@auth.requires_login()
def tabs():
    db.dtabs.f0.writable = True
    response.view = 'myadd/tabs.html'
    return dict(grid= mygrid('dtabs'))
#


@auth.requires_login()
def password_recovery():
    db.dpassword0recovery.f0.writable = True
    response.view = 'myadd/password-recovery.html'
    return dict(grid= mygrid('dpassword0recovery'))
#


@auth.requires_login()
def product_list():
    db.dproduct0list.f0.writable = True
    response.view = 'myadd/product-list.html'
    return dict(grid= mygrid('dproduct0list'))
#


@auth.requires_login()
def sparkline():
    db.dsparkline.f0.writable = True
    response.view = 'myadd/sparkline.html'
    return dict(grid= mygrid('dsparkline'))
#


@auth.requires_login()
def product_payment():
    db.dproduct0payment.f0.writable = True
    response.view = 'myadd/product-payment.html'
    return dict(grid= mygrid('dproduct0payment'))
#


@auth.requires_login()
def alerts():
    db.dalerts.f0.writable = True
    response.view = 'myadd/alerts.html'
    return dict(grid= mygrid('dalerts'))
#


@auth.requires_login()
def x_editable():
    db.dx0editable.f0.writable = True
    response.view = 'myadd/x-editable.html'
    return dict(grid= mygrid('dx0editable'))
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
def file_manager():
    db.dfile0manager.f0.writable = True
    response.view = 'myadd/file-manager.html'
    return dict(grid= mygrid('dfile0manager'))
#


@auth.requires_login()
def c3():
    db.dc3.f0.writable = True
    response.view = 'myadd/c3.html'
    return dict(grid= mygrid('dc3'))
#


@auth.requires_login()
def product_edit():
    db.dproduct0edit.f0.writable = True
    response.view = 'myadd/product-edit.html'
    return dict(grid= mygrid('dproduct0edit'))
#


@auth.requires_login()
def tinymc():
    db.dtinymc.f0.writable = True
    response.view = 'myadd/tinymc.html'
    return dict(grid= mygrid('dtinymc'))
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
def preloader():
    db.dpreloader.f0.writable = True
    response.view = 'myadd/preloader.html'
    return dict(grid= mygrid('dpreloader'))
#


@auth.requires_login()
def mailbox_view():
    db.dmailbox0view.f0.writable = True
    response.view = 'myadd/mailbox-view.html'
    return dict(grid= mygrid('dmailbox0view'))
#


@auth.requires_login()
def static_table():
    db.dstatic0table.f0.writable = True
    response.view = 'myadd/static-table.html'
    return dict(grid= mygrid('dstatic0table'))
#


@auth.requires_login()
def bar_charts():
    db.dbar0charts.f0.writable = True
    response.view = 'myadd/bar-charts.html'
    return dict(grid= mygrid('dbar0charts'))
#


@auth.requires_login()
def mailbox_compose():
    db.dmailbox0compose.f0.writable = True
    response.view = 'myadd/mailbox-compose.html'
    return dict(grid= mygrid('dmailbox0compose'))
#


@auth.requires_login()
def login():
    db.dlogin.f0.writable = True
    response.view = 'myadd/login.html'
    return dict(grid= mygrid('dlogin'))
#


@auth.requires_login()
def multi_upload():
    db.dmulti0upload.f0.writable = True
    response.view = 'myadd/multi-upload.html'
    return dict(grid= mygrid('dmulti0upload'))
#


@auth.requires_login()
def data_maps():
    db.ddata0maps.f0.writable = True
    response.view = 'myadd/data-maps.html'
    return dict(grid= mygrid('ddata0maps'))
#


@auth.requires_login()
def mailbox():
    db.dmailbox.f0.writable = True
    response.view = 'myadd/mailbox.html'
    return dict(grid= mygrid('dmailbox'))
#


@auth.requires_login()
def area_charts():
    db.darea0charts.f0.writable = True
    response.view = 'myadd/area-charts.html'
    return dict(grid= mygrid('darea0charts'))
#


@auth.requires_login()
def notifications():
    db.dnotifications.f0.writable = True
    response.view = 'myadd/notifications.html'
    return dict(grid= mygrid('dnotifications'))
#


@auth.requires_login()
def basic_form_element():
    db.dbasic0form0element.f0.writable = True
    response.view = 'myadd/basic-form-element.html'
    return dict(grid= mygrid('dbasic0form0element'))
#


@auth.requires_login()
def product_cart():
    db.dproduct0cart.f0.writable = True
    response.view = 'myadd/product-cart.html'
    return dict(grid= mygrid('dproduct0cart'))
#


@auth.requires_login()
def line_charts():
    db.dline0charts.f0.writable = True
    response.view = 'myadd/line-charts.html'
    return dict(grid= mygrid('dline0charts'))
#


@auth.requires_login()
def advance_form_element():
    db.dadvance0form0element.f0.writable = True
    response.view = 'myadd/advance-form-element.html'
    return dict(grid= mygrid('dadvance0form0element'))
#


@auth.requires_login()
def register():
    db.dregister.f0.writable = True
    response.view = 'myadd/register.html'
    return dict(grid= mygrid('dregister'))
#


@auth.requires_login()
def pdf_viewer():
    db.dpdf0viewer.f0.writable = True
    response.view = 'myadd/pdf-viewer.html'
    return dict(grid= mygrid('dpdf0viewer'))
#


@auth.requires_login()
def password_meter():
    db.dpassword0meter.f0.writable = True
    response.view = 'myadd/password-meter.html'
    return dict(grid= mygrid('dpassword0meter'))
#


@auth.requires_login()
def widgets():
    db.dwidgets.f0.writable = True
    response.view = 'myadd/widgets.html'
    return dict(grid= mygrid('dwidgets'))
#


@auth.requires_login()
def peity():
    db.dpeity.f0.writable = True
    response.view = 'myadd/peity.html'
    return dict(grid= mygrid('dpeity'))
#


@auth.requires_login()
def tree_view():
    db.dtree0view.f0.writable = True
    response.view = 'myadd/tree-view.html'
    return dict(grid= mygrid('dtree0view'))
#


@auth.requires_login()
def table_index1():
    db.dindex.f0.writable = True
    response.view = 'myadd/table_index1.html'
    return dict(grid= mygrid('dindex'))
#


@auth.requires_login()
def index_1():
    db.dindex01.f0.writable = True
    response.view = 'myadd/index-1.html'
    return dict(grid= mygrid('dindex01'))
#


@auth.requires_login()
def X500():
    db.d500.f0.writable = True
    response.view = 'myadd/500.html'
    return dict(grid= mygrid('d500'))
#


@auth.requires_login()
def blog_details():
    db.dblog0details.f0.writable = True
    response.view = 'myadd/blog-details.html'
    return dict(grid= mygrid('dblog0details'))
#


@auth.requires_login()
def lock():
    db.dlock.f0.writable = True
    response.view = 'myadd/lock.html'
    return dict(grid= mygrid('dlock'))
#


@auth.requires_login()
def google_map():
    db.dgoogle0map.f0.writable = True
    response.view = 'myadd/google-map.html'
    return dict(grid= mygrid('dgoogle0map'))
#


@auth.requires_login()
def data_table():
    db.ddata0table.f0.writable = True
    response.view = 'myadd/data-table.html'
    return dict(grid= mygrid('ddata0table'))
#


@auth.requires_login()
def blog():
    db.dblog.f0.writable = True
    response.view = 'myadd/blog.html'
    return dict(grid= mygrid('dblog'))
#


@auth.requires_login()
def images_cropper():
    db.dimages0cropper.f0.writable = True
    response.view = 'myadd/images-cropper.html'
    return dict(grid= mygrid('dimages0cropper'))
#


@auth.requires_login()
def X404():
    db.d404.f0.writable = True
    response.view = 'myadd/404.html'
    return dict(grid= mygrid('d404'))
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
def peitytable0ctrl():
    response.view = 'myadd/peitytable0ctrl.html'
    return dict(grid= mygrid('peitytable0'))
#


@auth.requires_login()
def peitytable1ctrl():
    response.view = 'myadd/peitytable1ctrl.html'
    return dict(grid= mygrid('peitytable1'))
#


@auth.requires_login()
def sparklinetable0ctrl():
    response.view = 'myadd/sparklinetable0ctrl.html'
    return dict(grid= mygrid('sparklinetable0'))
#


@auth.requires_login()
def static0tabletable0ctrl():
    response.view = 'myadd/static0tabletable0ctrl.html'
    return dict(grid= mygrid('static0tabletable0'))
#


@auth.requires_login()
def static0tabletable1ctrl():
    response.view = 'myadd/static0tabletable1ctrl.html'
    return dict(grid= mygrid('static0tabletable1'))
#


@auth.requires_login()
def static0tabletable2ctrl():
    response.view = 'myadd/static0tabletable2ctrl.html'
    return dict(grid= mygrid('static0tabletable2'))
#


@auth.requires_login()
def static0tabletable3ctrl():
    response.view = 'myadd/static0tabletable3ctrl.html'
    return dict(grid= mygrid('static0tabletable3'))
#


@auth.requires_login()
def static0tabletable4ctrl():
    response.view = 'myadd/static0tabletable4ctrl.html'
    return dict(grid= mygrid('static0tabletable4'))
#


@auth.requires_login()
def static0tabletable5ctrl():
    response.view = 'myadd/static0tabletable5ctrl.html'
    return dict(grid= mygrid('static0tabletable5'))
#


@auth.requires_login()
def data0tabletable0ctrl():
    response.view = 'myadd/data0tabletable0ctrl.html'
    return dict(grid= mygrid('data0tabletable0'))
#


@auth.requires_login()
def widgetstable0ctrl():
    response.view = 'myadd/widgetstable0ctrl.html'
    return dict(grid= mygrid('widgetstable0'))
#


@auth.requires_login()
def widgetstable1ctrl():
    response.view = 'myadd/widgetstable1ctrl.html'
    return dict(grid= mygrid('widgetstable1'))
#


@auth.requires_login()
def widgetstable2ctrl():
    response.view = 'myadd/widgetstable2ctrl.html'
    return dict(grid= mygrid('widgetstable2'))
#


@auth.requires_login()
def widgetstable3ctrl():
    response.view = 'myadd/widgetstable3ctrl.html'
    return dict(grid= mygrid('widgetstable3'))
#


@auth.requires_login()
def dpeityform0ctrl():
    response.view = 'myadd/dpeityform0ctrl.html'
    return dict(grid= mygrid('dpeityform0'))
#


@auth.requires_login()
def dpdf_viewerform0ctrl():
    response.view = 'myadd/dpdf_viewerform0ctrl.html'
    return dict(grid= mygrid('dpdf_viewerform0'))
#


@auth.requires_login()
def dtree_viewform0ctrl():
    response.view = 'myadd/dtree_viewform0ctrl.html'
    return dict(grid= mygrid('dtree_viewform0'))
#


@auth.requires_login()
def dgoogle_mapform0ctrl():
    response.view = 'myadd/dgoogle_mapform0ctrl.html'
    return dict(grid= mygrid('dgoogle_mapform0'))
#


@auth.requires_login()
def dblogform0ctrl():
    response.view = 'myadd/dblogform0ctrl.html'
    return dict(grid= mygrid('dblogform0'))
#


@auth.requires_login()
def ddata_mapsform0ctrl():
    response.view = 'myadd/ddata_mapsform0ctrl.html'
    return dict(grid= mygrid('ddata_mapsform0'))
#


@auth.requires_login()
def drounded_chartform0ctrl():
    response.view = 'myadd/drounded_chartform0ctrl.html'
    return dict(grid= mygrid('drounded_chartform0'))
#


@auth.requires_login()
def dindex_1form0ctrl():
    response.view = 'myadd/dindex_1form0ctrl.html'
    return dict(grid= mygrid('dindex_1form0'))
#


@auth.requires_login()
def dproduct_editform0ctrl():
    response.view = 'myadd/dproduct_editform0ctrl.html'
    return dict(grid= mygrid('dproduct_editform0'))
#


@auth.requires_login()
def dproduct_editform1ctrl():
    response.view = 'myadd/dproduct_editform1ctrl.html'
    return dict(grid= mygrid('dproduct_editform1'))
#


@auth.requires_login()
def dproduct_editform2ctrl():
    response.view = 'myadd/dproduct_editform2ctrl.html'
    return dict(grid= mygrid('dproduct_editform2'))
#


@auth.requires_login()
def dproduct_editform3ctrl():
    response.view = 'myadd/dproduct_editform3ctrl.html'
    return dict(grid= mygrid('dproduct_editform3'))
#


@auth.requires_login()
def dbar_chartsform0ctrl():
    response.view = 'myadd/dbar_chartsform0ctrl.html'
    return dict(grid= mygrid('dbar_chartsform0'))
#


@auth.requires_login()
def dmailbox_composeform0ctrl():
    response.view = 'myadd/dmailbox_composeform0ctrl.html'
    return dict(grid= mygrid('dmailbox_composeform0'))
#


@auth.requires_login()
def dmailbox_composeform1ctrl():
    response.view = 'myadd/dmailbox_composeform1ctrl.html'
    return dict(grid= mygrid('dmailbox_composeform1'))
#


@auth.requires_login()
def dbuttonsform0ctrl():
    response.view = 'myadd/dbuttonsform0ctrl.html'
    return dict(grid= mygrid('dbuttonsform0'))
#


@auth.requires_login()
def dtinymcform0ctrl():
    response.view = 'myadd/dtinymcform0ctrl.html'
    return dict(grid= mygrid('dtinymcform0'))
#


@auth.requires_login()
def dline_chartsform0ctrl():
    response.view = 'myadd/dline_chartsform0ctrl.html'
    return dict(grid= mygrid('dline_chartsform0'))
#


@auth.requires_login()
def dsparklineform0ctrl():
    response.view = 'myadd/dsparklineform0ctrl.html'
    return dict(grid= mygrid('dsparklineform0'))
#


@auth.requires_login()
def dpassword_recoveryform0ctrl():
    response.view = 'myadd/dpassword_recoveryform0ctrl.html'
    return dict(grid= mygrid('dpassword_recoveryform0'))
#


@auth.requires_login()
def dlockform0ctrl():
    response.view = 'myadd/dlockform0ctrl.html'
    return dict(grid= mygrid('dlockform0'))
#


@auth.requires_login()
def dpassword_meterform0ctrl():
    response.view = 'myadd/dpassword_meterform0ctrl.html'
    return dict(grid= mygrid('dpassword_meterform0'))
#


@auth.requires_login()
def dproduct_cartform0ctrl():
    response.view = 'myadd/dproduct_cartform0ctrl.html'
    return dict(grid= mygrid('dproduct_cartform0'))
#


@auth.requires_login()
def dloginform0ctrl():
    response.view = 'myadd/dloginform0ctrl.html'
    return dict(grid= mygrid('dloginform0'))
#


@auth.requires_login()
def dproduct_listform0ctrl():
    response.view = 'myadd/dproduct_listform0ctrl.html'
    return dict(grid= mygrid('dproduct_listform0'))
#


@auth.requires_login()
def dmulti_uploadform0ctrl():
    response.view = 'myadd/dmulti_uploadform0ctrl.html'
    return dict(grid= mygrid('dmulti_uploadform0'))
#


@auth.requires_login()
def dc3form0ctrl():
    response.view = 'myadd/dc3form0ctrl.html'
    return dict(grid= mygrid('dc3form0'))
#


@auth.requires_login()
def dstatic_tableform0ctrl():
    response.view = 'myadd/dstatic_tableform0ctrl.html'
    return dict(grid= mygrid('dstatic_tableform0'))
#


@auth.requires_login()
def dadvance_form_elementform0ctrl():
    response.view = 'myadd/dadvance_form_elementform0ctrl.html'
    return dict(grid= mygrid('dadvance_form_elementform0'))
#


@auth.requires_login()
def dproduct_detailform0ctrl():
    response.view = 'myadd/dproduct_detailform0ctrl.html'
    return dict(grid= mygrid('dproduct_detailform0'))
#


@auth.requires_login()
def dnotificationsform0ctrl():
    response.view = 'myadd/dnotificationsform0ctrl.html'
    return dict(grid= mygrid('dnotificationsform0'))
#


@auth.requires_login()
def ddual_list_boxform0ctrl():
    response.view = 'myadd/ddual_list_boxform0ctrl.html'
    return dict(grid= mygrid('ddual_list_boxform0'))
#


@auth.requires_login()
def ddual_list_boxform1ctrl():
    response.view = 'myadd/ddual_list_boxform1ctrl.html'
    return dict(grid= mygrid('ddual_list_boxform1'))
#


@auth.requires_login()
def dindexform0ctrl():
    response.view = 'myadd/dindexform0ctrl.html'
    return dict(grid= mygrid('dindexform0'))
#


@auth.requires_login()
def daccordionform0ctrl():
    response.view = 'myadd/daccordionform0ctrl.html'
    return dict(grid= mygrid('daccordionform0'))
#


@auth.requires_login()
def dfile_managerform0ctrl():
    response.view = 'myadd/dfile_managerform0ctrl.html'
    return dict(grid= mygrid('dfile_managerform0'))
#


@auth.requires_login()
def dpreloaderform0ctrl():
    response.view = 'myadd/dpreloaderform0ctrl.html'
    return dict(grid= mygrid('dpreloaderform0'))
#


@auth.requires_login()
def dtabsform0ctrl():
    response.view = 'myadd/dtabsform0ctrl.html'
    return dict(grid= mygrid('dtabsform0'))
#


@auth.requires_login()
def dalertsform0ctrl():
    response.view = 'myadd/dalertsform0ctrl.html'
    return dict(grid= mygrid('dalertsform0'))
#


@auth.requires_login()
def dindex_2form0ctrl():
    response.view = 'myadd/dindex_2form0ctrl.html'
    return dict(grid= mygrid('dindex_2form0'))
#


@auth.requires_login()
def dblog_detailsform0ctrl():
    response.view = 'myadd/dblog_detailsform0ctrl.html'
    return dict(grid= mygrid('dblog_detailsform0'))
#


@auth.requires_login()
def dblog_detailsform1ctrl():
    response.view = 'myadd/dblog_detailsform1ctrl.html'
    return dict(grid= mygrid('dblog_detailsform1'))
#


@auth.requires_login()
def dimages_cropperform0ctrl():
    response.view = 'myadd/dimages_cropperform0ctrl.html'
    return dict(grid= mygrid('dimages_cropperform0'))
#


@auth.requires_login()
def dx_editableform0ctrl():
    response.view = 'myadd/dx_editableform0ctrl.html'
    return dict(grid= mygrid('dx_editableform0'))
#


@auth.requires_login()
def dcode_editorform0ctrl():
    response.view = 'myadd/dcode_editorform0ctrl.html'
    return dict(grid= mygrid('dcode_editorform0'))
#


@auth.requires_login()
def ddata_tableform0ctrl():
    response.view = 'myadd/ddata_tableform0ctrl.html'
    return dict(grid= mygrid('ddata_tableform0'))
#


@auth.requires_login()
def dmailboxform0ctrl():
    response.view = 'myadd/dmailboxform0ctrl.html'
    return dict(grid= mygrid('dmailboxform0'))
#


@auth.requires_login()
def dbasic_form_elementform0ctrl():
    response.view = 'myadd/dbasic_form_elementform0ctrl.html'
    return dict(grid= mygrid('dbasic_form_elementform0'))
#


@auth.requires_login()
def dbasic_form_elementform1ctrl():
    response.view = 'myadd/dbasic_form_elementform1ctrl.html'
    return dict(grid= mygrid('dbasic_form_elementform1'))
#


@auth.requires_login()
def dbasic_form_elementform2ctrl():
    response.view = 'myadd/dbasic_form_elementform2ctrl.html'
    return dict(grid= mygrid('dbasic_form_elementform2'))
#


@auth.requires_login()
def dbasic_form_elementform3ctrl():
    response.view = 'myadd/dbasic_form_elementform3ctrl.html'
    return dict(grid= mygrid('dbasic_form_elementform3'))
#


@auth.requires_login()
def dbasic_form_elementform4ctrl():
    response.view = 'myadd/dbasic_form_elementform4ctrl.html'
    return dict(grid= mygrid('dbasic_form_elementform4'))
#


@auth.requires_login()
def dbasic_form_elementform5ctrl():
    response.view = 'myadd/dbasic_form_elementform5ctrl.html'
    return dict(grid= mygrid('dbasic_form_elementform5'))
#


@auth.requires_login()
def dwidgetsform0ctrl():
    response.view = 'myadd/dwidgetsform0ctrl.html'
    return dict(grid= mygrid('dwidgetsform0'))
#


@auth.requires_login()
def dmailbox_viewform0ctrl():
    response.view = 'myadd/dmailbox_viewform0ctrl.html'
    return dict(grid= mygrid('dmailbox_viewform0'))
#


@auth.requires_login()
def darea_chartsform0ctrl():
    response.view = 'myadd/darea_chartsform0ctrl.html'
    return dict(grid= mygrid('darea_chartsform0'))
#


@auth.requires_login()
def danalyticsform0ctrl():
    response.view = 'myadd/danalyticsform0ctrl.html'
    return dict(grid= mygrid('danalyticsform0'))
#


@auth.requires_login()
def dregisterform0ctrl():
    response.view = 'myadd/dregisterform0ctrl.html'
    return dict(grid= mygrid('dregisterform0'))
#


@auth.requires_login()
def dmodalsform0ctrl():
    response.view = 'myadd/dmodalsform0ctrl.html'
    return dict(grid= mygrid('dmodalsform0'))
#


@auth.requires_login()
def dproduct_paymentform0ctrl():
    response.view = 'myadd/dproduct_paymentform0ctrl.html'
    return dict(grid= mygrid('dproduct_paymentform0'))
#


@auth.requires_login()
def dproduct_paymentform1ctrl():
    response.view = 'myadd/dproduct_paymentform1ctrl.html'
    return dict(grid= mygrid('dproduct_paymentform1'))
#
