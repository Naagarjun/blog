from django.test import TestCase
from django.urls import reverse, resolve
from home.views import (PostListView, PostDetailView,
                    PostCreateView, PostUpdateView,
                    PostDeleteView, UserPostListView,
                    about,
                    )
import accounts
from django.contrib.auth import views as auth_views
import unittest

class TestHomeUrls(TestCase):

    def test_default_home_url(self):
        url = reverse('blog-home')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_home_about_url(self):
        url= reverse('blog-about')
        self.assertEquals(resolve(url).func, about)

    def test_home_post_create_url(self):
        url= reverse('post-create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_home_post_update_url(self):
        url= reverse('post-update', args=[2])
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_home_post_detail_view(self):
        url= reverse('post-detail', args=[2])
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_home_post_delete_view(self):
        url= reverse('post-delete', args=[2])
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)

    def test_home_user_post_url(self):
        url= reverse('user-post', args=['some user'])
        self.assertEquals(resolve(url).func.view_class, UserPostListView) 

    # Account and blog urls testing
    def test_account_login_url(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

    def test_account_logout_url(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)

    def test_account_password_reset_url(self):
        url = reverse('password_reset')
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetView)

    def test_account_password_reset_done_url(self):
        url = reverse('password_reset_done')
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetDoneView)

    # def test_account_password_reset_confirm_url(self):
    #     url = reverse('password_reset_confirm', args=['some uidb64','some token number'])
    #     self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetConfirmView)

    # def test_account_password_reset_complete_url(self):
    #     url = reverse('password_reset_complete')
    #     self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetCompleteView)

if __name__ == '__main__':
    unittest.main()