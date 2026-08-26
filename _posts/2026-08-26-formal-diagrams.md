---
layout: post
title:  Should diagrams be formal?
description: 'Should diagrams be formal?'
date:   2026-08-26 07:06:00 +0300
image:  '/images/blackboard.png'
seotags:   [bpmn,usm,modeling,diagrams]
tags:   [bpmn,usm,modeling,diagrams]
---

Sometimes, an innocent question can lead you deep into a rabbit hole, teaching you interesting things.

Diagrams are like maps. Maps omit some details and exaggerate others. For example, on a road map, the road 
symbols are exaggerated and other details are omitted, to make the maps more useful.

However, [the map is not the territory](https://en.wikipedia.org/wiki/Map%E2%80%93territory_relation)
and we should be careful not to confuse the diagram with the thing it illuminates.

***

Recently, I wanted to understand why Business Process Modeling Notation (BPMN) does not allow sequence flows
(continuous lines) to cross pool boundaries. If you cross pool boundaries, you must use seperate processes 
and message passing (dashed lines) between them, complicating the diagrams.

In BPMN, pools mark the process control boundary. Sequence flow is only allowed within a single process. BPMN has 
roots in process automation, where control structure is important, explaining the origins for the rule.

Organization and resource modeling is not fully in the scope of BPMN. For instance, there is no
standard way to define the Accountable role. It can appear for example in approval/decision 
steps, linked RACI models, annotations or in vendor-specific extensions.

The core BPMN notation has 116 element types, and research has found at least 267 element types. Most 
diagrams use only 10 basic elements, and 85% use 14 or less. The elements beyond the core 
set are shortcuts, that can be represented with the basic elements.

Sometimes the ambiguity in diagrams is useful. For example, the symbols in maps are not formally defined. 
For example, on a road map, the line width does not fully correspond with the road width.

It seems BPMN is a good drawing notationflow, but not sufficient for comprehensive formal process 
definitions. As we cannot use simple sequence flows to show how the responsibility flows across 
organizational boundaries, the responsibilities need to be defined separately. To communicate 
clearly using BPMN diagrams, it seems a good idea to keep to the basic elements.

**

If you need consulting related to system architectures in general, or LLMs or data integrations in
particular, please do not hesitate to contact Mikko Ahonen through the contact page.
