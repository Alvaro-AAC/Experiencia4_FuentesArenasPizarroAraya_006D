from tabnanny import verbose
from django.db import models
from django.contrib.auth.hashers import make_password, identify_hasher

# Create your models here.

class Region(models.Model):
    id_region = models.IntegerField(primary_key=True, null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return f'Region: {self.descripcion}'

    class Meta:
        verbose_name_plural = 'Regiones'

class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True, null=False, blank=False)
    id_region = models.ForeignKey('Region', on_delete=models.CASCADE, null=False, blank=False)
    descripcion = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return f'Ciudad: {self.descripcion}'

    class Meta:
        verbose_name_plural = 'Ciudades'

class Usuario(models.Model):
    rut = models.IntegerField(primary_key=True, null=False, blank=False)
    dv = models.CharField(max_length=1, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False, unique=True)
    password = models.CharField(max_length=800, null=False, blank=False)
    nombre = models.CharField(max_length=40, null=False, blank=False)
    apellido = models.CharField(max_length=40, null=False, blank=False)
    edad = models.IntegerField(null=False, blank=False)
    tel = models.IntegerField(null=True, blank=True)
    ciudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE, null=False, blank=False)
    direccion_calle = models.CharField(max_length=100, null=False, blank=False)
    direccion_numero = models.IntegerField(null=False, blank=False)

    class Meta:
        constraints = [
            models.CheckConstraint(check = models.Q(rut__range=(1000000, 40000000)), name='check_usuario_rut'),
            models.CheckConstraint(check = models.Q(dv__in='0123456789K'), name='check_usuario_dv'),
            models.CheckConstraint(check = models.Q(edad__gte=0), name='check_usuario_edad'),
        ]
    
    def save(self, *args, **kwargs):
        try:
            identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return f'Usuario: {self.rut}-{self.dv} -- {self.nombre}'

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        del self

class Tipo_mascota(models.Model):
    id_tipo_mascota = models.IntegerField(primary_key=True, null=False, blank=False)
    descripcion = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return f'Tipo: {self.descripcion}'

    class Meta:
        verbose_name = 'Tipo de mascota'
        verbose_name_plural = 'Tipos de mascota'

class Mascota(models.Model):
    id_mascota = models.IntegerField(primary_key=True)
    rut_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40, null=False, blank=False)
    edad = models.IntegerField(null=False, blank=False)
    enfermedad = models.IntegerField(null=False, blank=False)
    enfermedad_desc = models.CharField(max_length=200, null=True, blank=True)
    tipo = models.ForeignKey('Tipo_mascota', on_delete=models.CASCADE)
    raza = models.CharField(max_length=60, null=True, blank=True)
    sexo = models.CharField(max_length=1, null=False, blank=False)
    esterilizado = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(check = models.Q(edad__gte=0), name='check_mascota_edad'),
            models.CheckConstraint(check = models.Q(enfermedad__in=(0, 1)), name='check_mascota_enfermedad'),
            models.CheckConstraint(check = models.Q(sexo__in='HM'), name='check_mascota_sexo'),
            models.CheckConstraint(check = models.Q(esterilizado__in=(0, 1)), name='check_mascota_esterilizado'),
        ]
    
    def __str__(self):
        return f'Mascota: {self.nombre} -- {self.tipo} -- {self.raza}s'

class Producto(models.Model):
    id_producto = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(null=False, blank=False, max_length=50)
    precio = models.PositiveIntegerField(null=False, blank=False, )
    desc = models.CharField(null=False, blank=False, max_length=130, verbose_name="Descripcion del producto")
    stock = models.PositiveIntegerField(null=False, blank=False, )
    extra_desc = models.CharField(null=True, blank=True, max_length=50)
    imagen = models.ImageField(upload_to="galeria",null=True,blank=True)
    
    class Meta:
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombre

class Boleta(models.Model):
    ESTADO_CHOICES = [
        ('procesando', 'Procesando pedido'),
        ('preparando', 'Preparando pedido'),
        ('enviando', 'Enviando pedido'),
        ('camino', 'Pedido en camino'),
        ('recibido', 'Su pedido ha llegado al destino'),
    ]

    id_boleta = models.BigAutoField(primary_key=True)
    total = models.BigIntegerField()
    estado = models.CharField(choices=ESTADO_CHOICES, default='procesando', max_length=200)

    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    id_boleta = models.ForeignKey('Boleta', on_delete=models.CASCADE)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)

class descuento(models.Model):
    codigo = models.CharField(unique=True, max_length=40)
    porcentaje = models.IntegerField()

    def __str__(self):
        return str(self.codigo)