#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA| jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
ICU=$(echo $DATA | jq '.[0].inIcuCumulative')
RECOVERED=$(echo $DATA | jq '.[0].recovered')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative cases, $ICU people who had been in the ICU, and $RECOVERED people who have officially recovered."
