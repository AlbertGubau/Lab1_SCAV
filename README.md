# Lab1_SCAV
This is a GitHub repository that has been created to upload the results of SCAV Lab 1.

## Task 1 (rgb_yuv.py)
This script is able to change from RGB to YUV color values and vice-versa by applying a simple interactive menu and allowing the users to convert the value that they want.

## Task 2 (Rescaling an image)
This task can be found in the Task 2 folder of this repository. In this task, we can clearly see that we have an input image (spidey) and we have an output image that is re-scaled by using ffmpeg. The command line that we used to do so is the following one:
```
ffmpeg -i input_unscaled.png -vf scale=320:240 output_320x240_rescaled.png
```
With this, we obtain the results present in the Task 2 folder in which we get the re-scaled image and the compression that we get.

## Task 3 (Converting an image to B&W)
In this task we used the same image as in the previous task and we converted the image to Black & White by applying the following command line:
```
ffmpeg -i input_colored.png -vf hue=s=0 output_bw.png
```
With this, we are setting the hue and saturation values to 0 of the image, which allows us to get the desired result. Also, by using this command line, we can see that the output is compressed to (more comments in the task folder of the repository).

## Task 4 (Run-length encoding)
In this task we applied an algorithm which is capable of applying the run-length encoding procedure for a series of numbers. You can check the implementation in the file run_length_encoder.py in this repository.

## Task 5 (DCT Transform)
In this task, we tried to apply the DCT algorithm in a way that it is similar to the one that we saw in theory lectures. In the code we intend to explain the algorithm taking into account the theory lecture formulation and translating the correspondances. You can check the algorithm in the file dct_converter.py
