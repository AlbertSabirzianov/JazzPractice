function playById(num, musicKey) {
    document.getElementById('play_' + num + '_' + musicKey).play();
}


document.getElementById('accord_1_C').onclick = function() {
    playById('1', 'C');
}
document.getElementById('accord_1_G').onclick = function() {
    playById('1', 'G');
}

document.getElementById('accord_2_C').onclick = function() {
    playById('2', 'C');
}
document.getElementById('accord_2_G').onclick = function() {
    playById('2', 'G');
}

document.getElementById('accord_3_C').onclick = function() {
    playById('3', 'C');
}
document.getElementById('accord_3_G').onclick = function() {
    playById('3', 'G');
}
