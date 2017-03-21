$(document).ready(function() {
    $('#tasks-history-table').DataTable( {
        "order": [[ 3, "desc" ]],
        "iDisplayLength": 25
    } );   
} );
