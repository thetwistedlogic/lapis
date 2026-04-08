#!/bin/sh
# A simple script that converts certain files to html and runs prettier on them
for f in 06_MainDefinition.txt 08_Sentence.txt 09_SentenceFurigana.txt 11_Picture.txt 12_Glossary.txt 18_PitchPosition.txt 20_Frequency.txt; do 
  cp -- "$f" "$f.html"; prettier "$f.html" > "$f.2.html"; rm "$f" "$f.html"; mv "$f.2.html" "$f.html"
done
