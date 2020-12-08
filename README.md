# Python-based Evaluation Tool for Dense Captioning

This repository provides the python-based evaluation tool for dense captioning.

Codes are based on [PythonAPI of COCO evaluation tool [1]](https://github.com/cocodataset/cocoapi/tree/master/PythonAPI).

## Description

Dense captioning is the task that localizes and describes the visual contents of an image simultaneously [2].

To evaluate the performance of a dense captioning model, this tool calculates the mean Average Precision (mAP) score using IoU and METEOR metrics as thresholds.

## Requirements

- Java
- Python

## Installation

```
pip install .
```

## Examples

```python
from densecapeval.coco import COCO
from densecapeval.cocoeval import COCOeval

gt_path = "PATH/TO/GT.json"  # path of ground truch (.json)
dt_path = "PATH/TO/PRED.json"  # path of prediction result (.json)

coco_gt = COCO(gt_path)
coco_dt = coco_gt.loadRes(dt_path)
coco_eval = COCOeval(cocoGt=coco_gt, cocoDt=coco_dt)

coco_eval.evaluate()  # compute IoU score and METEOR score of each pair of bbox and caption per image
coco_eval.accumulate()  # accumulate per image evaluation
coco_eval.summarize()  # display summary of results
```

After `.summarize()`, the result is shown on the display.

```
Average Precision  (AP) @[ IoU=0.30:0.70 | METEOR=0.00:0.25 | area=   all | maxDets=100 ] = 0.800
Average Precision  (AP) @[ IoU=0.50      | METEOR=0.10      | area=   all | maxDets=100 ] = 1.000
Average Precision  (AP) @[ IoU=0.75      | METEOR=0.25      | area=   all | maxDets=100 ] = -1.000
Average Precision  (AP) @[ IoU=0.30:0.70 | METEOR=0.00:0.25 | area= small | maxDets=100 ] = -1.000
Average Precision  (AP) @[ IoU=0.30:0.70 | METEOR=0.00:0.25 | area=medium | maxDets=100 ] = 0.800
Average Precision  (AP) @[ IoU=0.30:0.70 | METEOR=0.00:0.25 | area= large | maxDets=100 ] = -1.000
Average Recall     (AR) @[ IoU=0.30:0.70 | METEOR=0.00:0.25 | area=   all | maxDets=  1 ] = 0.800
Average Recall     (AR) @[ IoU=0.30:0.70 | METEOR=0.00:0.25 | area=   all | maxDets= 10 ] = 0.800
Average Recall     (AR) @[ IoU=0.30:0.70 | METEOR=0.00:0.25 | area=   all | maxDets=100 ] = 0.800
Average Recall     (AR) @[ IoU=0.30:0.70 | METEOR=0.00:0.25 | area= small | maxDets=100 ] = -1.000
Average Recall     (AR) @[ IoU=0.30:0.70 | METEOR=0.00:0.25 | area=medium | maxDets=100 ] = 0.800
Average Recall     (AR) @[ IoU=0.30:0.70 | METEOR=0.00:0.25 | area= large | maxDets=100 ] = -1.000
```

## Data Format

### GT Format

```
{
    "annotations": [
        {
            "id": int,              # id of each object
            "image_id": int,        # id of each image
            "category_id": int,     # id of each category
            "area": float,          # area of each bbox
            "bbox": [x1, y2, w, h], # coordinates of each bbox
            "caption": [str],       # list of captions
            "iscrowd": 0 or 1       # if the bbox surrounds multiple objects, iscrowd = 1
        }
    ],

    "images": [
        {
            "id": int,              # id of each image
            "width": int,           # width of each image
            "height": int,          # height of each image
            "file_name": str,       # file name of each image
        }
    ],

    "categories": [
        {
            "id": int,              # id of each category
            "name": str,            # name of each category
        }
    ]
}
```


### Results Format

```
[
    {
        "image_id": int,        # id of each image
        "category_id": int,     # category is of bbox
        "bbox": [x1, y1, w, h], # coordinates of detected bbox
        "score": float,         # confidence score of bbox
        "caption": str          # predicted caption
    }
    ...
]
```


## Citation

```
@misc{densecapeval,
  author = {Kento Doi},
  title = {Python-based Evaluation Tool for Dense Captioning},
  year = {2020},
  howpublished = {\url{https://github.com/doiken23/densecapeval}}
}
```


## References

1. Piotr Dollar and Tsung-Yin Lin. COCO API. https://github.com/cocodataset/cocoapi

2. J. Johnson et al. DenseCap: Fully Convolutional Localization Networks for Dense Captioning. CVPR, 2016.
