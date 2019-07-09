#!/bin/bash

source bin/activate
cd linkcollect/linkcollect/spiders
scrapy crawl link --nolog
cd ../../../
python3  HttpStatusCode.py
