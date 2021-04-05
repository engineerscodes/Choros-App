import React from "react";
import { Tabs, Tab, Box } from "@material-ui/core";
import FileUpload from "../Layouts/FileUpload";
import MarksGiven from "../Layouts/MarksGiven";
import FileView from "../Layouts/FileView";
// import SigninForm from "../Forms/SigninForm";
// import Typography from "@material-ui/core/Typography";
// import Link from "@material-ui/core/Link";

function Toolbar() {
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
        // variant="fullWidth"
        centered
      >
        <Tab label="Upload Video" />
        <Tab label="Gallery" />
        <Tab label="Reviewed Videos" />
      </Tabs>

      <TabPanel value={value} index={0}>
        <FileUpload />
      </TabPanel>
      <TabPanel value={value} index={1}>
        <FileView />
      </TabPanel>
      <TabPanel value={value} index={2}>
        <MarksGiven />
      </TabPanel>
    </div>
  );
}

export default Toolbar;
