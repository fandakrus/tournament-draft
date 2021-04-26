var formcount = 1;

function AddTeam() {
    formcount = formcount + 1;
    container = document.getElementById('container');
    var teamdiv = document.createElement('div');
    var label = document.createElement("label");
    var input = document.createElement("input");
    label.htmlFor = "team" + formcount;
    label.appendChild(document.createTextNode("Team " + formcount));
    input.type = "text";
    input.name = "team" + formcount;
    teamdiv.appendChild(label);
    teamdiv.appendChild(input);
    teamdiv.appendChild(document.createElement('br'));
    container.appendChild(teamdiv);
}

function ThisWin(winnerId) {
    document.getElementById(winnerId).style.backgroundColor = '#33ff33';
    winfield = winnerId.split("-");
    if (winfield[0] === 'resultblue'){
        document.getElementById('resultred-' + winfield[1]).style.backgroundColor = 'red';
    } else {
        document.getElementById('resultblue-' + winfield[1]).style.backgroundColor = 'red';
    }
}