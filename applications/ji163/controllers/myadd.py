

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
def fixed_header():
    db.dfixed0header.f0.writable = True
    response.view = 'myadd/fixed-header.html'
    return dict(grid= mygrid('dfixed0header'))
#


@auth.requires_login()
def panel():
    db.dpanel.f0.writable = True
    response.view = 'myadd/panel.html'
    return dict(grid= mygrid('dpanel'))
#


@auth.requires_login()
def blank():
    db.dblank.f0.writable = True
    response.view = 'myadd/blank.html'
    return dict(grid= mygrid('dblank'))
#


@auth.requires_login()
def pricing():
    db.dpricing.f0.writable = True
    response.view = 'myadd/pricing.html'
    return dict(grid= mygrid('dpricing'))
#


@auth.requires_login()
def grid():
    db.dgrid.f0.writable = True
    response.view = 'myadd/grid.html'
    return dict(grid= mygrid('dgrid'))
#


@auth.requires_login()
def form_validation():
    db.dform0validation.f0.writable = True
    response.view = 'myadd/form-validation.html'
    return dict(grid= mygrid('dform0validation'))
#


@auth.requires_login()
def typography():
    db.dtypography.f0.writable = True
    response.view = 'myadd/typography.html'
    return dict(grid= mygrid('dtypography'))
#


@auth.requires_login()
def fixed_mini_sidebar():
    db.dfixed0mini0sidebar.f0.writable = True
    response.view = 'myadd/fixed-mini-sidebar.html'
    return dict(grid= mygrid('dfixed0mini0sidebar'))
#


@auth.requires_login()
def no_main_search():
    db.dno0main0search.f0.writable = True
    response.view = 'myadd/no-main-search.html'
    return dict(grid= mygrid('dno0main0search'))
#


@auth.requires_login()
def fixed_header_fixed_mini_sidebar():
    db.dfixed0header0fixed0mini0sidebar.f0.writable = True
    response.view = 'myadd/fixed-header-fixed-mini-sidebar.html'
    return dict(grid= mygrid('dfixed0header0fixed0mini0sidebar'))
#


@auth.requires_login()
def maps():
    db.dmaps.f0.writable = True
    response.view = 'myadd/maps.html'
    return dict(grid= mygrid('dmaps'))
#


@auth.requires_login()
def fixed_menu():
    db.dfixed0menu.f0.writable = True
    response.view = 'myadd/fixed-menu.html'
    return dict(grid= mygrid('dfixed0menu'))
#


@auth.requires_login()
def boxed():
    db.dboxed.f0.writable = True
    response.view = 'myadd/boxed.html'
    return dict(grid= mygrid('dboxed'))
#


@auth.requires_login()
def fixed_header_boxed():
    db.dfixed0header0boxed.f0.writable = True
    response.view = 'myadd/fixed-header-boxed.html'
    return dict(grid= mygrid('dfixed0header0boxed'))
#


@auth.requires_login()
def form_wizard():
    db.dform0wizard.f0.writable = True
    response.view = 'myadd/form-wizard.html'
    return dict(grid= mygrid('dform0wizard'))
#


@auth.requires_login()
def no_header():
    db.dno0header.f0.writable = True
    response.view = 'myadd/no-header.html'
    return dict(grid= mygrid('dno0header'))
#


@auth.requires_login()
def no_header_sidebar():
    db.dno0header0sidebar.f0.writable = True
    response.view = 'myadd/no-header-sidebar.html'
    return dict(grid= mygrid('dno0header0sidebar'))
#


@auth.requires_login()
def fixed_menu_boxed():
    db.dfixed0menu0boxed.f0.writable = True
    response.view = 'myadd/fixed-menu-boxed.html'
    return dict(grid= mygrid('dfixed0menu0boxed'))
#


@auth.requires_login()
def icon():
    db.dicon.f0.writable = True
    response.view = 'myadd/icon.html'
    return dict(grid= mygrid('dicon'))
#


@auth.requires_login()
def no_right_sidebar():
    db.dno0right0sidebar.f0.writable = True
    response.view = 'myadd/no-right-sidebar.html'
    return dict(grid= mygrid('dno0right0sidebar'))
#


@auth.requires_login()
def chart():
    db.dchart.f0.writable = True
    response.view = 'myadd/chart.html'
    return dict(grid= mygrid('dchart'))
#


@auth.requires_login()
def login():
    db.dlogin.f0.writable = True
    response.view = 'myadd/login.html'
    return dict(grid= mygrid('dlogin'))
#


@auth.requires_login()
def countdown():
    db.dcountdown.f0.writable = True
    response.view = 'myadd/countdown.html'
    return dict(grid= mygrid('dcountdown'))
#


@auth.requires_login()
def X503():
    db.d503.f0.writable = True
    response.view = 'myadd/503.html'
    return dict(grid= mygrid('d503'))
#


@auth.requires_login()
def bgcolor():
    db.dbgcolor.f0.writable = True
    response.view = 'myadd/bgcolor.html'
    return dict(grid= mygrid('dbgcolor'))
#


@auth.requires_login()
def alterne():
    db.dalterne.f0.writable = True
    response.view = 'myadd/alterne.html'
    return dict(grid= mygrid('dalterne'))
#


@auth.requires_login()
def no_left_sidebar_main_search():
    db.dno0left0sidebar0main0search.f0.writable = True
    response.view = 'myadd/no-left-sidebar-main-search.html'
    return dict(grid= mygrid('dno0left0sidebar0main0search'))
#


@auth.requires_login()
def dashboard():
    db.ddashboard.f0.writable = True
    response.view = 'myadd/dashboard.html'
    return dict(grid= mygrid('ddashboard'))
#


@auth.requires_login()
def bgimage():
    db.dbgimage.f0.writable = True
    response.view = 'myadd/bgimage.html'
    return dict(grid= mygrid('dbgimage'))
#


@auth.requires_login()
def form_general():
    db.dform0general.f0.writable = True
    response.view = 'myadd/form-general.html'
    return dict(grid= mygrid('dform0general'))
#


@auth.requires_login()
def no_left_sidebar():
    db.dno0left0sidebar.f0.writable = True
    response.view = 'myadd/no-left-sidebar.html'
    return dict(grid= mygrid('dno0left0sidebar'))
#


@auth.requires_login()
def progress():
    db.dprogress.f0.writable = True
    response.view = 'myadd/progress.html'
    return dict(grid= mygrid('dprogress'))
#


@auth.requires_login()
def no_left_right_sidebar():
    db.dno0left0right0sidebar.f0.writable = True
    response.view = 'myadd/no-left-right-sidebar.html'
    return dict(grid= mygrid('dno0left0right0sidebar'))
#


@auth.requires_login()
def table():
    db.dtable.f0.writable = True
    response.view = 'myadd/table.html'
    return dict(grid= mygrid('dtable'))
#


@auth.requires_login()
def fixed_header_mini_sidebar():
    db.dfixed0header0mini0sidebar.f0.writable = True
    response.view = 'myadd/fixed-header-mini-sidebar.html'
    return dict(grid= mygrid('dfixed0header0mini0sidebar'))
#


@auth.requires_login()
def table_index1():
    db.dindex.f0.writable = True
    response.view = 'myadd/table_index1.html'
    return dict(grid= mygrid('dindex'))
#


@auth.requires_login()
def calendar():
    db.dcalendar.f0.writable = True
    response.view = 'myadd/calendar.html'
    return dict(grid= mygrid('dcalendar'))
#


@auth.requires_login()
def X403():
    db.d403.f0.writable = True
    response.view = 'myadd/403.html'
    return dict(grid= mygrid('d403'))
#


@auth.requires_login()
def X500():
    db.d500.f0.writable = True
    response.view = 'myadd/500.html'
    return dict(grid= mygrid('d500'))
#


@auth.requires_login()
def fixed_header_menu():
    db.dfixed0header0menu.f0.writable = True
    response.view = 'myadd/fixed-header-menu.html'
    return dict(grid= mygrid('dfixed0header0menu'))
#


@auth.requires_login()
def sm():
    db.dsm.f0.writable = True
    response.view = 'myadd/sm.html'
    return dict(grid= mygrid('dsm'))
#


@auth.requires_login()
def fxhmoxed():
    db.dfxhmoxed.f0.writable = True
    response.view = 'myadd/fxhmoxed.html'
    return dict(grid= mygrid('dfxhmoxed'))
#


@auth.requires_login()
def X405():
    db.d405.f0.writable = True
    response.view = 'myadd/405.html'
    return dict(grid= mygrid('d405'))
#


@auth.requires_login()
def form_wysiwyg():
    db.dform0wysiwyg.f0.writable = True
    response.view = 'myadd/form-wysiwyg.html'
    return dict(grid= mygrid('dform0wysiwyg'))
#


@auth.requires_login()
def X404():
    db.d404.f0.writable = True
    response.view = 'myadd/404.html'
    return dict(grid= mygrid('d404'))
#


@auth.requires_login()
def button():
    db.dbutton.f0.writable = True
    response.view = 'myadd/button.html'
    return dict(grid= mygrid('dbutton'))
#


@auth.requires_login()
def offline():
    db.doffline.f0.writable = True
    response.view = 'myadd/offline.html'
    return dict(grid= mygrid('doffline'))
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
def dashboardtable0ctrl():
    response.view = 'myadd/dashboardtable0ctrl.html'
    return dict(grid= mygrid('dashboardtable0'))
#


@auth.requires_login()
def tabletable0ctrl():
    response.view = 'myadd/tabletable0ctrl.html'
    return dict(grid= mygrid('tabletable0'))
#


@auth.requires_login()
def tabletable1ctrl():
    response.view = 'myadd/tabletable1ctrl.html'
    return dict(grid= mygrid('tabletable1'))
#


@auth.requires_login()
def tabletable2ctrl():
    response.view = 'myadd/tabletable2ctrl.html'
    return dict(grid= mygrid('tabletable2'))
#


@auth.requires_login()
def tabletable3ctrl():
    response.view = 'myadd/tabletable3ctrl.html'
    return dict(grid= mygrid('tabletable3'))
#


@auth.requires_login()
def tabletable4ctrl():
    response.view = 'myadd/tabletable4ctrl.html'
    return dict(grid= mygrid('tabletable4'))
#


@auth.requires_login()
def tabletable5ctrl():
    response.view = 'myadd/tabletable5ctrl.html'
    return dict(grid= mygrid('tabletable5'))
#


@auth.requires_login()
def tabletable6ctrl():
    response.view = 'myadd/tabletable6ctrl.html'
    return dict(grid= mygrid('tabletable6'))
#


@auth.requires_login()
def typographytable0ctrl():
    response.view = 'myadd/typographytable0ctrl.html'
    return dict(grid= mygrid('typographytable0'))
#


@auth.requires_login()
def typographytable1ctrl():
    response.view = 'myadd/typographytable1ctrl.html'
    return dict(grid= mygrid('typographytable1'))
#


@auth.requires_login()
def alternetable0ctrl():
    response.view = 'myadd/alternetable0ctrl.html'
    return dict(grid= mygrid('alternetable0'))
#


@auth.requires_login()
def dbgimageform0ctrl():
    response.view = 'myadd/dbgimageform0ctrl.html'
    return dict(grid= mygrid('dbgimageform0'))
#


@auth.requires_login()
def dboxedform0ctrl():
    response.view = 'myadd/dboxedform0ctrl.html'
    return dict(grid= mygrid('dboxedform0'))
#


@auth.requires_login()
def dbuttonform0ctrl():
    response.view = 'myadd/dbuttonform0ctrl.html'
    return dict(grid= mygrid('dbuttonform0'))
#


@auth.requires_login()
def dfixed_header_fixed_mini_sidebarform0ctrl():
    response.view = 'myadd/dfixed_header_fixed_mini_sidebarform0ctrl.html'
    return dict(grid= mygrid('dfixed_header_fixed_mini_sidebarform0'))
#


@auth.requires_login()
def dX404form0ctrl():
    response.view = 'myadd/dX404form0ctrl.html'
    return dict(grid= mygrid('dX404form0'))
#


@auth.requires_login()
def ddashboardform0ctrl():
    response.view = 'myadd/ddashboardform0ctrl.html'
    return dict(grid= mygrid('ddashboardform0'))
#


@auth.requires_login()
def dno_right_sidebarform0ctrl():
    response.view = 'myadd/dno_right_sidebarform0ctrl.html'
    return dict(grid= mygrid('dno_right_sidebarform0'))
#


@auth.requires_login()
def dform_generalform0ctrl():
    response.view = 'myadd/dform_generalform0ctrl.html'
    return dict(grid= mygrid('dform_generalform0'))
#


@auth.requires_login()
def dform_generalform1ctrl():
    response.view = 'myadd/dform_generalform1ctrl.html'
    return dict(grid= mygrid('dform_generalform1'))
#


@auth.requires_login()
def dform_generalform2ctrl():
    response.view = 'myadd/dform_generalform2ctrl.html'
    return dict(grid= mygrid('dform_generalform2'))
#


@auth.requires_login()
def dform_generalform3ctrl():
    response.view = 'myadd/dform_generalform3ctrl.html'
    return dict(grid= mygrid('dform_generalform3'))
#


@auth.requires_login()
def dform_generalform4ctrl():
    response.view = 'myadd/dform_generalform4ctrl.html'
    return dict(grid= mygrid('dform_generalform4'))
#


@auth.requires_login()
def dform_generalform5ctrl():
    response.view = 'myadd/dform_generalform5ctrl.html'
    return dict(grid= mygrid('dform_generalform5'))
#


@auth.requires_login()
def dform_generalform6ctrl():
    response.view = 'myadd/dform_generalform6ctrl.html'
    return dict(grid= mygrid('dform_generalform6'))
#


@auth.requires_login()
def dform_generalform7ctrl():
    response.view = 'myadd/dform_generalform7ctrl.html'
    return dict(grid= mygrid('dform_generalform7'))
#


@auth.requires_login()
def dform_generalform8ctrl():
    response.view = 'myadd/dform_generalform8ctrl.html'
    return dict(grid= mygrid('dform_generalform8'))
#


@auth.requires_login()
def dform_generalform9ctrl():
    response.view = 'myadd/dform_generalform9ctrl.html'
    return dict(grid= mygrid('dform_generalform9'))
#


@auth.requires_login()
def dform_generalform10ctrl():
    response.view = 'myadd/dform_generalform10ctrl.html'
    return dict(grid= mygrid('dform_generalform10'))
#


@auth.requires_login()
def dindexform0ctrl():
    response.view = 'myadd/dindexform0ctrl.html'
    return dict(grid= mygrid('dindexform0'))
#


@auth.requires_login()
def dX503form0ctrl():
    response.view = 'myadd/dX503form0ctrl.html'
    return dict(grid= mygrid('dX503form0'))
#


@auth.requires_login()
def dmapsform0ctrl():
    response.view = 'myadd/dmapsform0ctrl.html'
    return dict(grid= mygrid('dmapsform0'))
#


@auth.requires_login()
def dmapsform1ctrl():
    response.view = 'myadd/dmapsform1ctrl.html'
    return dict(grid= mygrid('dmapsform1'))
#


@auth.requires_login()
def dtableform0ctrl():
    response.view = 'myadd/dtableform0ctrl.html'
    return dict(grid= mygrid('dtableform0'))
#


@auth.requires_login()
def dfixed_headerform0ctrl():
    response.view = 'myadd/dfixed_headerform0ctrl.html'
    return dict(grid= mygrid('dfixed_headerform0'))
#


@auth.requires_login()
def dloginform0ctrl():
    response.view = 'myadd/dloginform0ctrl.html'
    return dict(grid= mygrid('dloginform0'))
#


@auth.requires_login()
def dloginform1ctrl():
    response.view = 'myadd/dloginform1ctrl.html'
    return dict(grid= mygrid('dloginform1'))
#


@auth.requires_login()
def dloginform2ctrl():
    response.view = 'myadd/dloginform2ctrl.html'
    return dict(grid= mygrid('dloginform2'))
#


@auth.requires_login()
def dchartform0ctrl():
    response.view = 'myadd/dchartform0ctrl.html'
    return dict(grid= mygrid('dchartform0'))
#


@auth.requires_login()
def dgridform0ctrl():
    response.view = 'myadd/dgridform0ctrl.html'
    return dict(grid= mygrid('dgridform0'))
#


@auth.requires_login()
def diconform0ctrl():
    response.view = 'myadd/diconform0ctrl.html'
    return dict(grid= mygrid('diconform0'))
#


@auth.requires_login()
def dX403form0ctrl():
    response.view = 'myadd/dX403form0ctrl.html'
    return dict(grid= mygrid('dX403form0'))
#


@auth.requires_login()
def dfixed_header_menuform0ctrl():
    response.view = 'myadd/dfixed_header_menuform0ctrl.html'
    return dict(grid= mygrid('dfixed_header_menuform0'))
#


@auth.requires_login()
def dfixed_header_mini_sidebarform0ctrl():
    response.view = 'myadd/dfixed_header_mini_sidebarform0ctrl.html'
    return dict(grid= mygrid('dfixed_header_mini_sidebarform0'))
#


@auth.requires_login()
def dpanelform0ctrl():
    response.view = 'myadd/dpanelform0ctrl.html'
    return dict(grid= mygrid('dpanelform0'))
#


@auth.requires_login()
def dfixed_menu_boxedform0ctrl():
    response.view = 'myadd/dfixed_menu_boxedform0ctrl.html'
    return dict(grid= mygrid('dfixed_menu_boxedform0'))
#


@auth.requires_login()
def dfixed_mini_sidebarform0ctrl():
    response.view = 'myadd/dfixed_mini_sidebarform0ctrl.html'
    return dict(grid= mygrid('dfixed_mini_sidebarform0'))
#


@auth.requires_login()
def dno_left_sidebarform0ctrl():
    response.view = 'myadd/dno_left_sidebarform0ctrl.html'
    return dict(grid= mygrid('dno_left_sidebarform0'))
#


@auth.requires_login()
def dX405form0ctrl():
    response.view = 'myadd/dX405form0ctrl.html'
    return dict(grid= mygrid('dX405form0'))
#


@auth.requires_login()
def dfixed_header_boxedform0ctrl():
    response.view = 'myadd/dfixed_header_boxedform0ctrl.html'
    return dict(grid= mygrid('dfixed_header_boxedform0'))
#


@auth.requires_login()
def dtypographyform0ctrl():
    response.view = 'myadd/dtypographyform0ctrl.html'
    return dict(grid= mygrid('dtypographyform0'))
#


@auth.requires_login()
def dsmform0ctrl():
    response.view = 'myadd/dsmform0ctrl.html'
    return dict(grid= mygrid('dsmform0'))
#


@auth.requires_login()
def dprogressform0ctrl():
    response.view = 'myadd/dprogressform0ctrl.html'
    return dict(grid= mygrid('dprogressform0'))
#


@auth.requires_login()
def dalterneform0ctrl():
    response.view = 'myadd/dalterneform0ctrl.html'
    return dict(grid= mygrid('dalterneform0'))
#


@auth.requires_login()
def dofflineform0ctrl():
    response.view = 'myadd/dofflineform0ctrl.html'
    return dict(grid= mygrid('dofflineform0'))
#


@auth.requires_login()
def dblankform0ctrl():
    response.view = 'myadd/dblankform0ctrl.html'
    return dict(grid= mygrid('dblankform0'))
#


@auth.requires_login()
def dcountdownform0ctrl():
    response.view = 'myadd/dcountdownform0ctrl.html'
    return dict(grid= mygrid('dcountdownform0'))
#


@auth.requires_login()
def dcountdownform1ctrl():
    response.view = 'myadd/dcountdownform1ctrl.html'
    return dict(grid= mygrid('dcountdownform1'))
#


@auth.requires_login()
def dform_wysiwygform0ctrl():
    response.view = 'myadd/dform_wysiwygform0ctrl.html'
    return dict(grid= mygrid('dform_wysiwygform0'))
#


@auth.requires_login()
def dform_wysiwygform1ctrl():
    response.view = 'myadd/dform_wysiwygform1ctrl.html'
    return dict(grid= mygrid('dform_wysiwygform1'))
#


@auth.requires_login()
def dform_wysiwygform2ctrl():
    response.view = 'myadd/dform_wysiwygform2ctrl.html'
    return dict(grid= mygrid('dform_wysiwygform2'))
#


@auth.requires_login()
def dpricingform0ctrl():
    response.view = 'myadd/dpricingform0ctrl.html'
    return dict(grid= mygrid('dpricingform0'))
#


@auth.requires_login()
def dbgcolorform0ctrl():
    response.view = 'myadd/dbgcolorform0ctrl.html'
    return dict(grid= mygrid('dbgcolorform0'))
#


@auth.requires_login()
def dcalendarform0ctrl():
    response.view = 'myadd/dcalendarform0ctrl.html'
    return dict(grid= mygrid('dcalendarform0'))
#


@auth.requires_login()
def dno_left_right_sidebarform0ctrl():
    response.view = 'myadd/dno_left_right_sidebarform0ctrl.html'
    return dict(grid= mygrid('dno_left_right_sidebarform0'))
#


@auth.requires_login()
def dform_wizardform0ctrl():
    response.view = 'myadd/dform_wizardform0ctrl.html'
    return dict(grid= mygrid('dform_wizardform0'))
#


@auth.requires_login()
def dform_wizardform1ctrl():
    response.view = 'myadd/dform_wizardform1ctrl.html'
    return dict(grid= mygrid('dform_wizardform1'))
#


@auth.requires_login()
def dfixed_menuform0ctrl():
    response.view = 'myadd/dfixed_menuform0ctrl.html'
    return dict(grid= mygrid('dfixed_menuform0'))
#


@auth.requires_login()
def dfxhmoxedform0ctrl():
    response.view = 'myadd/dfxhmoxedform0ctrl.html'
    return dict(grid= mygrid('dfxhmoxedform0'))
#


@auth.requires_login()
def dX500form0ctrl():
    response.view = 'myadd/dX500form0ctrl.html'
    return dict(grid= mygrid('dX500form0'))
#


@auth.requires_login()
def dform_validationform0ctrl():
    response.view = 'myadd/dform_validationform0ctrl.html'
    return dict(grid= mygrid('dform_validationform0'))
#


@auth.requires_login()
def dform_validationform1ctrl():
    response.view = 'myadd/dform_validationform1ctrl.html'
    return dict(grid= mygrid('dform_validationform1'))
#


@auth.requires_login()
def dform_validationform2ctrl():
    response.view = 'myadd/dform_validationform2ctrl.html'
    return dict(grid= mygrid('dform_validationform2'))
#


@auth.requires_login()
def dform_validationform3ctrl():
    response.view = 'myadd/dform_validationform3ctrl.html'
    return dict(grid= mygrid('dform_validationform3'))
#
