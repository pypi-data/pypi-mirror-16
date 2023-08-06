# SkyFish Python SDK

Official Skyfish Python SDK for merchant inventory integrations.

Skyfish requires inventory sync for merchants to be able to use it effectively in the chat window. This SDK wraps the required endpoints, making it easier for merchant's tech team to implement it. All you have to do is attach it to your inventory's Create-Read-Update-Delete Handler.

## Setup

``` easy_install skyfish-py ```

or

``` pip install skyfish-py ```

## Usage

### Initialization
To start using you will need the following components when you initialize the SDK:

* `email` : This is the merchant email you use during registration.
* `passport_id` : This is the passport_id you receive this after registering
* `password` : This is the passport you use during registration.
* `request_module` : This is the dependency that you need to inject. For this use case we tend to use [requests](http://docs.python-requests.org/en/master/) but you can use whatever library you think is best as long as it follows the same abstraction.
* `is_production`: This is the marker of environment being used. If in production, set this to be True, this parameter is optional

to start using initialize the SDK using the above parameters:

```
"""
This example uses the requests module as http request library
"""
import requests
from skyfish import SkyFishSDK


sky = SkyFishSDK(
                email='somerandomemail@somerandomemail.com',
                passport_id='somepassportid',
                password='somepassword',
                request_module=requests)
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
### Create a Product

To create a product, all you need to do is:
```
product_info = dict() # use the json structure above for this
sky.create_product(
            sku='1234', 
            product_details=product_info)
```
### Update a Product

To update a product, all you need to do is:
```
product_info = dict() # use the json structure above for this
sky.update_product(
            sku='1234', 
            product_details=product_info)
```

### Get a Product

To get detailed info from a product, all you need to do is:
```
sky.get_product(sku='1234')
```
### Delete a Product

To delete a product, all you need to do is:
```
sky.delete_product(sku='1234')
```

