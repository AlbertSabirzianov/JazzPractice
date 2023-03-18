var element = document.getElementById('back');
element.onclick = function() {
    document.location = document.referrer;
}