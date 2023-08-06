from debug_toolbar.panels import Panel
from django.utils.translation import ugettext_lazy as _


class BaseVCSInfoPanel(Panel):
    title = _('Revision')
    _cached_client = None

    @property
    def client_class(self):
        raise NotImplementedError

    @property
    def client(self):
        if not self._cached_client:
            self._cached_client = self.client_class()
        return self._cached_client

    @property
    def nav_subtitle(self):
        if self.client.is_repository():
            return self.client.get_short_hash()
        return 'repository is not detected'

    @property
    def has_content(self):
        return self.client.is_repository()

    @property
    def template(self):
        return '{}.html'.format(self.client.base_command)

    def get_stats(self):
        context = super(BaseVCSInfoPanel, self).get_stats()
        if self.client.is_repository():
            context.update({
                'short_hash': self.client.get_short_hash(),
                'hash': self.client.get_hash(),
                'author': self.client.get_author_info(),
                'committer': self.client.get_committer_info(),
                'message': self.client.get_message(),
                'updated_at': self.client.get_date(),
                'branch_name': self.client.get_current_branch_name()
            })
        return context
