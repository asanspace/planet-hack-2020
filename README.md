# Cloud Sonification
[Moheeb Zara](http://twitter.com/virgilvox), [Alex Glow](http://twitter.com/glowascii), Tanya Harrison, Melissa Lamoreaux

## The project
Moheeb used Python with the Planet API to grab cloud-cover data from images of a particular area (Egypt) in a particular slice of time.

Alex made a Sonic Pi patch that takes in values 0-15 and turns them into a pretty-sounding arpeggio, cycling through a selectable chord progression, so that they sound musical but retain the cloud cover information (higher pitch = higher cloud cover in the photo).

Moheeb mashed them both together, so we can listen to the clouds!

It would be cool to create a version that selects a single area of interest and cycles forward/backward through time, producing music as it goes. :)