#!/usr/bin/env bash

gunicorn app:app -c "$PWD"/gunicorn.config.py
