# Generated by Django 3.2.16 on 2022-12-09 07:32

from django.conf import settings
from django.db import migrations, models
import dog_walks.core.validators
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Night',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('district', models.CharField(
                    choices=[('BLAGOEVGRAD', 'Благоевград'), ('BURGAS', 'Бургас'), ('VARNA', 'Варна'),
                             ('VELIKOTARNOVO', 'Велико Търново'), ('VIDIN', 'Видин'), ('VRATSA', 'Враца'),
                             ('GABROVO', 'Габрово'), ('DOBRICH', 'Добрич'), ('KYRDJALI', 'Кърджали'),
                             ('KYUSTENDIL', 'Кюстендил'), ('LOVECH', 'Ловеч'), ('MONTANA', 'Монтана'),
                             ('PAZARDZHIK', 'Пазарджик'), ('PERNIK', 'Перник'), ('PLEVEN', 'Плевен'),
                             ('PLOVDIV', 'Пловдив'), ('RAZGRAD', 'Разград'), ('RUSE', 'Русе'), ('SILISTRA', 'Силистра'),
                             ('SLIVEN', 'Сливен'), ('SMOLYAN', 'Смолян'), ('SOFIADISTRICT', 'Софийска област'),
                             ('SOFIA', 'София'), ('STARAZAGORA', 'Стара Загора'), ('TARGOVISHTE', 'Търговище'),
                             ('HASKOVO', 'Хасково'), ('SHUMEN', 'Шумен'), ('YAMBOL', 'Ямбол')], max_length=13)),
                ('city', models.CharField(max_length=50,
                                          validators=[dog_walks.core.validators.only_cyrillic_letters_validator])),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('description', models.TextField()),
                ('website', models.URLField(blank=True, null=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
                ('type', models.CharField(
                    choices=[('HOTEL', 'Хотел'), ('GUESTHOUSE', 'Вила/Къща за гости'), ('HUT', 'Хижа'),
                             ('BUNGALOW', 'Бунгало'), ('OTHER', 'Други')], max_length=10)),
                ('price', models.CharField(
                    choices=[('VERY_CHEAP', 'Много евтино'), ('CHEAP', 'Евтино'), ('NORMALLY', 'Нормално'),
                             ('EXPENSIVE', 'Скъпо'), ('VERY_EXPENSIVE', 'Много скъпо')], max_length=14)),
                ('beds_count', models.PositiveIntegerField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('image', models.ImageField(upload_to='nights-places')),
                ('dog_fee', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=models.SET('Несъществуващ'), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'unique_together': {('longitude', 'latitude')},
            },
        ),
    ]
