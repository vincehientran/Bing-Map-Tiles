# Bing-Map-Tiles  
Vincent Tran  
  
Project explanation can be found in the [presentation](docs/Aerial_Satellite%20Imagery%20Retrieval.pdf).

## Language  
Python 3.7.5

## Libraries  
```
$ pip install numpy  
$ pip install opencv-python  
$ pip install urllib.request  
```

## Execution  
Run the command in the "src" directory
```
$ python MainRunner.py lat1 lon1 lat2 lon2
```
lat1/lon1 are the lat/long of the top left corner of the bounding box  
lat2/lon2 are the lat/long of the bottom right corner of the bounding box  

## Output  
output.jpg