from flask import Flask
import redis
import time

#Presume a Flask app accepts http requests ie its a web app
#
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379) #default Redis port


#Good explanation of this resilience pattern at
#https://docs.docker.com/compose/gettingstarted/ 
def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

# So route tells Flask to run hello if the given path is requested
#
@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)