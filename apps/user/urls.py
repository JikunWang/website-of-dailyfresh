from django.conf.urls import url
# from user import views
from user.views import RegisterView, ActiveView, LoginView, UserInfoView, UserOderView, AddressView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #url(r"^register$", views.register, name="register"), # 注册
    url(r'^register$', RegisterView.as_view(), name='register'), # 注册
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'), # 用户激活
    url(r'^login$', LoginView.as_view(), name='login'), # 登录
    url(r'^logout$', LogoutView.as_view(), name='logout'), # 登出
    url(r'^order/(?P<page>\d+)$', UserOderView.as_view(), name='order'), # 用户订单
    url(r'^address$', AddressView.as_view(), name='address'), # 收件地址
    url(r'^$', UserInfoView.as_view(), name='user'), # 用户信息

    #url(r'^order$', login_required(UserOderView.as_view()), name='order'), # 用户订单
    #url(r'^address$', login_required(AddressView.as_view()), name='address'), # 收件地址
    #url(r'^$ ', login_required(UserInfoView.as_view()), name='user'), # 用户信息


]
