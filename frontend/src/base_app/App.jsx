import React from 'react';
import { Outlet, useLocation } from 'react-router-dom';
import { Box } from "@mui/material";
import Shell from './Shell';

const App = () => {
  const location = useLocation();

  let children = <Outlet />
  if (location.pathname === "/") {
    children = <Shell />;
  }

  return <Box>{children}</Box>
}

export default App;