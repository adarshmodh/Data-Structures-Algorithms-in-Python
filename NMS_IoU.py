import numpy as np

def iou(box1, box2):
    """Compute IoU between two boxes."""
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    
    inter_area = max(0, x2 - x1 + 1) * max(0, y2 - y1 + 1)
    box1_area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    box2_area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)
    
    union_area = box1_area + box2_area - inter_area
    
    return inter_area / union_area if union_area != 0 else 0

def non_max_suppression(boxes, scores, iou_threshold):
    """Perform Non-Maximum Suppression (NMS)."""
    indices = np.argsort(scores)[::-1]  # sort by scores descending
    keep = []

    while len(indices) > 0:
        current = indices[0]
        keep.append(current)
        remaining = []

        for idx in indices[1:]:
            if iou(boxes[current], boxes[idx]) < iou_threshold:
                remaining.append(idx)
        
        indices = remaining

    return keep

boxes = [
    [100, 100, 210, 210],
    [105, 105, 215, 215],
    [300, 300, 400, 400]
]
scores = [0.9, 0.85, 0.7]
iou_threshold = 0.5

kept_indices = non_max_suppression(boxes, scores, iou_threshold)
print("Kept boxes:", [boxes[i] for i in kept_indices])
