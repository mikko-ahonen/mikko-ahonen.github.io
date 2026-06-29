---
layout: post
title:  Transformations
description: 'Considering LLMs as transformers between different semantic representations helps us to use build more reliable systems based on them'
date:   2026-06-28 15:20:00 +0300
image:  '/images/transformers.png'
seotags:   [django,postgres]
tags:   [django,postgres]
---
We often talk about LLMs in terms of reasoning and generation. I have found it more helpful to think in terms of transformations and semantic layers. There appears to be some general principles that I have not found explicitly expressed elsewhere, on the relationship between semantic layers and transformations. Understanding them helps us to build more reliable systems with the help of LLMs.

***

The general principle could be expressed as:

> *The transformations available to a system are bounded by the semantics explicitly represented 
> in its internal model.*

Take as an example, a platform for creating training videos. If all you have is the recorded video, 
automating the postprocessing (such as highlighting the clicked element) is almost impossible. You would need
to analyze the content to understand what is going on, which is not reliable.

Now suppose the system producing the training videos also knows where the buttons, dialogs and forms are.
It can automatically zoom to the correct button, highlight a dialog, or keep an entire form visible.

The difference is in semantic representation.

If you add another semantic layer, and instead of UI elements, you make the systems aware about the actions 
available, for example that clicking a certain button is related to action *Create a Customer*. Now it becomes
possible to create an user guide, full training videos etc.

This leads to a simple second principle:

> *Each additional semantic layer enlarges the space of valid, automatable transformations.*

I think this principle shows up in many places in software development cycle. Compilers go through 
multiple intermediate representations when transforming a C program to executable. Browsers build DOM 
as an intermediate representation, instead of rendering the pixels directly.

These intermediate representations are partly done for architectural considerations, to make systems 
more maintainable. But they also appear to be fundamental in what transformations are feasible.

We can think of LLMs as semantic transformers that transform from one representation into another.

In software development, requirements are transformed into user stories, user stories are transformed 
into domain models, domain models are transformed to APIs, APIs arre transformed to code, code is 
transformed to tests. The quality of each transformation depends on how much of the semantics is explicit.

If a LLM receives a well-defined domain model and an API specification, generating code is mostly 
a direct transformation problem. If you prompt the LLM with "build me a CRM", it has to invent a domain model, 
workflows, APIs and architecture before it can write the code. In other words, it is filling the
gaps.

As LLMs have been trained on lots of code, this sometimes produces working software. But it can also
hallucinate or invent new requirements or features that were not there.

> *The reliable use of LLMs maximizes explicit semantic representations and minimizes transformations that 
> rely solely on implicit semantic knowledge.*

The key word here is *reliable*. LLMs have implicit semantic knowledge encoded in their weights. That's why 
they can and do invent what is missing to be able to complete their goal. These invented semantics 
are probabilistic.

Explicit semantics are constraints. The more meaning that is represented in the requirements, 
the more LLM becomes a reliable transformer instead of an inventor. It seems that for succesful use of 
LLMs, you need to have a taste for rich, meaningful semantic representations, and how these can interact well.

Learning LISP languages is often said to change your approach to programming in any language. One of these 
changes is that you start to think in terms of DSLs. Instead of imperatively developing the software, you envision a
DSL that would be perfect for writing your program. Then you write the program in that language. Finally you
implement that language. That is actually very useful way to approach LLM use.

***

If you need consulting related to system architectures in general, or LLMs or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.
