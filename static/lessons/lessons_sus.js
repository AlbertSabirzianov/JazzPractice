function playById(num, musicKey) {
    document.getElementById('play_' + num + '_' + musicKey).play();
}


document.getElementById('accord_19_C').onclick = function() {
    playById('19', 'C');
}
document.getElementById('accord_19_G').onclick = function() {
    playById('19', 'G');
}

document.getElementById('accord_20_C').onclick = function() {
    playById('20', 'C');
}
document.getElementById('accord_20_G').onclick = function() {
    playById('20', 'G');
}

document.getElementById('accord_21_C').onclick = function() {
    playById('21', 'C');
}
document.getElementById('accord_21_G').onclick = function() {
    playById('21', 'G');
}

