$(document).ready(function() {
    var table = $('#employees-table').DataTable( {
    	  	columns: [
    			null,
    			null,
    			null,
    			null,
    			{ orderable: false, width: '5%' },
  			],
  			"autoWidth": false
    	}
    ) ;
} );