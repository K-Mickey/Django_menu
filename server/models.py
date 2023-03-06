from django.db import models


class MenuCategory(models.Model):

    name = models.CharField('Name', max_length=255, blank=True, null=False)
    verbose_name = models.CharField('Verbose_name', max_length=255, blank=True, null=False)

    def __str__(self):
        return self.verbose_name

    class Meta:
        verbose_name = 'Menu_category'
        verbose_name_plural = 'Menu_categories'


class Menu(models.Model):

    name = models.CharField('Name', max_length=255, blank=True, null=False)
    category = models.ForeignKey(
        MenuCategory, verbose_name='Category', on_delete=models.CASCADE, blank=False, null=False
    )
    path = models.CharField('Link', max_length=1000, blank=True, null=False)
    parent = models.ForeignKey(
        'self', verbose_name='Parent_element', on_delete=models.SET_DEFAULT, null=True, blank=True, default=0
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'
