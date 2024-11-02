$(function () {
    $('form').submit(function (evt) {
        evt.preventDefault();
        let parametros = new FormData(this);
        let list_url = $(this).attr('data-url');
        $.ajax({
            headers: {'X-CSRFToken': csrfToken},
            url: pathname,
            type: 'POST',
            dataType: 'json',
            data: parametros,
            processData: false,
            contentType: false,
            success: function (response) {
                if (!response.hasOwnProperty('error')) {
                    location.href = list_url;
                    return false;
                }
                get_errores_servidor(response.error);
            },
            error: function (xhr, errorType, errorMessage) {
                alert(errorType + ' ' + errorMessage);
            },
            complete: function () {

            }
        });
    });
});