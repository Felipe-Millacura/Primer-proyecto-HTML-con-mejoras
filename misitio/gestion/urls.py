from django.conf.urls import url,include,include
from . import views
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', views.indexlogin),
    url(r'^perro/listar/$',views.perro_list),
    url(r'^perro/ver/$',views.perro_list_user),
    url(r'^perro/detalle/(?P<pk>[0-9]+)$',views.perro_detalle,''),
    url(r'^perro/eliminar/(?P<pk>[0-9]+)$',views.perro_eliminar,''),
    url(r'^perro/editar/(?P<pk>[0-9]+)$',views.perro_editar,''),
    url(r'^perro/new/$',views.perroo_nuevo,''),
    url(r'^perro/new/user/$',views.perroo_nuevo_user,''),
    url(r'^persona/new/$',views.user_nuevo,''),
    url(r'^administrador/$', views.administrador),
    url(r'^usuario/$', views.usuario),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)