$(document).ready(function() {
    var tasks_table = $('#tasks-history-table').DataTable( {
        "order": [[ 3, "desc" ]],
        "iDisplayLength": 25
    } );

} );
