#!/usr/bin/env bash
cd ../
rasa data split nlu -u data/data.md --out data --training-fraction=0.8