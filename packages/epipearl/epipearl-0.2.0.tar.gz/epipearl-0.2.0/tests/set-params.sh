#!/bin/bash

CREDS="admin:projectalamo"
DEVICE="http://dev-epiphan006.dce.harvard.edu"


curl -v --user ${CREDS} "${DEVICE}/admin/channel/set_params.cgi?touchscreen_recordctl=&touchscreen_enabled=on"





#"${DEVICE}/admin/channel1/get_params.cgi?touchscreen_enabled&touchscreen_info&touchscreen_preview&touchscreen_recordctl&touchscreen_timeout"
