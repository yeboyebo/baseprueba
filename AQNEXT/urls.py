from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings
# from django.utils.importlib import import_module
from YBUTILS import globalValues

# INCLUIMOS RAIZ
def raiz(request):
    return ''


urlpatterns = patterns('',)

# INCLUIMOS URL DE NUESTRAS APLICACIONES
for app in settings.YEBO_APPS:
    if app != 'models' and app != 'portal':
        urlpatterns += patterns(
            '',
            url(r'^{0}/'.format(app), include(app + '.urls_' + app, namespace=app)),
            # url(r'^{0}/'.format(app), import_module(app + '.viewset.views'), name='appviews'),
        )

# INCLUIMOS APLICACIONES POR DEFECTO EN EL RAIZ
urlpatterns += patterns(
    '',
    url(r'^admin/', admin.site.urls),
    url(r'^', include('portal.urls_portal', namespace='portal')),
    url(r'^', include('YBLOGIN.urls', namespace='YBLOGIN')),
    url(r'^', include('YBWEB.urls', namespace='YBWEB')),
)

urlpatterns += patterns(
    '',
    url(r'^$', raiz, name="root")
)

globalValues.registrarmodulos()
