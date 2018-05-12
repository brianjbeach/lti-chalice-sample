$ pip install chalice

$ chalice new-project lti-chalice-sample && cd lti-chalice-sample


In a real world application we could simply add pylti to requirements.txt.
However, in this case, the latest code that supports Chalice is not in the 
repo yet. Therefore, I am installing it localy. 

```
$ pip install pylti -t ./vendor/
```

Now, I am going to everwrite pylti with my latest changes. 

```
$ cp -R ~/pylti/pylti/ ./vendor/ 
```

Next, I open the autogenerated app.py and add the LTI decorator. I also change 
the method and content type tp the @app.route. My code looks like this.

```
from chalice import Chalice
from pylti.chalice import lti

app = Chalice(app_name='lti-chalice-sample')
app.debug = True 

@app.route('/', methods=['POST'], content_types=['application/x-www-form-urlencoded'])
@lti(request='initial', app=app)
def index(lti=lti):
    return {'hello': 'world'}
```

The last thing you need to do is add your key and secret. Secrets are stored 
as environment variables in Lambda. You can add an environement to 
.chalice/config.json. The key should be prefixed with CONSUMER_KEY_SECRET_. 
For example. 

```
{
  "stages": {
    "dev": {
      "api_gateway_stage": "api"
    }
  },
  "environment_variables": {
    "CONSUMER_KEY_SECRET___consumer_key__": "__lti_secret__"
  },
  "version": "2.0",
  "app_name": "lti-chalice-sample"
}
```

Now you can deploy your function to lambda.

```
$ chalice deploy
```

This will return the **Rest API URL** which you will need to enter into your 
LMS. For example in lambda it looks like this.

