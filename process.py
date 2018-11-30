import pykka
import time

from lib.process import Process
from lib.filter import Filter
from lib.notifyer import Notifyer
from lib.summarizer import Summarizer
from lib.replier import Replier

if __name__ == '__main__':
    Filter.start()
    Notifyer.start()
    summarizer = Summarizer.start()

    Process.start().tell({ 'message': 'started' })

    print("\n\n")
    # TODO: fix this..using sleep because its just an example
    time.sleep(3)
    print(summarizer.ask({ 'message': 'result' }))
    print("\n\n")

    # TODO: compute and do something with the summarized response

    pykka.ActorRegistry.stop_all()
