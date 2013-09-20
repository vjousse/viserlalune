$(function() {
    $('.reply').click(function() {
        $('.reply-form').hide();
        $("#reply-" + $(this).data("id")).toggle();
    });
});
