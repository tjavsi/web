# coding: utf-8
from django import forms
from django.shortcuts import get_object_or_404
from django.forms.extras import SelectDateWidget
from django.views.generic import UpdateView, TemplateView, CreateView, DeleteView
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Picture, Gallery
from ..tutor.auth import tutorbest_required



class UploadPictureForm(forms.ModelForm):
    class Meta:
        model = Picture


class NewGalleryView(CreateView):
    model = Gallery
    template_name = "creategallery.html"

    def get_success_url(self):
        return reverse("list_galleries")

    @method_decorator(tutorbest_required)
    def dispatch(self, *args, **kwargs):
        return super(NewGalleryView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        d = super(NewGalleryView, self).get_context_data(**kwargs)
        d['create'] = True
        return d


class UploadPictureView(CreateView):
    model = Picture
    template_name = "pictureuploader.html"
    form_class = UploadPictureForm

    def get_success_url(self):
        return reverse("list_galleries")

    @method_decorator(tutorbest_required)
    def dispatch(self, *args, **kwargs):
        return super(UploadPictureView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        d = super(UploadPictureView, self).get_context_data(**kwargs)
        d['create'] = True
        return d

class PublishPicturesView(UpdateView):
    model = Picture
    template_name = "publishpictures.html"
    form_class = UploadPictureForm

    def get_success_url(self):
        return reverse("list_"+self.object.type)
    @method_decorator(tutorbest_required)
    def dispatch(self, *args, **kwargs):
        return super(UploadPictureView,self).dispatch(*args,**kwargs)
    def get_context_data(self, **kwargs):
        d = super(UploadPictureView, self).get_context_data(**kwargs)
        d['create'] = False
        return d

class DeletePictureView(DeleteView):
    model = Picture

    def get_success_url(self):
        return reverse("list_"+self.object.type)

    @method_decorator(tutorbest_required)
    def dispatch(self, *args, **kwargs):
        return super(DeletePictureView, self).dispatch(*args, **kwargs)

class PublishView(TemplateView):
    def get_queryset(self):
        return Picture.objects.filter(is_published__exact = True)
    def get(self, request):
        pictures = self.get_queryset()
        params = {
                 "pictures":pictures,
        }        
        return self.render_to_response(params)

    @method_decorator(tutorbest_required)
    def dispatch(self, *args, **kwargs):
        return super(PublishView, self).dispatch(*args, **kwargs)

    def get_template_names(self):
        return ('gallery.html',)

class PictureView(TemplateView):
    def get_queryset(self):
        return Picture.objects.filter(is_published__exact = True)

    def get(self, request, id=None):
        gallery = get_object_or_404(Gallery.objects.filter(pk=id))
        
        pictures = Picture.objects.filter(gallery__exact=gallery)
        params = {
                 "gallery":gallery,
                 "pictures":pictures,
        }        
        return self.render_to_response(params)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PictureView, self).dispatch(*args, **kwargs)

    def get_template_names(self):
        return ('galleryview.html',)

class GalleryListView(TemplateView):
    def get_queryset(self):
        return Gallery.objects.all()

    def get(self, request):
        gallery_list = self.get_queryset()
        params = {
                 "gallery_list":gallery_list
        }        
        return self.render_to_response(params)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GalleryListView, self).dispatch(*args, **kwargs)

    def get_template_names(self):
        return ("galleries.html",)
