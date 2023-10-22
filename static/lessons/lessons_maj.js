function playById(num, musicKey) {
    document.getElementById('play_' + num + '_' + musicKey).play();
}


document.getElementById('accord_22_C').onclick = function() {
    playById('22', 'C');
}
document.getElementById('accord_22_G').onclick = function() {
    playById('22', 'G');
}

document.getElementById('accord_23_C').onclick = function() {
    playById('23', 'C');
}
document.getElementById('accord_23_G').onclick = function() {
    playById('23', 'G');
}

document.getElementById('accord_24_C').onclick = function() {
    playById('24', 'C');
}
document.getElementById('accord_24_G').onclick = function() {
    playById('24', 'G');
}

document.getElementById('accord_25_C').onclick = function() {
    playById('25', 'C');
}
document.getElementById('accord_25_G').onclick = function () {
    playById('25', 'G');
}

