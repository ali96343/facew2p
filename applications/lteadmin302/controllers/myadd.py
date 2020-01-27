

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
    form.element('textarea[name=replace]')['_rows']='4'
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
def languageIImenu():
    db.dlanguage0menu.f0.writable = True
    response.view = 'myadd/language-menu.html'
    return dict(grid= mygrid('dlanguage0menu'))
#


@auth.requires_login()
def inline():
    db.dinline.f0.writable = True
    response.view = 'myadd/inline.html'
    return dict(grid= mygrid('dinline'))
#


@auth.requires_login()
def legacyIIuserIImenu():
    db.dlegacy0user0menu.f0.writable = True
    response.view = 'myadd/legacy-user-menu.html'
    return dict(grid= mygrid('dlegacy0user0menu'))
#


@auth.requires_login()
def readIImail():
    db.dread0mail.f0.writable = True
    response.view = 'myadd/read-mail.html'
    return dict(grid= mygrid('dread0mail'))
#


@auth.requires_login()
def navbar():
    db.dnavbar.f0.writable = True
    response.view = 'myadd/navbar.html'
    return dict(grid= mygrid('dnavbar'))
#


@auth.requires_login()
def projectIIadd():
    db.dproject0add.f0.writable = True
    response.view = 'myadd/project_add.html'
    return dict(grid= mygrid('dproject0add'))
#


@auth.requires_login()
def blank():
    db.dblank.f0.writable = True
    response.view = 'myadd/blank.html'
    return dict(grid= mygrid('dblank'))
#


@auth.requires_login()
def fixedIItopnav():
    db.dfixed0topnav.f0.writable = True
    response.view = 'myadd/fixed-topnav.html'
    return dict(grid= mygrid('dfixed0topnav'))
#


@auth.requires_login()
def advanced():
    db.dadvanced.f0.writable = True
    response.view = 'myadd/advanced.html'
    return dict(grid= mygrid('dadvanced'))
#


@auth.requires_login()
def modals():
    db.dmodals.f0.writable = True
    response.view = 'myadd/modals.html'
    return dict(grid= mygrid('dmodals'))
#


@auth.requires_login()
def fixedIIsidebar():
    db.dfixed0sidebar.f0.writable = True
    response.view = 'myadd/fixed-sidebar.html'
    return dict(grid= mygrid('dfixed0sidebar'))
#


@auth.requires_login()
def invoice():
    db.dinvoice.f0.writable = True
    response.view = 'myadd/invoice.html'
    return dict(grid= mygrid('dinvoice'))
#


@auth.requires_login()
def pace():
    db.dpace.f0.writable = True
    response.view = 'myadd/pace.html'
    return dict(grid= mygrid('dpace'))
#


@auth.requires_login()
def compose():
    db.dcompose.f0.writable = True
    response.view = 'myadd/compose.html'
    return dict(grid= mygrid('dcompose'))
#


@auth.requires_login()
def simple():
    db.dsimple.f0.writable = True
    response.view = 'myadd/simple.html'
    return dict(grid= mygrid('dsimple'))
#


@auth.requires_login()
def contacts():
    db.dcontacts.f0.writable = True
    response.view = 'myadd/contacts.html'
    return dict(grid= mygrid('dcontacts'))
#


@auth.requires_login()
def collapsedIIsidebar():
    db.dcollapsed0sidebar.f0.writable = True
    response.view = 'myadd/collapsed-sidebar.html'
    return dict(grid= mygrid('dcollapsed0sidebar'))
#


@auth.requires_login()
def boxed():
    db.dboxed.f0.writable = True
    response.view = 'myadd/boxed.html'
    return dict(grid= mygrid('dboxed'))
#


@auth.requires_login()
def buttons():
    db.dbuttons.f0.writable = True
    response.view = 'myadd/buttons.html'
    return dict(grid= mygrid('dbuttons'))
#


@auth.requires_login()
def eIIcommerce():
    db.de0commerce.f0.writable = True
    response.view = 'myadd/e_commerce.html'
    return dict(grid= mygrid('de0commerce'))
#


@auth.requires_login()
def editors():
    db.deditors.f0.writable = True
    response.view = 'myadd/editors.html'
    return dict(grid= mygrid('deditors'))
#


@auth.requires_login()
def projectIIdetail():
    db.dproject0detail.f0.writable = True
    response.view = 'myadd/project_detail.html'
    return dict(grid= mygrid('dproject0detail'))
#


@auth.requires_login()
def chartjs():
    db.dchartjs.f0.writable = True
    response.view = 'myadd/chartjs.html'
    return dict(grid= mygrid('dchartjs'))
#


@auth.requires_login()
def ribbons():
    db.dribbons.f0.writable = True
    response.view = 'myadd/ribbons.html'
    return dict(grid= mygrid('dribbons'))
#


@auth.requires_login()
def projectIIedit():
    db.dproject0edit.f0.writable = True
    response.view = 'myadd/project_edit.html'
    return dict(grid= mygrid('dproject0edit'))
#


@auth.requires_login()
def icons():
    db.dicons.f0.writable = True
    response.view = 'myadd/icons.html'
    return dict(grid= mygrid('dicons'))
#


@auth.requires_login()
def index2():
    db.dindex2.f0.writable = True
    response.view = 'myadd/index2.html'
    return dict(grid= mygrid('dindex2'))
#


@auth.requires_login()
def projects():
    db.dprojects.f0.writable = True
    response.view = 'myadd/projects.html'
    return dict(grid= mygrid('dprojects'))
#


@auth.requires_login()
def login():
    db.dlogin.f0.writable = True
    response.view = 'myadd/login.html'
    return dict(grid= mygrid('dlogin'))
#


@auth.requires_login()
def index3():
    db.dindex3.f0.writable = True
    response.view = 'myadd/index3.html'
    return dict(grid= mygrid('dindex3'))
#


@auth.requires_login()
def mailbox():
    db.dmailbox.f0.writable = True
    response.view = 'myadd/mailbox.html'
    return dict(grid= mygrid('dmailbox'))
#


@auth.requires_login()
def recoverIIpassword():
    db.drecover0password.f0.writable = True
    response.view = 'myadd/recover-password.html'
    return dict(grid= mygrid('drecover0password'))
#


@auth.requires_login()
def forgotIIpassword():
    db.dforgot0password.f0.writable = True
    response.view = 'myadd/forgot-password.html'
    return dict(grid= mygrid('dforgot0password'))
#


@auth.requires_login()
def lockscreen():
    db.dlockscreen.f0.writable = True
    response.view = 'myadd/lockscreen.html'
    return dict(grid= mygrid('dlockscreen'))
#


@auth.requires_login()
def sliders():
    db.dsliders.f0.writable = True
    response.view = 'myadd/sliders.html'
    return dict(grid= mygrid('dsliders'))
#


@auth.requires_login()
def profile():
    db.dprofile.f0.writable = True
    response.view = 'myadd/profile.html'
    return dict(grid= mygrid('dprofile'))
#


@auth.requires_login()
def timeline():
    db.dtimeline.f0.writable = True
    response.view = 'myadd/timeline.html'
    return dict(grid= mygrid('dtimeline'))
#


@auth.requires_login()
def register():
    db.dregister.f0.writable = True
    response.view = 'myadd/register.html'
    return dict(grid= mygrid('dregister'))
#


@auth.requires_login()
def validation():
    db.dvalidation.f0.writable = True
    response.view = 'myadd/validation.html'
    return dict(grid= mygrid('dvalidation'))
#


@auth.requires_login()
def gallery():
    db.dgallery.f0.writable = True
    response.view = 'myadd/gallery.html'
    return dict(grid= mygrid('dgallery'))
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
def calendar():
    db.dcalendar.f0.writable = True
    response.view = 'myadd/calendar.html'
    return dict(grid= mygrid('dcalendar'))
#


@auth.requires_login()
def X500():
    db.d500.f0.writable = True
    response.view = 'myadd/500.html'
    return dict(grid= mygrid('d500'))
#


@auth.requires_login()
def topIInav():
    db.dtop0nav.f0.writable = True
    response.view = 'myadd/top-nav.html'
    return dict(grid= mygrid('dtop0nav'))
#


@auth.requires_login()
def general():
    db.dgeneral.f0.writable = True
    response.view = 'myadd/general.html'
    return dict(grid= mygrid('dgeneral'))
#


@auth.requires_login()
def fixedIIfooter():
    db.dfixed0footer.f0.writable = True
    response.view = 'myadd/fixed-footer.html'
    return dict(grid= mygrid('dfixed0footer'))
#


@auth.requires_login()
def jsgrid():
    db.djsgrid.f0.writable = True
    response.view = 'myadd/jsgrid.html'
    return dict(grid= mygrid('djsgrid'))
#


@auth.requires_login()
def starter():
    db.dstarter.f0.writable = True
    response.view = 'myadd/starter.html'
    return dict(grid= mygrid('dstarter'))
#


@auth.requires_login()
def flot():
    db.dflot.f0.writable = True
    response.view = 'myadd/flot.html'
    return dict(grid= mygrid('dflot'))
#


@auth.requires_login()
def topIInavIIsidebar():
    db.dtop0nav0sidebar.f0.writable = True
    response.view = 'myadd/top-nav-sidebar.html'
    return dict(grid= mygrid('dtop0nav0sidebar'))
#


@auth.requires_login()
def data():
    db.ddata.f0.writable = True
    response.view = 'myadd/data.html'
    return dict(grid= mygrid('ddata'))
#


@auth.requires_login()
def X404():
    db.d404.f0.writable = True
    response.view = 'myadd/404.html'
    return dict(grid= mygrid('d404'))
#


@auth.requires_login()
def invoiceIIprint():
    db.dinvoice0print.f0.writable = True
    response.view = 'myadd/invoice-print.html'
    return dict(grid= mygrid('dinvoice0print'))
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
def project_edittable0ctrl():
    response.view = 'myadd/project_edittable0ctrl.html'
    return dict(grid= mygrid('project_edittable0'))
#


@auth.requires_login()
def index3table0ctrl():
    response.view = 'myadd/index3table0ctrl.html'
    return dict(grid= mygrid('index3table0'))
#


@auth.requires_login()
def simpletable0ctrl():
    response.view = 'myadd/simpletable0ctrl.html'
    return dict(grid= mygrid('simpletable0'))
#


@auth.requires_login()
def simpletable1ctrl():
    response.view = 'myadd/simpletable1ctrl.html'
    return dict(grid= mygrid('simpletable1'))
#


@auth.requires_login()
def simpletable2ctrl():
    response.view = 'myadd/simpletable2ctrl.html'
    return dict(grid= mygrid('simpletable2'))
#


@auth.requires_login()
def simpletable3ctrl():
    response.view = 'myadd/simpletable3ctrl.html'
    return dict(grid= mygrid('simpletable3'))
#


@auth.requires_login()
def simpletable4ctrl():
    response.view = 'myadd/simpletable4ctrl.html'
    return dict(grid= mygrid('simpletable4'))
#


@auth.requires_login()
def simpletable5ctrl():
    response.view = 'myadd/simpletable5ctrl.html'
    return dict(grid= mygrid('simpletable5'))
#


@auth.requires_login()
def datatable0ctrl():
    response.view = 'myadd/datatable0ctrl.html'
    return dict(grid= mygrid('datatable0'))
#


@auth.requires_login()
def datatable1ctrl():
    response.view = 'myadd/datatable1ctrl.html'
    return dict(grid= mygrid('datatable1'))
#


@auth.requires_login()
def invoicetable0ctrl():
    response.view = 'myadd/invoicetable0ctrl.html'
    return dict(grid= mygrid('invoicetable0'))
#


@auth.requires_login()
def invoice0printtable0ctrl():
    response.view = 'myadd/invoice0printtable0ctrl.html'
    return dict(grid= mygrid('invoice0printtable0'))
#


@auth.requires_login()
def projectstable0ctrl():
    response.view = 'myadd/projectstable0ctrl.html'
    return dict(grid= mygrid('projectstable0'))
#


@auth.requires_login()
def index2table0ctrl():
    response.view = 'myadd/index2table0ctrl.html'
    return dict(grid= mygrid('index2table0'))
#


@auth.requires_login()
def dboxedform0ctrl():
    response.view = 'myadd/dboxedform0ctrl.html'
    return dict(grid= mygrid('dboxedform0'))
#


@auth.requires_login()
def dprojectIIeditform0ctrl():
    response.view = 'myadd/dprojectIIeditform0ctrl.html'
    return dict(grid= mygrid('dprojectIIeditform0'))
#


@auth.requires_login()
def dribbonsform0ctrl():
    response.view = 'myadd/dribbonsform0ctrl.html'
    return dict(grid= mygrid('dribbonsform0'))
#


@auth.requires_login()
def dgalleryform0ctrl():
    response.view = 'myadd/dgalleryform0ctrl.html'
    return dict(grid= mygrid('dgalleryform0'))
#


@auth.requires_login()
def diconsform0ctrl():
    response.view = 'myadd/diconsform0ctrl.html'
    return dict(grid= mygrid('diconsform0'))
#


@auth.requires_login()
def dindex3form0ctrl():
    response.view = 'myadd/dindex3form0ctrl.html'
    return dict(grid= mygrid('dindex3form0'))
#


@auth.requires_login()
def dinlineform0ctrl():
    response.view = 'myadd/dinlineform0ctrl.html'
    return dict(grid= mygrid('dinlineform0'))
#


@auth.requires_login()
def dadvancedform0ctrl():
    response.view = 'myadd/dadvancedform0ctrl.html'
    return dict(grid= mygrid('dadvancedform0'))
#


@auth.requires_login()
def dvalidationform0ctrl():
    response.view = 'myadd/dvalidationform0ctrl.html'
    return dict(grid= mygrid('dvalidationform0'))
#


@auth.requires_login()
def dvalidationform1ctrl():
    response.view = 'myadd/dvalidationform1ctrl.html'
    return dict(grid= mygrid('dvalidationform1'))
#


@auth.requires_login()
def dfixedIIsidebarform0ctrl():
    response.view = 'myadd/dfixedIIsidebarform0ctrl.html'
    return dict(grid= mygrid('dfixedIIsidebarform0'))
#


@auth.requires_login()
def dX404form0ctrl():
    response.view = 'myadd/dX404form0ctrl.html'
    return dict(grid= mygrid('dX404form0'))
#


@auth.requires_login()
def dX404form1ctrl():
    response.view = 'myadd/dX404form1ctrl.html'
    return dict(grid= mygrid('dX404form1'))
#


@auth.requires_login()
def dcollapsedIIsidebarform0ctrl():
    response.view = 'myadd/dcollapsedIIsidebarform0ctrl.html'
    return dict(grid= mygrid('dcollapsedIIsidebarform0'))
#


@auth.requires_login()
def dforgotIIpasswordform0ctrl():
    response.view = 'myadd/dforgotIIpasswordform0ctrl.html'
    return dict(grid= mygrid('dforgotIIpasswordform0'))
#


@auth.requires_login()
def dstarterform0ctrl():
    response.view = 'myadd/dstarterform0ctrl.html'
    return dict(grid= mygrid('dstarterform0'))
#


@auth.requires_login()
def djsgridform0ctrl():
    response.view = 'myadd/djsgridform0ctrl.html'
    return dict(grid= mygrid('djsgridform0'))
#


@auth.requires_login()
def dindexform0ctrl():
    response.view = 'myadd/dindexform0ctrl.html'
    return dict(grid= mygrid('dindexform0'))
#


@auth.requires_login()
def dindexform1ctrl():
    response.view = 'myadd/dindexform1ctrl.html'
    return dict(grid= mygrid('dindexform1'))
#


@auth.requires_login()
def dgeneralform0ctrl():
    response.view = 'myadd/dgeneralform0ctrl.html'
    return dict(grid= mygrid('dgeneralform0'))
#


@auth.requires_login()
def dbuttonsform0ctrl():
    response.view = 'myadd/dbuttonsform0ctrl.html'
    return dict(grid= mygrid('dbuttonsform0'))
#


@auth.requires_login()
def dreadIImailform0ctrl():
    response.view = 'myadd/dreadIImailform0ctrl.html'
    return dict(grid= mygrid('dreadIImailform0'))
#


@auth.requires_login()
def dsimpleform0ctrl():
    response.view = 'myadd/dsimpleform0ctrl.html'
    return dict(grid= mygrid('dsimpleform0'))
#


@auth.requires_login()
def ddataform0ctrl():
    response.view = 'myadd/ddataform0ctrl.html'
    return dict(grid= mygrid('ddataform0'))
#


@auth.requires_login()
def dloginform0ctrl():
    response.view = 'myadd/dloginform0ctrl.html'
    return dict(grid= mygrid('dloginform0'))
#


@auth.requires_login()
def dnavbarform0ctrl():
    response.view = 'myadd/dnavbarform0ctrl.html'
    return dict(grid= mygrid('dnavbarform0'))
#


@auth.requires_login()
def dnavbarform1ctrl():
    response.view = 'myadd/dnavbarform1ctrl.html'
    return dict(grid= mygrid('dnavbarform1'))
#


@auth.requires_login()
def dnavbarform2ctrl():
    response.view = 'myadd/dnavbarform2ctrl.html'
    return dict(grid= mygrid('dnavbarform2'))
#


@auth.requires_login()
def dnavbarform3ctrl():
    response.view = 'myadd/dnavbarform3ctrl.html'
    return dict(grid= mygrid('dnavbarform3'))
#


@auth.requires_login()
def dnavbarform4ctrl():
    response.view = 'myadd/dnavbarform4ctrl.html'
    return dict(grid= mygrid('dnavbarform4'))
#


@auth.requires_login()
def dnavbarform5ctrl():
    response.view = 'myadd/dnavbarform5ctrl.html'
    return dict(grid= mygrid('dnavbarform5'))
#


@auth.requires_login()
def dnavbarform6ctrl():
    response.view = 'myadd/dnavbarform6ctrl.html'
    return dict(grid= mygrid('dnavbarform6'))
#


@auth.requires_login()
def drecoverIIpasswordform0ctrl():
    response.view = 'myadd/drecoverIIpasswordform0ctrl.html'
    return dict(grid= mygrid('drecoverIIpasswordform0'))
#


@auth.requires_login()
def dprofileform0ctrl():
    response.view = 'myadd/dprofileform0ctrl.html'
    return dict(grid= mygrid('dprofileform0'))
#


@auth.requires_login()
def dprofileform1ctrl():
    response.view = 'myadd/dprofileform1ctrl.html'
    return dict(grid= mygrid('dprofileform1'))
#


@auth.requires_login()
def dprofileform2ctrl():
    response.view = 'myadd/dprofileform2ctrl.html'
    return dict(grid= mygrid('dprofileform2'))
#


@auth.requires_login()
def deditorsform0ctrl():
    response.view = 'myadd/deditorsform0ctrl.html'
    return dict(grid= mygrid('deditorsform0'))
#


@auth.requires_login()
def dinvoiceform0ctrl():
    response.view = 'myadd/dinvoiceform0ctrl.html'
    return dict(grid= mygrid('dinvoiceform0'))
#


@auth.requires_login()
def dfixedIItopnavform0ctrl():
    response.view = 'myadd/dfixedIItopnavform0ctrl.html'
    return dict(grid= mygrid('dfixedIItopnavform0'))
#


@auth.requires_login()
def dlockscreenform0ctrl():
    response.view = 'myadd/dlockscreenform0ctrl.html'
    return dict(grid= mygrid('dlockscreenform0'))
#


@auth.requires_login()
def dtopIInavIIsidebarform0ctrl():
    response.view = 'myadd/dtopIInavIIsidebarform0ctrl.html'
    return dict(grid= mygrid('dtopIInavIIsidebarform0'))
#


@auth.requires_login()
def dcomposeform0ctrl():
    response.view = 'myadd/dcomposeform0ctrl.html'
    return dict(grid= mygrid('dcomposeform0'))
#


@auth.requires_login()
def dprojectIIdetailform0ctrl():
    response.view = 'myadd/dprojectIIdetailform0ctrl.html'
    return dict(grid= mygrid('dprojectIIdetailform0'))
#


@auth.requires_login()
def dfixedIIfooterform0ctrl():
    response.view = 'myadd/dfixedIIfooterform0ctrl.html'
    return dict(grid= mygrid('dfixedIIfooterform0'))
#


@auth.requires_login()
def dblankform0ctrl():
    response.view = 'myadd/dblankform0ctrl.html'
    return dict(grid= mygrid('dblankform0'))
#


@auth.requires_login()
def dlegacyIIuserIImenuform0ctrl():
    response.view = 'myadd/dlegacyIIuserIImenuform0ctrl.html'
    return dict(grid= mygrid('dlegacyIIuserIImenuform0'))
#


@auth.requires_login()
def dtopIInavform0ctrl():
    response.view = 'myadd/dtopIInavform0ctrl.html'
    return dict(grid= mygrid('dtopIInavform0'))
#


@auth.requires_login()
def dcontactsform0ctrl():
    response.view = 'myadd/dcontactsform0ctrl.html'
    return dict(grid= mygrid('dcontactsform0'))
#


@auth.requires_login()
def dcalendarform0ctrl():
    response.view = 'myadd/dcalendarform0ctrl.html'
    return dict(grid= mygrid('dcalendarform0'))
#


@auth.requires_login()
def dmailboxform0ctrl():
    response.view = 'myadd/dmailboxform0ctrl.html'
    return dict(grid= mygrid('dmailboxform0'))
#


@auth.requires_login()
def dpaceform0ctrl():
    response.view = 'myadd/dpaceform0ctrl.html'
    return dict(grid= mygrid('dpaceform0'))
#


@auth.requires_login()
def dflotform0ctrl():
    response.view = 'myadd/dflotform0ctrl.html'
    return dict(grid= mygrid('dflotform0'))
#


@auth.requires_login()
def dprojectIIaddform0ctrl():
    response.view = 'myadd/dprojectIIaddform0ctrl.html'
    return dict(grid= mygrid('dprojectIIaddform0'))
#


@auth.requires_login()
def dchartjsform0ctrl():
    response.view = 'myadd/dchartjsform0ctrl.html'
    return dict(grid= mygrid('dchartjsform0'))
#


@auth.requires_login()
def dwidgetsform0ctrl():
    response.view = 'myadd/dwidgetsform0ctrl.html'
    return dict(grid= mygrid('dwidgetsform0'))
#


@auth.requires_login()
def dwidgetsform1ctrl():
    response.view = 'myadd/dwidgetsform1ctrl.html'
    return dict(grid= mygrid('dwidgetsform1'))
#


@auth.requires_login()
def dwidgetsform2ctrl():
    response.view = 'myadd/dwidgetsform2ctrl.html'
    return dict(grid= mygrid('dwidgetsform2'))
#


@auth.requires_login()
def dwidgetsform3ctrl():
    response.view = 'myadd/dwidgetsform3ctrl.html'
    return dict(grid= mygrid('dwidgetsform3'))
#


@auth.requires_login()
def dwidgetsform4ctrl():
    response.view = 'myadd/dwidgetsform4ctrl.html'
    return dict(grid= mygrid('dwidgetsform4'))
#


@auth.requires_login()
def dwidgetsform5ctrl():
    response.view = 'myadd/dwidgetsform5ctrl.html'
    return dict(grid= mygrid('dwidgetsform5'))
#


@auth.requires_login()
def dwidgetsform6ctrl():
    response.view = 'myadd/dwidgetsform6ctrl.html'
    return dict(grid= mygrid('dwidgetsform6'))
#


@auth.requires_login()
def dprojectsform0ctrl():
    response.view = 'myadd/dprojectsform0ctrl.html'
    return dict(grid= mygrid('dprojectsform0'))
#


@auth.requires_login()
def dlanguageIImenuform0ctrl():
    response.view = 'myadd/dlanguageIImenuform0ctrl.html'
    return dict(grid= mygrid('dlanguageIImenuform0'))
#


@auth.requires_login()
def dslidersform0ctrl():
    response.view = 'myadd/dslidersform0ctrl.html'
    return dict(grid= mygrid('dslidersform0'))
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
def dtimelineform0ctrl():
    response.view = 'myadd/dtimelineform0ctrl.html'
    return dict(grid= mygrid('dtimelineform0'))
#


@auth.requires_login()
def dindex2form0ctrl():
    response.view = 'myadd/dindex2form0ctrl.html'
    return dict(grid= mygrid('dindex2form0'))
#


@auth.requires_login()
def dindex2form1ctrl():
    response.view = 'myadd/dindex2form1ctrl.html'
    return dict(grid= mygrid('dindex2form1'))
#


@auth.requires_login()
def deIIcommerceform0ctrl():
    response.view = 'myadd/deIIcommerceform0ctrl.html'
    return dict(grid= mygrid('deIIcommerceform0'))
#


@auth.requires_login()
def dX500form0ctrl():
    response.view = 'myadd/dX500form0ctrl.html'
    return dict(grid= mygrid('dX500form0'))
#


@auth.requires_login()
def dX500form1ctrl():
    response.view = 'myadd/dX500form1ctrl.html'
    return dict(grid= mygrid('dX500form1'))
#
