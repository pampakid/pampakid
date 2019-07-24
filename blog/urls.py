from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import (
    index,
    manifesto,
    login,
    projects,
    contact,
    success,
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('manifesto/', manifesto),
    path('projects/', projects),
    path('contact/', contact, name='contact'),
    path('success/', success),
    path('blog/', post_list, name='post-list'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/', post_detail, name='post-detail'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete', post_delete, name='post-delete'),

    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', login, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
