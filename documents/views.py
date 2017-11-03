from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from .models import Document
from .forms import DocumentForm


class DocumentDetailView(DetailView):

    model = Document
    template_name = 'documents/document_detail.html'


class DocumentListView(ListView):

    model = Document
    template_name = 'documents/document_list.html'


class DocumentCreate(CreateView):

    model = Document
    template_name = 'documents/document_create.html'
    form_class = DocumentForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DocumentCreate, self).dispatch(*args, **kwargs)


class DocumentUpdate(UpdateView):

    model = Document
    form_class = DocumentForm
    template_name = 'documents/document_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DocumentUpdate, self).dispatch(*args, **kwargs)


class DocumentDelete(DeleteView):
    model = Document
    template_name = 'vocabs/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_documents')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DocumentDelete, self).dispatch(*args, **kwargs)
