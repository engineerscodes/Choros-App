import React from "react";
import { Button, TextField } from "@material-ui/core";
import { CloudUpload } from "@material-ui/icons";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  root: {
    // display: "flex",
    // flexDirection: "column",
    // alignItems: "center",
    // display: "flex",
    // justifyContent: "center",
    width: "20%",
    margin: "0 auto",
  },
  button: {
    margin: theme.spacing(5),
  },
}));

function FileUpload() {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <h2>
        <a href="/upload/videos/">GO TO GALLERY</a>
      </h2>
      <div></div>
      <br />
      <div>
        <form>
          <input type="file" name="" id="" />
          <Button
            type="file"
            onClick={() => console.log("uploaded")}
            variant="contained"
            color="primary"
            className={classes.button}
            startIcon={<CloudUpload />}
          >
            Upload
          </Button>
        </form>
      </div>
    </div>
  );
}

export default FileUpload;
