function playById(num, musicKey) {
    document.getElementById('play_' + num + '_' + musicKey).play();
}


document.getElementById('accord_17_C').onclick = function() {
    playById('17', 'C');
}
document.getElementById('accord_17_G').onclick = function() {
    playById('17', 'G');
}

document.getElementById('accord_18_C').onclick = function() {
    playById('18', 'C');
}
document.getElementById('accord_18_G').onclick = function() {
    playById('18', 'G');
}
