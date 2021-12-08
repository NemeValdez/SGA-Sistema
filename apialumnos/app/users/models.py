from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UsuarioManager(BaseUserManager):
    '''Control de la gestión de usuarios personalizado'''

    def _create_user(self, dni_usuario, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            dni_usuario=dni_usuario,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, dni_usuario, password=None, **extra_fields):
        return self._create_user(dni_usuario, password, False, False, **extra_fields)

    def create_superuser(self, dni_usuario, password=None, **extra_fields):
        return self._create_user(dni_usuario, password, True, True, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    '''Modelo de la Base de Dato para Gestión de Usuarios personalizados'''
    dni_usuario = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'dni_usuario'

    def __str__(self):
        return self.dni_usuario

    def natural_key(self):
        return (self.dni_usuario)
