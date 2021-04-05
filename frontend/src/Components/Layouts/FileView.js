import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";

const useStyles = makeStyles((theme) => ({
  root: {
    width: "70%",
    margin: "0 auto",
    display: "flex",
    justifyContent: "space-around",
  },
  details: {
    display: "flex",
    flexDirection: "column",
  },
  content: {
    flex: "0 auto",
  },
  cover: {
    width: 200,
  },
}));

function FileView() {
  const classes = useStyles();
  return (
    <div>
      <Card className={classes.root}>
        <label>1.</label>
        <div className={classes.details}>
          <CardContent className={classes.content}>
            <Typography component="h5" variant="h5">
              Live From Space
            </Typography>
            <Typography variant="subtitle1" color="textSecondary">
              Mac Miller
            </Typography>
          </CardContent>
        </div>
        <CardMedia
          className={classes.cover}
          component="video"
          height="140"
          image="http://127.0.0.1:8000/media/videos/21/Iron_Man_Vs_Thanos_-_Fight_Scene_-_Avengers_Infinity_War_2018_Movie_CLIP_4K_UL_8wygF64.mp4"
        />
        <a href="#">View File</a>
      </Card>
      <br />
      <Card className={classes.root}>
        <label>2</label>
        <div className={classes.details}>
          <CardContent className={classes.content}>
            <Typography component="h5" variant="h5">
              Live From Space
            </Typography>
            <Typography variant="subtitle1" color="textSecondary">
              Mac Miller
            </Typography>
          </CardContent>
        </div>
        <CardMedia
          className={classes.cover}
          component="video"
          height="140"
          image="http://localhost:8000/media/videos/21/file_example_MOV_1920_2_2MB_GR2NARO.mov"
        />
        <a href="#">View File</a>
      </Card>
    </div>
  );
}

// src="http://localhost:8000/media/videos/21/file_example_MOV_1920_2_2MB_GR2NARO.mov"
// src="http://127.0.0.1:8000/media/videos/21/Iron_Man_Vs_Thanos_-_Fight_Scene_-_Avengers_Infinity_War_2018_Movie_CLIP_4K_UL_8wygF64.mp4"
export default FileView;
