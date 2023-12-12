---
layout: post
title:  'Ordering, Transactions and Exactly-Once Semantics in Data Integrations'
description: 'There are three important aspects of robust data integrations when using queues: global ordering of messages, multi-message transactionality, and exactly-once semantics.'
date:   2023-12-12 11:05:00 +0300
image:  '/images/balls.png'
seotags:   [data, data-integration, data-integrity, communication-patterns]
tags:   [data integration]
---
This post is ninth part in a series about building and adopting a modern
streaming data integration platform. In this post I will discuss three important aspects of robust data integrations
when using the logging metaphor: global ordering of messages, multi-message transactionality, and exactly-once semantics. Focus is
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

Apache Kafka is commonly used platform for building streaming data integrations. On the
surface Kafka seems very suitable for this purpose. Confluent, the company
developing Kafka, was founded on the same vision I am discussing in this
series of blog posts.

Kafka has high performance and scalability due to parallelism. In Kafka, each
topic is a single queue. Parallelism is supported by partitioning the topics.
Each message has a key, which is used in the partitioning. The downside
of this approach is that Kafka cannot guarantee global ordering of events when
using multiple topics, or multiple partitions on topics. If you do not have
global ordering of events, then you do not have a change log in the strict
sense. In other words, you are not fully invested in the logging metaphor.

Kafka has nominal support for transactions. In practice this means that 
Kafka allows producer to send a batch of messages to multiple partitions so
that either all messages in the batch are eventually visible to any consumer, or none are 
ever visible to any consumer.

However, sink systems do not know when transactions start and end,
so they can read "transactionally" only individual messages. Without support for
multi-message transactions, it becomes difficult to maintain referential integrity
between messages, if individual messages contain entities.

Kafka has also optional support for exactly-once semantics. In practice this means that
Kafka can guarantee that a successful consume-transform-produce iteration is
executed only once. However, as the transform component may potentially call external 
systems or cause other side effects, the overall result may still be non-deterministic.

For the data integration platform development project I am describing in this series of
blog posts, we ended up choosing Apache Kafka as the central architectural component. 
We did not understand all the consequences of the technology choice. In a later 
post I will discuss the lessons I learned from this.

There are severe consequences from lack of referential integrity. You will
likely encounter complex data issues that are difficult to solve. At the minimum, 
applications using the data need to take into account eventual consistency, pushing 
the complexity to the application developers. Much of this complexity could be 
be handled by the data integration platform.

The benefit of this approach is high and scalable throughput. I recommend that you seriously
consider your requirements regarding performance and data integrity. The current 
trend appears to favor performance and scalability. In typical enterprise environments 
this may be a bad trade-off, even if there are no strict regulatory requirements for data integrity.

What are the alternatives? There seems to be two possibilities. The first alternative is to use IBM MQ. 
IBM MQ seems popular in industries which have high data integrity requirements. The second alternative is 
to build your own solution based on database features. This sounds like a huge effort, but ultimately 
the implementation is quite straight-forward, and can support features that are useful when you are
using the logging metaphor.

***

If you need consulting related to system architectures in general, or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.
