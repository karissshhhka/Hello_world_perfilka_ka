#!/bin/bash
read -p "weight (kg): " WEIGHT
read -p "height (m): " HEIGHT

BMI=$(echo "scale=0; $WEIGHT / ($HEIGHT * $HEIGHT)" | bc)
echo "BMI: $BMI"
