// import "./style.css";
import React from "react";
import * as Yup from "yup";
import { makeStyles } from "@material-ui/core/styles";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import {
  Grid,
  Avatar,
  Typography,
  TextField,
  Button,
  Link,
} from "@material-ui/core";
import { Formik, Form, Field, ErrorMessage } from "formik";

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: "90%",
    marginTop: theme.spacing(3),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

const onSubmit = (values, { setSubmitting }) => {
  setTimeout(() => {
    alert(JSON.stringify(values, null, 2));
    // perform async operations
    setSubmitting(false);
  }, 200);
};

const validationSchema = Yup.object({
  // email: Yup.string().email("Invalid email address").required("Required"),
  email: Yup.string()
    .matches(/^[\w.+-]+@vitap\.ac\.in$/, "Enter university email address")
    .required("Required"),
  password: Yup.string()
    .min(8, "Password must atleast 8 characters")
    .required("Required"),
});

function SigninForm({ handleChange }) {
  const classes = useStyles();

  return (
    <div className={classes.paper}>
      <Avatar className={classes.avatar}>
        <LockOutlinedIcon />
      </Avatar>
      <Typography component="h1" variant="h5">
        Sign in
      </Typography>

      <Formik
        initialValues={{ email: "", password: "" }}
        validationSchema={validationSchema}
        onSubmit={onSubmit}
      >
        <Form className={classes.form}>
          <Field
            name="email"
            as={TextField}
            type="email"
            variant="outlined"
            margin="normal"
            label="Email Address"
            fullWidth
          />
          <ErrorMessage
            name="email"
            render={(msg) => <span style={{ color: "red" }}>{msg}</span>}
          />

          <Field
            name="password"
            as={TextField}
            variant="outlined"
            margin="normal"
            type="password"
            label="Password"
            fullWidth
          />
          <ErrorMessage
            name="password"
            render={(msg) => <span style={{ color: "red" }}>{msg}</span>}
          />

          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
          >
            Sign In
          </Button>
          <Grid container>
            <Grid item xs>
              <Link href="#" variant="body2">
                {"Forgot password?"}
              </Link>
            </Grid>
            <Grid item>
              <Link
                href="#"
                onClick={() => handleChange("event", 1)}
                variant="body2"
              >
                {"Don't have an account? Sign Up"}
              </Link>
            </Grid>
          </Grid>
        </Form>
      </Formik>
    </div>
  );
}

export default SigninForm;
