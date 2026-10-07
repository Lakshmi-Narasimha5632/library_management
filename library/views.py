from django.contrib import messages
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from .forms import BookForm
from .models import Book


class HomeView(TemplateView):
    template_name = "library/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_count"] = Book.objects.count()
        context["genre_count"] = Book.objects.values("genre").distinct().count()
        context["author_count"] = Book.objects.values("author").distinct().count()
        context["recent_books"] = Book.objects.all()[:4]
        context["top_genres"] = Book.objects.values("genre").annotate(total=Count("id")).order_by("-total", "genre")[:3]
        return context


class BookListView(ListView):
    model = Book
    template_name = "library/book_list.html"
    context_object_name = "books"
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q", "").strip()
        genre = self.request.GET.get("genre", "").strip()
        if query:
            queryset = queryset.filter(title__icontains=query) | queryset.filter(author__icontains=query)
        if genre:
            queryset = queryset.filter(genre=genre)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("q", "").strip()
        context["selected_genre"] = self.request.GET.get("genre", "").strip()
        context["genres"] = Book.objects.values_list("genre", flat=True).distinct().order_by("genre")
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "library/book_detail.html"
    context_object_name = "book"


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "library/book_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Book added to your library.")
        return super().form_valid(form)


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "library/book_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Book details updated.")
        return super().form_valid(form)


class BookDeleteView(DeleteView):
    model = Book
    template_name = "library/book_confirm_delete.html"
    success_url = reverse_lazy("book-list")

    def form_valid(self, form):
        messages.success(self.request, "Book removed from your library.")
        return super().form_valid(form)
