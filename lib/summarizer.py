import pykka

class Summarizer(pykka.ThreadingActor):
    def __init__(self):
        super(Summarizer, self).__init__()
        self.result = {}

    def on_receive(self, message):
        if message.get('message') == 'replier_response_ok':
            self.result[str(message.get('replier_ref_id'))] = message.get('data')
        elif message.get('message') == 'result':
            return self.result
