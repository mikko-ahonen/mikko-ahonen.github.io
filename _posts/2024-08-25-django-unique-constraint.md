---
layout: post
title:  Adding a unique constraint to a Django model
description: 'Adding a unique constraint to a Django model with lots of data when using Postgres'
date:   2024-08-15 03:20:00 +0300
image:  '/images/clones.jpeg'
seotags:   [django,postgres]
tags:   [django,postgres]
---
Recently, a moderately high volume Django site started to fail on MultipleObjectsReturned. The offending model was 
an advertisement impression counter.

The counters were created dynamically using get_or_create(). It was failing, because the method may create
duplicates unless the model has unique constraints for the fields used in the filtering, which I did not have.

Fortunately, I did not have too many rows in the table, so I could just fix the data and then
add the constraint to the model.

While investigating this, I figured out how to do it if there are millions of rows and I need to run
the update online. I will leave it here for future reference. Use it only for ideas, I have not tested it.

### 1. Temporary fix

My production was failing, so I needed to have a quick temporary fix. Replacing get_or_create() with 
filter() and first() was enough to make the system work while I was fixing it.

### 2. Fix the data

I merged the counters by adding their values together. The code below is not transactional, and may lose some counts. 
If that is a problem, identify the offending counters and update each one inside a transaction.

```python
from django.db import migrations

def remove_duplicate_entries(apps, schema_editor):
    ImpressionCounter = apps.get_model('ads', 'ImpressionCounter')
    seen = dict()
    for counter in ImpressionCounter.objects.all():
        identifier = (counter.ad_id, counter.impression_date)
        if identifier in seen:
            seen[identifier].counter += counter.counter
            seen[identifier].save()
            counter.delete()
        else:
            seen[identifier] = counter

class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0011_alter_click_index_together'),
    ]

    operations = [
        migrations.RunPython(remove_duplicate_entries, migrations.RunPython.noop),
    ]
```

### 3. Add an index to the model

```python
class ImpressionCounter(models.Model):
    ...    

    class Meta:
        ...
        indexes = [
            models.Index(fields=['ad', 'impression_date'], name="index_impression_counter"),
        ]
```

### 4. Create the migration for the index

```bash
% python manage.py makemigrations
```

This will create a migration for the index. If you have lots of data, this would lock the table for a long
time. Luckily, since 3.0, Django has had a new AddIndexConcurrently feature which can be used.

To use it, open the generated migration file and change the AddIndex to AddIndexConcurrently and
RemoveIndex to RemoveIndexConcurrently.

Give a name to the index, so you can reference it when creating the constraint.

### 5. Add the constraint to the model

Django has two ways to make field combinations unique: the older unique_together and the newer constraints. The former
may be deprecated in the future, so it makes sense to use the latter.

```python
class ImpressionCounter(models.Model):
    ...    

    class Meta:
        ...
        constraints = [
            models.UniqueConstraint(fields=['ad', 'impression_date'], name='unique_ad_impression_date')
        ]
```

### 6. Create the migration for the constraint

The following command will create the migration for the constraint. It will not use the existing index by 
default.

```bash
% python manage.py makemigrations
```

Edit the migration to use the existing constraint.

Start off by printing the SQL commands for the migration and reverse migration:

```bash
% python manage.py sqlmigrate ads 0014
% python manage.py sqlmigrate ads 0014 --reverse
```
By using SeparateDatabaseAndState and the SQL commands from above, you can write the database modification by 
hand while still keeping Django informed about the migration.

```python
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0013_create_index'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations = [
              migrations.RunSQL(
                sql=
                """
                    ALTER TABLE "ads_impressioncounter" ADD CONSTRAINT "unique_ad_impression_date" UNIQUE ("ad_id", "impression_date") USING INDEX (index_impression_counter);
                """,
                reverse_sql="""
                    ALTER TABLE "ads_impressioncounter" DROP CONSTRAINT "unique_ad_impression_date";
                """),
            ], state_operations= [
                migrations.AddConstraint(
                    model_name='impressioncounter',
                    constraint=models.UniqueConstraint(fields=('ad', 'impression_date'), name='unique_ad_impression_date'),
                ),
            ]
    ]
```

### Sources

<a href="https://medium.com/@timmerop/how-to-add-a-uniqueconstraint-concurrently-in-django-2043c4752ee6">How to add unique constraint concurrently in Django</a>

***

If you need consulting related to system architectures in general, or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.
