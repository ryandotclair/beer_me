## Purpose

Simple flask webapp that look for a GET on /api/beer and returns a json request of:

```
{
  "Cost": "Free",
  "Temp": "Cold",
  "Brand": "Who Cares?"
}
```

## Setup

If this is on a Photon OS, just run the `run.sh` script. Otherwise, you'll need the following installed:

+ python3
+ Flask module (ex: `pip3 install flask`)
