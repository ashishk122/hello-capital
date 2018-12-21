#! /bin/sh

exec gunicorn main:APP -c run_conf.py
