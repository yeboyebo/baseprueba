from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings
import importlib

from YBUTILS import globalValues
from YBUTILS.viewREST import routers
from YBWEB.ctxJSON import DICTJSON


def raiz(request):
    return ''


urlpatterns = patterns('',)
apps = globalValues.registraRest()
sUrls = open("config/urls.json").read()
oUrls = DICTJSON.fromJSON(sUrls)

for app in settings.YEBO_APPS:
    if app == 'models':
        routerDef = routers.RESTDefaultRouterModel()

        for mod in apps[app]:
            routerDef.registerDynamic(mod)

        urlpatterns += patterns(
            '',
            url(r'^{0}/'.format(app), include(routerDef.urls)),
        )

    else:
        view = importlib.import_module(app + ".viewset.views_" + app)
        objView = view.FormInternalObj()
        objView._class_init()
        views = objView.iface
        objView.iface.ctx = views
        objView.iface.iface = views

        if app != "portal":
            routerLayOut = routers.LayOutDefaultRouter(aplicacion=app)

            for mod in apps['models']:
                routerLayOut.registerDynamicModel(mod)

            urlpatterns += patterns(
                '',
                url(r'^{0}/'.format(app), include(routerLayOut.urls)),
            )

        patt = r'^' if app == "portal" else r'^{0}/'.format(app)

        for extUrl in oUrls[app]:
            urlpatterns += patterns(
                app,
                url(r'{0}{1}'.format(patt, oUrls[app][extUrl]['url']), getattr(views, oUrls[app][extUrl]['func']), name=extUrl)
            )

urlpatterns += patterns(
    '',
    url(r'^admin/', admin.site.urls),
    url(r'^', include('YBLOGIN.urls', namespace='YBLOGIN')),
)

urlpatterns += patterns(
    '',
    url(r'^$', raiz, name="root")
)
