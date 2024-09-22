#!/usr/bin/bash

tail -n 1000 ~/nohup.out | grep -m 1 "update_slots" | sed 's/.*代词。\\nassistant\\n//;s/\\nuser.*//' | sed 's/\\n/\n/g'