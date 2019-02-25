# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-24 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=100, verbose_name='商品名称')),
                ('img_url', models.CharField(max_length=255, verbose_name='商品默认图片')),
                ('zhaiyao', models.CharField(max_length=255, verbose_name='摘要')),
                ('content', models.TextField(default='', verbose_name='商品详情')),
                ('status', models.IntegerField(default=0, verbose_name='是否下线')),
                ('is_red', models.IntegerField(default=0, verbose_name='是否推荐')),
                ('is_slide', models.IntegerField(default=0, verbose_name='是否轮播商品')),
                ('sub_title', models.CharField(max_length=255, verbose_name='子标题')),
                ('goods_no', models.CharField(max_length=100, verbose_name='商品编号')),
                ('stock', models.IntegerField(verbose_name='商品库存')),
                ('sales', models.IntegerField(verbose_name='销量')),
                ('market_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='市场价')),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='销售价')),
            ],
            options={
                'verbose_name_plural': '商品',
                'db_table': 't_goods',
                'verbose_name': '商品',
            },
        ),
        migrations.CreateModel(
            name='GoodsAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('thumb_path', models.CharField(max_length=255, verbose_name='缩略图url')),
                ('original_path', models.CharField(max_length=255, verbose_name='原图url')),
                ('remark', models.TextField(null=True, verbose_name='备注信息')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
            ],
            options={
                'verbose_name_plural': '商品图片',
                'db_table': 't_goods_album',
                'verbose_name': '商品图片',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=100, verbose_name='类别名称')),
                ('sort_id', models.IntegerField(verbose_name='排序权重')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='父类别')),
            ],
            options={
                'verbose_name_plural': '商品分类',
                'db_table': 't_goods_category',
                'verbose_name': '商品分类',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='类别'),
        ),
    ]
