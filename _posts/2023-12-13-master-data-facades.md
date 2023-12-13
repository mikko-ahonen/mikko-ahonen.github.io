---
layout: post
title:  Master Data and Façades
description: 'Lots of Master Data is locked in legacy systems. We need a migration path to release the data.'
date:   2023-12-13 09:18:00 +0300
image:  '/images/facade.png'
seotags:   [data, data-integration, architecture]
tags:   [architecture]
---
This post is tenth part in a series about building and adopting a modern
streaming data integration platform. In this post I will discuss how to release the master data locked in 
legacy systems, such as mainframes. 

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

***

When modernizing the architectures, some issues tend to repeat. One of such
issues is how to provide access to legacy systems, such as mainframes, that
hold important master data. Legacy systems are typically being phased out, and
it is difficult to justify building new, complex integrations to those systems.
But we still mechanisms to access the data and the logic in them, while those
systems are still running.

One common way is to create a façade in front of the legacy system, emulating
the APIs of the modern system. The API calls in the façade are implemented by
using calls to the legacy system. Then you gradually replace the calls to the
modern implementation.

The modern implementation should have the same API as
the façade, so you need to put effort in the design of the API. When all the
API calls have been implemented by the modern system, the façade is no longer
needed.  This is called the Strangler Fig pattern, a name popularized by
[Martin Fowler](https://martinfowler.com/bliki/StranglerFigApplication.html).

![Original Strangler Fig pattern](/images/strangler-fig.png)

When the façade is used to stream data, we need a little bit more complex
pattern.  Often mainframe systems cannot stream changes, so the intermediate
system often needs to pull database dump from the legacy system, compare the
result to the previous data dump, and then create a series of changes based on
the differences.

As the intermediate system is more complex, a façade is not
really an adequate name for it. Here we call it a "temporary modern system",
because it often contains some of the functionality of the modern system, but
might be replaced by a more permanent modern system later.

![Streaming Strangler Fig pattern](/images/streaming-strangler-fig.png)

In the original Strangler Fig pattern, the programming language choice is not
very important. You can also use an integration platform for this purpose. Basically, 
you need to carry out the API calls to the legacy system, and translate
data into more modern format, often JSON. Most modern programming languages
support this. However, in the streaming version of the Strangler Fig pattern,
you need more complex data manipulation, as well as a way to store the data. It is 
also beneficial if you can easily build user interfaces for manipulating some
data entities.

Low coding platforms, such as Outsystems, have recently gained popularity.
These platforms promise to make software development more productive. 
This is often understood to mean that the software development will be
cheaper. This would decrease the pressure on tight IT budgets.  Some platforms
even claim to empower "citizen developers". Are these platforms well suited
for building systems for Streaming Strangler?

The underlying idea of low coding is not new. During 80s and 90s, there was a
similar development, under the name Fourth Generation Languages (4GL). 4GL
languages were contrasted with Third Generation Languages (3GL), 
the traditional programming languages popular at the time, such as C, Pascal, COBOL, 
and so on.

Multiple kinds of 4GL products existed. Some succesful 4GL environments
revolved around "graphical" design tool to quickly create forms.
One popular such product was Oracle Forms. Also, there existed 4GLs that used 
text-based "programming language", such as Progress 4GL. However, the promised 
revolution, where 4GL would replace 3GL, never materialized.

Ultimately, 4th generation languages were judged to be less capable
than 3rd generation languages. For example, Progress 4GL name was changed to
"OpenEdge Advanced Business Language in order to overcome a presumed industry
perception that 4GLs were less capable than other languages." [^1]

Experienced developers and architects are often suspicious of
promises of order-of-magnitude improvements in software development productivity.
As the saying goes, there is "No Silver Bullet" [^2]. The lesson from 4GL
languages is that there is a hidden cost related to the promised productivity.

In trivial exmples, the low coding platforms may show promising productivity
improvements. But once you implement non-trivial applications, such as in our
use case, you start to encounter the limitations of the platform. To bypass the
limitations, you need to develop complex work-arounds that will offset any cost savings
from the initial development phase, and cause lots of developer frustration.
Low coding platforms may also have much higher licensing costs. 

Often up to 80% of the TCO of a system comes from the maintenance. Another 
large contributor to the TCO is knowing what to develop. The latter cost is
often not fully included in the calculations, because some of it happens outside the 
software development project. One example are the failed iterations of
the project. Several methods to reduce the cost and risk related to knowing
what to do have emerged, such as making wireframes, user interface prototypes,
incremental development methods, requirement specifications etc.

Low coding platforms may help, for example they may allow developing
inexpensive prototypes. But an alternative approach can provide the same
benefits without the limitations of the commercial low coding platforms.

Some open source web frameworks have survived over time, and matured to
include the benefits of low coding platforms, with some key benefits over them.

Firstly, there are no licensing costs in developing or running applications
with these frameworks, as these frameworks are open source. Secondly, these
languages expose the underlying general programming language and 
provide extensibility in a way that low coding platforms cannot do.

The most popular web frameworks are Django and Ruby on Rails. Rails is
currently more popular for building websites, but Django has a few clear benefits
for our Streaming Strangler Fig pattern use case.

Django uses the Python programming language, while Rails uses Ruby. Python has very high
market share in data manipulation tasks in general, and data sciences in
particular, especially in enterprises. Python is the most popular programming language
according to TIOBE [^3], while Ruby is 19th.

Django also has very good database schema migration framework, simple mechanism
for building REST APIs, and build-in admin UI for basic data manipulation
tasks.

Django hits the sweet spot for building the intermediate temporary system
needed in our Streaming Strangler Fig pattern.

***

If you need consulting related to system architectures in general, or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.

***

[^1]: [https://en.wikipedia.org/wiki/OpenEdge_Advanced_Business_Language](https://en.wikipedia.org/wiki/OpenEdge_Advanced_Business_Language)
[^2]: [https://en.wikipedia.org/wiki/No_Silver_Bullet](https://en.wikipedia.org/wiki/No_Silver_Bullet)
[^3]: [https://www.tiobe.com/tiobe-index/](https://www.tiobe.com/tiobe-index/)
