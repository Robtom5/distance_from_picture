# distance_from_picture
A small python module for determining the location of objects within static images based on characterstics of the object and the camera.

## Task list
 - [x] Initial distance finder for objects displacement away from the camera lense.
 - [ ] Include x and y offset calculations to determine 3d relative location of objects
 - [ ] Documentation
 - [ ] \(Optional) pep8 everything

## Example Use
```Python
import distancefrompicture

# Define an image that is 1000x1000px and has a field of view of 90 degrees in either direction
cam = distancefrompicture.CameraProperties((90,90), (1000,1000)) 
# Create a target that is 2m wide
targ = distancefrompicture.TargetProperties('test', 2)
# create the finder for this object
finder = distancefrompicture.DistanceFinder(cam, targ)

# Print some examples results
print(finder.find_distance((0,250), (00,-250))) # 1m away
print(finder.find_distance((0,500), (00,-500))) # 2m away

```
