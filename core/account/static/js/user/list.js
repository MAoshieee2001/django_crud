$(function () {
    $('#tbtListado').DataTable({
        serverSide: true,
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            headers: {'X-CSRFToken': csrfToken},
            data: {
                action: 'get_users',
            }, // parametros
            dataSrc: "user_list"
        },
        columns: [
            {"data": "index"},
            {"data": "full_names"},
            {"data": "fecha_nacimiento"},
            {"data": "username"},
            {"data": "email"},
            {"data": "is_active"},
            {"data": "last_login"},
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
            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return (data == true) ? '<span class="badge badge-success">Activo</span>' : '<span class="badge badge-warning">Inactivo</span>';
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});