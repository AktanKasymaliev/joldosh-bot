from django.db import models

class Problem(models.Model):
    description = models.TextField(verbose_name="Описание")
    latitude = models.DecimalField(verbose_name="Широта",max_digits=22, decimal_places=16)
    longitude = models.DecimalField(verbose_name="Долгота",max_digits=22, decimal_places=16)
    comment = models.TextField(verbose_name="Комментарий", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="Время добавления", auto_now_add=True)

    def __str__(self) -> str:
        return f"Проблема - {self.id}"
    
    
    class Meta:
        verbose_name = 'Проблема'
        verbose_name_plural = 'Проблемы'
    

class ProblemImage(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name="Фотография")

    def __str__(self):
        if self.image:
            return self.image.url
        else:
            return ''