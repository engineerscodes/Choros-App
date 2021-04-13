let gridvd = document.getElementsByClassName("vidoeGrid")[0];
let count = 0;
function getVideos(){
$.ajax({
  type: "GET",
  url: "getcontent/",
  data: {
    vdreq: ++count
  },
  success: function (respone) {
    let responeObject = respone.data;
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
      for (let j = 0; j < 3; j++) {
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
        divT.appendChild(h5);
      }
      gridvd.appendChild(divT);
    }
  },
  error: function (error) {},
});
}

 setTimeout(getVideos, 1000);


window.addEventListener('scroll',()=>{
     const { scrollTop, clientHeight, scrollHeight }=document.documentElement;
    
   if (scrollTop +clientHeight >= scrollHeight-1) {
      getVideos();
   }

});