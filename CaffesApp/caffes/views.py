from django.contrib.auth.decorators import login_required

from .models import Caffe, Comment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm

def detail_view(request, pk):
    caffe = get_object_or_404(Caffe, id=pk)
    return render(request, 'moth_site/detail.html', {
        'caffe': caffe,
    })

def add_comment_to_post(request, pk):
    caffe = get_object_or_404(Caffe, id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = caffe
            comment.author_id = request.user.id
            comment.save()
            return redirect('detail', pk=caffe.id)
    else:
        form = CommentForm()
    return render(request, 'moth_site/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('detail', pk=comment.post.pk)
