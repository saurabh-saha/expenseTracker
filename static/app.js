var dataEx = [
        {
            "expense_id": 1,
            "user_id": 1,
            "uuid": "4ee17dae-aa0a-46b5-aa82-f2eb50b30e36",
            "description": "In blanditiis unde id laudantium ipsam ea.",
            "currency": "SHP",
            "amount": 3116,
            "first_name": "Laila",
            "last_name": "Hellwig",
            "created_at": "2019-12-03T01:37:43"
        },
        {
            "expense_id": 2,
            "user_id": 2,
            "uuid": "714bf5cf-14fe-4f8f-adf6-48461a7881c7",
            "description": "Explicabo eligendi vero consequuntur aut aut.",
            "currency": "SVC",
            "amount": 8363,
            "first_name": "Irma",
            "last_name": "Wende",
            "created_at": "2019-12-10T08:28:05"
        }
]

function format ( d ) {
    return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">'+
        '<tr>'+
            '<td>Name:</td>'+
            '<td>'+d.first_name+' '+d.last_name+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Description:</td>'+
            '<td>'+d.description+'</td>'+
        '</tr>'+
    '</table>';
}
 
$(document).ready(function() {

    $.ajax({
      'url': "/expenses",
      'method': "GET",
      'contentType': 'application/json'
    }).done( function(data) {

        if (data.success){
          
            var table = $('#example').DataTable( {
            "data": data.expenses ,
            "columns": [
                {
                    "className":      'details-control',
                    "orderable":      false,
                    "data":           null,
                    "defaultContent": ''
                },
                { "data": "currency" },
                { "data": "amount" },
                { "data": "created_at" },
                { "data": "status" },
                {
		            "targets": -1,
		            "data": null,
		            "defaultContent": "<button data-event='approve'>Yes</button>"
        		},
                {
		            "targets": -1,
		            "data": null,
		            "defaultContent": "<button data-event='reject'>No</button>"
        		},
            	{ "data": "first_name" , "visible": false},
            	{ "data": "last_name" , "visible": false },
            	{ "data": "description" , "visible": false}
            ],
            "order": [[1, 'asc']]
            });

            // Add event listener for opening and closing details
            $('#example tbody').on('click', 'td.details-control', function () {
                var tr = $(this).closest('tr');
                var row = table.row( tr );
         
                if ( row.child.isShown() ) {
                    // This row is already open - close it
                    row.child.hide();
                    tr.removeClass('shown');
                }
                else {
                    // Open this row
                    row.child( format(row.data()) ).show();
                    tr.addClass('shown');
                }
            } );

            $('#example tbody').on( 'click', 'button', function () {
            	row = table.row( $(this).parents('tr') )
			    var data = row.data();
			    action = this.getAttribute('data-event')
			        $.ajax({
				      'url': "/expense?expense_id="+data.expense_id+'&action='+action,
				      'method': "GET",
				      'contentType': 'application/json'
				    }).done( function(response) {
				    	if(response.success){
				    		index = row.index()
				    		data.status = action
				    		$('#example').dataTable().fnUpdate(data,index,undefined,false);
				    		alert(response.message)
				    	}else{
				    		alert(response.message)
				    	}
				    });

		    } );

        } else {
          alert('Reload. ' + data.message)
        }
    });
     

} );