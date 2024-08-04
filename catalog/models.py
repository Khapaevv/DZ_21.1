from django.db import models, connection

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        # ordering = ['', '', '']

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        **NULLABLE,
    )
    image = models.ImageField(
        upload_to="catalog/images",
        verbose_name="Изображение",
        help_text="Загрузите фото продукта",
        **NULLABLE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Введите цену за покупку продукта"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        # ordering = ['', '', '']

    def __str__(self):
        return self.name
