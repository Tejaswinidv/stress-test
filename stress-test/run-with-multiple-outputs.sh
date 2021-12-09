#!/usr/bin/env bash

while read METRIC_VALUE; do
  echo ${METRIC_VALUE}
  curl -X POST -H "Authorization: Bearer ${WAVEFRONT_API_KEY}" \
  -d "${METRIC_NAME} ${METRIC_VALUE} source=concourse" \
  "https://vmwareprod.wavefront.com/report"
done < event/metric_value.txt
