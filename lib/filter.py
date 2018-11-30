import pykka

class Filter(pykka.ThreadingActor):
    def on_receive(self, message):
        if message.get('command') == 'filter':
            # TODO: use message.get('subject') to filter (by region, etc)
            replier_ref_ids = ['replier-1', 'replier-2', 'replier-3']
            pykka.ActorRegistry.broadcast(
                message={
                    'message': 'filtered_ok',
                    'replier_ref_ids': replier_ref_ids })
