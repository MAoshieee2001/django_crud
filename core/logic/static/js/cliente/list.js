$(function () {
    $('#tbtListado').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        serverSide: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            headers: {'X-CSRFToken': csrfToken},
            data: {
                action: 'get_clientes',
            }, // parametros
            dataSrc: "clientes"
        },
        columns: [
            {"data": "index"},
            {"data": "nombres"},
            {"data": "apellidos"},
            {"data": "dni"},
            {"data": "fecha_nacimiento"},
            {"data": "genero.names"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<a class="btn btn-warning btn-xs" href="' + pathname + 'update/' + data + '/"><i class="fas fa-edit"></i></a > ' +
                        '<a class="btn btn-danger btn-xs" href="' + pathname + 'delete/' + data + '/"><i class="fas fa-trash"></i></a >';
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});