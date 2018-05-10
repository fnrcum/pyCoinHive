**pyCoinHive** 
   - pyCoinHive is a python3 implementation of the PHP CoinHive API class

**Usage GET**

`python coinhive = CoinHiveAPI("YOUR_SECRET_KEY") stats = coinhive.get("/stats/site") print(stats.get("history")) `

**Usage POST**

`python coinhive = CoinHiveAPI("YOUR_SECRET_KEY") request = coinhive.post("/link/create", {'url': 'http://google.com/', 'hashes': 1024}) print(request) `