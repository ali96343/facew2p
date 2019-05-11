

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
def blank():
    db.dblank.f0.writable = True
    response.view = 'myadd/blank.html'
    return dict(grid= mygrid('dblank'))
#


@auth.requires_login()
def charts():
    db.dcharts.f0.writable = True
    response.view = 'myadd/charts.html'
    return dict(grid= mygrid('dcharts'))
#


@auth.requires_login()
def buttons():
    db.dbuttons.f0.writable = True
    response.view = 'myadd/buttons.html'
    return dict(grid= mygrid('dbuttons'))
#


@auth.requires_login()
def utilities_color():
    db.dutilities0color.f0.writable = True
    response.view = 'myadd/utilities-color.html'
    return dict(grid= mygrid('dutilities0color'))
#


@auth.requires_login()
def cards():
    db.dcards.f0.writable = True
    response.view = 'myadd/cards.html'
    return dict(grid= mygrid('dcards'))
#


@auth.requires_login()
def utilities_other():
    db.dutilities0other.f0.writable = True
    response.view = 'myadd/utilities-other.html'
    return dict(grid= mygrid('dutilities0other'))
#


@auth.requires_login()
def tables():
    db.dtables.f0.writable = True
    response.view = 'myadd/tables.html'
    return dict(grid= mygrid('dtables'))
#


@auth.requires_login()
def utilities_border():
    db.dutilities0border.f0.writable = True
    response.view = 'myadd/utilities-border.html'
    return dict(grid= mygrid('dutilities0border'))
#


@auth.requires_login()
def login():
    db.dlogin.f0.writable = True
    response.view = 'myadd/login.html'
    return dict(grid= mygrid('dlogin'))
#


@auth.requires_login()
def forgot_password():
    db.dforgot0password.f0.writable = True
    response.view = 'myadd/forgot-password.html'
    return dict(grid= mygrid('dforgot0password'))
#


@auth.requires_login()
def register():
    db.dregister.f0.writable = True
    response.view = 'myadd/register.html'
    return dict(grid= mygrid('dregister'))
#


@auth.requires_login()
def utilities_animation():
    db.dutilities0animation.f0.writable = True
    response.view = 'myadd/utilities-animation.html'
    return dict(grid= mygrid('dutilities0animation'))
#


@auth.requires_login()
def table_index1():
    db.dindex.f0.writable = True
    response.view = 'myadd/table_index1.html'
    return dict(grid= mygrid('dindex'))
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
def tablestable0ctrl():
    response.view = 'myadd/tablestable0ctrl.html'
    return dict(grid= mygrid('tablestable0'))
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
def dblankform0ctrl():
    response.view = 'myadd/dblankform0ctrl.html'
    return dict(grid= mygrid('dblankform0'))
#


@auth.requires_login()
def dblankform1ctrl():
    response.view = 'myadd/dblankform1ctrl.html'
    return dict(grid= mygrid('dblankform1'))
#


@auth.requires_login()
def dbuttonsform0ctrl():
    response.view = 'myadd/dbuttonsform0ctrl.html'
    return dict(grid= mygrid('dbuttonsform0'))
#


@auth.requires_login()
def dbuttonsform1ctrl():
    response.view = 'myadd/dbuttonsform1ctrl.html'
    return dict(grid= mygrid('dbuttonsform1'))
#


@auth.requires_login()
def dchartsform0ctrl():
    response.view = 'myadd/dchartsform0ctrl.html'
    return dict(grid= mygrid('dchartsform0'))
#


@auth.requires_login()
def dchartsform1ctrl():
    response.view = 'myadd/dchartsform1ctrl.html'
    return dict(grid= mygrid('dchartsform1'))
#


@auth.requires_login()
def dutilities_otherform0ctrl():
    response.view = 'myadd/dutilities_otherform0ctrl.html'
    return dict(grid= mygrid('dutilities_otherform0'))
#


@auth.requires_login()
def dutilities_otherform1ctrl():
    response.view = 'myadd/dutilities_otherform1ctrl.html'
    return dict(grid= mygrid('dutilities_otherform1'))
#


@auth.requires_login()
def dutilities_animationform0ctrl():
    response.view = 'myadd/dutilities_animationform0ctrl.html'
    return dict(grid= mygrid('dutilities_animationform0'))
#


@auth.requires_login()
def dutilities_animationform1ctrl():
    response.view = 'myadd/dutilities_animationform1ctrl.html'
    return dict(grid= mygrid('dutilities_animationform1'))
#


@auth.requires_login()
def dutilities_borderform0ctrl():
    response.view = 'myadd/dutilities_borderform0ctrl.html'
    return dict(grid= mygrid('dutilities_borderform0'))
#


@auth.requires_login()
def dutilities_borderform1ctrl():
    response.view = 'myadd/dutilities_borderform1ctrl.html'
    return dict(grid= mygrid('dutilities_borderform1'))
#


@auth.requires_login()
def dloginform0ctrl():
    response.view = 'myadd/dloginform0ctrl.html'
    return dict(grid= mygrid('dloginform0'))
#


@auth.requires_login()
def dregisterform0ctrl():
    response.view = 'myadd/dregisterform0ctrl.html'
    return dict(grid= mygrid('dregisterform0'))
#


@auth.requires_login()
def dtablesform0ctrl():
    response.view = 'myadd/dtablesform0ctrl.html'
    return dict(grid= mygrid('dtablesform0'))
#


@auth.requires_login()
def dtablesform1ctrl():
    response.view = 'myadd/dtablesform1ctrl.html'
    return dict(grid= mygrid('dtablesform1'))
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
def dutilities_colorform0ctrl():
    response.view = 'myadd/dutilities_colorform0ctrl.html'
    return dict(grid= mygrid('dutilities_colorform0'))
#


@auth.requires_login()
def dutilities_colorform1ctrl():
    response.view = 'myadd/dutilities_colorform1ctrl.html'
    return dict(grid= mygrid('dutilities_colorform1'))
#


@auth.requires_login()
def dforgot_passwordform0ctrl():
    response.view = 'myadd/dforgot_passwordform0ctrl.html'
    return dict(grid= mygrid('dforgot_passwordform0'))
#


@auth.requires_login()
def dcardsform0ctrl():
    response.view = 'myadd/dcardsform0ctrl.html'
    return dict(grid= mygrid('dcardsform0'))
#


@auth.requires_login()
def dcardsform1ctrl():
    response.view = 'myadd/dcardsform1ctrl.html'
    return dict(grid= mygrid('dcardsform1'))
#
