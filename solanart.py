import datetime
import requests
import threading
import time
import json
 
f = open('config.json',)
config = json.load(f)

OLD_NFTS = []
webhooks = config['webhooks']
collections = config['collections']
avatar_url = config['avatar_url']
footer_name = config['footer_name']
footer_img_link = config['footer_image_url']

def delete_nft(NFT):
    global OLD_NFTS
    print("Deleting : " + NFT['name'] + " in 10 minutes")
    time.sleep(600)
    OLD_NFTS.remove(NFT)

def getDate():
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

#### HANDLE NO RESPONSE    

def sendCode(name, price, img, nft_url, webhook_name, webhook_url, collection):
    data = {
        "embeds": [
            {
                "title": name,
                "description": "Price : " + price + " sol",
                "url": nft_url,
                "fields": [
                    {
                      "name": "Collection",
                      "value": "[" + collection + "]" + "(" + "https://solanart.io/collections/" + collection + ")"
                    }
                ],
                "thumbnail": {
                    "url": img
                },
                "footer": {
                    "text": footer_name + " | " + getDate(),
                    "icon_url": footer_img_link
                },
            }
        ],
        "username": "Solanart",
        "avatar_url": avatar_url
}
    result = requests.post(webhook_url, json=data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Webhook sent to : " + webhook_name)

def monitor(collection, price):
    while True:
        try:
            response = requests.get("https://jmccmlyu33.medianetwork.cloud/nft_for_sale?collection=" + collection)
            for NFTS in response.json():
                if NFTS['price'] <= price:
                    if NFTS not in OLD_NFTS:
                        OLD_NFTS.append(NFTS)
                        for webhook in webhooks:
                            sendCode(NFTS['name'], str(NFTS['price']), NFTS['link_img'], "https://solanart.io/search/?token=" + NFTS['token_add'], webhook['name'], webhook['url'], collection)
                        delete_nft_thread = threading.Thread(target=delete_nft, args=(NFTS,))
                        delete_nft_thread.start()
        except:
            print("Error detected !")

def main():
    for collection in collections:
        print("Monitoring : " + collection['collection'] + " <= " + str(collection['price']) + " sol")
        monitor_thread = threading.Thread(target=monitor, args=(collection['collection'],collection['price'],))
        monitor_thread.start()

main()
