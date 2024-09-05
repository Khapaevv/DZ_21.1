from django.db import models, connection

from users.models import User

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
            cursor.execute(
                f"TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE"
            )

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
        upload_to="products/image",
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
    owner = models.ForeignKey(User, verbose_name="Пользователь", **NULLABLE, on_delete=models.SET_NULL)
    is_published = models.BooleanField(verbose_name="Опубликовано", help_text="ВОпубликовано?", default=False)


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
            ('can_change_description', "Can change description of product"),
            ('can_change_category', "Can change category of product"),
            ('can_cancel__is_published', "Can cancel is_published")
        ]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name="Наименование продукта",
        related_name="version",
        on_delete=models.SET_NULL,
        **NULLABLE,
    )
    version_number = models.PositiveIntegerField(
        default=0,
        verbose_name="Номер версии продукта",
        help_text="Введите номер версии продукта",
        **NULLABLE,
    )
    version_name = models.CharField(
        max_length=50,
        verbose_name="Наименование версии продукта",
        help_text="Введите наименование версии продукта",
        **NULLABLE,
    )
    version_sign = models.BooleanField(
        verbose_name="признак текущей версии", help_text="Версия активна?", default=True
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["product", "version_number", "version_name"]

    def __str__(self):
        return self.version_name
