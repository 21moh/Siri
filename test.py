from bardapi import Bard
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("bwi4O0ymyiaSC1XYwBh9b_4LZHRfmUIUr-OhV9B4hpd5y7PmSoiRE3V8eQ7ds92E6vF-hQ.")
bard = Bard(token=token)  
result = bard.get_answer("What is the current stock price of NVDA?")
print(result)