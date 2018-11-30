import pykka

from lib.replier import Replier

class Notifyer(pykka.ThreadingActor):
    def on_receive(self, message):
        if message.get('command') == 'notify':
            repliers = [Replier.start() for _ in range(len(message.get('replier_ref_ids')))]

            for index, replier in enumerate(repliers):
                replier.ask({
                    'message': 'response',
                    'replier_ref_id': message.get('replier_ref_ids')[index],
                    'subject': message.get('subject') })
