#!/bin/bash
# File: run.sh

#===============================================================
# CONSTANTS
#===============================================================

CALLINFO="CALLINFO.txt"
ERR_USAGE="USAGE: ./run.sh"
ERR_PHONE_INPUT="INVALID LAYOUT/PHONE#. Please enter in E.164 format -> (+1xxxxxxxxxx)"
ERR_MSG_INPUT="INVALID LAYOUT/MSG. Please enter valid msg (500 character limit)"
INPUT_PHONE_PROMPT="Please enter a phone# you would like to call (+1xxxxxxxxxx): "
INPUT_MSG_PROMPT="Please enter your message. (500 character limit)"
PHONE_NUMBER_SUCCESS="Phone number saved... "
MSG_SUCCESS="Message saved... "
CONFIRMATION="Are you sure this is what you want your message to be? (Y/N)"
INVALIDYorN="INVALID"
INPUT_EMAIL="Please enter your email address linked to your google voice account:"
INPUT_EMAIL_PASSWD="Please enter your password linked to your google voice account:"

MSG_CHAR_CAP=500
PHONE_CHAR_CAP=12

#==============================================================
# CODE
#==============================================================

# checkMessage
# prompt for user input, test and write back to prompt. 
# Ask for confirmation.
#
# USAGE
#     checkMessage
function checkMessage {
    while [ 0 -eq 0 ]; do
        read -p "${INPUT_MSG_PROMPT}" message
        if ! [ -z "$message" ] ; then
            if [ "${#message}" -le "${MSG_CHAR_CAP}" ]; then
                echo "---------YOUR MESSAGE----------" #spacing
                echo "$message"
                echo "-------------------------------"
                read -p "${CONFIRMATION}" YorN
                case "$( echo $YorN | tr '[:lower:]' '[:upper:]' )" in
                    Y)
                        echo "${message}" >> "${CALLINFO}"
                        echo "${MSG_SUCCESS}"
                        return 0 ;;
                    N)
                        ;;
                    *)
                        echo "${INVALIDYorN}" ;;
                esac
                continue
            fi
        else
            echo "${ERR_MSG_INPUT}"
        fi
    done
}

# checkPhoneNumber
# Checks the user input to make sure it is valid before adding
# to the callinfo.txt.
#
# USAGE 
#    checkPhoneNumber phoneNumber
#
# INPUT
#    phoneNumber to be added
function checkPhoneNumber {
    if [ $# -eq 1 ]; then
        if [ "${#1}" -eq "${PHONE_CHAR_CAP}" ]; then
            if [ "$( echo "$1" | cut -c 1-1 )" == "+" ]; then
                i=1 #start at 2 because 1 should be +
                while (( i++ < ${#1} )); do
                    if ! [ "$( echo "$1" | cut -c $i-$i )" -eq "$( echo "$1" | cut -c $i-$i )" ] &> /dev/null; then
                        break #above command checks if not integer
                    fi
                done
                return 0 #success

            fi
        fi
    fi
    echo "${ERR_PHONE_INPUT}"
    return 1 #failure
}

# main
# purpose to instantiate and populate the CALLINFO.txt file
# for the python script. Basic error-handling.
# 
# USAGE
#    main
function main {
    #check to make sure CALLINFO exists
    rm -rf CALLINFO.txt message.mp3
    if ! [ -f  "${CALLINFO}" ]; then
        echo -n "File CALLINFO.txt does not exist. Making new..."
        touch "${CALLINFO}"
        echo "done"
    fi
    while [ 0 -eq 0 ]; do
        read -p "${INPUT_PHONE_PROMPT}" phoneNumber
        if checkPhoneNumber ${phoneNumber} ; then
            echo "${phoneNumber}" >> "${CALLINFO}"
            echo "${PHONE_NUMBER_SUCCESS}"
            break
        fi
    done

    #Prompt for user message    
    checkMessage

    echo "THIS PART HAS NO ERROR HANDLING. IF YOU INPUT YOUR EMAIL AND PASSWORD WRONG THIS WILL FAIL"
    read -p "${INPUT_EMAIL}" emailAddr
    echo "${emailAddr}" >> "${CALLINFO}"
    read -p "${INPUT_EMAIL_PASSWD}" emailPass
    echo "${emailPass}" >> "${CALLINFO}"
    $PWD/autoNumber.exe
}

#===============================================================
# INNIT
#===============================================================

if [ $# -gt 0 ]; then #innit args greater than zero
    echo "${ERR_USAGE}"
    exit 1
fi
main