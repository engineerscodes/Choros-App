import React from "react";
import {
  Button,
  TextField,
  Grid,
  Paper,
  Avatar,
  Typography,
} from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import EmailOutlinedIcon from "@material-ui/icons/EmailOutlined";

const useStyles = makeStyles((theme) => ({
  paper: {
    padding: 25,
    width: 400,
    height: "45vh",
    margin: "0 auto",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: "100%",
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

function ForgotPasswordForm() {
  const classes = useStyles();

  return (
    <Grid>
      <Paper elevation={10} className={classes.paper}>
        <Avatar className={classes.avatar}>
          <EmailOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Reset password
        </Typography>
        <form>
          <TextField
            variant="outlined"
            margin="normal"
            required
            id="email"
            label="Email Address"
            name="email"
            placeholder="Enter Email Address"
            fullWidth
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
          >
            Reset password
          </Button>
        </form>
      </Paper>
    </Grid>
  );
}

export default ForgotPasswordForm;
