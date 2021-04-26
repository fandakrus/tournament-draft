from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from random import shuffle

def get_teams(request):
    teams = []
    i = 1
    while True: 
        # gets all teams passed with POST request
        team = request.POST.get("team" + str(i), "")
        if team == "":
            break
        else:
            teams.append(team)
        i += 1
    return teams


def make_all_table(teams):
    # prepare the table for all-to-all mode
    matches = []
    for i in range(len(teams) - 1):
        team = teams[i]
        for j in range(len(teams) - i - 1):
            matches.append([team, teams[i + j + 1]])
    shuffle(matches)
    return matches
    


def index(request, *args, **kwargs):      # basic view for the first page with team picks
    return render(request, 'bracket/index.html')

def make(request, *args, **kwargs):
    # prepare the table for tournament and pass it to view
    if request.method == 'POST':
        if request.POST.get("format", "") == "everyone":
            # work when it is selected to play everyone with everyone
            teams = get_teams(request)
            matches = make_all_table(teams)
            return render(request, 'bracket/alltoall.html', {"matches": matches})
        
        else: 
            # when is selected the bracket mode
            team = request.POST.get("team5", "")
            return HttpResponse("this is not ready for your yet.")

    return HttpResponseRedirect('bracket/index.html')


