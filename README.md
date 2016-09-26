## Purpose

Simple flask webapp, designed to run on Cloud Foundry, that allows GET'ing beer.

Just GET <ip_of_webapp>/api/beer and you'll get a json of free beer:

```
{
  "Cost": "Free",
  "Temp": "Cold",
  "Brand": "Who Cares?",
  "Instance": instance
}
```

## Requirements

Cloud Foundry is required for this to run. You can get the "laptop" version of it here: https://github.com/pivotal-cf/pcfdev

## Running Beer Me

Run the following command while in the main directory of beer_me:

`cf push beerme`

## Configuring

The manifest file provides configuration specific data for Cloud Foundry. By default we're having CF run two instances of this application.

You can either change the manifest.yml file before you deploy, or you can simple change the number of instances using this command:

`cf scale beerme -i X` where `X` is the number of total instances you want running on Cloud Foundry.

## Consuming Beer

After the python app is uploaded and running on Cloud Foundry (default of 2 instances runs), there should be a url provided. If you're running the laptop version and used the same name as I'd used (`beerme`), then you should be able to consume beer using this command:

`curl beerme.local.pcfdev.io/api/beer`

