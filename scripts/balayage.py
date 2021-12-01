import albumentations as A
from typing import List, Callable
import numpy as np
import torch
from skimage.io import imread
from copy import deepcopy


class Repr:
    """Evaluatable string representation of an object"""

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"


class AlbumentationWrapper(Repr):
    """
    A wrapper for the albumentation package.
    Bounding boxes are expected to be in xyxy format (pascal_voc).
    Bounding boxes cannot be larger than the spatial image's dimensions.
    Use Clip() if your bounding boxes are outside of the image, before using this wrapper.
    """

    def __init__(self, albumentation: Callable, format: str = "pascal_voc"):
        self.albumentation = albumentation
        self.format = format

    def __call__(self, inp: np.ndarray, tar: dict):
        # input, target
        transform = A.Compose(
            [self.albumentation],
            bbox_params=A.BboxParams(format=self.format, label_fields=["class_labels"]),
        )

        out_dict = transform(image=inp, bboxes=tar["boxes"], class_labels=tar["labels"])

        input_out = np.array(out_dict["image"])
        boxes = np.array(out_dict["bboxes"])
        labels = np.array(out_dict["class_labels"])

        tar["boxes"] = boxes
        tar["labels"] = labels

        return input_out, tar


def balayage_inference_single(image: np.ndarray, crop_size, shift):
    l = len(image)
    w = len(image[0])
    L = l // shift
    W = w // shift
    dic = {}
    size_w = (w - (W - 2) * shift, crop_size[1])
    size_l = (crop_size[0], l - (L - 2) * shift)
    for i in range(W - 2):
        for j in range(L - 2):
            dic[(i, j)] = crop_single(image, crop_size, i * shift, j * shift)['image']

    for i in range(W - 2):
        dic[(i, L - 2)] = crop_single(image, size_w, i * shift, (L - 2) * shift, )['image']

    for j in range(L - 2):
        dic[(W - 2, j)] = crop_single(image, size_l, (W - 2) * shift, j * shift)['image']

    dic[(W - 2, L - 2)] = crop_single(image, (size_w[0], size_l[1]), (W - 2) * shift, (L - 2) * shift)['image']

    return dic

class AlbumentationWrapper_bis(Repr):
    """
    A wrapper for the albumentation package.
    Bounding boxes are expected to be in xyxy format (pascal_voc).
    Bounding boxes cannot be larger than the spatial image's dimensions.
    Use Clip() if your bounding boxes are outside of the image, before using this wrapper.
    """

    def __init__(self, albumentation: Callable, format: str = "pascal_voc"):
        self.albumentation = albumentation
        self.format = format

    def __call__(self, inp: np.ndarray, tar: dict):
        # input, target
        transform = A.Compose(
            [self.albumentation],
            bbox_params=A.BboxParams(format=self.format, label_fields=["class_labels"]),
        )

        out_dict = transform(image=inp, bboxes=tar["boxes"], class_labels=tar["labels"])

        input_out = np.array(out_dict["image"])
        boxes = np.array(out_dict["bboxes"])
        labels = np.array(out_dict["class_labels"])
        tar_ = deepcopy(tar)
        tar_["boxes"] = boxes
        tar_["labels"] = labels

        return input_out, tar_

def balayage_inference_double(image: np.ndarray, target, crop_size, shift):
    l = len(image)
    w = len(image[0])
    L = l // shift
    W = w // shift
    dic = {}
    size_w = (w - (W - 2) * shift, crop_size[1])
    size_l = (crop_size[0], l - (L - 2) * shift)
    for i in range(W - 2):
        for j in range(L - 2):
            dic[(i, j)] = crop_double(image, target, crop_size, i * shift, j * shift)

    for i in range(W - 2):
        dic[(i, L - 2)] = crop_double(image, target, size_w, i * shift, (L - 2) * shift)

    for j in range(L - 2):
        dic[(W - 2, j)] = crop_double(image, target, size_l, (W - 2) * shift, j * shift)

    dic[(W - 2, L - 2)] = crop_double(image, target, (size_w[0], size_l[1]), (W - 2) * shift, (L - 2) * shift)

    return dic

def crop_single(image: np.ndarray, crop_size, x_min, y_min):
    return A.Crop(y_min=y_min, x_min=x_min, x_max=x_min + crop_size[0], y_max=y_min + crop_size[1], p=1)(image=image)


def crop_double(image: np.ndarray, target, crop_size, x_min, y_min):
    return AlbumentationWrapper_bis(A.Crop(x_min=x_min, y_min=y_min, x_max=x_min + crop_size[0], y_max=y_min + crop_size[1], p=1))(image, target)


def inference_on_balayage(dic, model, transforms):
    preds = {}
    preds['boxes'] = []
    preds['labels'] = []
    preds['scores'] = []

    model.eval()
    k = 0
    for key, value in dic.items():
        with torch.no_grad():
            x = transforms(value)
            x = torch.from_numpy(x).type(torch.float32)
            pred = model([x])[0]
            for i in range(len(pred['boxes'])):
                box = pred['boxes'][i].tolist()
                new_box = [box[0] + key[0] * 512, box[1] + key[1] * 512, box[2] + key[0] * 512, box[3] + key[1] * 512]
                preds['boxes'].append(new_box)
                preds['labels'].append(pred['labels'][i].tolist())
                preds['scores'].append(pred['scores'][i].tolist())
        k += 1
    return preds
