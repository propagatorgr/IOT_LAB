from twython import Twython # Εισάγουμε την βιβλιοθήκη για επικοινωνία με το Twitter API
from auth import ( # Εισάγουμε τα στοιχεία μας ως μεταβλητές της Python.
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython( # Δηλώνουμε τα στοιχεία μας στο twitterAPI
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
message = "Hello world!" # Αποθήκευσε το μήνυμα στη μεταβλητή message
twitter.update_status(status=message) # Εκπομπή του μηνύματος στο Twitter
print("Tweeted: %s" % message) # Τύπωσε το μήνυμα στην οθόνη.
