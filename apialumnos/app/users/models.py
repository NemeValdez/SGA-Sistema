from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UsuarioManager(BaseUserManager):
    '''Control de la gestión de usuarios personalizado'''

    def create_user(self, dni_usuario, password=None):
        '''Creación de usuario básico'''
        if not dni_usuario:
            raise ValueError('El usuario debe tener un DNI')
        usuario = self.model(dni_usuario=dni_usuario)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, dni_usuario, password=None):
        '''Creación de usuario completo'''
        usuario = self.create_user(dni_usuario, password)
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save(using=self._db)
        return usuario


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
