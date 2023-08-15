# geo-distance-api
Geospatial distance API in Python with FastAPI


## Inspired by 
- [Distance Between Two Geo-Locations in Python - AskPython](https://www.askpython.com/python/examples/find-distance-between-two-geo-locations)
- [Calculate distance between latitude longitude pairs with Python](https://gist.github.com/rochacbruno/2883505)


## Getting started
```
python3 -m venv venv
source venv/bin/activate
pip install fastapi[all]
```

## Run locally
```
uvicorn app.main:app --reload
```

## Swagger / openapi.json

http://127.0.0.1:8000/docs


## Local build and run

Build container image
```
buildah build -t geo-distance:latest
```

Run:
```
podman run -it -p 8080:8080 geo-distance:latest
```

## Build container image with OpenShift Pipelines

### Create project/namespace
```
oc new-project geo-distance-api
```

### Deploy pipeline and start pipeline
```
oc apply -f manifests/geo-distance-pipeline.yaml
oc create -f manifests/geo-distance-pipeline-run.yaml
```

### Start the API Service
```
oc apply -f manifests/geo-distance-deployment.yaml
```
