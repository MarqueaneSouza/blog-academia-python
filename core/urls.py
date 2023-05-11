from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('exemplos/', include('exemplos.urls')),
    path('login/', include('autenticacao.urls')),
    path('contato/', include('contato.urls')),
    path('cursos/', include('cursos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('blog.urls')),
#     path('exemplos/', include('exemplos.urls')),
#     path('contas/', include('autenticacao.urls')),
#     path('contato/', include('contato.urls')),
#     path('cursos/', include('cursos.urls')),
#     path('ckeditor/', include('ckeditor_uploader.urls')),
#     path('criar_conta/', include('contas.urls')),
#     path('accounts/', include('allauth.urls')),
#     path('quiz/', include('quiz.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)