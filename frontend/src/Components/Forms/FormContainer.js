import React from "react";
import { Tabs, Tab, Box } from "@material-ui/core";
import SigninForm from "./SigninForm";
import SignupForm from "./SignupForm";
import Typography from "@material-ui/core/Typography";
import Link from "@material-ui/core/Link";

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {"Copyright © "}
      <Link color="inherit" href="#">
        VIT-AP Dance Club
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

function FormContainer() {
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  function TabPanel(props) {
    const { children, value, index } = props;
    return (
      <div role="tabpanel" hidden={value !== index}>
        {value === index && <Box>{children}</Box>}
      </div>
    );
  }

  return (
    <div>
      <Tabs
        value={value}
        indicatorColor="primary"
        textColor="primary"
        onChange={handleChange}
        variant="fullWidth"
      >
        <Tab label="Sign in" />
        <Tab label="Sign up" />
      </Tabs>

      <TabPanel value={value} index={0}>
        <SigninForm handleChange={handleChange} />
      </TabPanel>
      <TabPanel value={value} index={1}>
        <SignupForm handleChange={handleChange} />
      </TabPanel>
      <br />
      <br />
      <Copyright />
    </div>
  );
}

export default FormContainer;
