import wolframalpha

input = raw_input("Question: ")
app_id = "KRAKP4-EPUWHY9859"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text 

print(answer)