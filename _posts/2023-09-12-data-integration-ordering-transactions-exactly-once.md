---
layout: post
title:  Ordering, Transactions and Exactly Once Semantics in Data Integrations
description: There are three important aspects of robust data integrations when using queues: global ordering of messages, multi-message transactionality, and exactly-once semantics.
date:   2023-09-12 11:05:00 +0300
image:  '/images/balls.png'
seotags:   [data, data-integration, data-integrity, communication-patterns]
tags:   [data integration]
---
This post is ninth part in a series about building and adopting a modern
streaming data integration platform. In this post I will discuss three important aspects of robust data integrations
when using queues: global ordering of messages, multi-message transactionality, and exactly-once semantics. Focus is
on Apache Kafka, which is a common platform for implementing streaming data integrations.
 
Previous parts:
* [Part 1: Why to Build a Data Integration Platform?](https://jauzo.com/2023/08/11/why-dip/)
* [Part 2: About Logging](https://jauzo.com/2023/08/25/logging/)
* [Part 3: Data Integration Methods](https://jauzo.com/2023/08/28/data-integration-methods/)
* [Part 4: Role of Data Modeling in Data Integrations](https://jauzo.com/2023/08/29/data-modeling/)
* [Part 5: Data Integration Architectures](https://jauzo.com/2023/09/08/data-integration-architectures/)
* [Part 6: Lightweight Reference Data](https://jauzo.com/2023/09/09/lightweight-reference-data/)
* [Part 7: Lost Integrity On Data Integrity](https://jauzo.com/2023/09/10/data-integrity/)
* [Part 8: Communication Patterns in Data Integrations](https://jauzo.com/2023/09/11/data-integration-communication-patterns/)

***

Apache Kafka is commonly used for building streaming data integrations. On the
surface Kafka seems very suitable for this purpose. Confluent, the company
developing Kafka, was even founded on the same vision I am discussing in this
series of blog posts.

Kafka has high performance and scalability due to parallelism. In Kafka, a
topic is a single queue. Parallelism is supported by partitioning the topics.
Each message has a key, which is used for choosing the partition. The downside
of this approach is that Kafka cannot guarantee global ordering of events if
you use multiple topics, or multiple partitions on topics.  If you do not have
global ordering of events, then you do not have a change log in the strict
sense.

Kafka has nominal support for transactions. They allow a producer to send a
batch of messages to multiple partitions such that either all messages in the
batch are eventually visible to any consumer or none are ever visible to
consumers. However, sink systems do not know when transactions start and end,
so they can read transactionally only individualmessages. Without support for
multi-message transactions, it becomes difficult to keep referential integrity
between messages, if individual messages contain entities.

Kafka has also optional support for exactly-once semantics. In practice this means that
Kafka can guarantee that a successful consume-transform-produce iteration is
executed only once. However, as the transform component may call external systems
and cause other side effects, the overall result may still be non-deterministic.

For the data integration platform development project I am describing here, we 
ended up choosing Apache Kafka as the central component. We did not understand 
all the consequences when the technology was chosen. In a later post I will discuss 
the lessons I have learned from this.

There seems to be two alternatives to Apache Kafka.

The first alternative is IBM MQ, which seems popular in industries which have 
high data integrity requirements.

The second alternative is to built your own solution based on database features.

***

If you need consulting related to system architectures in general, or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.
