from cgi import test
from django.contrib.auth import views
from django.test import TestCase
from django.urls import resolve, reverse
from .views import user_login, user_logout
# Create your tests here.


class LoginViewUrlResolveTest(TestCase):
    def test_url_resolves_to_view(self):
        view_name = reverse('diaryapp:login')
        view_class = resolve(view_name).func.view_class

        self.assertIs(view_class, user_login)


class LoginViewInheritanceTest(TestCase):
    def test_view_inherits_from_auth_LoginView(self):
        auth = views.LoginView
        view = user_login

        assert issubclass(view, auth), '{} {} {}'.format(
            view, 'is not a subclass of ', auth
        )


class LoginViewAttributesTests(TestCase):
    def setUp(self):
        view_name = reverse('diaryapp:login')
        self.view_class = resolve(view_name).func.view_class

    def test_template_name_attribute_is_assigned_to_login_string(self):
        expected_string = 'diaryapp/login.html'
        current_string = self.view_class.template_name

        self.assertEqual(expected_string, current_string)

    def test_redirect_authenticated_user_attribute_is_assigned_to_True(self):
        self.assertTrue(self.view_class.redirect_authenticated_user)


class LogoutViewUrlResolveTest(TestCase):
    def test_url_resolves_to_view(self):
        view_name = reverse('diaryapp:logout')
        view_class = resolve(view_name).func.view_class

        self.assertIs(view_class, user_logout)


class LogoutViewInheritanceTest(TestCase):
    def test_view_inherits_from_auth_LogoutView(self):
        auth = views.LogoutView
        view = user_logout

        assert issubclass(view, auth), '{} {} {}'.format(
            view, 'is not a subclass of ', auth
        )


class LogoutViewAttributesTests(TestCase):
    def setUp(self):
        view_name = reverse('diaryapp:logout')
        self.view_class = resolve(view_name).func.view_class

    def test_template_name_attribute_is_assigned_to_login_string(self):
        expected_string = 'diaryapp/logout.html'
        current_string = self.view_class.template_name

        self.assertEqual(expected_string, current_string)
