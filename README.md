# Timing filestore.Client()
Simple repo to time the firestore.Client() call to determine if authentication happens each call


Requirements:
Your current GCP project has firestore database enabled in Native mode. Activate your project like so:
```
gcloud config set project <PROJECT>
```

Reproducing these results:
```
python3 -m venv testfirestore
source testfirestore/bin/activate
git clone https://github.com/pbrumblay/testfirestore
cd testfirestore
python load.py
python test.py
```

Example output:
```
python test.py
Reusing the client and collection reference took 4.373771083 seconds
Reusing the client but not the collection refrerence took 3.8674949749999996 seconds
Resetting the client took 184.230437095 seconds
```

Conclusions
1. Calling firestore.Client() forces reauthentication which is slow.
1. Caching the collection reference does not impact performance.
