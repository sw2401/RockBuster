window.onload = init;

function showMovie() {
    var x = document.getElementById("mSelect");
    var y = document.getElementById("tvSelect");
    var z = document.getElementById("vgSelect");

    var a = document.getElementById("mVal");
    var b = document.getElementById("tVal");
    var c = document.getElementById("vVal");

    x.style.display = "inline";
    y.style.display = "none";
    z.style.display = "none";

    a.style.color = "black";
    a.style.backgroundColor = "#FDB31E"
    b.style.color = "#FDB31E";
    b.style.backgroundColor = "black"
    c.style.color = "#FDB31E";
    c.style.backgroundColor = "black"
}

function showTV() {
    var x = document.getElementById("mSelect");
    var y = document.getElementById("tvSelect");
    var z = document.getElementById("vgSelect");

    var a = document.getElementById("mVal");
    var b = document.getElementById("tVal");
    var c = document.getElementById("vVal");

    x.style.display = "none";
    y.style.display = "inline";
    z.style.display = "none";

    a.style.color = "#FDB31E";
    a.style.backgroundColor = "black"
    b.style.color = "black";
    b.style.backgroundColor = "#FDB31E"
    c.style.color = "#FDB31E";
    c.style.backgroundColor = "black"
}

function showVG() {
    var x = document.getElementById("mSelect");
    var y = document.getElementById("tvSelect");
    var z = document.getElementById("vgSelect");

    var a = document.getElementById("mVal");
    var b = document.getElementById("tVal");
    var c = document.getElementById("vVal");

    x.style.display = "none";
    y.style.display = "none";
    z.style.display = "inline";

    a.style.color = "#FDB31E";
    a.style.backgroundColor = "black"
    b.style.color = "#FDB31E";
    b.style.backgroundColor = "black"
    c.style.color = "black";
    c.style.backgroundColor = "#FDB31E"
}

function init(){
  showMovie();

  var d = document.getElementById("mVal");
  var e = document.getElementById("tVal");
  var f = document.getElementById("vVal");

  var q = document.getElementById("mSelect");
  var r = document.getElementById("tvSelect");
  var s = document.getElementById("vgSelect");

  d.onclick = showMovie;
  e.onclick = showTV;
  f.onclick = showVG;
}
