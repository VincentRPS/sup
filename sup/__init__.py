"""SUP, The Story Utility Package Module.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SUP helps making stories or games with options, diverging paths, different endings and so on.

You can run a story in a minimum of 2 lines of code / 1 terminal command.

.. code-block:: python3

    from sup import Story

    Story("YourStoryName").start()

``sup yourstoryname``

You can also run stories online without installing them or upload your own for others to play.
You can find / upload stories in the `GitHub repo's atlas folder <https://github.com/EnokiUN/sup>`_.

.. code-block:: python3

    from sup import OnlineStory

    OnlineStory("OnlineStoryName").start()

``sup onlinestoryname -online``

The module has its own file extention (.sus standing for Story Utility Script) where all the
other stuff including the story's script, options, endings, attributes and more are in a way
designed to be fast and simple with basic syntax that's easy to learn and use for even people
with little to no programming knowledge and skill allowing anyone to create their own stories.

"""

__title__ = 'SUP'
__author__ = 'EnokiUN'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2021-present EnokiUN'
__version__ = '0.1.2.1a'

__all__ = ["Story", "StoryError", "OnlineStory"]

from .story import Story
from .storyerror import StoryError
from .onlinestory import OnlineStory
