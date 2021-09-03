from django.forms import forms
from django.http.response import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render , get_list_or_404 #useralrni posti
# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #logout bulga user uchun login suraydi

#listview kurinish
from django.views.generic import ListView, CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.models import User 

#model faylimizni chaqirib olamiz
from .models import Post

from django.http import HttpResponse ,FileResponse

#PDF uchun
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

def post_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, )

    #TExt object yaratish
    textob = c.beginText()
    textob.setTextOrigin(inch,9*inch)
    textob.setFont('Helvetica',11)

    post = Post.objects.all()

    lines = [' Barcha Postlar: ']
    for posts in post:

        _extracted_from_post_pdf_17(lines, posts)
    #Looop
    for line in lines:
        textob.textLine(line)

    #tugatish
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    #return
    return FileResponse(buf,as_attachment=True,filename='post.pdf')

def _extracted_from_post_pdf_17(lines, posts):
    lines.append(' ')
    lines.append(posts.title)
    lines.append(' ')
    lines.append(posts.content)

    lines.append('=========================================')
    lines.append(' ')

#Bu oddiy kurinishida.....
# def home(request):
#     content = {
#         'posts':Post.objects.all()
#     }
#     return render(request,'blog/home.html',content)

#like dislike
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked - True

    return HttpResponseRedirect(reverse('post-detail',args=[str(pk)]))

#based class view ---> ListView
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4 #varaqda 5ta post sigishi  http://127.0.0.1:8000/?page=1


#User yaratgan postlarni kurish uchun
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):   #userni kiritgan malumotlarini olish uchun uchun kerak buladi
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

#DetailView
class PostDetailView(DetailView):
    model = Post
  
    def get_context_data(self,*args, **kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        #like count
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = total_likes
        context['liked'] = liked

        return context



#post yasash uchun view
class PostCreateView(LoginRequiredMixin, CreateView):
    try:
        model = Post
        fields = ['image','title','content']
        
        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form) 
        
    except Exception:
        pass

#Add photo old code
def addPhoto(request):
    if request.method == 'POST':
        author = request.user
        data = request.POST
        image = request.FILES.get('image')

        photos = Post.objects.create(

            image=image,
            title = data['title'],
            content = data['content'],
            author = author,

        )
        return redirect('blog-home')
    return render(request,'blog/post_form.html')

#Post update
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    try:
        model = Post
        fields = ['image','title','content']

        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)
        #check
        def test_func(self):  # sourcery skip: return-identity
            post = self.get_object()
            if self.request.user == post.author:
                return True
            return False

    except Exception:
        pass

#delete view
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    try:
        model = Post
        success_url = '/'

        def test_func(self):  # sourcery skip: return-identity
            post = self.get_object()
            if self.request.user == post.author:
                return True
            else:
                return False
    except Exception:
        pass 

#itpro swagger
def about(request):
    return render(request,'blog/about.html')