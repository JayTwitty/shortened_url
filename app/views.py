from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from hashids import Hashids

# Create your views here.
from django.views.generic import View, ListView

from app.forms import BookmarkForm
from app.models import Bookmark


class FirstView(View):

    def get(self, request):
        bookmark_form = BookmarkForm()
        return render(request, "index.html", {"form": bookmark_form})

    def post(self, request):
        form_instance = BookmarkForm(request.POST)
        hashids = Hashids()
        if form_instance.is_valid():
            url_object = form_instance.save()
            hashid = hashids.encode(url_object.id)
            url_object.output_url=hashid
            url_object.save()
            bookmarks = Bookmark.objects.all()
        return render(request, 'index.html', {"bookmarks":bookmarks,
                                                'url': url_object})


def redirect_view(request, captured_id):
    redirect_object = Bookmark.objects.get(output_url=captured_id)
    redirect = redirect_object.input_url
    return HttpResponseRedirect(redirect)


class BookmarkListView(ListView):
    model = Bookmark

