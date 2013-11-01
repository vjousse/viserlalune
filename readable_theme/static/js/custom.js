$(function() {
    $('.reply').click(function() {
        $('.reply-form').hide();
        $("#reply-" + $(this).data("id")).toggle();
    });

    $('.comments-toggle').click(function() {
        $('#comments').show();
        $('#displaycomments').hide();
    });
});
