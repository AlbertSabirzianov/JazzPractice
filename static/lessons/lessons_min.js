function playById(num, musicKey) {
    document.getElementById('play_' + num + '_' + musicKey).play();
}


document.getElementById('accord_26_C').onclick = function() {
    playById('26', 'C');
}
document.getElementById('accord_26_G').onclick = function() {
    playById('26', 'G');
}

document.getElementById('accord_27_C').onclick = function() {
    playById('27', 'C');
}
document.getElementById('accord_27_G').onclick = function() {
    playById('27', 'G');
}

document.getElementById('accord_28_C').onclick = function() {
    playById('28', 'C');
}
document.getElementById('accord_28_G').onclick = function() {
    playById('28', 'G');
}
