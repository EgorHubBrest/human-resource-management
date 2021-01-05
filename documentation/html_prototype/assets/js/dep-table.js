$(document).ready(function() {
    var table = $('#departments-table').DataTable( {
    		columns: [
            { width: '75%', targets: 0 },
            { width: '20%', targets: 0 },
            { width: '5%', targets: 0, orderable: false }
        	],
        	"autoWidth": false
    	}
    ) ;
} );