import pykka

class Process(pykka.ThreadingActor):
    def __init__(self):
        super(Process, self).__init__()
        self.subject = {}

    def on_receive(self, message):
        if message.get('message') == 'started':
            pykka.ActorRegistry.broadcast(
                message={
                    'command': 'filter',
                    'subject': self.subject })
        elif message.get('message') == 'filtered_ok':
            pykka.ActorRegistry.broadcast(
                message={
                    'command': 'notify',
                    'replier_ref_ids': message.get('replier_ref_ids'),
                    'subject': self.subject })
