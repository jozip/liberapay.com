import mock

from liberapay.models.participant import Participant
from liberapay.testing import Harness


class EmailHarness(Harness):

    def setUp(self):
        Harness.setUp(self)
        self.mailer_patcher = mock.patch.object(Participant._mailer.messages, 'send')
        self.mailer = self.mailer_patcher.start()
        self.addCleanup(self.mailer_patcher.stop)
        sleep_patcher = mock.patch('liberapay.models.participant.sleep')
        sleep_patcher.start()
        self.addCleanup(sleep_patcher.stop)

    def get_last_email(self):
        return self.mailer.call_args[1]['message']
