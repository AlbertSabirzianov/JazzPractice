var element = document.getElementById('back');
element.onclick = function() {
    document.location = document.referrer;
}

var accord_C = document.getElementById('accord_C');
var accord_G = document.getElementById('accord_G');

accord_C.onclick = function() {
    document.getElementById('play_C').play();
}
accord_G.onclick = function() {
    document.getElementById('play_G').play()
}