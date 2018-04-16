# pyCoinHive
- pyCoinHive is a python3 implementation of the PHP CoinHive API class

### Usage GET

```python
coinhive = CoinHiveAPI("YOUR_SECRET_KEY")
stats = coinhive.get("/stats/site")
print(stats.get("history"))
```

### Usage POST

```python
coinhive = CoinHiveAPI("YOUR_SECRET_KEY")
request = coinhive.post("/link/create", {'url': 'http://google.com/', 'hashes': 1024})
print(request)
```

### Donations
[![Paypal donations](http://noororphansfund.org/wp-content/uploads/2014/06/paypalicon.png "Paypal donations")](https://www.paypal.me/xafnir "Paypal donations")
