import * as React from "react";
import { Link } from "react-router-dom";


import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Container from "@mui/material/Container";
import Stack from "@mui/material/Stack";


const Shell = () => {
  const registerLink = "/register";
  const loginLink = "/login";

  return (
    <>
      <Box component='main'>
        <Container maxWidth="sm">
          <Stack
            sx={{ pt: 4 }}
            direction="row"
            spacing={2}
            justifyContent="center"
          >
            <Link to={loginLink} underline="none">
              <Button variant="contained">Sign In</Button>
            </Link>
            <Link to={registerLink}>
              <Button variant="outlined">Register</Button>
            </Link>
          </Stack>
        </Container>
      </Box>
    </>
  );
}

export default Shell;