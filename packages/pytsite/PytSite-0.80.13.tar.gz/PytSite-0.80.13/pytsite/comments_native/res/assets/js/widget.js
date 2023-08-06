function createCommentSlot(comment) {
    var slot = $('<div class="comment-item" data-uid="' + comment['uid'] + '" data-parent-uid="' +
        comment['parent_uid'] + '">');

    if (comment['parent_uid'])
        slot.addClass('reply');

    var left = $('<div class="left"></div>');
    slot.append(left);

    var right = $('<div class="right"></div>');
    slot.append(right);

    var userPic = $('<div class="author-picture"><img src="' + comment['author']['picture_url'] + '">');
    left.append(userPic);

    var header = $('<div class="header"></div>');
    header.append($('<div class="author">' + comment['author']['full_name'] + '</div>'));
    header.append($('<div class="publish-time">' + comment['publish_time']['ago'] + '</div>'));
    header.append($('<div class="report"><a class="report-btn" href="#"><i class="fa fa-fw fa-flag"></i>&nbsp;' +
        t('pytsite.comments_native@report') + '</a></div>'));
    right.append(header);

    var body = $('<div class="body">' + comment['body'] + '</div>');
    right.append(body);

    var footer = $('<div class="footer">');
    //footer.append($('<div class="vote-up"><a href="#"><i class="fa fa-fw fa-chevron-up"></i></a></div>'));
    //footer.append($('<div class="vote-down"><a href="#"><i class="fa fa-fw fa-chevron-down"></i></a></div>'));
    footer.append($('<div class="reply"><a class="reply-btn" href="#"><i class="fa fa-fw fa-reply"></i>&nbsp;' +
        t('pytsite.comments_native@reply') + '</a></div>'));
    right.append(footer);

    var replies = $('<div class="replies">');
    right.append(replies);

    return slot;
}

$(window).on('pytsite.widget.init:pytsite.comments_native._widget.Comments', function (e, widget) {
    var em = widget.em;
    var threadUid = em.data('threadId');
    var form = em.find('.form');
    var formReplyTo = form.find('.reply-to');
    var formCommentBody = form.find('.comment-body');
    var formMessages = em.find('.messages');
    var commentsList = em.find('.comments-list');
    var commentsLoadOffset = 0;
    var commentsLoadRemains = 0;

    //  Load comments
    pytsite.httpApi.get(em.data('commentsLoadEp'), {
        thread_uid: threadUid,
        skip: commentsLoadOffset
    }).success(function (r) {
        commentsLoadOffset = r['items'].length;
        commentsLoadRemains = parseInt(r['remains']);

        for (var i = 0; i < r['items'].length; i++) {
            var newSlot = createCommentSlot(r['items'][i]);

            // Click on 'Reply' button
            newSlot.find('.reply-btn').click(function (e) {
                e.preventDefault();
                var btn = $(this);

                commentsList.find('.reply-btn.hidden').removeClass('hidden');
                btn.addClass('hidden');

                btn.closest('.right').find('.replies').first().prepend(form);
                formReplyTo.val(btn.closest('.comment-item').data('uid'));
                formCommentBody.focus();
            });

            var parentUid = r['items'][i]['parent_uid'];
            if (parentUid) {
                var parentSlot = commentsList.find('.comment-item[data-uid=' + parentUid + ']');
                parentSlot.find('.replies').append(newSlot);
            }
            else
                commentsList.append(newSlot);
        }
    });

    // Submit new comment
    form.submit(function (e) {
        e.preventDefault();

        formMessages.html('');

        pytsite.httpApi.post(em.data('commentSubmitEp'), {
            thread_uid: threadUid,
            parent_uid: formReplyTo.val(),
            body: formCommentBody.val()
        }).fail(function (e) {
            formMessages.append('<div class="alert alert-danger">' + e.responseJSON.error + '</div>');
        });
    });
});
