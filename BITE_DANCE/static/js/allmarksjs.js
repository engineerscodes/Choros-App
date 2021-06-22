$("#unseen").on("click", function () {
  $.ajax({
    type: "GET",
    url: "/bitdance/moderator/ajax",
    data: {
      videos: "unseen",
    },
    success: function (respone) {
      let responeObject = respone.data;
      let tab = document.getElementById("example");
      tab.style.display = "table";
      document.getElementById("dia").style.display = "none";
      document.getElementById("HeaderOut").innerHTML = "PENDING";
      tab.innerHTML = "";
      tab.innerHTML = `<thead>
            <tr>
                <th>SR.NO</th>
                <th>LINK</th>
                <th>UPLOADED DATE</th>
                <th>USER</th>
            </tr>
        </thead>`;
      let temptb = "";
      for (let i = 0; i < responeObject.length; i++) {
        temptb =
          temptb +
          ` <tr>
                <td></td>
                <td>${responeObject[i].date}</td>
                <td><a href="/videos/${
                  responeObject[i].url_64encoding
                }" target="_blank">View</a></td>
                <td>${responeObject[i].username.split("@")[0]}</td>
            </tr> `;
      }

      tab.innerHTML = tab.innerHTML + "<tbody>" + temptb + "</tbody>";
    },
  });
});

$("#verified").on("click", function () {
  $.ajax({
    type: "GET",
    url: "/bitdance/moderator/ajax",
    data: {
      videos: "verified",
    },
    success: function (respone) {
      let responeObject = respone.data;
      let tab = document.getElementById("example");
      tab.style.display = "table";
      document.getElementById("dia").style.display = "none";
      document.getElementById("HeaderOut").innerHTML = "CORRECTED";
      tab.innerHTML = "";

      tab.innerHTML = `<thead>
            <tr>
                <th>SR.NO</th>
                <th>EVENT NAME</th>
                <th>DATE</th>
                <th>LINK</th>
                <th>USER</th>
            </tr>
        </thead>`;
      let temptb = "";
      for (let i = 0; i < responeObject.length; i++) {
        temptb =
          temptb +
          ` <tr>
                <td></td>
                <td>${responeObject[i].EventName}</td>
                 <td>${responeObject[i].date}</td>
                <td><a href="/videos/${
                  responeObject[i].video_link
                }" target="_blank">View</a></td>
                <td>${responeObject[i].by_email.split("@")[0]}</td>
            </tr> `;
      }

      tab.innerHTML = tab.innerHTML + "<tbody>" + temptb + "</tbody>";
    },
  });
});

$("#filterbyevent").on("click", function () {
  $.ajax({
    type: "GET",
    url: "/events/",
    success: function (respone) {
      let responeObject = respone.data;
      let tab = document.getElementById("example");
      tab.style.display = "table";
      document.getElementById("dia").style.display = "none";
      document.getElementById(
        "HeaderOut"
      ).innerHTML = `<div style="margin:5px;">SEARCH</div><input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for eventnames.." title="Type in a name">`;
      tab.innerHTML = ``;
      tab.innerHTML = `<thead>
            <tr>
                <th>SR.NO</th>
                <th>EVENT NAME</th>
                <th>DATE</th>
                <th>LINK</th>
                <th>USER</th>
            </tr>
        </thead>`;
      let temptb = "";
      for (let i = 0; i < responeObject.length; i++) {
        temptb =
          temptb +
          ` <tr>
                <td></td>
                <td>${responeObject[i].EventName}</td>
                 <td>${responeObject[i].date}</td>
                <td><a href="/videos/${
                  responeObject[i].video_link
                }" target="_blank">View</a></td>
                <td>${responeObject[i].by_email.split("@")[0]}</td>
            </tr> `;
      }

      tab.innerHTML = tab.innerHTML + "<tbody>" + temptb + "</tbody>";
    },
  });
});

$("#analytics").on("click", () => {
  $.ajax({
    type: "GET",
    url: "/analaytics/",
    success: function (respone) {
      let responeObject = respone.data;
      let tab = document.getElementById("example");
      tab.style.display = "none";

      document.getElementById("HeaderOut").innerHTML = " statistics";
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

      let myChart = new Chart(diag, config);
    },
  });
});

function myFunction() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("example");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
