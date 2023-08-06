# SkyFish Python SDK

Official Skyfish Python SDK for merchant inventory integrations.

Skyfish requires inventory sync for merchants to be able to use it effectively in the chat window. This SDK wraps the required endpoints, making it easier for merchant's tech team to implement it. All you have to do is attach it to your inventory's Create-Read-Update-Delete Handler.

The use of the SDK requires the token that is granted during the login process. To learn more on how to login please refer to the [authorization documentation](http://docs.skyfish.id/authorization/)

## Setup

``` easy_install skyfish-py ```

or

``` pip install skyfish-py ```

## Usage

### Initialization
To start using you will need the following components when you initialize the SDK:

* `email` : This is the merchant email you use during registration.
* `passport_id` : This is the passport_id you receive after registering
* `token` : This is the token you receive from the login process.
* `client_key`: This is the client_key you receive after registering.
* `base_url`: This is the backend url that you will connect to.


You need to put this inside a dictionary and then create a `skyfish.models.Config` object with it.

```
from skyfish.models import Config

config_dictionary = dict(
    email='somerandomemail@somerandomemail.com',
    passport_id='somepassportid',
    token='ZU9YYUxsQUQ1RWpjd1RYdk9HSTFaVFJsTkdFdFl6SXdZUzAwWW1ZeExXSmhNRE10TlRkbVltUmxNak0zWTJNdzUyNTZ5NWxlcGt0NTQ1Zm8=',
    client_key='aalkdalkdnalkdnlakndlakdnlakdnlakndlakndlkanldkanldknakla',
    base_url='https://product-sandbox.skyfish.id'
)

config = Config(config_dictionary)
```

to start using initialize the SDK using the above parameters:

```
"""
This example uses the requests module as http request library
"""
import requests
from skyfish import SkyFishSDK
from skyfish.models import Config

config_dictionary = dict(
    email='somerandomemail@somerandomemail.com',
    passport_id='somepassportid',
    token='ZU9YYUxsQUQ1RWpjd1RYdk9HSTFaVFJsTkdFdFl6SXdZUzAwWW1ZeExXSmhNRE10TlRkbVltUmxNak0zWTJNdzUyNTZ5NWxlcGt0NTQ1Zm8=',
    client_key='aalkdalkdnalkdnlakndlakdnlakdnlakndlakndlkanldkanldknakla',
    base_url='https://product-sandbox.skyfish.id'
)

config = Config(config_dictionary)

sky = SkyFishSDK(configuration=config)
```

That's it and you're set to start integrating.

## Product Management

The product management uses the following standard JSON for Creation and update
```
{
  "name": "Lorem ipsum dolor sit amet", // Name of the product
  "limitless": true, // Set to true if you have a limit on inventory
  "price": 34500, // This is the price of the product
  "quantity": 5000, // This is the quantity of the product, will be ignored if limitless is true
  "need_address": true, // Set to false for virtual goods
  "image_url": [
    "https://blabla.com/gambar1.png",
    "https://blabla.com/gambar2.png"
  ], // This is quite self explanatory
  "description": "Lorem ipsum dolor sit amet", // This is the description of the product
  "environment_type": "DEVELOPMENT", // This is the environment the product is being submitted
  "weight": 600, // This is the weight of the product for shipping purposes
  "insurance_type": "NEEDED", // This is to determine whether shipping insurance is available
  "payment_types": [
    "BANK_TRANSFER",
    "CREDIT_CARD"
  ], // This is to determine available payment methods
  "sku": "testing sku", // This is the SKU from the merchant side
  "discount": { // This is the discount given
    "discount_type": "NOMINAL", // This is the type, NOMINAL and PERCENTAGE
    "amount": 1000
  },
  "product_variant": { // This is to set the available product variant
    "custom_message": [
      {
        "title": "sda",
        "validation_type": "STRING",
        "mandatory": true
      }
    ],
    "variant": [
      {
        "option_value": [
          "123",
          "123"
        ],
        "image_url": [
          "https://res.cloudinary.com/dvndkaqtk/image/upload/v1449201799/tf1zwevmcjwtjrrywoqa.png"
        ],
        "price": 0,
        "quantity": 0,
        "description": "123"
      },
      {
        "option_value": [
          "1234",
          "123"
        ],
        "image_url": [
          "https://res.cloudinary.com/dvndkaqtk/image/upload/v1449201807/osqtept9an4clrpnpcko.png"
        ],
        "price": 0,
        "quantity": 0,
        "description": "123"
      }
    ],
    "variant_parameter": [
      {
        "option_name": "asda",
        "option_value": [
          "123",
          "1234"
        ]
      },
      {
        "option_name": "123",
        "option_value": [
          "123"
        ]
      }
    ]
  }
}
```

To handle this and ensure that you have a valid model, we provide the `skyfish.models.ProductData` model.

Simply create your product in a dictionary and you can build the object that will be passed.

```
product = ProductData(product_dictionary)

# You access the parameters afterwards

print product.name # should print out Lorem ipsum dolor sit amet based on the structure above
```


### The response object

Skyfish provides a `skyfish.models.Response` model. This standardises the response received.

There are 4 main properties in a response object:

- `status_code`: This is the HTTP Status code of the response. You can leverage this to standardize error handling.
- `status`: This is the status given by the system.
- `message`: This is the message provided by the system.
- `data`: This is the data provided by skyfish. Expect 2 types of data types, `dict` and `ProductData`. `dict` is returned on error and success on `DELETE`actions. `ProductData` is returned for success on `GET`, `POST` and `PUT` actions.

### Create a Product

To create a product, all you need to do is:
```
product_info = dict() # use the json structure above for this
product = sky.create_product(
            sku='1234', 
            product_details=product_info)
```

Success and failed request will return a standard `skyfish.models.Response` object

```
product.status_code
product.status
product.message
product.data
```

The difference lies in the `data` where a success will return `skyfish.models.ProductData` and failure will return `dict`

### Update a Product

To update a product, all you need to do is:
```
product_info = dict() # use the json structure above for this
product = sky.update_product(
            sku='1234', 
            product_details=product_info)
```

Success and failed request will return a standard `skyfish.models.Response` object

```
product.status_code
product.status
product.message
product.data
```

The difference lies in the `data` where a success will return `skyfish.models.ProductData` and failure will return `dict`

### Get a Product

To get detailed info from a product, all you need to do is:
```
product = sky.get_product(sku='1234')
```

Success and failed request will return a standard `skyfish.models.Response` object

```
product.status_code
product.status
product.message
product.data
```

The difference lies in the `data` where a success will return `skyfish.models.ProductData` and failure will return `dict`

### Delete a Product

To delete a product, all you need to do is:
```
product = sky.delete_product(sku='1234')
```

Success and failed request will return a standard `skyfish.models.Response` object

```
product.status_code
product.status
product.message
product.data
```


