$("#unseen").on("click", function () {


});


$("#verified").on("click", function () {
  
});


$("#filterbyevent").on('click',function(){
    

});



$("#analytics").on('click',()=>{

   $.ajax({
     type: "GET",
     url: "/analaytics/",
     success: function (respone) {
       document.getElementsByClassName("output")[0].style.display="none";
       document.getElementById("dia").style.display = "flex";
       document.getElementById(
         "diag"
       ).innerHTML = `<canvas id="statcPie" ></canvas>`;
       let diag = document.getElementById("statcPie").getContext("2d");

         const data = {
           labels: ["CORRECTED ", "PENDING"],

           datasets: [
             {
               label: "My First Dataset",
               data: [respone.Actual_corrected, respone.Left_count],
               backgroundColor: ["rgb(255, 99, 132)", "rgb(54, 162, 235)"],
               hoverOffset: 4,
               options: {
                 responsive: true,
                 maintainAspectRatio: false,
                 layout: {
                   padding: 20,
                 },
               },
             },
           ],
         };
         
            const config = {
              type: "pie",
              data: data,
              
            };
           
            let  myChart = new Chart(diag, config);
             $("#example").DataTable();
     },
   });
});


 