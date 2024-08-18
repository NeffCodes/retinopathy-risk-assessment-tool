import * as React from "react";
import { Link } from "react-router-dom";

import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Container from "@mui/material/Container";
import Stack from "@mui/material/Stack";
import Toolbar from "@mui/material/Toolbar";

const Shell = () => {
  const registerLink = "/register";
  const loginLink = "/login";

  return (
    <>
      <AppBar position="relative">
        <Toolbar />
      </AppBar>
      <Container maxWidth="lg" sx={{outline: '1px solid red'}}>
        <Box component='main'>
          <Container maxWidth="sm">
            <Stack
              sx={{ pt: 4 }}
              direction="row"
              spacing={2}
              justifyContent="center"
            >

              <Link to={registerLink}>
                <Button variant="contained">Register</Button>
              </Link>
              <Link to={loginLink} underline="none">
                <Button variant="outlined">Sign In</Button>
              </Link>
            </Stack>
          </Container>
        </Box>
      </Container>
    </>
  );
}

export default Shell;