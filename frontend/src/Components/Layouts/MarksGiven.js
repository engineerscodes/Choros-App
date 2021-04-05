import React from "react";

function MarksGiven() {
  return (
    <div>
      <video controls="controls" width="500px" height="500px">
        <source src="{{i.video.url}}" type="video/mp4" />
      </video>

      <h1>captions</h1>
      <h3>by</h3>
      <h3>ID</h3>
      <h3>
        <a href="/upload/videos/{{i.url_64encoding}}">LINK</a>
      </h3>
    </div>
  );
}

export default MarksGiven;
