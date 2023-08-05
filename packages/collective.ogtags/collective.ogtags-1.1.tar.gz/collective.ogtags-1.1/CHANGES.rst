Changelog
=========

1.1 (2016-07-14)
----------------

- Select image field via adapter.  The default adapters work on
  dexterity and Archetypes content types and return either the image
  or the leadImage field.  [parruc]


1.0.2 (2016-06-24)
------------------

- Fixed double escaping of attributes, for example when you have ``&``
  in a title.  Fixes issue #3.  [parruc]


1.0.1 (2016-06-01)
------------------

- Fixed hidden Unauthorized error when called on a private folder with
  a published default page.  Show the image of the page anyway in this
  case, instead of showing the fallback image.  [maurits]


1.0.0 (2016-06-01)
------------------

- Fixed KeyError on traverse.
  Fixes https://github.com/collective/collective.ogtags/issues/1
  [parruc]

- Moved to https://github.com/collective/collective.ogtags. [maurits]


1.0.0rc3 (2016-04-12)
---------------------

- Add support namedimagefile images.  [jladage]

- Update Dutch translations and add missing en translations.  [jladage]


1.0.0rc2 (2016-04-08)
---------------------

- Improved PyPI page.  [maurits]


1.0.0rc1 (2016-04-08)
---------------------

- Support quintagroup.seoptimizer if it is installed and enabled.  We
  use its title, description and canonical url when set.  [maurits]


1.0.0b1 (2016-03-21)
--------------------

- prevent generating duplicate image tags
  [diederik]

- Documentation
  [diederik]

- Handle images and leadimages correctly.
  [jladage]

- Initial release
  [diederik]
