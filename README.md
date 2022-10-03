# rozvrh-bojiste

### open REST-api returning JSON file of the classes in day

- use `https://rozvrh-bojiste.herokuapp.com/get_schedule/<class>`

### data format
```
[
  {
    "bottom": [
      { "hodina": 0, "pauza": true },
      {
        "hodina": 1,
        "pauza": false,
        "predmet": "<class>",
        "ucebna": "<classroom>",
        "ucitel": "<teacher>"
      },
      ...
    ]
    "top": [
      {
        "hodina": 0,
        "pauza": false,
        "predmet": "<class>",
        "ucebna": "<classroom>",
        "ucitel": "<teacher>"
      },
      {
        "hodina": 0,
        "pauza": false,
        "predmet": "<class>",
        "ucebna": "<classroom>",
        "ucitel": "<teacher>"
      },
      ....
    ]
  },
  ...
] 
(top - main classes
 bottom - changed schedule / split-class hours)
```

*build in flask, deployed on heroku free dyno (might change after [November 28th, 2022](https://blog.heroku.com/next-chapter))*


