===============
Getting started
===============

We start with some basic concepts about Resolwe. Remember them well as
they will be used across documentation.

What is Resolwe, Resolwe Bio and Resolwe SDK for Python
=======================================================

`Resolwe`_ is an open source dataflow package for the
`Django framework`_. `Resolwe Bioinformatics`_ is an extension of
Resolwe that provides bioinformatics pipelines.

Together, they can handle large quantities of biological data, perform
complex data analysis, organize results and automatically document your
work in a reproducible fashion.

Resolwe SDK for Python allows you to access Resolwe & Resolwe Bio from
Python. It supports accessing, modifying, uploading and downloading the
data and also writing dataflow pipelines for Resolwe and Resolwe
Bioinformatics.

.. _Resolwe Bioinformatics: https://github.com/genialis/resolwe-bio
.. _Resolwe: https://github.com/genialis/resolwe
.. _Django framework: https://www.djangoproject.com/


.. figure:: images/resolwe_resdk.jpg
   :width: 100 %

   Resolwe and Resolwe-Bio are typically installed on a server computer
   with strong computing capabilities. ``resdk`` is a Python package
   installed on any local computer to interact with Resolwe through
   restAPI. The power of ``resdk`` is it's lightweight character - it
   can be installed with one simple commad, while it enables the
   manipulation of large quantities of data and heavy computing on a
   remote machine. As depicted on picture it can become very handy also
   for data transfer - local computer connected to both Resowle servers
   can transfer data with little effort.

Connect to Resolwe
------------------

We have a test Resolwe server on ``https://torta.bcm.genialis.com``. If
you do not have access to torta, you can use your own server or contact
us at info@genialis.com. The username and password on torta is
``admin/admin``. To connect to a Resolwe server run:

.. literalinclude:: files/resdk-example.py
   :lines: 1-5

The last two lines are not necessary, but are recommended if you are
working with ``resdk`` in an interactive session. They turn on usefull
messages that will help you understand what is happening behind the
scenes. To know more about what they do, read how the logging is
:ref:`configured in resdk<resdk_resdk_logger>` or about
`Python logging`_ in general.

.. _`Python logging`: https://docs.python.org/2/howto/logging.html

Resolwe basics - resources
==========================

In Resolwe, meta-data is stored in the PostgreSQL database tables:
Data, Sample, Collection, Study, Process, DescriptorSchema, Storage,
User and Group. We support the data management through `the REST API`_.
Each table is represented as a REST resource with a corresponding
endpont. The Sample table is a special case, represented by two
resources: ``sample`` and ``presample``. More details on samples will
follow.

In ``resdk`` each restAPI endpoint has it's corresponding class, with
the same name as in Resolwe: Process, Data, Sample... Most of these
resources are implemented in resdk as subclasses of a BaseResource
class.

.. _the REST API: https://torta.bcm.genialis.com/api/

Process and Data
----------------

Two most important resources in Resolwe are *process* and *data*.
Process represents an algorithm that transforms inputs to outputs. It
is a *blueprint* for one step in the analysis. Data object is an
instance of a process. It is a *complete record* of the process step.

Example: you have a file with reads (``reads.fastq``) and want to map
them to human genome (``hg38.fasta``) with *bowtie* alligner. To do
that, all you need to do is create a data object: define which process
to use and what are that inputs. When data object is created, it
automatically runs the specified process with the provided inputs.
A Data object can be considered as a coplete record in the sense that
it remembers what were the inputs (files, arguments, parameters...),
what was the process (the algorithm) and what are the outputs (files,
images, numbers...). Beside that, Data objects also store some useful
metadata. This makes it easy to reproduce any step in workflow as well
as simply accessing the information wheen needed.

.. note::

   In the documentation we will refer to process in two different
   contexts the first has just been presented: the blueprint for
   data object. In this respect, data object is an instance of a
   process. However, when talking about specific data object, we
   may wish to refer to the algorithm that turned inputs to
   outputs - on this specific data object. We sometimes refer to
   this as process as well. You will probably have no trouble
   recognizing the difference from the context.

In next sections we will examine how to access the content of existing
Data objects and how to create new Data objects.

Groups of Data objects
----------------------

Eventually, you will have many Data objects so it makes sense to
organize them. Resolwe includes several structures to help you group
Data objects in meaningful ways: *Sample*, *Collection* and *Study*.

*Sample* represents a biological entity. It includes user annotations
and arbitrary Data objects associated with this biological entity. In
practice, all Data objects on the sample are derived from an initial
single Data object. A Data object can belong to only one sample.
Typical set of Data object types in a same sample would be: raw reads,
allignment of reads to a reference and expression values. Two distinct
samples can never contain the same Data object

*Collection* is a working (user-defined, ad hoc) group of samples. In
addition to samples and their corresponding Data objects, collections
can also contain Data objects that are analysis results (e.g.,
differential expression that compares one group of samples to another).
Samples and Data objects can belong to multiple collections.

*Study* is an "upgraded" collection with some additional metadata.
Study relates the provenance or reason samples were generated. Each
sample can belong to only one study.

.. figure:: images/collections_relation.jpg
   :width: 100 %

   An example of how samples, collections ans studies relate. Samples
   are groups of Data objects originating from the same biological
   sample—this means that all Data objects in a sample are calculated
   from a single reads file. Collections are arbitrary groups of samples
   and Data objects that are result of analysis.

It is important to note that samples, collections and studies have
their own annotations, and the Data objects they contain have separate
annotations. An example of the annotation field on a Study is
``organism`` and an example of the annotation field on a Sample is
a ``barcode``. The annotation information for sample (or
collection/study) should hold true for all Data objects attached to it.

.. TODO: Image where clear disctinction between Resolwe models /
         endpoints and resdk classes is presented.

Query resources
===============

The ``resdk.Resolwe`` class (in the example above we named the class
instance ``res``) provides interfaces to the corresponding resource
endpoints:

* ``process``
* ``data``
* ``sample``
* ``collection``
* ``study``

Each endpoint has it's corresponding class in Resolwe

Interfaces support ``get()`` and ``filter()`` methods that enable users
to access the resources::

    resdk.Resolwe.<interface>.get(uid)
    resdk.Resolwe.<interface>.filter(**fields)

Method :any:`get() <ResolweQuerry.filter>` searches by a unique
identifier: ``id`` or ``slug``. It returns *a single object* of type
``<interface>``.

.. literalinclude:: files/resdk-example.py
   :lines: 38-42

Method :any:`filter(**fields)<ResolweQuerry.filter>` returns a *list*
of objects of type ``<interface>``:

.. literalinclude:: files/resdk-example.py
   :lines: 44-48

But the real power of method ``filter()`` is in combining multiple
search parameters:

.. literalinclude:: files/resdk-example.py
   :lines: 50

In just one line we obtained all data objects that:

* were succesfuly created (no errors)
* were made by user with id=2
* were using the process with name "Aligner (Bowtie 1.0.0)"

Additionally we ordered them by creation time and limited the number of
returned results to three. For full documentation of filter method
look :any:`here. <ResolweQuerry.filter>`

Access annotation and download files
------------------------------------

We have learned how to query the resources with ``get`` and ``filter``
methods. Now we will look at how to access the information contained
in these resources.

All the resources share some common attributes like ``name``, ``id``,
``slug``, ``created`` and ``permissions``. You can acess them like any
other Python class attributes.

Examples:

.. literalinclude:: files/resdk-example.py
   :lines: 52-59

Besides these attributes, each resource class has some specific
attributes and methods.

For example, resource classes ``Data``, ``Sample``, ``Collection`` and
``Study`` have methods ``files()`` and ``download()``.

``files()`` returns a list of all files attached to the resource:

 .. literalinclude:: files/resdk-example.py
    :lines: 105-115

Method ``download()`` downloads resource files. Optional parameters
``file_name`` and ``field_name`` have the same effect as in the
``files`` method. There is additional parameter ``download_dir`` -
it allows you to specify the target download directory:

.. literalinclude:: files/resdk-example.py
   :lines: 117-118

You can find the complete reference for each resource class and their
corresponding attributes and methods in the :doc:`Reference<ref>`.

.. note::

   Some attributes and methods are defined in
   :obj:`BaseCollection<resdk.resources.collection.BaseCollection>`
   and :obj:`BaseResource<resdk.resources.base.BaseResource>`
   classes. :obj:`BaseResource<resdk.resources.base.BaseResource>`
   is the parent of all resource classes in :obj:`resdk`.
   :obj:`BaseCollection<resdk.resources.collection.BaseCollection>`
   is the parent of all collection-like classes:
   :obj:`Sample<resdk.resources.Sample>`,
   :obj:`Collection<resdk.resources.Collection>` and
   :obj:`Study<resdk.resources.Study>`.
