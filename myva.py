import wikipedia
import wolframalpha
from pip._vendor.distlib.compat import raw_input

while True:
    input = raw_input("Question: ")
    try:
        #wolframalpha code here
        app_id = "KRAKP4-EPUWHY9859"
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print(answer)

    except:
        #wikipedia code here
        print(wikipedia.summary(input))