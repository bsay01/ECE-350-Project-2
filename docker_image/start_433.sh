# script to run rtl_433 with correct flags (RUNS AT CONTAINER STARTUP)

#sudo rtl_433 -s 2400000 -Y autolevel -Y ampest -Y squelch -H 30 -f 315000000 -f 433920000 -f 868000000 -f 915000000

su
mkdir -p data
rtl_433 -F csv:data/log.csv
