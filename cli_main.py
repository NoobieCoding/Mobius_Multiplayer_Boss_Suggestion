import data
import sys
import json

# Created by Nuttapong Rojanavanich

print """Hello, Welcome to Mobius Final Fantasy
Multiplayer mode job suggestion.
================================================"""

print """please Select the boss's element.
1) Fire, 2) Water, 3) Earth, 4) Wind, 5) Light, 6) Dark"""

try:
    eleInput = int(raw_input())
    selectedElement = data.elements[eleInput - 1]
    print "\nYou have selected " + selectedElement + ".\n"
except Exception as e:
    print "Error occurred "
    sys.exit(10)


print """please Select the role.
1) Attacker 2) Breaker, 3) Supporter, 4) Defender
"""

try:
    roleInput = int(raw_input())
    selectedRole = data.roles[roleInput - 1]
    print "\nYou have selected " + selectedRole + ".\n"
except Exception as e:
    print "Error occurred "
    sys.exit(10)

jobsData = {}

try:
    with open('jobs.json', 'r') as f:
        jobsData = json.load(f)
except Exception:
    print "Can't find json file."

print "Result"
print "================================================"

allSuggestedJobs = jobsData["suggestion"][selectedElement.lower()+""]
[selectedRole.lower()+""]
for x in allSuggestedJobs:
    print x

print "================================================"
print "\nHappy Mobius Final Fantasy Kupo!!\n"
