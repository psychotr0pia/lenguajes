#!/bin/bash
CONTADOR=10
until [ $CONTADOR -lt 0 ]
do
  echo El contador es $CONTADOR
  let CONTADOR--
done

