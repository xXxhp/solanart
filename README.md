# Solanart - Monitor

## Installation :

    pip install -r requirements.txt

## Configuration  :

**Edit : *config.json***

Exemple :
```
    "collections": [
        {
            "collection": "solsnatchers",
            "price": 2
        },
        {
            "collection": "degenape",
            "price": 45
        }
    ],  
    "webhooks": [
        {
            "name": "<name>",
            "url": "<url>"
        },
        {
            "name": "<name>",
            "url": "<url>"
        }
    ],
    "avatar_url": "https://pbs.twimg.com/profile_images/1434909426838814727/b1R0dmnf.jpg",
    "footer_name": "<footer_name>",
    "footer_image_url": "<footer_image_url>"
```

You can find collection name at the end of : https://solanart.io/collections/solsnatchers

#### Warning !

At the end of the last "}" do not put a "," !

Exemple :

```    
    "collections": [
        {
            "collection": "solsnatchers",
            "price": 1.99
        }
    ],  
```

```    
    "webhooks": [
        {
            "name": "<name>",
            "url": "<url>"
        },
        {
            "name": "<name>",
            "url": "<url>"
        }
    ],
```

## Execution :

    python solanart.py




