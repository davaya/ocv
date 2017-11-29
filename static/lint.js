
$(document).ready(function() {

    $("select").click(function() {
        file = this.selectedOptions[0].value;
        boxid = this.parentNode.attributes.refid.value;
        box = document.getElementById(boxid);
        if (file == '') {
            box.value = '';
        } else {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', '/static/' + file, true);
            xhr.responseType = 'text';      // or 'blob'
            xhr.onload = function (e) {
                if (this.status == 200) {
                    box.value = this.responseText;
                    // var blob = new Blob([this.response], {type: 'image/png'});
                }
            };
            xhr.send();
        }
    });

    $("li").click(function(){
        boxid = this.parentNode.getAttribute("refid");
        if (boxid) {
            box = document.getElementById(boxid);
            box.value = this.firstElementChild.innerText.trim();
        }
    });

    $(".hasclear").keyup(function() {
        var t = $(this);
        t.next('span').toggle(Boolean(t.val()));
    });

    $(".clearer").hide($(this).prev('input').val());

    $(".clearer").click(function () {
        $(this).prev('input').val('').focus();
        $(this).hide();
    });
});
