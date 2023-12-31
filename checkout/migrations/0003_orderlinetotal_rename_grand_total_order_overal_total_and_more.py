# Generated by Django 4.2.7 on 2023-12-03 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('checkout', '0002_orderlineitem_rename_overal_total_order_grand_total_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLineTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('itemline_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='grand_total',
            new_name='overal_total',
        ),
        migrations.DeleteModel(
            name='OrderLineItem',
        ),
        migrations.AddField(
            model_name='orderlinetotal',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemlines', to='checkout.order'),
        ),
        migrations.AddField(
            model_name='orderlinetotal',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
