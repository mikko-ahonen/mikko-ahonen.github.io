---
layout: post
title:  Data Integration Methods
description: Extract-Tranform-Load (ETL) is the traditional method for data integrations. More modern methods are Extract-Load-Transform (ELT). Sometimes APIs may also be used for data integrations. Data streaming has some benefits over all the alternatives.
date:   2023-08-28 09:55:00 +0300
image:  '/images/industrial-piping.jpeg'
seotags:   [datahub, data-integration, data-integration-platform, architecture, integration, etl, elt, api, data-streaming]
tags:   [data integration]
---
This post is third part in a series about building and adopting a modern streaming 
data integration platform. Here we discuss different methods for data integration, 
from Extract-Transform-Load (ETL) to data streaming.

Previous parts:
* [Part 1: Why to Build a Data Integration Platform?](https://jauzo.com/2023/08/11/why-dip/)
* [Part 2: About Logging](https://jauzo.com/2023/08/25/logging/)

***

Extract-Transform-Load (ETL) is the traditional, and most widely adopted
approach to data integrations. It is common for example when using data marts 
for data analytics.  The ETL is a well-established technology, and proven tools exist for it. It 
is also a relatively simple to create reliable data replication. 

ELT has downsides as well. If the source system data model is used directly, it encourages tight 
coupling between source and sink systems. Additionally, in such cases, the sink system
users need to understand the source system data models.

Another downside is that the ETL typically uses batch processing with the
full copy of the relevant tables in the source database. This limits replication frequency, 
especially if the database sizes grow. If you need to add new tables, there are
changes to the whole data pipeline.

Wide adoption of data marts has been critisized for contributing to the siloing of data.
Data warehouse, a single repository for structured data, was introduced as an
answer to the data siloing. The ETL method is typically used in data warehouses as well. 

Later, new products, such as Hadoop, contributed to the emergence of what is 
called a data lake. These products allowed ingestion of unstructured data along the
structured data. As organizations may have lots of unstructured data, 
the data lake allows access to more of the data in the organization.

| Extract-Transform-Load | Extract-Load-Transform | API-based          | Data Streaming         |
| ---------------------- | ---------------------- | ------------------ | ---------------------- |
| * Traditional method for reporting and analytics  | * More recent method for reporting and analytics | * Typical method in operative applications | * More recent method for operative applications |
| * Has good tooling, well-understood    | * Cloud tooling still under active development | * Has good tooling, well-understood, integration platforms may help | * Integration platform must support data streaming |
| * Often batch processing | * Often batch processing with cloud data pipelines | * Data stays in the source system | * Near real-time data streaming |
| * For data marts and data warehouses | * For data lakes | * For operative applications | * For cost-efficient, performant and reliable operative applications in enterprise environments |
| * Data freshness challenging | * Data freshness challenging, data marts expensive | * Backend systems may limit availability and performance, multiple copies of data models | * Not suitable for highly interactive use |

Data lakes use a new integration method, Extract-Load-Transform (ELT).
All the data in the source systems is extracted and loaded into the data lake. 
Transformation is done only for the data that is needed somewhere is transformed before 
consumption. This has the benefit that only transformation phase of data pipeline
needs to be changed when new data is needed.

Many organizations learned that data lakes became dumping grounds for unstructured, semi-structured 
and structured data and data lakes turned into data swamps. The formats for different kind of data are naturally 
different -- think video vs. database table. Data quality is difficult to handle, meaning
quality issue flow downstream. It is also difficult to find the data from data lakes,
and data is often duplicated in multiple places.

Both ETL and ELT typically use batch processing. If data sizes are large, 
the data is synced perhaps once per day. For reporting and analytics this
is usually not a problem -- it may even be a beneficial. But operational
applications may have different needs for data freshness. If the end customer signs
up for a service, then it should be visible almost immediately on the web 
service.

Therefore, direct APIs are often used for data integrations for operative
applications. The data needed by operative applications may reside in multiple 
backend systems. In typical modern architecture, the data is mapped to a 
more suitable data model, perhaps inside the operative application.
If you have many operative applications, each will neturally evolve their own internal
data model. Ultimately, you end up with multiple custom data models for the same data. This
encourages tight couoling, making data model changes difficult in the source systems.
Some backend systems might also not support the performance and availability 
needs of operative applications.

Another approach to data integrations is data streaming. If you have established
log of all the changes to the source data, then applying those changes to another system
allows you to maintain near real-time copy of the original data.

The benefit of this method is that providing access to near real-time data becomes possible. Also, 
as creating additional copies of the data is inexpensive, serving some of the complex
needs of the operative applications becomes possible, such as providing sufficient performance 
and availability of web services.

This approach requires investment as well. The source systems need to be modified to
support data streaming. You also need a data integration platform that supports streaming data. 
Some operative applications might also not be a good fit with the data streaming method. For example,
when the use is highly interactive, data streaming might not be suitable. 

***

If you need consulting related to system architectures in general, or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.
