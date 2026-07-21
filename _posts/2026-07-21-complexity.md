---
layout: post
title:  Complexity
description: 'Strategies for managing complexity'
date:   2026-07-21 8:05:00 +0300
image:  '/images/braided-rope.png'
seotags:   [complexity,software,platform,data-integrity]
tags:   [complexity,software,platform,data-intergrity]
---

Complexity arises from having many tangled parts. Complexity means that you cannot realistically look at each 
part separately, because it can only be understood in relation with the other parts.

Complexity may be intrinsic -- directly related to the problem we are trying to solve. Or it may be 
incidental -- related to how we are solving it. When we put these two types of complexity on a matrix, we 
can look at the ways how to unentangle the complexity.

***

Simplicity is necessary if you want to build reliable systems. Often we confuse simplicity with ease,
such as familiarity with the solution (microservices) or experience in a certain tool (Java). Simplicity 
does not come automatically, but requires additional effort and focus.

> *Simplicity is prerequisite for reliability.*
> -- Edsger W. Dijkstra

Solution is overengineered when intrinsically simple problem has an incidentally complex solution.
In such a case, you may be able to refactor the solution, if you start by clarifying your requirements. What 
is really the problem you want to solve? Do you really need the flexibility of seperate deployment? Do 
you really need the scalability at this stage? Often you will find that a simpler solution is possible.

![Complexity matrix](/images/complexity-matrix.png)

If you have a incidentally complex solution to a intrinsically complex problem, in other words 
you have complexity^2^, you might no longer be able to refactor the solution. You might not even 
be able to seperate the intrinsic complexity from incidental complexity. 
Even if we rewrite the system, how do we avoid the complexity creeping in?

> *I don't know.*
> *I don't want to know.*
> -- Rich Hickey in [Simple Made Easy](

We want to created components that encapsulate the complexity. But encapsulation is often based on
leaky abstractions. Good examples are rare, because you need to understand the problem domain, 
you need to understand many different kind of approaches, and avoid overengineering and other
traps.

One example of a system that encapsulates complexity well is the relational database. Various trends have not
been ble to replace relational databases.

Another class of systems that has encapsulated complexity succesfully are the transaction processing monitors 
(TP Monitors) running on mainframe, such as CICS and Tuxedo.

These are sharks, not dinosaurs, examples of *radical encapsulation*, as they can be used to solve
wide range of general computing problems.

Can we learn something from these systems for the modern times?

***

If you need consulting related to system architectures in general, or LLMs or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.
