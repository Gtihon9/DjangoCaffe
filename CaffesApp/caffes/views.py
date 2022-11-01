from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Caffe, Comment
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
def comment_edit(request, caffe_pk, comment_pk):
    caffe = get_object_or_404(Caffe, id=caffe_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "POST":
        form = CommentForm(instance=comment,
                           data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = caffe
            comment.author_id = request.user.id
            comment.save()
            return redirect('detail', pk=caffe.id)
    else:
        form = CommentForm(initial={
            "author": comment.author,
            "text": comment.text,
        }
        )
    return render(request, 'moth_site/edit_comment.html', {'form': form})


@login_required
def comment_remove(request, caffe_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('detail', pk=comment.post.pk)
