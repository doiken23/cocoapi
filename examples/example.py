#!/usr/bin/env python3

from densecapeval.coco import COCO
from densecapeval.cocoeval import COCOeval


def test_coco_eval():
    dt_path = 'tests/dt_data.json'
    gt_path = 'tests/gt_data.json'

    coco_gt = COCO(gt_path)
    coco_dt = coco_gt.loadRes(dt_path)

    coco_eval = COCOeval(cocoGt=coco_gt, cocoDt=coco_dt)

    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()


if __name__ == '__main__':
    test_coco_eval()
