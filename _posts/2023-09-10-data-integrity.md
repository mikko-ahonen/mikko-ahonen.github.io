---
layout: post
title:  Lost Integrity On Data Integrity
description: It seems we have lost our integrity on data integrity. We build systems mostly with eventual consistency as the default approach. At best, eventual consistency pushes the data integrity issues to application developers. At worst, data integrity is just ignored and resolved when problems arise. Better approaches have been available at least from the 1970s, but they seem to be ignored in modern software development.
date:   2023-09-10 08:18:00 +0300
image:  '/images/disintegration.png'
seotags:   [data, data-integration, data-integrity]
tags:   [data integration]
---

This post is seventh part in a series about building and adopting a modern streaming data integration platform. In this post
I discuss our lost integrity on data integrity.

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

In modern software development, microservice architectures are the norm. 
In microservices architecture, you need to split your systems into smaller services. 
As services are seperate, you will have references that cross the service boundaries. 
Microservice architectures make it very difficult to maintain proper data integrity. 

Having worked in financial sector as well as in Core R&D for a distributed
database system, I have learned to appreciate data integrity. But even if your system does
not directly have strict data integrity requirements, taking data integrity
seriously would simplify application development and make applications more robust.

Single microservice can trivially keep the data integrity by storing data in a database. 
However, in practice microservices are not built in a way that guarantees the data integrity over 
the service boundaries.

In the end, we are contended with eventual consistency. At best, eventual
consistency pushes the data integrity issues to application developers. At
worst, data integrity is just ignored and issues are resolved when they arise.

Better approaches have been available at least from the 1970s, but they seem to be
ignored in modern software development.

There are approaches, such as using compensating transactions in the case of
failures (also known as sagas), that may alleviate the issue somewhat. But this
does not guarantee isolation of changes. The data is typically visible immediately,
and it may already be propagated to some downstream systems. Compensating
everything becomes impossible.

If data integrity is serious requirement for the system, you often develop ad hoc custom 
distributed transaction handling logic. This requires lots of effort. It is also 
very difficult to get the details correct in all of the error scenarios.

Databases have solved the data integrity problem already in 70s. Why are we
leaving the difficult part of software development, the data integrity, to the developers?
Why don't we have platforms that help us with data integrity? Is the selling
point of microservices, the ease of seperate development and deployment, worth the price? 
A pushback against microservice architectures seems to be brewing, and I think it is
partly for this reason. But that is a seperate discussion.

An ex-collegue gifted me with a t-shirt with the text I &#9829; Mainframe. Neither
of us has much real-life experience using mainframes, so we have this romantic
notion the data integrity features of Transaction Processing Monitors (TPM)
such as CICS and Tuxedo.

In TPM, you can build services. Their scope can roughly be compared to a REST
endpoint or a serverless service (such as AWS Lambda). The
difference is that the TPM services can call other services within the context
of the higher transaction.  Eventually, when the service call tree has been
completed, the transaction is either committed or rolled back, maintaining the
data integrity, including all the ACID properties (atomicity, consistency, isolation
and durability).

Modern software development is missing a modern equivalent of those mainframe
TPM systems.  We need a platform where it is possible to write services that
call other services in the context of a transaction, while still keeping the
ability to deploy each service separately. It could be built on top REST or
serverless technology, but the performance penalty may be too high.

Imagine how much easier it would be to develop applications when you can rely
on data integrity.

***

If you need consulting related to system architectures in general, or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.
