
$(document).ready(function() {

    $(".txtbox").on('input', function() {
        check_json(this);
    });

    $("form").bind("reset", function(e) {
       $(".tstat").removeClass("alert-warning alert-success").html("");
    });


    function check_json(t) {
        emsg = "<b>OK</b>"; estat = "alert-success";
        if (t.value.length > 0) {
            try {
                JSON.parse(t.value);
            } catch(e) {
                emsg = "<b>Err</b>: " + e.message;
                estat = "alert-warning";
            }
        }
        ss = t.getAttribute("stat");
//        console.log(ss + ": " + estat + " n=" + t.value.length);
        $("#" + ss).html(emsg);
        $("#" + ss).removeClass("alert-warning alert-success").addClass(estat);
//        $("[refid=" + t.id + "]").removeClass("alert-warning alert-success").addClass(estat);
    }

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
                    check_json(box);
                    // var blob = new Blob([this.response], {type: 'image/png'});
                }
            };
            xhr.send();
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
