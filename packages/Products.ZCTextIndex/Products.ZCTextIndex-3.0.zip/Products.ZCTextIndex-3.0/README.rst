Overview
========

This distribution contains a full text indexing facility for Zope 2 and more
specifically for Products.ZCatalog.

This product is a replacement for the full text indexing facility of
Products.ZCatalog.

Advantages of using ZCTextIndex:

- A new query language, supporting both explicit and implicit Boolean
  operators, parentheses, globbing, and phrase searching.  Apart from
  explicit operators and globbing, the syntax is roughly the same as
  that popularized by Google.

- A more refined scoring algorithm, resulting in better selectiveness:
  it's much more likely that you'll find the document you are looking
  for among the first few highest-ranked results.

- Actually, ZCTextIndex gives you a choice of two scoring algorithms
  from recent literature: the Cosine ranking from the Managing
  Gigabytes book, and Okapi from more recent research papers.  Okapi
  usually does better, so it is the default (but your milage may
  vary).

- A redesigned Lexicon, using a pipeline architecture to split the
  input text into words.  This makes it possible to mix and match
  pipeline components, e.g. you can choose between an HTML-aware
  splitter and a plain text splitter, and additional components can be
  added to the pipeline for case folding, stopword removal, and other
  features.  Enough example pipeline components are provided to get
  you started, and it is very easy to write new components.
