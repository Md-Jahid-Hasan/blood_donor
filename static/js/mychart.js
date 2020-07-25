
var endpoint = '/statistic/a/'
var label = []
var mydata = []


$.ajax({
  method: "GET",
  url: endpoint,
  success: function(data){
       console.log(data)
       label = data.label
       mydata = data.blood_group
        chartDetails()

  },
});

function chartDetails(){

var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: label,
            datasets: [{
                label: 'Number of Donor in our Database',
                data: mydata,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

function chartDetails2(newlabel, newdata){
var ctx = document.getElementById('myChart2').getContext('2d');
if(window.bar != undefined)
    window.bar.destroy();

    //var myChart = new Chart(ctx, {
    window.bar = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: newlabel,
            datasets: [{
                label: 'Number of Donor Donet Blood in selected month',
                data: newdata,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {

            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true

                    }
                }]
            }
        }
    });
}


$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();

});


function create_post() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : endpoint, // the endpoint
        type : "POST", // http method
        data : { donate_year : $('#year').val(),
          donate_month:$('#month').val(),// data sent with the post request
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },

        // handle a successful response
        success : function(d) {
           var new_lebel = d.label
           var new_data = d.blood_group
           console.log(new_data)
           chartDetails2(new_lebel, new_data)
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

$(document).ready(function(){
    $("#year").change(function(){
        console.log("Hello dd");
        receive_year();
    });
});


$(document).ready(function(){
    $('#month').change(function(){
        console.log("Hello month");
         $.ajax({
            url: endpoint,
            type: "POST",
            data: {
                donate_month: $('#month').val(),
                donate_year: $('#year').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(d){
                newlabel = d.label
                newdata = d.blood_group
                console.log(d.blood_group)
                console.log(d.label)

                chartDetails2(newlabel, newdata)
            }

        });
    });
});


function receive_year(){
       $.ajax({
        url : endpoint,
        type : "POST",
        data : {
            donate_year : $('#year').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },

        success : function(d) {
            $("#month").empty();
            $("#month").prepend("<option>Month</option>");
            $.each(d.month, function(index, value){
                $("#month").prepend("<option value=" + value +" >" + value + "</option>")
            })
        },

    });
}

