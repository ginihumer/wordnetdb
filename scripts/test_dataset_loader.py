import csv
import json
import os

import datasets


# TODO: Add BibTeX citation
# Find for instance the citation on arxiv or on the dataset repo/website
_CITATION = """\
@InProceedings{huggingface:dataset,
title = {A great new dataset},
author={huggingface, Inc.
},
year={2020}
}
"""

# TODO: Add description of the dataset here
# You can copy an official description
_DESCRIPTION = """\
This new dataset is designed to solve this great NLP task and is crafted with a lot of care.
"""

# TODO: Add a link to an official homepage for the dataset here
_HOMEPAGE = ""

# TODO: Add the licence for the dataset here if you can find it
_LICENSE = ""

# TODO: Add link to the official dataset URLs here
# The HuggingFace Datasets library doesn't host the datasets but only points to the original files.
# This can be an arbitrary nested dict/list of URLs (see below in `_split_generators` method)
_URLS = {
    "first_domain": "https://huggingface.co/great-new-dataset-first_domain.zip",
    "second_domain": "https://huggingface.co/great-new-dataset-second_domain.zip",
}

_NAMES = []
                   
                    
class Food101Config(datasets.BuilderConfig):
    """Builder Config for Food-101"""

    def __init__(self, data_url, metadata_urls, **kwargs):
        """BuilderConfig for Food-101.
        Args:
          data_url: `string`, url to download the zip file from.
          metadata_urls: dictionary with keys 'train' and 'validation' containing the archive metadata URLs
          **kwargs: keyword arguments forwarded to super.
        """
        super(Food101Config, self).__init__(version=datasets.Version("1.0.0"), **kwargs)
        self.data_url = data_url
        self.metadata_urls = metadata_urls

class Food101(datasets.GeneratorBasedBuilder):
    """Food-101 Images dataset"""
    
    BUILDER_CONFIGS = [
        Food101Config(
            name="breakfast",
            description="Food types commonly eaten during breakfast.",
            data_url="https://link-to-breakfast-foods.zip",
            metadata_urls={
                "train": "https://link-to-breakfast-foods-train.txt", 
                "validation": "https://link-to-breakfast-foods-validation.txt"
            },
        )
    ]

    def _info(self):
        print("_info")
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "image": datasets.Image(),
                    "label": datasets.ClassLabel(names=_NAMES),
                }
            ),
            supervised_keys=("image", "label"),
            homepage=_HOMEPAGE,
            citation=_CITATION,
            license=_LICENSE,
            task_templates=[datasets.tasks.ImageClassification(image_column="image", label_column="label")],
        )

    def _split_generators(self, dl_manager):
        print("_split_generators")

    def _generate_examples(self, images, metadata_path):
        print("_generate_examples")
 