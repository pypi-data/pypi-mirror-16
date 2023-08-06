# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.template.defaultfilters import linebreaksbr, urlize
from future.builtins import int
from shuyucms import template
from shuyucms.conf import settings
from shuyucms.generic.forms import ThreadedCommentForm
from shuyucms.generic.models import ThreadedComment
from shuyucms.utils.importing import import_dotted_path
from shuyucms.utils.views import paginate
from wlapps.utils.common import get_theme

register = template.Library()


@register.inclusion_tag(get_theme() + "/generic/includes/comments.html", takes_context=True)
def zdcomments_for(context, obj):
    """
    主评论模块，和页面同步加载
    """
    form = ThreadedCommentForm(context["request"], obj)
    try:
        context["posted_comment_form"]
    except KeyError:
        context["posted_comment_form"] = form
    context["unposted_comment_form"] = form
    context["comment_url"] = reverse("comment")
    context["object_for_comments"] = obj
    return context


@register.inclusion_tag(get_theme() + "/generic/includes/comment.html", takes_context=True)
def zdcomment_thread(context, obj):
    """
    评论嵌入，非池，2015-08-31
    """
    if "all_comments" not in context:
        [the_app, the_mod] = str(obj._meta).split(".")
        the_cont = ContentType.objects.get(app_label=the_app, model=the_mod)
        comments_queryset = Comment.objects.filter(content_type=the_cont.id, object_pk=obj.pk).order_by('-submit_date')
        comments_queryset = paginate(comments_queryset, context["request"].GET.get("page", 1),
                                     settings.LIST_PER_PAGE, settings.MAX_PAGING_LINKS)
        # 这个循环本来是将评论按obj分组，为了分页和排序，改为默认就一个组，非池，2015-0830
        context["all_comments"] = comments_queryset

    try:
        replied_to = int(context["request"].POST["replied_to"])
    except KeyError:
        replied_to = 0
    context.update({
        "zdcomments_for_thread": context["all_comments"],
        "no_comments": not context["all_comments"],
        "replied_to": replied_to,
        "zdajaxid": "#comment_thread",
        "commenturl": obj.get_absolute_url() + 'comment/',
    })
    return context


# 引用父评论
@register.filter(name="show_parent_comment")
def show_parent_comment(pid):
    objs = ThreadedComment.objects.filter(pk=pid)
    if len(objs):
        result = objs[0].comment
        if objs[0].user.u_profile:
            result = objs[0].user.u_profile.title + ': ' + result
        else:
            result = objs[0].user.username + ': ' + result
        return result
    else:
        return pid


@register.inclusion_tag("admin/includes/recent_comments.html", takes_context=True)
def recent_comments(context):
    """
    Dashboard widget for displaying recent comments.
    """
    latest = context["settings"].COMMENTS_NUM_LATEST
    comments = ThreadedComment.objects.all().select_related("user")
    context["comments"] = comments.order_by("-id")[:latest]
    return context


@register.filter
def zdcomment_filter(comment_text):
    """
    Passed comment text to be rendered through the function defined
    by the ``COMMENT_FILTER`` setting. If no function is defined
    (the default), Django's ``linebreaksbr`` and ``urlize`` filters
    are used.
    """
    filter_func = settings.COMMENT_FILTER
    if not filter_func:
        def filter_func(s):
            return linebreaksbr(urlize(s, autoescape=True), autoescape=True)
    elif not callable(filter_func):
        filter_func = import_dotted_path(filter_func)
    return filter_func(comment_text)
