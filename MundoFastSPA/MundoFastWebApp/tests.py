from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):

    def test_create_user(self):
        Usuario = get_user_model()
        user = Usuario.objects.create_user(emailUsuario='normal@Usuario.com', password='foo')
        self.assertEqual(Usuario.emailUsuario, 'normal@Usuario.com')
        self.assertTrue(Usuario.is_active)
        self.assertFalse(Usuario.is_staff)
        self.assertFalse(Usuario.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(Usuario.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            Usuario.objects.create_user()
        with self.assertRaises(TypeError):
            Usuario.objects.create_user(emailUsuarioUsuario='')
        with self.assertRaises(ValueError):
            Usuario.objects.create_user(emailUsuario='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = Usuario.objects.create_superuser('super@Usuario.com', 'foo')
        self.assertEqual(admin_Usuario.emailUsuario, 'super@Usuario.com')
        self.assertTrue(admin_Usuario.is_active)
        self.assertTrue(admin_Usuario.is_staff)
        self.assertTrue(admin_Usuario.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_Usuario.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            Usuario.objects.create_superuser(
                emailUsuario='super@Usuario.com', password='foo', is_superuser=False)