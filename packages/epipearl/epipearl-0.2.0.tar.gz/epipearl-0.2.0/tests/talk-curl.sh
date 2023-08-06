#!/bin/bash

CREDS="admin:projectalamo"
DEVICE="http://dev-epiphan006.dce.harvard.edu"


#curl -v --user ${CREDS} "${DEVICE}/admin/timesynccfg" --data-urlencode "fn=date" \
#    --data-urlencode "tz=US/Alaska" --data-urlencode "rdate=auto" \
#    --data-urlencode "rdate_proto=NTP" --data-urlencode "server=north-america.pool.ntp.org"

#curl -v --user ${CREDS} "${DEVICE}/admin/touchscreencfg" \
#    -H "Content-Type: application/x-www-form-urlencoded" \
#    --data-urlencode "pfd_form_id=fn_episcreen" \
#    --data-urlencode "epiScreenEnabled=on" --data-urlencode "showVideo=on" \
#    --data-urlencode "showInfo=" --data-urlencode "epiScreenTimeout=123" \
#    --data-urlencode "epiScreenEnabled=on" \
#    --data-urlencode "recordControl="

#curl -v --user ${CREDS} "${DEVICE}/admin/reboot.cgi?noaction=yes"

#curl -v --user ${CREDS} "${DEVICE}/admin/channel3/layouts/1" \
#    --data '{"video":[{"type":"source","position":{"left":"0%","top":"0%","right":"50%","bottom":"50%","keep_aspect_ratio":true},"crop":{},"settings":{"source":"D2P280762.hdmi-a"}}],"audio":[],"background":"#000000"}'

#curl -v --user ${CREDS} "${DEVICE}/admin/channel1/streamsetup" \
#    --data-urlencode "rtmp_url=http:/fake-fake.akamai.com" \
#    --data-urlencode "rtmp_stream=dev-epiphan002-presenter-delivery.stream-1920x540_1_200@355694" \
#    --data-urlencode "rtmp_username=superfakeuser" \
#    --data-urlencode "rtmp_password=superfakeuser"

#curl -v --user ${CREDS} "${DEVICE}/admin/recorder4/archive" \
#    --data-urlencode "deleteid=m4" \
#    --data-urlencode "deletemode=trash"

#curl -v --user ${CREDS} "${DEVICE}/admin/recorder4/archive" \
#    --data-urlencode "pfd_form_id=rec_settings" \
#    --data-urlencode "timelimit=6:00:00" \
#    --data-urlencode "sizelimit=64000000" \
#    --data-urlencode "output_format=ts" \
#    --data-urlencode "afu_enabled=on" \
#    --data-urlencode "user_prefix=" \
#    --data-urlencode "upnp_enabled="

#curl -v --user ${CREDS} "${DEVICE}/admin/recorder4/archive" \
#    --data-urlencode "pfd_form_id=recorder_channels" \
#    --data-urlencode "rc[]=['1', '4']"

#curl -v --user ${CREDS} "${DEVICE}/admin/mhcfg" \
#    --data-urlencode "DEVICE_NAME=dev-epiphan006" \
#    --data-urlencode "DEVICE_USERNAME=bob" \
#    --data-urlencode "DEVICE_PASSWORD=dylan" \
#    --data-urlencode "DEVICE_CHANNEL=6" \
#    --data-urlencode "FILE_SEARCH_RANGE=100" \
#    --data-urlencode "ADMIN_SERVER_URL=http://52.72.59.90:80" \
#    --data-urlencode "ADMIN_SERVER_USER=jane" \
#    --data-urlencode "ADMIN_SERVER_PASSWD=doe" \
#    --data-urlencode "UPDATE_FREQUENCY=122" \
#    --data-urlencode "BACKUP_AGENT=False"

#curl -v --user ${CREDS} "${DEVICE}/admin/sources/D2P280762.hdmi-a" \
#    --data-urlencode "pfd_form_id=vsource" \
#    --data-urlencode "deinterlacing=on"

#curl -v --user ${CREDS} "${DEVICE}/admin/channel/set_params.cgi?touchscreen_recordctl=&touchscreen_enabled=on"
#"${DEVICE}/admin/channel1/get_params.cgi?touchscreen_enabled&touchscreen_info&touchscreen_preview&touchscreen_recordctl&touchscreen_timeout"

#curl -v --user ${CREDS} "${DEVICE}/admin/remotesupport.cgi" \
#    --data-urlencode "permanent_logs=" \
#    --data-urlencode "enablessh=on"

curl -v --user ${CREDS} "${DEVICE}/admin/infocfg"
