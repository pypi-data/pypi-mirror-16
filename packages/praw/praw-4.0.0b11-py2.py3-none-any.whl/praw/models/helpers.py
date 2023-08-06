"""Provide the helper classes."""
from json import dumps

from ..const import API_PATH
from .base import PRAWBase
from .reddit.multi import Multireddit


class LiveHelper(PRAWBase):
    """Provide a set of functions to interact with LiveThreads."""

    def create(self, title, description=None, nsfw=False, resources=None):
        """Create a new LiveThread.

        :param title: The title of the new LiveThread.
        :param description: (Optional) The new LiveThread's description.
        :param nsfw: (boolean) Indicate whether this thread is not safe for
            work (default: False).
        :param resources: (Optional) Markdown formatted information that is
            useful for the LiveThread.
        :returns: The new LiveThread object.

        """
        return self._reddit.post(API_PATH['livecreate'], data={
            'description': description, 'nsfw': nsfw, 'resources': resources,
            'title': title})


class MultiredditHelper(PRAWBase):
    """Provide a set of functions to interact with Multireddits."""

    def __call__(self, redditor, name):
        """Return a lazy instance of :class:`~.Multireddit`.

        :param redditor: A string or :class:`~.Redditor` instance who owns the
            multireddit.
        :param name: The name of the multireddit.

        """
        path = '/user/{}/m/{}'.format(redditor, name)
        return Multireddit(self._reddit, _data={'name': name, 'path': path})

    def create(self, display_name, subreddits, description_md=None,
               icon_name=None, key_color=None, visibility='private',
               weighting_scheme='classic'):
        """Create a new multireddit.

        :param display_name: The display name for the new multireddit.
        :param subreddits: Subreddits to add to the new multireddit.
        :param description_md: (Optional) Description for the new multireddit,
            formatted in markdown.
        :param icon_name: (Optional) Can be one of: ``art
            and design``, ``ask``, ``books``, ``business``, ``cars``,
            ``comics``, ``cute animals``, ``diy``, ``entertainment``, ``food
            and drink``, ``funny``, ``games``, ``grooming``, ``health``, ``life
            advice``, ``military``, ``models pinup``, ``music``, ``news``,
            ``philosophy``, ``pictures and gifs``, ``science``, ``shopping``,
            ``sports``, ``style``, ``tech``, ``travel``, ``unusual stories``,
            ``video``, or ``None``.
        :param key_color: (Optional) RGB hex color code of the form `#FFFFFF`.
        :param visibility: (Optional) Can be one of: ``hidden``, ``private``,
            ``public`` (Default: private).
        :param weighting_scheme: (Optional) Can be one of: ``classic``,
            ``fresh`` (Default: classic)
        :returns: The new Multireddit object.

        """
        model = {'description_md': description_md,
                 'display_name': display_name, 'icon_name': icon_name,
                 'key_color': key_color,
                 'subreddits': [{'name': str(sub)} for sub in subreddits],
                 'visibility': visibility,
                 'weighting_scheme': weighting_scheme}
        return self._reddit.post(API_PATH['multireddit_base'],
                                 data={'model': dumps(model)})
