# Image Processing Using OpenCV

This repository contains Python scripts for various image processing **projects** using OpenCV, showcasing my experience during an internship focused on image processing.

## Detailed Contents

- **Basic Image Manipulation and Annotation:**
  This section includes scripts for fundamental image operations such as resizing, cropping, and adding annotations like rectangles and text to images. These scripts serve as foundational tools for preprocessing and visual enhancement of images.

- **Brightest Spot Detection:**
  Includes a script to automatically detect the brightest spot in an image. This is useful for applications where identifying the most intense light source or area of interest is critical, such as in microscopy or astronomy.

- **Counting Objects:**
  Provides scripts for automatically counting objects in an image. This can be applied to various scenarios, including industrial quality control, inventory management, and medical image analysis.

- **Face Detection:**
  Contains scripts for detecting human faces in images using pre-trained deep learning models. This functionality is crucial for applications in security, surveillance, and facial recognition systems.

- **Object Detection:**
  Scripts for object detection using pre-trained Caffe models. This section includes tools for detecting and localizing multiple objects within an image, enhancing capabilities in automated image analysis and classification tasks.

- **Realtime Face Detection:**
  Offers scripts for real-time face detection from live video streams. This feature is essential for applications requiring continuous monitoring and analysis of video feeds, such as in video surveillance and interactive systems.

- **Realtime Video Detection:**
  Provides scripts for real-time object detection in video streams. This includes applications in video analytics, autonomous systems, and real-time monitoring where rapid detection and response are critical.

## Installation

To run the scripts in this repository, ensure you have Python and OpenCV installed on your system.

### Installing Python Dependencies

Install the required Python packages using pip:

```bash
pip install opencv-python
pip install imutils
```

## Cloning or Forking the Repository

You can clone or fork this repository to your local machine to get started. Here are the instructions:

### Cloning the Repository

To clone the repository to your local machine, open a terminal or command prompt and run:

```bash
git clone https://github.com/nawi-n/Image-processing-using-openCV.git
```

### Forking the Repository

To fork the repository on GitHub:

1. Navigate to the repository's GitHub page: [Image-processing-using-openCV](https://github.com/nawi-n/Image-processing-using-openCV.git).
2. Click on the **Fork** button in the top right corner of the page.
3. After forking, you can clone your forked repository using the command above.

## Scripts

### General Usage

Replace placeholders (`<image_path>`, `<prototxt_path>`, `<caffemodel_path>`, `<confidence_threshold>`) with actual values.

#### Example 1: Drawing Rectangle

```bash
python drawing_rectangle.py --image <image_path>
```

This script demonstrates basic image manipulation by drawing a rectangle on an image.

#### Example 2: Object Detection

```bash
python object_detection.py --prototxt <prototxt_path> --model <caffemodel_path> --confidence <confidence_threshold>
```

This script performs object detection using a pre-trained Caffe model and displays the detected objects with bounding boxes and labels.

Adjust the script arguments according to your specific requirements.

## Notes

- Ensure Python 3.x is used for compatibility with all features.
- The necessary Caffe models (`*.caffemodel`) and prototxt files (`*.prototxt`) are already included in this repository.
- Adjust file paths and script arguments (`--image`, `--prototxt`, `--model`, `--confidence`) based on your setup.
- Customize scripts and add additional functionalities as needed.


