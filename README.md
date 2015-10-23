# Uber Python StarterKit

Uber Hackathon Starter Kit for Python

The sample code makes calls to the [sandbox api](https://developer.uber.com/v1/sandbox/) endpoints at https://sandbox-api.uber.com/v1/

The sandbox url should be used for development.

The production api url is https://api.uber.com/v1/

## Requirements

- have an uber account
- create an app at https://developer.uber.com
- have python installed (tested with python 3.5.0 and 2.7.10)
- have pip installed
- use pip to install the [`requests`](http://docs.python-requests.org/) module
    - `pip install requests`
- clone this project, all commands are issued from inside this project directory

### Environment Variables

You should never commit your secret/private information to your scm.

Each script requires environment variables to be set in a file named `.env`

copy `.env-sample` to `.env` and follow the template to add your uber api keys

example

```
UBER_SERVER_TOKEN="YOUR-SECRET-KEY-HERE"
UBER_CLIENT_ID="YOUR-SECRET-KEY-HERE"
UBER_CLIENT_SECRET="YOUR-SECRET-KEY-HERE"
```

this information can be found from your uber developer console by editing an app that you have created. https://developer.uber.com/dashboard

scripts will be run by reading the `.env` file. the env variables are set during when running a script per _session_, that is, the environment variables will not persist.

this is done by running `env $(cat .env | xargs) ...your command`

if you do not have the `xargs` program (it is installed in osx and ubuntu linux by default), then you can install it for your operating system.

or, set each environment variable manually without `.env`

example

```
UBER_SERVER_TOKEN=your-uber-server-token \
UBER_CLIENT_ID=your-uber-client-id \
UBER_CLIENT_SECRET=your-cient-secret \
...your command
```

## Problems?

if you are seeing errors, make sure that there is a `.env` file located in the current directory which should be the project root, and that it is in the same format as `.env-sample` and that it has valid secret keys and tokens from the uber developer api.

## Simple requests

The Uber API has 3 routes that only require server side authentication, and do not require a user to authorize via OAuth2

```
GET /v1/products
GET /v1/estimates/time
GET /v1/estimates/price
```

### Products

**GET /v1/products**

https://developer.uber.com/v1/endpoints/#product-types

run the `simple_products.py` script

`env $(cat .env | xargs) python simple_products.py`

result _(truncated)_

```
{
  "products": [
    {
      "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberx.png",
      "product_id": "6e731b60-2994-4f68-b586-74c077573bbd",
      "display_name": "uberX",
      "description": "the low-cost uber",
      "capacity": 4,
      "price_details": {
        "cost_per_minute": 0.3,
        "currency_code": "USD",
        "distance_unit": "mile",
        "cancellation_fee": 5.0,
        "minimum": 4.05,
        "cost_per_distance": 1.4,
        "base": 2.15,
        "service_fees": [
          {
            "name": "Safe rides fee",
            "fee": 1.05
          }
        ]
      }
    },
    {
      "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberxl2.png",
      "product_id": "2d2af87b-b870-4286-a300-7e7a8a79cd8c",
      "display_name": "uberXL",
      "description": "low-cost rides for large groups",
      "capacity": 6,
      "price_details": {
        "cost_per_minute": 0.35,
        "currency_code": "USD",
        "distance_unit": "mile",
        "cancellation_fee": 5.0,
        "minimum": 7.05,
        "cost_per_distance": 2.8,
        "base": 3.85,
        "service_fees": [
          {
            "name": "Safe rides fee",
            "fee": 1.05
          }
        ]
      }
    },
...
```



### Price Estimate

**GET /v1/estimates/price**

https://developer.uber.com/v1/endpoints/#price-estimates

run the `simple_price_estimates.py` script

`env $(cat .env | xargs) python simple_price_estimates.py`

result _(truncated)_

```
{
  "prices": [
    {
      "estimate": "$11-15",
      "duration": 853,
      "currency_code": "USD",
      "product_id": "6e731b60-2994-4f68-b586-74c077573bbd",
      "surge_multiplier": 1.0,
      "display_name": "uberX",
      "high_estimate": 15,
      "localized_display_name": "uberX",
      "low_estimate": 11,
      "distance": 3.81,
      "minimum": 4
    },
    {
      "estimate": "$18-24",
      "duration": 853,
      "currency_code": "USD",
      "product_id": "2d2af87b-b870-4286-a300-7e7a8a79cd8c",
      "surge_multiplier": 1.0,
      "display_name": "uberXL",
      "high_estimate": 24,
      "localized_display_name": "uberXL",
      "low_estimate": 18,
      "distance": 3.81,
      "minimum": 7
    },
...
```



### Time Estimate

**GET /v1/estimates/time**

https://developer.uber.com/v1/endpoints/#time-estimates

run the `simple_time_estimates.py` script

`env $(cat .env | xargs) python simple_time_estimates.py`

result _(truncated)_

```
{
  "times": [
    {
      "display_name": "uberX",
      "localized_display_name": "uberX",
      "estimate": 501,
      "product_id": "6e731b60-2994-4f68-b586-74c077573bbd"
    },
    {
      "display_name": "uberXL",
      "localized_display_name": "uberXL",
      "estimate": 624,
      "product_id": "2d2af87b-b870-4286-a300-7e7a8a79cd8c"
    },
    {
      "display_name": "uberASSIST",
      "localized_display_name": "uberASSIST",
      "estimate": 501,
      "product_id": "11c96cc8-50ea-4e06-97cc-4646ae941669"
    },
...
```



