import data
import sys
import suggestion_system as suggest_sys

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

print "Result"
print "================================================"

allSuggestedJobs = (suggest_sys
                    .get_suggested_jobs_name
                    (selectedElement, selectedRole))
for x in allSuggestedJobs:
    print x

print "================================================"
print "\nHappy Mobius Final Fantasy Kupo!!\n"
