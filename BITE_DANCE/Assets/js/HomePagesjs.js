let gridvd = document.getElementsByClassName("vidoeGrid")[0];
let count = 0;
let res=0;
function getVideos() {
   
  /* if((count*6)-(count-1)*6>res && count!=0)
    {  console.log("count*6 :" + count * 6);
    console.log("res :" + res);
     return 0;
    }
    */

  $.ajax({
    type: "GET",
    url: "getcontent/",
    data: {
      vdreq: ++count,
    },
    success: function (respone) {
      let responeObject = respone.data;
       
      res=responeObject.length;
      for (i in responeObject) {
        let divT = document.createElement("div");
        divT.setAttribute("class", "vidoeDjango");
        let anc = document.createElement("a");
        anc.setAttribute("href", "/videos/" + responeObject[i].url_64encoding);
        let imgs = document.createElement("img");
        imgs.src = responeObject[i].thumbnail;
        imgs.style.width = "330px";
        imgs.style.height = "200px";
        anc.appendChild(imgs);
        divT.appendChild(anc);
        for (let j = 0; j < 4; j++) {
          let h5 = document.createElement("h5");
          if (j == 0) {
            h5.innerHTML = responeObject[i].captions;
            h5.setAttribute("id", "pad");
          }
          if (j == 1) {
            h5.innerHTML = responeObject[i].username;
          }
          if (j == 2) {
            h5.innerHTML = responeObject[i].date;
          }
          if(j==3)
          {
            h5.innerHTML = "Event Name :" + responeObject[i].EventName;
          }
          divT.appendChild(h5);
        }
        gridvd.appendChild(divT);
      }
    },
    error: function (error) {},
  });
}

setTimeout(getVideos, 1000);

window.addEventListener("scroll", () => {
  const { scrollTop, clientHeight, scrollHeight } = document.documentElement;

  if (scrollTop + clientHeight >= scrollHeight - 1) {
    getVideos();
  }
});

fromdate = document.getElementById("from");
todate = document.getElementById("to");
fromdate.defaultValue = "2021-04-01";
todate.defaultValue = new Date().toISOString().slice(0, 10);

function filterbydate() {
  if (fromdate.value != "" && todate.value != "") {
    $.ajax({
      type: "GET",
      url: "getcontent/filter",
      data: {
        fromdate: fromdate.value,
        todate: todate.value,
      },
      success: function (respone) {
        gridvd.innerHTML = "";
        let responeObject = respone.data;
        for (i in responeObject) {
          let divT = document.createElement("div");
          divT.setAttribute("class", "vidoeDjango");
          let anc = document.createElement("a");
          anc.setAttribute(
            "href",
            "/videos/" + responeObject[i].url_64encoding
          );
          let imgs = document.createElement("img");
          imgs.src = responeObject[i].thumbnail;
          imgs.style.width = "330px";
          imgs.style.height = "200px";
          anc.appendChild(imgs);
          divT.appendChild(anc);
          for (let j = 0; j < 4; j++) {
            let h5 = document.createElement("h5");
            if (j == 0) {
              h5.innerHTML = responeObject[i].captions;
              h5.setAttribute("id", "pad");
            }
            if (j == 1) {
              h5.innerHTML = responeObject[i].username;
            }
            if (j == 2) {
              h5.innerHTML = responeObject[i].date;
            }
            if (j == 3) {
              h5.innerHTML = "Event Name :" +responeObject[i].EventName;
            }
            divT.appendChild(h5);
          }
          gridvd.appendChild(divT);
        }
      },
      error: function (error) {},
    });
  }
}
