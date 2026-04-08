#!/bin/sh
# A simple script that converts certain files to html and runs prettier on them
for f in ./example_card/06_MainDefinition.txt ./example_card/08_Sentence.txt ./example_card/09_SentenceFurigana.txt ./example_card/11_Picture.txt ./example_card/12_Glossary.txt ./example_card/18_PitchPosition.txt ./example_card/20_Frequency.txt; do 
  base="${f%.*}"
  cp -- "$f" "$base.html"
  prettier "$base.html" > "$base.2.html"
  rm "$f" "$base.html"
  mv "$base.2.html" "$base.html"
done
