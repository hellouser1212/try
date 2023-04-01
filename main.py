import cloudscraper as cs
from dhooks import Webhook, Embed
from time import sleep

scraper = cs.create_scraper()
webhook = Webhook("https://discord.com/api/webhooks/1083469447303548958/S4QTW8y_NYEoemRZJ7iMtXheXBHDVNfeYibLCmj29FV3bF6nB_T-RZR2o_IEj4UPC7c5")

rain_active = False
while True:
    if rain_active == False:
        r = scraper.get("https://api.bloxflip.com/chat/history").json()['rain']
        if r['active'] == True:
            prize = r['prize']
            em = Embed(color=0x0025ff, timestamp='now')
            em.add_field(name='Rain!', value=f'Active Rain ${prize}[join rain](https://bloxflip.com)')
            webhook.send("@everyone")
            webhook.send(embed=em)
            rain_active = True
        else:
            rain_active = False
