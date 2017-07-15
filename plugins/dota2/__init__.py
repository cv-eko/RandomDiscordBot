import random
import dota2

command = "dota"
type = "message"

def process(args,client):
    return random.choice(list(dota2.get_all_heroes()))