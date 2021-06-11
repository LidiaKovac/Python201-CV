# Lesson 1:

What is the difference between Computational photography and Computer vision? 
While there is some overlap, computational photography is about analyzing photograpies and light, and the analysis is made to made cameras "smarter". Computer vision is more about the interpratation of the the images. 

## What is computer vision? 
Every picture tells a story, right? CV interprests images and we are going to take vision out of it. 
Fundamentally CV is about understanding something that is the image. 
Images have become of maximum importance in our everyday life. The manipulation and the extraction of info from images is now substancial more many many industries, such as traffic control. 
OCR, face and blink detection, smile shutter, are examples of computer vision. In a related way you can recognize objects, art pieces and statues. Computer vision also helps with motion capture and cgi, 3d modeling, sports, robotics, games, security, medical imaging. 

## Images as functions
An image is nothing but a function of x and y (=> I(x,y)). The higher the value, the brighter the color. Computer vision compute something from a function like this, often by outputting another image. 
We can think of images as a function from R^2 to R. It's going to be defined over some bounds (the rectangle), and a finite range (0,255).  
<div style='text-align: center'> ![](https://imgur.com/HBht7sc.png) </div>
We can think of images as the results of three functions stacked together. This is represented as "vector valued" function. Every pixel of the image are categorized using x and y axis. Tha values of x and y can be any real number, so the function would be f(x,y) ∈ \mathbb{R}

