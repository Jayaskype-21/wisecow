#!/bin/bash
STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:4499)
echo "Application Status: $STATUS_CODE"
