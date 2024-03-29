from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/<int:post_id>/post_detail', views.post_detail, name='post_detail'),
    path('blog/', views.blog, name='blog'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #possibilita que a imagem seja carregada no ambiente de desenvolvimento.
