from django.db.models import Count, Q

from app.models import Category, Tag


def common(request):
    context = {
        'categories': Category.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
        'tag': Tag.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
    }
    return context
