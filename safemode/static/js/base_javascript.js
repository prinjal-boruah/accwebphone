// to collapse navbar----------------------------------------------
$(document).ready(function () {
     $('#sidebarCollapse').on('click', function () {
         $('#sidebar').toggleClass('active');
     });
 });

$(document).ready(function() {
    $('#ipCamTable').DataTable();
} );

$(document).ready(function() {
    $('#webPhoneTable').DataTable();
} );

$(document).ready(function() {
    $('#mediaMasterTable').DataTable();
} );

$(document).ready(function() {
    setTimeout(function() {
        $('.message').fadeOut('slow');
    }, 2000);
});

// function for displaying time -----------------------------------
function display_c(){
    var refresh=1000; 
    mytime=setTimeout('display_ct()',refresh)
    }
    function display_ct() {
    var month = new Array();
    month[0] = "January";
    month[1] = "February";
    month[2] = "March";
    month[3] = "April";
    month[4] = "May";
    month[5] = "June";
    month[6] = "July";
    month[7] = "August";
    month[8] = "September";
    month[9] = "October";
    month[10] = "November";
    month[11] = "December";
    var x = new Date();

    currentHour =  x.getHours();
    currentHour = ("0" + currentHour).slice(-2);

    currentMinute = x.getMinutes();
    currentMinute = ("0" + currentMinute).slice(-2);

    currentSecond = x.getSeconds();
    currentSecond = ("0" + currentSecond).slice(-2);

    var x1= x.getDate() + " " + month[x.getMonth()]+ " " +x.getFullYear();
    x1 = x1 + " - " +  currentHour+ ":" +  currentMinute + ":" +  currentSecond;
    document.getElementById('clock').innerHTML = x1;
    display_c();

     }