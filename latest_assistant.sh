#!/usr/bin/bash

tail -n 1000 ~/nohup.out | grep -m 1 "request:  {\"model\":" #| sed 's/.*代词。\\nassistant\\n//;s/\\nuser.*//' | sed 's/\\n/\n/g'
