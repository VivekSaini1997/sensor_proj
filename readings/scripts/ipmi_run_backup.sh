pattern='[0-9]+\.[0-9]+'
ipmi_ip=$1

ipmitool -U ADMIN -P ADMIN -H $1 sensor > ../$1/ipmi_readings

tail -59 ../$1/fan_readings > ../$1/fan_readings_tmp && mv ../$1/fan_readings_tmp ../$1/fan_readings

cat ../$1/ipmi_readings | grep RPM > ../$1/fans_raw

printf "%s" $(date +%T) >> ../$1/fan_readings;while read p; do [[ $p =~ $pattern ]]; printf ', %s' ${BASH_REMATCH[0]}; done < ../$1/fans_raw >> ../$1/fan_readings; printf '\n' >> ../$1/fan_readings

tail -1 ../$1/fan_readings > ../$1/fan_readings_recent

tail -59 ../$1/temp_readings > ../$1/temp_readings_tmp && mv ../$1/temp_readings_tmp ../$1/temp_readings

cat ../$1/ipmi_readings | grep degrees  > ../$1/temps_raw

printf "%s" $(date +%T) >> ../$1/temp_readings;while read p; do [[ $p =~ $pattern ]]; printf ', %s' ${BASH_REMATCH[0]}; done < ../$1/temps_raw >> ../$1/temp_readings; printf '\n' >> ../$1/temp_readings

tail -1 ../$1/temp_readings > ../$1/temp_readings_recent
