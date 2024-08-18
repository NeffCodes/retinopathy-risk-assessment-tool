import React from 'react';
import { Outlet, useLocation } from 'react-router-dom';
import { Box } from "@mui/material";
import Shell from './Shell';
import Toolbar from "@mui/material/Toolbar";
import AppBar from "@mui/material/AppBar";
import Container from "@mui/material/Container";

const App = () => {
  const location = useLocation();

  let children = <Outlet />
  if (location.pathname === "/") {
    children = <Shell />;
  }

  return (<>
    <AppBar position="relative">
      <Toolbar>Diabetic Retinopathy</Toolbar>
    </AppBar>
    <Container maxWidth="lg" sx={{outline:'1px solid red'}}>
      <Box>{children}</Box>
    </Container>
  </>)
}

export default App;