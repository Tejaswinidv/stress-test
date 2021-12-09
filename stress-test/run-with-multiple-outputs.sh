#!/usr/bin/env bash
value=0
while read METRIC_VALUE; do
  echo ${METRIC_VALUE}
  value= $(value + METRIC_VALUE)
  curl -X POST -H "Authorization: Bearer ${WAVEFRONT_API_KEY}" \
  -d "${METRIC_NAME} ${METRIC_VALUE} source=concourse" \
  "https://vmwareprod.wavefront.com/report"
done < event/metric_value.txt
echo ${value}
