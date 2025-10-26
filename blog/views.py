from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView

from blog.models import BlogPost


class PostCreateView(CreateView):
    model = BlogPost
    fields = ["title", "content", "publication_sign", "preview"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post_list")


class PostUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "content", "publication_sign", "preview"]
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"pk": self.object.pk})


class PostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")


class PostListView(ListView):
    model = BlogPost
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        filtered_queryset = queryset.filter(publication_sign=True)
        return filtered_queryset


class PostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.number_of_views += 1
        obj.save()
        return obj
