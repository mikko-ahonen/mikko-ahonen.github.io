---
layout: post
title:  Lightweight Reference Data
description: Many enterprises have reference data, but it may not be systematically managed. There may be some code sets in data warehouse tables. Some larger business applications may internally some code sets as well. This post describes a lightweight option for storing subset of reference data, called code sets.
date:   2023-09-09 10:32:00 +0300
image:  '/images/dominos.jpeg'
seotags:   [datahub, data-integration, data-integration-platform, architecture, integration, data-modeling, reference-data, code-sets, code-service]
tags:   [data integration]
---
This post is sixth part in a series about building and adopting a modern streaming data integration platform. In this post 
I will describe a lightweight option for storing subset of reference data, called code sets.

Previous parts:
* [Part 1: Why to Build a Data Integration Platform?](https://jauzo.com/2023/08/11/why-dip/)
* [Part 2: About Logging](https://jauzo.com/2023/08/25/logging/)
* [Part 3: Data Integration Methods](https://jauzo.com/2023/08/28/data-integration-methods/)
* [Part 4: Role of Data Modeling in Data Integrations](https://jauzo.com/2023/08/29/data-modeling/)
* [Part 5: Data Integration Architectures](https://jauzo.com/2023/09/08/data-integration-architectures/)

***

Many larger business applications have something that can be called a code
service,  used to store and administer various code sets used by the
application. Technically, the code service might be a microservice, a set of
database tables or it might be just a set of configuration files. In this post,
I will use the term code service regardless of technology used to implement it.

The code service typically has many code sets, and each code set consists of a list of codes, 
with corresponding names. If the system supports localization, there may be multiple translations 
for the names. 

The codes are used in the application, for example for allowed values in dropdowns. Some of 
these code sets might be editable by the admin user, while others require changes to the 
software.

Also, many enterprises have some reference data in data warehouses. Examples include
list of countries or list of possible languages. Some reference data may 
follow similar simple structure as the code sets, while other reference data may 
be more complex.

The list of countries is well-defined by ISO standards. When you dig deeper, however,
there is more complexity. For example, there exists multiple (two-letter, three-letter, numeric) 
codes for each country, and not all countries have all the codes. There are also
political disputes about countries and the borders of countries.

Another example of more complex reference data is the relationship between
postal codes and municipalities.  There may also be a hierarchy between the code
sets. One typical example of a hierarchy is list of industries and the related sub-industries.

Many data quality issues are related to reference data. Some of them are obvious, 
such as when the reference data ownership is not clear, or organizational procedures to update 
the reference are not working properly. 

Another source of data quality issues is the misuse of code sets. Unless you are 
very clear about the usage, code sets easily get reused for other purpose, which appears to 
be close, but may be semantically very different. For example, list of existing 
countries might be reused as a list of countries of birth.

Such semantical data quality issues may be compounded by quick fixes. If 
a customer reports that they cannot add their country of birth, the reason might be that the country 
no longer exists. If the generic list of countries is the same as the list of 
birth countries, then the missing country will be added to the list, which will 
break the code sets both semantically and practically. Updating the data based on ISO data source
changes becomes unfeasible or at least difficult.

Adding new values to code sets may also cause more subtle issues. There are
some code sets, where adding a new value invalidates the old values. Gender is
one example. If the original options for choosing your gender are male and female, and then a new 
option is added, this logically invalidates the old data. We cannot know what the user would have
chosen if they also had the new option. This may sound a little bit theoretical, but are also practical 
issues related to adding new options. When adding new values, all the integrations that map from that code 
set need to be updated as well.

It is important to establish the ownership of reference data in the organization. One way is to
link ownership to data domains. Additionally, it is very helpful to link the reference data in general
and code sets in particular to the conceptual data models.

Commercial reference data products exist. I don't have personal experience using such 
systems, so I will not comment on them.

However, I have seen multiple custom implementations of centralized code services. As code sets
seem deceptively simple on the surface, it seems like a good idea to implement your own.

However, like always, the god is in the details. Just two commonly requested features, 
versioning and links between code sets, can make the service complex. If you allow
adding custom attributes to codes, application logic easily slips into your reference data.
If you allow additional flexibility in the data models to support custom data types needed by more
complex reference data, the service can easily become too generic. I have seen 
an effort to create a code service to fail from the complexity.

There is a lightweight approach to code sets that has proven succesful in
practice. The idea is to store code sets in a git repository using a standard JSON
format. Only simple code sets, with list of code and their corresponding localized names 
are supported. Other type of reference data is excluded from this service.

By using git, you automatically have support for versioning.  Integration
is also simple, as JSON format can be directly incorporated into application builds. 
This means that in many cases, you do not even need a seperate REST call, although you
lose the flexibility of modifying codes on the fly.

You can also create a publisher that broadcasts the reference data changes to interested parties and systems
if your git service provider (GitHub, GitLab etc.) has a method for listening of change events to the
repository. Alternatively, you can build your own publisher by detecting the changes.

I have found it useful to define the codes as typed and human-readable format 
instead of numeric values. In a corporate environment, debugging code values
from logs and integration messages becomes easier. If you want, you can use the URN (Uniform
Resource Name) standard (RFC 2141), or you can invent your own syntax.

An example of a value for "lang" code set value for Finnish could be "urn:x-xyz:code:lang:fin", where xyz 
would be your organization name. The method supports hierarchical values almost out of the box, as 
you can just add more parts to the end of the URNs.

To help adoption of such a code service, you should probably have client libraries. They should provide
the developers with enumerations (such as Java enum) of possible values of each code set. You can create 
build processes that automatically generate these libraries from the code sets. Just make sure that the
invalid values fail gracefully.

You should have a validity checker for the code sets to ensure data quality. This can be implemented
as a git pre-commit hook. The checker should verify the JSON format, required fields, required translations, 
duplicates, that the URN naming follows conventions etc.

It is helpful to provide the business users with a client for editing code set translations,
adding new codes and deprecating old codes. If you use git, this frontend should create merge 
requests from the changes. This way developers can maintain control of the changes.

Code set values should never be removed, because there may always be some system or temporary 
storage that contains those values. Instead, use a deprecation mechanism, by marking some codes as 
deprecated.

While this provides you with a lightweight code service, this is only the technical aspect. The difficult part 
will be deploying the workflows for updating the reference data, adding new reference data etc.

***

If you need consulting related to system architectures in general, or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.
