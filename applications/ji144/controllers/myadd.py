

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
def ui_alerts():
    db.dui0alerts.f0.writable = True
    response.view = 'myadd/ui-alerts.html'
    return dict(grid= mygrid('dui0alerts'))
#


@auth.requires_login()
def page_register():
    db.dpage0register.f0.writable = True
    response.view = 'myadd/page-register.html'
    return dict(grid= mygrid('dpage0register'))
#


@auth.requires_login()
def ui_switches():
    db.dui0switches.f0.writable = True
    response.view = 'myadd/ui-switches.html'
    return dict(grid= mygrid('dui0switches'))
#


@auth.requires_login()
def page_login():
    db.dpage0login.f0.writable = True
    response.view = 'myadd/page-login.html'
    return dict(grid= mygrid('dpage0login'))
#


@auth.requires_login()
def ui_badges():
    db.dui0badges.f0.writable = True
    response.view = 'myadd/ui-badges.html'
    return dict(grid= mygrid('dui0badges'))
#


@auth.requires_login()
def tables_data():
    db.dtables0data.f0.writable = True
    response.view = 'myadd/tables-data.html'
    return dict(grid= mygrid('dtables0data'))
#


@auth.requires_login()
def charts_peity():
    db.dcharts0peity.f0.writable = True
    response.view = 'myadd/charts-peity.html'
    return dict(grid= mygrid('dcharts0peity'))
#


@auth.requires_login()
def ui_tabs():
    db.dui0tabs.f0.writable = True
    response.view = 'myadd/ui-tabs.html'
    return dict(grid= mygrid('dui0tabs'))
#


@auth.requires_login()
def tables_basic():
    db.dtables0basic.f0.writable = True
    response.view = 'myadd/tables-basic.html'
    return dict(grid= mygrid('dtables0basic'))
#


@auth.requires_login()
def font_themify():
    db.dfont0themify.f0.writable = True
    response.view = 'myadd/font-themify.html'
    return dict(grid= mygrid('dfont0themify'))
#


@auth.requires_login()
def ui_cards():
    db.dui0cards.f0.writable = True
    response.view = 'myadd/ui-cards.html'
    return dict(grid= mygrid('dui0cards'))
#


@auth.requires_login()
def frame():
    db.dframe.f0.writable = True
    response.view = 'myadd/frame.html'
    return dict(grid= mygrid('dframe'))
#


@auth.requires_login()
def ui_typgraphy():
    db.dui0typgraphy.f0.writable = True
    response.view = 'myadd/ui-typgraphy.html'
    return dict(grid= mygrid('dui0typgraphy'))
#


@auth.requires_login()
def forms_advanced():
    db.dforms0advanced.f0.writable = True
    response.view = 'myadd/forms-advanced.html'
    return dict(grid= mygrid('dforms0advanced'))
#


@auth.requires_login()
def charts_chartjs():
    db.dcharts0chartjs.f0.writable = True
    response.view = 'myadd/charts-chartjs.html'
    return dict(grid= mygrid('dcharts0chartjs'))
#


@auth.requires_login()
def charts_flot():
    db.dcharts0flot.f0.writable = True
    response.view = 'myadd/charts-flot.html'
    return dict(grid= mygrid('dcharts0flot'))
#


@auth.requires_login()
def ui_progressbar():
    db.dui0progressbar.f0.writable = True
    response.view = 'myadd/ui-progressbar.html'
    return dict(grid= mygrid('dui0progressbar'))
#


@auth.requires_login()
def maps_gmap():
    db.dmaps0gmap.f0.writable = True
    response.view = 'myadd/maps-gmap.html'
    return dict(grid= mygrid('dmaps0gmap'))
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
def ui_buttons():
    db.dui0buttons.f0.writable = True
    response.view = 'myadd/ui-buttons.html'
    return dict(grid= mygrid('dui0buttons'))
#


@auth.requires_login()
def forms_basic():
    db.dforms0basic.f0.writable = True
    response.view = 'myadd/forms-basic.html'
    return dict(grid= mygrid('dforms0basic'))
#


@auth.requires_login()
def pages_forget():
    db.dpages0forget.f0.writable = True
    response.view = 'myadd/pages-forget.html'
    return dict(grid= mygrid('dpages0forget'))
#


@auth.requires_login()
def ui_social_buttons():
    db.dui0social0buttons.f0.writable = True
    response.view = 'myadd/ui-social-buttons.html'
    return dict(grid= mygrid('dui0social0buttons'))
#


@auth.requires_login()
def ui_grids():
    db.dui0grids.f0.writable = True
    response.view = 'myadd/ui-grids.html'
    return dict(grid= mygrid('dui0grids'))
#


@auth.requires_login()
def ui_modals():
    db.dui0modals.f0.writable = True
    response.view = 'myadd/ui-modals.html'
    return dict(grid= mygrid('dui0modals'))
#


@auth.requires_login()
def font_fontawesome():
    db.dfont0fontawesome.f0.writable = True
    response.view = 'myadd/font-fontawesome.html'
    return dict(grid= mygrid('dfont0fontawesome'))
#


@auth.requires_login()
def maps_vector():
    db.dmaps0vector.f0.writable = True
    response.view = 'myadd/maps-vector.html'
    return dict(grid= mygrid('dmaps0vector'))
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
def ui0switchestable0ctrl():
    response.view = 'myadd/ui0switchestable0ctrl.html'
    return dict(grid= mygrid('ui0switchestable0'))
#


@auth.requires_login()
def tables0datatable0ctrl():
    response.view = 'myadd/tables0datatable0ctrl.html'
    return dict(grid= mygrid('tables0datatable0'))
#


@auth.requires_login()
def tables0basictable0ctrl():
    response.view = 'myadd/tables0basictable0ctrl.html'
    return dict(grid= mygrid('tables0basictable0'))
#


@auth.requires_login()
def tables0basictable1ctrl():
    response.view = 'myadd/tables0basictable1ctrl.html'
    return dict(grid= mygrid('tables0basictable1'))
#


@auth.requires_login()
def tables0basictable2ctrl():
    response.view = 'myadd/tables0basictable2ctrl.html'
    return dict(grid= mygrid('tables0basictable2'))
#


@auth.requires_login()
def tables0basictable3ctrl():
    response.view = 'myadd/tables0basictable3ctrl.html'
    return dict(grid= mygrid('tables0basictable3'))
#


@auth.requires_login()
def tables0basictable4ctrl():
    response.view = 'myadd/tables0basictable4ctrl.html'
    return dict(grid= mygrid('tables0basictable4'))
#


@auth.requires_login()
def tables0basictable5ctrl():
    response.view = 'myadd/tables0basictable5ctrl.html'
    return dict(grid= mygrid('tables0basictable5'))
#


@auth.requires_login()
def dui_switchesform0ctrl():
    response.view = 'myadd/dui_switchesform0ctrl.html'
    return dict(grid= mygrid('dui_switchesform0'))
#


@auth.requires_login()
def dmaps_gmapform0ctrl():
    response.view = 'myadd/dmaps_gmapform0ctrl.html'
    return dict(grid= mygrid('dmaps_gmapform0'))
#


@auth.requires_login()
def dui_progressbarform0ctrl():
    response.view = 'myadd/dui_progressbarform0ctrl.html'
    return dict(grid= mygrid('dui_progressbarform0'))
#


@auth.requires_login()
def dfont_fontawesomeform0ctrl():
    response.view = 'myadd/dfont_fontawesomeform0ctrl.html'
    return dict(grid= mygrid('dfont_fontawesomeform0'))
#


@auth.requires_login()
def dui_tabsform0ctrl():
    response.view = 'myadd/dui_tabsform0ctrl.html'
    return dict(grid= mygrid('dui_tabsform0'))
#


@auth.requires_login()
def dpage_registerform0ctrl():
    response.view = 'myadd/dpage_registerform0ctrl.html'
    return dict(grid= mygrid('dpage_registerform0'))
#


@auth.requires_login()
def dcharts_peityform0ctrl():
    response.view = 'myadd/dcharts_peityform0ctrl.html'
    return dict(grid= mygrid('dcharts_peityform0'))
#


@auth.requires_login()
def dfont_themifyform0ctrl():
    response.view = 'myadd/dfont_themifyform0ctrl.html'
    return dict(grid= mygrid('dfont_themifyform0'))
#


@auth.requires_login()
def dindexform0ctrl():
    response.view = 'myadd/dindexform0ctrl.html'
    return dict(grid= mygrid('dindexform0'))
#


@auth.requires_login()
def dframeform0ctrl():
    response.view = 'myadd/dframeform0ctrl.html'
    return dict(grid= mygrid('dframeform0'))
#


@auth.requires_login()
def dforms_advancedform0ctrl():
    response.view = 'myadd/dforms_advancedform0ctrl.html'
    return dict(grid= mygrid('dforms_advancedform0'))
#


@auth.requires_login()
def dcharts_chartjsform0ctrl():
    response.view = 'myadd/dcharts_chartjsform0ctrl.html'
    return dict(grid= mygrid('dcharts_chartjsform0'))
#


@auth.requires_login()
def dmaps_vectorform0ctrl():
    response.view = 'myadd/dmaps_vectorform0ctrl.html'
    return dict(grid= mygrid('dmaps_vectorform0'))
#


@auth.requires_login()
def dpages_forgetform0ctrl():
    response.view = 'myadd/dpages_forgetform0ctrl.html'
    return dict(grid= mygrid('dpages_forgetform0'))
#


@auth.requires_login()
def dtables_dataform0ctrl():
    response.view = 'myadd/dtables_dataform0ctrl.html'
    return dict(grid= mygrid('dtables_dataform0'))
#


@auth.requires_login()
def dcharts_flotform0ctrl():
    response.view = 'myadd/dcharts_flotform0ctrl.html'
    return dict(grid= mygrid('dcharts_flotform0'))
#


@auth.requires_login()
def dui_badgesform0ctrl():
    response.view = 'myadd/dui_badgesform0ctrl.html'
    return dict(grid= mygrid('dui_badgesform0'))
#


@auth.requires_login()
def dui_modalsform0ctrl():
    response.view = 'myadd/dui_modalsform0ctrl.html'
    return dict(grid= mygrid('dui_modalsform0'))
#


@auth.requires_login()
def dui_buttonsform0ctrl():
    response.view = 'myadd/dui_buttonsform0ctrl.html'
    return dict(grid= mygrid('dui_buttonsform0'))
#


@auth.requires_login()
def dforms_basicform0ctrl():
    response.view = 'myadd/dforms_basicform0ctrl.html'
    return dict(grid= mygrid('dforms_basicform0'))
#


@auth.requires_login()
def dforms_basicform1ctrl():
    response.view = 'myadd/dforms_basicform1ctrl.html'
    return dict(grid= mygrid('dforms_basicform1'))
#


@auth.requires_login()
def dforms_basicform2ctrl():
    response.view = 'myadd/dforms_basicform2ctrl.html'
    return dict(grid= mygrid('dforms_basicform2'))
#


@auth.requires_login()
def dforms_basicform3ctrl():
    response.view = 'myadd/dforms_basicform3ctrl.html'
    return dict(grid= mygrid('dforms_basicform3'))
#


@auth.requires_login()
def dforms_basicform4ctrl():
    response.view = 'myadd/dforms_basicform4ctrl.html'
    return dict(grid= mygrid('dforms_basicform4'))
#


@auth.requires_login()
def dforms_basicform5ctrl():
    response.view = 'myadd/dforms_basicform5ctrl.html'
    return dict(grid= mygrid('dforms_basicform5'))
#


@auth.requires_login()
def dforms_basicform6ctrl():
    response.view = 'myadd/dforms_basicform6ctrl.html'
    return dict(grid= mygrid('dforms_basicform6'))
#


@auth.requires_login()
def dforms_basicform7ctrl():
    response.view = 'myadd/dforms_basicform7ctrl.html'
    return dict(grid= mygrid('dforms_basicform7'))
#


@auth.requires_login()
def dforms_basicform8ctrl():
    response.view = 'myadd/dforms_basicform8ctrl.html'
    return dict(grid= mygrid('dforms_basicform8'))
#


@auth.requires_login()
def dforms_basicform9ctrl():
    response.view = 'myadd/dforms_basicform9ctrl.html'
    return dict(grid= mygrid('dforms_basicform9'))
#


@auth.requires_login()
def dforms_basicform10ctrl():
    response.view = 'myadd/dforms_basicform10ctrl.html'
    return dict(grid= mygrid('dforms_basicform10'))
#


@auth.requires_login()
def dforms_basicform11ctrl():
    response.view = 'myadd/dforms_basicform11ctrl.html'
    return dict(grid= mygrid('dforms_basicform11'))
#


@auth.requires_login()
def dforms_basicform12ctrl():
    response.view = 'myadd/dforms_basicform12ctrl.html'
    return dict(grid= mygrid('dforms_basicform12'))
#


@auth.requires_login()
def dforms_basicform13ctrl():
    response.view = 'myadd/dforms_basicform13ctrl.html'
    return dict(grid= mygrid('dforms_basicform13'))
#


@auth.requires_login()
def dforms_basicform14ctrl():
    response.view = 'myadd/dforms_basicform14ctrl.html'
    return dict(grid= mygrid('dforms_basicform14'))
#


@auth.requires_login()
def dforms_basicform15ctrl():
    response.view = 'myadd/dforms_basicform15ctrl.html'
    return dict(grid= mygrid('dforms_basicform15'))
#


@auth.requires_login()
def dui_gridsform0ctrl():
    response.view = 'myadd/dui_gridsform0ctrl.html'
    return dict(grid= mygrid('dui_gridsform0'))
#


@auth.requires_login()
def dui_social_buttonsform0ctrl():
    response.view = 'myadd/dui_social_buttonsform0ctrl.html'
    return dict(grid= mygrid('dui_social_buttonsform0'))
#


@auth.requires_login()
def dui_typgraphyform0ctrl():
    response.view = 'myadd/dui_typgraphyform0ctrl.html'
    return dict(grid= mygrid('dui_typgraphyform0'))
#


@auth.requires_login()
def dwidgetsform0ctrl():
    response.view = 'myadd/dwidgetsform0ctrl.html'
    return dict(grid= mygrid('dwidgetsform0'))
#


@auth.requires_login()
def dtables_basicform0ctrl():
    response.view = 'myadd/dtables_basicform0ctrl.html'
    return dict(grid= mygrid('dtables_basicform0'))
#


@auth.requires_login()
def dui_alertsform0ctrl():
    response.view = 'myadd/dui_alertsform0ctrl.html'
    return dict(grid= mygrid('dui_alertsform0'))
#


@auth.requires_login()
def dpage_loginform0ctrl():
    response.view = 'myadd/dpage_loginform0ctrl.html'
    return dict(grid= mygrid('dpage_loginform0'))
#


@auth.requires_login()
def dui_cardsform0ctrl():
    response.view = 'myadd/dui_cardsform0ctrl.html'
    return dict(grid= mygrid('dui_cardsform0'))
#
