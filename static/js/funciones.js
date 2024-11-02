function get_errores_servidor(response) {
    let error = '<ul>';

    if (typeof (response) == 'object') {
        $.each(response, function (key, value) {
            error += '<li>' + value + '</li>';
        });
        error += '</ul>';
    } else {
        error = '<p>' + response + '</p>';
    }

    Swal.fire({
        title: 'Ocurrio un error!',
        html: error,
        icon: 'error',
    });
}