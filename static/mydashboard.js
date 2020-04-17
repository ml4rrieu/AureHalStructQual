
         
$.ajax({
url: "/calcNoiseLevel",
success: display_noiseLevel
});

function display_noiseLevel(result) {
  // console.log('dans la fonction')

  noiseHtml = '<h2>'+result['noiseLvl'] + ' % </h2>' 
  document.getElementById("noiseLvl").innerHTML = noiseHtml


  uvsqIncom = 'https://aurehal.archives-ouvertes.fr/structure/browse/critere/parentDocid_i%3A81173/solR/1/page/1/nbResultPerPage/50/tri/valid/filter/incoming/category/%2A'
  uvsqValid = 'https://aurehal.archives-ouvertes.fr/structure/browse/critere/parentDocid_i%3A81173/solR/1/page/1/nbResultPerPage/50/tri/valid/filter/valid/category/%2A'         

  incom =  '<a href="'+uvsqIncom+'" target="_blank">Entrantes</a>&emsp;'+ result['incoming']+'<br />'
  incom += '<a href="'+uvsqValid+'" target="_blank">Valides</a>&emsp;&emsp;' + result['valid']+'</a>'
  document.getElementById("incomValid").innerHTML = incom
}



// EVOL NOISE
window.onload = function () {
    console.log('script noise level')
    var ctx = document.getElementById("myChart").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        showTooltips: false,
        data: {
            labels: ['20 janv', '13 fev', '20 fev', '3 mars', '11 mars', '18 mars','25 mars','1 avril', '8 avril', '15 avril'],
            datasets: [{
                data: [180, 159, 158, 156, 153, 166, 175, 115, 90, 64],
                backgroundColor : "#e7c1f7",
                borderWidth: 1
            }]
        },
        options: {
          tooltips: {enabled: false},
          hover: {mode: null},
          legend: { display: false },
          title: {
            display: true,
            text: 'Evolution du % de bruit'
          },
          scales: {
           yAxes: [{
            ticks: {beginAtZero: true}              
          }]
        }
      }
    });
};



// INCOMMING STRUCT TABLE 

google.charts.load('current', {'packages':['table']});
    
$.ajax({
      url: "/getIncomingTable",
      success: displayTable
    });

function displayTable(result) {
  console.log('script display table')

  google.charts.setOnLoadCallback(drawTable);

  function drawTable() {   
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Structures entrantes');
    data.addColumn('string', 'Nb doc');
    data.addColumn('string', 'Last update');

    var url = '<a href="https://aurehal.archives-ouvertes.fr/structure/read/id/';
    var url2 = '<a href="https://hal.archives-ouvertes.fr/search/index/q/*/structId_i/'
    //array syntaxe [name, docid, nbdoc, date]
    for (var key in result){
      data.addRows([
          [ url+result[key][1]+'" target="_blank">'+result[key][0]+'</a>', result[key][2].toString(), result[key][3].toString() ]
        ]);

    }
    // data.addRows([
    //   ['structure main',  '9', '2019-06-23 '],
    //   ['structure main2',  '2', '2019-01-23 ']
    // ]);

    var table = new google.visualization.Table(document.getElementById('htmlIncomingTable'));

    table.draw(data, {allowHtml: true, showRowNumber: false, width: '100%', height: '100%'});
  }

 }