---
layout: post
title:  Role of Data Modeling in Data Integrations
description: When working with data integration platforms, it makes sense to think about your information architecture, especially the role that data modeling has in your integrations.
date:   2023-08-29 10:48:00 +0300
image:  '/images/dark-tile.jpeg'
seotags:   [datahub, data-integration, data-integration-platform, architecture, integration, data-modeling]
tags:   [data integration]
---
This post is fourth part in a series about building and adopting a modern streaming data integration platform. Here we 
discuss how the information architecture and data modeling are related to integrations.

Previous parts:
* [Part 1: Why to Build a Data Integration Platform?](https://jauzo.com/2023/08/11/why-dip/)
* [Part 2: About Logging](https://jauzo.com/2023/08/25/logging/)
* [Part 3: Data Integration Methods](https://jauzo.com/2023/08/28/data-integration-methods/)

***

Your Information Architecture (IA) may include data models at various levels of granularity.

| Contextual data model  | Conceptual data model | Logical data model | Integration data model | Physical data model |
| ---------------------- | --------------------- | ------------------ | ---------------------- | ------------------- |
| Block-level diagram of high-level subject areas and what kind of entities there are | Most important entities and their key attributes | All entities and all of their attributes, but no concern for implementation details | All entities and their attributes, data transfer details may impact models | All entities and their attributes, implementation details may impact models |
| Useful for example for specifying ownerships, making roadmaps, as high level map |  Useful for facilitating a wide agreement on key concepts within organization | Useful as the basic building block of IA | Useful as canonical data model when using hub-and-spoke integrations, not point-to-point integrations | Useful for understanding individual systems |

Not all of these levels are needed in all organizations. However, the bigger
the organization, more levels you will probably find useful.

If you are at least a medium size enterprise, you typically have "wide data" (and not "tall data").
In other words, you have large number of entity kinds but but less each kind of
entity. Your entity counts might be in the millions per kind, rather than in the
billions. In this case, creating a full-blown logical data model from zero is
probably going to take several years. By the time you are done, the logical
data model is already outdated.

Most of the cost of implementing integrations is about specifying what needs to
be done. Agreeing on syntax (such as CSV or JSON) and attribute names is pretty
straight-forward. The real cost is in understanding the business semantics of
various fields and their possible values, and how they need to be mapped and
cleaned up for downstream systems. By using canonical data models in your
integrations, it is possible to reduce the costs of later integrations.

In one organization, there was a need to work on the Information
Architecture. At the same time, we were developing DataHub, centralized integration platform with
support for real-time data streams. DataHub required having a coherent canonical
integration data model.  We saw that there was synergy between the IA and DataHub,
so we integrated these two developments.

One version of the contextual data model already existed, and some parts of
logical data model were fairly recent and useful. We started by organizing a
series of workshops to create the conceptual data model for the most important
subject areas.  This allowed us to better understand many central concepts and
agree on terminology throughout the organization.

Next we initiated a process where each new integration -- and actually indeed all
new development -- was started with collecting data needs on a form. These forms
were then used as the input for iteratively extending the logical data model.
We chose the iterative approach, because we knew that a comprehensive and detailed
logical data model would take several years to finish, and we did not have that time.

When possible, we also identified and collected the reference data that could be
used to formally define the value set for the attribute. There was both 
internal and external reference data.

Because we developed the logical data model iteratively, our integrations
needed to support iterative approach as well.  For this purpose, we developed
our own Domain-Specific Language (DSL) that was used to define the integration
data model.  This proved to be a great idea, although there was some hesitance
in the beginning.

Many schema languages exist, and we could have used one of them for defining
the data model.  But all of them had some restrictions on the extensibility due to 
their syntax. Having our own DSL made it possible for us to use the same definitions 
for multiple purposes with the exact semantics we needed.

The data models, described with DSL, were stored in the git repository. This allowed us to 
establish a release process for the data models. The system supported multiple concurrent 
versions of the data models, with fully automated schema evolution.


***

If you need consulting related to system architectures in general, or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.