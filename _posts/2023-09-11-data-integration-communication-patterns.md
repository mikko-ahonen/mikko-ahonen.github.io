---
layout: post
title:  Communication Patterns In Data Integrations
description: Data integrity is especially important in data integrations, whether you use batch or stream processing to deliver data. There are multiple communication patterns available, and only some of them are useful for real-time integrations. All of them have some caveats regarding data integrity.
date:   2023-09-11 11:05:00 +0300
image:  '/images/queue.png'
seotags:   [data, data-integration, data-integrity, communication-patterns]
tags:   [data integration]
---

This post is eigth part in a series about building and adopting a modern streaming data integration platform. In this post
I discuss the various communication patterns in real-time data integrations.

<!-- dip links start -->
* [Part 1: Why to Build a Data Integration Platform?](https://jauzo.com/2023/08/11/why-dip/)
* [Part 2: About Logging](https://jauzo.com/2023/08/25/logging/)
* [Part 3: Data Integration Methods](https://jauzo.com/2023/08/28/data-integration-methods/)
* [Part 4: Role of Data Modeling in Data Integrations](https://jauzo.com/2023/08/29/data-modeling/)
* [Part 5: Data Integration Architectures](https://jauzo.com/2023/09/08/data-integration-architectures/)
* [Part 6: Lightweight Reference Data](https://jauzo.com/2023/09/09/lightweight-reference-data/)
* [Part 7: Lost Integrity On Data Integrity](https://jauzo.com/2023/09/10/data-integrity/)
* [Part 8: Communication Patterns in Data Integrations](https://jauzo.com/2023/09/11/data-integration-communication-patterns/)
* [Part 9: Ordering, Transactions and Exactly-Once Semantics in Data Integrations](https://jauzo.com/2023/12/12/data-integration-ordering-etc/)
* [Part 10: Master Data and Façades](https://jauzo.com/2023/12/13/master-data-and-facades/)
* [Part 11: Optimizing Development vs. Maintenance Costs](https://jauzo.com/2023/12/13/capex-opex/)
<!-- dip links end -->

***

Data integrity is especially important in data integrations, whether you use batch or stream processing to deliver data.
There are multiple communication patterns available, and only some of them are useful for real-time integrations. All of them
have some caveats regarding data integrity.

### Full Copy

Traditional batch data integrations are typically the easiest to make robust in
terms of single-system data integrity.

If you make a full database copy from source to the target system in a single
step, you avoid many common pitfalls related to incremental data transfer.

Well-established products, such as Informatica, help in monitoring and error handling.

This solution is not suitable for near real-time streaming data integration, however.

### Online Iterative Push

When pushing data iteratively from source system, you are exposing yourself to 
new failure modes. In modern systems, REST calls are a common method for 
pushing the data.

However, such solutions depend on both source and target systems availability
when the data is created. It is possible to recover from temporary failures by 
implementing resend mechanism in the source system. Some integration platforms
support temporary resend as well. 

But such solutions might not be robust in case of source system failures, 
as the resending happens in memory, and not transactionally. Also, if there 
is a major service disruption, then temporary recovery mechanisms will fail,
causing cascading failures in other systems.

### Notification Plus Iterative Pull

Another alternative is to use some kind of off-band mechanism to notify the 
target system that there are changes in the source system. The notification
might include some identifier for the changed entity. Source system then fetches the data, 
often using a REST call.

This solution may be more robust regarding failures, depending on the
notification mechanism. Some solutions can enforce single ordering of events. 
Apache Kafka is commonly used, which allows the target system to acknowledge the
notification only after the change has been permanently stored.

The weakness of this kind of solutions is subtle. If there are multiple changes to 
entities, there will be multiple notifications. It is possible to use de-duplication
on the notification events, but making de-duplication robust is costly
and difficult to implement.

When there are duplicate notifications for an entity and related entities, they may cause 
cascading changes to other systems that happen in different order. This is not only a theoretical 
issue. If you have a frontend for changing customer contact information and the single save button will cause
multiple change events (for example one for phone number, another for address etc.) on the customer 
data master system, there are situations when conflict will happen when customer data is
replicated to an another system.

### Entities In Queues

The traditional mechanism for streamed data integrations is to use queues. The difference
between notification is to include the actual data in the queue messages.
This is difficult to make work for data with high volume and high latency, such as trading data, 
but in most cases the requirements are not so demanding.

This is the most robust mechanism, but even this solution has some caveats.
One source of issues is the granularity of the messages. (This is not only related to queues,
but any solution that sends the changes incrementally will have the same issue.)

One business action, such as creating a new customer, may cause creation of
multiple conceptual level entities, and even more database entities. If
customer needs to be created in multiple systems, such as the customer data master and
the CRM, synchronizing the business action with changes in entities becomes even more difficult.

Database Change-Data-Capture (CDC) mechanisms work on the granularity of the 
database-level entities. But it is often preferable to stream changes to entities on 
the logical level. You could rebuild logical changes from physical changes in the integration
layer, but this would push complex application logic to integration components. Therefore, it is 
preferable to capture logical changes already in the source system. This proably requires a
custom solution.

You also need to be careful how to handle the error situations in the source
system, such as when queue service is not available. The basic option is to
fail the operation in the source system if writing to queue fails. Sometimes
this is not possible. Alternative option is to record the change events
permanently in the source system. This option, called the transactional outbox,
is in practice the most robust way to implement systems.

***

If you need consulting related to system architectures in general, or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.
