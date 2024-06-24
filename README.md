# Image Processing Using OpenCV

This repository contains Python scripts for various image processing tasks using OpenCV, including object detection and basic image manipulation.

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


