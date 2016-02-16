# box-token-generator

This is a simple utility to get an enterprise token for your Box application. You'll first need to create an application from the [Box Developers website](https://developers.box.com). Once created, you can populate the client id, client secret, and enterprise id. You'll also have to generate a public/private keypair and store the public key in your app (then grab the jwt key id) and the private key with the executable (I called mine private_key.pem). That's all a bit painful the first time, but the good news is that you can just plug the values into this script and be good to go.

Now you can run the code as:

```
python auth.py
```

I'll add some more utilities to this as I go, but this is already pretty helpful for getting an enterprise token that you can use with Postman.

Fun fact: if you see the error 

```
Message: {"error":"invalid_grant","error_description":"Please check the 'exp' claim."} 
```

...this could be caused by your system time being out of sync. On my Mac, even though I had the time set to automatically update, it had become almost a minute out of sync. The Box servers give you a few seconds of leeway, but if they're not closed to sync'd up, your request will fail. Solution was easy to detect (my system time was off from actual), and easy to fix (turned automatic time update off then on again). But I'll never get the thirty minutes spent trying to figure this out back, so hopefully Google will cache this for others to learn from!





