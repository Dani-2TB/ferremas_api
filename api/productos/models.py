from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    def __str__(self):
        return f"Categoría: {self.nombre}"
    
    class Meta:
        ordering = ['nombre']

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) :
        return f'{self.categoria.nombre} -> {self.nombre}'

    class Meta:
        ordering = ['nombre']

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(
        verbose_name="Descripción del producto",
        max_length=300
        )
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    cantidad = models.IntegerField()
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
        )
    subcategoria = models.ForeignKey(
        Subcategoria, 
        on_delete=models.SET_NULL,
        null=True, 
        blank=True
        )

    def __str__(self):
        return f"Producto: {self.nombre}"

    class Meta:
        ordering = ['categoria', 'subcategoria', 'nombre']