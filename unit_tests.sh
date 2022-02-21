#!/bin/bash

# Run tests
echo "TEST 2015"
./main.py descriptions/2015.desc inputs/2015.ex.in > temp.parsed
diff temp.parsed parsed/2015.ex.parsed

echo "TEST 2016"
./main.py descriptions/2016.desc inputs/2016.ex.in > temp.parsed
diff temp.parsed parsed/2016.ex.parsed

echo "TEST 2017"
./main.py descriptions/2017.desc inputs/2017.ex.in > temp.parsed
diff temp.parsed parsed/2017.ex.parsed

echo "TEST picojr rustower"
./main.py descriptions/picojr_rustower.desc inputs/picojr_rustower.ex.in > temp.parsed
diff temp.parsed parsed/picojr_rustower.ex.parsed

echo "TEST 2016"
./main.py descriptions/2022_practice.desc inputs/2022_practice.ex.in > temp.parsed
diff temp.parsed parsed/2022_practice.ex.parsed

# Explain results
echo "=> Tests are successful if no diff are shown"

# Cleanup
rm temp.parsed

