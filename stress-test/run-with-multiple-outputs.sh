#!/usr/bin/env bash
value=0
apt-get install bc
while read METRIC_VALUE; do
  echo ${METRIC_VALUE}
  m_value=$(bc -l <<<"${METRIC_VALUE}") 
  #echo ${m_value}
  curl -X POST -H "Authorization: Bearer ${WAVEFRONT_API_KEY}" \
  -d "${METRIC_NAME} ${m_value} source=concourse" \
  "https://vmwareprod.wavefront.com/report"
done < event/metric_value.txt
echo ${value}

awk '{curl -X POST -H "Authorization: Bearer ${WAVEFRONT_API_KEY}" \
  -d "${METRIC_NAME} $0 source=concourse" \
  "https://vmwareprod.wavefront.com/report"}END{print $0}' event/metric_value.txt
