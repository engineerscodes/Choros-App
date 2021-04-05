import React from "react";
import * as Yup from "yup";
import {
  Grid,
  Button,
  Typography,
  Avatar,
  Link,
  TextField,
} from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import { Formik, Form, Field, ErrorMessage } from "formik";

const validationSchema = Yup.object({
  firstName: Yup.string()
    .max(10, "First name must 10 characters or less")
    .required("Required"),

  lastName: Yup.string()
    .max(15, "First name must 15 characters or less")
    .required("Required"),

  password: Yup.string()
    .min(8, "Password must atleast 8 characters")
    .required("Required"),

  // email: Yup.string().email("Invalid email address").required("Required"),
  email: Yup.string()
    .matches(/^[\w.+-]+@vitap\.ac\.in$/, "Enter university email address")
    .required("Required"),
});

const onSubmit = (values, { setSubmitting }) => {
  setTimeout(() => {
    alert(JSON.stringify(values, null, 2));
    // perform async operations
    setSubmitting(false);
  }, 200);
};

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

function SignupForm({ handleChange }) {
  const classes = useStyles();

  return (
    <div className={classes.paper}>
      <Avatar className={classes.avatar}>
        <LockOutlinedIcon />
      </Avatar>
      <Typography component="h1" variant="h5">
        Sign up
      </Typography>
      <Formik
        initialValues={{ firstName: "", lastName: "", email: "", password: "" }}
        validationSchema={validationSchema}
        onSubmit={onSubmit}
      >
        <Form className={classes.form}>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={6}>
              <Field
                as={TextField}
                name="firstName"
                variant="outlined"
                required
                fullWidth
                label="First Name"
              />
              <ErrorMessage
                name="firstName"
                render={(msg) => <span style={{ color: "red" }}>{msg}</span>}
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <Field
                as={TextField}
                name="lastName"
                variant="outlined"
                required
                fullWidth
                label="Last Name"
              />
              <ErrorMessage
                name="lastName"
                render={(msg) => <span style={{ color: "red" }}>{msg}</span>}
              />
            </Grid>
            <Grid item xs={12}>
              <Field
                as={TextField}
                name="email"
                variant="outlined"
                required
                fullWidth
                label="Email Address"
              />
              <ErrorMessage
                name="email"
                render={(msg) => <span style={{ color: "red" }}>{msg}</span>}
              />
            </Grid>
            <Grid item xs={12}>
              <Field
                as={TextField}
                variant="outlined"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
              />
              <ErrorMessage
                name="password"
                render={(msg) => <span style={{ color: "red" }}>{msg}</span>}
              />
            </Grid>
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
          >
            Sign Up
          </Button>
          <Grid item>
            <Link
              href="#"
              onClick={() => handleChange("event", 0)}
              variant="body2"
            >
              Already have an account? Sign in
            </Link>
          </Grid>
        </Form>
      </Formik>
    </div>
  );
}

export default SignupForm;
