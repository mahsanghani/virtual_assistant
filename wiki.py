import wikipedia
from pip._vendor.distlib.compat import raw_input

while True:
    my_input = raw_input("Question: ")
    print(wikipedia.summary(my_input))