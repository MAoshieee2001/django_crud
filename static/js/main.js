const pathname = window.location.pathname;

// * Función para obtener el valor de una cookie por su nombre
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// * Obtén el token CSRF desde las cookies
const csrfToken = getCookie('csrftoken');


$(function () {
    $('#btnCerrar').click(function (evt) {
        evt.preventDefault();
        $.ajax({
            headers: {'X-CSRFToken': csrfToken},
            url: '/logout/',
            type: 'POST',
            dataType: 'json',
            data: {
                action: 'cerrar_sesion',
            },
            success: function (response) {
                location.href = '/';
            },
            error: function (xhr, errorType, errorMessage) {

            },
            complete: function () {

            }
        });

    });
});
