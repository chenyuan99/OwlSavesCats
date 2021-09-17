from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import include, re_path
from django.conf.urls import url
from hello.views import HomePageView, SearchResultsView
admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

app_name = 'main'  # here for namespacing of urls.
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("register/", hello.views.register, name="register"),
    path("logout", hello.views.logout_request, name="logout"),
    path("login", hello.views.login_request, name="login"),
    re_path(r'^favicon\.ico$', favicon_view),
    path("about", hello.views.about, name="about"),
    path("faq", hello.views.faq, name="faq"),
    path("privacy-policy", hello.views.privacy, name="privacy-policy"),
    path("check-in", hello.views.paperclip, name="check-in"),
    path("add-guest", hello.views.add_guest, name="add-guest"),
    path("account", hello.views.account, name="account"),
    path("paperclips",hello.views.paperclips, name = "paperclips"),
    path("paperclips/<int:paperclip_id>/",hello.views.paperclip_detail, name = "paperclip_detail"),
    url(r'^add_paperclip$', hello.views.add_paperclip, name='add_paperclip'),
    # 其他 url 配置
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('blog/index', hello.views.display_blogs, name='blog/index'),
    url(r'^page_demo/', hello.views.page_demo),
]
