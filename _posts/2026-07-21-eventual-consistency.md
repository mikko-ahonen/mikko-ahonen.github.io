---
layout: post
title:  Eventual Consistency Is A Lie
description: 'An eventually consistent system is never guaranteed to be in consistent state'
date:   2026-07-21 8:05:00 +0300
image:  '/images/labyrinth.png'
seotags:   [complexity,software,platform,data-integrity,eventual-consistency,sagas]
tags:   [complexity,software,platform,data-intergrity,eventual-consistency,sagas]
---

The concept of *eventual consistency* often comes up when modern enterprise architectures are discussed,
especially in the context of microservices.

In typical configuration, an eventually consistent system is actually never guaranteed to be in consistent 
state. Therefore, it is more precise to say that the system is perpetually inconsisent, and at the minimum,
saying that a system is eventually consistent is a lie. And this is a dangerous lie, because it hides the 
complexity that arises.

***

To illustrate, let's take a simplified real-life example. Let's say that we are building a 
system where customers and orders are stored in different microservices. The order entity refers to 
a customer through weak links, using the customer identifier. 

The customer creation often takes several minutes, so it is often done asynchronously. The customer may be 
created through various processes, for example during ordering process. 

Now let's assume that we have a requirement that we should be able to complete orders even if the microservice 
containing customers is down. In this case, we would probably naturally generate a unique identifier for 
the customer on the ordering system (using UUID or similar), and then pass the identifier when generating the
customer.

In this case, all applications that show the order details must accomodate a scenario where the customers 
are assigned an identifier, but the customer details are actually not yet visible on the customer microservice.

In some scenarios, we might want to revert the customer creation. As the customer was created, in eventually 
consistent systems, the typical pattern is to send a compensating transaction (using the saga pattern) to 
the customer microservice.  However, some downstream microservice, such as invoicing, might already have 
used the creation event to create data that depends on the customer.

Although this example is a little contrived for illustration purposes, such situations are very typical 
in eventually consistent systems. All kind of complex distributed error scenarios arise, and the 
responsibility for recovering from various scenarios is pushed to the user interface developers. Without
very comprehensive testing for data, you can easily end up with flaky user interfaces.

In modern microservices architectures, no commonly used solutions exist for this issue. Historically,
transaction processing monitors (TP Monitors, such as CICS and Tuxedo) solved this by allowing service calls
to form a tree, where all calls where executed within the same transaction context, maintaining strong
data integrity.

In modern times, even this is not enough. Often we are communicating with internal and external systems
through APIs, over potentially unreliable networks and high latencies, and there is no way to run these 
within the same transactional context.

We have traded data integrity for some flexibility and scalability, creating lots of incidental
complexity. The difficult problems are left for the developer. This seems like a bad trade-off.

***

If you need consulting related to system architectures in general, or LLMs or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.
