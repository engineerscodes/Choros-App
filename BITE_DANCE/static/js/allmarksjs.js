$("#vd").on("change", function () {
  var val = $(this).val();

  //console.log(val);
  var token = $("input[name=csrfmiddlewaretoken]").val();
  //console.log(token)
  $.ajax({
    type: "GET",
    url: "/bitdance/moderator/ajax",
    data: {
      videos: val,
      //csrfmiddlewaretoken: token
    },
    success: function (respone) {
      let responeObject = respone.data;
      if (val === "verified") {
        let tb = document.getElementById("TB");
        tb.innerHTML = "";
        let upd = document.getElementById("UPD");
        upd.innerHTML = "DATE";
        for (i in responeObject) {
          let tr = document.createElement("tr");
          let link = responeObject[i].video_link;
          let date = responeObject[i].date;
          let uploadeduser = responeObject[i].by_email;

          for (let j = 0; j < 3; j++) {
            let td = document.createElement("td");
            if (j === 0) {
              let a = document.createElement("a");
              a.setAttribute("href", "/videos/" + link);
              a.setAttribute("target", "_blank");
              a.innerHTML = "LINK";
              td.appendChild(a);
            }
            if (j === 1) {
              td.innerHTML = date;
            }
            if (j === 2) {
              td.innerHTML = uploadeduser;
            }

            tr.appendChild(td);
          }
          tb.appendChild(tr);
        }
      }

      if (val === "unseen") {
        let tb = document.getElementById("TB");
        tb.innerHTML = "";
        let upd = document.getElementById("UPD");
        upd.innerHTML = "UPLOADED DATE";
        for (i in responeObject) {
          let tr = document.createElement("tr");
          let link = responeObject[i].url_64encoding;
          let date = responeObject[i].date;
          let uploadeduser = responeObject[i].username;

          for (let j = 0; j < 3; j++) {
            let td = document.createElement("td");
            if (j === 0) {
              let a = document.createElement("a");
              a.setAttribute("href", "/videos/" + link);
              a.setAttribute("target", "_blank");
              a.innerHTML = "LINK";
              td.appendChild(a);
            }
            if (j === 1) {
              td.innerHTML = date;
            }
            if (j === 2) {
              td.innerHTML = uploadeduser;
            }

            tr.appendChild(td);
          }
          tb.appendChild(tr);
        }
      }
    },
  });
});
