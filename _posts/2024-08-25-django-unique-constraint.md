---
layout: post
title:  Adding a unique constraint to a Django model
description: 'Adding a unique constraint to a Django model with lots of data when using Postgres'
date:   2024-08-25 03:20:00 +0300
image:  '/images/clones.jpeg'
seotags:   [django,postgres]
tags:   [django,postgres]
---
Recently, a moderately high volume Django site started to fail on MultipleObjectsReturned. The offending model was 
an advertisement impression counter. For each ad and day combination there was a row in the database.

The counters are created dynamically using get_or_create(). This method does not guarantee uniqueness, unless the 
model has unique constraint for the fields used in filtering. Fortunately, the related table did not have too 
many rows.

While investigating this, I learned what to do if the table has millions of rows. I have not tested 
the code below, because I did not need it. It is here for reference only.

***

If you need consulting related to system architectures in general, or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.
