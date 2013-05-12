from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, DeleteView
from ..tutor.auth import tutorbest_required
from .views import NewGalleryView, UploadPictureView, PublishPicturesView, PublishView, PictureView, DeletePictureView, GalleryListView
from .models import Picture, Gallery

urlpatterns = patterns('',
    url('new', NewGalleryView.as_view(), name='new_gallery'),
    url('upload', UploadPictureView.as_view(), name='upload_picture'),
    url(r'^publish/(?P<pk>\d+)/$', PublishPicturesView.as_view(), name='publish_picture'),
    url('publishgallery', PublishView.as_view(), name='publish_gallery'),
    url(r'^(?P<id>\d+)/$', PictureView.as_view(), name='picture_gallery'),
    url(r'^$', GalleryListView.as_view(), name='list_galleries'),
    url(r'^delete/(?P<pk>\d+)/$',
        DeletePictureView.as_view(),
        name='delete_picture'),
)
