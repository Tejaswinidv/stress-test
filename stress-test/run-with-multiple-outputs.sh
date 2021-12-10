#!/usr/bin/env bash
value=0
while read METRIC_VALUE; do
  echo ${METRIC_VALUE}
  m_value=`echo ${METRIC_VALUE}`  
  #echo ${m_value}
  curl -X POST -H "Authorization: Bearer ${WAVEFRONT_API_KEY}" \
  -d "${METRIC_NAME} ${m_value} source=concourse" \
  "https://vmwareprod.wavefront.com/report"
done < event/metric_value.txt
echo ${value}
