function hide() {
    $('.form-group').slice(3, 6).hide();
}

function show() {
    $('.form-group').show();
}

$(document).ready(function() {
    if (!$("#id_is_glass").is(':checked')) {
        hide();
    }
});

$('input[type="checkbox"][name="is_glass"]').change(function() {
    if (this.checked) {
        show();
    } else {
        hide();
    }
});