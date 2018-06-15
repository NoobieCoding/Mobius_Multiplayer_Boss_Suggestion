import json


def suggest(element, role):
    jobsData = {}
    try:
        with open('jobs.json', 'r') as f:
            jobsData = json.load(f)
    except Exception:
        print "Can't find json file."

    allSuggestedJobs = (jobsData
                        ["suggestion"]
                        [element.lower()+""]
                        [role.lower()+""])
    return allSuggestedJobs


def get_suggested_jobs_name(element, role):
    allSuggestedJobs = suggest(element, role)
    returnList = []
    for x in allSuggestedJobs:
        returnList.append(x["name"])
    return returnList


def get_suggested_pic_name(element, role):
    allSuggestedJobs = suggest(element, role)
    returnList = []
    for x in allSuggestedJobs:
        returnList.append(x["pic"])
    return returnList
