from .models import Quote
from urllib import response
import urllib.request,json


base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_random_quote():
    url = base_url 

    response = urllib.request.urlopen(url)
    data= json.loads(response.read())
    quote_details=[]

    quote = data.get('quote')
    author = data.get('author')


    new_quote= Quote(quote, author)
    quote_details.append(new_quote)

    return quote_details