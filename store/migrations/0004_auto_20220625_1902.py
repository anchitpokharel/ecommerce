# Generated by Django 4.0.5 on 2022-06-25 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.RunSQL("""
                INSERT INTO store_collection(title)
                VALUES('collection1')
            ""","""
                DELETE FROM store_collection 
                WHERE title = 'collection1'  
        """)
    ]
