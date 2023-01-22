---
layout: post
title:  Some Considerations When Working With Postgres Full-Text Search
description: There are some things that are useful to take into account when choosing between Postfres Full Text Search (FTS) and external indexing solutions such as ElasticSearch
date:   2009-01-03 15:01:35 +0300
image:  '/images/520.jpg'
tags:   #[databases, postgres, technical]
---
When one uses Postgres as a database, it is tempting to also use Postgres for indexing the data for supporting search features on the site. While ultimately this may be the best fit in many cases, the choice between Postgres Full Text Search (FTS) and external indexing solutions such as ElasticSearch is often done 
haphazadly, without understanding all the implications from the choice.

Here are some things it is useful to consider when thinking about using Postgres FTS:

1. Are you supporting multiple languages in the search? Do you wish the search to try to match any language regardlress of the language choice? Depending on how you have implemented your localization in the database, this may be more easy or more difficult.

1. Is the standard tokenizer sufficient for you? What characters should be matched exactly in your case, and which can be considered word separators?

1. Do you have fields that need exact matching, such as codes?

1. Postgres has the concept of stop words, which means that some words are so common they are ignored in the search. Are you going to have problems with this? If you are building cross-language search, stop word in one language might be a valid word in another language.

1. Do you want to support paging when viewing search results? Does your paging solution require you to provide the number of results in the interface?

1. What is the minimum number of characters you need to match your query with? If you wish to index with only one character, you may have problems with Postgres.

1. Do you need prefix-matching? Postgres FTS does not support it directly, but you need to build custom support for it.

1. Do you wish to show highlighting of the matching text in the front end? How does it need to be communicated? What if there are matches in multiple languages? 

1. Accent characters? How do you want those to behave in the searches?
