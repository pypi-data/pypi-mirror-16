Changelog
=========


1.6 (2016-08-23)
----------------

- Do not complain about brains in uid_catalog that are references.
  When their path points to `...at_references/<uid of brain>` then
  this is normal.  I started wondering about a site that had more than
  20 thousand problems reported this way.  [maurits]


1.5 (2015-07-31)
----------------

- Remove all items that have the ``portal_factory`` folder in their
  path.
  [maurits]


1.4 (2014-05-12)
----------------

- Catch KeyErrors when getting the path of a brain.
  [maurits]


1.3 (2013-09-02)
----------------

- Give less confusing message for comments that inherit the UID of
  their parent.  It sounded too much like an error.
  [maurits]


1.2 (2012-06-04)
----------------

- Improved the cleanup of non unique uids.
  [maurits]


1.1 (2012-05-14)
----------------

- When doing an reindexObject, only reindex the UID.
  [maurits]


1.0 (2012-04-27)
----------------

- Initial release
  [maurits]
