# -*- coding: utf-8 -*-

def _():
    app = request.application
    ctr = request.controller
    ctr_add = 'myadd'
    ctr_ima = 'myima'
    ctr_def = 'default'
    response.menu += [
        (T('Home'), False, URL('default', 'index'), []),
        (T('My Sites'), False, URL('admin', 'default', 'site')),
        (T('This App'), False, '#', [
            (T('Design'), False, URL('admin', 'default', 'design/%s' % app)),
            (T('Myadd ctrl'), False,
             URL(
                 'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr_add))),
            (T('Myima ctrl'), False,
             URL(
                 'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr_ima))),
            (T('default ctrl'), False,
             URL(
                 'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr_def))),
            (T('DB Model'), False,
             URL(
                 'admin', 'default', 'edit/%s/models/db.py' % app)),
            (T('Database'), False, URL(app, 'appadmin', 'index')),
            (T('Errors'), False, URL(
                'admin', 'default', 'errors/' + app)),
            (T('About'), False, URL(
                'admin', 'default', 'about/' + app)),
        ]),
    (T('auth'), False, URL('default', 'index'),
         [
         (T('events'), False, URL('myadd','auth_eventctrl')    ),
         (T('users'), False, URL('myadd','auth_userctrl')    ),
         (T('groups'), False, URL('myadd','auth_groupctrl')    ),
         (T('member'), False, URL('myadd','auth_membershipctrl')    ),
         ]),

      ]


add_myima= [(T('Myima'), False, URL('myima', 'index'), []), ] 
#response.menu += add_myima

add_myadd= [(T('Myadd'), False, URL('myadd', 'index'), []), ] 
response.menu += add_myadd

_()

if 'auth' in locals():
    auth.wikimenu()

