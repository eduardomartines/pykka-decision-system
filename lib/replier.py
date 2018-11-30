import pykka
import random

class Replier(pykka.ThreadingActor):
    def on_receive(self, message):
        if message.get('message') == 'response':
            # TODO: wait and receive response from external source
            pykka.ActorRegistry.broadcast(
                message={
                    'message': 'replier_response_ok',
                    'replier_ref_id': message.get('replier_ref_id'),
                    # TODO: get original response from replier
                    'data': round(random.uniform(2000.00, 4000.00)) })
            self.stop()
