#!/bin/bash
for (( x=2 ; x<= 3 ; x++ ))
do
touch "exercicio$x.py"
git add "exercicio$x.py"
done
