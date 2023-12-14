---
layout: post
title:  Optimizing Development vs. Maintenance Costs
description: 'Maintenance may take up to 80% of the total cost of applications during its life cycle. In practice, the actual percentage depends heavily on many things, especially on the life cycle of the system. It may be useful to optimize the development costs for some systems, and maintenance for others.'
date:   2023-12-13 09:18:00 +0300
image:  '/images/house.png'
seotags:   [data, data-integration, architecture]
tags:   [architecture]
---
This post is eleventh part in a series about building and adopting a modern
streaming data integration platform. In this post I will discuss how to think about
development and maintenance costs in various parts of the architecture.

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

As a rule of thumb, maintenance may take up to 80% of the total cost of
applications during its life cycle [^1]. In practice, the actual percentage
depends heavily on many things, especially on the life cycle of the system.

Customer-facing web and mobile applications might even need a rewrite every five
years, just due to the technological progress. There are web frameworks *du
jour*, and if you are using outdated technology, it is difficult to attract and keep
talent, sometimes even consultants. It may also be important that customer-facing applications
have a modern feel. Core business systems on the other hand have much
longer life cycle. In some industries thirty years is a typical life span for
a core business system. Data may need to be stored for even longer, even 100 years.

Regardless of how software development is budgeted in practice, business people
often mentally make a difference between capital and operational expenses
(CapEx and OpEx). If you look at things from high enough vantage point, the
maintenance costs are usually operational expenses, because they are about
keeping the current business running, not investment in the new growth. Of course
the line is drawn in sand.

![System with short life cycle](/images/capex-opex-short.png)

![System with longer life cycle](/images/capex-opex-long.png)

The two diagrams above show how the cost of the initial investment plays more
significant role for systems that have short life cycle (5 years) than for
systems that have a longer life cycle (10+ years). The difference becomes even
more dramatic when the systems have a really long life cycle (30+ years).

![Optimizing CapEx and OpEx](/images/optimize-capex-opex.png)

The practical consequence is that often you should optimize development costs in
customer-facing applications and operation and maintenance costs in core
business systems. It often makes sense to take this into account when
organizing the development efforts. This often has an impact on technology
choice as well.

To keep the application development costs low, the application development
should be as easy and fast as possible. This means that much of the
implementation logic should reside on the core system side. We can call these
core systems "the platform", and should have an corresponding platform API 
to support the development of applications. The platform API should be of 
high quality and well-productized.

***

[^1]: <sub>Jeff Hanby at [Lookfar blog](http://blog.lookfar.com/blog/2016/10/21/software-maintenance-understanding-and-estimating-costs/) has collected some estimates about the maintenance costs from research.
  Daniel D. Galorath — 75%
  [http://nyspin.org/Dan%20Galorath%20-%20Development%20is%20only%20Job%201.pdf](http://nyspin.org/Dan%20Galorath%20-%20Development%20is%20only%20Job%201.pdf)
  Stephen R. Schach — 67%
  [http://courses.cs.vt.edu/csonline/SE/Lessons/LifeCycle/Lesson.html#refs](http://courses.cs.vt.edu/csonline/SE/Lessons/LifeCycle/Lesson.html#refs)
  Thomas M. Pigoski — &gt;80%
  [https://en.wikipedia.org/wiki/Software_maintenance#cite_note-2](https://en.wikipedia.org/wiki/Software_maintenance#cite_note-2)
  Robert L. Glass — 40% — 80%
  [https://pdfs.semanticscholar.org/7eee/629b22cd3db63296cac13a0c37cb0a7235f6.pdf](https://pdfs.semanticscholar.org/7eee/629b22cd3db63296cac13a0c37cb0a7235f6.pdf)
  Jussi Koskinen — &gt;90%
  [https://wiki.uef.fi/download/attachments/38669960/SMCOSTS.pdf?version=2&modificationDate=1430404596000&api=v2](https://wiki.uef.fi/download/attachments/38669960/SMCOSTS.pdf?version=2&modificationDate=1430404596000&api=v2)
  </sub>

***

If you need consulting related to system architectures in general, or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.
