from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import include, re_path
from hello.views import HomePageView, SearchResultsView

admin.autodiscover()
from rest_framework import routers
import hello.views

router = routers.DefaultRouter()
router.register(r'users', hello.views.UserViewSet)
router.register(r'groups', hello.views.GroupViewSet)
router.register(r'petposts', hello.views.PetPostViewSet)

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
    path("account", hello.views.account, name="account"),
    path("paperclips", hello.views.paperclips, name="paperclips"),
    path("paperclips/<int:paperclip_id>/", hello.views.paperclip_detail, name="paperclip_detail"),
    re_path(r'^add_paperclip$', hello.views.add_paperclip, name='add_paperclip'),
    # 其他 url 配置
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('blog/index', hello.views.display_blogs, name='blog/index'),
    # 文章详情
    path('blog/detail/<int:id>/', hello.views.blog_detail, name='blog/detail'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
