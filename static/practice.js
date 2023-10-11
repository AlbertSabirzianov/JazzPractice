let right = document.getElementById('yes').textContent;

let element = document.getElementById('id_right_decision');
element.value = right;
element.style.visibility = 'hidden';
document.getElementById('yes').style.visibility = 'hidden';

var me = document.getElementById('play');
me.onclick = function() {
    document.getElementById('player').play();
}