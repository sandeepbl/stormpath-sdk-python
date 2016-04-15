"""Live tests of Client functionality."""


from .base import AuthenticatedLiveBase


class TestClientProperties(AuthenticatedLiveBase):
    """Assert all Client properties work as expected."""

    def test_applications(self):
        current_apps = len(self.client.applications)

        app = self.client.applications.create({'name': self.get_random_name()})

        self.assertEqual(len(self.client.applications), current_apps + 1)

        app.delete()

        self.assertEqual(len(self.client.applications), current_apps)

        total_applications_to_create = 150
        for i in range(total_applications_to_create):
            self.client.applications.create({'name': self.get_random_name()})

        self.assertEqual(len(self.client.applications), current_apps + 150)

    def test_directories(self):
        current_dirs = len(self.client.directories)

        d = self.client.directories.create({'name': self.get_random_name()})

        self.assertEqual(len(self.client.directories), current_dirs + 1)

        d.delete()

        self.assertEqual(len(self.client.directories), current_dirs)

        total_directories_to_create = 150
        for i in range(total_directories_to_create):
            self.client.directories.create({'name': self.get_random_name()})

        self.assertEqual(len(self.client.directories), current_dirs + 150)

    def test_accounts(self):
        current_accounts = len(self.client.accounts)

        app = self.client.applications.create({
            'name': self.get_random_name(),
        }, create_directory=True)

        self.assertEqual(len(self.client.accounts), current_accounts)

        account = app.create_account({
            'given_name': 'Randall',
            'surname': 'Degges',
            'email': '{}@example.com'.format(self.get_random_name()),
            'password': 'wootILOVEc00kies!!<33',
        })

        self.assertEqual(len(self.client.accounts), current_accounts + 1)

        account.delete()

        self.assertEqual(len(self.client.accounts), current_accounts)

        total_accounts_to_create = 150
        for i in range(total_accounts_to_create):
            app.accounts.create({
                'given_name': 'Randall',
                'surname': 'Degges',
                'email': '{}@example.com'.format(self.get_random_name()),
                'password': 'wootILOVEc00kies!!<33',
            })

        self.assertEqual(len(self.client.accounts), current_accounts + total_accounts_to_create)