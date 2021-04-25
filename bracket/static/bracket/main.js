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