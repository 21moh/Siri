from bardapi import Bard
import os
import time

os.environ['_BARD_API_KEY'] = 'cwiH2M9HZnlpFxoknbyv4ejB0KRhRBbv0lDV7_I3cUSHTLeRF9MvoTNiojb0-C1cLYV4Aw.'

input_text = "Why is the sky blue?"

print(Bard().get_answer(input_text)['content'])