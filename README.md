# Solanart - Monitor

## Installation :

    pip install -r requirements.txt

## Configuration :

**Edit : _config.json_**

Exemple :

```
{
    "collections": [
        {
            "collection": "<collection>",
            "price": 1,
            "webhooks": [
                {
                    "name": "<name>",
                    "url": "<url>",
                    "footer_name": "<footer_name>",
                    "footer_image_url": "<footer_image_url>"
                },
                {
                    "name": "<name>",
                    "url": "<url>",
                    "footer_name": "<footer_name>",
                    "footer_image_url": "<footer_image_url>"
                }
            ]
        },
        {
            "collection": "<collection>",
            "price": 1,
            "webhooks": [
                {
                    "name": "<name>",
                    "url": "<url>",
                    "footer_name": "<footer_name>",
                    "footer_image_url": "<footer_image_url>"
                },
                {
                    "name": "<name>",
                    "url": "<url>",
                    "footer_name": "<footer_name>",
                    "footer_image_url": "<footer_image_url>"
                }
            ]
        }
    ],
    "avatar_url": "https://pbs.twimg.com/profile_images/1434909426838814727/b1R0dmnf.jpg"
}
```

You can find collection name at the end of : https://solanart.io/collections/solsnatchers

#### Warning !

At the end of the last "}" or "]" do not put a ","

Exemple :

```
{
    "collections": [
        {
            "collection": "<collection>",
            "price": 1,
            "webhooks": [
                {
                    "name": "<name>",
                    "url": "<url>",
                    "footer_name": "<footer_name>",
                    "footer_image_url": "<footer_image_url>"
                } !!!
            ]
        } !!!
    ],
    "avatar_url": "https://pbs.twimg.com/profile_images/1434909426838814727/b1R0dmnf.jpg"
}
```

## Execution :

    python solanart.py
